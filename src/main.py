from classes import Link, ArchivoAudio, Recognition, Texto


def main():
    url = input("Ingrese la url del video que quiere utilizar")
    opcion = int(input(("""Indique que quiere hacer: 1)Descargar el audio de un video\n2)Extraer el audio de un video(.wav)
    y dividirlo en partes iguales\n3)Descargar video, extraer audio y pasarlo a archivo Word\n4)Transcribir archivos de audio""")))
    
    
    if opcion == 1:
        link = Link(url)
        link.descargar_audio()
    
    elif opcion == 2:
        audio = ArchivoAudio("Audio.wav")
        audio.division_partes_iguales()
    
    elif opcion == 3:
        link = Link(url)
        link.descargar_audio()
        link.conversion_formato_video_a_audio_wav()




if __name__ == '__main__':
    main()