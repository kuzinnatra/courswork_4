from src.connection_api import HH
from src.json_class import GetJson


get_hh = HH()
my_vacancy = GetJson()
name_vacancies = input("""Здравствуйте!
Введите ключевые слова для поиска вакансий на сайте hh.ru (например название профессии):\n""")
if get_hh.get_vacancies(100, name_vacancies) == []:
    print('Желаемые вакансии не найдены')
else:
    vac = get_hh.get_vacancies(100, name_vacancies)
    my_vacancy.write_data(vac)
    vacanc = my_vacancy.get_vacancies()
    for i in vacanc:
        print(f'{i}\n')

    zp = int(input("Укажите желаемую зарплату и на экране останутся только подходящие вакансии\n"))
    for i in vacanc:
        if i.salary_from >= zp:
            print(f'{i}\n')

    top_vac = int(input('Сколько вакансий показать с самой большой зарплатой?\nВведите число:\n'))
    vacanc.sort(key=lambda vacanc: vacanc.salary_from, reverse=True) #сортируем список вакансий по з/п

    for i in range(0, top_vac):
        print(f'{vacanc[i]}\n')

    my_vacancy.delete_vacancy() #очищаем файл vacancies.json