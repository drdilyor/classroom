from typing import List, Optional

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

class LessonInfo(BaseModel):
    id: int
    title: str
    course_part_id: int
    course_id: int

class CourseDetailed(Course):
    course_parts: List[CoursePart]


class CoursePartDetailed(CoursePart):
    lessons: List[Lesson]

class CourseVeryDetailed(Course):
    course_parts: List[CoursePartDetailed]


