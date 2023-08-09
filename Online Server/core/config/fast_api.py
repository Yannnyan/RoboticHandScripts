from .env.paths import *
from fastapi import FastAPI
from core.app.routes.server_routes_convexModel import initRoutes as initConvRoutes
from core.app.routes.server_routes_voxelModel import initRoutes as initVoxelRoutes
from starlette.exceptions import HTTPException
from fastapi.exceptions import RequestValidationError
from .exception_handlers import request_validation_exception_handler, http_exception_handler, unhandled_exception_handler
from .middleware import log_request_middleware

app = FastAPI()

initConvRoutes(app)
initVoxelRoutes(app)

app.middleware("http")(log_request_middleware)
app.add_exception_handler(RequestValidationError, request_validation_exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, unhandled_exception_handler)


