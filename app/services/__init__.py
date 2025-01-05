import logging
from .user_handler import verify_user
from .problem_fetcher import fetch_problems

def process_request(usernames, lower_lim, upper_lim, include_tags, exclude_tags):
    res = verify_user(usernames)
    if res[0] != True:
        return res
    else:
        logging.info("User verification successful")
        ret = fetch_problems(
            res[1],
            lower_lim,
            upper_lim,
            include_tags,
            exclude_tags
        )
        if ret[0] == True:
            return ret[1]
        else:
            return "Problem fetching unsuccessful"

    # return "Data retreived successfully"