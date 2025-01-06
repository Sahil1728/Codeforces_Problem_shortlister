from flask import Flask, render_template, Blueprint, request, jsonify
from app.services import process_request

main = Blueprint('main', __name__)

@main.route('/')
def home():
    heading = "Welcome to Codeforces Problem shortlister"
    content = "This is a web app that helps you to shortlist problems from Codeforces based on your preferred topics and difficulty levels."
    return render_template('index.html', heading = heading, content = content)

@main.route('/process', methods=['POST'])
def process():
    usernames = request.form.getlist('usernames[]')
    lower_lim = request.form.get('lower_limit')
    upper_lim = request.form.get('upper_limit')
    include_tags = request.form.get('include_tags')  # JSON string
    exclude_tags = request.form.get('exclude_tags')  # JSON string

    # Convert JSON strings to Python lists
    import json
    included_list = json.loads(include_tags) if include_tags else []
    excluded_list = json.loads(exclude_tags) if exclude_tags else []
    while '' in included_list:
        included_list.remove('')
    while '' in excluded_list:
        excluded_list.remove('')
    res = process_request(
        usernames,
        lower_lim,
        upper_lim,
        included_list,
        excluded_list
    )
    for _, problem in res.items():
        problem["url"] = f"https://codeforces.com/problemset/problem/{problem['contestID']}/{problem['number']}"
    return render_template('problems.html', problems = res)

app = Flask(__name__)
app.register_blueprint(main)

handler = app