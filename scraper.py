import os
import re


def scrape_positions(search_str : str, string : str):
    positions:list[tuple[int,int]] = []
    for match in re.finditer(search_str,string):
        start = match.end()
        stop = string.find("<",start)
        positions.append((start,stop))
    return positions

def index_to_string(index:tuple[int,int],string:str) -> str:
    i,j = index
    word = string[i:j]
    return word

def str_fraction_to_float(fraction : str) -> float:
    frac: list[str] = fraction.split("/",1)
    numer,denom = frac
    num = float(numer) / float(denom)
    return num

def show_pos_as_strings(string:str,positions:list[tuple[int,int]]) -> list[str]:
    return [index_to_string(i,string) for i in positions]

path = str(os.getcwd()) + "\\web_scraper\\"

filename = "top.html"

odds_search = '<span class="sgl-ParticipantOddsOnly80_Odds">'
teams_search = 'class="rcl-ParticipantFixtureDetailsTeam_TeamName ">'
teams_search2 = 'class="rcl-ParticipantFixtureDetailsTeam_TeamName " style="">'
#dividers_search = '"suf-CompetitionMarketGroupButton_Text ">'

with open(path+filename, 'rb') as f:
    try:  # catch OSError in case of a one line file
        f.seek(-2, os.SEEK_END)
        while f.read(1) != b'\n':
            f.seek(-2, os.SEEK_CUR)
    except OSError:
        f.seek(0)
    last_line = f.readline().decode()

odds_positions = scrape_positions(odds_search,last_line)
teams_positions = scrape_positions(teams_search,last_line) + scrape_positions(teams_search2,last_line)
#dividers_positions = scrape_positions(dividers_search,last_line)

all_positions = sorted(odds_positions+teams_positions)



matches:list[tuple[str,str]] = []
for i in range(0,len(teams_positions),2):
    team1 = index_to_string(teams_positions[i],last_line)
    team2 = index_to_string(teams_positions[i+1],last_line)
    match:tuple[str,str] = (team1,team2)
    matches.append(match)

print(show_pos_as_strings(last_line,sorted(odds_positions)))