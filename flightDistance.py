from math import sin, cos, sqrt, atan2, radians

class FlightDistance:
    
    def __init__(self):
        
        self.cord1 = input("City 1: ")
        self.cord2 = input("City 2: ")
        
        
        self.lat1 = self.cord1.split(',')[0]
        self.lon1 = self.cord1.split(',')[1]

        self.lat2 = self.cord2.split(',')[0]
        self.lon2 = self.cord2.split(',')[1]

        if "S" in self.lat1:
            self.lat1 = -(float(self.lat1.split(' ')[0]))
        else:
            self.lat1 = float(self.lat1.split(' ')[0])

        if "S" in self.lat2:
            self.lat2 = -(float(self.lat2.split(' ')[0]))
        else:
            self.lat2 = float(self.lat2.split(' ')[0])

        if "E" in self.lon1:
            self.lon1 = -(float(self.lon1.split(' ')[1]))
        else:
            self.lon1 = float(self.lon1.split(' ')[1])

        if "E" in self.lon2:
            self.lon2 = -(float(self.lon2.split(' ')[1]))
        else:
            self.lon2 = float(self.lon2.split(' ')[1])
            
    def calculateDistance(self):
        
        R = 6373.0

        lat1 = radians(self.lat1)
        lon1 = radians(self.lon1)
        lat2 = radians(self.lat2)
        lon2 = radians(self.lon2)

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c
        
        print("City 1 and City 2 are {} km apart ".format(round(distance,2)))
        

if __name__ == "__main__":

    f1 = FlightDistance()

    f1.calculateDistance()