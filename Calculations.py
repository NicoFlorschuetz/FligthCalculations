#Zeit berechnen
#Treibstoffverbrauch berechnen
#von km in nm
#von km/h in kn
#von m in ft
import sqlite3

class FlightPath(object):
    def __init__(self, distance = 2, velocity = 2, height = 2):
        self.distance = distance
        self.velocity = velocity
        self.height = height

    def distanceCalcculator(self, eingabe, DirectionToConvert, Wert):

        if eingabe == "Entfernung":
            if DirectionToConvert == "Km":
                return round(Wert*0.54,3)
            elif DirectionToConvert == "Nm":
                return round(Wert/0.54,3)
        elif eingabe == "Geschwindigkeit":
            if DirectionToConvert == "Km/h":
                return round(Wert*0.54,3)
            elif DirectionToConvert == "Knoten":
                return round(Wert/0.54,3)
        elif eingabe == "Höhe":
            if DirectionToConvert == "m":
                return round(Wert/0.3048,3)
            elif DirectionToConvert == "ft":
                return round(Wert*0.3048,3)


class Aircraft(object):
    def __init__(self, ID):
        self.ID = ID
        self.newAircraft()




    def newAircraft(self):
        self.connection = sqlite3.connect("aircrafts.db")
        cursor = self.connection.cursor()
        sql_command = "CREATE TABLE IF NOT EXISTS planes(" "ID text)"
        cursor.execute(sql_command)
        sql_command = "INSERT INTO planes (ID) VALUES(?)"
        cursor.execute(sql_command, (self.ID,))
        self.connection.commit()
        self.connection.close()
