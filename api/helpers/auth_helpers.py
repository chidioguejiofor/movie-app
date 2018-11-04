import jwt 
import datetime
from config import SECRET_KEY

def generate_token(data, expiration=datetime.timedelta(days=1)):

    return jwt.encode({
        **data, 
        'exp': datetime.datetime.utcnow() + expiration,
    }, SECRET_KEY, algorithm='HS256').decode('utf-8')


def decode_token(token):
    return jwt.decode(token, SECRET_KEY,'utf-8', algorithm='HS256')
