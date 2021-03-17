import asyncio
from typing import List

from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

import models
from auth import requires_auth, AuthError
from models import *
import schemas as s
from util import abort

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models and admin
asyncio.create_task(models.init(app))


def e404():
    raise HTTPException(404)


@app.get('/')
async def index():
    return {'message': 'Hello world'}


@app.get('/courses', response_model=List[s.Course])  # noqa
async def all_courses():
    return await Course.all()


@app.get('/courses/{course_id}', response_model=s.CourseDetailed)
async def get_course(course_id: int):
    qs = Course.filter(id=course_id).prefetch_related('course_parts')
    c: Course = await qs.get_or_none() or e404()
    return {
        **c.__dict__,
        'course_parts': await c.course_parts,  # noqa
    }

@app.get('/courses/{course_id}/is-enrolled')
async def is_user_enrolled(course_id: int, payload=Depends(requires_auth())):
    return {
        'is_enrolled': (await CourseMember.get_or_none(
            course_id=course_id,
            user_sub=payload['sub']
        )) is not None
    }


@app.get('/enrolled-courses', response_model=List[s.Course])  # noqa
async def get_enrolled_courses(payload=Depends(requires_auth())):
    qs = await CourseMember.filter(user_sub=payload['sub']).prefetch_related('course')
    return [i.course for i in qs]


@app.put('/courses/{course_id}/enroll')
async def enroll_course(course_id: int, payload=Depends(requires_auth())):
    c = await Course.get_or_none(id=course_id) or e404()
    _cm, created = await CourseMember.get_or_create(user_sub=payload['sub'], course=c)
    return {'created': created}


# Soon this will change
app.get('/enrolled-courses/{course_id}', response_model=s.CourseDetailed)(get_course)


@app.get('/enrolled-course-parts/{id}', response_model=s.CoursePartDetail)
async def get_detailed_course_part(id: int, payload=Depends(requires_auth())):  # noqa
    """Returns lessons as well"""
    cp = await CoursePart.get_or_none(id=id).prefetch_related('lessons') or e404()
    cm = await CourseMember.get_or_none(
        user_sub=payload['sub'],
        course_id=cp.course_id,
    ) or e404()
    print(payload['sub'])
    lessons = await cp.lessons
    for L in lessons:
        L.is_viewed = await LessonViewed.get_or_none(lesson=L, user_sub=payload['sub']) is not None
    return s.CoursePartDetail(**cp.__dict__, lessons=lessons)


@app.put('/lessons/{lesson_id}/viewed')
async def view_lesson(lesson_id: int, payload=Depends(requires_auth())):
    lesson = await Lesson.get_or_none(id=lesson_id) or abort(404)
    _lv, created = await LessonViewed.get_or_create(user_sub=payload['sub'], lesson=lesson)
    return {'created': created}


@app.get('/headers')
async def headers(payload=Depends(requires_auth())):
    return {'payload': payload}


@app.exception_handler(AuthError)
def auth_error(_request: Request, exc: AuthError):
    return JSONResponse(
        status_code=exc.status_code,
        content={'detail': exc.error}
    )
