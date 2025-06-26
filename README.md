# siri-spotify-dictation
Spotify Voice Shortcut This macOS Shortcut + Python script lets you say “Hey Siri, Music by Voice” and dictate any song you want. It will search Spotify, open the track instantly, and works even on free Spotify accounts — no auto-play needed.  Built with love, Spotipy, and frustration toward Apple Music defaults 😅
# 🎧 Spotify Voice Shortcut

A macOS Siri Shortcut + Python script that lets you **dictate a song name** and **open it in Spotify** — even with a free account.

##  How It Works

1. Say: _“Hey Siri, Music by Voice”_
2. Dictate the song title (e.g. “Bohemian Rhapsody by Queen”)
3. It opens the matching track in Spotify (click Play if you're on free)

No Apple Music. No Premium needed. No BS.

## 🛠 Requirements

- macOS with Shortcuts app
- Python 3
- [Spotify Developer App](https://developer.spotify.com/dashboard)
- `pip3 install spotipy`

## 📦 Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/bugbutcherr/spotify-voice-shortcut.git
   cd spotify-voice-shortcut
   
2. install dependencies:
   pip3 install -r requirements.txt
   if thats not working just type "pip3 install spotipy" in the terminal
   
4. Fill in your client_id, client_secret, and redirect_uri in iplay_song.py.(you get this in the spotify developer)

5. Create a Shortcut in macOS:

Dictate Text

Run Shell Script:

python3 /path/to/iplay_song.py "[Dictated Text]"

Or you could just click this link -> https://www.icloud.com/shortcuts/0ee765398e684f18b39583c4d6d32402
(please note you need to add the folder in by yourself if youre using the link)

Recommended Siri Phrase
Name your Shortcut: “Music by Voice”
This avoids Siri defaulting to Apple Music.

Thank you this is my first time creating a repository I just want to help the community out if you guys have any advices or issues just reach out to me
ill try to solve it ASAP🫶!!

