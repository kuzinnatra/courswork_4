from src.connection_api import HH



test1 = HH()

quantity_vacancies = input("введите желаемое количество отображаемых вакансий от 1 до 100\n")
name_vacancies = input("введите название желаемой профессии\n")
if int(quantity_vacancies) >100:
    print("вы указали желаемое число вакансий больше 100. Нужно указать от 1 до 100")
    exit()
if test1.get_vacancies(int(quantity_vacancies), name_vacancies) == []:
    print('Желаемые вакансии не найдены')
else:
    print(test1.get_vacancies(int(quantity_vacancies), name_vacancies))