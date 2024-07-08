from src.connection_api import HH
from src.json_class import GetJson


get_hh = HH()
my_vacancy = GetJson()
quantity_vacancies = input("Введите желаемое количество отображаемых вакансий от 1 до 100:\n")
name_vacancies = input("Введите ключевые слова для поиска (например название профессии):\n")
if int(quantity_vacancies) > 100:
    print("Превышено количество отображаемых вакансий (максимум 100)")
    exit()
if get_hh.get_vacancies(int(quantity_vacancies), name_vacancies) == []:
    print('Желаемые вакансии не найдены')
else:
    vac = get_hh.get_vacancies(int(quantity_vacancies), name_vacancies)
    my_vacancy.write_data(vac)
    vacanc = my_vacancy.get_vacancies()
    for i in vacanc:
        print(f'{i}\n')

    top_vac = int(input('Сколько вакансий показать с самой большой зарплатой?\nВведите число:\n'))

    vacanc.sort(key=lambda vacanc: vacanc.salary_from, reverse=True) #сортируем список вакансий по з/п

    for i in range(0, top_vac):
        print(f'{vacanc[i]}\n')

    my_vacancy.delete_vacancy() #очищаем файл vacancies.json