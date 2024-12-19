import sqlite3

connection = sqlite3.connect("myydatabase.db")
# Создаем курсор для выполнения SQL-запросов
cursor = connection.cursor()

# Создаем таблицу "users"
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL
)
''')

# Создаем таблицу "clients"
cursor.execute('''
CREATE TABLE IF NOT EXISTS clients (
    id_client INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    phone_number TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);
''')

# Создаем таблицу "cars"
cursor.execute('''
CREATE TABLE IF NOT EXISTS cars (
    id_car INTEGER PRIMARY KEY AUTOINCREMENT,
    id_client INTEGER NOT NULL,
    brand_car TEXT NOT NULL,
    car_model TEXT NOT NULL,
    car_number TEXT NOT NULL UNIQUE,
    FOREIGN KEY (id_client) REFERENCES clients(id_client) ON DELETE CASCADE
);
''')

# Создаем таблицу "orders"
cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
    id_order INTEGER PRIMARY KEY AUTOINCREMENT,
    id_car INTEGER NOT NULL,
    id_user INTEGER,
    order_client TEXT NOT NULL,
    price DECIMAL(10,2),
    order_date DATE NOT NULL,
    FOREIGN KEY (id_car) REFERENCES cars(id_car) ON DELETE CASCADE,
    FOREIGN KEY (id_user) REFERENCES users(id_user) ON DELETE SET NULL
);
''')

#cursor.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
 #              ('kirill982', 'wertuew82', 'kirill@gmail.com'))

#cursor.execute("INSERT INTO clients (first_name, last_name, phone_number, email) VALUES (?, ?, ?, ?)",
 #              ('Carlos', 'Sainz', '563214545', 'Sainz@example.com'))

#cursor.execute("INSERT INTO cars (id_client, brand_car, car_model, car_number) VALUES (?, ?, ?, ?)",
 #              (2, 'Ferrari', 'La Ferrari', 'ABS124'))

#cursor.execute("INSERT INTO orders (id_car, id_user, order_client, price, order_date) VALUES (?, ?, ?, ?, ?)",
 #              (2, 2, 'общая диагностика', 3600.00, '2023-10-30'))


# Сохраняем изменения и закрываем соединение
connection.commit()

cursor.execute("SELECT * FROM users")
users = cursor.fetchall()
print("Users in the database:")
for user in users:
    print(user)

connection.close()
