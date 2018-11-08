import numpy as np


class agent:
    def __init__(
        self,
        name,
        income,
        gullibility,
        politician=False,
        district=-1,
        proImm=False,
        prolgbt=False,
        proWar=False,
        race={
            "white": 0.0,
            "black": 0.0,
            "amind": 0.0,
            "asian": 0.0,
            "hawaii": 0.0,
            "other": 0.0,
        },
        disposable=0,
    ):
        self.name = name
        self.income = income
        self.gullibility = gullibility
        self.politician = politician
        self.district = district
        self.proImm = proImm
        self.prolgbt = prolgbt
        self.proWar = proWar
        self.race = race
        self.disposable = disposable

    def proCon(self, policy, real=True):
        if policy.taxes != ():
            brackets = len(policy.taxes)
            dtax = policy.taxes[int(self.income / (1.0 / brackets))]
        else:
            dtax = 0.0
        if policy.proImm != None:
            imm = ((self.proImm == policy.proImm) - 0.5) * -2.0
        else:
            imm = 0.0
        if policy.prolgbt != None:
            lgbt = ((self.prolgbt == policy.prolgbt) - 0.5) * -2.0
        else:
            lgbt = 0.0
        if policy.proWar != None:
            gowar = ((self.proWar == policy.proWar) - 0.5) * -2.0
        else:
            gowar = 0.0
        racism = sum([(self.race[k] - policy.race[k]) for k in self.race.keys()]) / 6.0
        war = policy.war * -1.0
        war /= 1.0 if policy.offensive else 2.0

        opinion = sum([dtax, imm, lgbt, gowar, racism, war]) / 6.0

        return opinion if real else (opinion <= 0.0)


testPolicy = {"taxIncrease": 0.04}

johnDoe = agent("John Doe", 30000, 0.5, 0.6, 0.2, False, False)

johnDoe.proCon(testPolicy, 0.3)

