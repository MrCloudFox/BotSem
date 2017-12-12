import config
import telebot
import infrastructure
import pymorphy2
import parse_message

connect = telebot.TeleBot(config.token)


@connect.message_handler(commands=['start'])
def start_message(message):
    connect.send_message(message.chat.id, "Привет! Напиши, что тебя интересует. Сейчас я могу подсказать тебе расписание."
                                          " Тебе нужно только попросить :)")
    config.dbman.set_state(message.chat.id, config.States.S_START.value)

@connect.message_handler(func = lambda message: config.dbman.get_current_state(message.chat.id) == config.States.S_START.value)
def simple_message(message):
    print(message.chat.id)
    parse_message.parser(message)
    #connect.send_message(message.chat.id, config.dbman.get_current_state(message.chat.id))
    #dbman.set_state(message.chat.id, config.States.S_START.value)

@connect.message_handler( func = lambda message: config.dbman.get_current_state(message.chat.id) == config.States.S_ENTER_GROUP.value)
def group_message(message):
    print(message.text)
    sample = config.dbman.simpleQuery("select subjectname from subjects")
        #config.dbman.simpleQuery("select su.subjectname, sc.numofauditorium, sc.lessonid, sc.numofweek from schedule sc, subjects su where sc.subjectid = su.id and groupid = (select id from groups where groupname = \'" + message.text + "\') order by sc.lessonid")
    for i in 10:
        print(' '.join(sample)[i])
    connect.send_message(message.chat.id, sample)



if __name__ == '__main__':
    connect.polling(none_stop=True)
    #print(dbman.selectFromDB("teachers", "where c_fullname = 'Vse budet COCA-COLA'")[0]["c_fullname"])
    #print(dbman.selectFromDB("teachers")[2]["c_fullname"])
    #print(dbman.selectFromDB("schedule", "where groupid = (select id from groups where groupname = \'" + group + "\') and nameofweekday = \'" + weekday + "\'"))
    #print(dbman.simpleQuery("select su.subjectname, sc.numofauditorium, sc.lessonid, sc.numofweek from schedule sc, subjects su where sc.subjectid = su.id and sc.nameofweekday = \'" + weekday + "\' and groupid = (select id from groups where groupname = \'" + group + "\') order by sc.lessonid"))
    #dbman.insertIntoDB("subjects", "Хранилища данных")