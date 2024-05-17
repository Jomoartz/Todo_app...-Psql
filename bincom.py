 #           ASSIGNENT 1: fibonacci sequence


def fibonacci_doubbler(initial_num, initial_incremnt):
    if type(initial_num) is not int:
        initial_num = 1
        initial_incremnt = initial_num + initial_num
    initial_result = initial_num + initial_incremnt
    fibonacci_series = [initial_num]

    while True:
        #increased initial_result by initial increase
        initial_result = initial_num + initial_incremnt
        new_result = initial_incremnt + initial_result
        #increased inital numbers fibonaci increment
        initial_num = initial_result
        initial_incremnt = new_result
        fibonacci_series.append(initial_result)
        fibonacci_series.append(new_result)
        if initial_result > 1500:
            break
        print(fibonacci_series)
        
#fibonacci doubler takes in two number and will form a fibonacci sequence with them.
#if a non interger is supplied, fibonacci increase by a default value of 1 and 2
fibonacci_doubbler(1, initial_incremnt = 2 )







#       ASSIGNMENT 2: PYTHON TODO_list




#create function to query data into the database  
import psycopg2


#  todo list using postgresql

def insert_todo(task, description):
    connection = None
    try:
        connection = psycopg2.connect(
            user = 'postgres',
            password = '0000',
            host = 'localhost',
            port = '5432',
            database = 'bincom'

        )

        cursor = connection.cursor()
        
        postgres_insert_query = '''INSERT INTO todo_list (title, descriptiom) VALUES (%s, %s)'''
        record_to_insert = (task, description)
        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print(count, 'records inserted successfully into todo_list table')

    except (Exception, psycopg2.Error) as error:
        print('failed to insert record', error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print('psql connection closed')


#create function to query data from database

def extract_todo():
    connection = psycopg2.connect(
        user = 'postgres',
        password = '0000',
        host = 'localhost',
        port = '5432',
        database = 'bincom'

    )

    cursor = connection.cursor()
    cursor.execute('SELECT title, descriptiom FROM todo_list')

    todo_items = cursor.fetchall()
    for tasks in todo_items:
        return tasks
    cursor.close
    connection.close




#create a function to create todo tasks and save to and extract from database using the above functions

#               manual for todo list


manual = '''
Commands: 
      create ----- To create todo item
      exit   ----- To exit todo list
      view   ----- To view todo items
      help   ----- To view manual
'''
command = 'help'
todo_list = []
todo_descrip = []

while command != 'exit':

 if command == 'create':
     todo_task = input('write your task here:  ')
     todo_description = input('describe your task:  ')
     todo_list.append(todo_task)
     todo_descrip.append(todo_description)
     insert_todo(todo_task, todo_description)
 
 elif command == 'view':
     print(extract_todo())
     
     if 10 > 20:
        for tasks in todo_list:
            for items in todo_descrip:
                extract_todo()
                print(f"""
                task: {tasks}
                description: {items}
                """)
 elif command == 'help':
     print(manual)

 command = input('command:  ')

