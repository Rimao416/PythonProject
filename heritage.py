class SportTeam:
    fine_amount=150000
    def __init__(self,name,wins,losses):
        self.name=name
        self.wins=wins
        self.losses=losses
        self.total_fines=0
    @classmethod
    def from_string(cls,stats_as_string):
        data=stats_as_string.split('-')
        return cls(data[0],data[1],data[2])

    def get_fines(self):
        self.total_fines +=self.fine_amount
    def getName(self):
        return self.name
    def getWins(self):
        return self.wins
    def getLosses(self):
        return self.losses
    def stats(self):
        a=(self.getName()), " a comme victoire ",str((self.getWins())), " et comme défaite ",str((self.getLosses()))
        #phrase=''.join(a)
        return ''.join(a)
    @classmethod 
    def set_fine_amount(cls,amount):
        cls.fine_amount=amount


class EquipeBasketBall(SportTeam):
    fine_amount=5000
    def stats(self):
        return "L'équipe de BasketBall"+super().stats();
class EquipeFootBall(SportTeam):
    def __init__(self, name, wins, losses,draw=0):
        super().__init__(name, wins, losses)
    fine_amount=20000
    def stats(self):
        return "L'équipe de Football"+super().stats()
team1=EquipeBasketBall("WARRIOR",140,12)
team2=EquipeBasketBall("WARRIOR",140,12)
team3=EquipeBasketBall("WARRIOR",140,12)
team4=EquipeBasketBall("WARRIOR",140,12)
#FOOTBALL
barcelone3=EquipeFootBall("BARCELONE",14,12)
barcelone4=EquipeFootBall("BARCELONE",14,12)
#BOUSCIL
print(barcelone3.__dict__)