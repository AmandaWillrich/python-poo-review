class Entertainment:
    def __init__(self, title, release_year):
        self._title = title.title()
        self.release_year = release_year
        self._likes = 0

    def likes(self):
        self._likes += 1

    @property
    def likes(self):
        return self._likes

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title


class Movies(Entertainment):
    def __init__(self, title, release_year, duration):
        super().__init__(title, release_year)
        self.duration = duration

    def __str__(self):
        return f'{self.title} - {self.release_year} - {self.duration} minutos - {self.likes} likes'


class TvShow(Entertainment):
    def __init__(self, title, release_year, seasons):
        super().__init__(title, release_year)
        self.seasons = seasons

    def __str__(self):
        return f'{self.title} - {self.release_year} - {self.seasons} temporadas - {self.likes} likes'


class Playlist(list):
    def __init__(self, name, shows):
        self.name = name
        super().__init__(shows)
