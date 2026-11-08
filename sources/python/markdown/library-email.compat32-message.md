### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/email.mime.html "email.mime: Creating email and MIME objects from scratch")
     |
*   [previous](https://docs.python.org/3/library/email.examples.html "email: Examples")
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
*   [`email.message.Message`: Representing an email message using the `compat32` API](https://docs.python.org/3/library/email.compat32-message.html)
    
*    
    
    |
*   Theme Auto Light Dark |

[`email.message.Message`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message "email.message.Message")
: Representing an email message using the [`compat32`](https://docs.python.org/3/library/email.policy.html#email.policy.compat32 "email.policy.compat32")
 API[¶](https://docs.python.org/3/library/email.compat32-message.html#email-message-message-representing-an-email-message-using-the-compat32-api "Link to this heading")

==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================

The [`Message`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message "email.message.Message")
 class is very similar to the [`EmailMessage`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage "email.message.EmailMessage")
 class, without the methods added by that class, and with the default behavior of certain other methods being slightly different. We also document here some methods that, while supported by the `EmailMessage` class, are not recommended unless you are dealing with legacy code.

The philosophy and structure of the two classes is otherwise the same.

This document describes the behavior under the default (for [`Message`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message "email.message.Message")
) policy [`Compat32`](https://docs.python.org/3/library/email.policy.html#email.policy.Compat32 "email.policy.Compat32")
. If you are going to use another policy, you should be using the [`EmailMessage`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage "email.message.EmailMessage")
 class instead.

An email message consists of _headers_ and a _payload_. Headers must be [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html)
 style names and values, where the field name and value are separated by a colon. The colon is not part of either the field name or the field value. The payload may be a simple text message, or a binary object, or a structured sequence of sub-messages each with their own set of headers and their own payload. The latter type of payload is indicated by the message having a MIME type such as _multipart/\*_ or _message/rfc822_.

The conceptual model provided by a [`Message`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message "email.message.Message")
 object is that of an ordered dictionary of headers with additional methods for accessing both specialized information from the headers, for accessing the payload, for generating a serialized version of the message, and for recursively walking over the object tree. Note that duplicate headers are supported but special methods must be used to access them.

The [`Message`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message "email.message.Message")
 pseudo-dictionary is indexed by the header names, which must be ASCII values. The values of the dictionary are strings that are supposed to contain only ASCII characters; there is some special handling for non-ASCII input, but it doesn’t always produce the correct results. Headers are stored and returned in case-preserving form, but field names are matched case-insensitively. There may also be a single envelope header, also known as the _Unix-From_ header or the `From_` header. The _payload_ is either a string or bytes, in the case of simple message objects, or a list of `Message` objects, for MIME container documents (e.g. _multipart/\*_ and _message/rfc822_).

Here are the methods of the [`Message`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message "email.message.Message")
 class:

class email.message.Message(_policy\=compat32_)[¶](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message "Link to this definition")

If _policy_ is specified (it must be an instance of a [`policy`](https://docs.python.org/3/library/email.policy.html#module-email.policy "email.policy: Controlling the parsing and generating of messages")
 class) use the rules it specifies to update and serialize the representation of the message. If _policy_ is not set, use the [`compat32`](https://docs.python.org/3/library/email.policy.html#email.policy.Compat32 "email.policy.Compat32")
 policy, which maintains backward compatibility with the Python 3.2 version of the email package. For more information see the `policy` documentation.

Changed in version 3.3: The _policy_ keyword argument was added.

as\_string(_unixfrom\=False_, _maxheaderlen\=0_, _policy\=None_)[¶](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.as_string "Link to this definition")

Return the entire message flattened as a string. When optional _unixfrom_ is true, the envelope header is included in the returned string. _unixfrom_ defaults to `False`. For backward compatibility reasons, _maxheaderlen_ defaults to `0`, so if you want a different value you must override it explicitly (the value specified for _max\_line\_length_ in the policy will be ignored by this method). The _policy_ argument may be used to override the default policy obtained from the message instance. This can be used to control some of the formatting produced by the method, since the specified _policy_ will be passed to the `Generator`.

Flattening the message may trigger changes to the `Message` if defaults need to be filled in to complete the transformation to a string (for example, MIME boundaries may be generated or modified).

Note that this method is provided as a convenience and may not always format the message the way you want. For example, by default it does not do the mangling of lines that begin with `From` that is required by the Unix mbox format. For more flexibility, instantiate a [`Generator`](https://docs.python.org/3/library/email.generator.html#email.generator.Generator "email.generator.Generator")
 instance and use its [`flatten()`](https://docs.python.org/3/library/email.generator.html#email.generator.Generator.flatten "email.generator.Generator.flatten")
 method directly. For example:

Copy

from io import StringIO
from email.generator import Generator
fp \= StringIO()
g \= Generator(fp, mangle\_from\_\=True, maxheaderlen\=60)
g.flatten(msg)
text \= fp.getvalue()

If the message object contains binary data that is not encoded according to RFC standards, the non-compliant data will be replaced by Unicode “unknown character” code points. (See also [`as_bytes()`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.as_bytes "email.message.Message.as_bytes")
 and [`BytesGenerator`](https://docs.python.org/3/library/email.generator.html#email.generator.BytesGenerator "email.generator.BytesGenerator")
.)

Changed in version 3.4: the _policy_ keyword argument was added.

\_\_str\_\_()[¶](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.__str__ "Link to this definition")

Equivalent to [`as_string()`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.as_string "email.message.Message.as_string")
. Allows `str(msg)` to produce a string containing the formatted message.

as\_bytes(_unixfrom\=False_, _policy\=None_)[¶](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.as_bytes "Link to this definition")

Return the entire message flattened as a bytes object. When optional _unixfrom_ is true, the envelope header is included in the returned string. _unixfrom_ defaults to `False`. The _policy_ argument may be used to override the default policy obtained from the message instance. This can be used to control some of the formatting produced by the method, since the specified _policy_ will be passed to the `BytesGenerator`.

Flattening the message may trigger changes to the `Message` if defaults need to be filled in to complete the transformation to a string (for example, MIME boundaries may be generated or modified).

Note that this method is provided as a convenience and may not always format the message the way you want. For example, by default it does not do the mangling of lines that begin with `From` that is required by the Unix mbox format. For more flexibility, instantiate a [`BytesGenerator`](https://docs.python.org/3/library/email.generator.html#email.generator.BytesGenerator "email.generator.BytesGenerator")
 instance and use its [`flatten()`](https://docs.python.org/3/library/email.generator.html#email.generator.BytesGenerator.flatten "email.generator.BytesGenerator.flatten")
 method directly. For example:

Copy

from io import BytesIO
from email.generator import BytesGenerator
fp \= BytesIO()
g \= BytesGenerator(fp, mangle\_from\_\=True, maxheaderlen\=60)
g.flatten(msg)
text \= fp.getvalue()

Added in version 3.4.

\_\_bytes\_\_()[¶](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.__bytes__ "Link to this definition")

Equivalent to [`as_bytes()`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.as_bytes "email.message.Message.as_bytes")
. Allows `bytes(msg)` to produce a bytes object containing the formatted message.

Added in version 3.4.

is\_multipart()[¶](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.is_multipart "Link to this definition")

Return `True` if the message’s payload is a list of sub-`Message` objects, otherwise return `False`. When `is_multipart()` returns `False`, the payload should be a string object (which might be a CTE encoded binary payload). (Note that `is_multipart()` returning `True` does not necessarily mean that “msg.get\_content\_maintype() == ‘multipart’” will return the `True`. For example, `is_multipart` will return `True` when the `Message` is of type `message/rfc822`.)

set\_unixfrom(_unixfrom_)[¶](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.set_unixfrom "Link to this definition")

Set the message’s envelope header to _unixfrom_, which should be a string.

get\_unixfrom()[¶](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.get_unixfrom "Link to this definition")

Return the message’s envelope header. Defaults to `None` if the envelope header was never set.

attach(_payload_)[¶](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.attach "Link to this definition")

Add the given _payload_ to the current payload, which must be `None` or a list of `Message` objects before the call. After the call, the payload will always be a list of `Message` objects. If you want to set the payload to a scalar object (e.g. a string), use [`set_payload()`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.set_payload "email.message.Message.set_payload")
 instead.

This is a legacy method. On the [`EmailMessage`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage "email.message.EmailMessage")
 class its functionality is replaced by [`set_content()`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.set_content "email.message.EmailMessage.set_content")
 and the related `make` and `add` methods.

get\_payload(_i\=None_, _decode\=False_)[¶](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.get_payload "Link to this definition")

Return the current payload, which will be a list of `Message` objects when [`is_multipart()`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.is_multipart "email.message.Message.is_multipart")
 is `True`, or a string when `is_multipart()` is `False`. If the payload is a list and you mutate the list object, you modify the message’s payload in place.

With optional argument _i_, `get_payload()` will return the _i_\-th element of the payload, counting from zero, if [`is_multipart()`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.is_multipart "email.message.Message.is_multipart")
 is `True`. An [`IndexError`](https://docs.python.org/3/builtins/exceptions.html#IndexError "IndexError")
 will be raised if _i_ is less than 0 or greater than or equal to the number of items in the payload. If the payload is a string (i.e. `is_multipart()` is `False`) and _i_ is given, a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 is raised.

Optional _decode_ is a flag indicating whether the payload should be decoded or not, according to the _Content-Transfer-Encoding_ header. When `True` and the message is not a multipart, the payload will be decoded if this header’s value is `quoted-printable` or `base64`. If some other encoding is used, or _Content-Transfer-Encoding_ header is missing, the payload is returned as-is (undecoded). In all cases the returned value is binary data. If the message is a multipart and the _decode_ flag is `True`, then `None` is returned. If the payload is base64 and it was not perfectly formed (missing padding, characters outside the base64 alphabet), then an appropriate defect will be added to the message’s defect property ([`InvalidBase64PaddingDefect`](https://docs.python.org/3/library/email.errors.html#email.errors.InvalidBase64PaddingDefect "email.errors.InvalidBase64PaddingDefect")
 or [`InvalidBase64CharactersDefect`](https://docs.python.org/3/library/email.errors.html#email.errors.InvalidBase64CharactersDefect "email.errors.InvalidBase64CharactersDefect")
, respectively).

When _decode_ is `False` (the default) the body is returned as a string without decoding the _Content-Transfer-Encoding_. However, for a _Content-Transfer-Encoding_ of 8bit, an attempt is made to decode the original bytes using the `charset` specified by the _Content-Type_ header, using the `replace` error handler. If no `charset` is specified, or if the `charset` given is not recognized by the email package, the body is decoded using the default ASCII charset.

This is a legacy method. On the [`EmailMessage`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage "email.message.EmailMessage")
 class its functionality is replaced by [`get_content()`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.get_content "email.message.EmailMessage.get_content")
 and [`iter_parts()`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.iter_parts "email.message.EmailMessage.iter_parts")
.

set\_payload(_payload_, _charset\=None_)[¶](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.set_payload "Link to this definition")

Set the entire message object’s payload to _payload_. It is the client’s responsibility to ensure the payload invariants. Optional _charset_ sets the message’s default character set; see [`set_charset()`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.set_charset "email.message.Message.set_charset")
 for details.

This is a legacy method. On the [`EmailMessage`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage "email.message.EmailMessage")
 class its functionality is replaced by [`set_content()`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.set_content "email.message.EmailMessage.set_content")
.

set\_charset(_charset_)[¶](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.set_charset "Link to this definition")

Set the character set of the payload to _charset_, which can either be a [`Charset`](https://docs.python.org/3/library/email.charset.html#email.charset.Charset "email.charset.Charset")
 instance (see [`email.charset`](https://docs.python.org/3/library/email.charset.html#module-email.charset "email.charset: Character Sets")
), a string naming a character set, or `None`. If it is a string, it will be converted to a `Charset` instance. If _charset_ is `None`, the `charset` parameter will be removed from the _Content-Type_ header (the message will not be otherwise modified). Anything else will generate a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
.

If there is no existing _MIME-Version_ header one will be added. If there is no existing _Content-Type_ header, one will be added with a value of _text/plain_. Whether the _Content-Type_ header already exists or not, its `charset` parameter will be set to _charset.output\_charset_. If _charset.input\_charset_ and _charset.output\_charset_ differ, the payload will be re-encoded to the _output\_charset_. If there is no existing _Content-Transfer-Encoding_ header, then the payload will be transfer-encoded, if needed, using the specified [`Charset`](https://docs.python.org/3/library/email.charset.html#email.charset.Charset "email.charset.Charset")
, and a header with the appropriate value will be added. If a _Content-Transfer-Encoding_ header already exists, the payload is assumed to already be correctly encoded using that _Content-Transfer-Encoding_ and is not modified.

This is a legacy method. On the [`EmailMessage`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage "email.message.EmailMessage")
 class its functionality is replaced by the _charset_ parameter of the [`email.message.EmailMessage.set_content()`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.set_content "email.message.EmailMessage.set_content")
 method.

get\_charset()[¶](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.get_charset "Link to this definition")

Return the [`Charset`](https://docs.python.org/3/library/email.charset.html#email.charset.Charset "email.charset.Charset")
 instance associated with the message’s payload.

This is a legacy method. On the [`EmailMessage`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage "email.message.EmailMessage")
 class it always returns `None`.

The following methods implement a mapping-like interface for accessing the message’s [**RFC 2822**](https://datatracker.ietf.org/doc/html/rfc2822.html)
 headers. Note that there are some semantic differences between these methods and a normal mapping (i.e. dictionary) interface. For example, in a dictionary there are no duplicate keys, but here there may be duplicate message headers. Also, in dictionaries there is no guaranteed order to the keys returned by [`keys()`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.keys "email.message.Message.keys")
, but in a `Message` object, headers are always returned in the order they appeared in the original message, or were added to the message later. Any header deleted and then re-added are always appended to the end of the header list.

These semantic differences are intentional and are biased toward maximal convenience.

Note that in all cases, any envelope header present in the message is not included in the mapping interface.

In a model generated from bytes, any header values that (in contravention of the RFCs) contain non-ASCII bytes will, when retrieved through this interface, be represented as [`Header`](https://docs.python.org/3/library/email.header.html#email.header.Header "email.header.Header")
 objects with a charset of `unknown-8bit`.

\_\_len\_\_()[¶](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.__len__ "Link to this definition")

Return the total number of headers, including duplicates.

\_\_contains\_\_(_name_)[¶](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.__contains__ "Link to this definition")

Return `True` if the message object has a field named _name_. Matching is done case-insensitively and _name_ should not include the trailing colon. Used for the `in` operator, e.g.:

Copy

if 'message-id' in myMessage:
   print('Message-ID:', myMessage\['message-id'\])

\_\_getitem\_\_(_name_)[¶](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.__getitem__ "Link to this definition")

Return the value of the named header field. _name_ should not include the colon field separator. If the header is missing, `None` is returned; a [`KeyError`](https://docs.python.org/3/builtins/exceptions.html#KeyError "KeyError")
 is never raised.

Note that if the named field appears more than once in the message’s headers, exactly which of those field values will be returned is undefined. Use the [`get_all()`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.get_all "email.message.Message.get_all")
 method to get the values of all the extant named headers.

\_\_setitem\_\_(_name_, _val_)[¶](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.__setitem__ "Link to this definition")

Add a header to the message with field name _name_ and value _val_. The field is appended to the end of the message’s existing fields.

Note that this does _not_ overwrite or delete any existing header with the same name. If you want to ensure that the new header is the only one present in the message with field name _name_, delete the field first, e.g.:

Copy

del msg\['subject'\]
msg\['subject'\] \= 'Python roolz!'

\_\_delitem\_\_(_name_)[¶](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.__delitem__ "Link to this definition")

Delete all occurrences of the field with name _name_ from the message’s headers. No exception is raised if the named field isn’t present in the headers.

keys()[¶](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.keys "Link to this definition")

Return a list of all the message’s header field names.

values()[¶](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.values "Link to this definition")

Return a list of all the message’s field values.

items()[¶](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.items "Link to this definition")

Return a list of 2-tuples containing all the message’s field headers and values.

get(_name_, _failobj\=None_)[¶](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.get "Link to this definition")

Return the value of the named header field. This is identical to [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__")
 except that optional _failobj_ is returned if the named header is missing (defaults to `None`).

Here are some additional useful methods:

get\_all(_name_, _failobj\=None_)[¶](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.get_all "Link to this definition")

Return a list of all the values for the field named _name_. If there are no such named headers in the message, _failobj_ is returned (defaults to `None`).

add\_header(_\_name_, _\_value_, _\*\*\_params_)[¶](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.add_header "Link to this definition")

Extended header setting. This method is similar to [`__setitem__()`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.__setitem__ "email.message.Message.__setitem__")
 except that additional header parameters can be provided as keyword arguments. _\_name_ is the header field to add and _\_value_ is the _primary_ value for the header.

For each item in the keyword argument dictionary _\_params_, the key is taken as the parameter name, with underscores converted to dashes (since dashes are illegal in Python identifiers). Normally, the parameter will be added as `key="value"` unless the value is `None`, in which case only the key will be added. If the value contains non-ASCII characters, it can be specified as a three tuple in the format `(CHARSET, LANGUAGE, VALUE)`, where `CHARSET` is a string naming the charset to be used to encode the value, `LANGUAGE` can usually be set to `None` or the empty string (see [**RFC 2231**](https://datatracker.ietf.org/doc/html/rfc2231.html)
 for other possibilities), and `VALUE` is the string value containing non-ASCII code points. If a three tuple is not passed and the value contains non-ASCII characters, it is automatically encoded in [**RFC 2231**](https://datatracker.ietf.org/doc/html/rfc2231.html)
 format using a `CHARSET` of `utf-8` and a `LANGUAGE` of `None`.

Here’s an example:

Copy

msg.add\_header('Content-Disposition', 'attachment', filename\='bud.gif')

This will add a header that looks like

Copy

Content\-Disposition: attachment; filename\="bud.gif"

An example with non-ASCII characters:

Copy

msg.add\_header('Content-Disposition', 'attachment',
               filename\=('iso-8859-1', '', 'Fußballer.ppt'))

Which produces

Copy

Content\-Disposition: attachment; filename\*="iso-8859-1''Fu%DFballer.ppt"

replace\_header(_\_name_, _\_value_)[¶](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.replace_header "Link to this definition")

Replace a header. Replace the first header found in the message that matches _\_name_, retaining header order and field name case. If no matching header was found, a [`KeyError`](https://docs.python.org/3/builtins/exceptions.html#KeyError "KeyError")
 is raised.

get\_content\_type()[¶](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.get_content_type "Link to this definition")

Return the message’s content type. The returned string is coerced to lower case of the form _maintype/subtype_. If there was no _Content-Type_ header in the message the default type as given by [`get_default_type()`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.get_default_type "email.message.Message.get_default_type")
 will be returned. Since according to [**RFC 2045**](https://datatracker.ietf.org/doc/html/rfc2045.html)
, messages always have a default type, `get_content_type()` will always return a value.

[**RFC 2045**](https://datatracker.ietf.org/doc/html/rfc2045.html)
 defines a message’s default type to be _text/plain_ unless it appears inside a _multipart/digest_ container, in which case it would be _message/rfc822_. If the _Content-Type_ header has an invalid type specification, [**RFC 2045**](https://datatracker.ietf.org/doc/html/rfc2045.html)
 mandates that the default type be _text/plain_.

get\_content\_maintype()[¶](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.get_content_maintype "Link to this definition")

Return the message’s main content type. This is the _maintype_ part of the string returned by [`get_content_type()`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.get_content_type "email.message.Message.get_content_type")
.

get\_content\_subtype()[¶](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.get_content_subtype "Link to this definition")

Return the message’s sub-content type. This is the _subtype_ part of the string returned by [`get_content_type()`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.get_content_type "email.message.Message.get_content_type")
.

get\_default\_type()[¶](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.get_default_type "Link to this definition")

Return the default content type. Most messages have a default content type of _text/plain_, except for messages that are subparts of _multipart/digest_ containers. Such subparts have a default content type of _message/rfc822_.

set\_default\_type(_ctype_)[¶](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.set_default_type "Link to this definition")

Set the default content type. _ctype_ should either be _text/plain_ or _message/rfc822_, although this is not enforced. The default content type is not stored in the _Content-Type_ header.

get\_params(_failobj\=None_, _header\='content-type'_, _unquote\=True_)[¶](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.get_params "Link to this definition")

Return the message’s _Content-Type_ parameters, as a list. The elements of the returned list are 2-tuples of key/value pairs, as split on the `'='` sign. The left hand side of the `'='` is the key, while the right hand side is the value. If there is no `'='` sign in the parameter the value is the empty string, otherwise the value is as described in [`get_param()`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.get_param "email.message.Message.get_param")
 and is unquoted if optional _unquote_ is `True` (the default).

Optional _failobj_ is the object to return if there is no _Content-Type_ header. Optional _header_ is the header to search instead of _Content-Type_.

This is a legacy method. On the [`EmailMessage`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage "email.message.EmailMessage")
 class its functionality is replaced by the _params_ property of the individual header objects returned by the header access methods.

get\_param(_param_, _failobj\=None_, _header\='content-type'_, _unquote\=True_)[¶](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.get_param "Link to this definition")

Return the value of the _Content-Type_ header’s parameter _param_ as a string. If the message has no _Content-Type_ header or if there is no such parameter, then _failobj_ is returned (defaults to `None`).

Optional _header_ if given, specifies the message header to use instead of _Content-Type_.

Parameter keys are always compared case insensitively. The return value can either be a string, or a 3-tuple if the parameter was [**RFC 2231**](https://datatracker.ietf.org/doc/html/rfc2231.html)
 encoded. When it’s a 3-tuple, the elements of the value are of the form `(CHARSET, LANGUAGE, VALUE)`. Note that both `CHARSET` and `LANGUAGE` can be `None`, in which case you should consider `VALUE` to be encoded in the `us-ascii` charset. You can usually ignore `LANGUAGE`.

If your application doesn’t care whether the parameter was encoded as in [**RFC 2231**](https://datatracker.ietf.org/doc/html/rfc2231.html)
, you can collapse the parameter value by calling [`email.utils.collapse_rfc2231_value()`](https://docs.python.org/3/library/email.utils.html#email.utils.collapse_rfc2231_value "email.utils.collapse_rfc2231_value")
, passing in the return value from `get_param()`. This will return a suitably decoded Unicode string when the value is a tuple, or the original string unquoted if it isn’t. For example:

Copy

rawparam \= msg.get\_param('foo')
param \= email.utils.collapse\_rfc2231\_value(rawparam)

In any case, the parameter value (either the returned string, or the `VALUE` item in the 3-tuple) is always unquoted, unless _unquote_ is set to `False`.

This is a legacy method. On the [`EmailMessage`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage "email.message.EmailMessage")
 class its functionality is replaced by the _params_ property of the individual header objects returned by the header access methods.

set\_param(_param_, _value_, _header\='Content-Type'_, _requote\=True_, _charset\=None_, _language\=''_, _replace\=False_)[¶](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.set_param "Link to this definition")

Set a parameter in the _Content-Type_ header. If the parameter already exists in the header, its value will be replaced with _value_. If the _Content-Type_ header as not yet been defined for this message, it will be set to _text/plain_ and the new parameter value will be appended as per [**RFC 2045**](https://datatracker.ietf.org/doc/html/rfc2045.html)
.

Optional _header_ specifies an alternative header to _Content-Type_, and all parameters will be quoted as necessary unless optional _requote_ is `False` (the default is `True`).

If optional _charset_ is specified, the parameter will be encoded according to [**RFC 2231**](https://datatracker.ietf.org/doc/html/rfc2231.html)
. Optional _language_ specifies the RFC 2231 language, defaulting to the empty string. Both _charset_ and _language_ should be strings.

If _replace_ is `False` (the default) the header is moved to the end of the list of headers. If _replace_ is `True`, the header will be updated in place.

Changed in version 3.4: `replace` keyword was added.

del\_param(_param_, _header\='content-type'_, _requote\=True_)[¶](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.del_param "Link to this definition")

Remove the given parameter completely from the _Content-Type_ header. The header will be re-written in place without the parameter or its value. All values will be quoted as necessary unless _requote_ is `False` (the default is `True`). Optional _header_ specifies an alternative to _Content-Type_.

set\_type(_type_, _header\='Content-Type'_, _requote\=True_)[¶](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.set_type "Link to this definition")

Set the main type and subtype for the _Content-Type_ header. _type_ must be a string in the form _maintype/subtype_, otherwise a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 is raised.

This method replaces the _Content-Type_ header, keeping all the parameters in place. If _requote_ is `False`, this leaves the existing header’s quoting as is, otherwise the parameters will be quoted (the default).

An alternative header can be specified in the _header_ argument. When the _Content-Type_ header is set a _MIME-Version_ header is also added.

This is a legacy method. On the [`EmailMessage`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage "email.message.EmailMessage")
 class its functionality is replaced by the `make_` and `add_` methods.

get\_filename(_failobj\=None_)[¶](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.get_filename "Link to this definition")

Return the value of the `filename` parameter of the _Content-Disposition_ header of the message. If the header does not have a `filename` parameter, this method falls back to looking for the `name` parameter on the _Content-Type_ header. If neither is found, or the header is missing, then _failobj_ is returned. The returned string will always be unquoted as per [`email.utils.unquote()`](https://docs.python.org/3/library/email.utils.html#email.utils.unquote "email.utils.unquote")
.

get\_boundary(_failobj\=None_)[¶](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.get_boundary "Link to this definition")

Return the value of the `boundary` parameter of the _Content-Type_ header of the message, or _failobj_ if either the header is missing, or has no `boundary` parameter. The returned string will always be unquoted as per [`email.utils.unquote()`](https://docs.python.org/3/library/email.utils.html#email.utils.unquote "email.utils.unquote")
.

set\_boundary(_boundary_)[¶](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.set_boundary "Link to this definition")

Set the `boundary` parameter of the _Content-Type_ header to _boundary_. `set_boundary()` will always quote _boundary_ if necessary. A [`HeaderParseError`](https://docs.python.org/3/library/email.errors.html#email.errors.HeaderParseError "email.errors.HeaderParseError")
 is raised if the message object has no _Content-Type_ header.

Note that using this method is subtly different than deleting the old _Content-Type_ header and adding a new one with the new boundary via [`add_header()`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.add_header "email.message.Message.add_header")
, because `set_boundary()` preserves the order of the _Content-Type_ header in the list of headers. However, it does _not_ preserve any continuation lines which may have been present in the original _Content-Type_ header.

get\_content\_charset(_failobj\=None_)[¶](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.get_content_charset "Link to this definition")

Return the `charset` parameter of the _Content-Type_ header, coerced to lower case. If there is no _Content-Type_ header, or if that header has no `charset` parameter, _failobj_ is returned.

Note that this method differs from [`get_charset()`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.get_charset "email.message.Message.get_charset")
 which returns the [`Charset`](https://docs.python.org/3/library/email.charset.html#email.charset.Charset "email.charset.Charset")
 instance for the default encoding of the message body.

get\_charsets(_failobj\=None_)[¶](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.get_charsets "Link to this definition")

Return a list containing the character set names in the message. If the message is a _multipart_, then the list will contain one element for each subpart in the payload, otherwise, it will be a list of length 1.

Each item in the list will be a string which is the value of the `charset` parameter in the _Content-Type_ header for the represented subpart. However, if the subpart has no _Content-Type_ header, no `charset` parameter, or is not of the _text_ main MIME type, then that item in the returned list will be _failobj_.

get\_content\_disposition()[¶](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.get_content_disposition "Link to this definition")

Return the lowercased value (without parameters) of the message’s _Content-Disposition_ header if it has one, or `None`. The possible values for this method are _inline_, _attachment_ or `None` if the message follows [**RFC 2183**](https://datatracker.ietf.org/doc/html/rfc2183.html)
.

Added in version 3.5.

walk()[¶](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.walk "Link to this definition")

The `walk()` method is an all-purpose generator which can be used to iterate over all the parts and subparts of a message object tree, in depth-first traversal order. You will typically use `walk()` as the iterator in a `for` loop; each iteration returns the next subpart.

Here’s an example that prints the MIME type of every part of a multipart message structure:

Copy

\>>> for part in msg.walk():
...     print(part.get\_content\_type())
multipart/report
text/plain
message/delivery-status
text/plain
text/plain
message/rfc822
text/plain

`walk` iterates over the subparts of any part where [`is_multipart()`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.is_multipart "email.message.Message.is_multipart")
 returns `True`, even though `msg.get_content_maintype() == 'multipart'` may return `False`. We can see this in our example by making use of the `_structure` debug helper function:

Copy

\>>> for part in msg.walk():
...     print(part.get\_content\_maintype() \== 'multipart',
...           part.is\_multipart())
True True
False False
False True
False False
False False
False True
False False
\>>> \_structure(msg)
multipart/report
    text/plain
    message/delivery-status
        text/plain
        text/plain
    message/rfc822
        text/plain

Here the `message` parts are not `multiparts`, but they do contain subparts. `is_multipart()` returns `True` and `walk` descends into the subparts.

`Message` objects can also optionally contain two instance attributes, which can be used when generating the plain text of a MIME message.

preamble[¶](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.preamble "Link to this definition")

The format of a MIME document allows for some text between the blank line following the headers, and the first multipart boundary string. Normally, this text is never visible in a MIME-aware mail reader because it falls outside the standard MIME armor. However, when viewing the raw text of the message, or when viewing the message in a non-MIME aware reader, this text can become visible.

The _preamble_ attribute contains this leading extra-armor text for MIME documents. When the [`Parser`](https://docs.python.org/3/library/email.parser.html#email.parser.Parser "email.parser.Parser")
 discovers some text after the headers but before the first boundary string, it assigns this text to the message’s _preamble_ attribute. When the [`Generator`](https://docs.python.org/3/library/email.generator.html#email.generator.Generator "email.generator.Generator")
 is writing out the plain text representation of a MIME message, and it finds the message has a _preamble_ attribute, it will write this text in the area between the headers and the first boundary. See [`email.parser`](https://docs.python.org/3/library/email.parser.html#module-email.parser "email.parser: Parse flat text email messages to produce a message object structure.")
 and [`email.generator`](https://docs.python.org/3/library/email.generator.html#module-email.generator "email.generator: Generate flat text email messages from a message structure.")
 for details.

Note that if the message object has no preamble, the _preamble_ attribute will be `None`.

epilogue[¶](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.epilogue "Link to this definition")

The _epilogue_ attribute acts the same way as the _preamble_ attribute, except that it contains text that appears between the last boundary and the end of the message.

You do not need to set the epilogue to the empty string in order for the [`Generator`](https://docs.python.org/3/library/email.generator.html#email.generator.Generator "email.generator.Generator")
 to print a newline at the end of the file.

defects[¶](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.defects "Link to this definition")

The _defects_ attribute contains a list of all the problems found when parsing this message. See [`email.errors`](https://docs.python.org/3/library/email.errors.html#module-email.errors "email.errors: The exception classes used by the email package.")
 for a detailed description of the possible parsing defects.

#### Previous topic

[`email`: Examples](https://docs.python.org/3/library/email.examples.html "previous chapter")

#### Next topic

[`email.mime`: Creating email and MIME objects from scratch](https://docs.python.org/3/library/email.mime.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=email.message.Message%3A+Representing+an+email+message+using+the+compat32+API&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Femail.compat32-message.html&pagesource=library%2Femail.compat32-message.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/email.compat32-message.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/email.mime.html "email.mime: Creating email and MIME objects from scratch")
     |
*   [previous](https://docs.python.org/3/library/email.examples.html "email: Examples")
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
*   [`email.message.Message`: Representing an email message using the `compat32` API](https://docs.python.org/3/library/email.compat32-message.html)
    
*    
    
    |
*   Theme Auto Light Dark |