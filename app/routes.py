from flask import Flask, render_template, Blueprint, request
from app.services import process_request

main = Blueprint('main', __name__)

@main.route('/')
def home():
    heading = "Welcome to Codeforces Problem shortlister"
    content = "This will help you to shortlist problems from Codeforces for mashup contests based on your preferred topics and difficulty levels."
    return render_template('index.html', heading = heading, content = content)

@main.route('/process', methods=['POST'])
def process():
    usernames = request.form.getlist('usernames[]')
    lower_lim = request.form.get('lower_limit')
    upper_lim = request.form.get('upper_limit')
    include_tags = request.form.getlist('include_tags[]')  # JSON string
    exclude_tags = request.form.getlist('exclude_tags[]')  # JSON string
    include_tags = ",".join(include_tags) if include_tags else ""

    # Handle empty string or '[]' input for tags and convert to list
    included_list = include_tags.split(',') if include_tags else []
    excluded_list = exclude_tags.split(',') if exclude_tags else []

    # Remove any empty strings from the lists
    included_list = [tag for tag in included_list if tag]
    excluded_list = [tag for tag in excluded_list if tag]
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