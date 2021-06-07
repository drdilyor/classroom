from typing import List, Optional

from pydantic import BaseModel as PydanticBaseModel, validator
from tortoise.fields.relational import ReverseRelation


class BaseModel(PydanticBaseModel):
    class Config:
        orm_mode = True
    
    @validator('*', pre=True)
    def reverse_relation_to_list(cls, value, **kwargs):
        if isinstance(value, ReverseRelation):
            return list(value)
        return value

class Author(BaseModel):
    name: str

class Course(BaseModel):
    id: int
    title: str
    description: str
    image_link: str
    language: str
    author: Author
    estimated_time: int

    @validator('language', pre=True)
    def get_name(cls, v):
        try:
            return v.name if not isinstance(v, str) else v
        except AttributeError as e:
            raise ValueError from e

class CoursePart(BaseModel):
    id: int
    title: str
    description: str
    course_id: int

class Lesson(BaseModel):
    id: int
    title: str
    video: str
    content: str
    course_part_id: int
    is_viewed: bool  # This will be set in a controller

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
