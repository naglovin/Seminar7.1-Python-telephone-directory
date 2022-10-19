def get_info ():
    info = []                                                                              # создаем лист и апендим в него данные
    last_name = input('Введите фамилию: ')
    info.append(last_name)
    first_name = input('Введите имя: ')
    info.append(first_name)
    phone_number = ''
    valid =False                                                                            # действительный номер 
    while not valid:
        try:
            phone_number = input('Введите номер телефона: ')
            if len(phone_number) != 11:
                print('В номере телефона должно быть 11 цифр.')                              # Проверка на на правильность написания номера
            else:
                phone_number = int(phone_number)
                valid = True
        except:                                                                          #except то ошибка
            print('Номер телефона должен состоять только из цифр.')
    info.append(phone_number)
    description = input('Введите описание: ')
    info.append(description)
    return info