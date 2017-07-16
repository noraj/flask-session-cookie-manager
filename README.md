# Flask Session Cookie Decoder/Encoder

Author : [**Wilson Sumanang**](https://github.com/saruberoz)

Imported from [saruberoz.github.io](http://saruberoz.github.io/flask-session-cookie-decoder-slash-encoder)

What you will need the:
+ flask app secret key (for encoding)
+ the session cookie structure/data for (decoding/encoding)

How to use the python script:
+ Use the session_cookie_decoder to get session cookie data/structure `python2 session_cookie_manager.py <decode> <session_cookie_value>`
+ Use the session_cookie_encoder to setup a stub/mock session cookie data `python2 session_cookie_manager.py <encode> <secret_key> <session_cookie_structure>`
