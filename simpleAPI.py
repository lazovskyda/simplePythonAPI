import random
import requests

from bs4 import BeautifulSoup


URL = 'https.python.com'
def main():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    movietags = soup.select('td.titleColumn')
    inner_movietags = soup.select('td.titleColumn a')
    ratingtags = soup.select('td.posterColumn span[name=ir]')
    def get_year(movie_tag):
        moviesplit = movie_tag.text.split()
        year = moviesplit[-1]
        return year
    years = [get_year(tag) for tag in movietags]
    actors_list = [tag['title'] for tag in inner_movietags]
    titles = [float(tag['data-value']) for tag in ratingtags]
    ratings = [float(tag['data_value']) for tag in ratingtags]

    n_movies = len(titles)
   
    while(True):
        idx = random.randrange(0, n_movies)
        print(f'{titles[idx]} {years[idx]}, Rating: {ratings[idx]:.1f}')
        break   

        user_input = input('Do you want another moview (y/n)?')
        if user_input != 'y':
            break


if __name__ == '__main__':
    main()