from datetime import date
class Personne:
    
    personnage=0
    def __init__(self,nom,postNom,age):
        self.nom=nom
        self.postNom=postNom
        self.age=age
        if(self.__class__.__name__=='Garcon'):
            Garcon.personnage+=1
        elif(self.__class__.__name__=='Fille'):
            Fille.personnage+=1
        Personne.personnage+=1
    @staticmethod
    def mon_age(age):
        if(age>10):
            print("Tu es adulte")
        else:
            print("Tu as encore à apprendre")
#    def intro(cls,nom,yearr):
#        current_date=date.today()
#        return cls(nom,(current_date.year - yearr))

class Garcon(Personne):
    def __init__(self,nom,postNom,age):
        super().__init__(nom,postNom,age)


class Fille(Personne):
    def __init__(self, nom, postNom, age,surnom=''):
        
        super().__init__(nom, postNom, age)
        self.surnom=surnom


Garcon1=Garcon('Garcon','Fille',8)
Garcon1.mon_age(Garcon1.age)