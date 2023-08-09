from FixPointAmountAlgo import runCSVAlgorithm, runPCDAlgorithm


def pipeline():
    runCSV = False

    output_CSV_path = r"C:\Users\Yan\Desktop\Robotic hand\data_logs\8.8.2023\pointsAlgo_noconv\fixedPCDPoints.csv"
    input_PCDFolder = r"C:\Users\Yan\Desktop\Robotic hand\Scripts\Voxelization\pcds"
    input_CSV_path = ""


    if runCSV:
        runCSVAlgorithm(output_csv_path=output_CSV_path,input_csv_path=input_CSV_path)
    else:
        runPCDAlgorithm(output_csv_path=output_CSV_path, pcd_dir_path=input_PCDFolder, targetsCSVPath=r"C:\Users\Yan\Desktop\PositionBonesRight.csv")

# pipeline()





