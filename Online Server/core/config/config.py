class _keys_Convex():
    toConv='toConv'
    convModelPath='convModelPath'
    maxPoints='maxPoints'

class _keys_Voxel():
    voxelModelPath='voxelModelPath'
    cubeShape= 'cubeShape'

class _keys_Scripts():
    convexScripts= 'convexScripts'
    voxelScripts= 'voxelScripts'

class _keys_Data():
    pcdDir='pcdDir'
    voxelsDir='voxelsDir'

keys_voxel = _keys_Voxel()

keys_convex = _keys_Convex()

keys_scripts = _keys_Scripts()

keys_data = _keys_Data()

config_ConvexModel = {
    keys_convex.toConv: False
    ,keys_convex.convModelPath: r"C:\Users\Yan\Desktop\Robotic hand\Scripts\Online Server\core\AI\pytorch_models\ConvexModelsVersions\V_9.8.23\convhull_trained_model.pt"
    ,keys_convex.maxPoints: 2000

}

config_VoxelModel = {
    keys_voxel.voxelModelPath: r"C:\Users\Yan\Desktop\Robotic hand\Scripts\Online Server\core\AI\pytorch_models\VoxelModelsVersions\V_5.8\voxelModel.pt"
    ,keys_voxel.cubeShape: (25,25,25)
}


config_Scripts = {
    "convexScripts": r"C:\Users\Yan\Desktop\Robotic hand\Scripts\ConvexHull"
    ,"voxelScripts" : r"C:\Users\Yan\Desktop\Robotic hand\Scripts\Voxelization"

}

config_Data = {
    keys_data.voxelsDir: r"C:\Users\Yan\Desktop\Robotic hand\Scripts\Online Server\core\public\data\voxels"
    ,keys_data.pcdDir: r"C:\Users\Yan\Desktop\Robotic hand\Scripts\Online Server\core\public\data\pcds"

}


