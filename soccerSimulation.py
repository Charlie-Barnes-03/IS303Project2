# Charlie Barnes, 
# P2 Soccer Simulation

def intro_display() :
    playerName = input("Enter your name: ")
    print(f"\nWelcome {playerName}! This program will simulate a soccer season where you provide the team names and the scores are randomly generated!")
    return playerName

sPlayerName = intro_display()

print(sPlayerName)