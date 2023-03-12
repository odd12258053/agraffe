from agraffe import Agraffe, Service

from fastapi_app import app, failed_app


entry_point = Agraffe.entry_point(app, Service.google_cloud_functions)


failed_entry_point = Agraffe.entry_point(failed_app, Service.google_cloud_functions)
