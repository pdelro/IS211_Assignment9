from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

def main():
    url = 'http://www.footballlocks.com/nfl_point_spreads.shtml'
    response = urllib.request.urlopen(url)

    soup = BeautifulSoup(response.read(), features='lxml')
    table = soup.find('table', attrs={'cols': '4'})
    games = table.find_all('tr')[1:]
    current_spreads = []

    for row in games:
        details = row.find_all('td')
        DAT = details[0].contents[0]
        favorite = details[1].contents[0]
        spread = details[2].contents[0]
        underdog = details[3].contents[0]
        game_info = {}
        game_info['Game Date and Time'] = DAT
        game_info['Favorite'] = favorite
        game_info['Spread'] = spread
        game_info['Underdog'] = underdog
        current_spreads.append(game_info)

    NFL_point_spreads = pd.DataFrame(current_spreads)
    print(NFL_point_spreads.to_string(index=False))


if __name__ == "__main__":
    main()
