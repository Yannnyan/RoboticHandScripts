
from ..controllers.server_controller_voxelModel import voxelController

def initRoutes(app):
    @app.get("/voxelmodel")
    async def root(msg: str):
        pass

    @app.post("/voxelmodel")
    async def root(msg: str):
        return {"message": voxelController.HandleData(msg=msg)}



