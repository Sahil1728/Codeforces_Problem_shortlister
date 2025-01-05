import requests
pos = 0
def in_excluded_tags(prob, excluded):
    tags = [tag.lower() for tag in prob['tags']]
    for ex in excluded:
        if any(ex.lower() in tag for tag in tags):
            return True
    return False

def in_included_tags(prob, included):
    tags = [tag.lower() for tag in prob['tags']]
    for inc in included:
        if any(inc.lower() in tag for tag in tags):
            return True
    return False

def construct_info(stats, prob):
    global pos
    pos += 1
    contestID = prob['contestId']
    number = prob['index']
    rating = int(prob.get('rating', '0'))
    name = prob['name']
    tags = list(set(prob['tags']))  # some problems have same tags mentioned multiple times
    solved = stats['solvedCount']
    return_dict = {
        'contestID': contestID,     # This is the contest ID of the contest in which the problem appeared
        'number': number,           # The problem no. eg A, B, C ...
        'rating': rating,           # Rating of the problem
        'name': name,               # Name of the problem
        'tags': tags,               # tags of the problem
        'solved': solved            # No of people who have solved the problem
    }
    return pos, return_dict

def out_of_limit(prob, lower_lim, upper_lim):
    points = int(prob.get('rating', False))
    if not points:
        return False
    lower_lim = int(lower_lim)
    upper_lim = int(upper_lim)
    if points < lower_lim or points > upper_lim:
        return True
    return False

def filter_problems(data, usernames, lower_lim, upper_lim, included, excluded):
    selected_problems = {}
    if not data['status'] == 'OK':
        return data
    total = len(data['result']['problems'])
    for idx in range(total):
        stats = data['result']['problemStatistics'][idx]
        prob = data['result']['problems'][idx]
        if out_of_limit(prob, lower_lim, upper_lim) or in_excluded_tags(prob, excluded):
            continue
        elif in_included_tags(prob, included):
            key, value = construct_info(stats, prob)
            selected_problems[key] = value
    return selected_problems


def fetch_problems(usernames, lower_lim, upper_lim, included_list, excluded_list):
    """
    This method will fetch the problems from Codeforces API based on the given parameters.
    """
    api_url = "https://codeforces.com/api/problemset.problems?"
    tags = f"tags={';'.join(included_list)}"
    url = f"{api_url}{tags}"
    resp = requests.get(url)
    data = resp.json()
    if resp.status_code not in [200, 201]:
        return (False, data.get('comment', 'Error in fetching data'))
    else:
        data = filter_problems(data, usernames, lower_lim, upper_lim, included_list, excluded_list)
    return (True, data)