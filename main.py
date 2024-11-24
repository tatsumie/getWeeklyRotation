from api import getWeeklyChamps, getGameVersion, getChampNamesFromID
import os 
weeklyRotation = getChampNamesFromID()
if weeklyRotation:
    print("This week's weekly rotation:")
    for champ in weeklyRotation:
        print(champ)
else:
    print("failed to get champ names")