import pandas as pd
import csv as csv

st = pd.read_csv('2023-2024SquadStandardStats.csv')
gs = pd.read_csv('2023-2024SquadGoalandShotCreation (1).csv')
wg = pd.read_csv('2023-2024SquadWages.csv')
ly = pd.read_csv('2022SquadStat.csv')
bt = pd.read_csv('Bettingodds.csv')

row_index = 0 
elo = {}
wages = []
goalrating = []
wageandgoal = {}
lastseasonstat = []
betodds = []
betandwageandgoal = {}
wageandgoalvalues = []

#prints a list with all teams ratings, derived from goals and ExpG
for row_index in range(17):
    goalrating.append( round((st.iloc[row_index].values[9]*.3) + (st.iloc[row_index].values[17]*.7),2) )

#print(sorted(goalrating, reverse=True))


##
##Goals value
##


#loops through all 17 teams and creates a value which is comprised of 30% goals and 70% Expected goals
for row_index in range(17):
    #returns a whole row of values in SquadStandardStats
    row_val = st.loc[row_index].values
    #creates a key value pair to store the calculated values
    elo[st.iloc[row_index].values[1]] = round((st.iloc[row_index].values[9]*.3) + (st.iloc[row_index].values[17]*.7),2)


#print(elo)
sortedlist = sorted(elo.items(), key=lambda x:x[1], reverse=True)
#print(dict(sortedlist))


##
##Wages and goals values
##

#prints a list with all teams annual wages
for row_index in range(17):
    wages.append(wg.iloc[row_index].values[11])

#print(wages)

#Calulates another value using the original elo value as well as the yearly wages of the team. The wages are weighted 10% of the total value
for row_index in range(17):
    wageandgoal[st.iloc[row_index].values[1]] = round((goalrating[row_index]*.9) + ((wages[row_index]/1000000)*.1),2)
    wageandgoalvalues.append(round((goalrating[row_index]*.9) + ((wages[row_index]/1000000)*.1),2))

#print(wageandgoal)
sortedWage = sorted(wageandgoal.items(), key=lambda x:x[1], reverse=True)
#print(dict(sortedWage))


##
## combines betting odds, wages, and goals
##

for row_index in range(17):
    betodds.append(bt.iloc[row_index].values[5])

#print(betodds)

##
## Final team rating values which include wages, goals, and betting odds. Betting odds are weighted 25%
##

for row_index in range(17):
    betandwageandgoal[st.iloc[row_index].values[1]] = round((wageandgoalvalues[row_index]*.75) + ((betodds[row_index])*.25),2)

#print(betandwageandgoal)
sortedBet = sorted(betandwageandgoal.items(), key=lambda x:x[1], reverse=True)
print(dict(sortedBet))





##
##Last season stat values
##

for row_index in range(17):
    lastseasonstat.append( round((ly.iloc[row_index].values[9]*.3) + (ly.iloc[row_index].values[17]*.7),2) )

#print(sorted(lastseasonstat, reverse=True))

