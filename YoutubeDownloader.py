import yt_dlp
from pywebio.output import put_text
from os import startfile


def video_download():
    while True:
        video_link = input("Informe o link do vídeo: ")
        
        if video_link.startswith("https://www.youtube.com/"):
            put_text("Fazendo download do vídeo...".title()).style('color: blue;font-size:50px')
            try:
                # Usando yt-dlp para baixar o vídeo
                ydl_opts = {
                    'outtmpl': r'C:\Users\Gustavo Gamer\Downloads\%(title)s.%(ext)s',  # Caminho de download
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([video_link])  # Baixa o vídeo

                put_text("Vídeo baixado com sucesso!".title()).style('color: red; font-size:50px')
                startfile(r'C:\Users\Gustavo Gamer\Downloads')  # Abrir a pasta de downloads
            except Exception as e:
                put_text(f"Ocorreu um erro: {e}").style('color: red; font-size:30px')
                break
        else:
            put_text("Link inválido! Por favor, informe um link válido do YouTube.").style('color: red; font-size:30px')

if __name__ == "__main__":
    video_download()
