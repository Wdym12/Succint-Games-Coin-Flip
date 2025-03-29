from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/flip')
def flip():
    result = random.choice(['Heads', 'Tails'])
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True) 