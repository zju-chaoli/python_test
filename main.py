#coding=utf-8

#first flask program


from flask import Flask
from flask import render_template,flash,redirect,url_for
from config import Config
from forms import LoginForm


app = Flask(__name__)
app.config.from_object(Config)
# print(app.config['OPENID_PROVIDERS'])

#mapping "/" to function hello_world
@app.route('/')
def hello_world():
	return "hello, world from flask in ubuntu on Python3 on 10-25-2018"



#mapping "/index" to function hello_world2
@app.route("/index")
def index():
	user = {'username':'Chao Li'}
	posts = [
	{
		'author':{'username':'john'},
		'body':'beautifuy day in portland'
	},
	{
		'author':{'username':'Susan'},
		'body':'the Avengers movie was so cool'
	}
	]

	return render_template('index.html',title = 'home',user=user,posts=posts)


#mapping "/login" to login web page
@app.route("/login",methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('login requested for OpenID= {}, remember_me={}'.format(form.openid.data,form.remember_me.data))
		return redirect(url_for('index'))
	return render_template('login.html',title = 'Sign In', form = form,providers=app.config['OPENID_PROVIDERS'])



#main entry point
if __name__ == '__main__':
	app.run()
else:
	print("debugging the main Module")




