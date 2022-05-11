# My cookie looks bloated with a lot of "b" and values are base64 encoded

cf. https://github.com/noraj/flask-session-cookie-manager/issues/9

1. Use python 3 rather than python 2 which is deprecated
2. Use the secret key if possible

Decoding the same cookie will result in different outputs:

```bash
# python 3 with secret key
{'number': '326410031505', 'username': 'admin'}
# python 3 without secret key
b'{"number":"326410031505","username":"admin"}'
# python 2 with secret key
{u'username': 'admin', u'number': '326410031505'}
# python 2 without secret key
{"number":{" b":"MzI2NDEwMDMxNTA1"},"username":{" b":"YWRtaW4="}}
```

# I can decode the cookie without the SECRET_KEY, why?

cf. https://github.com/noraj/flask-session-cookie-manager/issues/6

It's normal. Flask cookies are protected only on integrity thanks to cryptographic signature, so users can't spoof the data embedded in the cookie. But those cookie are not protected on confidentiality so users are free to read them. No issue there.

# I can't encode a cookie without a key.

cf. https://github.com/noraj/flask-session-cookie-manager/issues/5

Encrypting without a key is impossible. Creating a cookie with a random key will be invalid and so is not useful unless the server doesn't check the validity of the signature (not likely).
