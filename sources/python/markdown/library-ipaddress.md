### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/mm.html "Multimedia Services")
     |
*   [previous](https://docs.python.org/3/library/xmlrpc.server.html "xmlrpc.server — Basic XML-RPC servers")
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
*   [`ipaddress` — IPv4/IPv6 manipulation library](https://docs.python.org/3/library/ipaddress.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`ipaddress` — IPv4/IPv6 manipulation library[¶](https://docs.python.org/3/library/ipaddress.html#module-ipaddress "Link to this heading")

==========================================================================================================================================

**Source code:** [Lib/ipaddress.py](https://github.com/python/cpython/tree/3.15/Lib/ipaddress.py)

* * *

`ipaddress` provides the capabilities to create, manipulate and operate on IPv4 and IPv6 addresses and networks.

The functions and classes in this module make it straightforward to handle various tasks related to IP addresses, including checking whether or not two hosts are on the same subnet, iterating over all hosts in a particular subnet, checking whether or not a string represents a valid IP address or network definition, and so on.

This is the full module API reference—for an overview and introduction, see [An introduction to the ipaddress module](https://docs.python.org/3/howto/ipaddress.html#ipaddress-howto)
.

Added in version 3.3.

Convenience factory functions[¶](https://docs.python.org/3/library/ipaddress.html#convenience-factory-functions "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

The `ipaddress` module provides factory functions to conveniently create IP addresses, networks and interfaces:

ipaddress.ip\_address(_address_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.ip_address "Link to this definition")

Return an [`IPv4Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address "ipaddress.IPv4Address")
 or [`IPv6Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address "ipaddress.IPv6Address")
 object depending on the IP address passed as argument. Either IPv4 or IPv6 addresses may be supplied; integers less than `2**32` will be considered to be IPv4 by default. A [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 is raised if _address_ does not represent a valid IPv4 or IPv6 address.

Copy

\>>> ipaddress.ip\_address('192.168.0.1')
IPv4Address('192.168.0.1')
\>>> ipaddress.ip\_address('2001:db8::')
IPv6Address('2001:db8::')

ipaddress.ip\_network(_address_, _strict\=True_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.ip_network "Link to this definition")

Return an [`IPv4Network`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network "ipaddress.IPv4Network")
 or [`IPv6Network`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network "ipaddress.IPv6Network")
 object depending on the IP address passed as argument. _address_ is a string or integer representing the IP network. Either IPv4 or IPv6 networks may be supplied; integers less than `2**32` will be considered to be IPv4 by default. _strict_ is passed to `IPv4Network` or `IPv6Network` constructor. A [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 is raised if _address_ does not represent a valid IPv4 or IPv6 address, or if the network has host bits set.

Copy

\>>> ipaddress.ip\_network('192.168.0.0/28')
IPv4Network('192.168.0.0/28')

ipaddress.ip\_interface(_address_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.ip_interface "Link to this definition")

Return an [`IPv4Interface`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Interface "ipaddress.IPv4Interface")
 or [`IPv6Interface`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Interface "ipaddress.IPv6Interface")
 object depending on the IP address passed as argument. _address_ is a string or integer representing the IP address. Either IPv4 or IPv6 addresses may be supplied; integers less than `2**32` will be considered to be IPv4 by default. A [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 is raised if _address_ does not represent a valid IPv4 or IPv6 address.

One downside of these convenience functions is that the need to handle both IPv4 and IPv6 formats means that error messages provide minimal information on the precise error, as the functions don’t know whether the IPv4 or IPv6 format was intended. More detailed error reporting can be obtained by calling the appropriate version specific class constructors directly.

IP Addresses[¶](https://docs.python.org/3/library/ipaddress.html#ip-addresses "Link to this heading")

------------------------------------------------------------------------------------------------------

### Address objects[¶](https://docs.python.org/3/library/ipaddress.html#address-objects "Link to this heading")

The [`IPv4Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address "ipaddress.IPv4Address")
 and [`IPv6Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address "ipaddress.IPv6Address")
 objects share a lot of common attributes. Some attributes that are only meaningful for IPv6 addresses are also implemented by `IPv4Address` objects, in order to make it easier to write code that handles both IP versions correctly. Address objects are [hashable](https://docs.python.org/3/glossary.html#term-hashable)
, so they can be used as keys in dictionaries.

class ipaddress.IPv4Address(_address_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address "Link to this definition")

Construct an IPv4 address. An [`AddressValueError`](https://docs.python.org/3/library/ipaddress.html#ipaddress.AddressValueError "ipaddress.AddressValueError")
 is raised if _address_ is not a valid IPv4 address.

The following constitutes a valid IPv4 address:

1.  A string in decimal-dot notation, consisting of four decimal integers in the inclusive range 0–255, separated by dots (e.g. `192.168.0.1`). Each integer represents an octet (byte) in the address. Leading zeroes are not tolerated to prevent confusion with octal notation.
    
2.  An integer that fits into 32 bits.
    
3.  An integer packed into a [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
     object of length 4 (most significant octet first).
    

Copy

\>>> ipaddress.IPv4Address('192.168.0.1')
IPv4Address('192.168.0.1')
\>>> ipaddress.IPv4Address(3232235521)
IPv4Address('192.168.0.1')
\>>> ipaddress.IPv4Address(b'\\xC0\\xA8\\x00\\x01')
IPv4Address('192.168.0.1')

Changed in version 3.8: Leading zeros are tolerated, even in ambiguous cases that look like octal notation.

Changed in version 3.9.5: Leading zeros are no longer tolerated and are treated as an error. IPv4 address strings are now parsed as strict as glibc [`inet_pton()`](https://docs.python.org/3/library/socket.html#socket.inet_pton "socket.inet_pton")
.

version[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address.version "Link to this definition")

The appropriate version number: `4` for IPv4, `6` for IPv6.

Changed in version 3.14: Made available on the class.

max\_prefixlen[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address.max_prefixlen "Link to this definition")

The total number of bits in the address representation for this version: `32` for IPv4, `128` for IPv6.

The prefix defines the number of leading bits in an address that are compared to determine whether or not an address is part of a network.

Changed in version 3.14: Made available on the class.

compressed[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address.compressed "Link to this definition")

exploded[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address.exploded "Link to this definition")

The string representation in dotted decimal notation. Leading zeroes are never included in the representation.

As IPv4 does not define a shorthand notation for addresses with octets set to zero, these two attributes are always the same as `str(addr)` for IPv4 addresses. Exposing these attributes makes it easier to write display code that can handle both IPv4 and IPv6 addresses.

packed[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address.packed "Link to this definition")

The binary representation of this address - a [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 object of the appropriate length (most significant octet first). This is 4 bytes for IPv4 and 16 bytes for IPv6.

reverse\_pointer[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address.reverse_pointer "Link to this definition")

The name of the reverse DNS PTR record for the IP address, e.g.:

Copy

\>>> ipaddress.ip\_address("127.0.0.1").reverse\_pointer
'1.0.0.127.in-addr.arpa'
\>>> ipaddress.ip\_address("2001:db8::1").reverse\_pointer
'1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.8.b.d.0.1.0.0.2.ip6.arpa'

This is the name that could be used for performing a PTR lookup, not the resolved hostname itself.

Added in version 3.5.

is\_multicast[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address.is_multicast "Link to this definition")

`True` if the address is reserved for multicast use. See [**RFC 3171**](https://datatracker.ietf.org/doc/html/rfc3171.html)
 (for IPv4) or [**RFC 2373**](https://datatracker.ietf.org/doc/html/rfc2373.html)
 (for IPv6).

is\_private[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address.is_private "Link to this definition")

`True` if the address is defined as not globally reachable by [iana-ipv4-special-registry](https://www.iana.org/assignments/iana-ipv4-special-registry/iana-ipv4-special-registry.xhtml)
 (for IPv4) or [iana-ipv6-special-registry](https://www.iana.org/assignments/iana-ipv6-special-registry/iana-ipv6-special-registry.xhtml)
 (for IPv6) with the following exceptions:

*   `is_private` is `False` for the shared address space (`100.64.0.0/10`)
    
*   For IPv4-mapped IPv6-addresses the `is_private` value is determined by the semantics of the underlying IPv4 addresses and the following condition holds (see [`IPv6Address.ipv4_mapped`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address.ipv4_mapped "ipaddress.IPv6Address.ipv4_mapped")
    ):
    
    Copy
    
    address.is\_private \== address.ipv4\_mapped.is\_private
    

`is_private` has value opposite to [`is_global`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address.is_global "ipaddress.IPv4Address.is_global")
, except for the shared address space (`100.64.0.0/10` range) where they are both `False`.

Changed in version 3.13: Fixed some false positives and false negatives.

*   `192.0.0.0/24` is considered private with the exception of `192.0.0.9/32` and `192.0.0.10/32` (previously: only the `192.0.0.0/29` sub-range was considered private).
    
*   `64:ff9b:1::/48` is considered private.
    
*   `2002::/16` is considered private.
    
*   There are exceptions within `2001::/23` (otherwise considered private): `2001:1::1/128`, `2001:1::2/128`, `2001:3::/32`, `2001:4:112::/48`, `2001:20::/28`, `2001:30::/28`. The exceptions are not considered private.
    

is\_global[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address.is_global "Link to this definition")

`True` if the address is defined as globally reachable by [iana-ipv4-special-registry](https://www.iana.org/assignments/iana-ipv4-special-registry/iana-ipv4-special-registry.xhtml)
 (for IPv4) or [iana-ipv6-special-registry](https://www.iana.org/assignments/iana-ipv6-special-registry/iana-ipv6-special-registry.xhtml)
 (for IPv6) with the following exception:

For IPv4-mapped IPv6-addresses the `is_private` value is determined by the semantics of the underlying IPv4 addresses and the following condition holds (see [`IPv6Address.ipv4_mapped`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address.ipv4_mapped "ipaddress.IPv6Address.ipv4_mapped")
):

Copy

address.is\_global \== address.ipv4\_mapped.is\_global

`is_global` has value opposite to [`is_private`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address.is_private "ipaddress.IPv4Address.is_private")
, except for the shared address space (`100.64.0.0/10` range) where they are both `False`.

Added in version 3.4.

Changed in version 3.13: Fixed some false positives and false negatives, see [`is_private`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address.is_private "ipaddress.IPv4Address.is_private")
 for details.

is\_unspecified[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address.is_unspecified "Link to this definition")

`True` if the address is unspecified. See [**RFC 5735**](https://datatracker.ietf.org/doc/html/rfc5735.html)
 (for IPv4) or [**RFC 2373**](https://datatracker.ietf.org/doc/html/rfc2373.html)
 (for IPv6).

is\_reserved[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address.is_reserved "Link to this definition")

`True` if the address is noted as reserved by the IETF. For IPv4, this is only `240.0.0.0/4`, the `Reserved` address block. For IPv6, this is all addresses [allocated](https://www.iana.org/assignments/ipv6-address-space/ipv6-address-space.xhtml)
 as `Reserved by IETF` for future use.

Note

For IPv4, `is_reserved` is not related to the address block value of the `Reserved-by-Protocol` column in [iana-ipv4-special-registry](https://www.iana.org/assignments/iana-ipv4-special-registry/iana-ipv4-special-registry.xhtml)
.

Caution

For IPv6, `fec0::/10` a former Site-Local scoped address prefix is currently excluded from that list (see [`is_site_local`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address.is_site_local "ipaddress.IPv6Address.is_site_local")
 & [**RFC 3879**](https://datatracker.ietf.org/doc/html/rfc3879.html)
).

is\_loopback[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address.is_loopback "Link to this definition")

`True` if this is a loopback address. See [**RFC 3330**](https://datatracker.ietf.org/doc/html/rfc3330.html)
 (for IPv4) or [**RFC 2373**](https://datatracker.ietf.org/doc/html/rfc2373.html)
 (for IPv6).

is\_link\_local[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address.is_link_local "Link to this definition")

`True` if the address is reserved for link-local usage. See [**RFC 3927**](https://datatracker.ietf.org/doc/html/rfc3927.html)
.

ipv6\_mapped[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address.ipv6_mapped "Link to this definition")

[`IPv6Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address "ipaddress.IPv6Address")
 object representing the IPv4-mapped IPv6 address. See [**RFC 4291**](https://datatracker.ietf.org/doc/html/rfc4291.html)
.

Added in version 3.13.

IPv4Address.\_\_format\_\_(_fmt_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address.__format__ "Link to this definition")

Returns a string representation of the IP address, controlled by an explicit format string. _fmt_ can be one of the following: `'s'`, the default option, equivalent to [`str()`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
, `'b'` for a zero-padded binary string, `'X'` or `'x'` for an uppercase or lowercase hexadecimal representation, or `'n'`, which is equivalent to `'b'` for IPv4 addresses and `'x'` for IPv6. For binary and hexadecimal representations, the form specifier `'#'` and the grouping option `'_'` are available. `__format__` is used by `format`, `str.format` and f-strings.

Copy

\>>> format(ipaddress.IPv4Address('192.168.0.1'))
'192.168.0.1'
\>>> '{:#b}'.format(ipaddress.IPv4Address('192.168.0.1'))
'0b11000000101010000000000000000001'
\>>> f'{ipaddress.IPv6Address("2001:db8::1000"):s}'
'2001:db8::1000'
\>>> format(ipaddress.IPv6Address('2001:db8::1000'), '\_X')
'2001\_0DB8\_0000\_0000\_0000\_0000\_0000\_1000'
\>>> '{:#\_n}'.format(ipaddress.IPv6Address('2001:db8::1000'))
'0x2001\_0db8\_0000\_0000\_0000\_0000\_0000\_1000'

Added in version 3.9.

class ipaddress.IPv6Address(_address_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address "Link to this definition")

Construct an IPv6 address. An [`AddressValueError`](https://docs.python.org/3/library/ipaddress.html#ipaddress.AddressValueError "ipaddress.AddressValueError")
 is raised if _address_ is not a valid IPv6 address.

The following constitutes a valid IPv6 address:

1.  A string consisting of eight groups of four hexadecimal digits, each group representing 16 bits. The groups are separated by colons. This describes an _exploded_ (longhand) notation. The string can also be _compressed_ (shorthand notation) by various means. See [**RFC 4291**](https://datatracker.ietf.org/doc/html/rfc4291.html)
     for details. For example, `"0000:0000:0000:0000:0000:0abc:0007:0def"` can be compressed to `"::abc:7:def"`.
    
    Optionally, the string may also have a scope zone ID, expressed with a suffix `%scope_id`. If present, the scope ID must be non-empty, and may not contain `%`. See [**RFC 4007**](https://datatracker.ietf.org/doc/html/rfc4007.html)
     for details. For example, `fe80::1234%1` might identify address `fe80::1234` on the first link of the node.
    
2.  An integer that fits into 128 bits.
    
3.  An integer packed into a [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
     object of length 16, big-endian.
    

Copy

\>>> ipaddress.IPv6Address('2001:db8::1000')
IPv6Address('2001:db8::1000')
\>>> ipaddress.IPv6Address('ff02::5678%1')
IPv6Address('ff02::5678%1')

compressed[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address.compressed "Link to this definition")

The short form of the address representation, with leading zeroes in groups omitted and the longest sequence of groups consisting entirely of zeroes collapsed to a single empty group.

This is also the value returned by `str(addr)` for IPv6 addresses.

exploded[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address.exploded "Link to this definition")

The long form of the address representation, with all leading zeroes and groups consisting entirely of zeroes included.

For the following attributes and methods, see the corresponding documentation of the [`IPv4Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address "ipaddress.IPv4Address")
 class:

packed[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address.packed "Link to this definition")

reverse\_pointer[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address.reverse_pointer "Link to this definition")

version[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address.version "Link to this definition")

max\_prefixlen[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address.max_prefixlen "Link to this definition")

is\_multicast[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address.is_multicast "Link to this definition")

is\_private[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address.is_private "Link to this definition")

is\_global[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address.is_global "Link to this definition")

Added in version 3.4.

is\_unspecified[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address.is_unspecified "Link to this definition")

is\_reserved[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address.is_reserved "Link to this definition")

is\_loopback[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address.is_loopback "Link to this definition")

is\_link\_local[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address.is_link_local "Link to this definition")

is\_site\_local[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address.is_site_local "Link to this definition")

`True` if the address is reserved for site-local usage. Note that the site-local address space has been deprecated by [**RFC 3879**](https://datatracker.ietf.org/doc/html/rfc3879.html)
. Use [`is_private`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address.is_private "ipaddress.IPv4Address.is_private")
 to test if this address is in the space of unique local addresses as defined by [**RFC 4193**](https://datatracker.ietf.org/doc/html/rfc4193.html)
.

ipv4\_mapped[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address.ipv4_mapped "Link to this definition")

For addresses that appear to be IPv4 mapped addresses in the range `::FFFF:0:0/96` as defined by [**RFC 4291**](https://datatracker.ietf.org/doc/html/rfc4291.html)
, this property reports the embedded IPv4 address. For any other address, this property will be `None`.

scope\_id[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address.scope_id "Link to this definition")

For scoped addresses as defined by [**RFC 4007**](https://datatracker.ietf.org/doc/html/rfc4007.html)
, this property identifies the particular zone of the address’s scope that the address belongs to, as a string. When no scope zone is specified, this property will be `None`.

sixtofour[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address.sixtofour "Link to this definition")

For addresses that appear to be 6to4 addresses (starting with `2002::/16`) as defined by [**RFC 3056**](https://datatracker.ietf.org/doc/html/rfc3056.html)
, this property will report the embedded IPv4 address. For any other address, this property will be `None`.

teredo[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address.teredo "Link to this definition")

For addresses that appear to be Teredo addresses (starting with `2001::/32`) as defined by [**RFC 4380**](https://datatracker.ietf.org/doc/html/rfc4380.html)
, this property will report the embedded `(server, client)` IP address pair. For any other address, this property will be `None`.

IPv6Address.\_\_format\_\_(_fmt_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address.__format__ "Link to this definition")

Refer to the corresponding method documentation in [`IPv4Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address "ipaddress.IPv4Address")
.

Added in version 3.9.

### Conversion to Strings and Integers[¶](https://docs.python.org/3/library/ipaddress.html#conversion-to-strings-and-integers "Link to this heading")

To interoperate with networking interfaces such as the socket module, addresses must be converted to strings or integers. This is handled using the [`str()`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 and [`int()`](https://docs.python.org/3/builtins/functions.html#int "int")
 builtin functions:

Copy

\>>> str(ipaddress.IPv4Address('192.168.0.1'))
'192.168.0.1'
\>>> int(ipaddress.IPv4Address('192.168.0.1'))
3232235521
\>>> str(ipaddress.IPv6Address('::1'))
'::1'
\>>> int(ipaddress.IPv6Address('::1'))
1

Note that IPv6 scoped addresses are converted to integers without scope zone ID.

### Operators[¶](https://docs.python.org/3/library/ipaddress.html#operators "Link to this heading")

Address objects support some operators. Unless stated otherwise, operators can only be applied between compatible objects (i.e. IPv4 with IPv4, IPv6 with IPv6).

#### Comparison operators[¶](https://docs.python.org/3/library/ipaddress.html#comparison-operators "Link to this heading")

Address objects can be compared with the usual set of comparison operators. Same IPv6 addresses with different scope zone IDs are not equal. Some examples:

Copy

\>>> IPv4Address('127.0.0.2') \> IPv4Address('127.0.0.1')
True
\>>> IPv4Address('127.0.0.2') \== IPv4Address('127.0.0.1')
False
\>>> IPv4Address('127.0.0.2') != IPv4Address('127.0.0.1')
True
\>>> IPv6Address('fe80::1234') \== IPv6Address('fe80::1234%1')
False
\>>> IPv6Address('fe80::1234%1') != IPv6Address('fe80::1234%2')
True

#### Arithmetic operators[¶](https://docs.python.org/3/library/ipaddress.html#arithmetic-operators "Link to this heading")

Integers can be added to or subtracted from address objects. Some examples:

Copy

\>>> IPv4Address('127.0.0.2') + 3
IPv4Address('127.0.0.5')
\>>> IPv4Address('127.0.0.2') \- 3
IPv4Address('126.255.255.255')
\>>> IPv4Address('255.255.255.255') + 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ipaddress.AddressValueError: 4294967296 (>= 2\*\*32) is not permitted as an IPv4 address

IP Network definitions[¶](https://docs.python.org/3/library/ipaddress.html#ip-network-definitions "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

The [`IPv4Network`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network "ipaddress.IPv4Network")
 and [`IPv6Network`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network "ipaddress.IPv6Network")
 objects provide a mechanism for defining and inspecting IP network definitions. A network definition consists of a _mask_ and a _network address_, and as such defines a range of IP addresses that equal the network address when masked (binary AND) with the mask. For example, a network definition with the mask `255.255.255.0` and the network address `192.168.1.0` consists of IP addresses in the inclusive range `192.168.1.0` to `192.168.1.255`.

### Prefix, net mask and host mask[¶](https://docs.python.org/3/library/ipaddress.html#prefix-net-mask-and-host-mask "Link to this heading")

There are several equivalent ways to specify IP network masks. A _prefix_ `/<nbits>` is a notation that denotes how many high-order bits are set in the network mask. A _net mask_ is an IP address with some number of high-order bits set. Thus the prefix `/24` is equivalent to the net mask `255.255.255.0` in IPv4, or `ffff:ff00::` in IPv6. In addition, a _host mask_ is the logical inverse of a _net mask_, and is sometimes used (for example in Cisco access control lists) to denote a network mask. The host mask equivalent to `/24` in IPv4 is `0.0.0.255`.

### Network objects[¶](https://docs.python.org/3/library/ipaddress.html#network-objects "Link to this heading")

All attributes implemented by address objects are implemented by network objects as well. In addition, network objects implement additional attributes. All of these are common between [`IPv4Network`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network "ipaddress.IPv4Network")
 and [`IPv6Network`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network "ipaddress.IPv6Network")
, so to avoid duplication they are only documented for `IPv4Network`. Network objects are [hashable](https://docs.python.org/3/glossary.html#term-hashable)
, so they can be used as keys in dictionaries.

class ipaddress.IPv4Network(_address_, _strict\=True_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network "Link to this definition")

Construct an IPv4 network definition. _address_ can be one of the following:

1.  A string consisting of an IP address and an optional mask, separated by a slash (`/`). The IP address is the network address, and the mask can be either a single number, which means it’s a _prefix_, or a string representation of an IPv4 address. If it’s the latter, the mask is interpreted as a _net mask_ if it starts with a non-zero field, or as a _host mask_ if it starts with a zero field, with the single exception of an all-zero mask which is treated as a _net mask_. If no mask is provided, it’s considered to be `/32`.
    
    For example, the following _address_ specifications are equivalent: `192.168.1.0/24`, `192.168.1.0/255.255.255.0` and `192.168.1.0/0.0.0.255`.
    
2.  An integer that fits into 32 bits. This is equivalent to a single-address network, with the network address being _address_ and the mask being `/32`.
    
3.  An integer packed into a [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
     object of length 4, big-endian. The interpretation is similar to an integer _address_.
    
4.  A two-tuple of an address description and a netmask, where the address description is either a string, a 32-bits integer, a 4-bytes packed integer, or an existing [`IPv4Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address "ipaddress.IPv4Address")
     object; and the netmask is either an integer representing the prefix length (e.g. `24`) or a string representing the prefix mask (e.g. `255.255.255.0`).
    

An [`AddressValueError`](https://docs.python.org/3/library/ipaddress.html#ipaddress.AddressValueError "ipaddress.AddressValueError")
 is raised if _address_ is not a valid IPv4 address. A [`NetmaskValueError`](https://docs.python.org/3/library/ipaddress.html#ipaddress.NetmaskValueError "ipaddress.NetmaskValueError")
 is raised if the mask is not valid for an IPv4 address.

If _strict_ is `True` and host bits are set in the supplied address, then [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 is raised. Otherwise, the host bits are masked out to determine the appropriate network address.

Unless stated otherwise, all network methods accepting other network/address objects will raise [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 if the argument’s IP version is incompatible to `self`.

Changed in version 3.5: Added the two-tuple form for the _address_ constructor parameter.

version[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.version "Link to this definition")

max\_prefixlen[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.max_prefixlen "Link to this definition")

Refer to the corresponding attribute documentation in [`IPv4Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address "ipaddress.IPv4Address")
.

is\_multicast[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.is_multicast "Link to this definition")

is\_private[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.is_private "Link to this definition")

is\_unspecified[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.is_unspecified "Link to this definition")

is\_reserved[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.is_reserved "Link to this definition")

is\_loopback[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.is_loopback "Link to this definition")

is\_link\_local[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.is_link_local "Link to this definition")

These attributes are true for the network as a whole if they are true for both the network address and the broadcast address.

network\_address[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.network_address "Link to this definition")

The network address for the network. The network address and the prefix length together uniquely define a network.

broadcast\_address[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.broadcast_address "Link to this definition")

The broadcast address for the network. Packets sent to the broadcast address should be received by every host on the network.

hostmask[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.hostmask "Link to this definition")

The host mask, as an [`IPv4Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address "ipaddress.IPv4Address")
 object.

netmask[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.netmask "Link to this definition")

The net mask, as an [`IPv4Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address "ipaddress.IPv4Address")
 object.

with\_prefixlen[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.with_prefixlen "Link to this definition")

compressed[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.compressed "Link to this definition")

exploded[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.exploded "Link to this definition")

A string representation of the network, with the mask in prefix notation.

`with_prefixlen` and `compressed` are always the same as `str(network)`. `exploded` uses the exploded form the network address.

with\_netmask[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.with_netmask "Link to this definition")

A string representation of the network, with the mask in net mask notation.

with\_hostmask[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.with_hostmask "Link to this definition")

A string representation of the network, with the mask in host mask notation.

num\_addresses[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.num_addresses "Link to this definition")

The total number of addresses in the network.

prefixlen[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.prefixlen "Link to this definition")

Length of the network prefix, in bits.

hosts()[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.hosts "Link to this definition")

Returns an iterator over the usable hosts in the network. The usable hosts are all the IP addresses that belong to the network, except the network address itself and the network broadcast address. For networks with a mask length of 31, the network address and network broadcast address are also included in the result. Networks with a mask of 32 will return a list containing the single host address.

Copy

\>>> list(ip\_network('192.0.2.0/29').hosts())
\[IPv4Address('192.0.2.1'), IPv4Address('192.0.2.2'),\
 IPv4Address('192.0.2.3'), IPv4Address('192.0.2.4'),\
 IPv4Address('192.0.2.5'), IPv4Address('192.0.2.6')\]
\>>> list(ip\_network('192.0.2.0/31').hosts())
\[IPv4Address('192.0.2.0'), IPv4Address('192.0.2.1')\]
\>>> list(ip\_network('192.0.2.1/32').hosts())
\[IPv4Address('192.0.2.1')\]

overlaps(_other_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.overlaps "Link to this definition")

`True` if this network is partly or wholly contained in _other_ or _other_ is wholly contained in this network.

address\_exclude(_network_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.address_exclude "Link to this definition")

Computes the network definitions resulting from removing the given _network_ from this one. Returns an iterator of network objects. Raises [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 if _network_ is not completely contained in this network.

Copy

\>>> n1 \= ip\_network('192.0.2.0/28')
\>>> n2 \= ip\_network('192.0.2.1/32')
\>>> list(n1.address\_exclude(n2))
\[IPv4Network('192.0.2.8/29'), IPv4Network('192.0.2.4/30'),\
 IPv4Network('192.0.2.2/31'), IPv4Network('192.0.2.0/32')\]

subnets(_prefixlen\_diff\=1_, _new\_prefix\=None_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.subnets "Link to this definition")

The subnets that join to make the current network definition, depending on the argument values. _prefixlen\_diff_ is the amount our prefix length should be increased by. _new\_prefix_ is the desired new prefix of the subnets; it must be larger than our prefix. One and only one of _prefixlen\_diff_ and _new\_prefix_ must be set. Returns an iterator of network objects.

Copy

\>>> list(ip\_network('192.0.2.0/24').subnets())
\[IPv4Network('192.0.2.0/25'), IPv4Network('192.0.2.128/25')\]
\>>> list(ip\_network('192.0.2.0/24').subnets(prefixlen\_diff\=2))
\[IPv4Network('192.0.2.0/26'), IPv4Network('192.0.2.64/26'),\
 IPv4Network('192.0.2.128/26'), IPv4Network('192.0.2.192/26')\]
\>>> list(ip\_network('192.0.2.0/24').subnets(new\_prefix\=26))
\[IPv4Network('192.0.2.0/26'), IPv4Network('192.0.2.64/26'),\
 IPv4Network('192.0.2.128/26'), IPv4Network('192.0.2.192/26')\]
\>>> list(ip\_network('192.0.2.0/24').subnets(new\_prefix\=23))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    raise ValueError('new prefix must be longer')
ValueError: new prefix must be longer
\>>> list(ip\_network('192.0.2.0/24').subnets(new\_prefix\=25))
\[IPv4Network('192.0.2.0/25'), IPv4Network('192.0.2.128/25')\]

supernet(_prefixlen\_diff\=1_, _new\_prefix\=None_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.supernet "Link to this definition")

The supernet containing this network definition, depending on the argument values. _prefixlen\_diff_ is the amount our prefix length should be decreased by. _new\_prefix_ is the desired new prefix of the supernet; it must be smaller than our prefix. One and only one of _prefixlen\_diff_ and _new\_prefix_ must be set. Returns a single network object.

Copy

\>>> ip\_network('192.0.2.0/24').supernet()
IPv4Network('192.0.2.0/23')
\>>> ip\_network('192.0.2.0/24').supernet(prefixlen\_diff\=2)
IPv4Network('192.0.0.0/22')
\>>> ip\_network('192.0.2.0/24').supernet(new\_prefix\=20)
IPv4Network('192.0.0.0/20')

subnet\_of(_other_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.subnet_of "Link to this definition")

Return `True` if this network is a subnet of _other_.

Copy

\>>> a \= ip\_network('192.168.1.0/24')
\>>> b \= ip\_network('192.168.1.128/30')
\>>> b.subnet\_of(a)
True

Added in version 3.7.

supernet\_of(_other_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.supernet_of "Link to this definition")

Return `True` if this network is a supernet of _other_.

Copy

\>>> a \= ip\_network('192.168.1.0/24')
\>>> b \= ip\_network('192.168.1.128/30')
\>>> a.supernet\_of(b)
True

Added in version 3.7.

compare\_networks(_other_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.compare_networks "Link to this definition")

Compare this network to _other_. In this comparison only the network addresses are considered; host bits aren’t. Returns either `-1`, `0` or `1`.

Copy

\>>> ip\_network('192.0.2.1/32').compare\_networks(ip\_network('192.0.2.2/32'))
\-1
\>>> ip\_network('192.0.2.1/32').compare\_networks(ip\_network('192.0.2.0/32'))
1
\>>> ip\_network('192.0.2.1/32').compare\_networks(ip\_network('192.0.2.1/32'))
0

Deprecated since version 3.7: It uses the same ordering and comparison algorithm as “<”, “==”, and “>”

class ipaddress.IPv6Network(_address_, _strict\=True_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network "Link to this definition")

Construct an IPv6 network definition. _address_ can be one of the following:

1.  A string consisting of an IP address and an optional prefix length, separated by a slash (`/`). The IP address is the network address, and the prefix length must be a single number, the _prefix_. If no prefix length is provided, it’s considered to be `/128`.
    
    Note that currently expanded netmasks are not supported. That means `2001:db00::0/24` is a valid argument while `2001:db00::0/ffff:ff00::` is not.
    
2.  An integer that fits into 128 bits. This is equivalent to a single-address network, with the network address being _address_ and the mask being `/128`.
    
3.  An integer packed into a [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
     object of length 16, big-endian. The interpretation is similar to an integer _address_.
    
4.  A two-tuple of an address description and a netmask, where the address description is either a string, a 128-bits integer, a 16-bytes packed integer, or an existing [`IPv6Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address "ipaddress.IPv6Address")
     object; and the netmask is an integer representing the prefix length.
    

An [`AddressValueError`](https://docs.python.org/3/library/ipaddress.html#ipaddress.AddressValueError "ipaddress.AddressValueError")
 is raised if _address_ is not a valid IPv6 address. A [`NetmaskValueError`](https://docs.python.org/3/library/ipaddress.html#ipaddress.NetmaskValueError "ipaddress.NetmaskValueError")
 is raised if the mask is not valid for an IPv6 address.

If _strict_ is `True` and host bits are set in the supplied address, then [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 is raised. Otherwise, the host bits are masked out to determine the appropriate network address.

Changed in version 3.5: Added the two-tuple form for the _address_ constructor parameter.

version[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.version "Link to this definition")

max\_prefixlen[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.max_prefixlen "Link to this definition")

is\_multicast[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.is_multicast "Link to this definition")

is\_private[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.is_private "Link to this definition")

is\_unspecified[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.is_unspecified "Link to this definition")

is\_reserved[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.is_reserved "Link to this definition")

is\_loopback[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.is_loopback "Link to this definition")

is\_link\_local[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.is_link_local "Link to this definition")

network\_address[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.network_address "Link to this definition")

broadcast\_address[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.broadcast_address "Link to this definition")

hostmask[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.hostmask "Link to this definition")

netmask[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.netmask "Link to this definition")

with\_prefixlen[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.with_prefixlen "Link to this definition")

compressed[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.compressed "Link to this definition")

exploded[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.exploded "Link to this definition")

with\_netmask[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.with_netmask "Link to this definition")

with\_hostmask[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.with_hostmask "Link to this definition")

num\_addresses[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.num_addresses "Link to this definition")

prefixlen[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.prefixlen "Link to this definition")

hosts()[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.hosts "Link to this definition")

Returns an iterator over the usable hosts in the network. The usable hosts are all the IP addresses that belong to the network, except the Subnet-Router anycast address. For networks with a mask length of 127, the Subnet-Router anycast address is also included in the result. Networks with a mask of 128 will return a list containing the single host address.

overlaps(_other_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.overlaps "Link to this definition")

address\_exclude(_network_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.address_exclude "Link to this definition")

subnets(_prefixlen\_diff\=1_, _new\_prefix\=None_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.subnets "Link to this definition")

supernet(_prefixlen\_diff\=1_, _new\_prefix\=None_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.supernet "Link to this definition")

subnet\_of(_other_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.subnet_of "Link to this definition")

supernet\_of(_other_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.supernet_of "Link to this definition")

compare\_networks(_other_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.compare_networks "Link to this definition")

Refer to the corresponding attribute documentation in [`IPv4Network`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network "ipaddress.IPv4Network")
.

is\_site\_local[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.is_site_local "Link to this definition")

This attribute is true for the network as a whole if it is true for both the network address and the broadcast address.

### Operators[¶](https://docs.python.org/3/library/ipaddress.html#id1 "Link to this heading")

Network objects support some operators. Unless stated otherwise, operators can only be applied between compatible objects (i.e. IPv4 with IPv4, IPv6 with IPv6).

#### Logical operators[¶](https://docs.python.org/3/library/ipaddress.html#logical-operators "Link to this heading")

Network objects can be compared with the usual set of logical operators. Network objects are ordered first by network address, then by net mask.

#### Iteration[¶](https://docs.python.org/3/library/ipaddress.html#iteration "Link to this heading")

Network objects can be iterated to list all the addresses belonging to the network. For iteration, _all_ hosts are returned, including unusable hosts (for usable hosts, use the [`hosts()`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.hosts "ipaddress.IPv4Network.hosts")
 method). An example:

Copy

\>>> for addr in IPv4Network('192.0.2.0/28'):
...     addr
...
IPv4Address('192.0.2.0')
IPv4Address('192.0.2.1')
IPv4Address('192.0.2.2')
IPv4Address('192.0.2.3')
IPv4Address('192.0.2.4')
IPv4Address('192.0.2.5')
IPv4Address('192.0.2.6')
IPv4Address('192.0.2.7')
IPv4Address('192.0.2.8')
IPv4Address('192.0.2.9')
IPv4Address('192.0.2.10')
IPv4Address('192.0.2.11')
IPv4Address('192.0.2.12')
IPv4Address('192.0.2.13')
IPv4Address('192.0.2.14')
IPv4Address('192.0.2.15')

#### Networks as containers of addresses[¶](https://docs.python.org/3/library/ipaddress.html#networks-as-containers-of-addresses "Link to this heading")

Network objects can act as containers of addresses. Some examples:

Copy

\>>> IPv4Network('192.0.2.0/28')\[0\]
IPv4Address('192.0.2.0')
\>>> IPv4Network('192.0.2.0/28')\[15\]
IPv4Address('192.0.2.15')
\>>> IPv4Address('192.0.2.6') in IPv4Network('192.0.2.0/28')
True
\>>> IPv4Address('192.0.3.6') in IPv4Network('192.0.2.0/28')
False

Interface objects[¶](https://docs.python.org/3/library/ipaddress.html#interface-objects "Link to this heading")

----------------------------------------------------------------------------------------------------------------

Interface objects are [hashable](https://docs.python.org/3/glossary.html#term-hashable)
, so they can be used as keys in dictionaries.

class ipaddress.IPv4Interface(_address_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Interface "Link to this definition")

Construct an IPv4 interface. The meaning of _address_ is as in the constructor of [`IPv4Network`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network "ipaddress.IPv4Network")
, except that arbitrary host addresses are always accepted.

`IPv4Interface` is a subclass of [`IPv4Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address "ipaddress.IPv4Address")
, so it inherits all the attributes from that class. In addition, the following attributes are available:

ip[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Interface.ip "Link to this definition")

The address ([`IPv4Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address "ipaddress.IPv4Address")
) without network information.

Copy

\>>> interface \= IPv4Interface('192.0.2.5/24')
\>>> interface.ip
IPv4Address('192.0.2.5')

network[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Interface.network "Link to this definition")

The network ([`IPv4Network`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network "ipaddress.IPv4Network")
) this interface belongs to.

Copy

\>>> interface \= IPv4Interface('192.0.2.5/24')
\>>> interface.network
IPv4Network('192.0.2.0/24')

with\_prefixlen[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Interface.with_prefixlen "Link to this definition")

A string representation of the interface with the mask in prefix notation.

Copy

\>>> interface \= IPv4Interface('192.0.2.5/24')
\>>> interface.with\_prefixlen
'192.0.2.5/24'

with\_netmask[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Interface.with_netmask "Link to this definition")

A string representation of the interface with the network as a net mask.

Copy

\>>> interface \= IPv4Interface('192.0.2.5/24')
\>>> interface.with\_netmask
'192.0.2.5/255.255.255.0'

with\_hostmask[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Interface.with_hostmask "Link to this definition")

A string representation of the interface with the network as a host mask.

Copy

\>>> interface \= IPv4Interface('192.0.2.5/24')
\>>> interface.with\_hostmask
'192.0.2.5/0.0.0.255'

class ipaddress.IPv6Interface(_address_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Interface "Link to this definition")

Construct an IPv6 interface. The meaning of _address_ is as in the constructor of [`IPv6Network`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network "ipaddress.IPv6Network")
, except that arbitrary host addresses are always accepted.

`IPv6Interface` is a subclass of [`IPv6Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address "ipaddress.IPv6Address")
, so it inherits all the attributes from that class. In addition, the following attributes are available:

ip[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Interface.ip "Link to this definition")

network[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Interface.network "Link to this definition")

with\_prefixlen[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Interface.with_prefixlen "Link to this definition")

with\_netmask[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Interface.with_netmask "Link to this definition")

with\_hostmask[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Interface.with_hostmask "Link to this definition")

Refer to the corresponding attribute documentation in [`IPv4Interface`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Interface "ipaddress.IPv4Interface")
.

### Operators[¶](https://docs.python.org/3/library/ipaddress.html#id2 "Link to this heading")

Interface objects support some operators. Unless stated otherwise, operators can only be applied between compatible objects (i.e. IPv4 with IPv4, IPv6 with IPv6).

#### Logical operators[¶](https://docs.python.org/3/library/ipaddress.html#id3 "Link to this heading")

Interface objects can be compared with the usual set of logical operators.

For equality comparison (`==` and `!=`), both the IP address and network must be the same for the objects to be equal. An interface will not compare equal to any address or network object.

For ordering (`<`, `>`, etc) the rules are different. Interface and address objects with the same IP version can be compared, and the address objects will always sort before the interface objects. Two interface objects are first compared by their networks and, if those are the same, then by their IP addresses.

Other Module Level Functions[¶](https://docs.python.org/3/library/ipaddress.html#other-module-level-functions "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------

The module also provides the following module level functions:

ipaddress.v4\_int\_to\_packed(_address_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.v4_int_to_packed "Link to this definition")

Represent an address as 4 packed bytes in network (big-endian) order. _address_ is an integer representation of an IPv4 IP address. A [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 is raised if the integer is negative or too large to be an IPv4 IP address.

Copy

\>>> ipaddress.ip\_address(3221225985)
IPv4Address('192.0.2.1')
\>>> ipaddress.v4\_int\_to\_packed(3221225985)
b'\\xc0\\x00\\x02\\x01'

ipaddress.v6\_int\_to\_packed(_address_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.v6_int_to_packed "Link to this definition")

Represent an address as 16 packed bytes in network (big-endian) order. _address_ is an integer representation of an IPv6 IP address. A [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 is raised if the integer is negative or too large to be an IPv6 IP address.

ipaddress.summarize\_address\_range(_first_, _last_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.summarize_address_range "Link to this definition")

Return an iterator of the summarized network range given the first and last IP addresses. _first_ is the first [`IPv4Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address "ipaddress.IPv4Address")
 or [`IPv6Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address "ipaddress.IPv6Address")
 in the range and _last_ is the last `IPv4Address` or `IPv6Address` in the range. A [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 is raised if _first_ or _last_ are not IP addresses or are not of the same version. A [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 is raised if _last_ is not greater than _first_ or if _first_ address version is not 4 or 6.

Copy

\>>> \[ipaddr for ipaddr in ipaddress.summarize\_address\_range(\
...    ipaddress.IPv4Address('192.0.2.0'),\
...    ipaddress.IPv4Address('192.0.2.130'))\]
\[IPv4Network('192.0.2.0/25'), IPv4Network('192.0.2.128/31'), IPv4Network('192.0.2.130/32')\]

ipaddress.collapse\_addresses(_addresses_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.collapse_addresses "Link to this definition")

Return an iterator of the collapsed [`IPv4Network`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network "ipaddress.IPv4Network")
 or [`IPv6Network`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network "ipaddress.IPv6Network")
 objects. _addresses_ is an [iterable](https://docs.python.org/3/glossary.html#term-iterable)
 of `IPv4Network` or `IPv6Network` objects. A [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 is raised if _addresses_ contains mixed version objects.

Copy

\>>> \[ipaddr for ipaddr in\
... ipaddress.collapse\_addresses(\[ipaddress.IPv4Network('192.0.2.0/25'),\
... ipaddress.IPv4Network('192.0.2.128/25')\])\]
\[IPv4Network('192.0.2.0/24')\]

ipaddress.get\_mixed\_type\_key(_obj_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.get_mixed_type_key "Link to this definition")

Return a key suitable for sorting between networks and addresses. Address and Network objects are not sortable by default; they’re fundamentally different, so the expression:

Copy

IPv4Address('192.0.2.0') <= IPv4Network('192.0.2.0/24')

doesn’t make sense. There are some times however, where you may wish to have `ipaddress` sort these anyway. If you need to do this, you can use this function as the _key_ argument to [`sorted()`](https://docs.python.org/3/builtins/functions.html#sorted "sorted")
.

_obj_ is either a network or address object.

Custom Exceptions[¶](https://docs.python.org/3/library/ipaddress.html#custom-exceptions "Link to this heading")

----------------------------------------------------------------------------------------------------------------

To support more specific error reporting from class constructors, the module defines the following exceptions:

exception ipaddress.AddressValueError(_ValueError_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.AddressValueError "Link to this definition")

Any value error related to the address.

exception ipaddress.NetmaskValueError(_ValueError_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.NetmaskValueError "Link to this definition")

Any value error related to the net mask.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`ipaddress` — IPv4/IPv6 manipulation library](https://docs.python.org/3/library/ipaddress.html#)
    *   [Convenience factory functions](https://docs.python.org/3/library/ipaddress.html#convenience-factory-functions)
        
    *   [IP Addresses](https://docs.python.org/3/library/ipaddress.html#ip-addresses)
        *   [Address objects](https://docs.python.org/3/library/ipaddress.html#address-objects)
            
        *   [Conversion to Strings and Integers](https://docs.python.org/3/library/ipaddress.html#conversion-to-strings-and-integers)
            
        *   [Operators](https://docs.python.org/3/library/ipaddress.html#operators)
            *   [Comparison operators](https://docs.python.org/3/library/ipaddress.html#comparison-operators)
                
            *   [Arithmetic operators](https://docs.python.org/3/library/ipaddress.html#arithmetic-operators)
                
    *   [IP Network definitions](https://docs.python.org/3/library/ipaddress.html#ip-network-definitions)
        *   [Prefix, net mask and host mask](https://docs.python.org/3/library/ipaddress.html#prefix-net-mask-and-host-mask)
            
        *   [Network objects](https://docs.python.org/3/library/ipaddress.html#network-objects)
            
        *   [Operators](https://docs.python.org/3/library/ipaddress.html#id1)
            *   [Logical operators](https://docs.python.org/3/library/ipaddress.html#logical-operators)
                
            *   [Iteration](https://docs.python.org/3/library/ipaddress.html#iteration)
                
            *   [Networks as containers of addresses](https://docs.python.org/3/library/ipaddress.html#networks-as-containers-of-addresses)
                
    *   [Interface objects](https://docs.python.org/3/library/ipaddress.html#interface-objects)
        *   [Operators](https://docs.python.org/3/library/ipaddress.html#id2)
            *   [Logical operators](https://docs.python.org/3/library/ipaddress.html#id3)
                
    *   [Other Module Level Functions](https://docs.python.org/3/library/ipaddress.html#other-module-level-functions)
        
    *   [Custom Exceptions](https://docs.python.org/3/library/ipaddress.html#custom-exceptions)
        

#### Previous topic

[`xmlrpc.server` — Basic XML-RPC servers](https://docs.python.org/3/library/xmlrpc.server.html "previous chapter")

#### Next topic

[Multimedia Services](https://docs.python.org/3/library/mm.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=ipaddress+%E2%80%94+IPv4%2FIPv6+manipulation+library&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fipaddress.html&pagesource=library%2Fipaddress.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/ipaddress.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/mm.html "Multimedia Services")
     |
*   [previous](https://docs.python.org/3/library/xmlrpc.server.html "xmlrpc.server — Basic XML-RPC servers")
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
*   [`ipaddress` — IPv4/IPv6 manipulation library](https://docs.python.org/3/library/ipaddress.html)
    
*    
    
    |
*   Theme Auto Light Dark |