import spotipy
from spotipy.oauth2 import SpotifyOAuth

#wei client_id
# 245dbe2c7be14a3bacecd83487c53c66
#wei client_secret
# b3f6a52c20234ca4b54605d34a269cac

# ny client_id
# b6e42f8dd5b142d892b1eedeb03f141d
# ny client_secret
# 6d48c434bd0a448a94dc1b6a6423e72e
client_id = "b6e42f8dd5b142d892b1eedeb03f141d"
client_secret = "6d48c434bd0a448a94dc1b6a6423e72e"
redirect_uri = "http://127.0.0.1:5000/callback"

scope = "user-read-recently-played"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id = client_id,client_secret = client_secret,
                                                redirect_uri=redirect_uri))

print("Successfully authenticated as: ", sp.me()["display_name"])
results = sp.current_user_recently_played(limit=10)

song_ids = []
song_names = []
note_duration = [0 for i in range(12)]
chroma_scale = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

for idx, item in enumerate(results['items']):
    song_ids.append(item['track']['id'])
    song_names.append(item['track']['name'])

for i, id in enumerate(song_ids):
    print(song_names[i])
    segments = sp.audio_analysis(id)["segments"]
    
    for segment in segments:
        pitches = segment["pitches"]
        chroma = [pitches[i] for i in range(12)]
        current_note = chroma.index(max(chroma))
        note_duration[current_note] += segment["duration"]
print(song_names)
print("Most played note: ", chroma_scale[note_duration.index(max(note_duration))])