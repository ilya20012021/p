import pymongo


db_client = pymongo.MongoClient("mongodb://localhost:27017/")


current_db = db_client["dbdbd"]



collection = current_db["messages"]

def send_message():
  pylounge = {
    'username': str(input('Введите имя пользователя:')),
    'text': str(input('Введите сообщение:'))
  }

  ins_result = collection.insert_one(pylounge)

  return ins_result

send_message()

