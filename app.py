# app.py
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    # Потенциальная уязвимость: кривое преобразование данных от пользователя.
    # Это просто для демонстрации, Bandit может проверить и такие вещи.
    try:
        user_id = int(request.args.get('id', 1))
    except ValueError:
        user_id = 1
    return f'<h1>Hello, user #{user_id}!</h1>'


if __name__ == '__main__':
    app.run(debug=True)  # Уязвимость! Никогда не используйте debug=True в продакшене.
