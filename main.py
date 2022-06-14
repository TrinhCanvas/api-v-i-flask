from flask import Flask, request, json

app = Flask(__name__)

data = [{
	'id': '1',
	'name': 'Tuan',
	'_class': 'a1',
	'age': 'nam',
	'medium_score': '7'
}, {
	'id': '2',
	'name': 'Hong',
	'_class': 'a2',
	'age': 'nu',
	'medium_score': '8'
}, {
	'id': '3',
	'name': 'Minh',
	'_class': 'a1',
	'age': 'nam',
	'medium_score': '7'
}]


@app.route("/", methods=['POST'])
def add_student():
	id = request.form.get('id')
	name = request.form.get('name')
	Lop = request.form.get('class')
	age = request.form.get('age')
	medium_score = request.form.get('medium_score')
	obj = {
		'id': id,
		'name': name,
		'class': Lop,
		'age': age,
		'medium_score': medium_score
	}
	data.append(obj)

	return json.dumps(obj)


@app.route("/", methods=['get'])
def show_student():
	return json.dumps(data)


@app.route("/<id>", methods=['delete'])
def delete_student(id):
	for i in range(0, len(data) - 1):
		if data[i]['id'] == id:
			data.pop(i)
	return json.dumps(data)



@app.route("/<id>", methods=['put'])
def update_student(id):
	for i in range(0, len(data) - 1):
		if data[i]['id'] == id:
			data[i]['name'] = request.form.get('name')

	return "succesfull"


@app.route("/a", methods=['get'])
def get_max():
	max = data[0]['medium_score']
	for i in range(0, len(data)):
		if max < data[i]['medium_score']:
			max = data[i]['medium_score']
	return max


@app.route("/<scrip>", methods=['get'])
def get_studentbyname(scrip):
	for i in range(0, len(data) - 1):
		if data[i]['id'] == scrip:
			return json.dumps(data[i])
		if data[i]['name'].lower() == scrip.lower():
			return json.dumps(data[i])
	return "not found"


data_nam = []
data_nu =  []
@app.route("/age/<int:n>", methods=['get'])
def show_studentbyage(n):
	for i in range(0, len(data)):
		if data[i]['age'] == 'nam':
			data_nam.append(data[i])
		else:
			data_nu.append(data[i])
	if n == 1:
		return json.dumps(data_nam)
	if n == 2:
		return json.dumps(data_nu)
	else:
		return json.dumps(data_nam) + json.dumps(data_nu)



if __name__ == "__main__":
	app.run(debug=True)
