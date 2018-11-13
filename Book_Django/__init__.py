import pymysql
pymysql.install_as_MySQLdb()

from Book_Django.celery import app as celery_app

__all__ = ['celery_app']