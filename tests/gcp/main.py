from agraffe import Agraffe, Service

from app import app


entry_point = Agraffe.entry_point(app, Service.google_cloud_functions)
