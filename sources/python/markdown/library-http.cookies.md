### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/http.cookiejar.html "http.cookiejar — Cookie handling for HTTP clients")
     |
*   [previous](https://docs.python.org/3/library/http.server.html "http.server — HTTP servers")
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
*   [Internet Protocols and Support](https://docs.python.org/3/library/internet.html)
     »
*   [`http.cookies` — HTTP state management](https://docs.python.org/3/library/http.cookies.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`http.cookies` — HTTP state management[¶](https://docs.python.org/3/library/http.cookies.html#module-http.cookies "Link to this heading")

==========================================================================================================================================

**Source code:** [Lib/http/cookies.py](https://github.com/python/cpython/tree/3.15/Lib/http/cookies.py)

* * *

The `http.cookies` module defines classes for abstracting the concept of cookies, an HTTP state management mechanism. It supports both simple string-only cookies, and provides an abstraction for having any serializable data-type as cookie value.

The module formerly strictly applied the parsing rules described in the [**RFC 2109**](https://datatracker.ietf.org/doc/html/rfc2109.html)
 and [**RFC 2068**](https://datatracker.ietf.org/doc/html/rfc2068.html)
 specifications. It has since been discovered that MSIE 3.0x didn’t follow the character rules outlined in those specs; many current-day browsers and servers have also relaxed parsing rules when it comes to cookie handling. As a result, this module now uses parsing rules that are a bit less strict than they once were.

The character set, [`string.ascii_letters`](https://docs.python.org/3/library/string.html#string.ascii_letters "string.ascii_letters")
, [`string.digits`](https://docs.python.org/3/library/string.html#string.digits "string.digits")
 and ``!#$%&'*+-.^_`|~:`` denote the set of valid characters allowed by this module in a cookie name (as [`key`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.key "http.cookies.Morsel.key")
).

Changed in version 3.3: Allowed ‘:’ as a valid cookie name character.

Note

On encountering an invalid cookie, [`CookieError`](https://docs.python.org/3/library/http.cookies.html#http.cookies.CookieError "http.cookies.CookieError")
 is raised, so if your cookie data comes from a browser you should always prepare for invalid data and catch `CookieError` on parsing.

exception http.cookies.CookieError[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.CookieError "Link to this definition")

Exception failing because of [**RFC 2109**](https://datatracker.ietf.org/doc/html/rfc2109.html)
 invalidity: incorrect attributes, incorrect _Set-Cookie_ header, etc.

class http.cookies.BaseCookie(\[_input_\])[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.BaseCookie "Link to this definition")

This class is a dictionary-like object whose keys are strings and whose values are [`Morsel`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel "http.cookies.Morsel")
 instances. Note that upon setting a key to a value, the value is first converted to a `Morsel` containing the key and the value.

If _input_ is given, it is passed to the [`load()`](https://docs.python.org/3/library/http.cookies.html#http.cookies.BaseCookie.load "http.cookies.BaseCookie.load")
 method.

class http.cookies.SimpleCookie(\[_input_\])[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.SimpleCookie "Link to this definition")

This class derives from [`BaseCookie`](https://docs.python.org/3/library/http.cookies.html#http.cookies.BaseCookie "http.cookies.BaseCookie")
 and overrides [`value_decode()`](https://docs.python.org/3/library/http.cookies.html#http.cookies.BaseCookie.value_decode "http.cookies.BaseCookie.value_decode")
 and [`value_encode()`](https://docs.python.org/3/library/http.cookies.html#http.cookies.BaseCookie.value_encode "http.cookies.BaseCookie.value_encode")
. `SimpleCookie` supports strings as cookie values. When setting the value, `SimpleCookie` calls the builtin [`str()`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 to convert the value to a string. Values received from HTTP are kept as strings.

See also

Module [`http.cookiejar`](https://docs.python.org/3/library/http.cookiejar.html#module-http.cookiejar "http.cookiejar: Classes for automatic handling of HTTP cookies.")

HTTP cookie handling for web _clients_. The [`http.cookiejar`](https://docs.python.org/3/library/http.cookiejar.html#module-http.cookiejar "http.cookiejar: Classes for automatic handling of HTTP cookies.")
 and `http.cookies` modules do not depend on each other.

[**RFC 2109**](https://datatracker.ietf.org/doc/html/rfc2109.html)
 - HTTP State Management Mechanism

This is the state management specification implemented by this module.

Cookie Objects[¶](https://docs.python.org/3/library/http.cookies.html#cookie-objects "Link to this heading")

-------------------------------------------------------------------------------------------------------------

BaseCookie.value\_decode(_val_)[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.BaseCookie.value_decode "Link to this definition")

Return a tuple `(real_value, coded_value)` from a string representation. `real_value` can be any type. This method does no decoding in [`BaseCookie`](https://docs.python.org/3/library/http.cookies.html#http.cookies.BaseCookie "http.cookies.BaseCookie")
 — it exists so it can be overridden.

BaseCookie.value\_encode(_val_)[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.BaseCookie.value_encode "Link to this definition")

Return a tuple `(real_value, coded_value)`. _val_ can be any type, but `coded_value` will always be converted to a string. This method does no encoding in [`BaseCookie`](https://docs.python.org/3/library/http.cookies.html#http.cookies.BaseCookie "http.cookies.BaseCookie")
 — it exists so it can be overridden.

In general, it should be the case that `value_encode()` and [`value_decode()`](https://docs.python.org/3/library/http.cookies.html#http.cookies.BaseCookie.value_decode "http.cookies.BaseCookie.value_decode")
 are inverses on the range of _value\_decode_.

BaseCookie.output(_attrs\=None_, _header\='Set-Cookie:'_, _sep\='\\r\\n'_)[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.BaseCookie.output "Link to this definition")

Return a string representation suitable to be sent as HTTP headers. _attrs_ and _header_ are sent to each [`Morsel`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel "http.cookies.Morsel")
’s [`output()`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.output "http.cookies.Morsel.output")
 method. _sep_ is used to join the headers together, and is by default the combination `'\r\n'` (CRLF).

BaseCookie.js\_output(_attrs\=None_)[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.BaseCookie.js_output "Link to this definition")

Return an embeddable JavaScript snippet, which, if run on a browser which supports JavaScript, will act the same as if the HTTP headers was sent.

The meaning for _attrs_ is the same as in [`output()`](https://docs.python.org/3/library/http.cookies.html#http.cookies.BaseCookie.output "http.cookies.BaseCookie.output")
.

Deprecated since version 3.15, will be removed in version 3.19: This method generates a JavaScript snippet to set cookies in the browser, which is no longer considered a standard or recommended approach. Use [`output()`](https://docs.python.org/3/library/http.cookies.html#http.cookies.BaseCookie.output "http.cookies.BaseCookie.output")
 instead to generate HTTP headers.

BaseCookie.load(_rawdata_)[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.BaseCookie.load "Link to this definition")

If _rawdata_ is a string, parse it as an `HTTP_COOKIE` and add the values found there as [`Morsel`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel "http.cookies.Morsel")
s. If it is a dictionary, it is equivalent to:

Copy

for k, v in rawdata.items():
    cookie\[k\] \= v

Morsel Objects[¶](https://docs.python.org/3/library/http.cookies.html#morsel-objects "Link to this heading")

-------------------------------------------------------------------------------------------------------------

class http.cookies.Morsel[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel "Link to this definition")

Abstract a key/value pair, which has some [**RFC 2109**](https://datatracker.ietf.org/doc/html/rfc2109.html)
 attributes.

Morsels are dictionary-like objects, whose set of keys is constant — the valid [**RFC 2109**](https://datatracker.ietf.org/doc/html/rfc2109.html)
 attributes, which are:

> expires[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.expires "Link to this definition")
> 
> path[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.path "Link to this definition")
> 
> comment[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.comment "Link to this definition")
> 
> domain[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.domain "Link to this definition")
> 
> max-age
> 
> secure[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.secure "Link to this definition")
> 
> version[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.version "Link to this definition")
> 
> httponly[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.httponly "Link to this definition")
> 
> samesite[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.samesite "Link to this definition")
> 
> partitioned[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.partitioned "Link to this definition")

The attribute [`httponly`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.httponly "http.cookies.Morsel.httponly")
 specifies that the cookie is only transferred in HTTP requests, and is not accessible through JavaScript. This is intended to mitigate some forms of cross-site scripting.

The attribute [`samesite`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.samesite "http.cookies.Morsel.samesite")
 controls when the browser sends the cookie with cross-site requests. This helps to mitigate CSRF attacks. Valid values are “Strict” (only sent with same-site requests), “Lax” (sent with same-site requests and top-level navigations), and “None” (sent with same-site and cross-site requests). When using “None”, the “secure” attribute must also be set, as required by modern browsers.

The attribute [`partitioned`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.partitioned "http.cookies.Morsel.partitioned")
 indicates to user agents that these cross-site cookies _should_ only be available in the same top-level context that the cookie was first set in. For this to be accepted by the user agent, you **must** also set `Secure`.

In addition, it is recommended to use the `__Host-` prefix when setting partitioned cookies to make them bound to the hostname and not the registrable domain. Read [CHIPS (Cookies Having Independent Partitioned State)](https://github.com/privacycg/CHIPS/blob/main/README.md)
 for full details and examples.

The keys are case-insensitive and their default value is `''`.

Changed in version 3.5: `__eq__()` now takes [`key`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.key "http.cookies.Morsel.key")
 and [`value`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.value "http.cookies.Morsel.value")
 into account.

Changed in version 3.7: Attributes [`key`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.key "http.cookies.Morsel.key")
, [`value`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.value "http.cookies.Morsel.value")
 and [`coded_value`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.coded_value "http.cookies.Morsel.coded_value")
 are read-only. Use [`set()`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.set "http.cookies.Morsel.set")
 for setting them.

Changed in version 3.8: Added support for the [`samesite`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.samesite "http.cookies.Morsel.samesite")
 attribute.

Changed in version 3.14: Added support for the [`partitioned`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.partitioned "http.cookies.Morsel.partitioned")
 attribute.

Morsel.value[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.value "Link to this definition")

The value of the cookie.

Morsel.coded\_value[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.coded_value "Link to this definition")

The encoded value of the cookie — this is what should be sent.

Morsel.key[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.key "Link to this definition")

The name of the cookie.

Morsel.set(_key_, _value_, _coded\_value_)[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.set "Link to this definition")

Set the _key_, _value_ and _coded\_value_ attributes.

Morsel.isReservedKey(_K_)[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.isReservedKey "Link to this definition")

Whether _K_ is a member of the set of keys of a [`Morsel`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel "http.cookies.Morsel")
.

Morsel.output(_attrs\=None_, _header\='Set-Cookie:'_)[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.output "Link to this definition")

Return a string representation of the Morsel, suitable to be sent as an HTTP header. By default, all the attributes are included, unless _attrs_ is given, in which case it should be a list of attributes to use. _header_ is by default `"Set-Cookie:"`.

Morsel.js\_output(_attrs\=None_)[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.js_output "Link to this definition")

Return an embeddable JavaScript snippet, which, if run on a browser which supports JavaScript, will act the same as if the HTTP header was sent.

The meaning for _attrs_ is the same as in [`output()`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.output "http.cookies.Morsel.output")
.

Deprecated since version 3.15, will be removed in version 3.19: This method generates a JavaScript snippet to set cookies in the browser, which is no longer considered a standard or recommended approach. Use [`output()`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.output "http.cookies.Morsel.output")
 instead to generate HTTP headers.

Morsel.OutputString(_attrs\=None_)[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.OutputString "Link to this definition")

Return a string representing the Morsel, without any surrounding HTTP or JavaScript.

The meaning for _attrs_ is the same as in [`output()`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.output "http.cookies.Morsel.output")
.

Morsel.update(_values_)[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.update "Link to this definition")

Update the values in the Morsel dictionary with the values in the dictionary _values_. Raise an error if any of the keys in the _values_ dict is not a valid [**RFC 2109**](https://datatracker.ietf.org/doc/html/rfc2109.html)
 attribute.

Changed in version 3.5: an error is raised for invalid keys.

Morsel.copy(_value_)[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.copy "Link to this definition")

Return a shallow copy of the Morsel object.

Changed in version 3.5: return a Morsel object instead of a dict.

Morsel.setdefault(_key_, _value\=None_)[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.setdefault "Link to this definition")

Raise an error if key is not a valid [**RFC 2109**](https://datatracker.ietf.org/doc/html/rfc2109.html)
 attribute, otherwise behave the same as [`dict.setdefault()`](https://docs.python.org/3/builtins/stdtypes.html#dict.setdefault "dict.setdefault")
.

Example[¶](https://docs.python.org/3/library/http.cookies.html#example "Link to this heading")

-----------------------------------------------------------------------------------------------

The following example demonstrates how to use the `http.cookies` module.

Copy

\>>> from http import cookies
\>>> C \= cookies.SimpleCookie()
\>>> C\["fig"\] \= "newton"
\>>> C\["sugar"\] \= "wafer"
\>>> print(C) \# generate HTTP headers
Set-Cookie: fig=newton
Set-Cookie: sugar=wafer
\>>> print(C.output()) \# same thing
Set-Cookie: fig=newton
Set-Cookie: sugar=wafer
\>>> C \= cookies.SimpleCookie()
\>>> C\["rocky"\] \= "road"
\>>> C\["rocky"\]\["path"\] \= "/cookie"
\>>> print(C.output(header\="Cookie:"))
Cookie: rocky=road; Path=/cookie
\>>> print(C.output(attrs\=\[\], header\="Cookie:"))
Cookie: rocky=road
\>>> C \= cookies.SimpleCookie()
\>>> C.load("chips=ahoy; vienna=finger") \# load from a string (HTTP header)
\>>> print(C)
Set-Cookie: chips=ahoy
Set-Cookie: vienna=finger
\>>> C \= cookies.SimpleCookie()
\>>> C.load('keebler="E=everybody; L=\\\\"Loves\\\\"; fudge=;";')
\>>> print(C)
Set-Cookie: keebler="E=everybody; L=\\"Loves\\"; fudge=;"
\>>> C \= cookies.SimpleCookie()
\>>> C\["oreo"\] \= "doublestuff"
\>>> C\["oreo"\]\["path"\] \= "/"
\>>> print(C)
Set-Cookie: oreo=doublestuff; Path=/
\>>> C \= cookies.SimpleCookie()
\>>> C\["twix"\] \= "none for you"
\>>> C\["twix"\].value
'none for you'
\>>> C \= cookies.SimpleCookie()
\>>> C\["number"\] \= 7 \# equivalent to C\["number"\] = str(7)
\>>> C\["string"\] \= "seven"
\>>> C\["number"\].value
'7'
\>>> C\["string"\].value
'seven'
\>>> print(C)
Set-Cookie: number=7
Set-Cookie: string=seven

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`http.cookies` — HTTP state management](https://docs.python.org/3/library/http.cookies.html#)
    *   [Cookie Objects](https://docs.python.org/3/library/http.cookies.html#cookie-objects)
        
    *   [Morsel Objects](https://docs.python.org/3/library/http.cookies.html#morsel-objects)
        
    *   [Example](https://docs.python.org/3/library/http.cookies.html#example)
        

#### Previous topic

[`http.server` — HTTP servers](https://docs.python.org/3/library/http.server.html "previous chapter")

#### Next topic

[`http.cookiejar` — Cookie handling for HTTP clients](https://docs.python.org/3/library/http.cookiejar.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=http.cookies+%E2%80%94+HTTP+state+management&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fhttp.cookies.html&pagesource=library%2Fhttp.cookies.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/http.cookies.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/http.cookiejar.html "http.cookiejar — Cookie handling for HTTP clients")
     |
*   [previous](https://docs.python.org/3/library/http.server.html "http.server — HTTP servers")
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
*   [Internet Protocols and Support](https://docs.python.org/3/library/internet.html)
     »
*   [`http.cookies` — HTTP state management](https://docs.python.org/3/library/http.cookies.html)
    
*    
    
    |
*   Theme Auto Light Dark |