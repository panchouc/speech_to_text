from classes import Link


from classes import Link, ArchivoAudio, Recognition, Texto

Archivo = Link()
#Archivo.conversion_formato_video_a_audio_wav()
Archivo_2 = ArchivoAudio("Audio.wav")
#Archivo_2.division_partes_iguales()
#Reconocimiento = Recognition(1, 2, "Parte ")
#Reconocimiento.reconocimiento()
Words = Texto("Transcripcion", 1, 2)
Words.juntar_words_en_uno()