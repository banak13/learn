from faker import Faker
from operator import itemgetter, attrgetter

fake = Faker("pl_PL")


class Movie:
    def __init__(self, title, year, genre, plays):
        self.title = title
        self.year = year
        self.genre = genre
        self.plays = plays

    def play(self, step=1):
        self.plays += step

    def __str__(self):
        return f'{self.title, self.year, self.genre, self.plays}'

    def __repr__(self):
        return 'Movie(title: %s, year: %s, genre: %s, plays: %r)' % (self.title, self.year, self.genre, self.plays)

    def movie_details(self):
        return f"{self.title} ({self.year})"

    def isSeries(self):
        return False

    def to_list(self):
        return [self.title, self.year, self.genre, self.plays]


class Series(Movie):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season

    def series_details(self):
        return f"{self.title} S{self.season}E{self.episode}"

    def __repr__(self):
        return 'Series(title: %s, year: %s, genre: %s, plays: %r, episode: %r, season: %r)' % (
        self.title, self.year, self.genre, self.plays, self.episode, self.season)

    def play(self, step=1):
        self.plays += step

    def isSeries(self):
        return True

    def to_list(self):
        return [self.title, self.year, self.genre, self.plays, self.season, self.episode]


def generate_movies():
    for i in range(10):
        main_list.append(
            Movie(
                title=fake.name(),
                year=fake.year(),
                genre=fake.name(),
                plays=fake.random_int(0, 100)
            )
        )
    return main_list

def generate_series():
    for j in range(10):
        main_list.append(
            Series(
                title=fake.name(),
                year=fake.year(),
                genre=fake.name(),
                season=fake.random_int(1, 4),
                episode=fake.random_int(0, 20),
                plays=fake.random_int(0, 100)
            )
        )
    return main_list

def generate_data():
    generate_movies()
    generate_series()
    return main_list

def generate_views(main_list):
    for k in range(10):
        for l in main_list:
            Movie.play(l)
    return main_list

