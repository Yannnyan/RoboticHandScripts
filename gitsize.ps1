

$filename = '.gitignore'

$ignore_files = (type $filename).Split("\n") 

echo $ignore_files

$files = ls -r $filename

$total_size = 0

$amount_files = 0

foreach ($file in $files){
    if ($ignore_files -Contains $file -Or $ignore_files -Contains [IO.Path]::GetExtension($line))
    {
        $amount_files++
        $total_size += (Get-Item $file).Length
    }
}

echo Total size: $total_size
echo Total files: $amount_files
