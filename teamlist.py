#Robbie McVey
#Pre Built List of Teams and select teams
lstTeams = ["North Carolina Tar Heels",
    "Stanford Cardinal",
    "UCLA Bruins",
    "Florida State Seminoles",
    "Penn State Nittany Lions",
    "Georgetown Hoyas",
    "Virginia Cavaliers",
    "Notre Dame Fighting Irish",
    "Texas Longhorns",
    "Portland Pilots",
    "BYU Cougars"]

def chooseteam(sExcludedTeam =''):
    iTeamNum = 0
    print("Here is the list of teams available to choose.")
    for t in lstTeams:
        if t != sExcludedTeam:
            print(f'{iTeamNum + 1}. {t}')
            iTeamNum += 1
    iChoice = int(input("Please choose a team from the list: "))
    sSelectedTeam = lstTeams[iChoice - 1]
    lstTeams.remove(sSelectedTeam)
    return sSelectedTeam
print('\n Choose a Home Team.')
sHomeTeam = chooseteam()
print('\n Choose an Away Team')
sAwayTeam = chooseteam(sHomeTeam)

print(f'Home team: {sHomeTeam}')
print(f'Away team: {sAwayTeam}')
