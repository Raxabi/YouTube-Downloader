import os
import platform
from pytube import YouTube

# ! La funcion descargara el video y ordenara segun haya pedido el usuario

def detectedDownload(video_link, itag_selector_video, video_path):
    if os.path.isfile(video_path):
        print("Error, la ruta donde se vaya a guardar la descarga debe de ser una descarga")
    elif os.path.isdir(video_path):
        print("Carpeta valida, la descarga comenzara ahora...")
        finalSelection = video_link.streams.get_by_itag(itag_selector_video)
        video_name = finalSelection.download(video_path)
        finalSelection.download(video_path)
        print("Descarga exitosa!")
        print("Mira en la carpeta elegida si el archivo se encuentra ahi!")
            
    print("Comprobando la descarga del video...")

    # Probamos si el archivo ha sido descargado
    try:
        test_file = os.path.exists(video_name)
        if test_file == True:
            print("Perfecto! tu video se ha descargado \nEl archivo esta descargado en la carpeta indicada, gracias por usar este servicio :D")
    except:
        print("Algo a ido mal, revisa que hayas introducido bien los datos")

### * intrucciones imperativas

#? obtenemos la direccion del video
user_link = input("Añade aqui el enlace: ")
video_to_download = YouTube(user_link)
user_format_video = input("\nQuieres descargar solo audio?: [S]i o [N]o: ")

if "S" in user_format_video or "s" in user_format_video:
    print("Se ha seleccionado [S]i, buscando videos de acuerdo al filtro seleccionado:\n")
    array_stream_elements = video_to_download.streams.filter(only_audio=True)
    for i in array_stream_elements:
        print(i)
elif "N" in user_format_video or "n" in user_format_video:
    print("Se ha seleccionado [N]o, buscando todo tipo de descargas, tanto video como audio")
    for i in video_to_download.streams:
        print(i)
else:
    print("No se ha seleccionado ninguna opcion valida, debe ser S, para si o N para no")
    user_format_video = input("\nQuieres descargar solo audio?: [S]i o [N]o: ")

print("\n")

"""
    * Aqui recogemos la informacion de como se descargara el video
"""

user_download_video = input("Que descarga prefieres? \nSeleccione el video en base al identificador 'itag'")
print("\n")
# * Limpiamos la consola dependiende cual sea nuestro sistema operativo
if platform.system() == "Windows":
    os.system("cls")
elif platform.system() == "Linux": 
    os.system("clear")

print("Actualmente te encuentras en", "\ndeberas introducir una ruta final para tu archivo")
user_path = input("\nintroduce una ruta donde se vaya a guardar el archivo: ")

detectedDownload(video_to_download, user_download_video, user_path)