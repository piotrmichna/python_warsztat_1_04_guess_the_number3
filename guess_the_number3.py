from flask import Flask, render_template, request

app = Flask('GuessTheNumber')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        min_number = 0
        max_number = 1000
        return render_template('gues_the_number3.html', min_number=min_number, max_number=max_number)
    else:
        min_number = int(request.form["min_number"])
        max_number = int(request.form["max_number"])

        if request.form["answer"] != "You win":
            if request.form["answer"] == "To small":
                min_number = int(request.form["guess"])
            elif request.form["answer"] == "To big":
                max_number = int(request.form["guess"])

            guess = int((max_number - min_number) / 2 + min_number)
            return render_template('guess_the_number3_game.html', guess=guess, min_number=min_number,
                                   max_number=max_number)
        else:
            if request.form["answer"] == "You win":
                end_txt = f'Wygrałem! Twoja liczba to {request.form["guess"]}'
                return render_template('guess_the_number3_end.html', end_txt=end_txt)


app.run(debug=True)
