import json
from person import Person

class Customer(Person):


    def __init__(self, name, surname, father_name, FIN, age, is_active):
        super().__init__(name, surname, father_name, FIN, age, is_active)


    def new_customer(self):

        with open('db_customer.json', 'r') as f:
            data_dict = json.load(f)

        if not data_dict:
            data_dict = []

        self.new_person(self)

        data_dict.append({
            'id': len(data_dict) + 1,
            'name': self.name,
            'surname': self.surname,
            'father_name': self.father_name,
            'FIN': self._Fin,
            'age': self.age,
            'is_active': True
        })

        json_string = json.dumps(data_dict, indent=2)
        with open('db_customer.json', 'w') as f:
            f.write(json_string)

        print("Data db_customer.json ünvanında saxlanıldı")




        # with open('db_customer.json', 'r') as f:
        #     data_dict = json.load(f)

        # if not data_dict:
        #     data_dict = []

        # self.new_person(self)
        # data_dict.append(self.mydata)
        
        # json_string = json.dumps(data_dict, indent=2)
        # with open('db_customer.json', 'w') as f:
        #     f.write(json_string)


    def all_customer(self):
        with open('db_customer.json', 'r') as file:
            data_dict = json.load(file)

            # is_active true olanlari getir.

        self.all_person(self, data = data_dict)
                   

    def update_customer(self):
        with open('db_customer.json', 'r') as f:
            self.mydata = json.load(f)

        self.update_person(self)


        json_string = json.dumps(self.mydata, indent=2)
        with open('db_customer.json', 'w') as f:
            f.write(json_string)

        print("Data db_customer.json ünvanında saxlanıldı")



        # with open('db_customer.json', 'r') as f:
        #     json.loads(self.mydata)

        # self.update_person(self)


        # json_string = json.dumps(self.mydata, indent=2)
        # with open('db_customer.json', 'w') as f:
        #     f.write(json_string)


    def delete_customer(self):
        with open('db_customer.json', 'r') as f:
            self.mydata = json.load(f)
        
        self.delete_person(self)

        json_string = json.dumps(self.mydata, indent=2)
        with open('db_customer.json', 'w') as f:
            f.write(json_string) 


























# {
#   "customer": {
#     "1": {
#       "name": "John",
#       "age": 30
#     },
#     "2": {
#       "name": "Alice",
#       "age": 25
#     }
#   }
# }



    # customer_id = 1
    # db_customer = {}

    # # db_customer = {
    # #     1: {
    # #         'id': customer_id,
    # #         'name': 'Teymur',
    # #         'surname': 'Baxisev',
    # #         'father name': 'Zaur',
    # #         'fin': 415433,
    # #         'age': 24,
    # #         'is_active': True,
    # #         }
    # #     }

    # def __init__(self, name, surname, father_name, __FIN, age, is_active):
    #     super().__init__(name, surname, father_name, __FIN, age, is_active)


    # def new_Customer(self):
    #     self.name = str(input('Name: '))
    #     self.surname = str(input('Surname: '))
    #     self.father_name = str(input('Father name: '))
    #     self._Fin = int(input('FIN: '))

    #     self.age = int(input('Age: '))

    #     while True:
    #         if self.age > 80 or self.age < 10:
    #             print('Yanliş məlumat')
    #             self.age = int(input('Age: '))
    #         else:
    #             break

    #     self.is_active = True
    #     # self.customer_id += 1

    #     # new_customer = {
    #     #     'id': self.customer_id,
    #     #     'name': self.name,
    #     #     'surname': self.surname,
    #     #     'father name': self.father_name,
    #     #     'fin': self._Fin,
    #     #     'age': self.age,
    #     #     'is_active': self.is_active,
    #     # }
        
    #     # new_customer_id = max(self.db_customer.keys()) + 1

    #     # self.db_customer[new_customer_id] = new_customer


    #     self.db_customer[self.customer_id] = {
    #         'id': self.customer_id,
    #         'name': self.name,
    #         'surname': self.surname,
    #         'father name': self.father_name,
    #         'fin': self._Fin,
    #         'age': self.age,
    #         'is_active': self.is_active,
    #     }

    #     self.customer_id +=1
    #     print("Yeni musteri elave olundu.")



    # def all_Customer(self):

    #     filtering = input('Filter edilsin? ---> y/n:  ')

    #     if filtering == 'y':
    #         print('1/Name\n 2/Surname\n 3/Father_name\n 4/Age\n')

    #         customer_filter = input('Filteri secin: ')
    #         # car_filter = set(car_filter.split(','))
    #         customer_filter = [int(x) for x in customer_filter.split(",")]

    #         filtered_customers = self.db_customer.copy()
    #         ready_datas = []
    #         for customers in customer_filter:
    #             if customers == 1:
    #                 name_filter = input('Name: ')
    #                 filtered_customers = {self.customer_id: customers for self.customer_id, customers in filtered_customers.items() if customers['Name']  == name_filter}

    #             elif customers == 2:
    #                 surname_filter = input('Surname: ')
    #                 filtered_customers = {self.customer_id: customers for self.customer_id, customers in filtered_customers.items() if customers['Surname']  == surname_filter}


    #             elif customers == 3:
    #                 father_name_filter = input('Year: ')
    #                 filtered_customers = {self.customer_id: customers for self.customer_id, customers in filtered_customers.items() if customers['Father_name']  == father_name_filter}
    #             ready_datas.append(filtered_customers)


    #         for filtered_data in ready_datas:
    #             for customer_id, customer in filtered_data.items():
    #                 print("Customer ID:", customer_id)
    #                 for key, value in customer.items():
    #                     print(key + ":", value)
    #                 print()
                
        
    #     elif filtering == 'n':
    #          print(self.db_customer.values())
        
    #     else:
    #         print('Melumat yoxdur.')

















    #     # filtered_customer = []
    #     # filtering = input('Filter edilsin? ---> y/n:  ')
    #     # if filtering == 'y':
    #     #     print('1/Name\n 2/Surname\n 3/Father_name\n 4/Age\n')
    #     #     customer_filters = input('Filter etmek ucun reqem daxil edin:  ')

    #     #     # if customer_filters == 1:
    #     #     for customer in self.db_car:
    #     #         filtered_customer = []
    #     #         filtered_customer = self.db_customer
    #     #         if customer == 1:
    #     #             Name = input('Name: ')
    #     #             for customer in filtered_customer:
    #     #                 if customer["marka"] == Name:
    #     #                     filtered_customer.append(customer)





    #     # if self.db_customer == {}:
    #     #     print('Melumat yoxdur.\n')

    #     # else:
    #     #     print('Butun musteriler.\n')
    #     #     for key, value in self.db_customer.items():
    #     #         print(key, ':', value)

    #     #     for i in self.db_customer:
    #     #         print(self.db_customer[i])
    #     # print(self.db_customer)


    # def update_Customer(self):
    #     key = int(input('Id daxil edin: '))

    #     if key in self.db_customer:
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


    #         self.db_customer[key] = {
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


    # def delete_Customer(self):
        # key = int(input('Id daxil edin: '))

        # if key in self.db_customer:
        #     self.db_customer[key]['is_active'] = False
        #     # self.is_active = False
        #     print('silindi')

        # else:
        #     print('Yanliş məlumat')
