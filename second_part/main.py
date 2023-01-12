from model import Movies, Playlist, TvShow

avengers = Movies('avengers', 2018, 180)
this_is_us = TvShow('this is us', 2016, 7)

# print(f'Nome do filme: {avengers.title} - Ano de Lançamento:',
#       f'{avengers.release_year} - Duração: {avengers.duration}',
#       f' - Likes: {avengers.likes}')

avengers = Movies('avengers', 2018, 180)
this_is_us = TvShow('this is us', 2016, 7)
scream = Movies('scream', 1909, 100)
lucifer = TvShow('lucifer', 2015, 5)

# para resolver atributos diferentes em lista
list_of_shows = [avengers, this_is_us, scream, lucifer]
weekend_playlist = Playlist('Weekend Playlist', list_of_shows)

print(f'Tamanho da playlist: {len(weekend_playlist)}')

for show in weekend_playlist:
    print(show)
