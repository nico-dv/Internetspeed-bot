

with open("../bot-extras/credentials.txt") as crd:
    crd_list = crd.read().splitlines()


PROMISED_DOWN = 600
PROMISED_UP = 60
TWITTER_EMAIL = crd_list[0]
TWITTER_PASSWORD = crd_list[1]







