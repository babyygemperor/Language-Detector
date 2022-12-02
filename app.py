from flask import Flask, request, render_template
from sklearn.preprocessing import LabelEncoder
import pickle
import json
import pandas as pd

app = Flask(__name__)
data = pd.read_csv("language_detection.csv")

Y = data["Language"]

model = pickle.load(open("model.pkl", 'rb'))
cv = pickle.load(open("transform.pkl", 'rb'))
le = LabelEncoder()
Y = le.fit_transform(Y)


def predict(input_json):
    text = input_json['predict']
    x = cv.transform([text]).toarray()  # converting text to bag of words model (Vector)
    lang = model.predict(x)  # predicting the language
    lang = le.inverse_transform(lang)  # finding the language corresponding the the predicted value
    input_json['lang'] = lang[0]
    print(input_json)
    return input_json  # printing the language


@app.route('/predict', methods=["POST"])
def post_predict():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json = request.json
        print(json)
        if 'predict' in json.keys():
            return predict(json)
        return 'No requests found! Please put your prediction requests as {\'predict\' : \'Test string to predict\'}'
    return 'Content-Type not supported!'


@app.route('/')
def my_form():
    return render_template('my-form.html')


@app.route('/', methods=["POST"])
def post_gui_predict():
    text = request.form['text']
    input_vals = {'predict': text}
    return predict(input_vals)['lang']
