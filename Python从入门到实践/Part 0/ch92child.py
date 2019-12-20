from  ch92Car import Car
from  ch92battery import Battery

class ElectricCar(Car):
    "电动车"

    def __init__(self, make, model, year):
        "初始化父类的属性，再初始化电动车"
        super().__init__(make, model, year)
        self.battery = Battery(85) # Battery实例用作ElectricCar类的一个属性

