from pony.orm import *

db = Database()


class Cash(db.Entity):
    uah = Optional(int, default=0)
    usd = Optional(int, default=0)
    eur = Optional(int, default=0)
    all = Optional(int, default=0)


db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
db.generate_mapping(create_tables=True)


RUN = False

with db_session:
    if not Cash.select().exists():
        Cash()
    Cash.select().show()


while RUN:
    print('run')
    command = input('Write a command: ')
    if command == 'add':

        pass
    elif command == 'delete':
        pass
    elif command == 'show':
        pass
    elif command == 'exit':
        RUN = False
        print('Goodbye')
    else:
        print('Incorrect command, print "exit" to finish the program')
