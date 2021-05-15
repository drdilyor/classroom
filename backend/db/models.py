from fastapi import FastAPI
from fastapi_admin.models import AbstractUser
from tortoise.models import Model
from tortoise.fields import *
from tortoise import Tortoise, run_async

class ID:
    id = IntField(pk=True)

    def __repr__(self):
        return f'<{self.__class__.__name___} {self.id}>'


class Language(ID, Model):
    name = CharField(20)

    def __str__(self):
        return self.name


class Course(ID, Model):
    title = CharField(200)
    description = TextField()
    image_link = CharField(200)
    language = ForeignKeyField('models.Language', related_name='courses')
    author = CharField(80)
    estimated_time = IntField()

    course_parts: ReverseRelation['CoursePart']

    def __str__(self):
        return self.title


class CoursePart(ID, Model):
    title = CharField(200)
    description = TextField()
    course = ForeignKeyField('models.Course', index=True, related_name='course_parts')

    def __str__(self):
        return f'{self.course_id}: {self.title}'


class Lesson(ID, Model):
    title = CharField(max_length=200)
    video = CharField(50)
    content = TextField()
    course_part = ForeignKeyField('models.CoursePart', index=True, related_name='lessons')

    def __str__(self):
        return self.title


class CourseMember(ID, Model):
    user_sub = CharField(80, index=True)
    course = ForeignKeyField('models.Course', index=True, related_name='members')
    created_at = DatetimeField(auto_now_add=True)

    def __repr__(self):
        return f'<CourseMember {self.course_id} {self.user_sub}>'


class LessonViewed(ID, Model):
    user_sub = CharField(80, index=True)
    lesson = ForeignKeyField('models.Lesson', index=True, related_name='viewed_lessons')

    def __repr__(self):
        return f'<LessonViewed {self.lesson} {self.user_sub}>'


class AdminUser(AbstractUser):
    pass


async def init():
    Language.UZBEK   = await Language.get_or_create(name='Uzbek')
    Language.ENGLISH = await Language.get_or_create(name='English')


__all__ = [
    'Course',
    'CoursePart',
    'Lesson',
    'CourseMember',
    'LessonViewed',
]
