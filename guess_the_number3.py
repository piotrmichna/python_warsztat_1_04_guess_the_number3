from flask import Flask, render_template, request

app = Flask('GuessTheNumber')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('gues_the_number3.html')
    else:
        return render_template('gues_the_number3.html')


app.run(debug=True)
