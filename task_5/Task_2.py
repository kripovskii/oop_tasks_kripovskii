import random

class Car():
    def __init__(self,color,coast,year_of_issue):
        self.color = color
        self.coast = coast
        self.year_of_issue = year_of_issue
    
    def Drive():
        print(f'Car is driving, engine makes {Car.Engine.ra_ta_ta()} ')
    
    @staticmethod
    def Break_down():
        if Car.Engine.condition + Car.Chassis.condition_func() == 1:
            return Car.Drive()
        else:
            print('Oh no, car is broken, needs repair!')

    
    class Engine(): 
        volume = 5
        type = 'V12'
        condition = random.randint(0,1)

        def ra_ta_ta():
            return 'RA-TA-TA-TA-TA'

    class Chassis():
        count_of_wheels = 4
        type = 'multi-link'
        condition = None
        
        def condition_func():

            if Car.Chassis.Front_suspension.get_condition() + Car.Chassis.Back_suspension.get_condition() % 2 == 0:
                Car.Chassis.condition = 1
                return Car.Chassis.condition
            else:
                Car.Chassis.condition = 0
                return Car.Chassis.condition
        
        class Front_suspension():
            count_of_wheels = 2
            producing_country ='Germany'

            def __condition_func():
                condition = random.randint(0,10)
                return condition
            
            def get_condition():
                return Car.Chassis.Front_suspension.__condition_func()
        
        class Back_suspension():
            count_of_wheels = 2
            producing_country ='Germany'
           
            def __condition_func():
                condition = random.randint(0,10)
                return condition
            
            def get_condition():
                return Car.Chassis.Back_suspension.__condition_func()



Car.Break_down()