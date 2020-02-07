import requests # To send HTTP requests/recieve HTTP response.
from bs4 import BeautifulSoup # To parse the HTTP response.
import pandas as pd # For data analysis and manipulation.

# Setting custom user-agent for the HTTP requests.

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'
headers = {'User-Agent': user_agent}

# Setting up the variables.
num_of_seasons = 6
series_name = 'The Office'

#Paste URL excluding the season number.
imdb_url = 'https://www.imdb.com/title/tt0386676/episodes?season='

season_data = []
#Iterate following for every season

for season_num in range(1,num_of_seasons+1):
    
    final_url = f'{imdb_url}{season_num}' # Adding season number to the url.
    
    print(f'Requesting the page for season {season_num}!...')
    
    r = requests.get(final_url, headers = headers)
    soup = BeautifulSoup(r.text, "html.parser")
    
    episode_list = soup.findAll("div", {"class": "list_item"})
    
    for item in episode_list:
        episode_title = item.find("a", {"itemprop": "name"}).text
        episode_rating = item.find("span", {"class": "ipl-rating-star__rating"}).text
        episode_votes = item.find("span", {"class": "ipl-rating-star__total-votes"}).text
        episode_air_date = item.find("div", {"class": "airdate"}).text
        episode_description = item.find("div", {"class": "item_description"}).text
    
        episode_num = episode_list.index(item) + 1
        episode_data = [season_num,\
                        episode_num,\
                        episode_title,\
                        episode_rating,\
                        episode_votes,\
                        episode_air_date,\
                        episode_description]
#         print(episode_data)

        season_data.append(episode_data)

imdb_df = pd.DataFrame(data= season_data,columns=['Season','Episode #','Title','Rating','# of Votes','Air date','Description'])

# Saving to a CSV file
imdb_df.to_csv('imdb_data.csv')
Here’s how the data looked after downloading.
