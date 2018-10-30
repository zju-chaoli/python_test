#coding=utf-8

#first flask program


from flask import Flask
from flask import render_template

app = Flask("Test")

#mapping "/" to function hello_world
@app.route('/')
def hello_world():
	return "hello, world from flask in ubuntu on Python3 on 10-25-2018"



#mapping "/index" to function hello_world2
@app.route("/index")
def index():
	user = {'username':'Chao Li'}
	return render_template('index.html',title='home',user=user)



#main entry point
if __name__ == '__main__':
	app.run()




