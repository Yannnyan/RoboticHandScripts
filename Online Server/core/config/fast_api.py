from .env.paths import *
from fastapi import FastAPI
from core.app.routes.server_routes_convexModel import initRoutes as initConvRoutes
from core.app.routes.server_routes_voxelModel import initRoutes as initVoxelRoutes
app = FastAPI()

initConvRoutes(app)
initVoxelRoutes(app)




