### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/email.header.html "email.header: Internationalized headers")
     |
*   [previous](https://docs.python.org/3/library/email.compat32-message.html "email.message.Message: Representing an email message using the compat32 API")
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
*   [`email.mime`: Creating email and MIME objects from scratch](https://docs.python.org/3/library/email.mime.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`email.mime`: Creating email and MIME objects from scratch[¶](https://docs.python.org/3/library/email.mime.html#module-email.mime "Link to this heading")

==========================================================================================================================================================

**Source code:** [Lib/email/mime/](https://github.com/python/cpython/tree/3.15/Lib/email/mime/)

* * *

This module is part of the legacy (`Compat32`) email API. Its functionality is partially replaced by the [`contentmanager`](https://docs.python.org/3/library/email.contentmanager.html#module-email.contentmanager "email.contentmanager: Storing and Retrieving Content from MIME Parts")
 in the new API, but in certain applications these classes may still be useful, even in non-legacy code.

Ordinarily, you get a message object structure by passing a file or some text to a parser, which parses the text and returns the root message object. However you can also build a complete message structure from scratch, or even individual [`Message`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message "email.message.Message")
 objects by hand. In fact, you can also take an existing structure and add new `Message` objects, move them around, etc. This makes a very convenient interface for slicing-and-dicing MIME messages.

You can create a new object structure by creating [`Message`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message "email.message.Message")
 instances, adding attachments and all the appropriate headers manually. For MIME messages though, the [`email`](https://docs.python.org/3/library/email.html#module-email "email: Package supporting the parsing, manipulating, and generating email messages.")
 package provides some convenient subclasses to make things easier.

Here are the classes:

class email.mime.base.MIMEBase(_\_maintype_, _\_subtype_, _\*_, _policy\=compat32_, _\*\*\_params_)[¶](https://docs.python.org/3/library/email.mime.html#email.mime.base.MIMEBase "Link to this definition")

Module: [`email.mime.base`](https://docs.python.org/3/library/email.mime.html#module-email.mime.base "email.mime.base")

This is the base class for all the MIME-specific subclasses of [`Message`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message "email.message.Message")
. Ordinarily you won’t create instances specifically of `MIMEBase`, although you could. `MIMEBase` is provided primarily as a convenient base class for more specific MIME-aware subclasses.

_\_maintype_ is the _Content-Type_ major type (e.g. _text_ or _image_), and _\_subtype_ is the _Content-Type_ minor type (e.g. _plain_ or _gif_). _\_params_ is a parameter key/value dictionary and is passed directly to [`Message.add_header`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.add_header "email.message.Message.add_header")
.

If _policy_ is specified, (defaults to the [`compat32`](https://docs.python.org/3/library/email.policy.html#email.policy.Compat32 "email.policy.Compat32")
 policy) it will be passed to [`Message`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message "email.message.Message")
.

The `MIMEBase` class always adds a _Content-Type_ header (based on _\_maintype_, _\_subtype_, and _\_params_), and a _MIME-Version_ header (always set to `1.0`).

Changed in version 3.6: Added _policy_ keyword-only parameter.

class email.mime.nonmultipart.MIMENonMultipart[¶](https://docs.python.org/3/library/email.mime.html#email.mime.nonmultipart.MIMENonMultipart "Link to this definition")

Module: [`email.mime.nonmultipart`](https://docs.python.org/3/library/email.mime.html#module-email.mime.nonmultipart "email.mime.nonmultipart")

A subclass of [`MIMEBase`](https://docs.python.org/3/library/email.mime.html#email.mime.base.MIMEBase "email.mime.base.MIMEBase")
, this is an intermediate base class for MIME messages that are not _multipart_. The primary purpose of this class is to prevent the use of the [`attach()`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.attach "email.message.Message.attach")
 method, which only makes sense for _multipart_ messages. If `attach()` is called, a [`MultipartConversionError`](https://docs.python.org/3/library/email.errors.html#email.errors.MultipartConversionError "email.errors.MultipartConversionError")
 exception is raised.

class email.mime.multipart.MIMEMultipart(_\_subtype\='mixed'_, _boundary\=None_, _\_subparts\=None_, _\*_, _policy\=compat32_, _\*\*\_params_)[¶](https://docs.python.org/3/library/email.mime.html#email.mime.multipart.MIMEMultipart "Link to this definition")

Module: [`email.mime.multipart`](https://docs.python.org/3/library/email.mime.html#module-email.mime.multipart "email.mime.multipart")

A subclass of [`MIMEBase`](https://docs.python.org/3/library/email.mime.html#email.mime.base.MIMEBase "email.mime.base.MIMEBase")
, this is an intermediate base class for MIME messages that are _multipart_. Optional _\_subtype_ defaults to _mixed_, but can be used to specify the subtype of the message. A _Content-Type_ header of _multipart/\_subtype_ will be added to the message object. A _MIME-Version_ header will also be added.

Optional _boundary_ is the multipart boundary string. When `None` (the default), the boundary is calculated when needed (for example, when the message is serialized).

_\_subparts_ is a sequence of initial subparts for the payload. It must be possible to convert this sequence to a list. You can always attach new subparts to the message by using the [`Message.attach`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.attach "email.message.Message.attach")
 method.

Optional _policy_ argument defaults to [`compat32`](https://docs.python.org/3/library/email.policy.html#email.policy.Compat32 "email.policy.Compat32")
.

Additional parameters for the _Content-Type_ header are taken from the keyword arguments, or passed into the _\_params_ argument, which is a keyword dictionary.

Changed in version 3.6: Added _policy_ keyword-only parameter.

class email.mime.application.MIMEApplication(_\_data_, _\_subtype\='octet-stream'_, _\_encoder\=email.encoders.encode\_base64_, _\*_, _policy\=compat32_, _\*\*\_params_)[¶](https://docs.python.org/3/library/email.mime.html#email.mime.application.MIMEApplication "Link to this definition")

Module: [`email.mime.application`](https://docs.python.org/3/library/email.mime.html#module-email.mime.application "email.mime.application")

A subclass of [`MIMENonMultipart`](https://docs.python.org/3/library/email.mime.html#email.mime.nonmultipart.MIMENonMultipart "email.mime.nonmultipart.MIMENonMultipart")
, the `MIMEApplication` class is used to represent MIME message objects of major type _application_. _\_data_ contains the bytes for the raw application data. Optional _\_subtype_ specifies the MIME subtype and defaults to _octet-stream_.

Optional _\_encoder_ is a callable (i.e. function) which will perform the actual encoding of the data for transport. This callable takes one argument, which is the `MIMEApplication` instance. It should use [`get_payload()`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.get_payload "email.message.Message.get_payload")
 and [`set_payload()`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.set_payload "email.message.Message.set_payload")
 to change the payload to encoded form. It should also add any _Content-Transfer-Encoding_ or other headers to the message object as necessary. The default encoding is base64. See the [`email.encoders`](https://docs.python.org/3/library/email.encoders.html#module-email.encoders "email.encoders: Encoders for email message payloads.")
 module for a list of the built-in encoders.

Optional _policy_ argument defaults to [`compat32`](https://docs.python.org/3/library/email.policy.html#email.policy.Compat32 "email.policy.Compat32")
.

_\_params_ are passed straight through to the base class constructor.

Changed in version 3.6: Added _policy_ keyword-only parameter.

class email.mime.audio.MIMEAudio(_\_audiodata_, _\_subtype\=None_, _\_encoder\=email.encoders.encode\_base64_, _\*_, _policy\=compat32_, _\*\*\_params_)[¶](https://docs.python.org/3/library/email.mime.html#email.mime.audio.MIMEAudio "Link to this definition")

Module: [`email.mime.audio`](https://docs.python.org/3/library/email.mime.html#module-email.mime.audio "email.mime.audio")

A subclass of [`MIMENonMultipart`](https://docs.python.org/3/library/email.mime.html#email.mime.nonmultipart.MIMENonMultipart "email.mime.nonmultipart.MIMENonMultipart")
, the `MIMEAudio` class is used to create MIME message objects of major type _audio_. _\_audiodata_ contains the bytes for the raw audio data. If this data can be decoded as au, wav, aiff, or aifc, then the subtype will be automatically included in the _Content-Type_ header. Otherwise you can explicitly specify the audio subtype via the _\_subtype_ argument. If the minor type could not be guessed and _\_subtype_ was not given, then [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 is raised.

Optional _\_encoder_ is a callable (i.e. function) which will perform the actual encoding of the audio data for transport. This callable takes one argument, which is the `MIMEAudio` instance. It should use [`get_payload()`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.get_payload "email.message.Message.get_payload")
 and [`set_payload()`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.set_payload "email.message.Message.set_payload")
 to change the payload to encoded form. It should also add any _Content-Transfer-Encoding_ or other headers to the message object as necessary. The default encoding is base64. See the [`email.encoders`](https://docs.python.org/3/library/email.encoders.html#module-email.encoders "email.encoders: Encoders for email message payloads.")
 module for a list of the built-in encoders.

Optional _policy_ argument defaults to [`compat32`](https://docs.python.org/3/library/email.policy.html#email.policy.Compat32 "email.policy.Compat32")
.

_\_params_ are passed straight through to the base class constructor.

Changed in version 3.6: Added _policy_ keyword-only parameter.

class email.mime.image.MIMEImage(_\_imagedata_, _\_subtype\=None_, _\_encoder\=email.encoders.encode\_base64_, _\*_, _policy\=compat32_, _\*\*\_params_)[¶](https://docs.python.org/3/library/email.mime.html#email.mime.image.MIMEImage "Link to this definition")

Module: [`email.mime.image`](https://docs.python.org/3/library/email.mime.html#module-email.mime.image "email.mime.image")

A subclass of [`MIMENonMultipart`](https://docs.python.org/3/library/email.mime.html#email.mime.nonmultipart.MIMENonMultipart "email.mime.nonmultipart.MIMENonMultipart")
, the `MIMEImage` class is used to create MIME message objects of major type _image_. _\_imagedata_ contains the bytes for the raw image data. If this data type can be detected (jpeg, png, gif, tiff, rgb, pbm, pgm, ppm, rast, xbm, bmp, webp, and exr attempted), then the subtype will be automatically included in the _Content-Type_ header. Otherwise you can explicitly specify the image subtype via the _\_subtype_ argument. If the minor type could not be guessed and _\_subtype_ was not given, then [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 is raised.

Optional _\_encoder_ is a callable (i.e. function) which will perform the actual encoding of the image data for transport. This callable takes one argument, which is the `MIMEImage` instance. It should use [`get_payload()`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.get_payload "email.message.Message.get_payload")
 and [`set_payload()`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.set_payload "email.message.Message.set_payload")
 to change the payload to encoded form. It should also add any _Content-Transfer-Encoding_ or other headers to the message object as necessary. The default encoding is base64. See the [`email.encoders`](https://docs.python.org/3/library/email.encoders.html#module-email.encoders "email.encoders: Encoders for email message payloads.")
 module for a list of the built-in encoders.

Optional _policy_ argument defaults to [`compat32`](https://docs.python.org/3/library/email.policy.html#email.policy.Compat32 "email.policy.Compat32")
.

_\_params_ are passed straight through to the [`MIMEBase`](https://docs.python.org/3/library/email.mime.html#email.mime.base.MIMEBase "email.mime.base.MIMEBase")
 constructor.

Changed in version 3.6: Added _policy_ keyword-only parameter.

class email.mime.message.MIMEMessage(_\_msg_, _\_subtype\='rfc822'_, _\*_, _policy\=compat32_)[¶](https://docs.python.org/3/library/email.mime.html#email.mime.message.MIMEMessage "Link to this definition")

Module: [`email.mime.message`](https://docs.python.org/3/library/email.mime.html#module-email.mime.message "email.mime.message")

A subclass of [`MIMENonMultipart`](https://docs.python.org/3/library/email.mime.html#email.mime.nonmultipart.MIMENonMultipart "email.mime.nonmultipart.MIMENonMultipart")
, the `MIMEMessage` class is used to create MIME objects of main type _message_. _\_msg_ is used as the payload, and must be an instance of class [`Message`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message "email.message.Message")
 (or a subclass thereof), otherwise a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 is raised.

Optional _\_subtype_ sets the subtype of the message; it defaults to _rfc822_.

Optional _policy_ argument defaults to [`compat32`](https://docs.python.org/3/library/email.policy.html#email.policy.Compat32 "email.policy.Compat32")
.

Changed in version 3.6: Added _policy_ keyword-only parameter.

class email.mime.text.MIMEText(_\_text_, _\_subtype\='plain'_, _\_charset\=None_, _\*_, _policy\=compat32_)[¶](https://docs.python.org/3/library/email.mime.html#email.mime.text.MIMEText "Link to this definition")

Module: [`email.mime.text`](https://docs.python.org/3/library/email.mime.html#module-email.mime.text "email.mime.text")

A subclass of [`MIMENonMultipart`](https://docs.python.org/3/library/email.mime.html#email.mime.nonmultipart.MIMENonMultipart "email.mime.nonmultipart.MIMENonMultipart")
, the `MIMEText` class is used to create MIME objects of major type _text_. _\_text_ is the string for the payload. _\_subtype_ is the minor type and defaults to _plain_. _\_charset_ is the character set of the text and is passed as an argument to the `MIMENonMultipart` constructor; it defaults to `us-ascii` if the string contains only `ascii` code points, and `utf-8` otherwise. The _\_charset_ parameter accepts either a string or a [`Charset`](https://docs.python.org/3/library/email.charset.html#email.charset.Charset "email.charset.Charset")
 instance.

Unless the _\_charset_ argument is explicitly set to `None`, the MIMEText object created will have both a _Content-Type_ header with a `charset` parameter, and a _Content-Transfer-Encoding_ header. This means that a subsequent `set_payload` call will not result in an encoded payload, even if a charset is passed in the `set_payload` command. You can “reset” this behavior by deleting the `Content-Transfer-Encoding` header, after which a `set_payload` call will automatically encode the new payload (and add a new _Content-Transfer-Encoding_ header).

Optional _policy_ argument defaults to [`compat32`](https://docs.python.org/3/library/email.policy.html#email.policy.Compat32 "email.policy.Compat32")
.

Changed in version 3.5: _\_charset_ also accepts [`Charset`](https://docs.python.org/3/library/email.charset.html#email.charset.Charset "email.charset.Charset")
 instances.

Changed in version 3.6: Added _policy_ keyword-only parameter.

#### Previous topic

[`email.message.Message`: Representing an email message using the `compat32` API](https://docs.python.org/3/library/email.compat32-message.html "previous chapter")

#### Next topic

[`email.header`: Internationalized headers](https://docs.python.org/3/library/email.header.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=email.mime%3A+Creating+email+and+MIME+objects+from+scratch&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Femail.mime.html&pagesource=library%2Femail.mime.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/email.mime.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/email.header.html "email.header: Internationalized headers")
     |
*   [previous](https://docs.python.org/3/library/email.compat32-message.html "email.message.Message: Representing an email message using the compat32 API")
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
*   [`email.mime`: Creating email and MIME objects from scratch](https://docs.python.org/3/library/email.mime.html)
    
*    
    
    |
*   Theme Auto Light Dark |