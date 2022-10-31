# Тут метод чтения файла

def get_data(src, separator):

    dicts_from_file = []
    contents = ["id", "Name", "Phone number", "coments"]
    with open(src, "r", encoding="utf=8") as file:

        for line in file:
            dicts_from_file.append(dict(zip(contents, line.split(separator))))

    return dicts_from_file
