### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/email.contentmanager.html "email.contentmanager: Managing MIME Content")
     |
*   [previous](https://docs.python.org/3/library/email.errors.html "email.errors: Exception and Defect classes")
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
*   [`email.headerregistry`: Custom Header Objects](https://docs.python.org/3/library/email.headerregistry.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`email.headerregistry`: Custom Header Objects[¶](https://docs.python.org/3/library/email.headerregistry.html#module-email.headerregistry "Link to this heading")

=================================================================================================================================================================

**Source code:** [Lib/email/headerregistry.py](https://github.com/python/cpython/tree/3.15/Lib/email/headerregistry.py)

* * *

Added in version 3.6: [\[1\]](https://docs.python.org/3/library/email.headerregistry.html#id2)

Headers are represented by customized subclasses of [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
. The particular class used to represent a given header is determined by the [`header_factory`](https://docs.python.org/3/library/email.policy.html#email.policy.EmailPolicy.header_factory "email.policy.EmailPolicy.header_factory")
 of the [`policy`](https://docs.python.org/3/library/email.policy.html#module-email.policy "email.policy: Controlling the parsing and generating of messages")
 in effect when the headers are created. This section documents the particular `header_factory` implemented by the email package for handling [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html)
 compliant email messages, which not only provides customized header objects for various header types, but also provides an extension mechanism for applications to add their own custom header types.

When using any of the policy objects derived from [`EmailPolicy`](https://docs.python.org/3/library/email.policy.html#email.policy.EmailPolicy "email.policy.EmailPolicy")
, all headers are produced by [`HeaderRegistry`](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.HeaderRegistry "email.headerregistry.HeaderRegistry")
 and have [`BaseHeader`](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.BaseHeader "email.headerregistry.BaseHeader")
 as their last base class. Each header class has an additional base class that is determined by the type of the header. For example, many headers have the class [`UnstructuredHeader`](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.UnstructuredHeader "email.headerregistry.UnstructuredHeader")
 as their other base class. The specialized second class for a header is determined by the name of the header, using a lookup table stored in the `HeaderRegistry`. All of this is managed transparently for the typical application program, but interfaces are provided for modifying the default behavior for use by more complex applications.

The sections below first document the header base classes and their attributes, followed by the API for modifying the behavior of [`HeaderRegistry`](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.HeaderRegistry "email.headerregistry.HeaderRegistry")
, and finally the support classes used to represent the data parsed from structured headers.

class email.headerregistry.BaseHeader(_name_, _value_)[¶](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.BaseHeader "Link to this definition")

_name_ and _value_ are passed to `BaseHeader` from the [`header_factory`](https://docs.python.org/3/library/email.policy.html#email.policy.EmailPolicy.header_factory "email.policy.EmailPolicy.header_factory")
 call. The string value of any header object is the _value_ fully decoded to a string.

This base class defines the following read-only properties:

name[¶](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.BaseHeader.name "Link to this definition")

The name of the header (the portion of the field before the ‘:’). This is exactly the value passed in the [`header_factory`](https://docs.python.org/3/library/email.policy.html#email.policy.EmailPolicy.header_factory "email.policy.EmailPolicy.header_factory")
 call for _name_; that is, case is preserved.

defects[¶](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.BaseHeader.defects "Link to this definition")

A tuple of [`HeaderDefect`](https://docs.python.org/3/library/email.errors.html#email.errors.HeaderDefect "email.errors.HeaderDefect")
 instances reporting any RFC compliance problems found during parsing. The email package tries to be complete about detecting compliance issues. See the [`errors`](https://docs.python.org/3/library/email.errors.html#module-email.errors "email.errors: The exception classes used by the email package.")
 module for a discussion of the types of defects that may be reported.

max\_count[¶](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.BaseHeader.max_count "Link to this definition")

The maximum number of headers of this type that can have the same `name`. A value of `None` means unlimited. The `BaseHeader` value for this attribute is `None`; it is expected that specialized header classes will override this value as needed.

`BaseHeader` also provides the following method, which is called by the email library code and should not in general be called by application programs:

fold(_\*_, _policy_)[¶](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.BaseHeader.fold "Link to this definition")

Return a string containing [`linesep`](https://docs.python.org/3/library/email.policy.html#email.policy.Policy.linesep "email.policy.Policy.linesep")
 characters as required to correctly fold the header according to _policy_. A [`cte_type`](https://docs.python.org/3/library/email.policy.html#email.policy.Policy.cte_type "email.policy.Policy.cte_type")
 of `8bit` will be treated as if it were `7bit`, since headers may not contain arbitrary binary data. If [`utf8`](https://docs.python.org/3/library/email.policy.html#email.policy.EmailPolicy.utf8 "email.policy.EmailPolicy.utf8")
 is `False`, non-ASCII data will be [**RFC 2047**](https://datatracker.ietf.org/doc/html/rfc2047.html)
 encoded.

`BaseHeader` by itself cannot be used to create a header object. It defines a protocol that each specialized header cooperates with in order to produce the header object. Specifically, `BaseHeader` requires that the specialized class provide a [`classmethod()`](https://docs.python.org/3/builtins/functions.html#classmethod "classmethod")
 named `parse`. This method is called as follows:

Copy

parse(string, kwds)

`kwds` is a dictionary containing one pre-initialized key, `defects`. `defects` is an empty list. The parse method should append any detected defects to this list. On return, the `kwds` dictionary _must_ contain values for at least the keys `decoded`, `defects` and `parse_tree`. `decoded` should be the string value for the header (that is, the header value fully decoded to a string). `parse_tree` is set to the parse tree obtained from parsing the header. The parse method should assume that _string_ may contain content-transfer-encoded parts, but should correctly handle all valid Unicode characters as well so that it can parse un-encoded header values.

`BaseHeader`’s `__new__` then creates the header instance, and calls its `init` method. The specialized class only needs to provide an `init` method if it wishes to set additional attributes beyond those provided by `BaseHeader` itself. Such an `init` method should look like this:

Copy

def init(self, /, \*args, \*\*kw):
    self.\_myattr \= kw.pop('myattr')
    super().init(\*args, \*\*kw)

That is, anything extra that the specialized class puts in to the `kwds` dictionary should be removed and handled, and the remaining contents of `kw` (and `args`) passed to the `BaseHeader` `init` method.

class email.headerregistry.UnstructuredHeader[¶](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.UnstructuredHeader "Link to this definition")

An “unstructured” header is the default type of header in [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html)
. Any header that does not have a specified syntax is treated as unstructured. The classic example of an unstructured header is the _Subject_ header.

In [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html)
, an unstructured header is a run of arbitrary text in the ASCII character set. [**RFC 2047**](https://datatracker.ietf.org/doc/html/rfc2047.html)
, however, has an [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html)
 compatible mechanism for encoding non-ASCII text as ASCII characters within a header value. When a _value_ containing encoded words is passed to the constructor, the `UnstructuredHeader` parser converts such encoded words into a string, following the [**RFC 2047**](https://datatracker.ietf.org/doc/html/rfc2047.html)
 rules for unstructured text. The parser uses heuristics to attempt to decode certain non-compliant encoded words. Defects are registered in such cases, as well as defects for issues such as invalid characters within the encoded words or the non-encoded text.

This header type provides no additional attributes.

class email.headerregistry.DateHeader[¶](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.DateHeader "Link to this definition")

[**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html)
 specifies a very specific format for dates within email headers. The `DateHeader` parser recognizes that date format, as well as recognizing a number of variant forms that are sometimes found “in the wild”.

This header type provides the following additional attributes:

datetime[¶](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.DateHeader.datetime "Link to this definition")

If the header value can be recognized as a valid date of one form or another, this attribute will contain a [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")
 instance representing that date. If the timezone of the input date is specified as `-0000` (indicating it is in UTC but contains no information about the source timezone), then [`datetime`](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.DateHeader.datetime "email.headerregistry.DateHeader.datetime")
 will be a naive `datetime`. If a specific timezone offset is found (including `+0000`), then `datetime` will contain an aware `datetime` that uses [`datetime.timezone`](https://docs.python.org/3/library/datetime.html#datetime.timezone "datetime.timezone")
 to record the timezone offset.

The `decoded` value of the header is determined by formatting the `datetime` according to the [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html)
 rules; that is, it is set to:

Copy

email.utils.format\_datetime(self.datetime)

When creating a `DateHeader`, _value_ may be [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")
 instance. This means, for example, that the following code is valid and does what one would expect:

Copy

msg\['Date'\] \= datetime(2011, 7, 15, 21)

Because this is a naive `datetime` it will be interpreted as a UTC timestamp, and the resulting value will have a timezone of `-0000`. Much more useful is to use the [`localtime()`](https://docs.python.org/3/library/email.utils.html#email.utils.localtime "email.utils.localtime")
 function from the [`utils`](https://docs.python.org/3/library/email.utils.html#module-email.utils "email.utils: Miscellaneous email package utilities.")
 module:

Copy

msg\['Date'\] \= utils.localtime()

This example sets the date header to the current time and date using the current timezone offset.

class email.headerregistry.AddressHeader[¶](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.AddressHeader "Link to this definition")

Address headers are one of the most complex structured header types. The `AddressHeader` class provides a generic interface to any address header.

This header type provides the following additional attributes:

groups[¶](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.AddressHeader.groups "Link to this definition")

A tuple of [`Group`](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.Group "email.headerregistry.Group")
 objects encoding the addresses and groups found in the header value. Addresses that are not part of a group are represented in this list as single-address `Groups` whose [`display_name`](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.Group.display_name "email.headerregistry.Group.display_name")
 is `None`.

addresses[¶](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.AddressHeader.addresses "Link to this definition")

A tuple of [`Address`](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.Address "email.headerregistry.Address")
 objects encoding all of the individual addresses from the header value. If the header value contains any groups, the individual addresses from the group are included in the list at the point where the group occurs in the value (that is, the list of addresses is “flattened” into a one dimensional list).

The `decoded` value of the header will have all encoded words decoded to a string. [`idna`](https://docs.python.org/3/library/codecs.html#module-encodings.idna "encodings.idna: Internationalized Domain Names implementation")
 encoded domain names are also decoded to a string. The `decoded` value is set by [joining](https://docs.python.org/3/builtins/stdtypes.html#meth-str-join)
 the [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 value of the elements of the `groups` attribute with `', '`.

A list of [`Address`](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.Address "email.headerregistry.Address")
 and [`Group`](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.Group "email.headerregistry.Group")
 objects in any combination may be used to set the value of an address header. `Group` objects whose `display_name` is `None` will be interpreted as single addresses, which allows an address list to be copied with groups intact by using the list obtained from the `groups` attribute of the source header.

class email.headerregistry.SingleAddressHeader[¶](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.SingleAddressHeader "Link to this definition")

A subclass of [`AddressHeader`](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.AddressHeader "email.headerregistry.AddressHeader")
 that adds one additional attribute:

address[¶](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.SingleAddressHeader.address "Link to this definition")

The single address encoded by the header value. If the header value actually contains more than one address (which would be a violation of the RFC under the default [`policy`](https://docs.python.org/3/library/email.policy.html#module-email.policy "email.policy: Controlling the parsing and generating of messages")
), accessing this attribute will result in a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
.

Many of the above classes also have a `Unique` variant (for example, `UniqueUnstructuredHeader`). The only difference is that in the `Unique` variant, [`max_count`](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.BaseHeader.max_count "email.headerregistry.BaseHeader.max_count")
 is set to 1.

class email.headerregistry.MIMEVersionHeader[¶](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.MIMEVersionHeader "Link to this definition")

There is really only one valid value for the _MIME-Version_ header, and that is `1.0`. For future proofing, this header class supports other valid version numbers. If a version number has a valid value per [**RFC 2045**](https://datatracker.ietf.org/doc/html/rfc2045.html)
, then the header object will have non-`None` values for the following attributes:

version[¶](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.MIMEVersionHeader.version "Link to this definition")

The version number as a string, with any whitespace and/or comments removed.

major[¶](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.MIMEVersionHeader.major "Link to this definition")

The major version number as an integer

minor[¶](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.MIMEVersionHeader.minor "Link to this definition")

The minor version number as an integer

class email.headerregistry.ParameterizedMIMEHeader[¶](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.ParameterizedMIMEHeader "Link to this definition")

MIME headers all start with the prefix ‘Content-’. Each specific header has a certain value, described under the class for that header. Some can also take a list of supplemental parameters, which have a common format. This class serves as a base for all the MIME headers that take parameters.

params[¶](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.ParameterizedMIMEHeader.params "Link to this definition")

A dictionary mapping parameter names to parameter values.

Changed in version 3.15: It is now a [`frozendict`](https://docs.python.org/3/builtins/stdtypes.html#frozendict "frozendict")
 instead of a [`types.MappingProxyType`](https://docs.python.org/3/library/types.html#types.MappingProxyType "types.MappingProxyType")
.

class email.headerregistry.ContentTypeHeader[¶](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.ContentTypeHeader "Link to this definition")

A [`ParameterizedMIMEHeader`](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.ParameterizedMIMEHeader "email.headerregistry.ParameterizedMIMEHeader")
 class that handles the _Content-Type_ header.

content\_type[¶](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.ContentTypeHeader.content_type "Link to this definition")

The content type string, in the form `maintype/subtype`.

maintype[¶](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.ContentTypeHeader.maintype "Link to this definition")

subtype[¶](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.ContentTypeHeader.subtype "Link to this definition")

class email.headerregistry.ContentDispositionHeader[¶](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.ContentDispositionHeader "Link to this definition")

A [`ParameterizedMIMEHeader`](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.ParameterizedMIMEHeader "email.headerregistry.ParameterizedMIMEHeader")
 class that handles the _Content-Disposition_ header.

content\_disposition[¶](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.ContentDispositionHeader.content_disposition "Link to this definition")

`inline` and `attachment` are the only valid values in common use.

class email.headerregistry.ContentTransferEncodingHeader[¶](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.ContentTransferEncodingHeader "Link to this definition")

Handles the _Content-Transfer-Encoding_ header.

cte[¶](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.ContentTransferEncodingHeader.cte "Link to this definition")

Valid values are `7bit`, `8bit`, `base64`, and `quoted-printable`. See [**RFC 2045**](https://datatracker.ietf.org/doc/html/rfc2045.html)
 for more information.

class email.headerregistry.HeaderRegistry(_base\_class\=BaseHeader_, _default\_class\=UnstructuredHeader_, _use\_default\_map\=True_)[¶](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.HeaderRegistry "Link to this definition")

This is the factory used by [`EmailPolicy`](https://docs.python.org/3/library/email.policy.html#email.policy.EmailPolicy "email.policy.EmailPolicy")
 by default. `HeaderRegistry` builds the class used to create a header instance dynamically, using _base\_class_ and a specialized class retrieved from a registry that it holds. When a given header name does not appear in the registry, the class specified by _default\_class_ is used as the specialized class. When _use\_default\_map_ is `True` (the default), the standard mapping of header names to classes is copied in to the registry during initialization. _base\_class_ is always the last class in the generated class’s [`__bases__`](https://docs.python.org/3/reference/datamodel.html#type.__bases__ "type.__bases__")
 list.

The default mappings are:

> subject:
> 
> UniqueUnstructuredHeader
> 
> date:
> 
> UniqueDateHeader
> 
> resent-date:
> 
> DateHeader
> 
> orig-date:
> 
> UniqueDateHeader
> 
> sender:
> 
> UniqueSingleAddressHeader
> 
> resent-sender:
> 
> SingleAddressHeader
> 
> to:
> 
> UniqueAddressHeader
> 
> resent-to:
> 
> AddressHeader
> 
> cc:
> 
> UniqueAddressHeader
> 
> resent-cc:
> 
> AddressHeader
> 
> bcc:
> 
> UniqueAddressHeader
> 
> resent-bcc:
> 
> AddressHeader
> 
> from:
> 
> UniqueAddressHeader
> 
> resent-from:
> 
> AddressHeader
> 
> reply-to:
> 
> UniqueAddressHeader
> 
> mime-version:
> 
> MIMEVersionHeader
> 
> content-type:
> 
> ContentTypeHeader
> 
> content-disposition:
> 
> ContentDispositionHeader
> 
> content-transfer-encoding:
> 
> ContentTransferEncodingHeader
> 
> message-id:
> 
> MessageIDHeader

`HeaderRegistry` has the following methods:

map\_to\_type(_self_, _name_, _cls_)[¶](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.HeaderRegistry.map_to_type "Link to this definition")

_name_ is the name of the header to be mapped. It will be converted to lower case in the registry. _cls_ is the specialized class to be used, along with _base\_class_, to create the class used to instantiate headers that match _name_.

\_\_getitem\_\_(_name_)[¶](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.HeaderRegistry.__getitem__ "Link to this definition")

Construct and return a class to handle creating a _name_ header.

\_\_call\_\_(_name_, _value_)[¶](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.HeaderRegistry.__call__ "Link to this definition")

Retrieves the specialized header associated with _name_ from the registry (using _default\_class_ if _name_ does not appear in the registry) and composes it with _base\_class_ to produce a class, calls the constructed class’s constructor, passing it the same argument list, and finally returns the class instance created thereby.

The following classes are the classes used to represent data parsed from structured headers and can, in general, be used by an application program to construct structured values to assign to specific headers.

class email.headerregistry.Address(_display\_name\=''_, _username\=''_, _domain\=''_, _addr\_spec\=None_)[¶](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.Address "Link to this definition")

The class used to represent an email address. The general form of an address is:

Copy

\[display\_name\] <username@domain\>

or:

Copy

username@domain

where each part must conform to specific syntax rules spelled out in [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html)
.

As a convenience _addr\_spec_ can be specified instead of _username_ and _domain_, in which case _username_ and _domain_ will be parsed from the _addr\_spec_. An _addr\_spec_ must be a properly RFC quoted string; if it is not `Address` will raise an error. Unicode characters are allowed and will be property encoded when serialized. However, per the RFCs, Unicode is _not_ allowed in the username portion of the address.

display\_name[¶](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.Address.display_name "Link to this definition")

The display name portion of the address, if any, with all quoting removed. If the address does not have a display name, this attribute will be an empty string.

username[¶](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.Address.username "Link to this definition")

The `username` portion of the address, with all quoting removed.

domain[¶](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.Address.domain "Link to this definition")

The `domain` portion of the address.

addr\_spec[¶](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.Address.addr_spec "Link to this definition")

The `username@domain` portion of the address, correctly quoted for use as a bare address (the second form shown above). This attribute is not mutable.

\_\_str\_\_()[¶](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.Address.__str__ "Link to this definition")

The `str` value of the object is the address quoted according to [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html)
 rules, but with no Content Transfer Encoding of any non-ASCII characters.

To support SMTP ([**RFC 5321**](https://datatracker.ietf.org/doc/html/rfc5321.html)
), `Address` handles one special case: if `username` and `domain` are both the empty string (or `None`), then the string value of the `Address` is `<>`.

class email.headerregistry.Group(_display\_name\=None_, _addresses\=None_)[¶](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.Group "Link to this definition")

The class used to represent an address group. The general form of an address group is:

Copy

display\_name: \[address\-list\];

As a convenience for processing lists of addresses that consist of a mixture of groups and single addresses, a `Group` may also be used to represent single addresses that are not part of a group by setting _display\_name_ to `None` and providing a list of the single address as _addresses_.

display\_name[¶](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.Group.display_name "Link to this definition")

The `display_name` of the group. If it is `None` and there is exactly one `Address` in `addresses`, then the `Group` represents a single address that is not in a group.

addresses[¶](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.Group.addresses "Link to this definition")

A possibly empty tuple of [`Address`](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.Address "email.headerregistry.Address")
 objects representing the addresses in the group.

\_\_str\_\_()[¶](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.Group.__str__ "Link to this definition")

The `str` value of a `Group` is formatted according to [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html)
, but with no Content Transfer Encoding of any non-ASCII characters. If `display_name` is none and there is a single `Address` in the `addresses` list, the `str` value will be the same as the `str` of that single `Address`.

Footnotes

#### Previous topic

[`email.errors`: Exception and Defect classes](https://docs.python.org/3/library/email.errors.html "previous chapter")

#### Next topic

[`email.contentmanager`: Managing MIME Content](https://docs.python.org/3/library/email.contentmanager.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=email.headerregistry%3A+Custom+Header+Objects&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Femail.headerregistry.html&pagesource=library%2Femail.headerregistry.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/email.headerregistry.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/email.contentmanager.html "email.contentmanager: Managing MIME Content")
     |
*   [previous](https://docs.python.org/3/library/email.errors.html "email.errors: Exception and Defect classes")
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
*   [`email.headerregistry`: Custom Header Objects](https://docs.python.org/3/library/email.headerregistry.html)
    
*    
    
    |
*   Theme Auto Light Dark |