from flask import render_template, Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def home():
    heading = "Welcome to Codeforces Problem shortlister"
    content = "This is a web app that helps you to shortlist problems from Codeforces based on your preferred topics and difficulty levels."
    return render_template('index.html', heading = heading, content = content)