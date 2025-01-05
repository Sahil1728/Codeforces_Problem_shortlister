import requests


def format_usernames(usernames):
    new_usernames = []
    for username in usernames:
        new_usernames.append(username.strip())
    return ';'.join(new_usernames)

def verify_user(usernames):
    """
    This method will check if the user_handles passed are valid or not. 
    """
    usernames = format_usernames(usernames)
    api_url = "https://codeforces.com/api/user.info?handles="
    unames = f"{usernames}"
    chh = "checkHistoricHandles=false"
    url = f"{api_url}{unames}&{chh}"
    resp = requests.get(url)
    data = resp.json()
    if resp.status_code not in [200, 201]:
        return (False, data.get('comment', 'Error in fetching data'))
    return (True, usernames)