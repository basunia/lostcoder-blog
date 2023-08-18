class Persion:
    name = ''
    age = 0
    def __init__(self, persion_name, person_age) -> None:
        self.name = persion_name
        self.age = person_age
        
    def __str__(self) -> str:
        return f'Mahmud class'
    
    def showPersion(self) -> str:
        return f'name {self.name} age {self.age}'

p = Persion(persion_name='Mahmud', person_age=43)
print(p)
print(p.showPersion())