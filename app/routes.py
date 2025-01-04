from flask import render_template, Blueprint, request

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

    print(usernames)
    print(lower_lim)
    print(upper_lim)
    print("Include Tags:", included_list)
    print("Exclude Tags:", excluded_list)

    return "Data retreived successfully"