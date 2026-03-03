from django.http import HttpResponse

def about_page(request):
    html_content = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Меню - Уютная кофейня</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #faf3e0;  /* Нежный кремовый */
            color: #5e4b3c;  /* Мягкий коричневый */
            line-height: 1.6;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        header {
            background-color: #ffe4e1;  /* Нежно-розовый */
            padding: 30px 0;
            border-radius: 0 0 30px 30px;
            box-shadow: 0 4px 15px rgba(233, 196, 176, 0.3);
            margin-bottom: 40px;
        }
        
        h1 {
            font-size: 2.5em;
            color: #8b6b4d;  /* Теплый коричневый */
            margin-bottom: 10px;
            text-align: center;
            font-weight: 300;
            letter-spacing: 2px;
        }
        
        .subtitle {
            text-align: center;
            color: #b1947a;  /* Бежевый */
            font-style: italic;
        }
        
        nav {
            background-color: #fff5ee;  /* Сливочный */
            padding: 15px;
            border-radius: 50px;
            margin: 20px 0;
            text-align: center;
        }
        
        nav a {
            color: #8b6b4d;
            text-decoration: none;
            margin: 0 25px;
            font-size: 1.2em;
            padding: 10px 20px;
            border-radius: 30px;
            transition: all 0.3s ease;
        }
        
        nav a:hover {
            background-color: #ffd9d4;  /* Светло-персиковый */
            color: #5e4b3c;
        }
        
        .menu-section {
            margin: 50px 0;
        }
        
        .menu-section h2 {
            color: #8b6b4d;
            font-size: 2em;
            font-weight: 300;
            margin-bottom: 30px;
            padding-bottom: 10px;
            border-bottom: 2px dashed #ffd9d4;
        }
        
        .menu-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 25px;
        }
        
        .menu-item {
            background-color: #fff9f0;
            border-radius: 25px;
            padding: 25px;
            display: flex;
            flex-direction: column;
            box-shadow: 0 4px 15px rgba(218, 184, 170, 0.1);
            transition: transform 0.3s ease;
            border: 1px solid #ffeae5;
        }
        
        .menu-item:hover {
            transform: translateY(-5px);
            background-color: #fff5f0;
            box-shadow: 0 6px 20px rgba(210, 180, 140, 0.2);
        }
        
        .menu-item-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
        }
        
        .menu-item h3 {
            color: #8b6b4d;
            font-size: 1.4em;
            font-weight: 400;
        }
        
        .price {
            background-color: #ffd9d4;
            color: #5e4b3c;
            padding: 5px 15px;
            border-radius: 30px;
            font-weight: bold;
            font-size: 1.1em;
        }
        
        .description {
            color: #a3876f;
            margin-bottom: 15px;
            font-size: 0.95em;
        }
        
        .ingredients {
            color: #b1947a;
            font-size: 0.9em;
            font-style: italic;
            margin-top: auto;
            border-top: 1px solid #ffe4e1;
            padding-top: 15px;
        }
        
        .special-badge {
            background-color: #e8d1c0;
            color: #5e4b3c;
            padding: 3px 12px;
            border-radius: 20px;
            font-size: 0.8em;
            margin-left: 10px;
        }
        
        footer {
            background-color: #ffe4e1;
            padding: 30px 0;
            border-radius: 30px 30px 0 0;
            margin-top: 60px;
            text-align: center;
            color: #8b6b4d;
        }
        
        .btn {
            display: inline-block;
            background-color: #ffd9d4;
            color: #5e4b3c;
            padding: 12px 35px;
            text-decoration: none;
            border-radius: 50px;
            font-size: 1.1em;
            transition: all 0.3s ease;
            border: 1px solid #ecc9c0;
        }
        
        .btn:hover {
            background-color: #ffc9c1;
            transform: scale(1.05);
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <h1>☕ Наше меню</h1>
            <p class="subtitle">Вдохновение в каждой чашке</p>
        </div>
    </header>
    
    <div class="container">
        <nav>
            <a href="/">Главная</a>
            <a href="about/">Меню</a>
        </nav>
        
        <section class="menu-section">
            <h2>Кофе</h2>
            <div class="menu-grid">
                <div class="menu-item">
                    <div class="menu-item-header">
                        <h3>Эспрессо</h3>
                        <span class="price">150₽</span>
                    </div>
                    <p class="description">Крепкий, насыщенный кофе для настоящих ценителей</p>
                    <p class="ingredients">30 мл чистой энергии</p>
                </div>
                
                <div class="menu-item">
                    <div class="menu-item-header">
                        <h3>Капучино</h3>
                        <span class="price">250₽</span>
                    </div>
                    <p class="description">Идеальный баланс эспрессо и молочной пенки</p>
                    <p class="ingredients">Эспрессо, молоко, нежная молочная пена</p>
                </div>
                
                <div class="menu-item">
                    <div class="menu-item-header">
                        <h3>Латте</h3>
                        <span class="price">270₽</span>
                    </div>
                    <p class="description">Мягкий молочный вкус с легким кофейным оттенком</p>
                    <p class="ingredients">Эспрессо, много молока, молочная пена</p>
                </div>
                
                <div class="menu-item">
                    <div class="menu-item-header">
                        <h3>Раф-кофе</h3>
                        <span class="price">290₽</span>
                        <span class="special-badge">Хит</span>
                    </div>
                    <p class="description">Нежный кофе со сливками и ванильным сиропом</p>
                    <p class="ingredients">Эспрессо, сливки, ванильный сироп</p>
                </div>
                
                <div class="menu-item">
                    <div class="menu-item-header">
                        <h3>Американо</h3>
                        <span class="price">170₽</span>
                    </div>
                    <p class="description">Классический черный кофе для тех, кто любит объем</p>
                    <p class="ingredients">Эспрессо, горячая вода</p>
                </div>
                
                <div class="menu-item">
                    <div class="menu-item-header">
                        <h3>Мокко</h3>
                        <span class="price">300₽</span>
                    </div>
                    <p class="description">Кофейно-шоколадное наслаждение</p>
                    <p class="ingredients">Эспрессо, шоколад, молоко</p>
                </div>
            </div>
        </section>
        
        <section class="menu-section">
            <h2>Десерты</h2>
            <div class="menu-grid">
                <div class="menu-item">
                    <div class="menu-item-header">
                        <h3>Чизкейк Нью-Йорк</h3>
                        <span class="price">320₽</span>
                    </div>
                    <p class="description">Нежный сливочный сыр на тонкой песочной основе</p>
                    <p class="ingredients">Сливочный сыр, песочное тесто, ягоды</p>
                </div>
                
                <div class="menu-item">
                    <div class="menu-item-header">
                        <h3>Морковный торт</h3>
                        <span class="price">280₽</span>
                    </div>
                    <p class="description">Влажный, ароматный, с орехами и кремом</p>
                    <p class="ingredients">Морковь, грецкие орехи, сливочный крем</p>
                </div>
                
                <div class="menu-item">
                    <div class="menu-item-header">
                        <h3>Эклер ванильный</h3>
                        <span class="price">180₽</span>
                    </div>
                    <p class="description">Заварное пирожное с нежным кремом</p>
                    <p class="ingredients">Заварное тесто, ванильный заварной крем</p>
                </div>
                
                <div class="menu-item">
                    <div class="menu-item-header">
                        <h3>Тирамису</h3>
                        <span class="price">350₽</span>
                        <span class="special-badge">Фирменное</span>
                    </div>
                    <p class="description">Итальянский десерт с маскарпоне и кофе</p>
                    <p class="ingredients">Маскарпоне, печенье савоярди, эспрессо</p>
                </div>
                
                <div class="menu-item">
                    <div class="menu-item-header">
                        <h3>Брауни</h3>
                        <span class="price">220₽</span>
                    </div>
                    <p class="description">Шоколадный пирог с орехами и жидкой сердцевиной</p>
                    <p class="ingredients">Темный шоколад, орехи, сливочное масло</p>
                </div>
                
                <div class="menu-item">
                    <div class="menu-item-header">
                        <h3>Круассан миндальный</h3>
                        <span class="price">210₽</span>
                    </div>
                    <p class="description">Хрустящая выпечка с миндальным кремом</p>
                    <p class="ingredients">Слоеное тесто, миндальный крем, сахарная пудра</p>
                </div>
            </div>
        </section>
        
        <section class="menu-section">
            <h2>Авторские напитки</h2>
            <div class="menu-grid">
                <div class="menu-item">
                    <div class="menu-item-header">
                        <h3>Лавандовый раф</h3>
                        <span class="price">320₽</span>
                    </div>
                    <p class="description">Нежный кофе с ароматом прованса</p>
                    <p class="ingredients">Эспрессо, сливки, лавандовый сироп</p>
                </div>
                
                <div class="menu-item">
                    <div class="menu-item-header">
                        <h3>Карамельный латте с солью</h3>
                        <span class="price">290₽</span>
                    </div>
                    <p class="description">Идеальный баланс сладкого и соленого</p>
                    <p class="ingredients">Эспрессо, молоко, карамель, морская соль</p>
                </div>
                
                <div class="menu-item">
                    <div class="menu-item-header">
                        <h3>Матча-латте</h3>
                        <span class="price">310₽</span>
                        <span class="special-badge">Новинка</span>
                    </div>
                    <p class="description">Японский зеленый чай с молоком</p>
                    <p class="ingredients">Пудра матча, молоко, сироп</p>
                </div>
            </div>
        </section>
        
        <div style="text-align: center; margin: 50px 0;">
            <p style="color: #b1947a; font-size: 1.2em;">Действует доставка от 500₽</p>
            <p style="color: #b1947a; margin-top: 10px;">"Ваш любимый кофе ждет вас"</p>
        </div>
    </div>
    
    <footer>
        <div class="container">
            <p>📍 ул. Кофейная, 15 | ☎ +7 (999) 123-45-67</p>
            <p style="margin-top: 15px; font-size: 0.9em;">© 2024 Уютная кофейня. Все права защищены</p>
        </div>
    </footer>
</body>
</html>
    """
    return HttpResponse(html_content)