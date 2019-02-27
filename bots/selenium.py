from instapy import InstaPy


def get_session(bot):
    session = InstaPy(username=bot.username,
                      password=bot.password,
                      selenium_local_session=False)
    session.set_selenium_remote_session(selenium_url='http://selenium:4444/wd/hub')
    session.login()
    # session.aborting turns True iff login failed.
    return not session.aborting
