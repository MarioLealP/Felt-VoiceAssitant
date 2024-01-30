import spotipy
from spotipy.oauth2 import SpotifyOAuth
from apiKeys import spotifyID, spotifySecret, spoitfyURL

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotifyID,
                                               client_secret=spotifySecret,
                                               redirect_uri=spoitfyURL))


def playSpotifyMusic(music_name):
    print("Music name: " + music_name)
    # Search for a track
    track_name = music_name  # Change this to the desired track
    results = sp.search(q=track_name, type='track')

    # Get the first track from the results
    track_uri = results['tracks']['items'][0]['uri']

    # Play the track
    sp.start_playback(uris=[track_uri])