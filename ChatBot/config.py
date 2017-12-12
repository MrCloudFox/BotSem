from enum import Enum
import infrastructure

token = 'yourToken'
dbman = infrastructure.DBManager('pq://postgres:postgres@localhost:5432/ChatBot')

class States(Enum):
    S_START = "0"  # Начало нового диалога
    S_ENTER_GROUP = "1"
    S_ENTER_DAY = "2"