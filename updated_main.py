import jwt
import time
from faker import Faker
import random

# Auto token generator for Classplus every 98 videos
def generate_fake_token():
    fake = Faker()
    payload = {
        "id": random.randint(100000000, 999999999),
        "orgId": random.randint(100000, 999999),
        "type": 1,
        "mobile": "91" + str(random.randint(6000000000, 9999999999)),
        "name": fake.name(),
        "email": fake.email().replace("@", f"+{random.randint(1000,9999)}@"),
        "isFirstLogin": True,
        "defaultLanguage": "EN",
        "countryCode": "IN",
        "isInternational": False,
        "isDiy": True,
        "loginVia": "Otp",
        "fingerprintId": fake.uuid4().replace('-', ''),
        "iat": int(time.time()),
        "exp": int(time.time()) + 7 * 24 * 60 * 60
    }
    SECRET_KEY = "test123"
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

# Token counter init
video_counter = 0
classplus_token = generate_fake_token()

# Inside the for loop where links are processed
            elif "classplusapp.com/drm/" in url:
                video_counter += 1
                if video_counter % 98 == 0:
                    classplus_token = generate_fake_token()
                url = f"https://key-one-gamma.vercel.app/api?url={url}&token={classplus_token}"
                mpd, keys = helper.get_mps_and_keys(url)
                url = mpd
                keys_string = " ".join([f"--key {key}" for key in keys])
