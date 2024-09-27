import sqlite3 


conn = sqlite3.connect('magic_school.db') 
cursor = conn.cursor()

cursor.execute('''
          CREATE TABLE IF NOT EXISTS wizards (
             id INTEGER PRIMARY KEY AUTOINCREMENT, 
             first_name VARCHAR(20) ,
             last_name VARCHAR(20),
             age INTEGER,
             house VARCHAR(20) ,
             magic_level INTEGER ,
             special_ability VARCHAR(50) 
)''')

conn.commit()

def add_wizard(first_name, last_name, age, house, magic_level, special_ability):
    cursor.execute('''
                   INSERT INTO wizards (first_name , last_name, age , house , magic_level, special_ability)
                   VALUES (?, ?, ?, ?, ?, ?)''',
                (first_name, last_name, age, house, magic_level, special_ability))
    conn.commit() 
    
    
    
    
def find_wizard_by_ability(ability): 
    cursor.execute('SELECT * FROM wizards WHERE special_ability = ?', (ability,))
    result = cursor.fetchall() 
    for row in result:
        print(row)

def list_wizards_by_house(house):
    cursor.execute('SELECT * FROM wizards WHERE house = ?', (house, )) 
    result = cursor.fetchall()
    for row in result:
        print(row)

def update_magic_level(wizard_id, new_magic_level): 
    cursor.execute('UPDATE wizards SET magic_level = ? WHERE id = ?', (new_magic_level, wizard_id)) 
    conn.commit()

def delete_wizard(wizard_id): 
    cursor.execute('DELETE FROM wizards WHERE id = ?', (wizard_id, )) 
    conn.commit()

add_wizard('Гарри', 'Поттер', 15, 'Гриффиндор', 85, 'разговаривать со змеями')
add_wizard('Драко', 'Малфой', 16, 'Слизерин', 80, 'летать на метле')

find_wizard_by_ability('разговаривать со змеями')

list_wizards_by_house('Гриффиндор')

update_magic_level(1, 90)

delete_wizard(2)

conn.close()