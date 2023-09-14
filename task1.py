def read_csv(filename): # функция чтения файла
    phone_book= []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']

    with open(filename, 'r', encoding= 'utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.split(',')))
            phone_book.append(record)
            
    return phone_book


def write_csv(filename, phone_book): # фукция записи файла
    with open('phonebook.csv', 'w', encoding= 'utf-8') as phout:
        for i in range(len(phone_book)):
            s = ''
            for v in phone_book[i].values():
                s+= v +','
            phout.write(f'{s[:-1]}\n')

def show_menu(): # функция вывода на экран меню
    print(
        '1. Распечатать справочник',
        '2. Найти телефон по фамилии',
        '3. Изменить номер телефона',
        '4. Удалить запись',
        '5. Найти абонента по номеру телефона',
        '6. Добавить абонента в справочник',
        '7. Закончить работу', sep = "\n")
    choice = int(input('Введите номер вызываемой команды: '))
    return choice

def work_with_phonebook(): # основная фукция по работе с телефонным справочником
    choice = show_menu()
    phone_book = read_csv("phonebook.csv")
    while choice <=6:
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name = input('Введите фамилию абонента: ')
            print(find_last_name(phone_book, last_name))
        elif choice ==3:
            last_name = input('Введите фамилию абонента: ')
            new_number = input('Введите новый номер телефона: ')
            print(change_number(phone_book, last_name, new_number))
        elif choice == 4:
            last_name = input('Введите фамилию абонента: ')
            print(delete_last_name(phone_book, last_name))
        elif choice == 5:
            number = input('Введите номер телефона абонента: ')
            print(find_by_number(phone_book, number))
        elif choice == 6:
            user_data = input('Введите через запятую фамилию, имя, номер телефона и описание для нового абонента: ')
            print(add_user(phone_book, user_data))
            write_csv('phonebook.csv', phone_book)
        
        choice = show_menu()


# функция вывода на печать
def print_result(phone_book):
    for i in phone_book:
        print (i)
    return 
# функция нохождения номера телефона по фамилии
def find_last_name(phone_book, last_name):
    for item in phone_book:
        if item['Фамилия'] == last_name:
            return item['Телефон']
    return   
#функция замены номера
def change_number(phone_book, last_name, new_number):
    for item in phone_book:
        if item['Фамилия'] == last_name :
            item['Телефон'] = new_number
            return item['Телефон']
    return
# функция удаления абонента
def delete_last_name(phone_book, last_name):
    new_phone_book = []
    for item in phone_book:
        if item['Фамилия'] != last_name:
            new_phone_book.append(item)
    return new_phone_book
# функция находжения номера телефона по фамилии
def find_by_number(phone_book, number):
    for item in phone_book:
        if item['Телефон'] == number:
            return item['Фамилия']
    return
# функция добавления абонента
def add_user(phone_book, user_data):
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    new_record = dict(zip(fields, user_data.split(',')))
    phone_book.append(new_record)
    return phone_book

work_with_phonebook()







