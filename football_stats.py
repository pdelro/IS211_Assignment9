from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

def main():
    url = 'https://www.cbssports.com/nfl/stats/player/scoring/nfl/regular/all/?sortcol=rutd&sortdir=descending'
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response.read(), features='lxml')
    player_info = soup.find_all('tr')[1:21]
    top_twenty = []

    for row in player_info:
        player_stats = {}
        player_name = row.select('a')[1].contents[0]
        player_position = row.select('span')[2].contents[0].strip()
        player_team = row.select('span')[3].contents[0].strip()
        rushing_touchdowns = row.select('td')[2].contents[0].strip()
        player_stats['Name'] = player_name
        player_stats['Position'] = player_position
        player_stats['Team'] = player_team
        player_stats['Rushing Touchdowns'] = rushing_touchdowns
        top_twenty.append(player_stats)

    player_info = pd.DataFrame(top_twenty)
    player_info.index += 1
    print(player_info)


if __name__ == "__main__":
    main()
