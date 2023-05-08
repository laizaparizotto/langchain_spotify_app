from ai_agents import initialize_agent_zero_shot
from ai_tools import tool_start_playing_song_by_lyrics, tool_start_playing_song_by_name, tool_add_song_to_queue_by_song_name, tool_pause_song

# Initialize agent
tools = [
    tool_start_playing_song_by_lyrics(),
    tool_start_playing_song_by_name(),
    tool_add_song_to_queue_by_song_name(),
    tool_pause_song(),
]

agent = initialize_agent_zero_shot(tools=tools)

print("\nEaiiii, o que quer escutar hoje?")

while True:
    request = input(
        "\n\nFala ai: ")
    result = agent({"input": request})
    answer = result["output"]
    print(answer)
