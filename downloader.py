import os
from pytube import YouTube

def downloader(input_url: str, itag_selector: str, download_path: str):
    url = YouTube(input_url)
    if os.path.isfile(download_path):
        print("Error, la ruta donde se vaya a guardar la descarga debe de ser una descarga")
    elif os.path.isdir(download_path):
        print("Carpeta valida, la descarga comenzara ahora...")
        url.streams.get_by_itag(itag_selector).download(download_path)