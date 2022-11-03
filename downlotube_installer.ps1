Clear-Host;

$work_dir = ($HOME + "\.downlotube");

New-Item -Path $work_dir -ItemType "directory";

New-Item -Path ($work_dir + "./downlotube_lib/src") -ItemType "directory"

Set-Location -Path $work_dir;

$get_downlotube_main = Invoke-WebRequest -Uri "https://raw.githubusercontent.com/Raxabi/YouTube-Downloader/main/downlotube.py";
$get_downlotube_src = Invoke-WebRequest -Uri "https://raw.githubusercontent.com/Raxabi/YouTube-Downloader/main/downlotube_lib/src/downloader.py";

$Core_Stream = [System.IO.StreamWriter]::new($work_dir + "./downlotube.py");
$Lib_Stream = [System.IO.StreamWriter]::new($work_dir + "./downlotube_lib/src/downloader.py");

try {
    $Core_Stream.Write($get_downlotube_main.Content);
    $Lib_Stream.Write($get_downlotube_src.Content);
} finally {
    $Core_Stream.Dispose();
    $Lib_Stream.Dispose();
}

$nombre_variable = Read-Host "Introduce el nombre de la variable de entorno";

Set-Location -Path ($HOME + "/desktop/");

$ruta_actual = Get-Location;
Write-Host "Ten en cuenta que tu ruta actual es: " $ruta_actual;

$ruta_musica = Read-Host "Introduce una ruta para descargar tu musica";

$path_environment_variable = [System.Environment]::GetEnvironmentVariable("Path", "User");

$ruta_musica = Resolve-Path $ruta_musica;
[System.Environment]::SetEnvironmentVariable($nombre_variable, $ruta_musica, "User");
[System.Environment]::SetEnvironmentVariable("Path", ($path_environment_variable += ($work_dir)), "User");

python -m pip install pytube;