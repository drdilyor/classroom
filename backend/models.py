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
    user_id = IntField(index=True)
    course = ForeignKeyField('models.Course', index=True, related_name='members')


class LessonViewed(Model):
    id = IntField(pk=True)
    user_id = IntField(index=True)
    lesson = ForeignKeyField('models.Lesson', index=True, related_name='viewed_lessons')


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
