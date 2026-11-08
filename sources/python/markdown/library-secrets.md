### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/allos.html "Generic Operating System Services")
     |
*   [previous](https://docs.python.org/3/library/hmac.html "hmac — Keyed-Hashing for Message Authentication")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [The Python standard library](https://docs.python.org/3/library/index.html)
     »
*   [Cryptographic Services](https://docs.python.org/3/library/crypto.html)
     »
*   [`secrets` — Generate secure random numbers for managing secrets](https://docs.python.org/3/library/secrets.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`secrets` — Generate secure random numbers for managing secrets[¶](https://docs.python.org/3/library/secrets.html#module-secrets "Link to this heading")

=========================================================================================================================================================

Added in version 3.6.

**Source code:** [Lib/secrets.py](https://github.com/python/cpython/tree/3.15/Lib/secrets.py)

* * *

The `secrets` module is used for generating cryptographically strong random numbers suitable for managing data such as passwords, account authentication, security tokens, and related secrets.

In particular, `secrets` should be used in preference to the default pseudo-random number generator in the [`random`](https://docs.python.org/3/library/random.html#module-random "random: Generate pseudo-random numbers with various common distributions.")
 module, which is designed for modelling and simulation, not security or cryptography.

See also

[**PEP 506**](https://peps.python.org/pep-0506/)

Random numbers[¶](https://docs.python.org/3/library/secrets.html#random-numbers "Link to this heading")

--------------------------------------------------------------------------------------------------------

The `secrets` module provides access to the most secure source of randomness that your operating system provides.

class secrets.SystemRandom[¶](https://docs.python.org/3/library/secrets.html#secrets.SystemRandom "Link to this definition")

A class for generating random numbers using the highest-quality sources provided by the operating system. See [`random.SystemRandom`](https://docs.python.org/3/library/random.html#random.SystemRandom "random.SystemRandom")
 for additional details.

secrets.choice(_seq_)[¶](https://docs.python.org/3/library/secrets.html#secrets.choice "Link to this definition")

Return a randomly chosen element from a non-empty sequence.

secrets.randbelow(_exclusive\_upper\_bound_)[¶](https://docs.python.org/3/library/secrets.html#secrets.randbelow "Link to this definition")

Return a random int in the range \[0, _exclusive\_upper\_bound_).\
\
secrets.randbits(_k_)[¶](https://docs.python.org/3/library/secrets.html#secrets.randbits "Link to this definition")\
\
Return a non-negative int with _k_ random bits.\
\
Generating tokens[¶](https://docs.python.org/3/library/secrets.html#generating-tokens "Link to this heading")\
\
--------------------------------------------------------------------------------------------------------------\
\
The `secrets` module provides functions for generating secure tokens, suitable for applications such as password resets, hard-to-guess URLs, and similar.\
\
secrets.token\_bytes(_nbytes\=None_)[¶](https://docs.python.org/3/library/secrets.html#secrets.token_bytes "Link to this definition")\
\
Return a random byte string containing _nbytes_ number of bytes.\
\
If _nbytes_ is not specified or `None`, [`DEFAULT_ENTROPY`](https://docs.python.org/3/library/secrets.html#secrets.DEFAULT_ENTROPY "secrets.DEFAULT_ENTROPY")\
 is used instead.\
\
Copy\
\
\>>> token\_bytes(16)\
b'\\xebr\\x17D\*t\\xae\\xd4\\xe3S\\xb6\\xe2\\xebP1\\x8b'\
\
secrets.token\_hex(_nbytes\=None_)[¶](https://docs.python.org/3/library/secrets.html#secrets.token_hex "Link to this definition")\
\
Return a random text string, in hexadecimal. The string has _nbytes_ random bytes, each byte converted to two hex digits.\
\
If _nbytes_ is not specified or `None`, [`DEFAULT_ENTROPY`](https://docs.python.org/3/library/secrets.html#secrets.DEFAULT_ENTROPY "secrets.DEFAULT_ENTROPY")\
 is used instead.\
\
Copy\
\
\>>> token\_hex(16)\
'f9bf78b9a18ce6d46a0cd2b0b86df9da'\
\
secrets.token\_urlsafe(_nbytes\=None_)[¶](https://docs.python.org/3/library/secrets.html#secrets.token_urlsafe "Link to this definition")\
\
Return a random URL-safe text string, containing _nbytes_ random bytes. The text is Base64 encoded, so on average each byte results in approximately 1.3 characters.\
\
If _nbytes_ is not specified or `None`, [`DEFAULT_ENTROPY`](https://docs.python.org/3/library/secrets.html#secrets.DEFAULT_ENTROPY "secrets.DEFAULT_ENTROPY")\
 is used instead.\
\
Copy\
\
\>>> token\_urlsafe(16)\
'Drmhze6EPcv0fN\_81Bj-nA'\
\
### How many bytes should tokens use?[¶](https://docs.python.org/3/library/secrets.html#how-many-bytes-should-tokens-use "Link to this heading")\
\
To be secure against [brute-force attacks](https://en.wikipedia.org/wiki/Brute-force_attack)\
, tokens need to have sufficient randomness. Unfortunately, what is considered sufficient will necessarily increase as computers get more powerful and able to make more guesses in a shorter period. As of 2015, it is believed that 32 bytes (256 bits) of randomness is sufficient for the typical use-case expected for the `secrets` module.\
\
For those who want to manage their own token length, you can explicitly specify how much randomness is used for tokens by giving an [`int`](https://docs.python.org/3/builtins/functions.html#int "int")\
 argument to the various `token_*` functions. That argument is taken as the number of bytes of randomness to use.\
\
Otherwise, if no argument is provided, or if the argument is `None`, the `token_*` functions use [`DEFAULT_ENTROPY`](https://docs.python.org/3/library/secrets.html#secrets.DEFAULT_ENTROPY "secrets.DEFAULT_ENTROPY")\
 instead.\
\
secrets.DEFAULT\_ENTROPY[¶](https://docs.python.org/3/library/secrets.html#secrets.DEFAULT_ENTROPY "Link to this definition")\
\
Default number of bytes of randomness used by the `token_*` functions.\
\
The exact value is subject to change at any time, including during maintenance releases.\
\
Other functions[¶](https://docs.python.org/3/library/secrets.html#other-functions "Link to this heading")\
\
----------------------------------------------------------------------------------------------------------\
\
secrets.compare\_digest(_a_, _b_)[¶](https://docs.python.org/3/library/secrets.html#secrets.compare_digest "Link to this definition")\
\
Return `True` if strings or [bytes-like objects](https://docs.python.org/3/glossary.html#term-bytes-like-object)\
 _a_ and _b_ are equal, otherwise `False`, using a “constant-time compare” to reduce the risk of [timing attacks](https://web.archive.org/web/20250815071532/https://codahale.com/a-lesson-in-timing-attacks/)\
. See [`hmac.compare_digest()`](https://docs.python.org/3/library/hmac.html#hmac.compare_digest "hmac.compare_digest")\
 for additional details.\
\
Recipes and best practices[¶](https://docs.python.org/3/library/secrets.html#recipes-and-best-practices "Link to this heading")\
\
--------------------------------------------------------------------------------------------------------------------------------\
\
This section shows recipes and best practices for using `secrets` to manage a basic level of security.\
\
Generate an eight-character alphanumeric password:\
\
Copy\
\
import string\
import secrets\
alphabet \= string.ascii\_letters + string.digits\
password \= ''.join(secrets.choice(alphabet) for i in range(8))\
\
Note\
\
Applications should not [**store passwords in a recoverable format**](https://cwe.mitre.org/data/definitions/257.html)\
, whether plain text or encrypted. They should be salted and hashed using a cryptographically strong one-way (irreversible) hash function.\
\
Generate a ten-character alphanumeric password with at least one lowercase character, at least one uppercase character, and at least three digits:\
\
Copy\
\
import string\
import secrets\
alphabet \= string.ascii\_letters + string.digits\
while True:\
    password \= ''.join(secrets.choice(alphabet) for i in range(10))\
    if (any(c.islower() for c in password)\
            and any(c.isupper() for c in password)\
            and sum(c.isdigit() for c in password) \>= 3):\
        break\
\
Generate an [XKCD-style passphrase](https://xkcd.com/936/)\
:\
\
Copy\
\
import secrets\
\# On standard Linux systems, use a convenient dictionary file.\
\# Other platforms may need to provide their own word-list.\
with open('/usr/share/dict/words') as f:\
    words \= \[word.strip() for word in f\]\
    password \= ' '.join(secrets.choice(words) for i in range(4))\
\
Generate a hard-to-guess temporary URL containing a security token suitable for password recovery applications:\
\
Copy\
\
import secrets\
url \= 'https://example.com/reset=' + secrets.token\_urlsafe()\
\
### [Table of Contents](https://docs.python.org/3/contents.html)\
\
*   [`secrets` — Generate secure random numbers for managing secrets](https://docs.python.org/3/library/secrets.html#)\
    *   [Random numbers](https://docs.python.org/3/library/secrets.html#random-numbers)\
        \
    *   [Generating tokens](https://docs.python.org/3/library/secrets.html#generating-tokens)\
        *   [How many bytes should tokens use?](https://docs.python.org/3/library/secrets.html#how-many-bytes-should-tokens-use)\
            \
    *   [Other functions](https://docs.python.org/3/library/secrets.html#other-functions)\
        \
    *   [Recipes and best practices](https://docs.python.org/3/library/secrets.html#recipes-and-best-practices)\
        \
\
#### Previous topic\
\
[`hmac` — Keyed-Hashing for Message Authentication](https://docs.python.org/3/library/hmac.html "previous chapter")\
\
#### Next topic\
\
[Generic Operating System Services](https://docs.python.org/3/library/allos.html "next chapter")\
\
### This page\
\
*   [Report a bug](https://docs.python.org/3/bugs.html)\
    \
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=secrets+%E2%80%94+Generate+secure+random+numbers+for+managing+secrets&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fsecrets.html&pagesource=library%2Fsecrets.rst)\
    \
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/secrets.rst?plain=1)\
    \
\
«\
\
### Navigation\
\
*   [index](https://docs.python.org/3/genindex.html "General Index")\
    \
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")\
     |\
*   [next](https://docs.python.org/3/library/allos.html "Generic Operating System Services")\
     |\
*   [previous](https://docs.python.org/3/library/hmac.html "hmac — Keyed-Hashing for Message Authentication")\
     |\
*   ![Python logo](https://docs.python.org/3/_static/py.svg)\
*   [Python](https://www.python.org/)\
     »\
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文\
    \
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6\
    \
\
*   [3.15.2 documentation](https://docs.python.org/3/index.html)\
     »\
*   [The Python standard library](https://docs.python.org/3/library/index.html)\
     »\
*   [Cryptographic Services](https://docs.python.org/3/library/crypto.html)\
     »\
*   [`secrets` — Generate secure random numbers for managing secrets](https://docs.python.org/3/library/secrets.html)\
    \
*    \
    \
    |\
*   Theme Auto Light Dark |