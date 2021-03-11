from typing import List

from pydantic import BaseModel


class Course(BaseModel):
    id: int
    title: str
    description: str
    image_link: str

    class Config:
        orm_mode = True


class CoursePart(BaseModel):
    id: int
    title: str
    description: str
    course_id: int

    class Config:
        orm_mode = True


class Lesson(BaseModel):
    id: int
    title: str
    video: str
    content: str
    course_part_id: int
    is_viewed: bool  # This will be set in a controller

    class Config:
        orm_mode = True


class CourseDetailed(Course):
    course_parts: List[CoursePart]


class CoursePartDetail(CoursePart):
    lessons: List[Lesson]

