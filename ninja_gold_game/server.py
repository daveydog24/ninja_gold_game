from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime
app = Flask(__name__)
app.secret_key = 'davidsninjagoldassingment'

@app.route('/')
def index():
    if 'gold_counter' not in session:
        session['gold_counter'] = 0
    if 'activity_log' not in session:
        session['activity_log'] = []
    print session['activity_log']

    return render_template('index.html', counter=session['gold_counter'], activity_log=session['activity_log'])

@app.route('/process_money', methods=['POST'])
def process_money():
    building = request.form['building']
    if 'gold_transfer' not in session:
        session['gold_transfer'] = 0
    if 'color_switch' in session:
        session.pop('color_switch')
        
    if building == 'farm':
        random_gold = random.randrange(10, 21)
        session['gold_transfer'] = random_gold
        session['activity_log'].append('Earned ' + str(session['gold_transfer']) + ' from the ' + building + ' (' + datetime.now().strftime('%Y/%m/%d %I:%M %p') + ')')
        session['color_switch'] = True
    elif building == 'cave':
        random_gold = random.randrange(5, 11)
        session['gold_transfer'] = random_gold
        session['activity_log'].append('Earned ' + str(session['gold_transfer']) + ' from the ' + building + ' (' + datetime.now().strftime('%Y/%m/%d %I:%M %p') + ')')
        session['color_switch'] = True
    elif building == 'house':
        random_gold = random.randrange(2, 6)
        session['gold_transfer'] = random_gold
        session['activity_log'].append('Earned ' + str(session['gold_transfer']) + ' from the ' + building + ' (' + datetime.now().strftime('%Y/%m/%d %I:%M %p') + ')')
        session['color_switch'] = True
    elif building == 'casino':
        random_gold = random.randrange(0, 51)
        random_test = random.randrange(0,2)
        if random_test == 1:
            session['gold_transfer'] = random_gold * -1
            session['activity_log'].append('Entered a casino and lost ' + str(session['gold_transfer'] * -1) + ' golds... Ouch.. ' +' (' + datetime.now().strftime('%Y/%m/%d %I:%M %p') + ')')
            session['color_switch'] = False

        else:
            session['gold_transfer'] = random_gold
            session['activity_log'].append('Earned ' + str(session['gold_transfer']) + ' from the ' + building + ' (' + datetime.now().strftime('%Y/%m/%d %I:%M %p') + ')')
            session['color_switch'] = True

    session['gold_counter'] += session['gold_transfer']
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.pop('gold_counter')
    session.pop('activity_log')
    return redirect('/')
app.run(debug=True)