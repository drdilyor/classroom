import asyncio
from typing import List

from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

import models
from auth import requires_auth, AuthError
from models import *
import schemas as s


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


@app.get('/headers')
async def headers(payload=Depends(requires_auth())):
    return {'payload': payload}


@app.exception_handler(AuthError)
def auth_error(_request: Request, exc: AuthError):
    return JSONResponse(
        status_code=exc.status_code,
        content={'detail': exc.error}
    )
