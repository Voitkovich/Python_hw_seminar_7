def add_contact():
    
    contact = []

    name = input('Введите имя: ')
    contact.append(name.title())

    sirname = input('Введите фамилию: ')
    contact.append(sirname.title())

    phone_number = input('Введите номер телефона: ')
    contact.append(phone_number)

    comment = input('Коментарий: ')
    contact.append(comment.title())

    print('Абонент записан: ', contact)
    return contact