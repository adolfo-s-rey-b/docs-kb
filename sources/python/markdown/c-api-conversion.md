### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/hash.html "PyHash API")
     |
*   [previous](https://docs.python.org/3/c-api/arg.html "Parsing arguments and building values")
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
*   [Utilities](https://docs.python.org/3/c-api/utilities.html)
     »
*   [String conversion and formatting](https://docs.python.org/3/c-api/conversion.html)
    
*    
    
    |
*   Theme Auto Light Dark |

String conversion and formatting[¶](https://docs.python.org/3/c-api/conversion.html#string-conversion-and-formatting "Link to this heading")

=============================================================================================================================================

Functions for number conversion and formatted string output.

int PyOS\_snprintf(char \*str, size\_t size, const char \*format, ...)[¶](https://docs.python.org/3/c-api/conversion.html#c.PyOS_snprintf "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Output not more than _size_ bytes to _str_ according to the format string _format_ and the extra arguments. See the Unix man page _[snprintf(3)](https://manpages.debian.org/snprintf(3))
_.

int PyOS\_vsnprintf(char \*str, size\_t size, const char \*format, va\_list va)[¶](https://docs.python.org/3/c-api/conversion.html#c.PyOS_vsnprintf "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Output not more than _size_ bytes to _str_ according to the format string _format_ and the variable argument list _va_. Unix man page _[vsnprintf(3)](https://manpages.debian.org/vsnprintf(3))
_.

[`PyOS_snprintf()`](https://docs.python.org/3/c-api/conversion.html#c.PyOS_snprintf "PyOS_snprintf")
 and [`PyOS_vsnprintf()`](https://docs.python.org/3/c-api/conversion.html#c.PyOS_vsnprintf "PyOS_vsnprintf")
 wrap the Standard C library functions `snprintf()` and `vsnprintf()`. Their purpose is to guarantee consistent behavior in corner cases, which the Standard C functions do not.

The wrappers ensure that `str[size-1]` is always `'\0'` upon return. They never write more than _size_ bytes (including the trailing `'\0'`) into str. Both functions require that `str != NULL`, `size > 0`, `format != NULL` and `size < INT_MAX`. Note that this means there is no equivalent to the C99 `n = snprintf(NULL, 0, ...)` which would determine the necessary buffer size.

The return value (_rv_) for these functions should be interpreted as follows:

*   When `0 <= rv < size`, the output conversion was successful and _rv_ characters were written to _str_ (excluding the trailing `'\0'` byte at `str[rv]`).
    
*   When `rv >= size`, the output conversion was truncated and a buffer with `rv + 1` bytes would have been needed to succeed. `str[size-1]` is `'\0'` in this case.
    
*   When `rv < 0`, the output conversion failed and `str[size-1]` is `'\0'` in this case too, but the rest of _str_ is undefined. The exact cause of the error depends on the underlying platform.
    

The following functions provide locale-independent string to number conversions.

unsigned long PyOS\_strtoul(const char \*str, char \*\*ptr, int base)[¶](https://docs.python.org/3/c-api/conversion.html#c.PyOS_strtoul "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Convert the initial part of the string in `str` to an unsigned long value according to the given `base`, which must be between `2` and `36` inclusive, or be the special value `0`.

Leading white space and case of characters are ignored. If `base` is zero it looks for a leading `0b`, `0o` or `0x` to tell which base. If these are absent it defaults to `10`. Base must be 0 or between 2 and 36 (inclusive). If `ptr` is non-`NULL` it will contain a pointer to the end of the scan.

If the converted value falls out of range of corresponding return type, range error occurs (`errno` is set to `ERANGE`) and `ULONG_MAX` is returned. If no conversion can be performed, `0` is returned.

See also the Unix man page _[strtoul(3)](https://manpages.debian.org/strtoul(3))
_.

Added in version 3.2.

long PyOS\_strtol(const char \*str, char \*\*ptr, int base)[¶](https://docs.python.org/3/c-api/conversion.html#c.PyOS_strtol "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Convert the initial part of the string in `str` to an long value according to the given `base`, which must be between `2` and `36` inclusive, or be the special value `0`.

Same as [`PyOS_strtoul()`](https://docs.python.org/3/c-api/conversion.html#c.PyOS_strtoul "PyOS_strtoul")
, but return a long value instead and `LONG_MAX` on overflows.

See also the Unix man page _[strtol(3)](https://manpages.debian.org/strtol(3))
_.

Added in version 3.2.

double PyOS\_string\_to\_double(const char \*s, char \*\*endptr, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*overflow\_exception)[¶](https://docs.python.org/3/c-api/conversion.html#c.PyOS_string_to_double "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Convert a string `s` to a double, raising a Python exception on failure. The set of accepted strings corresponds to the set of strings accepted by Python’s [`float()`](https://docs.python.org/3/builtins/functions.html#float "float")
 constructor, except that `s` must not have leading or trailing whitespace. The conversion is independent of the current locale.

If `endptr` is `NULL`, convert the whole string. Raise [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 and return `-1.0` if the string is not a valid representation of a floating-point number.

If endptr is not `NULL`, convert as much of the string as possible and set `*endptr` to point to the first unconverted character. If no initial segment of the string is the valid representation of a floating-point number, set `*endptr` to point to the beginning of the string, raise ValueError, and return `-1.0`.

If `s` represents a value that is too large to store in a float (for example, `"1e500"` is such a string on many platforms) then if `overflow_exception` is `NULL` return `INFINITY` (with an appropriate sign) and don’t set any exception. Otherwise, `overflow_exception` must point to a Python exception object; raise that exception and return `-1.0`. In both cases, set `*endptr` to point to the first character after the converted value.

If any other error occurs during the conversion (for example an out-of-memory error), set the appropriate Python exception and return `-1.0`.

Added in version 3.1.

char \*PyOS\_double\_to\_string(double val, char format\_code, int precision, int flags, int \*ptype)[¶](https://docs.python.org/3/c-api/conversion.html#c.PyOS_double_to_string "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Convert a double _val_ to a string using supplied _format\_code_, _precision_, and _flags_.

_format\_code_ must be one of `'e'`, `'E'`, `'f'`, `'F'`, `'g'`, `'G'` or `'r'`. For `'r'`, the supplied _precision_ must be 0 and is ignored. The `'r'` format code specifies the standard [`repr()`](https://docs.python.org/3/builtins/functions.html#repr "repr")
 format.

_flags_ can be zero or more of the following values or-ed together:

Py\_DTSF\_SIGN[¶](https://docs.python.org/3/c-api/conversion.html#c.Py_DTSF_SIGN "Link to this definition")
  

Always precede the returned string with a sign character, even if _val_ is non-negative.

Py\_DTSF\_ADD\_DOT\_0[¶](https://docs.python.org/3/c-api/conversion.html#c.Py_DTSF_ADD_DOT_0 "Link to this definition")
  

Ensure that the returned string will not look like an integer.

Py\_DTSF\_ALT[¶](https://docs.python.org/3/c-api/conversion.html#c.Py_DTSF_ALT "Link to this definition")
  

Apply “alternate” formatting rules. See the documentation for the [`PyOS_snprintf()`](https://docs.python.org/3/c-api/conversion.html#c.PyOS_snprintf "PyOS_snprintf")
 `'#'` specifier for details.

Py\_DTSF\_NO\_NEG\_0[¶](https://docs.python.org/3/c-api/conversion.html#c.Py_DTSF_NO_NEG_0 "Link to this definition")
  

Negative zero is converted to positive zero.

Added in version 3.11.

If _ptype_ is non-`NULL`, then the value it points to will be set to one of the following constants depending on the type of _val_:

| _\*ptype_ | type of _val_ |
| --- | --- |
| Py\_DTST\_FINITE[¶](https://docs.python.org/3/c-api/conversion.html#c.Py_DTST_FINITE "Link to this definition") | finite number |
| Py\_DTST\_INFINITE[¶](https://docs.python.org/3/c-api/conversion.html#c.Py_DTST_INFINITE "Link to this definition") | infinite number |
| Py\_DTST\_NAN[¶](https://docs.python.org/3/c-api/conversion.html#c.Py_DTST_NAN "Link to this definition") | not a number |

The return value is a pointer to _buffer_ with the converted string or `NULL` if the conversion failed. The caller is responsible for freeing the returned string by calling [`PyMem_Free()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_Free "PyMem_Free")
.

Added in version 3.1.

int PyOS\_mystricmp(const char \*str1, const char \*str2)[¶](https://docs.python.org/3/c-api/conversion.html#c.PyOS_mystricmp "Link to this definition")
  

int PyOS\_mystrnicmp(const char \*str1, const char \*str2, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 size)[¶](https://docs.python.org/3/c-api/conversion.html#c.PyOS_mystrnicmp "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Case insensitive comparison of strings. These functions work almost identically to `strcmp()` and `strncmp()` (respectively), except that they ignore the case of ASCII characters.

Return `0` if the strings are equal, a negative value if _str1_ sorts lexicographically before _str2_, or a positive value if it sorts after.

In the _str1_ or _str2_ arguments, a NUL byte marks the end of the string. For `PyOS_mystrnicmp()`, the _size_ argument gives the maximum size of the string, as if NUL was present at the index given by _size_.

These functions do not use the locale.

int PyOS\_stricmp(const char \*str1, const char \*str2)[¶](https://docs.python.org/3/c-api/conversion.html#c.PyOS_stricmp "Link to this definition")
  

int PyOS\_strnicmp(const char \*str1, const char \*str2, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 size)[¶](https://docs.python.org/3/c-api/conversion.html#c.PyOS_strnicmp "Link to this definition")
  

Case insensitive comparison of strings.

On Windows, these are aliases of `stricmp()` and `strnicmp()`, respectively.

On other platforms, they are aliases of [`PyOS_mystricmp()`](https://docs.python.org/3/c-api/conversion.html#c.PyOS_mystricmp "PyOS_mystricmp")
 and [`PyOS_mystrnicmp()`](https://docs.python.org/3/c-api/conversion.html#c.PyOS_mystrnicmp "PyOS_mystrnicmp")
, respectively.

Character classification and conversion[¶](https://docs.python.org/3/c-api/conversion.html#character-classification-and-conversion "Link to this heading")

===========================================================================================================================================================

The following macros provide locale-independent (unlike the C standard library `ctype.h`) character classification and conversion. The argument must be a signed or unsigned char.

Py\_ISALNUM(c)[¶](https://docs.python.org/3/c-api/conversion.html#c.Py_ISALNUM "Link to this definition")
  

Return true if the character _c_ is an alphanumeric character.

Py\_ISALPHA(c)[¶](https://docs.python.org/3/c-api/conversion.html#c.Py_ISALPHA "Link to this definition")
  

Return true if the character _c_ is an alphabetic character (`a-z` and `A-Z`).

Py\_ISDIGIT(c)[¶](https://docs.python.org/3/c-api/conversion.html#c.Py_ISDIGIT "Link to this definition")
  

Return true if the character _c_ is a decimal digit (`0-9`).

Py\_ISLOWER(c)[¶](https://docs.python.org/3/c-api/conversion.html#c.Py_ISLOWER "Link to this definition")
  

Return true if the character _c_ is a lowercase ASCII letter (`a-z`).

Py\_ISUPPER(c)[¶](https://docs.python.org/3/c-api/conversion.html#c.Py_ISUPPER "Link to this definition")
  

Return true if the character _c_ is an uppercase ASCII letter (`A-Z`).

Py\_ISSPACE(c)[¶](https://docs.python.org/3/c-api/conversion.html#c.Py_ISSPACE "Link to this definition")
  

Return true if the character _c_ is a whitespace character (space, tab, carriage return, newline, vertical tab, or form feed).

Py\_ISXDIGIT(c)[¶](https://docs.python.org/3/c-api/conversion.html#c.Py_ISXDIGIT "Link to this definition")
  

Return true if the character _c_ is a hexadecimal digit (`0-9`, `a-f`, and `A-F`).

Py\_TOLOWER(c)[¶](https://docs.python.org/3/c-api/conversion.html#c.Py_TOLOWER "Link to this definition")
  

Return the lowercase equivalent of the character _c_.

Py\_TOUPPER(c)[¶](https://docs.python.org/3/c-api/conversion.html#c.Py_TOUPPER "Link to this definition")
  

Return the uppercase equivalent of the character _c_.

Bit masks[¶](https://docs.python.org/3/c-api/conversion.html#bit-masks "Link to this heading")

-----------------------------------------------------------------------------------------------

The following constants are bit masks used by the character classification macros above:

PY\_CTF\_ALNUM[¶](https://docs.python.org/3/c-api/conversion.html#c.PY_CTF_ALNUM "Link to this definition")
  

PY\_CTF\_ALPHA[¶](https://docs.python.org/3/c-api/conversion.html#c.PY_CTF_ALPHA "Link to this definition")
  

PY\_CTF\_DIGIT[¶](https://docs.python.org/3/c-api/conversion.html#c.PY_CTF_DIGIT "Link to this definition")
  

PY\_CTF\_LOWER[¶](https://docs.python.org/3/c-api/conversion.html#c.PY_CTF_LOWER "Link to this definition")
  

PY\_CTF\_SPACE[¶](https://docs.python.org/3/c-api/conversion.html#c.PY_CTF_SPACE "Link to this definition")
  

PY\_CTF\_UPPER[¶](https://docs.python.org/3/c-api/conversion.html#c.PY_CTF_UPPER "Link to this definition")
  

PY\_CTF\_XDIGIT[¶](https://docs.python.org/3/c-api/conversion.html#c.PY_CTF_XDIGIT "Link to this definition")
  

Values used internally by the `Py_IS*` classification macros above. Exposed for backwards compatibility only.

[Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 since version 3.15.2.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [String conversion and formatting](https://docs.python.org/3/c-api/conversion.html#)
    
*   [Character classification and conversion](https://docs.python.org/3/c-api/conversion.html#character-classification-and-conversion)
    *   [Bit masks](https://docs.python.org/3/c-api/conversion.html#bit-masks)
        

#### Previous topic

[Parsing arguments and building values](https://docs.python.org/3/c-api/arg.html "previous chapter")

#### Next topic

[PyHash API](https://docs.python.org/3/c-api/hash.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=String+conversion+and+formatting&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fconversion.html&pagesource=c-api%2Fconversion.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/conversion.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/hash.html "PyHash API")
     |
*   [previous](https://docs.python.org/3/c-api/arg.html "Parsing arguments and building values")
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
*   [Utilities](https://docs.python.org/3/c-api/utilities.html)
     »
*   [String conversion and formatting](https://docs.python.org/3/c-api/conversion.html)
    
*    
    
    |
*   Theme Auto Light Dark |