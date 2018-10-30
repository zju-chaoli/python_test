#coding=utf-8

#first flask program


from flask import Flask

app = Flask("Test")

#mapping "/" to function hello_world
@app.route('/')
def hello_world():
	return "hello, world from flask in ubuntu on Python3"



#mapping "/index" to function hello_world2
@app.route("/index")
def hello_world2():
	return "hello world2 associated to /index"



#main entry point
if __name__ == '__main__':
	app.run(port=9999)




