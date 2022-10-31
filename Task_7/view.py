from tabulate import tabulate


def user_comand():
    number = int(input(

        "Выберите команду: \n 1. --> Найти контакт \n 2. --> Создать новый контакт \n 3. --> Показать все контакты \n 4. --> Закрыть программу \n"))
    if 0 < number < 5:
        return number
    else:
        print(input("Неверная команда! Повторите попытку "))

        return user_comand()


def find_contact():
    find_me = str(input("Введите имя контакта: ")).capitalize()
    return find_me


def create_contact():
    new_contact = {"id": ""}
    new_contact["name"] = input("Введите имя: ")
    new_contact["phone_number"] = input("Введите номер: ")
    new_contact["coments"] = input("Введите комментарий: ")

    print(new_contact)
    return new_contact
# print(create_contact())


def print_all_contacts(data):
    data_to_print = []

    for i in range(len(data)):
        listik = list(data[i].values())
        # listik.pop(0)
        data_to_print.append(listik)

    column_name = ["id", "Name", "Phone number", "coments"]
    # print(data_to_print)
    print(tabulate(data_to_print, headers=column_name,
          tablefmt="heavy_grid"))
