from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'bcb7ffe0ac419a62db2c7c402745f997a848ba1f2088693bfe3f7b83a2ff230d'


@app.route('/')
def index():
    if 'num' not in session:
        session['num'] = random.randint(1,100)

    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    if 'attempts' not in session:
        session['attempts'] = 0
    session['attempts'] += 1
    session['guess'] = int(request.form['guess'])
    return redirect('/')

@app.route('/restart')
def restart_game():
    session.clear()
    return redirect('/')








if __name__ == '__main__':
    app.run(debug=True)