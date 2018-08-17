'''
TODO:
- Different tax rates
- Tax dispersion calculation
- Loophole integration
'''

class taxes:
    def __init__(self,effectedRanges,initDate,returnOnInvestment):
        self.effectedRanges = effectedRanges
        self.initDate = initDate
        self.returnOnInvestment = returnOnInvestment