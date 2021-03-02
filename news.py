from flask import Flask, render_template, url_for

app = Flask(__name__)

# app.config['SECRET_KEY'] ='7509080330a25355310420247db0ab5c' 

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/register")
def register():
    return render_template('register.html', title='Register')


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/Account")
def account():
    return render_template('account.html', title='Account')


@app.route("/post")
def post():
    return render_template('post.html', title='Post')







if __name__ == '__main__':
    app.run(debug=True)


    