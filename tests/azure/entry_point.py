from agraffe import Agraffe, Service

from app import app

main = Agraffe.entry_point(app, Service.azure_functions)
