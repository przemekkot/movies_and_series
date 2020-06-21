class Film:
    def __init__(self, title, year, genre, times_played):
        self.title = title
        self.year = year
        self.genre = genre
        self.times_played = times_played
    
    def play(self, play_one=1):
        self.times_played += play_one

    def __str__(self):
        return f'{self.title}, {self.year}, {self.genre}, {self.times_played}'
        
    def __repr__(self):
        return f"Film(title={self.title} year={self.year}, genre={self.genre}, times_played={self.times_played})"
    
    #Variables
    list = []
    films = []
        
    def get_movies(self):
      for i in self.list:
        films = [i for i in self.list if isinstance(i, Film)]
      else:
        pass
    
    
    
        
class Series(Film):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season
        
    def play(self, play_one=1):
        self.times_played += play_one

    def __str__(self):
        return f'{self.title}, {self.year}, {self.genre}, S{self.season}, E{self.episode}, {self.times_played}'
    
    def __repr__(self):
        return f"Series(title={self.title} season={self.season} episode={self.episode} year={self.year}, genre={self.genre}, times_played={self.times_played})"
    
film1 = Film(title="Forrest Gump", year="1994", genre="comedy", times_played=0)
film2 = Film(title="Twister", year="1996", genre="catastrophic", times_played=0)
film3 = Film(title="Siniser", year="2012", genre="horror", times_played=0)

series1_1 = Series(title="Friends", year="1994", genre="comedy", season="01", episode="01", times_played=0)
series1_2 = Series(title="Friends", year="1994", genre="comedy", season="01", episode="02", times_played=0)
series1_3 = Series(title="Friends", year="1994", genre="comedy", season="01", episode="03", times_played=0)

print(film1)
print(film2)
print(film3)

print(series1_1)
print(series1_3)
print(series1_3)

#load_to_list = ""
list = []
#films = []
series = []

list.append(film1)
list.append(film2)
list.append(film3)
list.append(series1_1)
list.append(series1_2)
list.append(series1_3)

print(list)

def get_movies(self):
      for i in self.list:
        films = [i for i in self.list if isinstance(i, Film)]
      else:
        pass

print(get_movies(self))
