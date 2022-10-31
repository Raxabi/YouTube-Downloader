import os
import platform
from downloader import downloader

# Third-Party modules
from pytube import YouTube

user_link = input("Añade aqui el enlace: ")
video_to_download = YouTube(user_link)
control = 5
while control == 5:
    user_format_video = input("\nQuieres descargar solo audio?: [S]i o [N]o: ").upper()
    match user_format_video:
        case 'S':
            control = 4
            print("Se ha seleccionado [S]i, buscando videos de acuerdo al filtro seleccionado:\n")
            array_stream_elements = video_to_download.streams.filter(only_audio = True)
            for i in array_stream_elements:
                print(i)
        case other:
            print("No se han encontrado coincidencias")

user_download_video = input("\nSeleccione el video en base al identificador 'itag': ")

match platform.system():
    case "Windows":
        os.system("cls")
    case "Linux":
        os.system("clear")

print("----", "Ten en cuenta que tu ruta actual es:", __file__, "----")
user_path = input("Introduce una ruta donde se vaya a guardar el archivo: ")

downloader(user_link, user_download_video, user_path)