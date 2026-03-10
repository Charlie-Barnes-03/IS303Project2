#Robbie McVey, Charlie Barns, Eli Weaver

#import random for generating scores of games
import random

#function to display name entry and explantation of game
def intro_display() :
    playerName = input("Enter your name: ")
    print(f"\nWelcome {playerName}! This program will simulate a soccer season where you provide the team names and the scores are randomly generated!")
    return playerName        

def chooseteam(sExcludedTeam =''):
    iTeamNum = 0
    print("Here is the list of teams available to choose.\n")
    for t in lstTeams:
        if t != sExcludedTeam:
            print(f'{iTeamNum + 1}. {t}')
            iTeamNum += 1
    iChoice = int(input("\nPlease choose a team from the list: "))
    sSelectedTeam = lstTeams[iChoice - 1]
    lstTeams.remove(sSelectedTeam)
    return sSelectedTeam


def showMenu() :
    bPlay = True

    #Establish variables to keep track of the total wins and losses.
    iHomeWins = 0
    iHomeLosses = 0

    while (bPlay == True) :
        print(" 1 - Play the game")
        print(" 2 - Display final record")
        print(" 3 - Exit\n")

        iChoice = int( input("Make a selection: "))

        
        if iChoice == 1 :
            # A function that creates random numbers which represent the score of soccer games
            def scores() :
                global iHomeScore, iAwayScore
                iHomeScore = random.randrange(0,4)
                iAwayScore = random.randrange(0,4)
                return iHomeScore, iAwayScore


            # generate scores for the game, make sure there is no tie
            iHomeScore, iAwayScore = scores()
            while iHomeScore == iAwayScore :
                iHomeScore, iAwayScore = scores()

            if iHomeScore > iAwayScore :
                iHomeWins = iHomeWins + 1
                print(f"\t{sHomeTeam}'s score: {iHomeScore} - {sAwayTeam}'s score: {iAwayScore}\n")

            elif iHomeScore < iAwayScore :
                iHomeLosses = iHomeLosses + 1
                print(f"\t{sHomeTeam}'s score: {iHomeScore} - {sAwayTeam}'s score: {iAwayScore}\n")

        if iChoice == 2 :
            print(f"{sHomeTeam} has a final record of {iHomeWins} wins and {iHomeLosses} losses.\n")

        if iChoice == 3 :
            print(f"Thanks for playing {sPlayerName}! Come back soon.\n")
            bPlay = False

sPlayerName = intro_display()

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

print('\n Choose a Home Team.\n')
sHomeTeam = chooseteam()
print('\n Choose an Away Team\n')
sAwayTeam = chooseteam(sHomeTeam)

print(f'\nHome team: {sHomeTeam}')
print(f'Away team: {sAwayTeam}\n')

showMenu()