import asyncio
import logging
import os
from typing import List

from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

import db
from auth import requires_auth, AuthError
from db.models import *
import schemas as s
from util import abort

logging.basicConfig(level=getattr(
    logging,
    os.environ.get('LOG_LEVEL', 'DEBUG').upper(),
    logging.DEBUG,
))

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
asyncio.create_task(db.init(app))


def e404():
    raise HTTPException(404)


@app.get('/')
async def index():
    return {'message': 'Hello world'}


@app.get('/courses', response_model=List[s.Course])  # noqa
async def all_courses():
    return [
        {
            **c.__dict__,
            'language': c.language.name,
            'author': c.author.name,
        } for c in await Course.all().select_related('language', 'author')
    ]


@app.get('/courses/{course_id}', response_model=s.CourseDetailed)
async def get_course(course_id: int):
    qs = Course.filter(id=course_id).prefetch_related('course_parts').select_related('language', 'author')
    c: Course = await qs.get_or_none() or e404()
    return {
        **c.__dict__,
        'language': c.language.name,
        'course_parts': await c.course_parts,  # noqa
        'author': c.author.name,
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
    qs = await CourseMember.filter(user_sub=payload['sub']).select_related('course__language', 'course__author')
    return [s.Course(**i.course.__dict__,
                     language=i.course.language.name,
                     author=i.course.author.name) for i in qs]


@app.put('/courses/{course_id}/enroll')
async def enroll_course(course_id: int, payload=Depends(requires_auth())):
    c = await Course.get_or_none(id=course_id) or e404()
    _cm, created = await CourseMember.get_or_create(user_sub=payload['sub'], course=c)
    return {'created': created}


@app.get('/enrolled-courses/{id}', response_model=s.CourseVeryDetailed)
async def enrolled_course(id: int, payload=Depends(requires_auth())):  # noqa
    print('start')
    # check if user is enrolled
    member = await CourseMember.get_or_none(
        user_sub=payload['sub'],
        course_id=id,
    ) or abort(403)

    query = Course.filter(id=id).prefetch_related('course_parts__lessons').select_related('language', 'author')

    course: Course = await query.get_or_none() or e404()
    parts = await course.course_parts

    course_dict = {**course.__dict__}
    course_dict['language'] = course.language.name
    course_dict['author'] = course.author.name
    # 'cause pydantic doesn't await on Course.lessons
    course_dict['course_parts'] = [await format_course_part(i, payload['sub']) for i in parts]

    return course_dict


async def format_course_part(part, sub):
    part_dict = {**part.__dict__}
    part_dict['lessons'] = []

    for L in await part.lessons:  # noqa
        L.is_viewed = await LessonViewed.get_or_none(lesson=L, user_sub=sub) is not None
        part_dict['lessons'].append(L)
    return part_dict


@app.get('/lessons/{lesson_id}', response_model=s.LessonInfo)
async def get_lesson_info(
    lesson_id: int,
    payload=Depends(requires_auth()),
):
    lesson = await Lesson.get_or_none(id=lesson_id) or e404()
    return {
        **lesson.__dict__,
        'course_id': (await lesson.course_part).course_id,
    }


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
