import json


class Person:
    customer_id = 1
    mydata = {}


    def __init__(self, name, surname, father_name, FIN, age, is_active):
        self.__name = name
        self.__surname = surname
        self.__father_name = father_name
        self.__Fin = FIN
        self.__age = age
        self.__is_active = is_active


    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_surname(self):
        return self.__surname
    
    def set_surname(self, surname):
        self.__surname = surname

    def get_father_name(self):
        return self.__father_name
    
    def set_father_name(self, father_name):
        self.__father_name = father_name

    def get_FIN(self):
        return self.__Fin
    
    def set_FIN(self, FIN):
        self.__Fin = FIN

    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        self.__age = age

    def get_is_active(self):
        return self.__is_active
    
    def set_is_active(self, is_active):
        self.__is_active = is_active


    def new_person(self):
        self.name = str(input('Name: '))
        self.surname = str(input('Surname: '))
        self.father_name = str(input('Father name: '))
        self._Fin = input('FIN: ')

        while True:
            # if len(self._Fin) > 7 or len(self._Fin) < 7:
            if len(self._Fin) != 7 or self._Fin.isdigit() or self._Fin.isalpha():
                print('Yanliş məlumat')
                self._Fin = input('FIN: ')
            else:
                break


        self.age = int(input('Age: '))

        while True:
            if self.age > 80 or self.age < 10:
                print('Yanliş məlumat')
                self.age = int(input('Age: '))
            else:
                break

        self.is_active = True


        self.mydata[self.customer_id] = {
            # 'id': self.customer_id,
            'name': self.name,
            'surname': self.surname,
            'father name': self.father_name,
            'fin': self._Fin,
            'age': self.age,
            'is_active': self.is_active,
        }

        self.customer_id +=1
        # print("Yeni musteri elave olundu.")


    def all_person(self, data):

        apply_filter = input("Filtr etmək istəyirsiniz? (y/n): ")

        if apply_filter.lower() == 'y':
            name_filter = input("İsim filtr etmək (boş buraxmaq üçün Enter'a basın): ")
            surname_filter = input("Soyad filtr etmək (boş buraxmaq üçün Enter'a basın): ")
            age_filter = input("Yaş filtr etmək (boş buraxmaq üçün Enter'a basın): ")
            
            # Filtr etmek.
            filtered_data = []
            for entry in data:
                if name_filter and entry['name'] != name_filter:
                    continue
                if surname_filter and entry['surname'] != surname_filter:
                    continue
                if age_filter and entry['age'] != int(age_filter):
                    continue
                if 'is_active' in entry and not entry['is_active']:
                    continue
                filtered_data.append(entry)
        else:
            # Butun datani getirme.
            filtered_data = [entry for entry in data if 'is_active' not in entry or entry['is_active']]
            # filtered_data = data

        print("Filtr edilmis datalar:")
        for entry in filtered_data:
            filtered_entry = {key: value for key, value in entry.items() if key != 'is_active'}
            print(filtered_entry)
            # print(entry)
            







        # with open('db_customer.json', 'r') as f:
        #     data_dict = json.load(f)

        # filter_option = input("Filtr etmək istəyirsiniz? (y/n): ")

        # if filter_option.lower() == "y":
        #     filter_field = input("Filtr  alanını daxil edin (name, surname, age): ")

        #     filtered_data = []
        #     if filter_field:
        #         for data in data_dict:
        #             if filter_field in data:
        #                 filtered_data.append(data[filter_field])
        #     else:
        #         filtered_data = data_dict

        #     for data in filtered_data:
        #         print(data)
        # else:
        #     for data in data_dict:
        #         print(data)



    def update_person(self):

        key = int(input('Id daxil edin: '))
        
        for item in self.mydata:
            if item['id'] == key:
                self.name = str(input('Name: '))
                self.surname = str(input('Surname: '))
                self.father_name = str(input('Father name: '))  
                self._Fin = input('FIN: ')

                while True:
                    # if len(self._Fin) > 7 or len(self._Fin) < 7:
                    if len(self._Fin) != 7 or self._Fin.isdigit() or self._Fin.isalpha():
                        print('Yanliş məlumat')
                        self._Fin = input('FIN: ')
                    else:
                        break

                self.age = int(input('Age: '))
                if self.age > 80 or self.age < 10:
                    print('Yanliş məlumat')
                    self.age = int(input('Age: '))

                self.is_active = True
                # self.is_active = bool(input('is_active: '))

                item['name'] = self.name
                item['surname'] = self.surname
                item['father_name'] = self.father_name
                item['FIN'] = self._Fin
                item['age'] = self.age
                item['is_active'] = self.is_active

                print('Guncellendi.')
                break

        else:
            print('Yanliş məlumat')

            

        # def update_person(self):
        #     key = int(input('Id daxil edin: '))

        #     if key in self.mydata:
        #         self.name = str(input('Name: '))
        #         self.surname = str(input('Surname: '))
        #         self.father_name = str(input('Father name: '))  
        #         self._Fin = int(input('FIN: '))
    
        #         self.age = int(input('Age: '))
        #         if self.age > 80 or self.age < 10:
        #             print('Yanliş məlumat')
        #             self.age = int(input('Age: '))

        #         self.is_active = True
        #         # self.is_active = bool(input('is_active: '))



        #         self.mydata[key] = {
        #             'name': self.name,
        #             'surname': self.surname,
        #             'father name': self.father_name,
        #             'fin': self._Fin,
        #             'age': self.age,
        #             'is_active': self.is_active,
        #         }
        #         print('Guncellendi.')

        #     else:
        #         print('Yanliş məlumat')


    def delete_person(self):
        key = int(input('Id daxil edin: '))

        for item in self.mydata:
            if item['id'] == key:
                item['is_active'] = False
                print('Silindi.')
                break
        else:
            print('Yanliş məlumat')


        # with open('db_customer.json', 'r') as f:
        #     self.mydata = json.load(f)

        # key = int(input('Id daxil edin: '))
        
        # for item in self.mydata:
        #     if item['id'] == key:

        # # if key in self.mydata:
        #         self.mydata[key]['is_active'] = False
        #         # self.is_active = False
        #         print('silindi')

        # else:
        #     print('Yanliş məlumat')
 