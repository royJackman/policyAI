"""
TODO:
- Enforcement rates
- Popularity
- Framing/perception
"""


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
        self.racism["white"], self.racism["black"], self.racism["amind"], self.racism["asian"], self.racism["hawaii"], self.racism["other"] = racism
        self.war = war
        self.offensive = offensive
