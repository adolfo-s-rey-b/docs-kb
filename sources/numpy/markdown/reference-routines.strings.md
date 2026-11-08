[Skip to main content](https://numpy.org/doc/stable/reference/routines.strings.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/routines.strings.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/routines.strings.html)
[2.4](https://numpy.org/doc/2.4/reference/routines.strings.html)
[2.3](https://numpy.org/doc/2.3/reference/routines.strings.html)
[2.2](https://numpy.org/doc/2.2/reference/routines.strings.html)
[2.1](https://numpy.org/doc/2.1/reference/routines.strings.html)
[2.0](https://numpy.org/doc/2.0/reference/routines.strings.html)
[1.26](https://numpy.org/doc/1.26/reference/routines.strings.html)
[1.25](https://numpy.org/doc/1.25/reference/routines.strings.html)
[1.24](https://numpy.org/doc/1.24/reference/routines.strings.html)
[1.23](https://numpy.org/doc/1.23/reference/routines.strings.html)
[1.22](https://numpy.org/doc/1.22/reference/routines.strings.html)
[1.21](https://numpy.org/doc/1.21/reference/routines.strings.html)
[1.20](https://numpy.org/doc/1.20/reference/routines.strings.html)
[1.19](https://numpy.org/doc/1.19/reference/routines.strings.html)
[1.18](https://numpy.org/doc/1.18/reference/routines.strings.html)
[1.17](https://numpy.org/doc/1.17/reference/routines.strings.html)
[1.16](https://numpy.org/doc/1.16/reference/routines.strings.html)
[1.15](https://numpy.org/doc/1.15/reference/routines.strings.html)
[1.14](https://numpy.org/doc/1.14/reference/routines.strings.html)
[1.13](https://numpy.org/doc/1.13/reference/routines.strings.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

String functionality[#](https://numpy.org/doc/stable/reference/routines.strings.html#module-numpy.strings "Link to this heading")

==================================================================================================================================

The [`numpy.strings`](https://numpy.org/doc/stable/reference/routines.strings.html#module-numpy.strings "numpy.strings")
 module provides a set of universal functions operating on arrays of type [`numpy.str_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.str_ "numpy.str_")
 or [`numpy.bytes_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.bytes_ "numpy.bytes_")
. For example,

Try it in your browser!

\>>> np.strings.add(\["num", "doc"\], \["py", "umentation"\])
array(\['numpy', 'documentation'\], dtype='<U13')

Copy to clipboard

Go BackOpen In Tab

These universal functions are also used in [`numpy.char`](https://numpy.org/doc/stable/reference/routines.char.html#module-numpy.char "numpy.char")
, which provides the [`numpy.char.chararray`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.html#numpy.char.chararray "numpy.char.chararray")
 array subclass, in order for those routines to get the performance benefits as well.

Note

Prior to NumPy 2.0, all string functionality was in [`numpy.char`](https://numpy.org/doc/stable/reference/routines.char.html#module-numpy.char "numpy.char")
, which only operated on fixed-width strings. That module will not be getting updates and will be deprecated at some point in the future.

String operations[#](https://numpy.org/doc/stable/reference/routines.strings.html#string-operations "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`add`](https://numpy.org/doc/stable/reference/generated/numpy.strings.add.html#numpy.strings.add "numpy.strings.add")<br>(x1, x2, /\[, out, where, casting, order, ...\]) | Add arguments element-wise. |
| [`center`](https://numpy.org/doc/stable/reference/generated/numpy.strings.center.html#numpy.strings.center "numpy.strings.center")<br>(a, width\[, fillchar\]) | Return a copy of _a_ with its elements centered in a string of length _width_. |
| [`capitalize`](https://numpy.org/doc/stable/reference/generated/numpy.strings.capitalize.html#numpy.strings.capitalize "numpy.strings.capitalize")<br>(a) | Return a copy of `a` with only the first character of each element capitalized. |
| [`decode`](https://numpy.org/doc/stable/reference/generated/numpy.strings.decode.html#numpy.strings.decode "numpy.strings.decode")<br>(a\[, encoding, errors\]) | Calls [`bytes.decode`](https://docs.python.org/3/library/stdtypes.html#bytes.decode "(in Python v3.14)")<br> element-wise. |
| [`encode`](https://numpy.org/doc/stable/reference/generated/numpy.strings.encode.html#numpy.strings.encode "numpy.strings.encode")<br>(a\[, encoding, errors\]) | Calls [`str.encode`](https://docs.python.org/3/library/stdtypes.html#str.encode "(in Python v3.14)")<br> element-wise. |
| [`expandtabs`](https://numpy.org/doc/stable/reference/generated/numpy.strings.expandtabs.html#numpy.strings.expandtabs "numpy.strings.expandtabs")<br>(a\[, tabsize\]) | Return a copy of each string element where all tab characters are replaced by one or more spaces. |
| [`ljust`](https://numpy.org/doc/stable/reference/generated/numpy.strings.ljust.html#numpy.strings.ljust "numpy.strings.ljust")<br>(a, width\[, fillchar\]) | Return an array with the elements of _a_ left-justified in a string of length _width_. |
| [`lower`](https://numpy.org/doc/stable/reference/generated/numpy.strings.lower.html#numpy.strings.lower "numpy.strings.lower")<br>(a) | Return an array with the elements converted to lowercase. |
| [`lstrip`](https://numpy.org/doc/stable/reference/generated/numpy.strings.lstrip.html#numpy.strings.lstrip "numpy.strings.lstrip")<br>(a\[, chars\]) | For each element in _a_, return a copy with the leading characters removed. |
| [`mod`](https://numpy.org/doc/stable/reference/generated/numpy.strings.mod.html#numpy.strings.mod "numpy.strings.mod")<br>(a, values) | Return (a % i), that is pre-Python 2.6 string formatting (interpolation), element-wise for a pair of array\_likes of str or unicode. |
| [`multiply`](https://numpy.org/doc/stable/reference/generated/numpy.strings.multiply.html#numpy.strings.multiply "numpy.strings.multiply")<br>(a, i) | Return (a \* i), that is string multiple concatenation, element-wise. |
| [`partition`](https://numpy.org/doc/stable/reference/generated/numpy.strings.partition.html#numpy.strings.partition "numpy.strings.partition")<br>(a, sep) | Partition each element in `a` around `sep`. |
| [`replace`](https://numpy.org/doc/stable/reference/generated/numpy.strings.replace.html#numpy.strings.replace "numpy.strings.replace")<br>(a, old, new\[, count\]) | For each element in `a`, return a copy of the string with occurrences of substring `old` replaced by `new`. |
| [`rjust`](https://numpy.org/doc/stable/reference/generated/numpy.strings.rjust.html#numpy.strings.rjust "numpy.strings.rjust")<br>(a, width\[, fillchar\]) | Return an array with the elements of _a_ right-justified in a string of length _width_. |
| [`rpartition`](https://numpy.org/doc/stable/reference/generated/numpy.strings.rpartition.html#numpy.strings.rpartition "numpy.strings.rpartition")<br>(a, sep) | Partition (split) each element around the right-most separator. |
| [`rstrip`](https://numpy.org/doc/stable/reference/generated/numpy.strings.rstrip.html#numpy.strings.rstrip "numpy.strings.rstrip")<br>(a\[, chars\]) | For each element in _a_, return a copy with the trailing characters removed. |
| [`slice`](https://numpy.org/doc/stable/reference/generated/numpy.strings.slice.html#numpy.strings.slice "numpy.strings.slice")<br>(a\[, start, stop, step\]) | Slice the strings in _a_ by slices specified by _start_, _stop_, _step_. |
| [`strip`](https://numpy.org/doc/stable/reference/generated/numpy.strings.strip.html#numpy.strings.strip "numpy.strings.strip")<br>(a\[, chars\]) | For each element in _a_, return a copy with the leading and trailing characters removed. |
| [`swapcase`](https://numpy.org/doc/stable/reference/generated/numpy.strings.swapcase.html#numpy.strings.swapcase "numpy.strings.swapcase")<br>(a) | Return element-wise a copy of the string with uppercase characters converted to lowercase and vice versa. |
| [`title`](https://numpy.org/doc/stable/reference/generated/numpy.strings.title.html#numpy.strings.title "numpy.strings.title")<br>(a) | Return element-wise title cased version of string or unicode. |
| [`translate`](https://numpy.org/doc/stable/reference/generated/numpy.strings.translate.html#numpy.strings.translate "numpy.strings.translate")<br>(a, table\[, deletechars\]) | For each element in _a_, return a copy of the string where all characters occurring in the optional argument _deletechars_ are removed, and the remaining characters have been mapped through the given translation table. |
| [`upper`](https://numpy.org/doc/stable/reference/generated/numpy.strings.upper.html#numpy.strings.upper "numpy.strings.upper")<br>(a) | Return an array with the elements converted to uppercase. |
| [`zfill`](https://numpy.org/doc/stable/reference/generated/numpy.strings.zfill.html#numpy.strings.zfill "numpy.strings.zfill")<br>(a, width) | Return the numeric string left-filled with zeros. |

Comparison[#](https://numpy.org/doc/stable/reference/routines.strings.html#comparison "Link to this heading")

--------------------------------------------------------------------------------------------------------------

The [`numpy.strings`](https://numpy.org/doc/stable/reference/routines.strings.html#module-numpy.strings "numpy.strings")
 module also exports the comparison universal functions that can now operate on string arrays as well.

|     |     |
| --- | --- |
| [`equal`](https://numpy.org/doc/stable/reference/generated/numpy.strings.equal.html#numpy.strings.equal "numpy.strings.equal")<br>(x1, x2, /\[, out, where, casting, ...\]) | Return (x1 == x2) element-wise. |
| [`not_equal`](https://numpy.org/doc/stable/reference/generated/numpy.strings.not_equal.html#numpy.strings.not_equal "numpy.strings.not_equal")<br>(x1, x2, /\[, out, where, casting, ...\]) | Return (x1 != x2) element-wise. |
| [`greater_equal`](https://numpy.org/doc/stable/reference/generated/numpy.strings.greater_equal.html#numpy.strings.greater_equal "numpy.strings.greater_equal")<br>(x1, x2, /\[, out, where, ...\]) | Return the truth value of (x1 >= x2) element-wise. |
| [`less_equal`](https://numpy.org/doc/stable/reference/generated/numpy.strings.less_equal.html#numpy.strings.less_equal "numpy.strings.less_equal")<br>(x1, x2, /\[, out, where, casting, ...\]) | Return the truth value of (x1 <= x2) element-wise. |
| [`greater`](https://numpy.org/doc/stable/reference/generated/numpy.strings.greater.html#numpy.strings.greater "numpy.strings.greater")<br>(x1, x2, /\[, out, where, casting, ...\]) | Return the truth value of (x1 > x2) element-wise. |
| [`less`](https://numpy.org/doc/stable/reference/generated/numpy.strings.less.html#numpy.strings.less "numpy.strings.less")<br>(x1, x2, /\[, out, where, casting, ...\]) | Return the truth value of (x1 < x2) element-wise. |

String information[#](https://numpy.org/doc/stable/reference/routines.strings.html#string-information "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`count`](https://numpy.org/doc/stable/reference/generated/numpy.strings.count.html#numpy.strings.count "numpy.strings.count")<br>(a, sub\[, start, end\]) | Returns an array with the number of non-overlapping occurrences of substring `sub` in the range \[`start`, `end`). |\
| [`endswith`](https://numpy.org/doc/stable/reference/generated/numpy.strings.endswith.html#numpy.strings.endswith "numpy.strings.endswith")<br>(a, suffix\[, start, end\]) | Returns a boolean array which is _True_ where the string element in `a` ends with `suffix`, otherwise _False_. |\
| [`find`](https://numpy.org/doc/stable/reference/generated/numpy.strings.find.html#numpy.strings.find "numpy.strings.find")<br>(a, sub\[, start, end\]) | For each element, return the lowest index in the string where substring `sub` is found, such that `sub` is contained in the range \[`start`, `end`). |\
| [`index`](https://numpy.org/doc/stable/reference/generated/numpy.strings.index.html#numpy.strings.index "numpy.strings.index")<br>(a, sub\[, start, end\]) | Like [`find`](https://numpy.org/doc/stable/reference/generated/numpy.strings.find.html#numpy.strings.find "numpy.strings.find")<br>, but raises [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)")<br> when the substring is not found. |\
| [`isalnum`](https://numpy.org/doc/stable/reference/generated/numpy.strings.isalnum.html#numpy.strings.isalnum "numpy.strings.isalnum")<br>(x, /\[, out, where, casting, order, ...\]) | Returns true for each element if all characters in the string are alphanumeric and there is at least one character, false otherwise. |\
| [`isalpha`](https://numpy.org/doc/stable/reference/generated/numpy.strings.isalpha.html#numpy.strings.isalpha "numpy.strings.isalpha")<br>(x, /\[, out, where, casting, order, ...\]) | Returns true for each element if all characters in the data interpreted as a string are alphabetic and there is at least one character, false otherwise. |\
| [`isdecimal`](https://numpy.org/doc/stable/reference/generated/numpy.strings.isdecimal.html#numpy.strings.isdecimal "numpy.strings.isdecimal")<br>(x, /\[, out, where, casting, ...\]) | For each element, return True if there are only decimal characters in the element. |\
| [`isdigit`](https://numpy.org/doc/stable/reference/generated/numpy.strings.isdigit.html#numpy.strings.isdigit "numpy.strings.isdigit")<br>(x, /\[, out, where, casting, order, ...\]) | Returns true for each element if all characters in the string are digits and there is at least one character, false otherwise. |\
| [`islower`](https://numpy.org/doc/stable/reference/generated/numpy.strings.islower.html#numpy.strings.islower "numpy.strings.islower")<br>(x, /\[, out, where, casting, order, ...\]) | Returns true for each element if all cased characters in the string are lowercase and there is at least one cased character, false otherwise. |\
| [`isnumeric`](https://numpy.org/doc/stable/reference/generated/numpy.strings.isnumeric.html#numpy.strings.isnumeric "numpy.strings.isnumeric")<br>(x, /\[, out, where, casting, ...\]) | For each element, return True if there are only numeric characters in the element. |\
| [`isspace`](https://numpy.org/doc/stable/reference/generated/numpy.strings.isspace.html#numpy.strings.isspace "numpy.strings.isspace")<br>(x, /\[, out, where, casting, order, ...\]) | Returns true for each element if there are only whitespace characters in the string and there is at least one character, false otherwise. |\
| [`istitle`](https://numpy.org/doc/stable/reference/generated/numpy.strings.istitle.html#numpy.strings.istitle "numpy.strings.istitle")<br>(x, /\[, out, where, casting, order, ...\]) | Returns true for each element if the element is a titlecased string and there is at least one character, false otherwise. |\
| [`isupper`](https://numpy.org/doc/stable/reference/generated/numpy.strings.isupper.html#numpy.strings.isupper "numpy.strings.isupper")<br>(x, /\[, out, where, casting, order, ...\]) | Return true for each element if all cased characters in the string are uppercase and there is at least one character, false otherwise. |\
| [`rfind`](https://numpy.org/doc/stable/reference/generated/numpy.strings.rfind.html#numpy.strings.rfind "numpy.strings.rfind")<br>(a, sub\[, start, end\]) | For each element, return the highest index in the string where substring `sub` is found, such that `sub` is contained in the range \[`start`, `end`). |\
| [`rindex`](https://numpy.org/doc/stable/reference/generated/numpy.strings.rindex.html#numpy.strings.rindex "numpy.strings.rindex")<br>(a, sub\[, start, end\]) | Like [`rfind`](https://numpy.org/doc/stable/reference/generated/numpy.strings.rfind.html#numpy.strings.rfind "numpy.strings.rfind")<br>, but raises [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)")<br> when the substring _sub_ is not found. |\
| [`startswith`](https://numpy.org/doc/stable/reference/generated/numpy.strings.startswith.html#numpy.strings.startswith "numpy.strings.startswith")<br>(a, prefix\[, start, end\]) | Returns a boolean array which is _True_ where the string element in `a` starts with `prefix`, otherwise _False_. |\
| [`str_len`](https://numpy.org/doc/stable/reference/generated/numpy.strings.str_len.html#numpy.strings.str_len "numpy.strings.str_len")<br>(x, /\[, out, where, casting, order, ...\]) | Returns the length of each element. |\
\
On this page