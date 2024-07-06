from src.connection_api import HH
from src.json_class import GetJson


get_hh = HH()
jsonfiletest = GetJson()
quantity_vacancies = input("введите желаемое количество отображаемых вакансий от 1 до 100\n")
name_vacancies = input("введите ключевые слова для поиска (например название профессии)\n")
if int(quantity_vacancies) > 100:
    print("Превышено количество отображаемых вакансий (максимум 100)")
    exit()
if get_hh.get_vacancies(int(quantity_vacancies), name_vacancies) == []:
    print('Желаемые вакансии не найдены')
else:
    vac = get_hh.get_vacancies(int(quantity_vacancies), name_vacancies)
    jsonfiletest.write_data(vac)
    vacanc = jsonfiletest.get_vacancies()
    for i in vacanc:
        print(f'{i}\n')
    jsonfiletest.delete_vacancy()

