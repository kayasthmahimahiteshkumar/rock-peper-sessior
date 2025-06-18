from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

choices = ['Rock', 'Paper', 'Scissors']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    user_choice = request.form['choice']
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a draw!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper') or \
         (user_choice == 'Paper' and computer_choice == 'Rock'):
        result = 'You win!'
    else:
        result = 'You lose!'

    return render_template('index.html', user_choice=user_choice, computer_choice=computer_choice, result=result)

if __name__ == '__main__':
    app.run(debug=True)