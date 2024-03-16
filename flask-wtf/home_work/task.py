from flask import Flask, render_template, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'


@app.route('/')
def index():
    return redirect('/distribution')

@app.route('/distribution')
def distr():
    users = ['Ридли Скотт', 'Энди Уир', 'Марк Уотни', 'Венката Капур',
             'Тедди Сандерс', 'Шон Бин']
    return render_template('distr.html', users=users)


if __name__ == '__main__':
    app.run(debug=True)