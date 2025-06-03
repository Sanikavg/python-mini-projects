n=int(input("Enter number of teams: "))
for i in range(n):
    name=input("Enter team name: ")
    w=int(input("enter wins: "))
    l=int(input("Enter losses: "))
    team[name]=(w,l)
print(team)

#display team's winning percentage
t=input("enter team name: ")
print("winning percentage: ",team[t][0]/sum(team[t]*100))

#entries of number of wins of each team
winteam=[]
for i in team.values():
    winteam+=i[0]
print(winteam)

#teams having winning records
winrec=[]
for i in team:
    if i[0] in winteam:
        winrec+=i
print(winrec)
