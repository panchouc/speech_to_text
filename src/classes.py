from pytube import YouTube
from moviepy.editor import VideoFileClip

class Link:
    """Idea es que se guardé un link, y se descargue ya sea el audio o video de este link"""
    
    
    def __init__(self, url):
        self.url = url
        
    
    def descargar_audio(self):
        """Del respectivo link, va a descargar solamente el audio en un solo archivo"""
        
        yt = YouTube(self.url)
        print("El nombre del video es " + yt.title)
        print(yt.streams.filter(only_audio=True))
        tag = int(input("Ingrese el tag que quiere utilizar: "))
        stream = yt.streams.get_by_itag(tag)
        stream.download()
        print("El audio del video ha sido descargado de forma exitosa\n")
        
    
    def extraccion_formato_video_a_audio_mp3(self):
        """Sirve para extraer audio por ejemplo de un archivo .mp4 y lo escribe uno .mp3"""
        
        nombre_clip = input("Ingresa el nombre del archivo, ejemplo: Cancion1.mp4")
        my_clip = VideoFileClip(r"{nombre}".format(nombre=nombre_clip))
        my_clip.audio.write_audiofile("Audio.mp3")
        print("El audio ha sido separado de su video de forma exitosa\n")
        
    
    def conversion_formato_video_a_audio_wav(self):
        """Extrae el audio de un video y lo escribe en un formato .wav"""
        
        clip = input("Ingresa el nombre del archivo completo, ejemplo: Video1.mp4")
        video = VideoFileClip(clip)
        audio = video.audio
        nombre_archivo = input("Ingrese como quiere escribir el audio y su extension, Ej: Audio.wav :")
        audio.write_audiofile(nombre_archivo)
        print("Se ha extraido el audio de su video de forma exitosa")
        