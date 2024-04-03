from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask CI/CD Demo"

@app.route('/new-deployment')
def new_deployment():
    return "New deployment from CI/CD"

@app.route('/info')
def info():
    user_agent = request.headers.get('User-Agent')
    return f"Your user agent is: {user_agent}"

if __name__ == "__main__":
    app.run(debug=True)
