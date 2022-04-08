import os

from agraffe import Agraffe

from app import app


entry_point = Agraffe.entry_point(app, os.environ['AgraffeService'])
