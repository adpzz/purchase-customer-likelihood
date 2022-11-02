from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model_name = './models/logistic/best_logic_mod.sav'
model = pickle.load(open(model_name, 'rb'))

@app.route('/')
def home():
	result = ''
	return render_template('index.html', **locals())

@app.route('/predict', methods=['POST', 'GET'])
def predict():
	x1 = float(request.form['x1'])
	x2 = float(request.form['x2'])
	x3 = float(request.form['x3'])
	x4 = float(request.form['x4'])
	x5 = float(request.form['x5'])
	x6 = float(request.form['x6'])

	pred = model.predict([[x1, x2, x3, x4, x5, x6]])[0]
	return render_template("index.html", **locals())

if __name__ == '__main__':
	app.run(debug=True)