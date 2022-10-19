def creating_file ():
    file = 'Phonebook.csv'                                                            # создаем файл с расширение ксв 
    with open (file, 'w', encoding = 'utf-8') as data:                                # открываем файл и записываем в него, стандарт кодирования 
        data.write(f'Фамилия;Имя;Номер телефона;Описание\n')

