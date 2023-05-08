# Langchain Spotify App

This is a chat to play songs on spotify using Langchain Agents.

# Setup
- Sign up for Spotify and Spotify API (developer.spotify.com)

- Create an app on your spotify developer account and and save "client id", "client secret".

- As we are running this repository locally, select a random redirect URI i.e. "http://localhost/". (will be updated later)

- Sign up for OpenAI API Key

- Clone git repo.

- Create a .env file and write these values in

```
OPENAI_API_KEY=
SPOTIFY_CLIENT_ID=
SPOTIFY_CLIENT_SECRET=
SPOTIFY_REDIRECT_URI=
```

- Create a new Python virtual environment

py -m venv langchain_spotify_app (Windows 11)

- Start virtual environment manually by running:

.\langchain_spotify_app\Scripts\activate (Windows 11)

- Install Python requirements in the project repository: pip install -r requirements.txt

# Usage
To start: py main.py (Windows 11)
