from pytube import YouTube
import moviepy.editor as mp
import re
import os

# endereco do video e endereco onde salvar
link = input("Digite o link que deseja baixar: ")
path = input("Digite o caminho onde deseja salvar o arquivo: ")

yt = YouTube(link)

# comeca o dowload
print("Baixando...")
ys = yt.streams.filter(only_audio=True).first().download(path)
print("Download completo!!!")

#converte para mp3
print("Convertendo arquivo...")
for file in os.listdir(path):
    if re.search('mp4', file):
        mp4_path = os.path.join(path, file)
        mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3')
        new_file = mp.AudioFileClip(mp4_path)
        new_file.write_audiofile(mp3_path)
        os.remove(mp4_path)

print("Sucesso")
