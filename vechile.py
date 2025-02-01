class Vechile:
    def _init_(self,model,color):
        def display_info(self):
            print("This is a vehicle.")

    def start_engine(self):
        print("Engine started.")

    def stop_engine(self):
        print("Engine stopped.")
class Car(Vechile):
    def _init_(self, model, color,year):
        super()._init_(model, color)
        self.model=model
        self.color=color
        self.year=year
    def showBMW(self):
        print(f" car model:{self.model} color:{self.color} manufactured in year{self.year}\n") 
    def display_car_info(self):
        print("This is a car.")

    def open_trunk(self):
        print("Trunk opened.")    
          
class Electricalcar(Car):
    def _init_(self, model, color,year):
        super()._init_(model, color,year)
        self.model=model
        self.color=color
        self.year=year
    def showFerari(self):
        print(f" car{self.model}, color:{self.color} manufactured in year{self.year}")  
    def display_electric_car_details(self):
        print("This is an electric car.")

    def charge_battery(self):
        print("Battery charging...")
ob=Electricalcar("ddgh","green",2022)                           
ob.showFerari()
print()
ob.display_electric_car_details()
ob.start_engine()
ob.stop_engine()
ob.showBMW()
ob.display_car_info()
ob.open_trunk()
ob.charge_battery()