from flask import Flask, request, render_template

app = Flask(__name__)

#@app.route('/')
#def home():
#    return "Welcome to the Flask CI/CD Demo"

@app.route('/')
def home():
    title = "Flask CI/CD Demo"
    subtitle = "A simple example of deploying a Flask app with CI/CD"
    return render_template('index.html', title=title, subtitle=subtitle)

@app.route('/new-deployment')
def new_deployment():
    return "New deployment from CI/CD"

@app.route('/info')
def info():
    user_agent = request.headers.get('User-Agent')
    return f"Your user agent is: {user_agent}"

if __name__ == "__main__":
    app.run(debug=True)
