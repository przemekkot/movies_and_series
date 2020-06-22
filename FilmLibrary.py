import operator
import random
from random import randrange
from random import randint

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
    
        
class Series(Film):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season
        
    def __str__(self):
        return f'{self.title}, {self.year}, {self.genre}, S{self.season}, E{self.episode}, {self.times_played}'
    
    def __repr__(self):
        return f"Series(title={self.title} season={self.season} episode={self.episode} year={self.year}, genre={self.genre}, times_played={self.times_played})"
    
film1 = Film(title="Forrest Gump", year="1994", genre="comedy", times_played=0)
film2 = Film(title="Twister", year="1996", genre="catastrophic", times_played=0)
film3 = Film(title="Sinister", year="2012", genre="horror", times_played=0)

series1_1 = Series(title="Friends", year="1994", genre="comedy", season="01", episode="01", times_played=0)
series1_2 = Series(title="Friends", year="1994", genre="comedy", season="01", episode="02", times_played=0)
series1_3 = Series(title="Friends", year="1994", genre="comedy", season="01", episode="03", times_played=0)

#print(film1)
#print(film2)
#print(film3)

#print(series1_1)
#print(series1_3)
#print(series1_3)

#load_to_list = ""
full_list = []
films = []
series = []

full_list.append(film1)
full_list.append(film2)
full_list.append(film3)
full_list.append(series1_1)
full_list.append(series1_2)
full_list.append(series1_3)

#print(full_list)
#sorted_full_list = sorted(full_list, key=operator.attrgetter('title'))
#print(sorted_full_list)
#print(sorted(full_list))
#full_list_sorted = sorted(full_list, key=lambda 1: 1.count, reverse=True)
#print(full_list_sorted)

def get_movies():
      for i in full_list:
        films = [i for i in full_list if isinstance(i, Film)]
        sorted_films = sorted(films, key=operator.attrgetter('title'))
      else:
        pass
      return sorted_films
      
print(get_movies())

def get_series():
      for i in full_list:
        series = [i for i in full_list if isinstance(i, Series)]
        sorted_series = sorted(series, key=operator.attrgetter('title'))
      else:
        pass
      return sorted_series

print(get_series())


search_result = []

def search(name):
    for i in full_list:
        search_result = [i for i in full_list if name == operator.attrgetter('title')]
    else:
        print("W bazie nie ma takiego tytułu")
    return search_result

print(search('Twister'))


random_result = []

def generate_views():
    for i in full_list:
        random_result = [random.choice(full_list)]
    #operator.attrgetter('times_played') = random.randint(1,100)
    return random_result

print(generate_views())


random_10_results = []
result = 0

def generate_views_10times():
    for i in range(10):
        for i in full_list:
            result = random.choice(full_list)
            random_10_results.append(result)
    return random_10_results

print(generate_views_10times())
