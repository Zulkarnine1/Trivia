import requests

def get_questions():
    response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
    response.raise_for_status()
    data = response.json()["results"]
    return data

question_data = get_questions()
