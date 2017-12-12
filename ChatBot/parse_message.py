import pymorphy2
import re
import telebot
import config
import bot

morph = pymorphy2.MorphAnalyzer()

def parser(message):
    str = message.text
    rFilter = re.compile(
        u"""[\'\.\,\!\"\№\;\%\:\?\@\$\^\*\&\(\)\_\+\…\#]""")  # регулярка для убийства знаков препинания
    str = rFilter.sub(' ', str)  # все препинание заменяем на пробелы
    str = ' '.join(str.split())
    str.lower()
    temp = str.split(' ')
    words = []
    for i in temp:
        word = morph.normal_forms(i)[0]
        words.append(word)

    if "расписание" in words:
        bot.connect.send_message(message.chat.id, "Введи свою группу в формате 'АБВ-123'")
        config.dbman.update_state(message.chat.id, config.States.S_ENTER_GROUP.value)