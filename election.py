'''
TODO: 
- Basic elections
- Differnet electoral systems
- Misscounts
'''

class election:
    def __init__(self,type,exclusivity,time,mailIn):
        self.type = type
        self.exclusivity = exclusivity
        self.time = time
        self.mailIn = mailIn