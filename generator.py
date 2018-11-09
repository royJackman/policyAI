import numpy as np

from agent import agent

def rAgent(
    name,
    income=None,
    gullibility=None,
    politician=None,
    district=None,
    proImm=None,
    prolgbt=None,
    proWar=None,
    race=None,
    disposableIncome=None):
    return agent(
        name,
        (income if (income != None) else np.random.rand()),
        (gullibility if (gullibility != None) else np.random.rand()),
        (politician if (politician != None) else (np.random.rand()>0.5)),
        (district if (district != None) else 0),
        (proImm if (proImm != None) else (np.random.rand()>0.5)),
        (prolgbt if (prolgbt != None) else (np.random.rand()>0.5)),
        (proWar if (proWar != None) else (np.random.rand()>0.5)),
        (race if (race != None) else {"white": np.random.rand(), "black": np.random.rand(), "amind": np.random.rand(), "asian": np.random.rand(), "hawaii": np.random.rand(), "other": np.random.rand()}),
        (disposableIncome if (disposableIncome != None) else np.random.rand()))

def population(count=3257, districts=[]):
    retval = {}
    if districts == []:
        districts = [count]
    for i in range(len(districts)):
        for j in range(districts[i]):
            name = str(i)+"_"+str(j)
            retval[name] = rAgent(name,district=i).tojson()
    return retval
        
