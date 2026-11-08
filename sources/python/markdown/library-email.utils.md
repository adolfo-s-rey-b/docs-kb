### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/email.iterators.html "email.iterators: Iterators")
     |
*   [previous](https://docs.python.org/3/library/email.encoders.html "email.encoders: Encoders")
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
*   [`email.utils`: Miscellaneous utilities](https://docs.python.org/3/library/email.utils.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`email.utils`: Miscellaneous utilities[¶](https://docs.python.org/3/library/email.utils.html#module-email.utils "Link to this heading")

========================================================================================================================================

**Source code:** [Lib/email/utils.py](https://github.com/python/cpython/tree/3.15/Lib/email/utils.py)

* * *

There are a couple of useful utilities provided in the `email.utils` module:

email.utils.localtime(_dt\=None_)[¶](https://docs.python.org/3/library/email.utils.html#email.utils.localtime "Link to this definition")

Return local time as an aware datetime object. If called without arguments, return the current time. Otherwise the _dt_ argument should be a [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")
 instance, and it is converted to the local time zone according to the system time zone database. If _dt_ is naive (that is, `dt.tzinfo` is `None`), it is assumed to be in local time.

Added in version 3.3.

Deprecated since version 3.12, removed in version 3.14: The _isdst_ parameter.

email.utils.make\_msgid(_idstring\=None_, _domain\=None_)[¶](https://docs.python.org/3/library/email.utils.html#email.utils.make_msgid "Link to this definition")

Returns a string suitable for an [**RFC 2822**](https://datatracker.ietf.org/doc/html/rfc2822.html)
\-compliant _Message-ID_ header. Optional _idstring_, if given, is a string used to strengthen the uniqueness of the message id. Optional _domain_, if given, provides the portion of the msgid after the ‘@’. The default is the local hostname. It is normally not necessary to override this default, but may be useful in certain cases, such as constructing a distributed system that uses a consistent domain name across multiple hosts.

Changed in version 3.2: Added the _domain_ keyword.

The remaining functions are part of the legacy (`Compat32`) email API. There is no need to directly use these with the new API, since the parsing and formatting they provide is done automatically by the header parsing machinery of the new API.

email.utils.quote(_str_)[¶](https://docs.python.org/3/library/email.utils.html#email.utils.quote "Link to this definition")

Return a new string with backslashes in _str_ replaced by two backslashes, and double quotes replaced by backslash-double quote.

email.utils.unquote(_str_)[¶](https://docs.python.org/3/library/email.utils.html#email.utils.unquote "Link to this definition")

Return a new string which is an _unquoted_ version of _str_. If _str_ ends and begins with double quotes, they are stripped off. Likewise if _str_ ends and begins with angle brackets, they are stripped off.

email.utils.parseaddr(_address_, _\*_, _strict\=True_)[¶](https://docs.python.org/3/library/email.utils.html#email.utils.parseaddr "Link to this definition")

Parse address – which should be the value of some address-containing field such as _To_ or _Cc_ – into its constituent _realname_ and _email address_ parts. Returns a tuple of that information, unless the parse fails, in which case a 2-tuple of `('', '')` is returned.

If _strict_ is true, use a strict parser which rejects malformed inputs.

Changed in version 3.13: Add _strict_ optional parameter and reject malformed inputs by default.

email.utils.formataddr(_pair_, _charset\='utf-8'_)[¶](https://docs.python.org/3/library/email.utils.html#email.utils.formataddr "Link to this definition")

The inverse of [`parseaddr()`](https://docs.python.org/3/library/email.utils.html#email.utils.parseaddr "email.utils.parseaddr")
, this takes a 2-tuple of the form `(realname, email_address)` and returns the string value suitable for a _To_ or _Cc_ header. If the first element of _pair_ is false, then the second element is returned unmodified.

Optional _charset_ is the character set that will be used in the [**RFC 2047**](https://datatracker.ietf.org/doc/html/rfc2047.html)
 encoding of the `realname` if the `realname` contains non-ASCII characters. Can be an instance of [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 or a [`Charset`](https://docs.python.org/3/library/email.charset.html#email.charset.Charset "email.charset.Charset")
. Defaults to `utf-8`.

Changed in version 3.3: Added the _charset_ option.

email.utils.getaddresses(_fieldvalues_, _\*_, _strict\=True_)[¶](https://docs.python.org/3/library/email.utils.html#email.utils.getaddresses "Link to this definition")

This function returns a list of 2-tuples of the form returned by [`parseaddr()`](https://docs.python.org/3/library/email.utils.html#email.utils.parseaddr "email.utils.parseaddr")
. _fieldvalues_ is a sequence of header field values as might be returned by [`Message.get_all()`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.get_all "email.message.Message.get_all")
.

If _strict_ is true, use a strict parser which rejects malformed inputs.

Here’s a simple example that gets all the recipients of a message:

Copy

from email.utils import getaddresses

tos \= msg.get\_all('to', \[\])
ccs \= msg.get\_all('cc', \[\])
resent\_tos \= msg.get\_all('resent-to', \[\])
resent\_ccs \= msg.get\_all('resent-cc', \[\])
all\_recipients \= getaddresses(tos + ccs + resent\_tos + resent\_ccs)

Changed in version 3.13: Add _strict_ optional parameter and reject malformed inputs by default.

email.utils.parsedate(_date_)[¶](https://docs.python.org/3/library/email.utils.html#email.utils.parsedate "Link to this definition")

Attempts to parse a date according to the rules in [**RFC 2822 Section 3.3**](https://datatracker.ietf.org/doc/html/rfc2822.html#section-3.3)
. However, some mailers don’t follow that format as specified, so `parsedate()` tries to guess correctly in such cases. _date_ is a string containing an [**RFC 2822**](https://datatracker.ietf.org/doc/html/rfc2822.html)
 date, such as `"Mon, 20 Nov 1995 19:12:08 -0500"`. If it succeeds in parsing the date, `parsedate()` returns a 9-tuple that can be passed directly to [`time.mktime()`](https://docs.python.org/3/library/time.html#time.mktime "time.mktime")
; otherwise `None` will be returned. Note that indexes 6, 7, and 8 of the result tuple are not usable.

email.utils.parsedate\_tz(_date_)[¶](https://docs.python.org/3/library/email.utils.html#email.utils.parsedate_tz "Link to this definition")

Performs the same function as [`parsedate()`](https://docs.python.org/3/library/email.utils.html#email.utils.parsedate "email.utils.parsedate")
, but returns either `None` or a 10-tuple; the first 9 elements make up a tuple that can be passed directly to [`time.mktime()`](https://docs.python.org/3/library/time.html#time.mktime "time.mktime")
, and the tenth is the offset of the date’s timezone from UTC (which is the official term for Greenwich Mean Time) [\[1\]](https://docs.python.org/3/library/email.utils.html#id2)
. If the input string has no timezone, the last element of the tuple returned is `0`, which represents UTC. Note that indexes 6, 7, and 8 of the result tuple are not usable.

email.utils.parsedate\_to\_datetime(_date_)[¶](https://docs.python.org/3/library/email.utils.html#email.utils.parsedate_to_datetime "Link to this definition")

The inverse of [`format_datetime()`](https://docs.python.org/3/library/email.utils.html#email.utils.format_datetime "email.utils.format_datetime")
. Performs the same function as [`parsedate()`](https://docs.python.org/3/library/email.utils.html#email.utils.parsedate "email.utils.parsedate")
, but on success returns a [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")
; otherwise [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 is raised if _date_ contains an invalid value such as an hour greater than 23 or a timezone offset not between -24 and 24 hours. If the input date has a timezone of `-0000`, the `datetime` will be a naive `datetime`, and if the date conforms to the RFCs it will represent a time in UTC but with no indication of the actual source timezone of the message the date comes from. If the input date has any other valid timezone offset, the `datetime` will be an aware `datetime` whose corresponding [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.datetime.tzinfo "datetime.datetime.tzinfo")
 attribute is a [`timezone`](https://docs.python.org/3/library/datetime.html#datetime.timezone "datetime.timezone")
 object.

Added in version 3.3.

email.utils.mktime\_tz(_tuple_)[¶](https://docs.python.org/3/library/email.utils.html#email.utils.mktime_tz "Link to this definition")

Turn a 10-tuple as returned by [`parsedate_tz()`](https://docs.python.org/3/library/email.utils.html#email.utils.parsedate_tz "email.utils.parsedate_tz")
 into a UTC timestamp (seconds since the Epoch). If the timezone item in the tuple is `None`, assume local time.

email.utils.formatdate(_timeval\=None_, _localtime\=False_, _usegmt\=False_)[¶](https://docs.python.org/3/library/email.utils.html#email.utils.formatdate "Link to this definition")

Returns a date string as per [**RFC 2822**](https://datatracker.ietf.org/doc/html/rfc2822.html)
, for example:

Copy

Fri, 09 Nov 2001 01:08:47 \-0000

Optional _timeval_, if given, is a floating-point time value as accepted by [`time.gmtime()`](https://docs.python.org/3/library/time.html#time.gmtime "time.gmtime")
 and [`time.localtime()`](https://docs.python.org/3/library/time.html#time.localtime "time.localtime")
, otherwise the current time is used.

Optional _localtime_ is a flag that when `True`, interprets _timeval_, and returns a date relative to the local timezone instead of UTC, properly taking daylight saving time into account. The default is `False` meaning UTC is used.

Optional _usegmt_ is a flag that when `True`, outputs a date string with the timezone as an ASCII string `GMT`, rather than a numeric `-0000`. This is needed for some protocols (such as HTTP). This only applies when _localtime_ is `False`. The default is `False`.

email.utils.format\_datetime(_dt_, _usegmt\=False_)[¶](https://docs.python.org/3/library/email.utils.html#email.utils.format_datetime "Link to this definition")

Like [`formatdate()`](https://docs.python.org/3/library/email.utils.html#email.utils.formatdate "email.utils.formatdate")
, but the input is a [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")
 instance. If it is a naive datetime, it is assumed to be “UTC with no information about the source timezone”, and the conventional `-0000` is used for the timezone. If it is an aware `datetime`, then the numeric timezone offset is used. If it is an aware timezone with offset zero, then _usegmt_ may be set to `True`, in which case the string `GMT` is used instead of the numeric timezone offset. This provides a way to generate standards-conformant HTTP date headers.

Added in version 3.3.

email.utils.decode\_rfc2231(_s_)[¶](https://docs.python.org/3/library/email.utils.html#email.utils.decode_rfc2231 "Link to this definition")

Decode the string _s_ according to [**RFC 2231**](https://datatracker.ietf.org/doc/html/rfc2231.html)
.

email.utils.encode\_rfc2231(_s_, _charset\=None_, _language\=None_)[¶](https://docs.python.org/3/library/email.utils.html#email.utils.encode_rfc2231 "Link to this definition")

Encode the string _s_ according to [**RFC 2231**](https://datatracker.ietf.org/doc/html/rfc2231.html)
. Optional _charset_ and _language_, if given, are the character set name and language name to use. If neither is given, _s_ is returned as-is. If _charset_ is given but _language_ is not, the string is encoded using the empty string for _language_.

email.utils.collapse\_rfc2231\_value(_value_, _errors\='replace'_, _fallback\_charset\='us-ascii'_)[¶](https://docs.python.org/3/library/email.utils.html#email.utils.collapse_rfc2231_value "Link to this definition")

When a header parameter is encoded in [**RFC 2231**](https://datatracker.ietf.org/doc/html/rfc2231.html)
 format, [`Message.get_param()`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.get_param "email.message.Message.get_param")
 may return a 3-tuple containing the character set, language, and value. `collapse_rfc2231_value()` turns this into a string. Optional _errors_ is passed to the _errors_ argument of [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
’s [`encode()`](https://docs.python.org/3/builtins/stdtypes.html#str.encode "str.encode")
 method; it defaults to `'replace'`. Optional _fallback\_charset_ specifies the character set to use if the one in the [**RFC 2231**](https://datatracker.ietf.org/doc/html/rfc2231.html)
 header is not known by Python; it defaults to `'us-ascii'`.

For convenience, if the _value_ passed to `collapse_rfc2231_value()` is not a tuple, it should be a string and it is returned unquoted.

email.utils.decode\_params(_params_)[¶](https://docs.python.org/3/library/email.utils.html#email.utils.decode_params "Link to this definition")

Decode parameters list according to [**RFC 2231**](https://datatracker.ietf.org/doc/html/rfc2231.html)
. _params_ is a sequence of 2-tuples containing elements of the form `(content-type, string-value)`.

Footnotes

#### Previous topic

[`email.encoders`: Encoders](https://docs.python.org/3/library/email.encoders.html "previous chapter")

#### Next topic

[`email.iterators`: Iterators](https://docs.python.org/3/library/email.iterators.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=email.utils%3A+Miscellaneous+utilities&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Femail.utils.html&pagesource=library%2Femail.utils.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/email.utils.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/email.iterators.html "email.iterators: Iterators")
     |
*   [previous](https://docs.python.org/3/library/email.encoders.html "email.encoders: Encoders")
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
*   [`email.utils`: Miscellaneous utilities](https://docs.python.org/3/library/email.utils.html)
    
*    
    
    |
*   Theme Auto Light Dark |