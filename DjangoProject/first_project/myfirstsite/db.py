import sqlite3

def create_menu_database():
    
    # Подключаемся к базе данных (файл создастся автоматически)
    conn = sqlite3.connect('coffee_shop_menu.db')
    cursor = conn.cursor()
    
    # Создаем таблицу категорий
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        description TEXT
    )
    ''')
    
    # Создаем таблицу позиций меню
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS menu_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        description TEXT,
        ingredients TEXT,
        price INTEGER NOT NULL,
        is_hit BOOLEAN DEFAULT 0,
        is_signature BOOLEAN DEFAULT 0,
        is_new BOOLEAN DEFAULT 0,
        FOREIGN KEY (category_id) REFERENCES categories (id)
    )
    ''')
    
    # Очищаем таблицы перед вставкой (чтобы избежать дубликатов)
    cursor.execute('DELETE FROM menu_items')
    cursor.execute('DELETE FROM categories')
    
    # Вставляем категории
    categories = [
        ('Кофе', 'Классические и авторские кофейные напитки'),
        ('Десерты', 'Сладкая выпечка и десерты ручной работы'),
        ('Авторские напитки', 'Уникальные напитки от наших бариста')
    ]
    
    cursor.executemany('INSERT INTO categories (name, description) VALUES (?, ?)', categories)
    
    # Получаем ID категорий для связей
    cursor.execute('SELECT id, name FROM categories')
    category_ids = {name: id for id, name in cursor.fetchall()}
    
    # Данные для вставки на основе HTML
    menu_data = [
        # Кофе
        (category_ids['Кофе'], 'Эспрессо', 'Крепкий, насыщенный кофе для настоящих ценителей', 
         '30 мл чистой энергии', 150, 0, 0, 0),
        (category_ids['Кофе'], 'Капучино', 'Идеальный баланс эспрессо и молочной пенки', 
         'Эспрессо, молоко, нежная молочная пена', 250, 0, 0, 0),
        (category_ids['Кофе'], 'Латте', 'Мягкий молочный вкус с легким кофейным оттенком', 
         'Эспрессо, много молока, молочная пена', 270, 0, 0, 0),
        (category_ids['Кофе'], 'Раф-кофе', 'Нежный кофе со сливками и ванильным сиропом', 
         'Эспрессо, сливки, ванильный сироп', 290, 1, 0, 0),
        (category_ids['Кофе'], 'Американо', 'Классический черный кофе для тех, кто любит объем', 
         'Эспрессо, горячая вода', 170, 0, 0, 0),
        (category_ids['Кофе'], 'Мокко', 'Кофейно-шоколадное наслаждение', 
         'Эспрессо, шоколад, молоко', 300, 0, 0, 0),
        
        # Десерты
        (category_ids['Десерты'], 'Чизкейк Нью-Йорк', 'Нежный сливочный сыр на тонкой песочной основе', 
         'Сливочный сыр, песочное тесто, ягоды', 320, 0, 0, 0),
        (category_ids['Десерты'], 'Морковный торт', 'Влажный, ароматный, с орехами и кремом', 
         'Морковь, грецкие орехи, сливочный крем', 280, 0, 0, 0),
        (category_ids['Десерты'], 'Эклер ванильный', 'Заварное пирожное с нежным кремом', 
         'Заварное тесто, ванильный заварной крем', 180, 0, 0, 0),
        (category_ids['Десерты'], 'Тирамису', 'Итальянский десерт с маскарпоне и кофе', 
         'Маскарпоне, печенье савоярди, эспрессо', 350, 0, 1, 0),
        (category_ids['Десерты'], 'Брауни', 'Шоколадный пирог с орехами и жидкой сердцевиной', 
         'Темный шоколад, орехи, сливочное масло', 220, 0, 0, 0),
        (category_ids['Десерты'], 'Круассан миндальный', 'Хрустящая выпечка с миндальным кремом', 
         'Слоеное тесто, миндальный крем, сахарная пудра', 210, 0, 0, 0),
        
        # Авторские напитки
        (category_ids['Авторские напитки'], 'Лавандовый раф', 'Нежный кофе с ароматом прованса', 
         'Эспрессо, сливки, лавандовый сироп', 320, 0, 0, 0),
        (category_ids['Авторские напитки'], 'Карамельный латте с солью', 'Идеальный баланс сладкого и соленого', 
         'Эспрессо, молоко, карамель, морская соль', 290, 0, 0, 0),
        (category_ids['Авторские напитки'], 'Матча-латте', 'Японский зеленый чай с молоком', 
         'Пудра матча, молоко, сироп', 310, 0, 0, 1)
    ]
    
    cursor.executemany('''
        INSERT INTO menu_items 
        (category_id, name, description, ingredients, price, is_hit, is_signature, is_new) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', menu_data)
    
    # Сохраняем изменения
    conn.commit()
    
    print("База данных успешно создана!")

    # Закрываем соединение
    conn.close()

create_menu_database()