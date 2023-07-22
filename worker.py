from person import Person
import json
import sqlite3

class Worker(Person):
    db_car = "renr_a_car.db"


    def __init__(self, name, surname, father_name, FIN, age, position, is_active):
        super().__init__(name, surname, father_name, FIN, age, is_active)
        self.__position = position

    def get_position(self):
        return self.__position
    
    def set_position(self, position):
        self.__position = position

    
    def new_worker(self):
        self.new_person(self)
        self.position =  str(input('Position: '))

        self.conn = sqlite3.connect(self.db_car)
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS workers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                surname TEXT,
                father_name TEXT,
                fin TEXT,
                position TEXT,
                age INTEGER,
                is_active INTEGER  
            )
        """)

        self.cursor.execute("""
            INSERT INTO workers (name, surname, father_name, fin, position, age, is_active)
            VALUES(?, ?, ?, ?, ?, ?, ?)
        """, (self.name, self.surname, self.father_name, self._Fin, self.position, self.age, self.is_active))

        self.conn.commit()
        self.conn.close()

        print("Data db_car ünvanında saxlanıldı")








        # with open('db_worker.json', 'r') as f:
        #     data_dict = json.load(f)

        # if not data_dict:
        #     data_dict = []

        # self.new_person(self)

        # self.position =  str(input('Position: '))
        

        # data_dict.append({
        #     'id': len(data_dict) + 1,
        #     'name': self.name,
        #     'surname': self.surname,
        #     'father_name': self.father_name,
        #     'FIN': self._Fin,
        #     'age': self.age,
        #     'position': self.position,
        #     'is_active': True
        # })

        # json_string = json.dumps(data_dict, indent=2)
        # with open('db_worker.json', 'w') as f:
        #     f.write(json_string)

        # print("Data db_worker.json ünvanında saxlanıldı")


    def all_worker(self):
        self.conn = sqlite3.connect(self.db_car)
        self.cursor = self.conn.cursor()

        self.cursor.execute("SELECT * FROM workers")
        rows = self.cursor.fetchall()

        data = [{'name': row[1], 'surname': row[2], 'father_name': row[3], 'FIN': row[4], 'position': row[5], 'age': row[6], 'is_active': bool(row[7])} for row in rows]

        filtered_data = self.all_person(self, data)

        print("Filtr edilmis datalar:")
        for entry in filtered_data:
            filtered_entry = {key: value for key, value in entry.items() if key != 'is_active'}
            print(filtered_entry)
        
        self.conn.close()











        # with open('db_worker.json', 'r') as file:
        #     data_dict = json.load(file)

        # apply_filter = input("Filtr etmək istəyirsiniz? (y/n): ")

        # if apply_filter.lower() == 'y':

        #     name_filter = input("İsim filtr etmək (boş buraxmaq üçün Enter'a basın): ")
        #     surname_filter = input("Soyad filtr etmək (boş buraxmaq üçün Enter'a basın): ")
        #     age_filter = input("Yaş filtr etmək (boş buraxmaq üçün Enter'a basın): ")

        #     position_filter = input("Position filtr etmək (boş buraxmaq üçün Enter'a basın): ")

        #     filtered_data = []
        #     for entry in data_dict:
        #         if name_filter and entry.get('name') != name_filter:
        #             continue
        #         if surname_filter and entry.get('surname') != surname_filter:
        #             continue
        #         if age_filter and entry.get('age') != int(age_filter):
        #             continue
        #         if position_filter and entry.get('position') != position_filter:
        #             continue
        #         filtered_data.append(entry)

        # else:
        #     filtered_data = [entry for entry in data_dict if 'is_active' not in entry or entry['is_active']]

        # print("Filtr edilmiş işçi dataları:")
        # for entry in filtered_data:
        #     filtered_entry = {key: value for key, value in entry.items() if key != 'is_active'}
        #     print(filtered_entry)
            # print(entry)













        # with open('db_worker.json', 'r') as file:
        #     data_dict = json.load(file)

        # self.all_person(self, data = data_dict)

        # position_filter = input("Position filtr etmək (boş buraxmaq üçün Enter'a basın): ")

        # filtered_data = []
        # for entry in data_dict:
        #     if position_filter and entry.get('position') != position_filter:
        #         continue
        #     filtered_data.append(entry)

        # print("Filtr edilmis işçi dataları:")
        # for entry in filtered_data:
        #     print(entry)

        #     # Position elave etmek.

        
    

    def update_worker(self):
        self.conn = sqlite3.connect(self.db_car)
        self.cursor = self.conn.cursor()

        key = int(input('Id daxil edin: '))


        self.name = str(input('Name: '))
        self.surname = str(input('Surname: '))
        self.father_name = str(input('Father name: '))  
        self._Fin = input('FIN: ')

        while True:
            if len(self._Fin) != 7 or self._Fin.isdigit() or self._Fin.isalpha():
                print('Yanliş məlumat')
                self._Fin = input('FIN: ')
            else:
                break

        self.__position = input('Position: ')
        

        self.age = int(input('Age: '))
        while True:
            if self.age > 80 or self.age < 10:
                print('Yanliş məlumat')
                self.age = int(input('Age: '))
            else:
                break

        self.is_active = True

        self.cursor.execute("""
            UPDATE workers
            SET name=?, surname=?, father_name=?, FIN=?, age=?, position=?, is_active=?
            WHERE id=?
        """, (self.name, self.surname, self.father_name, self._Fin, self.age, self.__position, self.is_active, key))

        self.conn.commit()
        self.conn.close()

        print('Güncellendi.')








        # with open('db_worker.json', 'r') as f:
        #     self.mydata = json.load(f)
        
        # key = int(input('Id daxil edin: '))
        
        # for item in self.mydata:
        #     if item['id'] == key:
        #         self.name = str(input('Name: '))
        #         self.surname = str(input('Surname: '))
        #         self.father_name = str(input('Father name: '))  
        #         self._Fin = input('FIN: ')

        #         while True:
        #             # if len(self._Fin) > 7 or len(self._Fin) < 7:
        #             if len(self._Fin) != 7 or self._Fin.isdigit() or self._Fin.isalpha():
        #                 print('Yanliş məlumat')
        #                 self._Fin = input('FIN: ')
        #             else:
        #                 break

        #         self.__position = input('Position: ')

        #         self.age = int(input('Age: '))
        #         if self.age > 80 or self.age < 10:
        #             print('Yanliş məlumat')
        #             self.age = int(input('Age: '))

        #         self.is_active = True
        #         # self.is_active = bool(input('is_active: '))

        #         item['name'] = self.name
        #         item['surname'] = self.surname
        #         item['father_name'] = self.father_name
        #         item['FIN'] = self._Fin
        #         item['age'] = self.age
        #         item['position'] = self.__position
        #         item['is_active'] = self.is_active

        #         print('Guncellendi.')
        #         break

        # else:
        #     print('Yanliş məlumat')


        # json_string = json.dumps(self.mydata, indent=2)
        # with open('db_worker.json', 'w') as f:
        #     f.write(json_string)

        # print("Data db_worker.json ünvanında saxlanıldı")


    def delete_worker(self):
        key = int(input('Id daxil edin: '))
        self.delete_person(self, 'workers', key)



        # with open('db_worker.json', 'r') as f:
        #     self.mydata = json.load(f)

        # self.delete_person(self)

        # json_string = json.dumps(self.mydata, indent=2)
        # with open('db_worker.json', 'w') as f:
        #     f.write(json_string) 

