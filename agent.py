class agent:
    def __init__(self,name,income,belief,gullibility,poliInterest,politician=False,immigrant=False):
        self.name = name
        self.income = income
        self.belief = belief
        self.gullibility = gullibility
        self.poliInterest = poliInterest
        self.politician = politician
        self.immigrant = immigrant
    
    def proCon(self,policy,truth=1.0):
        for ideal in policy:
            print(ideal)
    
testPolicy = {"taxIncrease":0.04}

johnDoe = agent("John Doe", 30000, 0.5, 0.6, 0.2, False, False)

johnDoe.proCon(testPolicy,0.3)