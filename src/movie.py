import imdb

def movie(name):
    ia = imdb.IMDb()
    movie_obj = ia.search_movie(name)
    el = ia.get_movie(movie_obj[0].movieID)
    title = str(el.get('title'))
    year = str(el.get('year'))
    plot = str(el.get('plot')[0])
    ty = False
    if str(el.get('kind')) == 'tv series':
        ty = True
    return(title,year,plot,ty)