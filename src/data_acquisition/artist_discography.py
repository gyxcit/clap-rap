import discogs_client
import pprint

from ..config import get_discogs_token

# Remplacez par votre token
TOKEN = get_discogs_token()

artiste='freeze corleone'
d = discogs_client.Client('DiscographyFetcher/1.0', user_token=TOKEN)
results = d.search(artiste, type='artist')
artist_id = results[0].id


for release in results[0].releases:
    title=release.title
    artist_name=release.data.get('artist')
    if artiste in artist_name.lower():
        print(f"artiste : {artist_name}\ntitle : {title} \n{20*'-'} ")
