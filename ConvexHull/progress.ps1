

$total_rows = 15840
$size_per_row_bytes = 102862.802706
$estimated_file_size = ($total_rows * $size_per_row_bytes)
$file_path = "C:\Users\Yan\Desktop\Robotic hand\data_logs\8.8.2023\pointsAlgo_noconv\fixedPCDPoints.csv"
$log_file = "logger_better.txt"

while($true)
{
    $cur_size = (Get-Item $file_path).Length
    $progress = $cur_size / $estimated_file_size
    $date_now = Get-Date 
    echo "$date_now Progress made: $progress" >> $log_file
    Start-Sleep 60

}




