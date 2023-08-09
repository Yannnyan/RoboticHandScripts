
from ..controllers.server_controller_voxelModel import voxelController
from ..models.server_models_Data import Data


def initRoutes(app):
    @app.get("/voxelmodel")
    async def root(msg: str):
        pass

    @app.post("/voxelmodel")
    async def root(msg: Data):
        body = msg
        prediction = voxelController.HandleData(msg=body)
        return {"message": prediction}



