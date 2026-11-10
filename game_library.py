class VideoGame:
    def __init__(self, title: str, platform: str, hours_played: int)->None:
        self.title = title
        self.platform = platform
        self.hours_played = hours_played

    def add_play_time(self, hours: int)->None:
        self.hours_played += hours

    def has_been_played(self)->bool:        
        return self.hours_played > 0

    def __str__(self)->str:
        return f"{self.title} on {self.platform} ({self.hours_played} hours played)"

def main():
    game1 = VideoGame('stormworks','pc',0)
    print (game1.has_been_played())
    game1.add_play_time(1275)
    print (game1.has_been_played())
    print(game1)

    games: list[VideoGame] = []#typehint saying list of VideoGame objects

    games.append(game1)
    games.append(VideoGame("Final fantasy","NES",27))
    games.append(VideoGame("War Thunder","PC",100))

    #list the games
    for game in games:
        print(game)

    #just titles
    for game in games:
        print(game.title)







if __name__== "__main__":
    main()