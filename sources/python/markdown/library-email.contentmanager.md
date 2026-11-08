### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/email.examples.html "email: Examples")
     |
*   [previous](https://docs.python.org/3/library/email.headerregistry.html "email.headerregistry: Custom Header Objects")
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
*   [`email.contentmanager`: Managing MIME Content](https://docs.python.org/3/library/email.contentmanager.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`email.contentmanager`: Managing MIME Content[¶](https://docs.python.org/3/library/email.contentmanager.html#module-email.contentmanager "Link to this heading")

=================================================================================================================================================================

**Source code:** [Lib/email/contentmanager.py](https://github.com/python/cpython/tree/3.15/Lib/email/contentmanager.py)

* * *

Added in version 3.6: [\[1\]](https://docs.python.org/3/library/email.contentmanager.html#id2)

class email.contentmanager.ContentManager[¶](https://docs.python.org/3/library/email.contentmanager.html#email.contentmanager.ContentManager "Link to this definition")

Base class for content managers. Provides the standard registry mechanisms to register converters between MIME content and other representations, as well as the `get_content` and `set_content` dispatch methods.

get\_content(_msg_, _\*args_, _\*\*kw_)[¶](https://docs.python.org/3/library/email.contentmanager.html#email.contentmanager.ContentManager.get_content "Link to this definition")

Look up a handler function based on the `mimetype` of _msg_ (see next paragraph), call it, passing through all arguments, and return the result of the call. The expectation is that the handler will extract the payload from _msg_ and return an object that encodes information about the extracted data.

To find the handler, look for the following keys in the registry, stopping with the first one found:

*   the string representing the full MIME type (`maintype/subtype`)
    
*   the string representing the `maintype`
    
*   the empty string
    

If none of these keys produce a handler, raise a [`KeyError`](https://docs.python.org/3/builtins/exceptions.html#KeyError "KeyError")
 for the full MIME type.

set\_content(_msg_, _obj_, _\*args_, _\*\*kw_)[¶](https://docs.python.org/3/library/email.contentmanager.html#email.contentmanager.ContentManager.set_content "Link to this definition")

If the `maintype` is `multipart`, raise a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
; otherwise look up a handler function based on the type of _obj_ (see next paragraph), call [`clear_content()`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.clear_content "email.message.EmailMessage.clear_content")
 on the _msg_, and call the handler function, passing through all arguments. The expectation is that the handler will transform and store _obj_ into _msg_, possibly making other changes to _msg_ as well, such as adding various MIME headers to encode information needed to interpret the stored data.

To find the handler, obtain the type of _obj_ (`typ = type(obj)`), and look for the following keys in the registry, stopping with the first one found:

*   the type itself (`typ`)
    
*   the type’s fully qualified name (`typ.__module__ + '.' + typ.__qualname__`).
    
*   the type’s [`qualname`](https://docs.python.org/3/reference/datamodel.html#type.__qualname__ "type.__qualname__")
     (`typ.__qualname__`)
    
*   the type’s [`name`](https://docs.python.org/3/reference/datamodel.html#type.__name__ "type.__name__")
     (`typ.__name__`).
    

If none of the above match, repeat all of the checks above for each of the types in the [MRO](https://docs.python.org/3/glossary.html#term-MRO)
 ([`typ.__mro__`](https://docs.python.org/3/reference/datamodel.html#type.__mro__ "type.__mro__")
). Finally, if no other key yields a handler, check for a handler for the key `None`. If there is no handler for `None`, raise a [`KeyError`](https://docs.python.org/3/builtins/exceptions.html#KeyError "KeyError")
 for the fully qualified name of the type.

Also add a _MIME-Version_ header if one is not present (see also [`MIMEPart`](https://docs.python.org/3/library/email.message.html#email.message.MIMEPart "email.message.MIMEPart")
).

add\_get\_handler(_key_, _handler_)[¶](https://docs.python.org/3/library/email.contentmanager.html#email.contentmanager.ContentManager.add_get_handler "Link to this definition")

Record the function _handler_ as the handler for _key_. For the possible values of _key_, see [`get_content()`](https://docs.python.org/3/library/email.contentmanager.html#email.contentmanager.get_content "email.contentmanager.get_content")
.

add\_set\_handler(_typekey_, _handler_)[¶](https://docs.python.org/3/library/email.contentmanager.html#email.contentmanager.ContentManager.add_set_handler "Link to this definition")

Record _handler_ as the function to call when an object of a type matching _typekey_ is passed to [`set_content()`](https://docs.python.org/3/library/email.contentmanager.html#email.contentmanager.set_content "email.contentmanager.set_content")
. For the possible values of _typekey_, see `set_content()`.

Content Manager Instances[¶](https://docs.python.org/3/library/email.contentmanager.html#content-manager-instances "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------

Currently the email package provides only one concrete content manager, [`raw_data_manager`](https://docs.python.org/3/library/email.contentmanager.html#email.contentmanager.raw_data_manager "email.contentmanager.raw_data_manager")
, although more may be added in the future. `raw_data_manager` is the [`content_manager`](https://docs.python.org/3/library/email.policy.html#email.policy.EmailPolicy.content_manager "email.policy.EmailPolicy.content_manager")
 provided by [`EmailPolicy`](https://docs.python.org/3/library/email.policy.html#email.policy.EmailPolicy "email.policy.EmailPolicy")
 and its derivatives.

email.contentmanager.raw\_data\_manager[¶](https://docs.python.org/3/library/email.contentmanager.html#email.contentmanager.raw_data_manager "Link to this definition")

This content manager provides only a minimum interface beyond that provided by [`Message`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message "email.message.Message")
 itself: it deals only with text, raw bytes, and `Message` objects. Nevertheless, it provides significant advantages compared to the base API: `get_content` on a text part will return a string without the application needing to manually decode it, `set_content` provides a rich set of options for controlling the headers added to a part and controlling the content transfer encoding, and it enables the use of the various `add_` methods, thereby simplifying the creation of multipart messages.

email.contentmanager.get\_content(_msg_, _errors\='replace'_)[¶](https://docs.python.org/3/library/email.contentmanager.html#email.contentmanager.get_content "Link to this definition")

Return the payload of the part as either a string (for `text` parts), an [`EmailMessage`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage "email.message.EmailMessage")
 object (for `message/rfc822` parts), or a `bytes` object (for all other non-multipart types). Raise a [`KeyError`](https://docs.python.org/3/builtins/exceptions.html#KeyError "KeyError")
 if called on a `multipart`. If the part is a `text` part and _errors_ is specified, use it as the error handler when decoding the payload to a string. The default error handler is `replace`.

email.contentmanager.set\_content(_msg_, _<'str'>_, _subtype\="plain"_, _charset\='utf-8'_, _cte\=None_, _disposition\=None_, _filename\=None_, _cid\=None_, _params\=None_, _headers\=None_)[¶](https://docs.python.org/3/library/email.contentmanager.html#email.contentmanager.set_content "Link to this definition")

email.contentmanager.set\_content(_msg_, _<'bytes'>_, _maintype_, _subtype_, _cte\="base64"_, _disposition\=None_, _filename\=None_, _cid\=None_, _params\=None_, _headers\=None_)

email.contentmanager.set\_content(_msg_, _<'EmailMessage'>_, _cte\=None_, _disposition\=None_, _filename\=None_, _cid\=None_, _params\=None_, _headers\=None_)

Add headers and payload to _msg_:

Add a _Content-Type_ header with a `maintype/subtype` value.

*   For `str`, set the MIME `maintype` to `text`, and set the subtype to _subtype_ if it is specified, or `plain` if it is not.
    
*   For `bytes`, use the specified _maintype_ and _subtype_, or raise a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
     if they are not specified.
    
*   For [`EmailMessage`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage "email.message.EmailMessage")
     objects, set the maintype to `message`, and set the subtype to _subtype_ if it is specified or `rfc822` if it is not. If _subtype_ is `partial`, raise an error (`bytes` objects must be used to construct `message/partial` parts).
    

If _charset_ is provided (which is valid only for `str`), encode the string to bytes using the specified character set. The default is `utf-8`. If the specified _charset_ is a known alias for a standard MIME charset name, use the standard charset instead.

If _cte_ is set, encode the payload using the specified content transfer encoding, and set the _Content-Transfer-Encoding_ header to that value. Possible values for _cte_ are `quoted-printable`, `base64`, `7bit`, `8bit`, and `binary`. If the input cannot be encoded in the specified encoding (for example, specifying a _cte_ of `7bit` for an input that contains non-ASCII values), raise a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
.

*   For `str` objects, if _cte_ is not set use heuristics to determine the most compact encoding. Prior to encoding, [`str.splitlines()`](https://docs.python.org/3/builtins/stdtypes.html#str.splitlines "str.splitlines")
     is used to normalize all line boundaries, ensuring that each line of the payload is terminated by the current policy’s [`linesep`](https://docs.python.org/3/library/email.policy.html#email.policy.Policy.linesep "email.policy.Policy.linesep")
     property (even if the original string did not end with one).
    
*   For `bytes` objects, _cte_ is taken to be base64 if not set, and the aforementioned newline translation is not performed.
    
*   For [`EmailMessage`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage "email.message.EmailMessage")
    , per [**RFC 2046**](https://datatracker.ietf.org/doc/html/rfc2046.html)
    , raise an error if a _cte_ of `quoted-printable` or `base64` is requested for _subtype_ `rfc822`, and for any _cte_ other than `7bit` for _subtype_ `external-body`. For `message/rfc822`, use `8bit` if _cte_ is not specified. For all other values of _subtype_, use `7bit`.
    

Note

A _cte_ of `binary` does not actually work correctly yet. The `EmailMessage` object as modified by `set_content` is correct, but [`BytesGenerator`](https://docs.python.org/3/library/email.generator.html#email.generator.BytesGenerator "email.generator.BytesGenerator")
 does not serialize it correctly.

If _disposition_ is set, use it as the value of the _Content-Disposition_ header. If not specified, and _filename_ is specified, add the header with the value `attachment`. If _disposition_ is not specified and _filename_ is also not specified, do not add the header. The only valid values for _disposition_ are `attachment` and `inline`.

If _filename_ is specified, use it as the value of the `filename` parameter of the _Content-Disposition_ header.

If _cid_ is specified, add a _Content-ID_ header with _cid_ as its value.

If _params_ is specified, iterate its `items` method and use the resulting `(key, value)` pairs to set additional parameters on the _Content-Type_ header.

If _headers_ is specified and is a list of strings of the form `headername: headervalue` or a list of `header` objects (distinguished from strings by having a `name` attribute), add the headers to _msg_.

Footnotes

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`email.contentmanager`: Managing MIME Content](https://docs.python.org/3/library/email.contentmanager.html#)
    *   [Content Manager Instances](https://docs.python.org/3/library/email.contentmanager.html#content-manager-instances)
        

#### Previous topic

[`email.headerregistry`: Custom Header Objects](https://docs.python.org/3/library/email.headerregistry.html "previous chapter")

#### Next topic

[`email`: Examples](https://docs.python.org/3/library/email.examples.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=email.contentmanager%3A+Managing+MIME+Content&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Femail.contentmanager.html&pagesource=library%2Femail.contentmanager.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/email.contentmanager.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/email.examples.html "email: Examples")
     |
*   [previous](https://docs.python.org/3/library/email.headerregistry.html "email.headerregistry: Custom Header Objects")
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
*   [`email.contentmanager`: Managing MIME Content](https://docs.python.org/3/library/email.contentmanager.html)
    
*    
    
    |
*   Theme Auto Light Dark |