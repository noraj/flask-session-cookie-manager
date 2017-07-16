""" Flask Session Cookie Decoder/Encoder """
__author__ = 'Wilson Sumanang'

# standard imports
import sys
import zlib
from itsdangerous import base64_decode
import ast

# external Imports
from flask.sessions import SecureCookieSessionInterface


class MockApp(object):

    def __init__(self, secret_key):
        self.secret_key = secret_key


def session_cookie_encoder(secret_key, session_cookie_structure):
    """ Encode a Flask session cookie

    Example:
        cookie_structure = dict(
        	gplus_id     = 1285135705050360459231,
            email        = john.doe@gmail.com,
            user_info    = dict(
                            full_name = john doe,
                        )
        )
        session_cookie_encoder(b'development key', cookie_structure)

    Args:
        secret_key (string): Flask App secret key
        session_cookie_structure (dict): Flask session cookie structure

    Return:
        value (string): Flask session cookie
    """
    try:
        app = MockApp(secret_key)

        session_cookie_structure = dict(ast.literal_eval(session_cookie_structure))
        si = SecureCookieSessionInterface()
        s = si.get_signing_serializer(app)

        return s.dumps(session_cookie_structure)
    except Exception as e:
        return "[Encoding error]{}".format(e)


def session_cookie_decoder(session_cookie_value):
    """ Decode a Flask cookie

    Args:
        session_cookie_value (string): Flask session cookie to decode
    """
    try:
        compressed = False
        payload = session_cookie_value

        if payload.startswith(b'.'):
            compressed = True
            payload = payload[1:]

        data = payload.split(".")[0]

        data = base64_decode(data)
        if compressed:
            data = zlib.decompress(data)

        return data
    except Exception as e:
        return "[Decoding error]{}".format(e)


if __name__ == "__main__":
    encoder_guide = "Usage: session_cookie_manager.py <encode> <secret_key> <session_cookie_structure>"
    decoder_guide = "Usage: session_cookie_manager.py <decode> <session_cookie_value>"
    print sys.argv
    if len(sys.argv) == 3:
        status, session_cookie_value = sys.argv[1:]
        if status.lower() == 'decode':
            print session_cookie_decoder(session_cookie_value)
        else:
            print decoder_guide
            sys.exit(1)
    elif len(sys.argv) == 4:
        status, secret_key, session_cookie_structure = sys.argv[1:]
        if status.lower() == 'encode':
            print session_cookie_encoder(secret_key, session_cookie_structure)
            sys.exit(1)
        else:
            print encoder_guide
    else:
        print decoder_guide
        print encoder_guide
        sys.exit(1)
