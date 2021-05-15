import os

from fastapi import FastAPI
from fastapi_admin.factory import app as admin_app
from fastapi_admin.site import Site
from tortoise import Tortoise

from db import models


TORTOISE_ORM = {
    'connections': {'default': os.environ.get('DATABASE', 'postgres://postgres:postgres@localhost:5432/classroom')},
    'apps': {
        'models': {
            'models': ['db.models', 'aerich.models'],
            'default_connection': 'default',
        }
    }
}

async def init_tortoise():
    await Tortoise.init(config=TORTOISE_ORM)
    await models.init()


async def init_admin(app: FastAPI):
    print('admin init')
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
