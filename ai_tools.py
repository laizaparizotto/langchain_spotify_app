from langchain.agents import Tool
from spotify import start_playing_song_by_name, start_playing_song_by_lyrics, add_song_to_queue_by_song_name, pause_music


def tool_start_playing_song_by_name():
    return Tool(name="Song given a name", func=lambda song_name: start_playing_song_by_name(song_name), description=f"""Given a song name, start playing a song. Action Input is a string of song_name.""", return_direct=True)  # type: ignore


def tool_start_playing_song_by_lyrics():
    return Tool(name="Song given lyrics", func=lambda lyrics: start_playing_song_by_lyrics(lyrics), description=f"""Given lyrics, start playing a song. Action Input is a string of lyrics.""", return_direct=True)  # type: ignore

def tool_add_song_to_queue_by_song_name():
    return Tool(name="Add to queue", func=lambda song_name: add_song_to_queue_by_song_name(song_name), description=f"""Add the song to the queue. Action Input is a string of song_name.""", return_direct=True)

def tool_pause_song():
    return Tool(name="Pause music", func=lambda tool_input: pause_music(None), description="Stop music. Action Input is a string = None", return_direct=True)