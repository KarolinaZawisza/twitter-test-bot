import os
from dotenv import load_dotenv
load_dotenv('C:/Users/zawis/Documents/EV/.env')

TWITTER_LOGIN = os.getenv('twitter_login')
TWITTER_PASSWORD = os.getenv('twitter_password')