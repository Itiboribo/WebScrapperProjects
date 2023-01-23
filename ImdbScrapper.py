from bs4 import BeautifulSoup
import requests, openpyxl
import csv

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'Top Rated Movies'
sheet.append(['Movie Rank', 'Movie Name', 'Year of release', 'Movie Rating'])


try:
    source = requests.get('https://www.imdb.com/chart/top/')
    source.raise_for_status()

    soup = BeautifulSoup(source.text,'html.parser')

    movies = soup.find('tbody', class_='lister-list').find_all('tr')

    for movie in movies:

        MovieName = movie.find('td', class_='titleColumn').a.get_text()
        MovieRank = movie.find('td', class_='titleColumn').get_text(strip=True).split('.')[0]
        MovieYear = movie.find('td', class_='titleColumn').span.get_text().strip('()')
        MovieRating = movie.find('td', class_='ratingColumn imdbRating').strong.get_text()

        print(MovieRank, MovieName, MovieYear, MovieRating)
        sheet.append([MovieRank, MovieName, MovieYear, MovieRating])
        
except Exception as e:
    print(e)

excel.save('IMDB Top 250 Rated movies.xlsx')
 
