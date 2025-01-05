import requests

def filter_problems(data, usernames, lower_lim, upper_lim):
    return data


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
        data = filter_problems(data, usernames, lower_lim, upper_lim)
    return (True, data)