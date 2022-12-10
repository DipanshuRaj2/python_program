# WAP THAT HAS A CLASS CARS TWO OBJECTS AND SET CAR 1 TO BE A RED CONVERTIBLE WITH PRICE
# RS 10 LAKH  AND NAME PUGO, AND CAR 2 TO BE A BLUE SEDAN NAMED MAVO WORTH RS6 LAKH. 
# DISPLAY THE DETAILS OF BOTH THE CARS. 



class cars:
    def __init__(self,name,color,price):
        self.name=name
        self.color=color
        self.price=price
car1 = cars('pugo','red',1000000)
car2= cars('Mavo','Blue',6000000)
print('details of car1:')
print('name is:',car1.name)
print('color is:',car1.color)
print('price is :',car1.price)
print('details of car2:')
print('name is:',car2.name)
print('color is:',car2.color)
print('price is :',car2.price)

     