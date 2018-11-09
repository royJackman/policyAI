import numpy as np

'''
TODO: 
- Basic elections
- Differnet electoral systems
- Misscounts
'''

def elect(electorate,houses=[435,100],districts=[],candidates=[]):
    races = {}
    if districts == []:
        districts.append(houses)
    for i in range(len(districts)):
        for j in range(districts[i]):
            for k in range(districts[i][j]):
                race = "d"+str(i)+"_h"+str(j)+"_r"+str(k)
                races[race] = {cands:[],vote:[],winner=None}
    if candidates != []:
        for c in candidates:
            races[c[0]].cands.append(candidates[1])
    for i in range(len(districts)):
        for j in range(districts[i]):
            for k in range(districts[i][j]):
                race = "d"+str(i)+"_h"+str(j)+"_r"+str(k)
                race = races[race]
                if len(race.candidates) == 0:
                    race.candidates = np.random.choice([electorate[k] for k in list(filter(lambda x: x.startswith(str(i)+"_"), electorate.keys()))],1).tolist()
                elif len(race.candidates) == 1:
                    race.candidates.append(np.random.choice([electorate[k] for k in list(filter(lambda x: x.startswith(str(i)+"_"), electorate.keys()))],2).tolist()[0])

    