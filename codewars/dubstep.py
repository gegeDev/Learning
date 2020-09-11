def song_recorder(song):
    return "".join(x + " " for x in song.split("WUB") if x != '')[:-1]

print("AWUBWUBWUBWUBBWUBWUBWUBC".split("WUB"))
print(song_recorder("AWUBWUBWUBWUBBWUBWUBWUBC"))
