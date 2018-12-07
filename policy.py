"""
TODO:
- Enforcement rates
- Popularity
- Framing/perception
"""
import time
import datetime
import numpy as np


class Policy:
    def __init__(
        self,
        name,
        taxes=(),
        proImm=None,
        prolgbt=None,
        proWar=None,
        entitlement=(),
        racism=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
        war=False,
        offensive=False,
    ):
        self.name = name
        self.taxes = taxes
        self.proImm = proImm
        self.prolgbt = prolgbt
        self.proWar = proWar
        self.entitlement = entitlement
        self.racism = {}
        self.racism["white"], self.racism["black"], self.racism["amind"], self.racism[
            "asian"
        ], self.racism["hawaii"], self.racism["other"] = racism
        self.war = war
        self.offensive = offensive

    def print(self):
        print("Policy:\t" + self.name)
        print("Taxes: \t" + str(self.taxes))
        print(
            "Social:\t" + str(100 * self.proImm + 10 * self.prolgbt + 1 * self.proWar)
        )
        print("Titles:\t" + str(self.entitlement))
        print("racism:\t" + str(self.racism))
        print("Waring:\t" + str(self.war))
        print("Monger:\t" + str(self.offensive))
    
    def toDatum(self):
        return [sum(self.taxes)/len(self.taxes),self.proImm*1,self.prolgbt*1,self.proWar*1,sum(self.entitlement)/len(self.entitlement),self.racism['white'],self.racism['black'],self.racism['amind'],self.racism['asian'],self.racism['hawaii'],self.racism['other'],self.war*1,self.offensive*1]


def random(name=-1, seed=1618):
    # np.random.seed(seed)
    if name == -1:
        name = datetime.datetime.fromtimestamp(time.time()).strftime(
            "%d/%m/%Y-%H:%M:%S"
        )
    return Policy(
        name,
        taxes=2 * (np.random.rand(np.random.randint(1, 7, size=1)[0]) - 0.5),
        proImm=(np.random.rand() >= 0.5),
        prolgbt=(np.random.rand() >= 0.5),
        proWar=(np.random.rand() >= 0.5),
        entitlement=0.2 * (np.random.rand(np.random.randint(1, 7, size=1)[0]) - 0.2),
        racism=np.random.rand(6),
        war=(np.random.rand() >= 0.95),
        offensive=(np.random.rand() >= 0.5),
    )
