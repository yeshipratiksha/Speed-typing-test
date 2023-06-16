import time
import random
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "Programming is fun and challenging.",
        "Hello, World! Welcome to the speed typing test.",
        "This Flask Tutorial is the latest and comprehensive guide designed for beginners and professionals to learn Python Flask framework, which is one of the most popular Python-based web frameworks",
    ]
    sentence = random.choice(sentences)
    start_time = time.time()
    return render_template('typing.html', sentence=sentence, start_time=start_time)

@app.route('/result', methods=['POST'])
def result():
    end_time = time.time()
    elapsed_time = end_time - float(request.form['start_time'])
    user_input = request.form['user_input']
    num_characters = len(user_input)
    typing_speed = (num_characters / elapsed_time) * 60
    return render_template('result.html', elapsed_time=elapsed_time, num_characters=num_characters, typing_speed=typing_speed)

if __name__ == '__main__':
    app.run(debug=True)
