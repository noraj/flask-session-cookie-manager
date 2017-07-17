# Flask Session Cookie Decoder/Encoder

Author : [**Wilson Sumanang**](https://github.com/saruberoz)

Imported from [saruberoz.github.io](http://saruberoz.github.io/flask-session-cookie-decoder-slash-encoder)

## Depencencies

+ [itsdangerous](https://pypi.python.org/pypi/itsdangerous)
+ [Flask](https://pypi.python.org/pypi/Flask)

## Usage

```
usage: session_cookie_manager.py [-h] {encode,decode} ...

Flask Session Cookie Decoder/Encoder

positional arguments:
  {encode,decode}  sub-command help
    encode         encode
    decode         decode

optional arguments:
  -h, --help       show this help message and exit
```

### Encode

```
usage: session_cookie_manager.py encode [-h] -s <string> -t <string>

optional arguments:
  -h, --help            show this help message and exit
  -s <string>, --secret-key <string>
                        Secret key
  -t <string>, --cookie-structure <string>
                        Session cookie structure
```

### Decode

```
usage: session_cookie_manager.py decode [-h] [-s <string>] -c <string>

optional arguments:
  -h, --help            show this help message and exit
  -s <string>, --secret-key <string>
                        Secret key
  -c <string>, --cookie-value <string>
                        Session cookie value
```

## Examples

### Encode

```
$ python2 session_cookie_manager.py encode -s '.{y]tR&sp&77RdO~u3@XAh#TalD@Oh~yOF_51H(QV};K|ghT^d' -t '{"number":"326410031505","username":"admin"}'
eyJudW1iZXIiOnsiIGIiOiJNekkyTkRFd01ETXhOVEExIn0sInVzZXJuYW1lIjp7IiBiIjoiWVdSdGFXND0ifX0.DE2iRA.ig5KSlnmsDH4uhDpmsFRPupB5Vw
```

**Note**: the session cookie structure must be a valid python dictionary

### Decode

With secret key:

```
$ python2 session_cookie_manager.py decode -c 'eyJudW1iZXIiOnsiIGIiOiJNekkyTkRFd01ETXhOVEExIn0sInVzZXJuYW1lIjp7IiBiIjoiWVdSdGFXND0ifX0.DE2iRA.ig5KSlnmsDH4uhDpmsFRPupB5Vw' -s '.{y]tR&sp&77RdO~u3@XAh#TalD@Oh~yOF_51H(QV};K|ghT^d'
{u'username': 'admin', u'number': '326410031505'}
```


Without secret key (less pretty output):

```
$ python2 session_cookie_manager.py decode -c 'eyJudW1iZXIiOnsiIGIiOiJNekkyTkRFd01ETXhOVEExIn0sInVzZXJuYW1lIjp7IiBiIjoiWVdSdGFXND0ifX0.DE2iRA.ig5KSlnmsDH4uhDpmsFRPupB5Vw'
{"number":{" b":"MzI2NDEwMDMxNTA1"},"username":{" b":"YWRtaW4="}}
```
