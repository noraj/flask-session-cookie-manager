# Flask Session Cookie Decoder/Encoder

Original author : [**Wilson Sumanang**](https://github.com/saruberoz)

Fixes and improvements author : [**Alexandre ZANNI**](https://github.com/noraj)

Imported from [saruberoz.github.io](http://saruberoz.github.io/flask-session-cookie-decoder-slash-encoder)

## Depencencies

+ Python 2 or Python 3
+ [itsdangerous](https://pypi.python.org/pypi/itsdangerous)
+ [Flask](https://pypi.python.org/pypi/Flask)

## Installation

### ArchLinux

#### Python 3

```
# pacman -S python
# pacman -S python-itsdangerous python-flask --asdep
```

#### Python 2

```
# pacman -S python2
# pacman -S python2-itsdangerous python2-flask --asdep
```

### Other distros

Find your way with your package manager, use pip in a virtual environment or use [pyenv](https://github.com/pyenv/pyenv).

## Usage

Use `flask_session_cookie_manager3.py` with Python 3 and `flask_session_cookie_manager2.py` with Python 2.

```
usage: flask_session_cookie_manager{2,3}.py [-h] {encode,decode} ...

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
usage: flask_session_cookie_manager{2,3}.py encode [-h] -s <string> -t <string>

optional arguments:
  -h, --help            show this help message and exit
  -s <string>, --secret-key <string>
                        Secret key
  -t <string>, --cookie-structure <string>
                        Session cookie structure
```

### Decode

```
usage: flask_session_cookie_manager.py decode [-h] [-s <string>] -c <string>

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
$ python{2,3} flask_session_cookie_manager{2,3}.py encode -s '.{y]tR&sp&77RdO~u3@XAh#TalD@Oh~yOF_51H(QV};K|ghT^d' -t '{"number":"326410031505","username":"admin"}'
eyJudW1iZXIiOnsiIGIiOiJNekkyTkRFd01ETXhOVEExIn0sInVzZXJuYW1lIjp7IiBiIjoiWVdSdGFXND0ifX0.DE2iRA.ig5KSlnmsDH4uhDpmsFRPupB5Vw
```

**Note**: the session cookie structure must be a valid python dictionary

### Decode

With secret key:

```
$ python{2,3} flask_session_cookie_manager{2,3}.py decode -c 'eyJudW1iZXIiOnsiIGIiOiJNekkyTkRFd01ETXhOVEExIn0sInVzZXJuYW1lIjp7IiBiIjoiWVdSdGFXND0ifX0.DE2iRA.ig5KSlnmsDH4uhDpmsFRPupB5Vw' -s '.{y]tR&sp&77RdO~u3@XAh#TalD@Oh~yOF_51H(QV};K|ghT^d'
{u'username': 'admin', u'number': '326410031505'}
```


Without secret key (less pretty output):

```
$ python{2,3} flask_session_cookie_manager{2,3}.py decode -c 'eyJudW1iZXIiOnsiIGIiOiJNekkyTkRFd01ETXhOVEExIn0sInVzZXJuYW1lIjp7IiBiIjoiWVdSdGFXND0ifX0.DE2iRA.ig5KSlnmsDH4uhDpmsFRPupB5Vw'
{"number":{" b":"MzI2NDEwMDMxNTA1"},"username":{" b":"YWRtaW4="}}
```
