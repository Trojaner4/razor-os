#!/usr/bin/python3
import os
from pydub import AudioSegment
from pydub.playback import play
os.system('clear')
print("""

██████╗░░█████╗░███████╗░█████╗░██████╗░░░░░░░██████╗░██╗░░░░░░█████╗░██╗░░░██╗
██╔══██╗██╔══██╗╚════██║██╔══██╗██╔══██╗░░░░░░██╔══██╗██║░░░░░██╔══██╗╚██╗░██╔╝
██████╔╝███████║░░███╔═╝██║░░██║██████╔╝█████╗██████╔╝██║░░░░░███████║░╚████╔╝░
██╔══██╗██╔══██║██╔══╝░░██║░░██║██╔══██╗╚════╝██╔═══╝░██║░░░░░██╔══██║░░╚██╔╝░░
██║░░██║██║░░██║███████╗╚█████╔╝██║░░██║░░░░░░██║░░░░░███████╗██║░░██║░░░██║░░░
╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝░░░░░░╚═╝░░░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░
""")
song_input  = input("file eingeben-->")

song = AudioSegment.from_mp3(song_input)
play(song)
