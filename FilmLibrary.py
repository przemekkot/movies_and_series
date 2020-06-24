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
film4 = Film(title="Argo", year="2012", genre="thriller", times_played=0)
film5 = Film(title="Focus", year="2015", genre="comedy", times_played=0)

series1_1 = Series(title="Friends", year="1994", genre="comedy", season="01", episode="01", times_played=0)
series1_2 = Series(title="Friends", year="1994", genre="comedy", season="01", episode="02", times_played=0)
series1_3 = Series(title="Friends", year="1994", genre="comedy", season="01", episode="03", times_played=0)
series1_4 = Series(title="Friends", year="1994", genre="comedy", season="01", episode="04", times_played=0)
series1_5 = Series(title="Friends", year="1994", genre="comedy", season="01", episode="05", times_played=0)


full_list = []
films = []
series = []

full_list.append(film1)
full_list.append(film2)
full_list.append(film3)
full_list.append(film4)
full_list.append(film5)
full_list.append(series1_1)
full_list.append(series1_2)
full_list.append(series1_3)
full_list.append(series1_4)
full_list.append(series1_5)

#7
def get_movies():
      for i in full_list:
        films = [i for i in full_list if type(i) == Film]
        sorted_films = sorted(films, key=operator.attrgetter('title'))
        #sorted_films = sorted(films, key=lambda Film: Film.title)
      return sorted_films
      
print(get_movies())

def get_series():
      for i in full_list:
        series = [i for i in full_list if isinstance(i, Series)]
        sorted_series = sorted(series, key=operator.attrgetter('title'))
        #sorted_series = sorted(series, key=lambda Series: Series.title)
      return sorted_series

print(get_series())

#8

def search(name):
    for i in full_list:
        if name in i.title:
        #if i.title == name:
            return i
    else:
        print("W bazie nie ma takiego tytułu")

print(search('Twister'))

#9

def generate_views():
    random_result = random.choice(full_list)
    #random_result.times_played = random.randint(1,100)
    for i in range(random.randint(1,100)):
        random_result.play()
    return random_result

print(generate_views())

#10

result = 0
entire_library = []

def generate_views_10times():
    for n in range(10):
        result = generate_views()
        entire_library.append(result)
    return entire_library

print(generate_views_10times())

#11

def top_titles(top):
    top_n_titles = []
    top_n_titles = sorted(entire_library, key = lambda film: film.times_played, reverse = True)[:top]
    return top_n_titles

print(top_titles(3))

#top_titles() z content_type

def top_titles(content_type, top):
    selected_data_by_type = []
    if content_type == "top_films":
        selected_data_by_type = [i for i in entire_library if type(i) == Film]
    elif content_type == "top_series":
        selected_data_by_type = [i for i in entire_library if isinstance(i, Series)]       
    else:
        selected_data_by_type = entire_library

    return sorted(selected_data_by_type, key = lambda film: film.times_played, reverse = True)[:top]

print(top_titles("top_series", 2))
