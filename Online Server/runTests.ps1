# $toRunConvex = $true
$toRunConvex = $false


if ($toRunConvex)
{
    python -m tests.testModels.tests_testModels_testConvexmodel
}
else
{
    python -m tests.testModels.tests_testModels_testVoxelmodel

}