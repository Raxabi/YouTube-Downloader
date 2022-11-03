import os
from pytube import YouTube, helpers

proxy_socket = "192.168.5.254:3128"

proxy_configuration = {
    "http": proxy_socket,
    "https": proxy_socket
}

def downloader(input_url: str, itag_selector: str, download_path: str):
    url = YouTube(input_url)
    if os.path.isfile(download_path):
        print("Error, la ruta donde se vaya a guardar la descarga debe de ser una carpeta")
    elif os.path.isdir(download_path):
        print(f"La carpeta '{download_path}' es una carpeta valida, estamos trabajando en la descarga...\n\nMuchas gracias por usar downlotube")
        url.streams.get_by_itag(itag_selector).download(download_path)