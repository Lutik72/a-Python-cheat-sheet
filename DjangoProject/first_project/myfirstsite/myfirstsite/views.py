from django.http import HttpResponse

def index_page(request):
    html_content = """
    <!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Уютная кофейня</title>
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
        
        .hero {
            background-color: #fff0e7;  /* Нежный персиковый */
            border-radius: 30px;
            padding: 60px 40px;
            margin: 40px 0;
            text-align: center;
            box-shadow: 0 6px 20px rgba(210, 180, 140, 0.2);
        }
        
        .hero h2 {
            font-size: 2em;
            color: #8b6b4d;
            margin-bottom: 20px;
            font-weight: 300;
        }
        
        .hero p {
            font-size: 1.2em;
            max-width: 800px;
            margin: 0 auto 30px;
            color: #7a5c44;
        }
        
        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 30px;
            margin: 50px 0;
        }
        
        .feature-card {
            background-color: #fff9f0;  /* Кремовый */
            padding: 30px 20px;
            border-radius: 25px;
            text-align: center;
            box-shadow: 0 4px 15px rgba(218, 184, 170, 0.2);
            transition: transform 0.3s ease;
        }
        
        .feature-card:hover {
            transform: translateY(-5px);
            background-color: #ffeae5;
        }
        
        .feature-card h3 {
            color: #8b6b4d;
            margin-bottom: 15px;
            font-size: 1.5em;
            font-weight: 400;
        }
        
        .feature-card p {
            color: #a3876f;
        }
        
        .feature-icon {
            font-size: 3em;
            margin-bottom: 15px;
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
            <h1>☕ Уютная кофейня</h1>
            <p class="subtitle">Место, где время останавливается ради чашки кофе</p>
        </div>
    </header>
    
    <div class="container">
        <nav>
            <a href="/">Главная</a>
            <a href="about/">Меню</a>
        </nav>
        
        <div class="hero">
            <h2>Добро пожаловать в нашу кофейню</h2>
            <p>Мы создаем атмосферу уюта и варим самый вкусный кофе в городе. 
               Здесь вы можете отдохнуть от суеты, поработать в спокойной обстановке 
               или встретиться с друзьями.</p>
            <a href="menu.html" class="btn">Посмотреть меню</a>
        </div>
        
        <div class="features">
            <div class="feature-card">
                <div class="feature-icon">🌿</div>
                <h3>Свежая обжарка</h3>
                <p>Мы обжариваем зерна каждое утро для насыщенного вкуса</p>
            </div>
            
            <div class="feature-card">
                <div class="feature-icon">🍰</div>
                <h3>Домашняя выпечка</h3>
                <p>Нежные десерты и пирожные от нашего кондитера</p>
            </div>
            
            <div class="feature-card">
                <div class="feature-icon">📚</div>
                <h3>Уютная атмосфера</h3>
                <p>Мягкие кресла, книги и живая музыка по вечерам</p>
            </div>
            
            <div class="feature-card">
                <div class="feature-icon">🎵</div>
                <h3>Wi-Fi и музыка</h3>
                <p>Идеальное место для работы и отдыха</p>
            </div>
        </div>
        
        <div style="text-align: center; margin: 40px 0;">
            <p style="color: #b1947a; font-size: 1.2em;">Ждем вас ежедневно с 8:00 до 22:00</p>
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