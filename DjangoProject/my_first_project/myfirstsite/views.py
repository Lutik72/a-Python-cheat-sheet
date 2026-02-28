from django.http import HttpResponse


def simple_page(request):
    html_content = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Моя первая страница</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 40px;
                background-color: #f0f0f0;
                color: #333;
            }
            h1 {
                color: #0066cc;
            }
            .container {
                max-width: 800px;
                margin: 0 auto;
                background: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Добро пожаловать!</h1>
            <p>Это моя первая страница на Django.</p>

        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)