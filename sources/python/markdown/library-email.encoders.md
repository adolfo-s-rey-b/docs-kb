### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/email.utils.html "email.utils: Miscellaneous utilities")
     |
*   [previous](https://docs.python.org/3/library/email.charset.html "email.charset: Representing character sets")
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
*   [Internet Data Handling](https://docs.python.org/3/library/netdata.html)
     »
*   [`email` — An email and MIME handling package](https://docs.python.org/3/library/email.html)
     »
*   [`email.encoders`: Encoders](https://docs.python.org/3/library/email.encoders.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`email.encoders`: Encoders[¶](https://docs.python.org/3/library/email.encoders.html#module-email.encoders "Link to this heading")

==================================================================================================================================

**Source code:** [Lib/email/encoders.py](https://github.com/python/cpython/tree/3.15/Lib/email/encoders.py)

* * *

This module is part of the legacy (`Compat32`) email API. In the new API the functionality is provided by the _cte_ parameter of the [`set_content()`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.set_content "email.message.EmailMessage.set_content")
 method.

This module is deprecated in Python 3. The functions provided here should not be called explicitly since the [`MIMEText`](https://docs.python.org/3/library/email.mime.html#email.mime.text.MIMEText "email.mime.text.MIMEText")
 class sets the content type and CTE header using the _\_subtype_ and _\_charset_ values passed during the instantiation of that class.

The remaining text in this section is the original documentation of the module.

When creating [`Message`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message "email.message.Message")
 objects from scratch, you often need to encode the payloads for transport through compliant mail servers. This is especially true for _image/\*_ and _text/\*_ type messages containing binary data.

The [`email`](https://docs.python.org/3/library/email.html#module-email "email: Package supporting the parsing, manipulating, and generating email messages.")
 package provides some convenient encoders in its `encoders` module. These encoders are actually used by the [`MIMEAudio`](https://docs.python.org/3/library/email.mime.html#email.mime.audio.MIMEAudio "email.mime.audio.MIMEAudio")
 and [`MIMEImage`](https://docs.python.org/3/library/email.mime.html#email.mime.image.MIMEImage "email.mime.image.MIMEImage")
 class constructors to provide default encodings. All encoder functions take exactly one argument, the message object to encode. They usually extract the payload, encode it, and reset the payload to this newly encoded value. They should also set the _Content-Transfer-Encoding_ header as appropriate.

Note that these functions are not meaningful for a multipart message. They must be applied to individual subparts instead, and will raise a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 if passed a message whose type is multipart.

Here are the encoding functions provided:

email.encoders.encode\_quopri(_msg_)[¶](https://docs.python.org/3/library/email.encoders.html#email.encoders.encode_quopri "Link to this definition")

Encodes the payload into quoted-printable form and sets the _Content-Transfer-Encoding_ header to `quoted-printable` [\[1\]](https://docs.python.org/3/library/email.encoders.html#id2)
. This is a good encoding to use when most of your payload is normal printable data, but contains a few unprintable characters.

email.encoders.encode\_base64(_msg_)[¶](https://docs.python.org/3/library/email.encoders.html#email.encoders.encode_base64 "Link to this definition")

Encodes the payload into base64 form and sets the _Content-Transfer-Encoding_ header to `base64`. This is a good encoding to use when most of your payload is unprintable data since it is a more compact form than quoted-printable. The drawback of base64 encoding is that it renders the text non-human readable.

email.encoders.encode\_7or8bit(_msg_)[¶](https://docs.python.org/3/library/email.encoders.html#email.encoders.encode_7or8bit "Link to this definition")

This doesn’t actually modify the message’s payload, but it does set the _Content-Transfer-Encoding_ header to either `7bit` or `8bit` as appropriate, based on the payload data.

email.encoders.encode\_noop(_msg_)[¶](https://docs.python.org/3/library/email.encoders.html#email.encoders.encode_noop "Link to this definition")

This does nothing; it doesn’t even set the _Content-Transfer-Encoding_ header.

Footnotes

#### Previous topic

[`email.charset`: Representing character sets](https://docs.python.org/3/library/email.charset.html "previous chapter")

#### Next topic

[`email.utils`: Miscellaneous utilities](https://docs.python.org/3/library/email.utils.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=email.encoders%3A+Encoders&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Femail.encoders.html&pagesource=library%2Femail.encoders.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/email.encoders.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/email.utils.html "email.utils: Miscellaneous utilities")
     |
*   [previous](https://docs.python.org/3/library/email.charset.html "email.charset: Representing character sets")
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
*   [Internet Data Handling](https://docs.python.org/3/library/netdata.html)
     »
*   [`email` — An email and MIME handling package](https://docs.python.org/3/library/email.html)
     »
*   [`email.encoders`: Encoders](https://docs.python.org/3/library/email.encoders.html)
    
*    
    
    |
*   Theme Auto Light Dark |