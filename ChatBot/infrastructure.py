import postgresql

class DBManager:

    def __init__(self, connectUrl):
        self.db = postgresql.open(connectUrl) # 'pq://postgres:postgres@localhost:5432/ChatBot'

    def simpleQuery(self, query):
        return self.db.query(query)

    def update_state(self, iduser, state):
        self.db.execute("update states set state = \'" + str(state) + "\' where idofuser = \'" + str(iduser) + "\'")
        #print("INSERT INTO states  VALUES (\'" + iduser + "\', \'" + value + "\')")

    def set_state(self, iduser, value):
        self.db.execute("INSERT INTO states VALUES (\'" + str(iduser) + "\', \'" + str(value) + "\')")
        #print("INSERT INTO states  VALUES (\'" + iduser + "\', \'" + value + "\')")

    def get_current_state(self, iduser):
        return self.db.query("SELECT * FROM STATES WHERE idofuser = \'" + str(iduser) + "\'")[0]["state"]

    def selectFromDB(self, table, conditions = None):
        # namesOfColumns = self.db.query(
        #    "select column_name from information_schema.columns where table_schema='public' and table_name = " + table)
        # strNamesOfColumns = ', '.join(namesOfColumns)

        if conditions is not None:
            #print("SELECT * FROM " + table + " " + conditions)
            response = self.db.query("SELECT * FROM " + table + " " + conditions)
        else:
            response = self.db.query("SELECT * FROM " + table)

        return response  # print(response[id]["nameOfColumn"].strip())



    def insertIntoDB(self, table, *values):
        if len(values) != 0:
            maxID = int(self.db.query("select max(id) from " + table)[0][0]) + 1
            insertedValues = "', '".join(values)
            insertedValues = str(maxID) + ",\'" + insertedValues + "\'"
            print("INSERT INTO " + table + " VALUES (" + insertedValues + ")")
            self.db.execute("INSERT INTO " + table + " VALUES (" + insertedValues + ")")