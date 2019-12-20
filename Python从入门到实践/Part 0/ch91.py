class Car():
    def __init__(self, model, name , year):
        self.model = model
        self.name = name
        self.year = year
        self.licheng = 0

    def get_descriptive_name(self):
        print("我在" + str(self.year) + "年买了一辆" + self.model.title()
              + " "+ self.name.title() + "。")

    def read_licheng(self):
        print("这辆车走了" + str(self.licheng) + "米。")

    def increment_licheng(self, miles):
        if miles > 0:
            self.licheng += miles
        else:
            print("增加的里程不能是负值！")

class Battery():
    def __init__(self,battery_size=70):
        self.battery_size = battery_size
    def describe_battery(self):
       print("这辆车的电池是" + str(self.battery_size) + "伏的。")

class ElectricCar(Car):
    def __init__(self, model, name, year):
        super().__init__(model, name, year)
        self.battery = Battery()


