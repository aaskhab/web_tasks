from flask import Flask, render_template


app = Flask(__name__)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    user = {'title': 'Анкета',
            'surname': 'Wathy',
            'name': 'Mark',
            'education': 'выше среднего',
            'profession': 'штурман марсохода',
            'sex': 'male',
            'motivation': 'Всегда мечтал застрять на марсе',
            'ready': True}
    return render_template('auto_answer.html', **user)


if __name__ == '__main__':
    app.run(debug=True)