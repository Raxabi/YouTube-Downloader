Clear-Host;

$work_dir = ($HOME + "\.downlotube");

New-Item -Path $work_dir -ItemType "directory";

New-Item -Path ($work_dir + "./downlotube_lib/src") -ItemType "directory";

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

Write-Host "El nombre de la variable de entorno sera: 'musica'";

Set-Location -Path ($HOME + "/desktop/");

Write-Host "`nTen en cuenta que tu ruta actual es: " (Get-Location) "`n";

$ruta_musica = Read-Host "Introduce una ruta para descargar tu musica";

$path_environment_variable = [System.Environment]::GetEnvironmentVariable("Path", "User");

if (-not (Test-Path -Path $ruta_musica)) {
    Write-Host "`nLa ruta no existe!`nNo te preocupes, el instalador creara la ruta introducida por ti :D";
    New-Item -Path $ruta_musica -ItemType "directory";
}

$ruta_musica = Resolve-Path $ruta_musica;

Write-Host $ruta_musica;

[System.Environment]::SetEnvironmentVariable("musica", $ruta_musica, "User");
[System.Environment]::SetEnvironmentVariable("Path", ($path_environment_variable += $work_dir), "User");

python -m pip install pytube;