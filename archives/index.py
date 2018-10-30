#coding=utf-8

#first flask program


from flask import Flask

app = Flask("Test")

@app.route('/')
def hello_world():
	return "hello, world from flask in ubuntu on Python3"


if __name__ == '__main__':
	app.run(port=9999)




