import flask

app = flask.Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if flask.request.method == 'GET':
        return flask.jsonify({'message': 'Successful GET Request!'})
    if flask.request.method == 'POST':
        print("Received POST request with data:", flask.request.json)
        data = flask.request.json
        if data:
            return flask.jsonify({'message': 'Successful POST Request!', 'data': data})


if __name__ == '__main__':
    app.run(debug=True)