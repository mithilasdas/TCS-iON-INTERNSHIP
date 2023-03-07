from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
# load the model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    result = ''
    return render_template('index.html', **locals())


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    age = float(request.form['age'])
    workclass = float(request.form['workclass'])
    education = float(request.form['education'])
    marital_status = float(request.form['marital_status'])
    occupation = float(request.form['occupation'])
    relationship = float(request.form['relationship'])
    race = float(request.form['race'])
    sex = float(request.form['sex'])
    hours_per_week = float(request.form['hours_per_week'])
    native_country = float(request.form['native_country'])
    result = model.predict([[age,workclass,education,marital_status,occupation,relationship,race,sex,hours_per_week,native_country]])[0]
    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run(port=3333)