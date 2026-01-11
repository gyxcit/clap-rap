# Installer yt_dlp si nécessaire :
# pip install yt-dlp

from yt_dlp import YoutubeDL

# Saisie de l'artiste et de la chanson
artiste = input("Nom de l'artiste : ")
chanson = input("Nom de la chanson : ")

# Requête de recherche
query = f"{artiste} - {chanson}"

# Options pour télécharger uniquement l'audio et convertir en mp3
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',  # nom du fichier
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192',
    }],
    'quiet': False,
    'noplaylist': True,  # ne pas télécharger de playlist, juste la première vidéo
}

with YoutubeDL(ydl_opts) as ydl:
    # Recherche et téléchargement
    print(f"Recherche et téléchargement de : {query}")
    ydl.download([f"ytsearch1:{query}"])
