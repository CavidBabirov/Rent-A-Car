from car import Car
from customer import Customer
from worker import Worker

login = 'admin'
password = 'rac_444'

rlogin = str(input('Login: '))
if rlogin == login:
    rpassword = str(input('Password: '))
    if rpassword == password:
            while True:
                print('1 --> Yeni avtomobil')
                print('2 --> Butun avtomobiller')
                print('3 --> Avtomobil melumatlarini yenile')
                print('4 --> Avtomobil sil\n')

                print('5 ---> Yeni Musteri')
                print('6 ---> Butun musteriler')
                print('7 ---> Musteri melumatlarini yenile')
                print('8 ---> Musterini sil\n')

                print('9 ---> Yeni Isci')
                print('10 ---> Butun isciler')
                print('11 ---> Isci melumatlarini yenile')
                print('12 ---> Isci sil\n')

                print('0 ---> Exit\n')


                secim = int(input('Secim: '))
                if secim == 1:
                    Car.new_Car(Car)
                            
                elif secim == 2:
                    Car.all_Car(Car)

                elif secim == 3:
                    Car.update_Car(Car)

                elif secim == 4:
                    Car.delete_Car(Car)

                elif secim == 5:
                    Customer.new_customer(Customer)

                elif secim == 6:
                    Customer.all_customer(Customer)

                elif secim == 7:
                    Customer.update_customer(Customer)

                elif secim == 8:
                    Customer.delete_customer(Customer)

                elif secim == 9:
                    Worker.new_worker(Worker)
                            
                elif secim == 10:
                    Worker.all_worker(Worker)

                elif secim == 11:
                    Worker.update_worker(Worker)

                elif secim == 12:
                    Worker.delete_worker(Worker)

                elif secim == 0:
                    exit()

                else:
                    print('Yanliş məlumat')

    else:
        print('Yanliş məlumat')
else:
    print('Yanliş məlumat')

# car = Car()