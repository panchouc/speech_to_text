from pytube import YouTube
from moviepy.editor import VideoFileClip
from moviepy import AudioFileClip
from docx import Document
import speech_recognition as sr



class Link:
    """Idea es que se guardé un link, y se descargue ya sea el audio o video de este link"""
    
    
    def __init__(self, url : str = "") -> None:
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


class Recognition():
    
    """Pones el nombre del primer archivo y el último. Ejemplo: Si hay Audio1.wav, Audio2.wav y Audio3.wav, pones Recognition(1, 3, Audio).
    El audio tiene que estar en formato .wav
    """
    
    def __init__(self, inicio: int, fin: int, nombre_documento: str = "") -> None:
        self.inicio = inicio
        self.fin = fin
        self.nombre = nombre_documento
        
        
    def reconocimiento(self):
        
        """Convierte todos los archivos de audio que tienen el mismo nombre, pero distinto número, en un word único
        con todo el texto"""
        
        r = sr.Recognizer()
        print("Recuerda que tienes que tener los documentos con el mismo nombre principal y distinto número. Ejemplo: Audio1.wav, Audio2.wav ...")
        
        for i in range(self.inicio, self.fin + 1):
            with sr.AudioFile(f"{self.nombre}{i}.wav") as source:
                audio_text = r.listen(source)
                
                try:
                    text = r.recognize_google(audio_text, language="es-CL")
                    print("Convirtiendo a texto")
                    document = Document()
                    document.add_paragraph(text)
                    document.save(f"Transcripcion{i}.docx")
                    print("La transcripción ha sido realizada con éxito")
                    print("")
                except:
                    print("Intenta de nuevo")
                    
                    
class ArchivoAudio:
    
    "Tiene que ser un archivo de audio junto con su extensión: Ejemplo Cancion.wav"
    
    def __init__(self, nombre_archivo):
        self.nombre = nombre_archivo
        
    def division_partes_iguales(self):
        my_audio = AudioFileClip(my_audio)
        print(f"La duración del audio en segundos es de : {my_audio.duration} segundos")
        print(f"Puedes dividir el audio en {my_audio.duration / 180} partes de 3 minutos cada una")
        cantidad_final = int(my_audio.duration / 180)
        t_1 = 0
        t_2 = 180
        
        for i in range(1, cantidad_final + 1):
            clip_1 = my_audio.subclip(t_1, t_2)
            clip_1.write_audiofile(f"Parte {i}.wav")
            t_1 += 180
            t_2 += 180
            
        print(f"Se logró dividir el audio en partes iguales de forma exitosa\n")
        