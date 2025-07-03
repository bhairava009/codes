from flask import Flask, render_template #url_for

app = Flask(__name__)

# Home route
@app.route('/')
def hello():
    return 'Hi im learning'
# Home route
@app.route('/home')
def home():
    return render_template('home.html')

# Contact route
@app.route('/contact')
def contact():
    # return "This is my contact"
    return render_template('contact.html')

# Address route
@app.route('/address')
def address():
    # return "This is the address"
    return render_template('address.html')
# Bio route
@app.route('/bio')
def bio():
    # return "This is my bio"/
    return render_template('bio.html')

# Dynamic route with username
@app.route("/user/<name>")
def user(name):
    return render_template("user.html",name=name)

@app.route("/post/<int:id>",methods =['GET'])
def post(id):
    # return f'post ID:{id}'
    return render_template("post.html",id=id)

@app.route("/about")
def about():
    return render_template("about.html")


# Run the app
if __name__ == '__main__':
    app.run(debug=True)

