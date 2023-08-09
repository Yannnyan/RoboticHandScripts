
$timer = [Diagnostics.StopWatch]::StartNew()
$dirname = "./voxels"
$start_count = (ls $dirname | Measure-Object).Count
$last_count = $start_count
$start_date = Get-Date

# $timer.elapsed.totalseconds -lt 10
while ($true)
{    

    Start-Sleep -Seconds 60
    
    $last_count = $count

    $count = (ls $dirname | Measure-Object).Count
    
    $num_new = $count - $start_count
    
    $cur_date = Get-Date
    
    $seconds_passed = (New-TimeSpan -Start $start_date -End $cur_date).TotalSeconds

    $msg_update = ' current Amount of files are: {0}, Number of files Added are: {1}' -f $count, ($count - $last_count)

    $msg_avg = 'On Average there are: {0} new files each minute, Date: {1}' -f (60 * $num_new / $seconds_passed), $cur_date

    echo $msg_update >> query.txt

    echo $msg_avg >> query.txt
}

$timer.stop()








