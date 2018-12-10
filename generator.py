import policy
import election
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
    disposableIncome=None,
):
    return agent(
        name,
        (income if (income != None) else (np.random.rand() * 0.006) + 0.027),
        (gullibility if (gullibility != None) else np.random.rand()),
        (politician if (politician != None) else False),
        (district if (district != None) else 0),
        (proImm if (proImm != None) else (np.random.rand() > 0.5)),
        (prolgbt if (prolgbt != None) else (np.random.rand() > 0.5)),
        (proWar if (proWar != None) else (np.random.rand() > 0.5)),
        (
            race
            if (race != None)
            else {
                "white": np.random.rand(),
                "black": np.random.rand(),
                "amind": np.random.rand(),
                "asian": np.random.rand(),
                "hawaii": np.random.rand(),
                "other": np.random.rand(),
            }
        ),
        (disposableIncome if (disposableIncome != None) else np.random.rand()),
    )


def population(
    count=3257,
    avginc=[
        0.045,
        0.0733,
        0.0515,
        0.042,
        0.065,
        0.064,
        0.071,
        0.061,
        0.049,
        0.051,
        0.073,
        0.048,
        0.06,
        0.05,
        0.055,
        0.054,
        0.045,
        0.046,
        0.051,
        0.076,
        0.071,
        0.051,
        0.063,
        0.041,
        0.05,
        0.05,
        0.055,
        0.052,
        0.07,
        0.072,
        0.045,
        0.061,
        0.048,
        0.061,
        0.051,
        0.049,
        0.054,
        0.056,
        0.058,
        0.047,
        0.053,
        0.047,
        0.056,
        0.063,
        0.057,
        0.066,
        0.64,
        0.042,
        0.056,
        0.06,
    ],
    districts=[
        50,
        7,
        69,
        30,
        393,
        56,
        37,
        11,
        207,
        104,
        15,
        17,
        129,
        67,
        32,
        29,
        45,
        47,
        13,
        61,
        69,
        99,
        56,
        31,
        62,
        10,
        20,
        29,
        14,
        90,
        22,
        197,
        101,
        8,
        119,
        40,
        41,
        129,
        11,
        51,
        9,
        67,
        280,
        31,
        9,
        84,
        74,
        18,
        59,
        8,
    ],
    immigration=0.67 * np.ones(50),
    lgbt=[
        0.32,
        0.54,
        0.58,
        0.36,
        0.61,
        0.6,
        0.67,
        0.57,
        0.52,
        0.44,
        0.64,
        0.53,
        0.59,
        0.47,
        0.57,
        0.5,
        0.4,
        0.42,
        0.63,
        0.56,
        0.73,
        0.55,
        0.58,
        0.32,
        0.57,
        0.47,
        0.54,
        0.6,
        0.75,
        0.66,
        0.58,
        0.63,
        0.44,
        0.5,
        0.53,
        0.57,
        0.63,
        0.56,
        0.7,
        0.39,
        0.44,
        0.39,
        0.48,
        0.43,
        0.67,
        0.5,
        0.63,
        0.37,
        0.59,
        0.41,
    ],
    wars=0.43 * np.ones(50),
):
    retval = {}
    if districts == []:
        districts = [count]
    for i in range(len(districts)):
        for j in range(districts[i]):
            name = str(i) + "_" + str(j)
            retval[name] = rAgent(
                name,
                income=(np.random.rand() * 0.006) + (avginc[i] - 0.003),
                district=i,
                proImm=True if (np.random.rand() <= immigration[i]) else False,
                prolgbt=True if (np.random.rand() <= lgbt[i]) else False,
                proWar=True if (np.random.rand() <= wars[i]) else False,
            ).tojson()
    return retval


def policyGen(count=3000, seed=1234, data=False, translator=False, previous=None):
    #     np.random.seed(seed)
    if translator:
        if previous == None:
            print("No previous data")
        else:
            retval = previous
    else:
        retval = []
        for i in range(count):
            retval.append(policy.random(name="law_" + str(i)))
    if not data:
        return retval
    data = np.zeros((count, 13))
    for i in range(count):
        data[i, :] = retval[i].toDatum()
    return data


def publicOpinion(population, policies):
    totals = np.zeros(len(policies))
    for p in range(len(policies)):
        total = 0.0
        for k in population.keys():
            total += election.quickAgent(population[k]).proCon(policies[p])
        totals[p] = total
    return totals/len(population.keys())
