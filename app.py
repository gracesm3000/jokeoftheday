import os
import flask
import pandas as pd

port = int(os.environ.get("PORT", 5008))


joke_df = pd.read_csv('database/JOD.csv')


def get_random_joke(db):
    random_row = db.sample(1)
    question = random_row['Joke'].iloc[0]
    answer = random_row['Answer'].iloc[0]
    return question, answer


app = flask.Flask(__name__, template_folder='templates')

@app.route('/')

def main():
    question, answer = get_random_joke(joke_df)
    return flask.render_template('main.html', question=question, answer=answer)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)
