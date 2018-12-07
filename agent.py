import numpy as np
from policy import Policy


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
        disposableIncome=0,
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
        self.disposableIncome = disposableIncome

    def proCon(self, policy, real=True, verbose=False):
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
        if policy.entitlement != ():
            brackets = len(policy.entitlement)
            dtax += policy.entitlement[int(self.income / (1.0 / brackets))]
        racism = (
            sum([(self.race[k] - policy.racism[k]) for k in self.race.keys()]) / 6.0
        )
        war = policy.war * -1.0
        war /= 1.0 if policy.offensive else 2.0

        opinion = sum([dtax, imm, lgbt, gowar, racism, war]) / 6.0
        if verbose:
            print(dtax, imm, lgbt, gowar, racism, war)
        return (-1 * opinion) if real else (opinion <= 0.0)

    def optimal(self, taxes=(), entitlement=(), militaristic=False):
        return Policy(
            self.name + "_optimal",
            taxes,
            self.proImm,
            self.prolgbt,
            self.proWar,
            entitlement,
            (
                self.race["white"],
                self.race["black"],
                self.race["amind"],
                self.race["asian"],
                self.race["hawaii"],
                self.race["other"],
            ),
            self.proWar,
            militaristic,
        )

    def tojson(self):
        return {
            "name": self.name,
            "income": self.income,
            "gullibility": self.gullibility,
            "politician": self.politician,
            "proImm": self.proImm,
            "prolgbt": self.prolgbt,
            "proWar": self.proWar,
            "race": self.race,
            "disposableIncome": self.disposableIncome,
        }
