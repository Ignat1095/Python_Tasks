
import read
import write
import view

data = read.get_data("Tasks.py\Task_7\Phone_Book.csv", ";")


def last_id():
    id_last = [int(i["id"]) for i in data if i["id"].isdigit()]
    return str(max(id_last)+1)


def what_contact(what_find):
    # print(data_to_print)
    data_to_print = [i for i in data if what_find in i["Name"]]

    # print(data_to_print)
    return data_to_print


def main_logic():
    value = 0
    while value != 4:
        value = view.user_comand()

        if value == 1:
            what_find = view.find_contact()
            view.print_all_contacts(what_contact(what_find))

        elif value == 2:
            contact = view.create_contact()
            contact["id"] = last_id()
            data.append(contact)
            write.save_data(data, "Phone_Book.csv")

        elif value == 3:
            view.print_all_contacts(data)

        elif value == 4:
            print("Программа закрывается. ")
            break
        print("Вы выбрали {}-й пункт".format(value))
