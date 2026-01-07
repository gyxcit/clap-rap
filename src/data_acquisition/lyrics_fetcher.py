import lyricsgenius
import requests

# local imports
from  ..config import get_genius_token


def get_lyrics_genius(title, artist):
    token=get_genius_token()
    genius = lyricsgenius.Genius(token)
    song = genius.search_song(title, artist)
    if song:
        return song.lyrics
    return None



def get_lyrics_ovh(title, artist):
    # API Lyrics.ovh (gratuit)
    url = f"https://api.lyrics.ovh/v1/{artist}/{title}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data.get("lyrics")
    else:
        return None


if __name__ == "__main__":
    titre = "DKR"
    artiste = "Booba"
    #genius
    # paroles = get_lyrics_genius(titre, artiste)

    # if paroles:
    #     print(paroles)
    # else:
    #     print("Paroles non trouvées.")
    #lyrics.ovh
    paroles = get_lyrics_ovh(titre, artiste)
    if paroles:
        print(paroles)
    else:
        print("Paroles non trouvées.")
