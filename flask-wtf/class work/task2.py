from flask import Flask, render_template


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/training/<profession>')
def training(profession):
    return render_template('training.html', profession=profession)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)