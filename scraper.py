import os
import re

path = str(os.getcwd()) + "\\web\\"

filename = "bet365.html"

odds_search = '<span class="sgl-ParticipantOddsOnly80_Odds">'
team_search = 'class="rcl-ParticipantFixtureDetailsTeam_TeamName ">'
date_search = 'class="rcl-MarketHeaderLabel rcl-MarketHeaderLabel-leftalign ">'
date_search2 = '"rcl-MarketHeaderLabel-leftalign rcl-MarketHeaderLabel ">'

with open(path+filename, 'rb') as f:
    try:  # catch OSError in case of a one line file
        f.seek(-2, os.SEEK_END)
        while f.read(1) != b'\n':
            f.seek(-2, os.SEEK_CUR)
    except OSError:
        f.seek(0)
    last_line = f.readline().decode()

def scrape(search_str : str, last_line : str):
    vals:list[str] = []
    for match in re.finditer(search_str,last_line):
        start = match.end()
        stop = last_line.find("<",start)
        vals.append(last_line[start:stop])
    return vals

odds = scrape(odds_search,last_line)
teams = scrape(team_search,last_line)
dates = scrape(date_search,last_line)+scrape(date_search2,last_line)

