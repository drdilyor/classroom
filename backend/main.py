import asyncio
from typing import List

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

import models
from models import *
import schemas as s


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

asyncio.create_task(models.init())


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
