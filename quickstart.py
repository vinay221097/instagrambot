"""
This template is written by @boldestfortune
What does this quickstart script aim to do?
- Just started playing around with Quota Supervisor, so I'm still tweaking
these settings
"""

import random
from instapy import InstaPy
from instapy import smart_run

# get a session!
session = InstaPy(username='smithjohn4321234', password='abcd4321@',headless_browser=True)

# let's go! :>
with smart_run(session):
    # general settings
    session.set_quota_supervisor(enabled=True, sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"], sleepyhead=True, stochastic_flow=True, notify_me=True,
                              peak_likes_hourly=57,
                              peak_likes_daily=585,
                               peak_comments_hourly=21,
                               peak_comments_daily=182,
                                peak_follows_hourly=48,
                                peak_follows_daily=None,
                                 peak_unfollows_hourly=35,
                                 peak_unfollows_daily=402,
                                  peak_server_calls_hourly=None,
                                  peak_server_calls_daily=4700)
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=-1.3,
                                    delimit_by_numbers=True,
                                    max_followers=10000,
                                    max_following=15000,
                                    min_followers=75,
                                    min_following=75)
    session.set_do_comment(False, percentage=10)
    session.set_comments(['aMEIzing!', 'So much fun!!', 'Nicey!',
			'Just incredible :open_mouth:',
			'What camera did you use @{}?',
			'Love your posts @{}',
			'Looks awesome @{}',
      			'Fan of your Posts @{}',
      			'Awesome post @{}',
			'Getting inspired by you @{}',
			':raised_hands: Yes!',
			'I can feel your passion @{} :muscle:'])
    session.set_use_clarifai(enabled=True, api_key='')
    session.clarifai_check_img_for(
        ["nsfw", "gay", "hijab", "niqab", "religion", "shirtless", "fitness",
         "yamaka", "rightwing"], comment=False)
    session.set_dont_like(
        ["dick", "squirt", "gay", "homo", "#fit", "#fitfam", "#fittips",
         "#abs", "#kids", "#children", "#child",
         "[nazi",
         "jew", "judaism", "[muslim", "[islam", "bangladesh", "[hijab",
         "[niqab", "[farright", "[rightwing",
         "#conservative", "death", "racist"])
    session.set_do_follow(enabled=True, percentage=25, times=2)
    hash_tags_list = ["interiordesign", "artshow", "restaurant", "artist", "losangeles",
         "newyork", "miami"]
    hash_tags_list = [x.encode('utf-8') for x in hash_tags_list]

    # like by tags activity
    session.set_smart_hashtags(
        hash_tags_list,
        limit=10, sort='random', log_tags=True)
    session.set_dont_like(['promoter', 'nightclub'])
    session.set_delimit_liking(enabled=True, max_likes=1005, min_likes=20)
    session.like_by_tags(hash_tags_list,amount=random.randint(1, 15))

    # interact user followers activity
    session.set_user_interact(amount=5, randomize=True, percentage=50,
                              media='Photo')
    session.set_do_follow(enabled=True, percentage=70)
    session.set_do_like(enabled=True, percentage=70)
    session.set_comments([u"👍" , 'Nice shot! @{}',
	    'I love your profile! @{}',
	    'Your feed is an inspiration :thumbsup:',
	    'Just incredible :open_mouth:',
	    'What camera did you use @{}?',
	    'Love your posts @{}',
	    'Looks awesome @{}',
	    'Fan of your paost @{}',
	    'Awesome post @{}',
	    'Getting inspired by you @{}',
	    ':raised_hands: Yes!'])
    session.set_do_comment(enabled=True, percentage=30)
    session.interact_user_followers([''], amount=random.randint(1, 10),
                                    randomize=True)

    # unfollow activity
    session.set_dont_unfollow_active_users(enabled=True, posts=3)
    session.unfollow_users(amount=random.randint(30, 100),
                           InstapyFollowed=(True, "all"), style="FIFO",
                           unfollow_after=90 * 60 * 60, sleep_delay=501)

    """ Joining Engagement Pods...
    """
    session.join_pods(topic='sports')
