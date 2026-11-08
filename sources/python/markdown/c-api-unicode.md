### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/tuple.html "Tuple Objects")
     |
*   [previous](https://docs.python.org/3/c-api/bytearray.html "Byte Array Objects")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python/C API reference manual](https://docs.python.org/3/c-api/index.html)
     »
*   [Concrete Objects Layer](https://docs.python.org/3/c-api/concrete.html)
     »
*   [Unicode Objects and Codecs](https://docs.python.org/3/c-api/unicode.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Unicode Objects and Codecs[¶](https://docs.python.org/3/c-api/unicode.html#unicode-objects-and-codecs "Link to this heading")

==============================================================================================================================

Unicode Objects[¶](https://docs.python.org/3/c-api/unicode.html#unicode-objects "Link to this heading")

--------------------------------------------------------------------------------------------------------

Since the implementation of [**PEP 393**](https://peps.python.org/pep-0393/)
 in Python 3.3, Unicode objects internally use a variety of representations, in order to allow handling the complete range of Unicode characters while staying memory efficient. There are special cases for strings where all code points are below 128, 256, or 65536; otherwise, code points must be below 1114112 (which is the full Unicode range).

UTF-8 representation is created on demand and cached in the Unicode object.

**CPython implementation detail:** The internal buffer always includes an extra trailing null character for compatibility with null terminated C strings. This extra character is not counted in [`PyUnicode_GetLength()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_GetLength "PyUnicode_GetLength")
 nor in the various _size_ arguments of the functions below.

Note

The [`Py_UNICODE`](https://docs.python.org/3/c-api/unicode.html#c.Py_UNICODE "Py_UNICODE")
 representation has been removed since Python 3.12 with deprecated APIs. See [**PEP 623**](https://peps.python.org/pep-0623/)
 for more information.

### Unicode Type[¶](https://docs.python.org/3/c-api/unicode.html#unicode-type "Link to this heading")

These are the basic Unicode object types used for the Unicode implementation in Python:

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyUnicode\_Type[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This instance of [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 represents the Python Unicode type. It is exposed to Python code as [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyUnicodeIter\_Type[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeIter_Type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This instance of [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 represents the Python Unicode iterator type. It is used to iterate over Unicode string objects.

type Py\_UCS4[¶](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Link to this definition")
  

type Py\_UCS2[¶](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS2 "Link to this definition")
  

type Py\_UCS1[¶](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS1 "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

These types are typedefs for unsigned integer types wide enough to contain characters of 32 bits, 16 bits and 8 bits, respectively. When dealing with single Unicode characters, use [`Py_UCS4`](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
.

Added in version 3.3.

type PyASCIIObject[¶](https://docs.python.org/3/c-api/unicode.html#c.PyASCIIObject "Link to this definition")
  

type PyCompactUnicodeObject[¶](https://docs.python.org/3/c-api/unicode.html#c.PyCompactUnicodeObject "Link to this definition")
  

type PyUnicodeObject[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeObject "Link to this definition")
  

These subtypes of [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 represent a Python Unicode object. In almost all cases, they shouldn’t be used directly, since all API functions that deal with Unicode objects take and return `PyObject` pointers.

Added in version 3.3.

The structure of a particular object can be determined using the following macros. The macros cannot fail; their behavior is undefined if their argument is not a Python Unicode object.

PyUnicode\_IS\_COMPACT(o)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_IS_COMPACT "Link to this definition")
  

True if _o_ uses the [`PyCompactUnicodeObject`](https://docs.python.org/3/c-api/unicode.html#c.PyCompactUnicodeObject "PyCompactUnicodeObject")
 structure.

Added in version 3.3.

PyUnicode\_IS\_COMPACT\_ASCII(o)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_IS_COMPACT_ASCII "Link to this definition")
  

True if _o_ uses the [`PyASCIIObject`](https://docs.python.org/3/c-api/unicode.html#c.PyASCIIObject "PyASCIIObject")
 structure.

Added in version 3.3.

The following APIs are C macros and static inlined functions for fast checks and access to internal read-only data of Unicode objects:

int PyUnicode\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Check "Link to this definition")
  

Return true if the object _obj_ is a Unicode object or an instance of a Unicode subtype. This function always succeeds.

int PyUnicode\_CheckExact([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_CheckExact "Link to this definition")
  

Return true if the object _obj_ is a Unicode object, but not an instance of a subtype. This function always succeeds.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 PyUnicode\_GET\_LENGTH([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_GET_LENGTH "Link to this definition")
  

Return the length of the Unicode string, in code points. _unicode_ has to be a Unicode object in the “canonical” representation (not checked).

Added in version 3.3.

[Py\_UCS1](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS1 "Py_UCS1")
 \*PyUnicode\_1BYTE\_DATA([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_1BYTE_DATA "Link to this definition")
  

[Py\_UCS2](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS2 "Py_UCS2")
 \*PyUnicode\_2BYTE\_DATA([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_2BYTE_DATA "Link to this definition")
  

[Py\_UCS4](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
 \*PyUnicode\_4BYTE\_DATA([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_4BYTE_DATA "Link to this definition")
  

Return a pointer to the canonical representation cast to UCS1, UCS2 or UCS4 integer types for direct character access. No checks are performed if the canonical representation has the correct character size; use [`PyUnicode_KIND()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_KIND "PyUnicode_KIND")
 to select the right function.

Added in version 3.3.

PyUnicode\_1BYTE\_KIND[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_1BYTE_KIND "Link to this definition")
  

PyUnicode\_2BYTE\_KIND[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_2BYTE_KIND "Link to this definition")
  

PyUnicode\_4BYTE\_KIND[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_4BYTE_KIND "Link to this definition")
  

Return values of the [`PyUnicode_KIND()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_KIND "PyUnicode_KIND")
 macro.

Added in version 3.3.

Changed in version 3.12: `PyUnicode_WCHAR_KIND` has been removed.

int PyUnicode\_KIND([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_KIND "Link to this definition")
  

Return one of the PyUnicode kind constants (see above) that indicate how many bytes per character this Unicode object uses to store its data. _unicode_ has to be a Unicode object in the “canonical” representation (not checked).

Added in version 3.3.

void \*PyUnicode\_DATA([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DATA "Link to this definition")
  

Return a void pointer to the raw Unicode buffer. _unicode_ has to be a Unicode object in the “canonical” representation (not checked).

Added in version 3.3.

void PyUnicode\_WRITE(int kind, void \*data, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 index, [Py\_UCS4](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
 value)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_WRITE "Link to this definition")
  

Write the code point _value_ to the given zero-based _index_ in a string.

The _kind_ value and _data_ pointer must have been obtained from a string using [`PyUnicode_KIND()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_KIND "PyUnicode_KIND")
 and [`PyUnicode_DATA()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DATA "PyUnicode_DATA")
 respectively. You must hold a reference to that string while calling `PyUnicode_WRITE()`. All requirements of [`PyUnicode_WriteChar()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_WriteChar "PyUnicode_WriteChar")
 also apply.

The function performs no checks for any of its requirements, and is intended for usage in loops.

Added in version 3.3.

[Py\_UCS4](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
 PyUnicode\_READ(int kind, void \*data, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 index)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_READ "Link to this definition")
  

Read a code point from a canonical representation _data_ (as obtained with [`PyUnicode_DATA()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DATA "PyUnicode_DATA")
). No checks are performed.

**CPython implementation detail:** Accept reading the trailing null character at index [`PyUnicode_GetLength()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_GetLength "PyUnicode_GetLength")
.

Added in version 3.3.

[Py\_UCS4](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
 PyUnicode\_READ\_CHAR([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 index)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_READ_CHAR "Link to this definition")
  

Read a character from a Unicode object _unicode_, which must be in the “canonical” representation. This is less efficient than [`PyUnicode_READ()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_READ "PyUnicode_READ")
 if you do multiple consecutive reads.

**CPython implementation detail:** Accept reading the trailing null character at index [`PyUnicode_GetLength()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_GetLength "PyUnicode_GetLength")
.

Added in version 3.3.

[Py\_UCS4](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
 PyUnicode\_MAX\_CHAR\_VALUE([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_MAX_CHAR_VALUE "Link to this definition")
  

Return the maximum code point that is suitable for creating another string based on _unicode_, which must be in the “canonical” representation. This is always an approximation but more efficient than iterating over the string.

Added in version 3.3.

int PyUnicode\_IsIdentifier([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_IsIdentifier "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return `1` if the string is a valid identifier according to the language definition, section [Names (identifiers and keywords)](https://docs.python.org/3/reference/lexical_analysis.html#identifiers)
. Return `0` otherwise.

Changed in version 3.9: The function does not call [`Py_FatalError()`](https://docs.python.org/3/c-api/sys.html#c.Py_FatalError "Py_FatalError")
 anymore if the string is not ready.

unsigned int PyUnicode\_IS\_ASCII([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_IS_ASCII "Link to this definition")
  

Return true if the string only contains ASCII characters. Equivalent to [`str.isascii()`](https://docs.python.org/3/builtins/stdtypes.html#str.isascii "str.isascii")
.

Added in version 3.2.

[Py\_hash\_t](https://docs.python.org/3/c-api/hash.html#c.Py_hash_t "Py_hash_t")
 PyUnstable\_Unicode\_GET\_CACHED\_HASH([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*str)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnstable_Unicode_GET_CACHED_HASH "Link to this definition")
  

_This is [Unstable API](https://docs.python.org/3/c-api/stable.html#unstable-c-api)
. It may change without warning in minor releases._

If the hash of _str_, as returned by [`PyObject_Hash()`](https://docs.python.org/3/c-api/object.html#c.PyObject_Hash "PyObject_Hash")
, has been cached and is immediately available, return it. Otherwise, return `-1` _without_ setting an exception.

If _str_ is not a string (that is, if `PyUnicode_Check(obj)` is false), the behavior is undefined.

This function never fails with an exception.

Note that there are no guarantees on when an object’s hash is cached, and the (non-)existence of a cached hash does not imply that the string has any other properties.

### Unicode Character Properties[¶](https://docs.python.org/3/c-api/unicode.html#unicode-character-properties "Link to this heading")

Unicode provides many different character properties. The most often needed ones are available through these macros which are mapped to C functions depending on the Python configuration.

int Py\_UNICODE\_ISSPACE([Py\_UCS4](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
 ch)[¶](https://docs.python.org/3/c-api/unicode.html#c.Py_UNICODE_ISSPACE "Link to this definition")
  

Return `1` or `0` depending on whether _ch_ is a whitespace character.

int Py\_UNICODE\_ISLOWER([Py\_UCS4](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
 ch)[¶](https://docs.python.org/3/c-api/unicode.html#c.Py_UNICODE_ISLOWER "Link to this definition")
  

Return `1` or `0` depending on whether _ch_ is a lowercase character.

int Py\_UNICODE\_ISUPPER([Py\_UCS4](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
 ch)[¶](https://docs.python.org/3/c-api/unicode.html#c.Py_UNICODE_ISUPPER "Link to this definition")
  

Return `1` or `0` depending on whether _ch_ is an uppercase character.

int Py\_UNICODE\_ISTITLE([Py\_UCS4](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
 ch)[¶](https://docs.python.org/3/c-api/unicode.html#c.Py_UNICODE_ISTITLE "Link to this definition")
  

Return `1` or `0` depending on whether _ch_ is a titlecase character.

int Py\_UNICODE\_ISLINEBREAK([Py\_UCS4](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
 ch)[¶](https://docs.python.org/3/c-api/unicode.html#c.Py_UNICODE_ISLINEBREAK "Link to this definition")
  

Return `1` or `0` depending on whether _ch_ is a linebreak character.

int Py\_UNICODE\_ISDECIMAL([Py\_UCS4](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
 ch)[¶](https://docs.python.org/3/c-api/unicode.html#c.Py_UNICODE_ISDECIMAL "Link to this definition")
  

Return `1` or `0` depending on whether _ch_ is a decimal character.

int Py\_UNICODE\_ISDIGIT([Py\_UCS4](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
 ch)[¶](https://docs.python.org/3/c-api/unicode.html#c.Py_UNICODE_ISDIGIT "Link to this definition")
  

Return `1` or `0` depending on whether _ch_ is a digit character.

int Py\_UNICODE\_ISNUMERIC([Py\_UCS4](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
 ch)[¶](https://docs.python.org/3/c-api/unicode.html#c.Py_UNICODE_ISNUMERIC "Link to this definition")
  

Return `1` or `0` depending on whether _ch_ is a numeric character.

int Py\_UNICODE\_ISALPHA([Py\_UCS4](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
 ch)[¶](https://docs.python.org/3/c-api/unicode.html#c.Py_UNICODE_ISALPHA "Link to this definition")
  

Return `1` or `0` depending on whether _ch_ is an alphabetic character.

int Py\_UNICODE\_ISALNUM([Py\_UCS4](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
 ch)[¶](https://docs.python.org/3/c-api/unicode.html#c.Py_UNICODE_ISALNUM "Link to this definition")
  

Return `1` or `0` depending on whether _ch_ is an alphanumeric character.

int Py\_UNICODE\_ISPRINTABLE([Py\_UCS4](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
 ch)[¶](https://docs.python.org/3/c-api/unicode.html#c.Py_UNICODE_ISPRINTABLE "Link to this definition")
  

Return `1` or `0` depending on whether _ch_ is a printable character, in the sense of [`str.isprintable()`](https://docs.python.org/3/builtins/stdtypes.html#str.isprintable "str.isprintable")
.

These APIs can be used for fast direct character conversions:

[Py\_UCS4](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
 Py\_UNICODE\_TOLOWER([Py\_UCS4](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
 ch)[¶](https://docs.python.org/3/c-api/unicode.html#c.Py_UNICODE_TOLOWER "Link to this definition")
  

Return the character _ch_ converted to lower case.

[Py\_UCS4](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
 Py\_UNICODE\_TOUPPER([Py\_UCS4](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
 ch)[¶](https://docs.python.org/3/c-api/unicode.html#c.Py_UNICODE_TOUPPER "Link to this definition")
  

Return the character _ch_ converted to upper case.

[Py\_UCS4](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
 Py\_UNICODE\_TOTITLE([Py\_UCS4](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
 ch)[¶](https://docs.python.org/3/c-api/unicode.html#c.Py_UNICODE_TOTITLE "Link to this definition")
  

Return the character _ch_ converted to title case.

int Py\_UNICODE\_TODECIMAL([Py\_UCS4](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
 ch)[¶](https://docs.python.org/3/c-api/unicode.html#c.Py_UNICODE_TODECIMAL "Link to this definition")
  

Return the character _ch_ converted to a decimal positive integer. Return `-1` if this is not possible. This function does not raise exceptions.

int Py\_UNICODE\_TODIGIT([Py\_UCS4](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
 ch)[¶](https://docs.python.org/3/c-api/unicode.html#c.Py_UNICODE_TODIGIT "Link to this definition")
  

Return the character _ch_ converted to a single digit integer. Return `-1` if this is not possible. This function does not raise exceptions.

double Py\_UNICODE\_TONUMERIC([Py\_UCS4](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
 ch)[¶](https://docs.python.org/3/c-api/unicode.html#c.Py_UNICODE_TONUMERIC "Link to this definition")
  

Return the character _ch_ converted to a double. Return `-1.0` if this is not possible. This function does not raise exceptions.

These APIs can be used to work with surrogates:

int Py\_UNICODE\_IS\_SURROGATE([Py\_UCS4](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
 ch)[¶](https://docs.python.org/3/c-api/unicode.html#c.Py_UNICODE_IS_SURROGATE "Link to this definition")
  

Check if _ch_ is a surrogate (`0xD800 <= ch <= 0xDFFF`).

int Py\_UNICODE\_IS\_HIGH\_SURROGATE([Py\_UCS4](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
 ch)[¶](https://docs.python.org/3/c-api/unicode.html#c.Py_UNICODE_IS_HIGH_SURROGATE "Link to this definition")
  

Check if _ch_ is a high surrogate (`0xD800 <= ch <= 0xDBFF`).

int Py\_UNICODE\_IS\_LOW\_SURROGATE([Py\_UCS4](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
 ch)[¶](https://docs.python.org/3/c-api/unicode.html#c.Py_UNICODE_IS_LOW_SURROGATE "Link to this definition")
  

Check if _ch_ is a low surrogate (`0xDC00 <= ch <= 0xDFFF`).

[Py\_UCS4](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
 Py\_UNICODE\_HIGH\_SURROGATE([Py\_UCS4](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
 ch)[¶](https://docs.python.org/3/c-api/unicode.html#c.Py_UNICODE_HIGH_SURROGATE "Link to this definition")
  

Return the high UTF-16 surrogate (`0xD800` to `0xDBFF`) for a Unicode code point in the range `[0x10000; 0x10FFFF]`.

[Py\_UCS4](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
 Py\_UNICODE\_LOW\_SURROGATE([Py\_UCS4](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
 ch)[¶](https://docs.python.org/3/c-api/unicode.html#c.Py_UNICODE_LOW_SURROGATE "Link to this definition")
  

Return the low UTF-16 surrogate (`0xDC00` to `0xDFFF`) for a Unicode code point in the range `[0x10000; 0x10FFFF]`.

[Py\_UCS4](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
 Py\_UNICODE\_JOIN\_SURROGATES([Py\_UCS4](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
 high, [Py\_UCS4](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
 low)[¶](https://docs.python.org/3/c-api/unicode.html#c.Py_UNICODE_JOIN_SURROGATES "Link to this definition")
  

Join two surrogate code points and return a single [`Py_UCS4`](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
 value. _high_ and _low_ are respectively the leading and trailing surrogates in a surrogate pair. _high_ must be in the range `[0xD800; 0xDBFF]` and _low_ must be in the range `[0xDC00; 0xDFFF]`.

### Creating and accessing Unicode strings[¶](https://docs.python.org/3/c-api/unicode.html#creating-and-accessing-unicode-strings "Link to this heading")

To create Unicode objects and access their basic sequence properties, use these APIs:

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_New([Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 size, [Py\_UCS4](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
 maxchar)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_New "Link to this definition")
  

_Return value: New reference._

Create a new Unicode object. _maxchar_ should be the true maximum code point to be placed in the string. As an approximation, it can be rounded up to the nearest value in the sequence 127, 255, 65535, 1114111.

On error, set an exception and return `NULL`.

After creation, the string can be filled by [`PyUnicode_WriteChar()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_WriteChar "PyUnicode_WriteChar")
, [`PyUnicode_CopyCharacters()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_CopyCharacters "PyUnicode_CopyCharacters")
, [`PyUnicode_Fill()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Fill "PyUnicode_Fill")
, [`PyUnicode_WRITE()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_WRITE "PyUnicode_WRITE")
 or similar. Since strings are supposed to be immutable, take care to not “use” the result while it is being modified. In particular, before it’s filled with its final contents, a string:

*   must not be hashed,
    
*   must not be [`converted to UTF-8`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsUTF8AndSize "PyUnicode_AsUTF8AndSize")
    , or another non-“canonical” representation,
    
*   must not have its reference count changed,
    
*   must not be shared with code that might do one of the above.
    

This list is not exhaustive. Avoiding these uses is your responsibility; Python does not always check these requirements.

To avoid accidentally exposing a partially-written string object, prefer using the [`PyUnicodeWriter`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter "PyUnicodeWriter")
 API, or one of the `PyUnicode_From*` functions below.

Added in version 3.3.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_FromKindAndData(int kind, const void \*buffer, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 size)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FromKindAndData "Link to this definition")
  

_Return value: New reference._

Create a new Unicode object with the given _kind_ (possible values are [`PyUnicode_1BYTE_KIND`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_1BYTE_KIND "PyUnicode_1BYTE_KIND")
 etc., as returned by [`PyUnicode_KIND()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_KIND "PyUnicode_KIND")
). The _buffer_ must point to an array of _size_ units of 1, 2 or 4 bytes per character, as given by the kind.

If necessary, the input _buffer_ is copied and transformed into the canonical representation. For example, if the _buffer_ is a UCS4 string ([`PyUnicode_4BYTE_KIND`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_4BYTE_KIND "PyUnicode_4BYTE_KIND")
) and it consists only of codepoints in the UCS1 range, it will be transformed into UCS1 ([`PyUnicode_1BYTE_KIND`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_1BYTE_KIND "PyUnicode_1BYTE_KIND")
).

All characters must be in range \[U+0000; U+10ffff\]. If _kind_ is [`PyUnicode_4BYTE_KIND`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_4BYTE_KIND "PyUnicode_4BYTE_KIND")
 and the string contains invalid characters, the behavior is undefined.

Added in version 3.3.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_FromStringAndSize(const char \*str, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 size)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FromStringAndSize "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Create a Unicode object from the char buffer _str_. The bytes will be interpreted as being UTF-8 encoded. The buffer is copied into the new object. The return value might be a shared object, i.e. modification of the data is not allowed.

This function raises [`SystemError`](https://docs.python.org/3/builtins/exceptions.html#SystemError "SystemError")
 when:

*   _size_ < 0,
    
*   _str_ is `NULL` and _size_ > 0
    

Changed in version 3.12: _str_ == `NULL` with _size_ > 0 is not allowed anymore.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_FromString(const char \*str)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FromString "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Create a Unicode object from a UTF-8 encoded null-terminated char buffer _str_.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_FromFormat(const char \*format, ...)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FromFormat "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Take a C `printf()`\-style _format_ string and a variable number of arguments, calculate the size of the resulting Python Unicode string and return a string with the values formatted into it. The variable arguments must be C types and must correspond exactly to the format characters in the _format_ ASCII-encoded string.

A conversion specifier contains two or more characters and has the following components, which must occur in this order:

1.  The `'%'` character, which marks the start of the specifier.
    
2.  Conversion flags (optional), which affect the result of some conversion types.
    
3.  Minimum field width (optional). If specified as an `'*'` (asterisk), the actual width is given in the next argument, which must be of type int, and the object to convert comes after the minimum field width and optional precision.
    
4.  Precision (optional), given as a `'.'` (dot) followed by the precision. If specified as `'*'` (an asterisk), the actual precision is given in the next argument, which must be of type int, and the value to convert comes after the precision.
    
5.  Length modifier (optional).
    
6.  Conversion type.
    

The conversion flag characters are:

| Flag | Meaning |
| --- | --- |
| `0` | The conversion will be zero padded for numeric values. |
| `-` | The converted value is left adjusted (overrides the `0` flag if both are given). |

The length modifiers for following integer conversions (`d`, `i`, `o`, `u`, `x`, or `X`) specify the type of the argument (int by default):

| Modifier | Types |
| --- | --- |
| `l` | long or unsigned long |
| `ll` | long long or unsigned long long |
| `j` | `intmax_t` or `uintmax_t` |
| `z` | `size_t` or `ssize_t` |
| `t` | `ptrdiff_t` |

The length modifier `l` for following conversions `s` or `V` specify that the type of the argument is const wchar\_t\*.

The conversion specifiers are:

| Conversion Specifier | Type | Comment |
| --- | --- | --- |
| `%` | _n/a_ | The literal `%` character. |
| `d`, `i` | Specified by the length modifier | The decimal representation of a signed C integer. |
| `u` | Specified by the length modifier | The decimal representation of an unsigned C integer. |
| `o` | Specified by the length modifier | The octal representation of an unsigned C integer. |
| `x` | Specified by the length modifier | The hexadecimal representation of an unsigned C integer (lowercase). |
| `X` | Specified by the length modifier | The hexadecimal representation of an unsigned C integer (uppercase). |
| `c` | int | A single character. |
| `s` | const char\* or const wchar\_t\* | A null-terminated C character array. |
| `p` | const void\* | The hex representation of a C pointer. Mostly equivalent to `printf("%p")` except that it is guaranteed to start with the literal `0x` regardless of what the platform’s `printf` yields. |
| `A` | [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br>\* | The result of calling [`ascii()`](https://docs.python.org/3/builtins/functions.html#ascii "ascii")<br>. |
| `U` | [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br>\* | A Unicode object. |
| `V` | [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br>\*, const char\* or const wchar\_t\* | A Unicode object (which may be `NULL`) and a null-terminated C character array as a second parameter (which will be used, if the first parameter is `NULL`). |
| `S` | [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br>\* | The result of calling [`PyObject_Str()`](https://docs.python.org/3/c-api/object.html#c.PyObject_Str "PyObject_Str")<br>. |
| `R` | [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br>\* | The result of calling [`PyObject_Repr()`](https://docs.python.org/3/c-api/object.html#c.PyObject_Repr "PyObject_Repr")<br>. |
| `T` | [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br>\* | Get the fully qualified name of an object type; call [`PyType_GetFullyQualifiedName()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetFullyQualifiedName "PyType_GetFullyQualifiedName")<br>. |
| `#T` | [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br>\* | Similar to `T` format, but use a colon (`:`) as separator between the module name and the qualified name. |
| `N` | [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")<br>\* | Get the fully qualified name of a type; call [`PyType_GetFullyQualifiedName()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetFullyQualifiedName "PyType_GetFullyQualifiedName")<br>. |
| `#N` | [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")<br>\* | Similar to `N` format, but use a colon (`:`) as separator between the module name and the qualified name. |

Note

The width formatter unit is number of characters rather than bytes. The precision formatter unit is number of bytes or `wchar_t` items (if the length modifier `l` is used) for `"%s"` and `"%V"` (if the `PyObject*` argument is `NULL`), and a number of characters for `"%A"`, `"%U"`, `"%S"`, `"%R"` and `"%V"` (if the `PyObject*` argument is not `NULL`).

Note

Unlike to C `printf()` the `0` flag has effect even when a precision is given for integer conversions (`d`, `i`, `u`, `o`, `x`, or `X`).

Changed in version 3.2: Support for `"%lld"` and `"%llu"` added.

Changed in version 3.3: Support for `"%li"`, `"%lli"` and `"%zi"` added.

Changed in version 3.4: Support width and precision formatter for `"%s"`, `"%A"`, `"%U"`, `"%V"`, `"%S"`, `"%R"` added.

Changed in version 3.12: Support for conversion specifiers `o` and `X`. Support for length modifiers `j` and `t`. Length modifiers are now applied to all integer conversions. Length modifier `l` is now applied to conversion specifiers `s` and `V`. Support for variable width and precision `*`. Support for flag `-`.

An unrecognized format character now sets a [`SystemError`](https://docs.python.org/3/builtins/exceptions.html#SystemError "SystemError")
. In previous versions it caused all the rest of the format string to be copied as-is to the result string, and any extra arguments discarded.

Changed in version 3.13: Support for `%T`, `%#T`, `%N` and `%#N` formats added.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_FromFormatV(const char \*format, va\_list vargs)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FromFormatV "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Identical to [`PyUnicode_FromFormat()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FromFormat "PyUnicode_FromFormat")
 except that it takes exactly two arguments.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_FromObject([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FromObject "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Copy an instance of a Unicode subtype to a new true Unicode object if necessary. If _obj_ is already a true Unicode object (not a subtype), return a new [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 to the object.

Objects other than Unicode or its subtypes will cause a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_FromOrdinal(int ordinal)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FromOrdinal "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Create a Unicode Object from the given Unicode code point _ordinal_.

The ordinal must be in `range(0x110000)`. A [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 is raised in the case it is not.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_FromEncodedObject([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj, const char \*encoding, const char \*errors)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FromEncodedObject "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Decode an encoded object _obj_ to a Unicode object.

[`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
, [`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")
 and other [bytes-like objects](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 are decoded according to the given _encoding_ and using the error handling defined by _errors_. Both can be `NULL` to have the interface use the default values (see [Built-in Codecs](https://docs.python.org/3/c-api/unicode.html#builtincodecs)
 for details).

All other objects, including Unicode objects, cause a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 to be set.

The API returns `NULL` if there was an error. The caller is responsible for decref’ing the returned objects.

void PyUnicode\_Append([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*\*p\_left, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*right)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Append "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Append the string _right_ to the end of _p\_left_. _p\_left_ must point to a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 to a Unicode object; `PyUnicode_Append()` releases (”[steals](https://docs.python.org/3/glossary.html#term-steal)
”) this reference.

On error, set _\*p\_left_ to `NULL` and set an exception.

On success, set _\*p\_left_ to a new strong reference to the result.

void PyUnicode\_AppendAndDel([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*\*p\_left, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*right)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AppendAndDel "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

The function is similar to [`PyUnicode_Append()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Append "PyUnicode_Append")
, with the only difference being that it decrements the reference count of _right_ by one.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_BuildEncodingMap([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*string)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_BuildEncodingMap "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return a mapping suitable for decoding a custom single-byte encoding. Given a Unicode string _string_ of up to 256 characters representing an encoding table, returns either a compact internal mapping object or a dictionary mapping character ordinals to byte values. Raises a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 and return `NULL` on invalid input.

Added in version 3.2.

const char \*PyUnicode\_GetDefaultEncoding(void)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_GetDefaultEncoding "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return the name of the default string encoding, `"utf-8"`. See [`sys.getdefaultencoding()`](https://docs.python.org/3/library/sys.html#sys.getdefaultencoding "sys.getdefaultencoding")
.

The returned string does not need to be freed, and is valid until interpreter shutdown.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 PyUnicode\_GetLength([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_GetLength "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.7._

Return the length of the Unicode object, in code points.

On error, set an exception and return `-1`.

**CPython implementation detail:** The length does not count the trailing null character.

Added in version 3.3.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 PyUnicode\_CopyCharacters([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*to, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 to\_start, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*from, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 from\_start, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 how\_many)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_CopyCharacters "Link to this definition")
  

Copy characters from one Unicode object into another. This function performs character conversion when necessary and falls back to `memcpy()` if possible. Returns `-1` and sets an exception on error, otherwise returns the number of copied characters.

The string must not have been “used” yet. See [`PyUnicode_New()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_New "PyUnicode_New")
 for details.

Added in version 3.3.

int PyUnicode\_Resize([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*\*unicode, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 length);[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Resize "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Resize a Unicode object _\*unicode_ to the new _length_ in code points.

Try to resize the string in place (which is usually faster than allocating a new string and copying characters), or create a new string.

_\*unicode_ is modified to point to the new (resized) object and `0` is returned on success. Otherwise, `-1` is returned and an exception is set, and _\*unicode_ is left untouched.

The function doesn’t check string content, the result may not be a string in canonical representation.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 PyUnicode\_Fill([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 start, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 length, [Py\_UCS4](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
 fill\_char)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Fill "Link to this definition")
  

Fill a string with a character: write _fill\_char_ into `unicode[start:start+length]`.

Fail if _fill\_char_ is bigger than the string maximum character, or if the string has more than 1 reference.

The string must not have been “used” yet. See [`PyUnicode_New()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_New "PyUnicode_New")
 for details.

Return the number of written characters, or return `-1` and raise an exception on error.

Added in version 3.3.

int PyUnicode\_WriteChar([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 index, [Py\_UCS4](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
 character)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_WriteChar "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.7._

Write a _character_ to the string _unicode_ at the zero-based _index_. Return `0` on success, `-1` on error with an exception set.

This function checks that _unicode_ is a Unicode object, that the index is not out of bounds, and that the object’s reference count is one. See [`PyUnicode_WRITE()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_WRITE "PyUnicode_WRITE")
 for a version that skips these checks, making them your responsibility.

The string must not have been “used” yet. See [`PyUnicode_New()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_New "PyUnicode_New")
 for details.

Added in version 3.3.

[Py\_UCS4](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
 PyUnicode\_ReadChar([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 index)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_ReadChar "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.7._

Read a character from a string. This function checks that _unicode_ is a Unicode object and the index is not out of bounds, in contrast to [`PyUnicode_READ_CHAR()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_READ_CHAR "PyUnicode_READ_CHAR")
, which performs no error checking.

Return character on success, `-1` on error with an exception set.

**CPython implementation detail:** Do not accept reading the trailing null character at index [`PyUnicode_GetLength()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_GetLength "PyUnicode_GetLength")
.

Added in version 3.3.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_Substring([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 start, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 end)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Substring "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.7._

Return a substring of _unicode_, from character index _start_ (included) to character index _end_ (excluded). Negative indices are not supported. On error, set an exception and return `NULL`.

Added in version 3.3.

[Py\_UCS4](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
 \*PyUnicode\_AsUCS4([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode, [Py\_UCS4](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
 \*buffer, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 buflen, int copy\_null)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsUCS4 "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.7._

Copy the string _unicode_ into a UCS4 buffer, including a null character, if _copy\_null_ is set. Returns `NULL` and sets an exception on error (in particular, a [`SystemError`](https://docs.python.org/3/builtins/exceptions.html#SystemError "SystemError")
 if _buflen_ is smaller than the length of _unicode_). _buffer_ is returned on success.

Added in version 3.3.

[Py\_UCS4](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
 \*PyUnicode\_AsUCS4Copy([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsUCS4Copy "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.7._

Copy the string _unicode_ into a new UCS4 buffer that is allocated using [`PyMem_Malloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_Malloc "PyMem_Malloc")
. If this fails, `NULL` is returned with a [`MemoryError`](https://docs.python.org/3/builtins/exceptions.html#MemoryError "MemoryError")
 set. The returned buffer always has an extra null code point appended.

Added in version 3.3.

### Locale Encoding[¶](https://docs.python.org/3/c-api/unicode.html#locale-encoding "Link to this heading")

The current locale encoding can be used to decode text from the operating system.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_DecodeLocaleAndSize(const char \*str, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 length, const char \*errors)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeLocaleAndSize "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.7._

Decode a string from UTF-8 on Android and VxWorks, or from the current locale encoding on other platforms. The supported error handlers are `"strict"` and `"surrogateescape"` ([**PEP 383**](https://peps.python.org/pep-0383/)
). The decoder uses `"strict"` error handler if _errors_ is `NULL`. _str_ must end with a null character but cannot contain embedded null characters.

Use [`PyUnicode_DecodeFSDefaultAndSize()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeFSDefaultAndSize "PyUnicode_DecodeFSDefaultAndSize")
 to decode a string from the [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler)
.

This function ignores the [Python UTF-8 Mode](https://docs.python.org/3/library/os.html#utf8-mode)
.

See also

The [`Py_DecodeLocale()`](https://docs.python.org/3/c-api/sys.html#c.Py_DecodeLocale "Py_DecodeLocale")
 function.

Added in version 3.3.

Changed in version 3.7: The function now also uses the current locale encoding for the `surrogateescape` error handler, except on Android. Previously, [`Py_DecodeLocale()`](https://docs.python.org/3/c-api/sys.html#c.Py_DecodeLocale "Py_DecodeLocale")
 was used for the `surrogateescape`, and the current locale encoding was used for `strict`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_DecodeLocale(const char \*str, const char \*errors)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeLocale "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.7._

Similar to [`PyUnicode_DecodeLocaleAndSize()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeLocaleAndSize "PyUnicode_DecodeLocaleAndSize")
, but compute the string length using `strlen()`.

Added in version 3.3.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_EncodeLocale([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode, const char \*errors)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_EncodeLocale "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.7._

Encode a Unicode object to UTF-8 on Android and VxWorks, or to the current locale encoding on other platforms. The supported error handlers are `"strict"` and `"surrogateescape"` ([**PEP 383**](https://peps.python.org/pep-0383/)
). The encoder uses `"strict"` error handler if _errors_ is `NULL`. Return a [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 object. _unicode_ cannot contain embedded null characters.

Use [`PyUnicode_EncodeFSDefault()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_EncodeFSDefault "PyUnicode_EncodeFSDefault")
 to encode a string to the [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler)
.

This function ignores the [Python UTF-8 Mode](https://docs.python.org/3/library/os.html#utf8-mode)
.

See also

The [`Py_EncodeLocale()`](https://docs.python.org/3/c-api/sys.html#c.Py_EncodeLocale "Py_EncodeLocale")
 function.

Added in version 3.3.

Changed in version 3.7: The function now also uses the current locale encoding for the `surrogateescape` error handler, except on Android. Previously, [`Py_EncodeLocale()`](https://docs.python.org/3/c-api/sys.html#c.Py_EncodeLocale "Py_EncodeLocale")
 was used for the `surrogateescape`, and the current locale encoding was used for `strict`.

### File System Encoding[¶](https://docs.python.org/3/c-api/unicode.html#file-system-encoding "Link to this heading")

Functions encoding to and decoding from the [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler)
 ([**PEP 383**](https://peps.python.org/pep-0383/)
 and [**PEP 529**](https://peps.python.org/pep-0529/)
).

To encode file names to [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 during argument parsing, the `"O&"` converter should be used, passing `PyUnicode_FSConverter()` as the conversion function:

int PyUnicode\_FSConverter([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj, void \*result)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FSConverter "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

[PyArg\_Parse\* converter](https://docs.python.org/3/c-api/arg.html#arg-parsing)
: encode [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 objects – obtained directly or through the [`os.PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "os.PathLike")
 interface – to [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 using [`PyUnicode_EncodeFSDefault()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_EncodeFSDefault "PyUnicode_EncodeFSDefault")
; `bytes` objects are output as-is. _result_ must be an address of a C variable of type [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\* (or [PyBytesObject](https://docs.python.org/3/c-api/bytes.html#c.PyBytesObject "PyBytesObject")
\*). On success, set the variable to a new [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 to a [bytes object](https://docs.python.org/3/c-api/bytes.html#bytesobjects)
 which must be released when it is no longer used and return a non-zero value ([`Py_CLEANUP_SUPPORTED`](https://docs.python.org/3/c-api/arg.html#c.Py_CLEANUP_SUPPORTED "Py_CLEANUP_SUPPORTED")
). Embedded null bytes are not allowed in the result. On failure, return `0` with an exception set.

If _obj_ is `NULL`, the function releases a strong reference stored in the variable referred by _result_ and returns `1`.

Added in version 3.1.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

To decode file names to [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 during argument parsing, the `"O&"` converter should be used, passing `PyUnicode_FSDecoder()` as the conversion function:

int PyUnicode\_FSDecoder([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj, void \*result)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FSDecoder "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

[PyArg\_Parse\* converter](https://docs.python.org/3/c-api/arg.html#arg-parsing)
: decode [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 objects – obtained either directly or indirectly through the [`os.PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "os.PathLike")
 interface – to [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 using [`PyUnicode_DecodeFSDefaultAndSize()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeFSDefaultAndSize "PyUnicode_DecodeFSDefaultAndSize")
; `str` objects are output as-is. _result_ must be an address of a C variable of type [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\* (or [PyUnicodeObject](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeObject "PyUnicodeObject")
\*). On success, set the variable to a new [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 to a [Unicode object](https://docs.python.org/3/c-api/unicode.html#unicodeobjects)
 which must be released when it is no longer used and return a non-zero value ([`Py_CLEANUP_SUPPORTED`](https://docs.python.org/3/c-api/arg.html#c.Py_CLEANUP_SUPPORTED "Py_CLEANUP_SUPPORTED")
). Embedded null characters are not allowed in the result. On failure, return `0` with an exception set.

If _obj_ is `NULL`, release the strong reference to the object referred to by _result_ and return `1`.

Added in version 3.2.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_DecodeFSDefaultAndSize(const char \*str, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 size)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeFSDefaultAndSize "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Decode a string from the [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler)
.

If you need to decode a string from the current locale encoding, use [`PyUnicode_DecodeLocaleAndSize()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeLocaleAndSize "PyUnicode_DecodeLocaleAndSize")
.

See also

The [`Py_DecodeLocale()`](https://docs.python.org/3/c-api/sys.html#c.Py_DecodeLocale "Py_DecodeLocale")
 function.

Changed in version 3.6: The [filesystem error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler)
 is now used.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_DecodeFSDefault(const char \*str)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeFSDefault "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Decode a null-terminated string from the [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler)
.

If the string length is known, use [`PyUnicode_DecodeFSDefaultAndSize()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeFSDefaultAndSize "PyUnicode_DecodeFSDefaultAndSize")
.

Changed in version 3.6: The [filesystem error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler)
 is now used.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_EncodeFSDefault([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_EncodeFSDefault "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Encode a Unicode object to the [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler)
, and return [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
. Note that the resulting `bytes` object can contain null bytes.

If you need to encode a string to the current locale encoding, use [`PyUnicode_EncodeLocale()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_EncodeLocale "PyUnicode_EncodeLocale")
.

See also

The [`Py_EncodeLocale()`](https://docs.python.org/3/c-api/sys.html#c.Py_EncodeLocale "Py_EncodeLocale")
 function.

Added in version 3.2.

Changed in version 3.6: The [filesystem error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler)
 is now used.

### wchar\_t Support[¶](https://docs.python.org/3/c-api/unicode.html#wchar-t-support "Link to this heading")

`wchar_t` support for platforms which support it:

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_FromWideChar(const wchar\_t \*wstr, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 size)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FromWideChar "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Create a Unicode object from the `wchar_t` buffer _wstr_ of the given _size_. Passing `-1` as the _size_ indicates that the function must itself compute the length, using `wcslen()`. Return `NULL` on failure.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 PyUnicode\_AsWideChar([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode, wchar\_t \*wstr, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 size)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsWideChar "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Copy the Unicode object contents into the `wchar_t` buffer _wstr_. At most _size_ `wchar_t` characters are copied (excluding a possibly trailing null termination character). Return the number of `wchar_t` characters copied or `-1` in case of an error.

When _wstr_ is `NULL`, instead return the _size_ that would be required to store all of _unicode_ including a terminating null.

Note that the resulting wchar\_t\* string may or may not be null-terminated. It is the responsibility of the caller to make sure that the wchar\_t\* string is null-terminated in case this is required by the application. Also, note that the wchar\_t\* string might contain null characters, which would cause the string to be truncated when used with most C functions.

wchar\_t \*PyUnicode\_AsWideCharString([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 \*size)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsWideCharString "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.7._

Convert the Unicode object to a wide character string. The output string always ends with a null character. If _size_ is not `NULL`, write the number of wide characters (excluding the trailing null termination character) into _\*size_. Note that the resulting `wchar_t` string might contain null characters, which would cause the string to be truncated when used with most C functions. If _size_ is `NULL` and the wchar\_t\* string contains null characters a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 is raised.

Returns a buffer allocated by [`PyMem_New`](https://docs.python.org/3/c-api/memory.html#c.PyMem_New "PyMem_New")
 (use [`PyMem_Free()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_Free "PyMem_Free")
 to free it) on success. On error, returns `NULL` and _\*size_ is undefined. Raises a [`MemoryError`](https://docs.python.org/3/builtins/exceptions.html#MemoryError "MemoryError")
 if memory allocation is failed.

Added in version 3.2.

Changed in version 3.7: Raises a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 if _size_ is `NULL` and the wchar\_t\* string contains null characters.

Built-in Codecs[¶](https://docs.python.org/3/c-api/unicode.html#built-in-codecs "Link to this heading")

--------------------------------------------------------------------------------------------------------

Python provides a set of built-in codecs which are written in C for speed. All of these codecs are directly usable via the following functions.

Many of the following APIs take two arguments encoding and errors, and they have the same semantics as the ones of the built-in [`str()`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 string object constructor.

Setting encoding to `NULL` causes the default encoding to be used which is UTF-8. The file system calls should use [`PyUnicode_FSConverter()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FSConverter "PyUnicode_FSConverter")
 for encoding file names. This uses the [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler)
 internally.

Error handling is set by errors which may also be set to `NULL` meaning to use the default handling defined for the codec. Default error handling for all built-in codecs is “strict” ([`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 is raised).

The codecs all use a similar interface. Only deviations from the following generic ones are documented for simplicity.

### Generic Codecs[¶](https://docs.python.org/3/c-api/unicode.html#generic-codecs "Link to this heading")

The following macro is provided:

Py\_UNICODE\_REPLACEMENT\_CHARACTER[¶](https://docs.python.org/3/c-api/unicode.html#c.Py_UNICODE_REPLACEMENT_CHARACTER "Link to this definition")
  

The Unicode code point `U+FFFD` (replacement character).

This Unicode character is used as the replacement character during decoding if the _errors_ argument is set to “replace”.

These are the generic codec APIs:

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_Decode(const char \*str, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 size, const char \*encoding, const char \*errors)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Decode "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Create a Unicode object by decoding _size_ bytes of the encoded string _str_. _encoding_ and _errors_ have the same meaning as the parameters of the same name in the [`str()`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 built-in function. The codec to be used is looked up using the Python codec registry. Return `NULL` if an exception was raised by the codec.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_AsEncodedString([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode, const char \*encoding, const char \*errors)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsEncodedString "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Encode a Unicode object and return the result as Python bytes object. _encoding_ and _errors_ have the same meaning as the parameters of the same name in the Unicode [`encode()`](https://docs.python.org/3/builtins/stdtypes.html#str.encode "str.encode")
 method. The codec to be used is looked up using the Python codec registry. Return `NULL` if an exception was raised by the codec.

### UTF-8 Codecs[¶](https://docs.python.org/3/c-api/unicode.html#utf-8-codecs "Link to this heading")

These are the UTF-8 codec APIs:

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_DecodeUTF8(const char \*str, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 size, const char \*errors)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeUTF8 "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Create a Unicode object by decoding _size_ bytes of the UTF-8 encoded string _str_. Return `NULL` if an exception was raised by the codec.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_DecodeUTF8Stateful(const char \*str, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 size, const char \*errors, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 \*consumed)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeUTF8Stateful "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

If _consumed_ is `NULL`, behave like [`PyUnicode_DecodeUTF8()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeUTF8 "PyUnicode_DecodeUTF8")
. If _consumed_ is not `NULL`, trailing incomplete UTF-8 byte sequences will not be treated as an error. Those bytes will not be decoded and the number of bytes that have been decoded will be stored in _consumed_.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_AsUTF8String([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsUTF8String "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Encode a Unicode object using UTF-8 and return the result as Python bytes object. Error handling is “strict”. Return `NULL` if an exception was raised by the codec.

The function fails if the string contains surrogate code points (`U+D800` - `U+DFFF`).

const char \*PyUnicode\_AsUTF8AndSize([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 \*size)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsUTF8AndSize "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.10._

Return a pointer to the UTF-8 encoding of the Unicode object, and store the size of the encoded representation (in bytes) in _size_. The _size_ argument can be `NULL`; in this case no size will be stored. The returned buffer always has an extra null byte appended (not included in _size_), regardless of whether there are any other null code points.

On error, set an exception, set _size_ to `-1` (if it’s not NULL) and return `NULL`.

The function fails if the string contains surrogate code points (`U+D800` - `U+DFFF`).

This caches the UTF-8 representation of the string in the Unicode object, and subsequent calls will return a pointer to the same buffer. The caller is not responsible for deallocating the buffer. The buffer is deallocated and pointers to it become invalid when the Unicode object is garbage collected.

Added in version 3.3.

Changed in version 3.7: The return type is now `const char *` rather than `char *`.

Changed in version 3.10: This function is a part of the [limited API](https://docs.python.org/3/c-api/stable.html#limited-c-api)
.

const char \*PyUnicode\_AsUTF8([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsUTF8 "Link to this definition")
  

As [`PyUnicode_AsUTF8AndSize()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsUTF8AndSize "PyUnicode_AsUTF8AndSize")
, but does not store the size.

Warning

This function does not have any special behavior for [null characters](https://en.wikipedia.org/wiki/Null_character)
 embedded within _unicode_. As a result, strings containing null characters will remain in the returned string, which some C functions might interpret as the end of the string, leading to truncation. If truncation is an issue, it is recommended to use [`PyUnicode_AsUTF8AndSize()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsUTF8AndSize "PyUnicode_AsUTF8AndSize")
 instead.

Added in version 3.3.

Changed in version 3.7: The return type is now `const char *` rather than `char *`.

### UTF-32 Codecs[¶](https://docs.python.org/3/c-api/unicode.html#utf-32-codecs "Link to this heading")

These are the UTF-32 codec APIs:

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_DecodeUTF32(const char \*str, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 size, const char \*errors, int \*byteorder)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeUTF32 "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Decode _size_ bytes from a UTF-32 encoded buffer string and return the corresponding Unicode object. _errors_ (if non-`NULL`) defines the error handling. It defaults to “strict”.

If _byteorder_ is non-`NULL`, the decoder starts decoding using the given byte order:

\*byteorder \== \-1: little endian
\*byteorder \== 0:  native order
\*byteorder \== 1:  big endian

If `*byteorder` is zero, and the first four bytes of the input data are a byte order mark (BOM), the decoder switches to this byte order and the BOM is not copied into the resulting Unicode string. If `*byteorder` is `-1` or `1`, any byte order mark is copied to the output.

After completion, _\*byteorder_ is set to the current byte order at the end of input data.

If _byteorder_ is `NULL`, the codec starts in native order mode.

Return `NULL` if an exception was raised by the codec.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_DecodeUTF32Stateful(const char \*str, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 size, const char \*errors, int \*byteorder, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 \*consumed)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeUTF32Stateful "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

If _consumed_ is `NULL`, behave like [`PyUnicode_DecodeUTF32()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeUTF32 "PyUnicode_DecodeUTF32")
. If _consumed_ is not `NULL`, [`PyUnicode_DecodeUTF32Stateful()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeUTF32Stateful "PyUnicode_DecodeUTF32Stateful")
 will not treat trailing incomplete UTF-32 byte sequences (such as a number of bytes not divisible by four) as an error. Those bytes will not be decoded and the number of bytes that have been decoded will be stored in _consumed_.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_AsUTF32String([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsUTF32String "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return a Python byte string using the UTF-32 encoding in native byte order. The string always starts with a BOM mark. Error handling is “strict”. Return `NULL` if an exception was raised by the codec.

### UTF-16 Codecs[¶](https://docs.python.org/3/c-api/unicode.html#utf-16-codecs "Link to this heading")

These are the UTF-16 codec APIs:

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_DecodeUTF16(const char \*str, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 size, const char \*errors, int \*byteorder)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeUTF16 "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Decode _size_ bytes from a UTF-16 encoded buffer string and return the corresponding Unicode object. _errors_ (if non-`NULL`) defines the error handling. It defaults to “strict”.

If _byteorder_ is non-`NULL`, the decoder starts decoding using the given byte order:

\*byteorder \== \-1: little endian
\*byteorder \== 0:  native order
\*byteorder \== 1:  big endian

If `*byteorder` is zero, and the first two bytes of the input data are a byte order mark (BOM), the decoder switches to this byte order and the BOM is not copied into the resulting Unicode string. If `*byteorder` is `-1` or `1`, any byte order mark is copied to the output (where it will result in either a `\ufeff` or a `\ufffe` character).

After completion, `*byteorder` is set to the current byte order at the end of input data.

If _byteorder_ is `NULL`, the codec starts in native order mode.

Return `NULL` if an exception was raised by the codec.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_DecodeUTF16Stateful(const char \*str, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 size, const char \*errors, int \*byteorder, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 \*consumed)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeUTF16Stateful "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

If _consumed_ is `NULL`, behave like [`PyUnicode_DecodeUTF16()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeUTF16 "PyUnicode_DecodeUTF16")
. If _consumed_ is not `NULL`, [`PyUnicode_DecodeUTF16Stateful()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeUTF16Stateful "PyUnicode_DecodeUTF16Stateful")
 will not treat trailing incomplete UTF-16 byte sequences (such as an odd number of bytes or a split surrogate pair) as an error. Those bytes will not be decoded and the number of bytes that have been decoded will be stored in _consumed_.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_AsUTF16String([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsUTF16String "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return a Python byte string using the UTF-16 encoding in native byte order. The string always starts with a BOM mark. Error handling is “strict”. Return `NULL` if an exception was raised by the codec.

### UTF-7 Codecs[¶](https://docs.python.org/3/c-api/unicode.html#utf-7-codecs "Link to this heading")

These are the UTF-7 codec APIs:

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_DecodeUTF7(const char \*str, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 size, const char \*errors)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeUTF7 "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Create a Unicode object by decoding _size_ bytes of the UTF-7 encoded string _str_. Return `NULL` if an exception was raised by the codec.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_DecodeUTF7Stateful(const char \*str, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 size, const char \*errors, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 \*consumed)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeUTF7Stateful "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

If _consumed_ is `NULL`, behave like [`PyUnicode_DecodeUTF7()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeUTF7 "PyUnicode_DecodeUTF7")
. If _consumed_ is not `NULL`, trailing incomplete UTF-7 base-64 sections will not be treated as an error. Those bytes will not be decoded and the number of bytes that have been decoded will be stored in _consumed_.

### Unicode-Escape Codecs[¶](https://docs.python.org/3/c-api/unicode.html#unicode-escape-codecs "Link to this heading")

These are the “Unicode Escape” codec APIs:

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_DecodeUnicodeEscape(const char \*str, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 size, const char \*errors)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeUnicodeEscape "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Create a Unicode object by decoding _size_ bytes of the Unicode-Escape encoded string _str_. Return `NULL` if an exception was raised by the codec.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_AsUnicodeEscapeString([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsUnicodeEscapeString "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Encode a Unicode object using Unicode-Escape and return the result as a bytes object. Error handling is “strict”. Return `NULL` if an exception was raised by the codec.

### Raw-Unicode-Escape Codecs[¶](https://docs.python.org/3/c-api/unicode.html#raw-unicode-escape-codecs "Link to this heading")

These are the “Raw Unicode Escape” codec APIs:

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_DecodeRawUnicodeEscape(const char \*str, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 size, const char \*errors)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeRawUnicodeEscape "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Create a Unicode object by decoding _size_ bytes of the Raw-Unicode-Escape encoded string _str_. Return `NULL` if an exception was raised by the codec.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_AsRawUnicodeEscapeString([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsRawUnicodeEscapeString "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Encode a Unicode object using Raw-Unicode-Escape and return the result as a bytes object. Error handling is “strict”. Return `NULL` if an exception was raised by the codec.

### Latin-1 Codecs[¶](https://docs.python.org/3/c-api/unicode.html#latin-1-codecs "Link to this heading")

These are the Latin-1 codec APIs: Latin-1 corresponds to the first 256 Unicode ordinals and only these are accepted by the codecs during encoding.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_DecodeLatin1(const char \*str, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 size, const char \*errors)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeLatin1 "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Create a Unicode object by decoding _size_ bytes of the Latin-1 encoded string _str_. Return `NULL` if an exception was raised by the codec.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_AsLatin1String([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsLatin1String "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Encode a Unicode object using Latin-1 and return the result as Python bytes object. Error handling is “strict”. Return `NULL` if an exception was raised by the codec.

### ASCII Codecs[¶](https://docs.python.org/3/c-api/unicode.html#ascii-codecs "Link to this heading")

These are the ASCII codec APIs. Only 7-bit ASCII data is accepted. All other codes generate errors.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_DecodeASCII(const char \*str, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 size, const char \*errors)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeASCII "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Create a Unicode object by decoding _size_ bytes of the ASCII encoded string _str_. Return `NULL` if an exception was raised by the codec.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_AsASCIIString([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsASCIIString "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Encode a Unicode object using ASCII and return the result as Python bytes object. Error handling is “strict”. Return `NULL` if an exception was raised by the codec.

### Character Map Codecs[¶](https://docs.python.org/3/c-api/unicode.html#character-map-codecs "Link to this heading")

This codec is special in that it can be used to implement many different codecs (and this is in fact what was done to obtain most of the standard codecs included in the `encodings` package). The codec uses mappings to encode and decode characters. The mapping objects provided must support the [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__")
 mapping interface; dictionaries and sequences work well.

These are the mapping codec APIs:

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_DecodeCharmap(const char \*str, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 length, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*mapping, const char \*errors)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeCharmap "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Create a Unicode object by decoding _size_ bytes of the encoded string _str_ using the given _mapping_ object. Return `NULL` if an exception was raised by the codec.

If _mapping_ is `NULL`, Latin-1 decoding will be applied. Else _mapping_ must map bytes ordinals (integers in the range from 0 to 255) to Unicode strings, integers (which are then interpreted as Unicode ordinals) or `None`. Unmapped data bytes – ones which cause a [`LookupError`](https://docs.python.org/3/builtins/exceptions.html#LookupError "LookupError")
, as well as ones which get mapped to `None`, `0xFFFE` or `'\ufffe'`, are treated as undefined mappings and cause an error.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_AsCharmapString([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*mapping)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsCharmapString "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Encode a Unicode object using the given _mapping_ object and return the result as a bytes object. Error handling is “strict”. Return `NULL` if an exception was raised by the codec.

The _mapping_ object must map Unicode ordinal integers to bytes objects, integers in the range from 0 to 255 or `None`. Unmapped character ordinals (ones which cause a [`LookupError`](https://docs.python.org/3/builtins/exceptions.html#LookupError "LookupError")
) as well as mapped to `None` are treated as “undefined mapping” and cause an error.

The following codec API is special in that maps Unicode to Unicode.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_Translate([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*table, const char \*errors)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Translate "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Translate a string by applying a character mapping table to it and return the resulting Unicode object. Return `NULL` if an exception was raised by the codec.

The mapping table must map Unicode ordinal integers to Unicode ordinal integers or `None` (causing deletion of the character).

Mapping tables need only provide the [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__")
 interface; dictionaries and sequences work well. Unmapped character ordinals (ones which cause a [`LookupError`](https://docs.python.org/3/builtins/exceptions.html#LookupError "LookupError")
) are left untouched and are copied as-is.

_errors_ has the usual meaning for codecs. It may be `NULL` which indicates to use the default error handling.

### MBCS codecs for Windows[¶](https://docs.python.org/3/c-api/unicode.html#mbcs-codecs-for-windows "Link to this heading")

These are the MBCS codec APIs. They are currently only available on Windows and use the Win32 MBCS converters to implement the conversions. Note that MBCS (or DBCS) is a class of encodings, not just one. The target encoding is defined by the user settings on the machine running the codec.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_DecodeMBCS(const char \*str, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 size, const char \*errors)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeMBCS "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 on Windows since version 3.7._

Create a Unicode object by decoding _size_ bytes of the MBCS encoded string _str_. Return `NULL` if an exception was raised by the codec.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_DecodeMBCSStateful(const char \*str, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 size, const char \*errors, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 \*consumed)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeMBCSStateful "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 on Windows since version 3.7._

If _consumed_ is `NULL`, behave like [`PyUnicode_DecodeMBCS()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeMBCS "PyUnicode_DecodeMBCS")
. If _consumed_ is not `NULL`, [`PyUnicode_DecodeMBCSStateful()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeMBCSStateful "PyUnicode_DecodeMBCSStateful")
 will not decode trailing lead byte and the number of bytes that have been decoded will be stored in _consumed_.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_DecodeCodePageStateful(int code\_page, const char \*str, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 size, const char \*errors, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 \*consumed)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeCodePageStateful "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 on Windows since version 3.7._

Similar to [`PyUnicode_DecodeMBCSStateful()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeMBCSStateful "PyUnicode_DecodeMBCSStateful")
, except uses the code page specified by _code\_page_.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_AsMBCSString([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsMBCSString "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 on Windows since version 3.7._

Encode a Unicode object using MBCS and return the result as Python bytes object. Error handling is “strict”. Return `NULL` if an exception was raised by the codec.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_EncodeCodePage(int code\_page, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode, const char \*errors)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_EncodeCodePage "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 on Windows since version 3.7._

Encode the Unicode object using the specified code page and return a Python bytes object. Return `NULL` if an exception was raised by the codec. Use `CP_ACP` code page to get the MBCS encoder.

Added in version 3.3.

Methods and Slot Functions[¶](https://docs.python.org/3/c-api/unicode.html#methods-and-slot-functions "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

The following APIs are capable of handling Unicode objects and strings on input (we refer to them as strings in the descriptions) and return Unicode objects or integers as appropriate.

They all return `NULL` or `-1` if an exception occurs.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_Concat([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*left, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*right)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Concat "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Concat two strings giving a new Unicode string.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_Split([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*sep, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 maxsplit)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Split "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Split a string giving a list of Unicode strings. If _sep_ is `NULL`, splitting will be done at all whitespace substrings. Otherwise, splits occur at the given separator. At most _maxsplit_ splits will be done. If negative, no limit is set. Separators are not included in the resulting list.

On error, return `NULL` with an exception set.

Equivalent to [`str.split()`](https://docs.python.org/3/builtins/stdtypes.html#str.split "str.split")
.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_RSplit([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*sep, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 maxsplit)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_RSplit "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Similar to [`PyUnicode_Split()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Split "PyUnicode_Split")
, but splitting will be done beginning at the end of the string.

On error, return `NULL` with an exception set.

Equivalent to [`str.rsplit()`](https://docs.python.org/3/builtins/stdtypes.html#str.rsplit "str.rsplit")
.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_Splitlines([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode, int keepends)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Splitlines "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Split a Unicode string at line breaks, returning a list of Unicode strings. CRLF is considered to be one line break. If _keepends_ is `0`, the Line break characters are not included in the resulting strings.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_Partition([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*sep)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Partition "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Split a Unicode string at the first occurrence of _sep_, and return a 3-tuple containing the part before the separator, the separator itself, and the part after the separator. If the separator is not found, return a 3-tuple containing the string itself, followed by two empty strings.

_sep_ must not be empty.

On error, return `NULL` with an exception set.

Equivalent to [`str.partition()`](https://docs.python.org/3/builtins/stdtypes.html#str.partition "str.partition")
.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_RPartition([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*sep)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_RPartition "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Similar to [`PyUnicode_Partition()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Partition "PyUnicode_Partition")
, but split a Unicode string at the last occurrence of _sep_. If the separator is not found, return a 3-tuple containing two empty strings, followed by the string itself.

_sep_ must not be empty.

On error, return `NULL` with an exception set.

Equivalent to [`str.rpartition()`](https://docs.python.org/3/builtins/stdtypes.html#str.rpartition "str.rpartition")
.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_Join([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*separator, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*seq)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Join "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Join a sequence of strings using the given _separator_ and return the resulting Unicode string.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 PyUnicode\_Tailmatch([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*substr, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 start, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 end, int direction)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Tailmatch "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return `1` if _substr_ matches `unicode[start:end]` at the given tail end (_direction_ == `-1` means to do a prefix match, _direction_ == `1` a suffix match), `0` otherwise. Return `-1` if an error occurred.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 PyUnicode\_Find([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*substr, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 start, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 end, int direction)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Find "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return the first position of _substr_ in `unicode[start:end]` using the given _direction_ (_direction_ == `1` means to do a forward search, _direction_ == `-1` a backward search). The return value is the index of the first match; a value of `-1` indicates that no match was found, and `-2` indicates that an error occurred and an exception has been set.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 PyUnicode\_FindChar([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode, [Py\_UCS4](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
 ch, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 start, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 end, int direction)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FindChar "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.7._

Return the first position of the character _ch_ in `unicode[start:end]` using the given _direction_ (_direction_ == `1` means to do a forward search, _direction_ == `-1` a backward search). The return value is the index of the first match; a value of `-1` indicates that no match was found, and `-2` indicates that an error occurred and an exception has been set.

Added in version 3.3.

Changed in version 3.7: _start_ and _end_ are now adjusted to behave like `unicode[start:end]`.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 PyUnicode\_Count([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*substr, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 start, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 end)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Count "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return the number of non-overlapping occurrences of _substr_ in `unicode[start:end]`. Return `-1` if an error occurred.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_Replace([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*substr, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*replstr, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 maxcount)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Replace "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Replace at most _maxcount_ occurrences of _substr_ in _unicode_ with _replstr_ and return the resulting Unicode object. _maxcount_ == `-1` means replace all occurrences.

int PyUnicode\_Compare([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*left, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*right)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Compare "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Compare two strings and return `-1`, `0`, `1` for less than, equal, and greater than, respectively.

This function returns `-1` upon failure, so one should call [`PyErr_Occurred()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Occurred "PyErr_Occurred")
 to check for errors.

See also

The [`PyUnicode_Equal()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Equal "PyUnicode_Equal")
 function.

int PyUnicode\_Equal([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*a, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*b)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Equal "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.14._

Test if two strings are equal:

*   Return `1` if _a_ is equal to _b_.
    
*   Return `0` if _a_ is not equal to _b_.
    
*   Set a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
     exception and return `-1` if _a_ or _b_ is not a [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
     object.
    

The function always succeeds if _a_ and _b_ are [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 objects.

The function works for [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 subclasses, but does not honor custom `__eq__()` method.

See also

The [`PyUnicode_Compare()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Compare "PyUnicode_Compare")
 function.

Added in version 3.14.

int PyUnicode\_EqualToUTF8AndSize([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode, const char \*string, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 size)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_EqualToUTF8AndSize "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.13._

Compare a Unicode object with a char buffer which is interpreted as being UTF-8 or ASCII encoded and return true (`1`) if they are equal, or false (`0`) otherwise. If the Unicode object contains surrogate code points (`U+D800` - `U+DFFF`) or the C string is not valid UTF-8, false (`0`) is returned.

This function does not raise exceptions.

Added in version 3.13.

int PyUnicode\_EqualToUTF8([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode, const char \*string)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_EqualToUTF8 "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.13._

Similar to [`PyUnicode_EqualToUTF8AndSize()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_EqualToUTF8AndSize "PyUnicode_EqualToUTF8AndSize")
, but compute _string_ length using `strlen()`. If the Unicode object contains null characters, false (`0`) is returned.

Added in version 3.13.

int PyUnicode\_CompareWithASCIIString([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode, const char \*string)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_CompareWithASCIIString "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Compare a Unicode object, _unicode_, with _string_ and return `-1`, `0`, `1` for less than, equal, and greater than, respectively. It is best to pass only ASCII-encoded strings, but the function interprets the input string as ISO-8859-1 if it contains non-ASCII characters.

This function does not raise exceptions.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_RichCompare([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*left, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*right, int op)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_RichCompare "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Rich compare two Unicode strings and return one of the following:

*   `NULL` in case an exception was raised
    
*   [`Py_True`](https://docs.python.org/3/c-api/bool.html#c.Py_True "Py_True")
     or [`Py_False`](https://docs.python.org/3/c-api/bool.html#c.Py_False "Py_False")
     for successful comparisons
    
*   [`Py_NotImplemented`](https://docs.python.org/3/c-api/object.html#c.Py_NotImplemented "Py_NotImplemented")
     in case the type combination is unknown
    

Possible values for _op_ are [`Py_GT`](https://docs.python.org/3/c-api/typeobj.html#c.Py_GT "Py_GT")
, [`Py_GE`](https://docs.python.org/3/c-api/typeobj.html#c.Py_GE "Py_GE")
, [`Py_EQ`](https://docs.python.org/3/c-api/typeobj.html#c.Py_EQ "Py_EQ")
, [`Py_NE`](https://docs.python.org/3/c-api/typeobj.html#c.Py_NE "Py_NE")
, [`Py_LT`](https://docs.python.org/3/c-api/typeobj.html#c.Py_LT "Py_LT")
, and [`Py_LE`](https://docs.python.org/3/c-api/typeobj.html#c.Py_LE "Py_LE")
.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_Format([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*format, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*args)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Format "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return a new string object from _format_ and _args_; this is analogous to `format % args`.

int PyUnicode\_Contains([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*substr)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Contains "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Check whether _substr_ is contained in _unicode_ and return true or false accordingly.

_substr_ has to coerce to a one element Unicode string. `-1` is returned if there was an error.

void PyUnicode\_InternInPlace([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*\*p\_unicode)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_InternInPlace "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Intern the argument \*[p\_unicode](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_InternInPlace "p_unicode")
 in place. The argument must be the address of a pointer variable pointing to a Python Unicode string object. If there is an existing interned string that is the same as \*p\_unicode, it sets \*p\_unicode to it (releasing the reference to the old string object and creating a new [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 to the interned string object), otherwise it leaves \*p\_unicode alone and interns it.

(Clarification: even though there is a lot of talk about references, think of this function as reference-neutral. You must own the object you pass in; after the call you no longer own the passed-in reference, but you newly own the result.)

This function never raises an exception. On error, it leaves its argument unchanged without interning it.

Instances of subclasses of [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 may not be interned, that is, [PyUnicode\_CheckExact](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_CheckExact "PyUnicode_CheckExact")
(\*[p\_unicode](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_InternInPlace "p_unicode")
) must be true. If it is not, then – as with any other error – the argument is left unchanged.

Note that interned strings are not “immortal”. You must keep a reference to the result to benefit from interning.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicode\_InternFromString(const char \*str)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_InternFromString "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

A combination of [`PyUnicode_FromString()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FromString "PyUnicode_FromString")
 and [`PyUnicode_InternInPlace()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_InternInPlace "PyUnicode_InternInPlace")
, meant for statically allocated strings.

Return a new (“owned”) reference to either a new Unicode string object that has been interned, or an earlier interned string object with the same value.

Python may keep a reference to the result, or make it [immortal](https://docs.python.org/3/glossary.html#term-immortal)
, preventing it from being garbage-collected promptly. For interning an unbounded number of different strings, such as ones coming from user input, prefer calling [`PyUnicode_FromString()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FromString "PyUnicode_FromString")
 and [`PyUnicode_InternInPlace()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_InternInPlace "PyUnicode_InternInPlace")
 directly.

unsigned int PyUnicode\_CHECK\_INTERNED([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*str)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_CHECK_INTERNED "Link to this definition")
  

Return a non-zero value if _str_ is interned, zero if not. The _str_ argument must be a string; this is not checked. This function always succeeds.

**CPython implementation detail:** A non-zero return value may carry additional information about _how_ the string is interned. The meaning of such non-zero values, as well as each specific string’s intern-related details, may change between CPython versions.

PyUnicodeWriter[¶](https://docs.python.org/3/c-api/unicode.html#pyunicodewriter "Link to this heading")

--------------------------------------------------------------------------------------------------------

The [`PyUnicodeWriter`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter "PyUnicodeWriter")
 API can be used to create a Python [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 object.

Added in version 3.14.

type PyUnicodeWriter[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter "Link to this definition")
  

A Unicode writer instance.

The instance must be destroyed by [`PyUnicodeWriter_Finish()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter_Finish "PyUnicodeWriter_Finish")
 on success, or [`PyUnicodeWriter_Discard()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter_Discard "PyUnicodeWriter_Discard")
 on error.

The API is **not thread safe**. To share a writer with multiple threads, a critical section or a lock is needed.

[PyUnicodeWriter](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter "PyUnicodeWriter")
 \*PyUnicodeWriter\_Create([Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 length)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter_Create "Link to this definition")
  

Create a Unicode writer instance.

_length_ must be greater than or equal to `0`.

If _length_ is greater than `0`, preallocate an internal buffer of _length_ characters.

Set an exception and return `NULL` on error.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicodeWriter\_Finish([PyUnicodeWriter](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter "PyUnicodeWriter")
 \*writer)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter_Finish "Link to this definition")
  

Return the final Python [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 object and destroy the writer instance.

Set an exception and return `NULL` on error.

The writer instance is invalid after this call.

void PyUnicodeWriter\_Discard([PyUnicodeWriter](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter "PyUnicodeWriter")
 \*writer)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter_Discard "Link to this definition")
  

Discard the internal Unicode buffer and destroy the writer instance.

If _writer_ is `NULL`, no operation is performed.

The writer instance is invalid after this call.

int PyUnicodeWriter\_WriteChar([PyUnicodeWriter](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter "PyUnicodeWriter")
 \*writer, [Py\_UCS4](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
 ch)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter_WriteChar "Link to this definition")
  

Write the single Unicode character _ch_ into _writer_.

On success, return `0`. On error, set an exception, leave the writer unchanged, and return `-1`.

int PyUnicodeWriter\_WriteUTF8([PyUnicodeWriter](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter "PyUnicodeWriter")
 \*writer, const char \*str, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 size)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter_WriteUTF8 "Link to this definition")
  

Decode the string _str_ from UTF-8 in strict mode and write the output into _writer_.

_size_ is the string length in bytes. If _size_ is equal to `-1`, call `strlen(str)` to get the string length.

On success, return `0`. On error, set an exception, leave the writer unchanged, and return `-1`.

See also [`PyUnicodeWriter_DecodeUTF8Stateful()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter_DecodeUTF8Stateful "PyUnicodeWriter_DecodeUTF8Stateful")
.

int PyUnicodeWriter\_WriteASCII([PyUnicodeWriter](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter "PyUnicodeWriter")
 \*writer, const char \*str, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 size)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter_WriteASCII "Link to this definition")
  

Write the ASCII string _str_ into _writer_.

_size_ is the string length in bytes. If _size_ is equal to `-1`, call `strlen(str)` to get the string length.

_str_ must only contain ASCII characters. The behavior is undefined if _str_ contains non-ASCII characters.

On success, return `0`. On error, set an exception, leave the writer unchanged, and return `-1`.

int PyUnicodeWriter\_WriteWideChar([PyUnicodeWriter](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter "PyUnicodeWriter")
 \*writer, const wchar\_t \*str, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 size)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter_WriteWideChar "Link to this definition")
  

Write the wide string _str_ into _writer_.

_size_ is a number of wide characters. If _size_ is equal to `-1`, call `wcslen(str)` to get the string length.

On success, return `0`. On error, set an exception, leave the writer unchanged, and return `-1`.

int PyUnicodeWriter\_WriteUCS4([PyUnicodeWriter](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter "PyUnicodeWriter")
 \*writer, const [Py\_UCS4](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
 \*str, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 size)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter_WriteUCS4 "Link to this definition")
  

Write the UCS4 string _str_ into _writer_.

_size_ is a number of UCS4 characters.

All characters must be in range \[U+0000; U+10ffff\]. If the string contains invalid characters, the behavior is undefined.

On success, return `0`. On error, set an exception, leave the writer unchanged, and return `-1`.

int PyUnicodeWriter\_WriteStr([PyUnicodeWriter](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter "PyUnicodeWriter")
 \*writer, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter_WriteStr "Link to this definition")
  

Call [`PyObject_Str()`](https://docs.python.org/3/c-api/object.html#c.PyObject_Str "PyObject_Str")
 on _obj_ and write the output into _writer_.

On success, return `0`. On error, set an exception, leave the writer unchanged, and return `-1`.

To write a [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 subclass which overrides the [`__str__()`](https://docs.python.org/3/reference/datamodel.html#object.__str__ "object.__str__")
 method, [`PyUnicode_FromObject()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FromObject "PyUnicode_FromObject")
 can be used to get the original string.

int PyUnicodeWriter\_WriteRepr([PyUnicodeWriter](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter "PyUnicodeWriter")
 \*writer, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter_WriteRepr "Link to this definition")
  

Call [`PyObject_Repr()`](https://docs.python.org/3/c-api/object.html#c.PyObject_Repr "PyObject_Repr")
 on _obj_ and write the output into _writer_.

If _obj_ is `NULL`, write the string `"<NULL>"` into _writer_.

On success, return `0`. On error, set an exception, leave the writer unchanged, and return `-1`.

Changed in version 3.14.4: Added support for `NULL`.

int PyUnicodeWriter\_WriteSubstring([PyUnicodeWriter](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter "PyUnicodeWriter")
 \*writer, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*str, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 start, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 end)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter_WriteSubstring "Link to this definition")
  

Write the substring `str[start:end]` into _writer_.

_str_ must be Python [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 object. _start_ must be greater than or equal to 0, and less than or equal to _end_. _end_ must be less than or equal to _str_ length.

On success, return `0`. On error, set an exception, leave the writer unchanged, and return `-1`.

int PyUnicodeWriter\_Format([PyUnicodeWriter](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter "PyUnicodeWriter")
 \*writer, const char \*format, ...)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter_Format "Link to this definition")
  

Similar to [`PyUnicode_FromFormat()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FromFormat "PyUnicode_FromFormat")
, but write the output directly into _writer_.

On success, return `0`. On error, set an exception, leave the writer unchanged, and return `-1`.

int PyUnicodeWriter\_DecodeUTF8Stateful([PyUnicodeWriter](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter "PyUnicodeWriter")
 \*writer, const char \*string, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 length, const char \*errors, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 \*consumed)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter_DecodeUTF8Stateful "Link to this definition")
  

Decode the string _str_ from UTF-8 with _errors_ error handler and write the output into _writer_.

_size_ is the string length in bytes. If _size_ is equal to `-1`, call `strlen(str)` to get the string length.

_errors_ is an [error handler](https://docs.python.org/3/library/codecs.html#error-handlers)
 name, such as `"replace"`. If _errors_ is `NULL`, use the strict error handler.

If _consumed_ is not `NULL`, set _\*consumed_ to the number of decoded bytes on success. If _consumed_ is `NULL`, treat trailing incomplete UTF-8 byte sequences as an error.

On success, return `0`. On error, set an exception, leave the writer unchanged, and return `-1`.

See also [`PyUnicodeWriter_WriteUTF8()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter_WriteUTF8 "PyUnicodeWriter_WriteUTF8")
.

Deprecated API[¶](https://docs.python.org/3/c-api/unicode.html#deprecated-api "Link to this heading")

------------------------------------------------------------------------------------------------------

The following API is deprecated.

type Py\_UNICODE[¶](https://docs.python.org/3/c-api/unicode.html#c.Py_UNICODE "Link to this definition")
  

This is a typedef of `wchar_t`, which is a 16-bit type or 32-bit type depending on the platform. Please use `wchar_t` directly instead.

Changed in version 3.3: In previous versions, this was a 16-bit type or a 32-bit type depending on whether you selected a “narrow” or “wide” Unicode version of Python at build time.

Deprecated since version 3.13, removed in version 3.15.

int PyUnicode\_READY([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_READY "Link to this definition")
  

Do nothing and return `0`. This API is kept only for backward compatibility, but there are no plans to remove it.

Added in version 3.3.

Deprecated since version 3.10: This API does nothing since Python 3.12. Previously, this needed to be called for each string created using the old API (`PyUnicode_FromUnicode()` or similar).

unsigned int PyUnicode\_IS\_READY([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unicode)[¶](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_IS_READY "Link to this definition")
  

Do nothing and return `1`. This API is kept only for backward compatibility, but there are no plans to remove it.

Added in version 3.3.

Deprecated since version 3.14: This API does nothing since Python 3.12. Previously, this could be called to check if [`PyUnicode_READY()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_READY "PyUnicode_READY")
 is necessary.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Unicode Objects and Codecs](https://docs.python.org/3/c-api/unicode.html#)
    *   [Unicode Objects](https://docs.python.org/3/c-api/unicode.html#unicode-objects)
        *   [Unicode Type](https://docs.python.org/3/c-api/unicode.html#unicode-type)
            
        *   [Unicode Character Properties](https://docs.python.org/3/c-api/unicode.html#unicode-character-properties)
            
        *   [Creating and accessing Unicode strings](https://docs.python.org/3/c-api/unicode.html#creating-and-accessing-unicode-strings)
            
        *   [Locale Encoding](https://docs.python.org/3/c-api/unicode.html#locale-encoding)
            
        *   [File System Encoding](https://docs.python.org/3/c-api/unicode.html#file-system-encoding)
            
        *   [wchar\_t Support](https://docs.python.org/3/c-api/unicode.html#wchar-t-support)
            
    *   [Built-in Codecs](https://docs.python.org/3/c-api/unicode.html#built-in-codecs)
        *   [Generic Codecs](https://docs.python.org/3/c-api/unicode.html#generic-codecs)
            
        *   [UTF-8 Codecs](https://docs.python.org/3/c-api/unicode.html#utf-8-codecs)
            
        *   [UTF-32 Codecs](https://docs.python.org/3/c-api/unicode.html#utf-32-codecs)
            
        *   [UTF-16 Codecs](https://docs.python.org/3/c-api/unicode.html#utf-16-codecs)
            
        *   [UTF-7 Codecs](https://docs.python.org/3/c-api/unicode.html#utf-7-codecs)
            
        *   [Unicode-Escape Codecs](https://docs.python.org/3/c-api/unicode.html#unicode-escape-codecs)
            
        *   [Raw-Unicode-Escape Codecs](https://docs.python.org/3/c-api/unicode.html#raw-unicode-escape-codecs)
            
        *   [Latin-1 Codecs](https://docs.python.org/3/c-api/unicode.html#latin-1-codecs)
            
        *   [ASCII Codecs](https://docs.python.org/3/c-api/unicode.html#ascii-codecs)
            
        *   [Character Map Codecs](https://docs.python.org/3/c-api/unicode.html#character-map-codecs)
            
        *   [MBCS codecs for Windows](https://docs.python.org/3/c-api/unicode.html#mbcs-codecs-for-windows)
            
    *   [Methods and Slot Functions](https://docs.python.org/3/c-api/unicode.html#methods-and-slot-functions)
        
    *   [PyUnicodeWriter](https://docs.python.org/3/c-api/unicode.html#pyunicodewriter)
        
    *   [Deprecated API](https://docs.python.org/3/c-api/unicode.html#deprecated-api)
        

#### Previous topic

[Byte Array Objects](https://docs.python.org/3/c-api/bytearray.html "previous chapter")

#### Next topic

[Tuple Objects](https://docs.python.org/3/c-api/tuple.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Unicode+Objects+and+Codecs&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Funicode.html&pagesource=c-api%2Funicode.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/unicode.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/tuple.html "Tuple Objects")
     |
*   [previous](https://docs.python.org/3/c-api/bytearray.html "Byte Array Objects")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python/C API reference manual](https://docs.python.org/3/c-api/index.html)
     »
*   [Concrete Objects Layer](https://docs.python.org/3/c-api/concrete.html)
     »
*   [Unicode Objects and Codecs](https://docs.python.org/3/c-api/unicode.html)
    
*    
    
    |
*   Theme Auto Light Dark |