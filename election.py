import numpy as np

from agent import agent

'''
TODO: 
- Basic elections
- Differnet electoral systems
- Misscounts
'''

def quickAgent(data):
    return agent(name=data["name"],income=data["income"],gullibility=data["gullibility"],politician=data["politician"],proImm=data["proImm"],prolgbt=data["prolgbt"],proWar=data["proWar"],race=data["race"],disposableIncome=data["disposableIncome"])

def elect(electorate,houses=[435,100,1],districts=[],candidates=[]):
    races = {}
    if districts == []:
        districts.append(houses)
    for i in range(len(districts)):
        for j in range(len(districts[i])):
            for k in range(districts[i][j]):
                race = "d"+str(i)+"_h"+str(j)+"_r"+str(k)
                races[race] = {"cands":[],"vote":[],"winner":None}
    if candidates != []:
        for c in candidates:
            races[c[0]]["cands"].append(candidates[1])
    for i in range(len(districts)):
        subElec = [electorate[j] for j in list(filter(lambda x: x.startswith(str(i)+"_"), electorate.keys()))]
        for j in range(len(districts[i])):
            for k in range(districts[i][j]):
                race = races["d"+str(i)+"_h"+str(j)+"_r"+str(k)]
                if len(race["cands"]) == 0:
                    race["cands"] = np.random.choice([electorate[l] for l in list(filter(lambda x: x.startswith(str(i)+"_"), electorate.keys()))],2).tolist()
                elif len(race["cands"]) == 1:
                    race["cands"].append(np.random.choice([electorate[l] for l in list(filter(lambda x: x.startswith(str(i)+"_"), electorate.keys()))],1).tolist()[0])
                for c in race["cands"]:
                    race["vote"].append(sum([quickAgent(l).proCon(quickAgent(c).optimal()) for l in subElec])/len(subElec))
                race["winner"] = race["cands"][race["vote"].index(max(race["vote"]))]
    return races

    