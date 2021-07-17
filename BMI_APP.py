from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])

def index():
	bmi = ''
	name = ''
	if request.method=='POST' and 'username' in request.form:
		name = request.form.get('username')
		height = float(request.form.get('height'))
		weight = float(request.form.get('weight'))
		bmi = bmi_calc(weight,height)

	return render_template("BMI_APP.html",
							bmi=bmi,name=name)
def bmi_calc(weight,height):
	return round((weight/((height/100)**2)),2)
