# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pyramid.config import Configurator
import os


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    settings['sqlalchemy.url'] = os.environ['DATABASE_URL']
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('.models')
    config.include('.routes')
    config.add_static_view(name='static', path='myproject_sql:static')
    config.scan()
    return config.make_wsgi_app()
