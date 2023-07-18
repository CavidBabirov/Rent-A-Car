from datetime import MAXYEAR, MINYEAR
import json

class Car:
    mydata = {}
    car_id = 1

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

        with open('db_car.json', 'r') as f:
            data_dict = json.load(f)

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

        self.mydata[self.car_id] = {
            # id elave et.
            'id': self.car_id,
            'Marka': self.marka,
            'Model': self.model,
            'Max Speed': self.max_speed,
            'Year': self.year,
            'Horse Power': self.horse_power,
        }

        self.car_id +=1
        print('Yeni avtomobil elave olundu.\n')

        if not data_dict:
            data_dict = []

        data_dict.append({
            'id': len(data_dict) + 1,
            'Marka': self.marka,
            'Model': self.model,
            'Max Speed': self.max_speed,
            'Year': self.year,
            'Horse Power': self.horse_power,
        })

        json_string = json.dumps(data_dict, indent=2)
        with open('db_car.json', 'w') as f:
            f.write(json_string)

        print("Data db_car.json ünvanında saxlanıldı")


    def all_Car(self):
        with open('db_car.json', 'r') as file:
            data_dict = json.load(file)


        apply_filter = input("Filtr etmək istəyirsiniz? (y/n): ")

        if apply_filter.lower() == 'y':
            marka_filter = input("Marka filtr etmək (boş buraxmaq üçün Enter'a basın): ")
            model_filter = input("Model filtr etmək (boş buraxmaq üçün Enter'a basın): ")
            year_filter = input("Year filtr etmək (boş buraxmaq üçün Enter'a basın): ")
            
            # Filtr etmek.
            filtered_data = []
            for entry in data_dict:
                if marka_filter and entry['Marka'] != marka_filter:
                    continue
                if model_filter and entry['Model'] != model_filter:
                    continue
                if year_filter and entry['Year'] != int(year_filter):
                    continue
                filtered_data.append(entry)
        else:
            # Butun datani getirme.
            filtered_data = data_dict

        print("Filtr edilmis datalar:")
        for entry in filtered_data:
            print(entry)


    def update_Car(self):
        with open('db_car.json', 'r') as f:
            self.mydata = json.load(f)


        key = int(input('Id daxil edin: '))

        for item in self.mydata:
            if item['id'] == key:
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

                item['Marka'] = self.marka
                item['Model'] = self.model
                item['Max Speed'] = self.max_speed
                item['Year'] = self.year
                item['Horse Power'] = self.horse_power

                print('Guncellendi.')
                break

        else:
            print('Yanliş məlumat')


        json_string = json.dumps(self.mydata, indent=2)
        with open('db_car.json', 'w') as f:
            f.write(json_string)

        print("Data db_car.json ünvanında saxlanıldı")


    def delete_Car(self):

        with open('db_car.json', 'r') as f:
            self.mydata = json.load(f)
        
        key = int(input('Id daxil edin: '))

        deleted = False
        for i, item in enumerate(self.mydata):
            if item['id'] == key:
                self.mydata.pop(i)
                deleted = True
                print('Silindi.')
                break

        if deleted:
            # Silinen masinin id'sini bir sonraki masina elave etmek.
            for i in range(i, len(self.mydata)):
                self.mydata[i]['id'] -= 1

            json_string = json.dumps(self.mydata, indent=2)
            with open('db_car.json', 'w') as f:
                f.write(json_string)
        else:
            print('Yanliş məlumat')

        print("Data db_car.json ünvanında saxlanıldı")



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



        