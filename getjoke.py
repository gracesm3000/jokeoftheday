import pandas as pd

joke_df = pd.read_csv('database/JOD.csv')


def get_random_joke(db):
    random_row = db.sample(1)
    question = random_row['Joke'].iloc[0]
    answer = random_row['Answer'].iloc[0]
    return question, answer

# question, answer = get_random_joke(joke_df)
# print(question)
# print(answer)