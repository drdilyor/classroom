from tortoise.models import Model
from tortoise.fields import *
from tortoise import Tortoise

class Course(Model):
    title = CharField(200)
    description = TextField()
    image_link = CharField(200)

    def __str__(self):
        return self.title


class CoursePart(Model):
    title = CharField(200)
    description = TextField()
    course = ForeignKeyField('models.Course', index=True)


class Lesson(Model):
    title = CharField(max_length=200)
    video = CharField(50)
    content = TextField()
    course_part = ForeignKeyField('models.CoursePart', index=True)


class CourseMember(Model):
    user_id = IntField(index=True)
    course = ForeignKeyField('models.Course', index=True)


class LessonViewed(Model):
    user_id = IntField(index=True)
    lesson = ForeignKeyField('models.Lesson', index=True)


async def init():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['models']},
    )
    await Tortoise.generate_schemas()

__all__ = [
    'init',
    'Course',
    'CoursePart',
    'Lesson',
    'CourseMember',
    'LessonViewed',
]
