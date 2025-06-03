
sourse = 'C:/Users/Admin/PycharmProjects/Files_for_reading/codstelefone.txt'


def reading_file(file_dir) -> dict:
    list_numbers = []
    try:
        with open(file_dir, 'r', encoding="utf-8") as files:
            read_content = files.readlines()
            for line in read_content:
                # формуємо список списків
                list_numbers.append(line.replace('\n','').split("\t"))
        # dict_numbers = {item[0]: item[1:] for item in list_numbers} # also works
        # return {line.split("\t")[0]: line.split("\t")[1:] for line in read_content} # also works
        dict_numbers = dict(list_numbers) # зі списку списків робимо словник

    except FileNotFoundError:
        return {}

    return  dict_numbers


def find_country_by_code(code):
    cods = reading_file(sourse)
    if not cods.get(code): return 'Немає такого коду!'
    return cods.get(code)


def find_code_by_country(country):
    if not country:  # перевірка на пустий рядок
        return str('Введіть назву країни!')

    cods = reading_file(sourse)

    if not cods: return None # перевірка чи не пустий словник
    country = country.lower() # введений параметр до ниж регістру
    for code, name in cods.items():
        if country in name.lower(): return str(code)  # значення до ниж регістру
    return str('Такої країни, по ходу, немає!')


print(reading_file(sourse))

print(find_country_by_code('+94'))

print(find_code_by_country('австралія'))
print(find_code_by_country('Австралія'))
