class Songs:
    def __init__(self):
        self.song_stack = []
        self.index = 0

    def add_song(self, name):
        self.song_stack.append(name)


    def delete_song(self, name):
        isfound = False
        for i in self.song_stack:
            if i == name:
                self.song_stack.remove(i)
                print("song removed!")
                isfound = True

            if not isfound: print("song not found!")

    def next(self):
        if len(self.song_stack) == 0: print("Please add song first")
        else:
            print("next song is:", self.song_stack[self.index])
            self.index += 1


    def current_song(self):
        if len(self.song_stack) == 0: print("Add song")
        else: print("current song is:", self.song_stack[self.index])


    def suffle(self):
        import random
        if len(self.song_stack) == 0: print("No song")
        else:
            self.index = random.randrange(0, len(self.song_stack))
            print("your shuffle song is", self.song_stack[self.index])


song = Songs()
song.current_song()
song.add_song("TERE NAAM")
song.add_song("CHUNARIYA")
song.add_song("CHUNARIYA123")
song.next()
song.delete_song("TERE NAAM")

song.current_song()
song.next()




