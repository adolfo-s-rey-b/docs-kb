### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/email.parser.html "email.parser: Parsing email messages")
     |
*   [previous](https://docs.python.org/3/library/email.html "email — An email and MIME handling package")
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
*   [`email.message`: Representing an email message](https://docs.python.org/3/library/email.message.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`email.message`: Representing an email message[¶](https://docs.python.org/3/library/email.message.html#module-email.message "Link to this heading")

====================================================================================================================================================

**Source code:** [Lib/email/message.py](https://github.com/python/cpython/tree/3.15/Lib/email/message.py)

* * *

Added in version 3.6: [\[1\]](https://docs.python.org/3/library/email.message.html#id3)

The central class in the [`email`](https://docs.python.org/3/library/email.html#module-email "email: Package supporting the parsing, manipulating, and generating email messages.")
 package is the [`EmailMessage`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage "email.message.EmailMessage")
 class, imported from the `email.message` module. It is the base class for the `email` object model. `EmailMessage` provides the core functionality for setting and querying header fields, for accessing message bodies, and for creating or modifying structured messages.

An email message consists of _headers_ and a _payload_ (which is also referred to as the _content_). Headers are [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html)
 or [**RFC 6532**](https://datatracker.ietf.org/doc/html/rfc6532.html)
 style field names and values, where the field name and value are separated by a colon. The colon is not part of either the field name or the field value. The payload may be a simple text message, or a binary object, or a structured sequence of sub-messages each with their own set of headers and their own payload. The latter type of payload is indicated by the message having a MIME type such as _multipart/\*_ or _message/rfc822_.

The conceptual model provided by an [`EmailMessage`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage "email.message.EmailMessage")
 object is that of an ordered dictionary of headers coupled with a _payload_ that represents the [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html)
 body of the message, which might be a list of sub-`EmailMessage` objects. In addition to the normal dictionary methods for accessing the header names and values, there are methods for accessing specialized information from the headers (for example the MIME content type), for operating on the payload, for generating a serialized version of the message, and for recursively walking over the object tree.

The [`EmailMessage`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage "email.message.EmailMessage")
 dictionary-like interface is indexed by the header names, which must be ASCII values. The values of the dictionary are strings with some extra methods. Headers are stored and returned in case-preserving form, but field names are matched case-insensitively. The keys are ordered, but unlike a real dict, there can be duplicates. Additional methods are provided for working with headers that have duplicate keys.

The _payload_ is either a string or bytes object, in the case of simple message objects, or a list of [`EmailMessage`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage "email.message.EmailMessage")
 objects, for MIME container documents such as _multipart/\*_ and _message/rfc822_ message objects.

class email.message.EmailMessage(_policy\=default_)[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage "Link to this definition")

If _policy_ is specified use the rules it specifies to update and serialize the representation of the message. If _policy_ is not set, use the [`default`](https://docs.python.org/3/library/email.policy.html#email.policy.default "email.policy.default")
 policy, which follows the rules of the email RFCs except for line endings (instead of the RFC mandated `\r\n`, it uses the Python standard `\n` line endings). For more information see the [`policy`](https://docs.python.org/3/library/email.policy.html#module-email.policy "email.policy: Controlling the parsing and generating of messages")
 documentation. [\[2\]](https://docs.python.org/3/library/email.message.html#id4)

as\_string(_unixfrom\=False_, _maxheaderlen\=None_, _policy\=None_)[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.as_string "Link to this definition")

Return the entire message flattened as a string. When optional _unixfrom_ is true, the envelope header is included in the returned string. _unixfrom_ defaults to `False`. For backward compatibility with the base [`Message`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message "email.message.Message")
 class _maxheaderlen_ is accepted, but defaults to `None`, which means that by default the line length is controlled by the [`max_line_length`](https://docs.python.org/3/library/email.policy.html#email.policy.Policy.max_line_length "email.policy.Policy.max_line_length")
 of the policy. The _policy_ argument may be used to override the default policy obtained from the message instance. This can be used to control some of the formatting produced by the method, since the specified _policy_ will be passed to the [`Generator`](https://docs.python.org/3/library/email.generator.html#email.generator.Generator "email.generator.Generator")
.

Flattening the message may trigger changes to the `EmailMessage` if defaults need to be filled in to complete the transformation to a string (for example, MIME boundaries may be generated or modified).

Note that this method is provided as a convenience and may not be the most useful way to serialize messages in your application, especially if you are dealing with multiple messages. See [`email.generator.Generator`](https://docs.python.org/3/library/email.generator.html#email.generator.Generator "email.generator.Generator")
 for a more flexible API for serializing messages. Note also that this method is restricted to producing messages serialized as “7 bit clean” when [`utf8`](https://docs.python.org/3/library/email.policy.html#email.policy.EmailPolicy.utf8 "email.policy.EmailPolicy.utf8")
 is `False`, which is the default.

Changed in version 3.6: the default behavior when _maxheaderlen_ is not specified was changed from defaulting to 0 to defaulting to the value of _max\_line\_length_ from the policy.

\_\_str\_\_()[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.__str__ "Link to this definition")

Equivalent to `as_string(policy=self.policy.clone(utf8=True))`. Allows `str(msg)` to produce a string containing the serialized message in a readable format.

Changed in version 3.4: the method was changed to use `utf8=True`, thus producing an [**RFC 6531**](https://datatracker.ietf.org/doc/html/rfc6531.html)
\-like message representation, instead of being a direct alias for [`as_string()`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.as_string "email.message.EmailMessage.as_string")
.

as\_bytes(_unixfrom\=False_, _policy\=None_)[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.as_bytes "Link to this definition")

Return the entire message flattened as a bytes object. When optional _unixfrom_ is true, the envelope header is included in the returned string. _unixfrom_ defaults to `False`. The _policy_ argument may be used to override the default policy obtained from the message instance. This can be used to control some of the formatting produced by the method, since the specified _policy_ will be passed to the [`BytesGenerator`](https://docs.python.org/3/library/email.generator.html#email.generator.BytesGenerator "email.generator.BytesGenerator")
.

Flattening the message may trigger changes to the `EmailMessage` if defaults need to be filled in to complete the transformation to a string (for example, MIME boundaries may be generated or modified).

Note that this method is provided as a convenience and may not be the most useful way to serialize messages in your application, especially if you are dealing with multiple messages. See [`email.generator.BytesGenerator`](https://docs.python.org/3/library/email.generator.html#email.generator.BytesGenerator "email.generator.BytesGenerator")
 for a more flexible API for serializing messages.

\_\_bytes\_\_()[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.__bytes__ "Link to this definition")

Equivalent to [`as_bytes()`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.as_bytes "email.message.EmailMessage.as_bytes")
. Allows `bytes(msg)` to produce a bytes object containing the serialized message.

is\_multipart()[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.is_multipart "Link to this definition")

Return `True` if the message’s payload is a list of sub-`EmailMessage` objects, otherwise return `False`. When `is_multipart()` returns `False`, the payload should be a string object (which might be a CTE encoded binary payload). Note that `is_multipart()` returning `True` does not necessarily mean that “msg.get\_content\_maintype() == ‘multipart’” will return the `True`. For example, `is_multipart` will return `True` when the `EmailMessage` is of type `message/rfc822`.

set\_unixfrom(_unixfrom_)[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.set_unixfrom "Link to this definition")

Set the message’s envelope header to _unixfrom_, which should be a string. (See [`mboxMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.mboxMessage "mailbox.mboxMessage")
 for a brief description of this header.)

get\_unixfrom()[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.get_unixfrom "Link to this definition")

Return the message’s envelope header. Defaults to `None` if the envelope header was never set.

The following methods implement the mapping-like interface for accessing the message’s headers. Note that there are some semantic differences between these methods and a normal mapping (i.e. dictionary) interface. For example, in a dictionary there are no duplicate keys, but here there may be duplicate message headers. Also, in dictionaries there is no guaranteed order to the keys returned by [`keys()`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.keys "email.message.EmailMessage.keys")
, but in an `EmailMessage` object, headers are always returned in the order they appeared in the original message, or in which they were added to the message later. Any header deleted and then re-added is always appended to the end of the header list.

These semantic differences are intentional and are biased toward convenience in the most common use cases.

Note that in all cases, any envelope header present in the message is not included in the mapping interface.

\_\_len\_\_()[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.__len__ "Link to this definition")

Return the total number of headers, including duplicates.

\_\_contains\_\_(_name_)[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.__contains__ "Link to this definition")

Return `True` if the message object has a field named _name_. Matching is done without regard to case and _name_ does not include the trailing colon. Used for the `in` operator. For example:

Copy

if 'message-id' in myMessage:
   print('Message-ID:', myMessage\['message-id'\])

\_\_getitem\_\_(_name_)[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.__getitem__ "Link to this definition")

Return the value of the named header field. _name_ does not include the colon field separator. If the header is missing, `None` is returned; a [`KeyError`](https://docs.python.org/3/builtins/exceptions.html#KeyError "KeyError")
 is never raised.

Note that if the named field appears more than once in the message’s headers, exactly which of those field values will be returned is undefined. Use the [`get_all()`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.get_all "email.message.EmailMessage.get_all")
 method to get the values of all the extant headers named _name_.

Using the standard (non-`compat32`) policies, the returned value is an instance of a subclass of [`email.headerregistry.BaseHeader`](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.BaseHeader "email.headerregistry.BaseHeader")
.

\_\_setitem\_\_(_name_, _val_)[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.__setitem__ "Link to this definition")

Add a header to the message with field name _name_ and value _val_. The field is appended to the end of the message’s existing headers.

Note that this does _not_ overwrite or delete any existing header with the same name. If you want to ensure that the new header is the only one present in the message with field name _name_, delete the field first, e.g.:

Copy

del msg\['subject'\]
msg\['subject'\] \= 'Python roolz!'

If the [`policy`](https://docs.python.org/3/library/email.policy.html#module-email.policy "email.policy: Controlling the parsing and generating of messages")
 defines certain headers to be unique (as the standard policies do), this method may raise a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 when an attempt is made to assign a value to such a header when one already exists. This behavior is intentional for consistency’s sake, but do not depend on it as we may choose to make such assignments do an automatic deletion of the existing header in the future.

\_\_delitem\_\_(_name_)[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.__delitem__ "Link to this definition")

Delete all occurrences of the field with name _name_ from the message’s headers. No exception is raised if the named field isn’t present in the headers.

keys()[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.keys "Link to this definition")

Return a list of all the message’s header field names.

values()[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.values "Link to this definition")

Return a list of all the message’s field values.

items()[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.items "Link to this definition")

Return a list of 2-tuples containing all the message’s field headers and values.

get(_name_, _failobj\=None_)[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.get "Link to this definition")

Return the value of the named header field. This is identical to [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__")
 except that optional _failobj_ is returned if the named header is missing (_failobj_ defaults to `None`).

Here are some additional useful header related methods:

get\_all(_name_, _failobj\=None_)[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.get_all "Link to this definition")

Return a list of all the values for the field named _name_. If there are no such named headers in the message, _failobj_ is returned (defaults to `None`).

add\_header(_\_name_, _\_value_, _\*\*\_params_)[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.add_header "Link to this definition")

Extended header setting. This method is similar to [`__setitem__()`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.__setitem__ "email.message.EmailMessage.__setitem__")
 except that additional header parameters can be provided as keyword arguments. _\_name_ is the header field to add and _\_value_ is the _primary_ value for the header.

For each item in the keyword argument dictionary _\_params_, the key is taken as the parameter name, with underscores converted to dashes (since dashes are illegal in Python identifiers). Normally, the parameter will be added as `key="value"` unless the value is `None`, in which case only the key will be added.

If the value contains non-ASCII characters, the charset and language may be explicitly controlled by specifying the value as a three tuple in the format `(CHARSET, LANGUAGE, VALUE)`, where `CHARSET` is a string naming the charset to be used to encode the value, `LANGUAGE` can usually be set to `None` or the empty string (see [**RFC 2231**](https://datatracker.ietf.org/doc/html/rfc2231.html)
 for other possibilities), and `VALUE` is the string value containing non-ASCII code points. If a three tuple is not passed and the value contains non-ASCII characters, it is automatically encoded in [**RFC 2231**](https://datatracker.ietf.org/doc/html/rfc2231.html)
 format using a `CHARSET` of `utf-8` and a `LANGUAGE` of `None`.

Here is an example:

Copy

msg.add\_header('Content-Disposition', 'attachment', filename\='bud.gif')

This will add a header that looks like

Copy

Content\-Disposition: attachment; filename\="bud.gif"

An example of the extended interface with non-ASCII characters:

Copy

msg.add\_header('Content-Disposition', 'attachment',
               filename\=('iso-8859-1', '', 'Fußballer.ppt'))

replace\_header(_\_name_, _\_value_)[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.replace_header "Link to this definition")

Replace a header. Replace the first header found in the message that matches _\_name_, retaining header order and field name case of the original header. If no matching header is found, raise a [`KeyError`](https://docs.python.org/3/builtins/exceptions.html#KeyError "KeyError")
.

get\_content\_type()[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.get_content_type "Link to this definition")

Return the message’s content type, coerced to lower case of the form _maintype/subtype_. If there is no _Content-Type_ header in the message return the value returned by [`get_default_type()`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.get_default_type "email.message.EmailMessage.get_default_type")
. If the _Content-Type_ header is invalid, return `text/plain`.

(According to [**RFC 2045**](https://datatracker.ietf.org/doc/html/rfc2045.html)
, messages always have a default type, `get_content_type()` will always return a value. [**RFC 2045**](https://datatracker.ietf.org/doc/html/rfc2045.html)
 defines a message’s default type to be _text/plain_ unless it appears inside a _multipart/digest_ container, in which case it would be _message/rfc822_. If the _Content-Type_ header has an invalid type specification, [**RFC 2045**](https://datatracker.ietf.org/doc/html/rfc2045.html)
 mandates that the default type be _text/plain_.)

get\_content\_maintype()[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.get_content_maintype "Link to this definition")

Return the message’s main content type. This is the _maintype_ part of the string returned by [`get_content_type()`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.get_content_type "email.message.EmailMessage.get_content_type")
.

get\_content\_subtype()[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.get_content_subtype "Link to this definition")

Return the message’s sub-content type. This is the _subtype_ part of the string returned by [`get_content_type()`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.get_content_type "email.message.EmailMessage.get_content_type")
.

get\_default\_type()[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.get_default_type "Link to this definition")

Return the default content type. Most messages have a default content type of _text/plain_, except for messages that are subparts of _multipart/digest_ containers. Such subparts have a default content type of _message/rfc822_.

set\_default\_type(_ctype_)[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.set_default_type "Link to this definition")

Set the default content type. _ctype_ should either be _text/plain_ or _message/rfc822_, although this is not enforced. The default content type is not stored in the _Content-Type_ header, so it only affects the return value of the `get_content_type` methods when no _Content-Type_ header is present in the message.

set\_param(_param_, _value_, _header\='Content-Type'_, _requote\=True_, _charset\=None_, _language\=''_, _replace\=False_)[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.set_param "Link to this definition")

Set a parameter in the _Content-Type_ header. If the parameter already exists in the header, replace its value with _value_. When _header_ is `Content-Type` (the default) and the header does not yet exist in the message, add it, set its value to _text/plain_, and append the new parameter value. Optional _header_ specifies an alternative header to _Content-Type_.

If the value contains non-ASCII characters, the charset and language may be explicitly specified using the optional _charset_ and _language_ parameters. Optional _language_ specifies the [**RFC 2231**](https://datatracker.ietf.org/doc/html/rfc2231.html)
 language, defaulting to the empty string. Both _charset_ and _language_ should be strings. The default is to use the `utf8` _charset_ and `None` for the _language_.

If _replace_ is `False` (the default) the header is moved to the end of the list of headers. If _replace_ is `True`, the header will be updated in place.

Use of the _requote_ parameter with `EmailMessage` objects is deprecated.

Note that existing parameter values of headers may be accessed through the [`params`](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.ParameterizedMIMEHeader.params "email.headerregistry.ParameterizedMIMEHeader.params")
 attribute of the header value (for example, `msg['Content-Type'].params['charset']`).

Changed in version 3.4: `replace` keyword was added.

del\_param(_param_, _header\='content-type'_, _requote\=True_)[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.del_param "Link to this definition")

Remove the given parameter completely from the _Content-Type_ header. The header will be re-written in place without the parameter or its value. Optional _header_ specifies an alternative to _Content-Type_.

Use of the _requote_ parameter with `EmailMessage` objects is deprecated.

get\_filename(_failobj\=None_)[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.get_filename "Link to this definition")

Return the value of the `filename` parameter of the _Content-Disposition_ header of the message. If the header does not have a `filename` parameter, this method falls back to looking for the `name` parameter on the _Content-Type_ header. If neither is found, or the header is missing, then _failobj_ is returned. The returned string will always be unquoted as per [`email.utils.unquote()`](https://docs.python.org/3/library/email.utils.html#email.utils.unquote "email.utils.unquote")
.

get\_boundary(_failobj\=None_)[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.get_boundary "Link to this definition")

Return the value of the `boundary` parameter of the _Content-Type_ header of the message, or _failobj_ if either the header is missing, or has no `boundary` parameter. The returned string will always be unquoted as per [`email.utils.unquote()`](https://docs.python.org/3/library/email.utils.html#email.utils.unquote "email.utils.unquote")
.

set\_boundary(_boundary_)[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.set_boundary "Link to this definition")

Set the `boundary` parameter of the _Content-Type_ header to _boundary_. `set_boundary()` will always quote _boundary_ if necessary. A [`HeaderParseError`](https://docs.python.org/3/library/email.errors.html#email.errors.HeaderParseError "email.errors.HeaderParseError")
 is raised if the message object has no _Content-Type_ header.

Note that using this method is subtly different from deleting the old _Content-Type_ header and adding a new one with the new boundary via [`add_header()`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.add_header "email.message.EmailMessage.add_header")
, because `set_boundary()` preserves the order of the _Content-Type_ header in the list of headers.

get\_content\_charset(_failobj\=None_)[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.get_content_charset "Link to this definition")

Return the `charset` parameter of the _Content-Type_ header, coerced to lower case. If there is no _Content-Type_ header, or if that header has no `charset` parameter, _failobj_ is returned.

get\_charsets(_failobj\=None_)[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.get_charsets "Link to this definition")

Return a list containing the character set names in the message. If the message is a _multipart_, then the list will contain one element for each subpart in the payload, otherwise, it will be a list of length 1.

Each item in the list will be a string which is the value of the `charset` parameter in the _Content-Type_ header for the represented subpart. If the subpart has no _Content-Type_ header, no `charset` parameter, or is not of the _text_ main MIME type, then that item in the returned list will be _failobj_.

is\_attachment()[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.is_attachment "Link to this definition")

Return `True` if there is a _Content-Disposition_ header and its (case insensitive) value is `attachment`, `False` otherwise.

Changed in version 3.4.2: is\_attachment is now a method instead of a property, for consistency with [`is_multipart()`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.is_multipart "email.message.Message.is_multipart")
.

get\_content\_disposition()[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.get_content_disposition "Link to this definition")

Return the lowercased value (without parameters) of the message’s _Content-Disposition_ header if it has one, or `None`. The possible values for this method are _inline_, _attachment_ or `None` if the message follows [**RFC 2183**](https://datatracker.ietf.org/doc/html/rfc2183.html)
.

Added in version 3.5.

The following methods relate to interrogating and manipulating the content (payload) of the message.

walk()[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.walk "Link to this definition")

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

`walk` iterates over the subparts of any part where [`is_multipart()`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.is_multipart "email.message.EmailMessage.is_multipart")
 returns `True`, even though `msg.get_content_maintype() == 'multipart'` may return `False`. We can see this in our example by making use of the `_structure` debug helper function:

Copy

\>>> from email.iterators import \_structure
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

get\_body(_preferencelist\=('related', 'html', 'plain')_)[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.get_body "Link to this definition")

Return the MIME part that is the best candidate to be the “body” of the message.

_preferencelist_ must be a sequence of strings from the set `related`, `html`, and `plain`, and indicates the order of preference for the content type of the part returned.

Start looking for candidate matches with the object on which the `get_body` method is called.

If `related` is not included in _preferencelist_, consider the root part (or subpart of the root part) of any related encountered as a candidate if the (sub-)part matches a preference.

When encountering a `multipart/related`, check the `start` parameter and if a part with a matching _Content-ID_ is found, consider only it when looking for candidate matches. Otherwise consider only the first (default root) part of the `multipart/related`.

If a part has a _Content-Disposition_ header, only consider the part a candidate match if the value of the header is `inline`.

If none of the candidates matches any of the preferences in _preferencelist_, return `None`.

Notes: (1) For most applications the only _preferencelist_ combinations that really make sense are `('plain',)`, `('html', 'plain')`, and the default `('related', 'html', 'plain')`. (2) Because matching starts with the object on which `get_body` is called, calling `get_body` on a `multipart/related` will return the object itself unless _preferencelist_ has a non-default value. (3) Messages (or message parts) that do not specify a _Content-Type_ or whose _Content-Type_ header is invalid will be treated as if they are of type `text/plain`, which may occasionally cause `get_body` to return unexpected results.

iter\_attachments()[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.iter_attachments "Link to this definition")

Return an iterator over all of the immediate sub-parts of the message that are not candidate “body” parts. That is, skip the first occurrence of each of `text/plain`, `text/html`, `multipart/related`, or `multipart/alternative` (unless they are explicitly marked as attachments via _Content-Disposition: attachment_), and return all remaining parts. When applied directly to a `multipart/related`, return an iterator over the all the related parts except the root part (ie: the part pointed to by the `start` parameter, or the first part if there is no `start` parameter or the `start` parameter doesn’t match the _Content-ID_ of any of the parts). When applied directly to a `multipart/alternative` or a non-`multipart`, return an empty iterator.

iter\_parts()[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.iter_parts "Link to this definition")

Return an iterator over all of the immediate sub-parts of the message, which will be empty for a non-`multipart`. (See also [`walk()`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.walk "email.message.EmailMessage.walk")
.)

get\_content(_\*args_, _content\_manager\=None_, _\*\*kw_)[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.get_content "Link to this definition")

Call the [`get_content()`](https://docs.python.org/3/library/email.contentmanager.html#email.contentmanager.ContentManager.get_content "email.contentmanager.ContentManager.get_content")
 method of the _content\_manager_, passing self as the message object, and passing along any other arguments or keywords as additional arguments. If _content\_manager_ is not specified, use the `content_manager` specified by the current [`policy`](https://docs.python.org/3/library/email.policy.html#module-email.policy "email.policy: Controlling the parsing and generating of messages")
.

set\_content(_\*args_, _content\_manager\=None_, _\*\*kw_)[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.set_content "Link to this definition")

Call the [`set_content()`](https://docs.python.org/3/library/email.contentmanager.html#email.contentmanager.ContentManager.set_content "email.contentmanager.ContentManager.set_content")
 method of the _content\_manager_, passing self as the message object, and passing along any other arguments or keywords as additional arguments. If _content\_manager_ is not specified, use the `content_manager` specified by the current [`policy`](https://docs.python.org/3/library/email.policy.html#module-email.policy "email.policy: Controlling the parsing and generating of messages")
.

make\_related(_boundary\=None_)[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.make_related "Link to this definition")

Convert a non-`multipart` message into a `multipart/related` message, moving any existing _Content-_ headers and payload into a (new) first part of the `multipart`. If _boundary_ is specified, use it as the boundary string in the multipart, otherwise leave the boundary to be automatically created when it is needed (for example, when the message is serialized).

make\_alternative(_boundary\=None_)[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.make_alternative "Link to this definition")

Convert a non-`multipart` or a `multipart/related` into a `multipart/alternative`, moving any existing _Content-_ headers and payload into a (new) first part of the `multipart`. If _boundary_ is specified, use it as the boundary string in the multipart, otherwise leave the boundary to be automatically created when it is needed (for example, when the message is serialized).

make\_mixed(_boundary\=None_)[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.make_mixed "Link to this definition")

Convert a non-`multipart`, a `multipart/related`, or a `multipart/alternative` into a `multipart/mixed`, moving any existing _Content-_ headers and payload into a (new) first part of the `multipart`. If _boundary_ is specified, use it as the boundary string in the multipart, otherwise leave the boundary to be automatically created when it is needed (for example, when the message is serialized).

add\_related(_\*args_, _content\_manager\=None_, _\*\*kw_)[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.add_related "Link to this definition")

If the message is a `multipart/related`, create a new message object, pass all of the arguments to its [`set_content()`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.set_content "email.message.EmailMessage.set_content")
 method, and [`attach()`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.attach "email.message.Message.attach")
 it to the `multipart`. If the message is a non-`multipart`, call [`make_related()`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.make_related "email.message.EmailMessage.make_related")
 and then proceed as above. If the message is any other type of `multipart`, raise a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
. If _content\_manager_ is not specified, use the `content_manager` specified by the current [`policy`](https://docs.python.org/3/library/email.policy.html#module-email.policy "email.policy: Controlling the parsing and generating of messages")
. If the added part has no _Content-Disposition_ header, add one with the value `inline`.

add\_alternative(_\*args_, _content\_manager\=None_, _\*\*kw_)[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.add_alternative "Link to this definition")

If the message is a `multipart/alternative`, create a new message object, pass all of the arguments to its [`set_content()`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.set_content "email.message.EmailMessage.set_content")
 method, and [`attach()`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.attach "email.message.Message.attach")
 it to the `multipart`. If the message is a non-`multipart` or `multipart/related`, call [`make_alternative()`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.make_alternative "email.message.EmailMessage.make_alternative")
 and then proceed as above. If the message is any other type of `multipart`, raise a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
. If _content\_manager_ is not specified, use the `content_manager` specified by the current [`policy`](https://docs.python.org/3/library/email.policy.html#module-email.policy "email.policy: Controlling the parsing and generating of messages")
.

add\_attachment(_\*args_, _content\_manager\=None_, _\*\*kw_)[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.add_attachment "Link to this definition")

If the message is a `multipart/mixed`, create a new message object, pass all of the arguments to its [`set_content()`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.set_content "email.message.EmailMessage.set_content")
 method, and [`attach()`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.attach "email.message.Message.attach")
 it to the `multipart`. If the message is a non-`multipart`, `multipart/related`, or `multipart/alternative`, call [`make_mixed()`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.make_mixed "email.message.EmailMessage.make_mixed")
 and then proceed as above. If _content\_manager_ is not specified, use the `content_manager` specified by the current [`policy`](https://docs.python.org/3/library/email.policy.html#module-email.policy "email.policy: Controlling the parsing and generating of messages")
. If the added part has no _Content-Disposition_ header, add one with the value `attachment`. This method can be used both for explicit attachments (_Content-Disposition: attachment_) and `inline` attachments (_Content-Disposition: inline_), by passing appropriate options to the `content_manager`.

clear()[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.clear "Link to this definition")

Remove the payload and all of the headers.

clear\_content()[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.clear_content "Link to this definition")

Remove the payload and all of the _!Content-_ headers, leaving all other headers intact and in their original order.

`EmailMessage` objects have the following instance attributes:

preamble[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.preamble "Link to this definition")

The format of a MIME document allows for some text between the blank line following the headers, and the first multipart boundary string. Normally, this text is never visible in a MIME-aware mail reader because it falls outside the standard MIME armor. However, when viewing the raw text of the message, or when viewing the message in a non-MIME aware reader, this text can become visible.

The _preamble_ attribute contains this leading extra-armor text for MIME documents. When the [`Parser`](https://docs.python.org/3/library/email.parser.html#email.parser.Parser "email.parser.Parser")
 discovers some text after the headers but before the first boundary string, it assigns this text to the message’s _preamble_ attribute. When the [`Generator`](https://docs.python.org/3/library/email.generator.html#email.generator.Generator "email.generator.Generator")
 is writing out the plain text representation of a MIME message, and it finds the message has a _preamble_ attribute, it will write this text in the area between the headers and the first boundary. See [`email.parser`](https://docs.python.org/3/library/email.parser.html#module-email.parser "email.parser: Parse flat text email messages to produce a message object structure.")
 and [`email.generator`](https://docs.python.org/3/library/email.generator.html#module-email.generator "email.generator: Generate flat text email messages from a message structure.")
 for details.

Note that if the message object has no preamble, the _preamble_ attribute will be `None`.

epilogue[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.epilogue "Link to this definition")

The _epilogue_ attribute acts the same way as the _preamble_ attribute, except that it contains text that appears between the last boundary and the end of the message. As with the [`preamble`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.preamble "email.message.EmailMessage.preamble")
, if there is no epilog text this attribute will be `None`.

defects[¶](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.defects "Link to this definition")

The _defects_ attribute contains a list of all the problems found when parsing this message. See [`email.errors`](https://docs.python.org/3/library/email.errors.html#module-email.errors "email.errors: The exception classes used by the email package.")
 for a detailed description of the possible parsing defects.

class email.message.MIMEPart(_policy\=default_)[¶](https://docs.python.org/3/library/email.message.html#email.message.MIMEPart "Link to this definition")

This class represents a subpart of a MIME message. It is identical to [`EmailMessage`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage "email.message.EmailMessage")
, except that no _MIME-Version_ headers are added when [`set_content()`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.set_content "email.message.EmailMessage.set_content")
 is called, since sub-parts do not need their own _MIME-Version_ headers.

Footnotes

#### Previous topic

[`email` — An email and MIME handling package](https://docs.python.org/3/library/email.html "previous chapter")

#### Next topic

[`email.parser`: Parsing email messages](https://docs.python.org/3/library/email.parser.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=email.message%3A+Representing+an+email+message&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Femail.message.html&pagesource=library%2Femail.message.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/email.message.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/email.parser.html "email.parser: Parsing email messages")
     |
*   [previous](https://docs.python.org/3/library/email.html "email — An email and MIME handling package")
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
*   [`email.message`: Representing an email message](https://docs.python.org/3/library/email.message.html)
    
*    
    
    |
*   Theme Auto Light Dark |