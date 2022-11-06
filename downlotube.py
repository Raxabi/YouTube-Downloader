import os
import platform
from downlotube_lib.src.downloader import downloader

# Third-Party modules
from pytube import YouTube

exit_control = True
download_path = os.environ.get("musica")

while exit_control:
    user_url = input("Añade aqui el enlace: ")

    video_to_download = YouTube(user_url)

    input_control = True # For catch the input

    while input_control:
        user_format_video = input("\nQuieres descargar solo audio?: [S]i o [N]o: ").upper()
        match user_format_video:
            case 'S':
                input_control = False
                print("Se ha seleccionado '[S]i', buscando videos de acuerdo al filtro seleccionado:\n")
                array_stream_elements = video_to_download.streams.filter(only_audio = True)
                for i in array_stream_elements:
                    print(i)
            case other:
                print("No se han encontrado coincidencias")

    user_itag_selection = input("\nSeleccione el video en base al identificador 'itag': ")

    match platform.system():
        case "Windows":
            os.system("cls")
        case "Linux":
            os.system("clear")

    downloader(user_url, user_itag_selection, download_path)

    print("Descarga completada")

    continue_program_control = True

    while continue_program_control:
        user_continue_program = input("\nQuieres descargar otro archivo?: [S]i o [N]o: ").upper()
        match user_continue_program:
            case "S":
                continue_program_control = False
            case "N":
                continue_program_control = False
                exit_control = False
            case other:
                print(f"No se encontraron opciones validas, use '[S]i o [N]o' en lugar de '{user_continue_program}'")
