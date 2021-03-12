class SportTeam:
    fine_amount=150000
    NombreEquipeCree=0
    def __init__(self,namee,wins,losses):
        self.namee=namee
        self.wins=wins
        self.losses=losses
        self.total_fines=0
        if self.__class__.__name__=='EquipeBasketBall':
            EquipeBasketBall.NombreEquipeCree+=1
        elif self.__class__.__name__=='EquipeFootBall':
            EquipeFootBall.NombreEquipeCree+=1
#        self.__class__.NombreEquipeCree+=1       
 #       SportTeam.NombreEquipeCree+=1    
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
    NombreEquipeCree=0
    def stats(self):
        return "L'équipe de BasketBall"+super().stats();
class EquipeFootBall(SportTeam):
    NombreEquipeCree=0
    def stats(self):
        return "L'équipe de Football"+super().stats()
class EquipeBousCill(SportTeam):
    NombreEquipeCree=0
    def stats(self):
        return "L'équipe de Bouscile"+super().stats()
team1=EquipeBasketBall("WARRIOR",140,12)
team2=EquipeBasketBall("WARRIOR",140,12)
team3=EquipeBasketBall("WARRIOR",140,12)
team4=EquipeBasketBall("WARRIOR",140,12)
#FOOTBALL
barcelone3=EquipeFootBall("BARCELONE",14,12)
barcelone4=EquipeFootBall("BARCELONE",14,12)
#BOUSCIL
bousc1=EquipeBousCill("SERGE",100,120)
bousc2=EquipeBousCill("SERGE",100,120)
bousc3=EquipeBousCill("SERGE",100,120)
print(EquipeBasketBall.__dict__)
print(EquipeBousCill.__dict__)
print(EquipeFootBall.__dict__)
print(EquipeFootBall.NombreEquipeCree)