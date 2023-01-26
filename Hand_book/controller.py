import view as ac
import find as fc
import choice
import log

def button_click():
    button = choice.choice()
    if button == 1:
        print('Запись нового абонента')
        contact = ac.add_contact()
        log.log_to_file(contact)
        button_click()
    if button == 2:
        print('\nПоиск абонента\n')
        contact = fc.find()
        log.reading_file(contact)
        button_click()
    if button == 3:
        print('Просмотр всего справочника')
        log.reading_all()
        button_click()
    if button == 4:
        print('***До встречи!***')
        exit
    log.log(button)    