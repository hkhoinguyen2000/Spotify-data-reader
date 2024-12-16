import json
import heapq
from collections import defaultdict

json_file = r"/Users/khoinguyen/Downloads/Spotify Extended Streaming History/Streaming_History_Audio_2023-2024.json"


# Open and load the JSON file
with open(json_file, "r") as file:
    data = json.load(file)

# Access elements

artist_album_ct = defaultdict(lambda: defaultdict(int))  
artists = defaultdict(int)

for entry in data:
    artist = entry['master_metadata_album_artist_name']
    album = entry['master_metadata_album_album_name']

    artists[artist] += 1


    artist_album_ct[artist][album] += 1

heap = [(-val, key) for key, val in artists.items()]

while heap:
    artist_ct, artist = heapq.heappop(heap)
    print(artist)
