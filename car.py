from datetime import MAXYEAR, MINYEAR
import json
import sqlite3

class Car:
    # mydata = {}
    # car_id = 1
    db_car = "renr_a_car.db"

    conn = sqlite3.connect(db_car)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cars (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            marka TEXT,
            model TEXT,
            max_speed INTEGER,
            year INTEGER,
            horse_power INTEGER
        )
    """)

    conn.commit()
    # conn.close()


    def __init__(self, marka, model, max_speed, year, horse_power):
        self.__marka = marka
        self.__model = model
        self.__max_speed = max_speed
        self.__year = year
        self.__horse_power = horse_power


    def get_marka(self):
        return self.__marka
    
    def set_marka(self, marka):
        self.__marka = marka

    def get_model(self):
        return self.__model
    
    def set_model(self, model):
        self.__model = model

    def get_max_speed(self):
        return self.__max_speed
    
    def set_max_speed(self, max_speed):
        self.__max_speed = max_speed

    def get_year(self):
        return self.__year
    
    def set_year(self, year):
        self.__year = year

    def get_horse_power(self):
        return self.__horse_power
    
    def set_horse_power(self, horse_power):
        self.__horse_power = horse_power
    


    def new_Car(self):

        # with open('db_car.json', 'r') as f:
        #     data_dict = json.load(f)

        self.conn = sqlite3.connect(self.db_car)
        self.cursor = self.conn.cursor()

        self.marka = str(input('Marka: '))
        self.model = input('Model: ')

        try:
            self.max_speed = int(input('Max Speed: '))
        except ValueError:
            print('Yalniz reqem daxil edin!\n')
            self.max_speed = int(input('Max Speed: '))

        while True:
            if self.max_speed > 300 or self.max_speed < 180:
                print('Yanliş məlumat')
                self.max_speed = int(input('Max Speed: '))
            else:
                break

        
        self.year = int(input('Year: '))
        while True:
            if self.year > 2023 or self.year < 1950:
                print('Yanliş məlumat')
                self.year = int(input('Year: '))

            else:
                break

        
        self.horse_power = int(input('Horse Power: '))
        while True:
            if self.horse_power > 1000 or self.horse_power < 50:
                print('Yanliş məlumat')
                self.horse_power = int(input('Horse Power: '))
            
            else:
                break


        self.cursor.execute("""
            INSERT INTO cars (marka, model, max_speed, year, horse_power)
            VALUES (?, ?, ?, ?, ?)
        """, (self.marka, self.model, self.max_speed, self.year, self.horse_power))

        self.conn.commit()
        self.conn.close()

        print("Data db_car ünvanında saxlanıldı")

        # self.mydata[self.car_id] = {
        #     # id elave et.
        #     'id': self.car_id,
        #     'Marka': self.marka,
        #     'Model': self.model,
        #     'Max Speed': self.max_speed,
        #     'Year': self.year,
        #     'Horse Power': self.horse_power,
        # }

        # self.car_id +=1
        # print('Yeni avtomobil elave olundu.\n')

        # if not data_dict:
        #     data_dict = []

        # data_dict.append({
        #     'id': len(data_dict) + 1,
        #     'Marka': self.marka,
        #     'Model': self.model,
        #     'Max Speed': self.max_speed,
        #     'Year': self.year,
        #     'Horse Power': self.horse_power,
        # })

        # json_string = json.dumps(data_dict, indent=2)
        # with open('db_car.json', 'w') as f:
        #     f.write(json_string)

        # print("Data db_car.json ünvanında saxlanıldı")


    def all_Car(self):
        # with open('db_car.json', 'r') as file:
        #     data_dict = json.load(file)

        self.conn = sqlite3.connect(self.db_car)
        self.cursor = self.conn.cursor()


        apply_filter = input("Filtr etmək istəyirsiniz? (y/n): ")

        if apply_filter.lower() == 'y':
            marka_filter = input("Marka filtr etmək (boş buraxmaq üçün Enter'a basın): ")
            model_filter = input("Model filtr etmək (boş buraxmaq üçün Enter'a basın): ")
            year_filter = input("Year filtr etmək (boş buraxmaq üçün Enter'a basın): ")

            query = "SELECT * FROM  cars WHERE 1=1"
            params = []

            if marka_filter:
                query += f" AND marka=?"
                params.append(marka_filter)

            if model_filter:
                query += f" AND model=?"
                params.append(model_filter)

            if year_filter:
                query += f" AND year=?"
                params.append(int(year_filter))

            self.cursor.execute(query, tuple(params))
            filtered_data = self.cursor.fetchall()

            print("Filtr edilmis datalar:")
            for entry in filtered_data:
                print(entry)
            
            # # Filtr etmek.
            # filtered_data = []
            # for entry in data_dict:
            #     if marka_filter and entry['Marka'] != marka_filter:
            #         continue
            #     if model_filter and entry['Model'] != model_filter:
            #         continue
            #     if year_filter and entry['Year'] != int(year_filter):
            #         continue
            #     filtered_data.append(entry)
        else:
            # Butun datani getirme.
            # filtered_data = data_dict
            self.cursor.execute("SELECT * FROM cars")
            filtered_data = self.cursor.fetchall()

            print("Butun datalar:")
            for entry in filtered_data:
                print(entry)

        self.conn.close()




    def update_Car(self):
        # with open('db_car.json', 'r') as f:
        #     self.mydata = json.load(f)

        self.conn = sqlite3.connect(self.db_car)
        self.cursor = self.conn.cursor()

        key = int(input('Id daxil edin: '))

        self.cursor.execute("SELECT * FROM cars WHERE id=?", (key,))
        car = self.cursor.fetchone()

        # for item in self.db_car:
        #     if item['id'] == key:
        if car:
            self.marka = str(input('Marka: '))
            self.model = input('Model: ')
            self.max_speed = int(input('Max Speed: '))

            if self.max_speed > 300 or self.max_speed < 180:
                print('Yanliş məlumat')
                self.max_speed = int(input('Max Speed: '))

            self.year = int(input('Year: '))

            if self.year > 2023 or self.year < 1950:
                print('Yanliş məlumat')
                self.year = int(input('Year: '))

        
            self.horse_power = int(input('Horse Power: '))

            if self.horse_power > 1000 or self.horse_power < 50:
                print('Yanliş məlumat')
                self.horse_power = int(input('Horse Power: '))


            self.cursor.execute("""
                UPDATE cars
                SET marka=?, model=?, max_speed=?, year=?, horse_power=?
                WHERE id=?
            """, (self.marka, self.model, self.max_speed, self.year, self.horse_power, key))


            self.conn.commit()
            self.conn.close()

            print(f'Masin (ID: {key}) guncellendi.')

            print("Data db_car ünvanında saxlanıldı")

                # item['Marka'] = self.marka
                # item['Model'] = self.model
                # item['Max Speed'] = self.max_speed
                # item['Year'] = self.year
                # item['Horse Power'] = self.horse_power

                # print('Guncellendi.')
                # break

        else:
            print('Yanliş məlumat')




        # json_string = json.dumps(self.mydata, indent=2)
        # with open('db_car.json', 'w') as f:
        #     f.write(json_string)

        


    def delete_Car(self):

        # with open('db_car.json', 'r') as f:
        #     self.mydata = json.load(f)

        self.conn = sqlite3.connect(self.db_car)
        self.cursor = self.conn.cursor()
        
        key = int(input('Id daxil edin: '))

        self.cursor.execute("SELECT * FROM cars WHERE id=?", (key,))
        car_delete = self.cursor.fetchone()


        if car_delete:
            self.cursor.execute("DELETE FROM cars WHERE id=?", (key,))
            self.conn.commit()
            self.conn.close()

            print(f"ID'si {key} olan masin silindi.")
            print("Data db_car ünvanında saxlanıldı")

        else:
            print('Yanliş məlumat')

        # deleted = False
        # for i, item in enumerate(self.mydata):
        #     if item['id'] == key:
        #         self.mydata.pop(i)
        #         deleted = True
        #         print('Silindi.')
        #         break

        # if deleted:
        #     # Silinen masinin id'sini bir sonraki masina elave etmek.
        #     for i in range(i, len(self.mydata)):
        #         self.mydata[i]['id'] -= 1

        #     json_string = json.dumps(self.mydata, indent=2)
        #     with open('db_car.json', 'w') as f:
        #         f.write(json_string)
        # else:
        #     print('Yanliş məlumat')

        



        # with open('db_car.json', 'r') as f:
        #     self.mydata = json.load(f)
        
        # key = int(input('Id daxil edin: '))

        # for item in self.mydata:
        #     if item['id'] == key:
        #         self.mydata.remove(item)
        #         print('Silindi.')
        #         break
        # else:
        #     print('Yanliş məlumat')

        # json_string = json.dumps(self.mydata, indent=2)
        # with open('db_car.json', 'w') as f:
        #     f.write(json_string) 



        