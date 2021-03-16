from fastapi import FastAPI
from fastapi_admin.factory import app as admin_app
from fastapi_admin.models import AbstractUser
from fastapi_admin.site import Site
from tortoise.models import Model
from tortoise.fields import *
from tortoise import Tortoise

class Course(Model):
    id = IntField(pk=True)
    title = CharField(200)
    description = TextField()
    image_link = CharField(200)

    def __str__(self):
        return self.title


class CoursePart(Model):
    id = IntField(pk=True)
    title = CharField(200)
    description = TextField()
    course = ForeignKeyField('models.Course', index=True, related_name='course_parts')


class Lesson(Model):
    id = IntField(pk=True)
    title = CharField(max_length=200)
    video = CharField(50)
    content = TextField()
    course_part = ForeignKeyField('models.CoursePart', index=True, related_name='lessons')


class CourseMember(Model):
    id = IntField(pk=True)
    user_sub = CharField(80, index=True)
    course = ForeignKeyField('models.Course', index=True, related_name='members')


class LessonViewed(Model):
    id = IntField(pk=True)
    user_sub = CharField(80, index=True)
    lesson = ForeignKeyField('models.Lesson', index=True, related_name='viewed_lessons')


class AdminUser(AbstractUser):
    pass


async def init(app: FastAPI):
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['models']},
    )
    await Tortoise.generate_schemas()

    #register_tortoise(app, config=TORTOISE_ORM, generate_schemas=True)
    app.mount('/admin', admin_app)

    await admin_app.init(
        admin_secret="test",
        site=Site(
            name="FastAPI-Admin DEMO",
            login_footer="FASTAPI ADMIN - FastAPI Admin Dashboard",
            login_description="FastAPI Admin Dashboard",
            locale="en-US",
            locale_switcher=True,
            theme_switcher=True,
        ),
    )


__all__ = [
    'init',
    'Course',
    'CoursePart',
    'Lesson',
    'CourseMember',
    'LessonViewed',
]
