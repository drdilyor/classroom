import os

from fastapi import FastAPI
from fastapi_admin.factory import app as admin_app
from fastapi_admin.models import AbstractUser
from fastapi_admin.site import Site
from tortoise.models import Model
from tortoise.fields import *
from tortoise import Tortoise, run_async

class ID:
    id = IntField(pk=True)

    def __repr__(self):
        return f'<{self.__class__.__name___} {self.id}>'

class Course(ID, Model):
    title = CharField(200)
    description = TextField()
    image_link = CharField(200)

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


async def init_tortoise():
    db_url = os.environ.get('DATABASE', 'sqlite://db.sqlite3')
    print(f'{db_url=}')
    await Tortoise.init(
        db_url=db_url,
        modules={'models': ['models']},
    )
    await Tortoise.generate_schemas()


async def init_admin(app: FastAPI):
    app.mount('/admin', admin_app)

    await admin_app.init(
        admin_secret="test",
        site=Site(
            name="Classroom",
            login_footer="Classroom - a simple E-Learning platform",
            login_description="Classroom admin",
            locale="en-US",
            theme_switcher=True,
            footer='Classroom - a simple E-Learning platform<br>Fork me on '
                   '<a href="https://github.com/drdilyor/classroom" target="_blank">GitHub</a>'
        ),
    )

async def init(app: FastAPI):
    await init_tortoise()
    await init_admin(app)


if __name__ == '__main__':
    run_async(init_tortoise())


__all__ = [
    'init',
    'init_tortoise',
    'init_admin',
    'Course',
    'CoursePart',
    'Lesson',
    'CourseMember',
    'LessonViewed',
]
