from flash import flask
from theraeding import Thread

app = flask('app')

@app.route('/')
def main():
	return 'Bot active!'

def run():
	app.run(host="0.0.0.0", port=8080)

def keep_alive():
	server = Thread(target=run)
	server.start()