[Skip to main content](https://numpy.org/doc/stable/reference/routines.char.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/routines.char.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/routines.char.html)
[2.4](https://numpy.org/doc/2.4/reference/routines.char.html)
[2.3](https://numpy.org/doc/2.3/reference/routines.char.html)
[2.2](https://numpy.org/doc/2.2/reference/routines.char.html)
[2.1](https://numpy.org/doc/2.1/reference/routines.char.html)
[2.0](https://numpy.org/doc/2.0/reference/routines.char.html)
[1.26](https://numpy.org/doc/1.26/reference/routines.char.html)
[1.25](https://numpy.org/doc/1.25/reference/routines.char.html)
[1.24](https://numpy.org/doc/1.24/reference/routines.char.html)
[1.23](https://numpy.org/doc/1.23/reference/routines.char.html)
[1.22](https://numpy.org/doc/1.22/reference/routines.char.html)
[1.21](https://numpy.org/doc/1.21/reference/routines.char.html)
[1.20](https://numpy.org/doc/1.20/reference/routines.char.html)
[1.19](https://numpy.org/doc/1.19/reference/routines.char.html)
[1.18](https://numpy.org/doc/1.18/reference/routines.char.html)
[1.17](https://numpy.org/doc/1.17/reference/routines.char.html)
[1.16](https://numpy.org/doc/1.16/reference/routines.char.html)
[1.15](https://numpy.org/doc/1.15/reference/routines.char.html)
[1.14](https://numpy.org/doc/1.14/reference/routines.char.html)
[1.13](https://numpy.org/doc/1.13/reference/routines.char.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Legacy fixed-width string functionality[#](https://numpy.org/doc/stable/reference/routines.char.html#module-numpy.char "Link to this heading")

===============================================================================================================================================

Legacy

This submodule is considered legacy and will no longer receive updates. This could also mean it will be removed in future NumPy versions. The string operations in this module are planned to be deprecated in the future, and the [`numpy.char.chararray`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.html#numpy.char.chararray "numpy.char.chararray")
 class is deprecated in NumPy 2.5. Use [`numpy.strings`](https://numpy.org/doc/stable/reference/routines.strings.html#module-numpy.strings "numpy.strings")
 instead.

The [`numpy.char`](https://numpy.org/doc/stable/reference/routines.char.html#module-numpy.char "numpy.char")
 module provides a set of vectorized string operations for arrays of type [`numpy.str_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.str_ "numpy.str_")
 or [`numpy.bytes_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.bytes_ "numpy.bytes_")
. For example

Try it in your browser!

\>>> import numpy as np
\>>> np.char.capitalize(\["python", "numpy"\])
array(\['Python', 'Numpy'\], dtype='<U6')
\>>> np.char.add(\["num", "doc"\], \["py", "umentation"\])
array(\['numpy', 'documentation'\], dtype='<U13')

Copy to clipboard

Go BackOpen In Tab

The methods in this module are based on the methods in [`string`](https://docs.python.org/3/library/string.html#module-string "(in Python v3.14)")

String operations[#](https://numpy.org/doc/stable/reference/routines.char.html#string-operations "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`add`](https://numpy.org/doc/stable/reference/generated/numpy.char.add.html#numpy.char.add "numpy.char.add")<br>(x1, x2, /\[, out, where, casting, order, ...\]) | Add arguments element-wise. |
| [`multiply`](https://numpy.org/doc/stable/reference/generated/numpy.char.multiply.html#numpy.char.multiply "numpy.char.multiply")<br>(a, i) | Return (a \* i), that is string multiple concatenation, element-wise. |
| [`mod`](https://numpy.org/doc/stable/reference/generated/numpy.char.mod.html#numpy.char.mod "numpy.char.mod")<br>(a, values) | Return (a % i), that is pre-Python 2.6 string formatting (interpolation), element-wise for a pair of array\_likes of str or unicode. |
| [`capitalize`](https://numpy.org/doc/stable/reference/generated/numpy.char.capitalize.html#numpy.char.capitalize "numpy.char.capitalize")<br>(a) | Return a copy of `a` with only the first character of each element capitalized. |
| [`center`](https://numpy.org/doc/stable/reference/generated/numpy.char.center.html#numpy.char.center "numpy.char.center")<br>(a, width\[, fillchar\]) | Return a copy of _a_ with its elements centered in a string of length _width_. |
| [`decode`](https://numpy.org/doc/stable/reference/generated/numpy.char.decode.html#numpy.char.decode "numpy.char.decode")<br>(a\[, encoding, errors\]) | Calls [`bytes.decode`](https://docs.python.org/3/library/stdtypes.html#bytes.decode "(in Python v3.14)")<br> element-wise. |
| [`encode`](https://numpy.org/doc/stable/reference/generated/numpy.char.encode.html#numpy.char.encode "numpy.char.encode")<br>(a\[, encoding, errors\]) | Calls [`str.encode`](https://docs.python.org/3/library/stdtypes.html#str.encode "(in Python v3.14)")<br> element-wise. |
| [`expandtabs`](https://numpy.org/doc/stable/reference/generated/numpy.char.expandtabs.html#numpy.char.expandtabs "numpy.char.expandtabs")<br>(a\[, tabsize\]) | Return a copy of each string element where all tab characters are replaced by one or more spaces. |
| [`join`](https://numpy.org/doc/stable/reference/generated/numpy.char.join.html#numpy.char.join "numpy.char.join")<br>(sep, seq) | Return a string which is the concatenation of the strings in the sequence _seq_. |
| [`ljust`](https://numpy.org/doc/stable/reference/generated/numpy.char.ljust.html#numpy.char.ljust "numpy.char.ljust")<br>(a, width\[, fillchar\]) | Return an array with the elements of _a_ left-justified in a string of length _width_. |
| [`lower`](https://numpy.org/doc/stable/reference/generated/numpy.char.lower.html#numpy.char.lower "numpy.char.lower")<br>(a) | Return an array with the elements converted to lowercase. |
| [`lstrip`](https://numpy.org/doc/stable/reference/generated/numpy.char.lstrip.html#numpy.char.lstrip "numpy.char.lstrip")<br>(a\[, chars\]) | For each element in _a_, return a copy with the leading characters removed. |
| [`partition`](https://numpy.org/doc/stable/reference/generated/numpy.char.partition.html#numpy.char.partition "numpy.char.partition")<br>(a, sep) | Partition each element in _a_ around _sep_. |
| [`replace`](https://numpy.org/doc/stable/reference/generated/numpy.char.replace.html#numpy.char.replace "numpy.char.replace")<br>(a, old, new\[, count\]) | For each element in `a`, return a copy of the string with occurrences of substring `old` replaced by `new`. |
| [`rjust`](https://numpy.org/doc/stable/reference/generated/numpy.char.rjust.html#numpy.char.rjust "numpy.char.rjust")<br>(a, width\[, fillchar\]) | Return an array with the elements of _a_ right-justified in a string of length _width_. |
| [`rpartition`](https://numpy.org/doc/stable/reference/generated/numpy.char.rpartition.html#numpy.char.rpartition "numpy.char.rpartition")<br>(a, sep) | Partition (split) each element around the right-most separator. |
| [`rsplit`](https://numpy.org/doc/stable/reference/generated/numpy.char.rsplit.html#numpy.char.rsplit "numpy.char.rsplit")<br>(a\[, sep, maxsplit\]) | For each element in _a_, return a list of the words in the string, using _sep_ as the delimiter string. |
| [`rstrip`](https://numpy.org/doc/stable/reference/generated/numpy.char.rstrip.html#numpy.char.rstrip "numpy.char.rstrip")<br>(a\[, chars\]) | For each element in _a_, return a copy with the trailing characters removed. |
| [`split`](https://numpy.org/doc/stable/reference/generated/numpy.char.split.html#numpy.char.split "numpy.char.split")<br>(a\[, sep, maxsplit\]) | For each element in _a_, return a list of the words in the string, using _sep_ as the delimiter string. |
| [`splitlines`](https://numpy.org/doc/stable/reference/generated/numpy.char.splitlines.html#numpy.char.splitlines "numpy.char.splitlines")<br>(a\[, keepends\]) | For each element in _a_, return a list of the lines in the element, breaking at line boundaries. |
| [`strip`](https://numpy.org/doc/stable/reference/generated/numpy.char.strip.html#numpy.char.strip "numpy.char.strip")<br>(a\[, chars\]) | For each element in _a_, return a copy with the leading and trailing characters removed. |
| [`swapcase`](https://numpy.org/doc/stable/reference/generated/numpy.char.swapcase.html#numpy.char.swapcase "numpy.char.swapcase")<br>(a) | Return element-wise a copy of the string with uppercase characters converted to lowercase and vice versa. |
| [`title`](https://numpy.org/doc/stable/reference/generated/numpy.char.title.html#numpy.char.title "numpy.char.title")<br>(a) | Return element-wise title cased version of string or unicode. |
| [`translate`](https://numpy.org/doc/stable/reference/generated/numpy.char.translate.html#numpy.char.translate "numpy.char.translate")<br>(a, table\[, deletechars\]) | For each element in _a_, return a copy of the string where all characters occurring in the optional argument _deletechars_ are removed, and the remaining characters have been mapped through the given translation table. |
| [`upper`](https://numpy.org/doc/stable/reference/generated/numpy.char.upper.html#numpy.char.upper "numpy.char.upper")<br>(a) | Return an array with the elements converted to uppercase. |
| [`zfill`](https://numpy.org/doc/stable/reference/generated/numpy.char.zfill.html#numpy.char.zfill "numpy.char.zfill")<br>(a, width) | Return the numeric string left-filled with zeros. |

Comparison[#](https://numpy.org/doc/stable/reference/routines.char.html#comparison "Link to this heading")

-----------------------------------------------------------------------------------------------------------

Unlike the standard numpy comparison operators, the ones in the _char_ module strip trailing whitespace characters before performing the comparison.

|     |     |
| --- | --- |
| [`equal`](https://numpy.org/doc/stable/reference/generated/numpy.char.equal.html#numpy.char.equal "numpy.char.equal")<br>(x1, x2) | Return (x1 == x2) element-wise. |
| [`not_equal`](https://numpy.org/doc/stable/reference/generated/numpy.char.not_equal.html#numpy.char.not_equal "numpy.char.not_equal")<br>(x1, x2) | Return (x1 != x2) element-wise. |
| [`greater_equal`](https://numpy.org/doc/stable/reference/generated/numpy.char.greater_equal.html#numpy.char.greater_equal "numpy.char.greater_equal")<br>(x1, x2) | Return (x1 >= x2) element-wise. |
| [`less_equal`](https://numpy.org/doc/stable/reference/generated/numpy.char.less_equal.html#numpy.char.less_equal "numpy.char.less_equal")<br>(x1, x2) | Return (x1 <= x2) element-wise. |
| [`greater`](https://numpy.org/doc/stable/reference/generated/numpy.char.greater.html#numpy.char.greater "numpy.char.greater")<br>(x1, x2) | Return (x1 > x2) element-wise. |
| [`less`](https://numpy.org/doc/stable/reference/generated/numpy.char.less.html#numpy.char.less "numpy.char.less")<br>(x1, x2) | Return (x1 < x2) element-wise. |
| [`compare_chararrays`](https://numpy.org/doc/stable/reference/generated/numpy.char.compare_chararrays.html#numpy.char.compare_chararrays "numpy.char.compare_chararrays")<br>(a1, a2, cmp, rstrip) | Performs element-wise comparison of two string arrays using the comparison operator specified by _cmp_. |

String information[#](https://numpy.org/doc/stable/reference/routines.char.html#string-information "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`count`](https://numpy.org/doc/stable/reference/generated/numpy.char.count.html#numpy.char.count "numpy.char.count")<br>(a, sub\[, start, end\]) | Returns an array with the number of non-overlapping occurrences of substring `sub` in the range \[`start`, `end`). |\
| [`endswith`](https://numpy.org/doc/stable/reference/generated/numpy.char.endswith.html#numpy.char.endswith "numpy.char.endswith")<br>(a, suffix\[, start, end\]) | Returns a boolean array which is _True_ where the string element in `a` ends with `suffix`, otherwise _False_. |\
| [`find`](https://numpy.org/doc/stable/reference/generated/numpy.char.find.html#numpy.char.find "numpy.char.find")<br>(a, sub\[, start, end\]) | For each element, return the lowest index in the string where substring `sub` is found, such that `sub` is contained in the range \[`start`, `end`). |\
| [`index`](https://numpy.org/doc/stable/reference/generated/numpy.char.index.html#numpy.char.index "numpy.char.index")<br>(a, sub\[, start, end\]) | Like [`find`](https://numpy.org/doc/stable/reference/generated/numpy.char.find.html#numpy.char.find "numpy.char.find")<br>, but raises [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)")<br> when the substring is not found. |\
| [`isalpha`](https://numpy.org/doc/stable/reference/generated/numpy.char.isalpha.html#numpy.char.isalpha "numpy.char.isalpha")<br>(x, /\[, out, where, casting, order, ...\]) | Returns true for each element if all characters in the data interpreted as a string are alphabetic and there is at least one character, false otherwise. |\
| [`isalnum`](https://numpy.org/doc/stable/reference/generated/numpy.char.isalnum.html#numpy.char.isalnum "numpy.char.isalnum")<br>(x, /\[, out, where, casting, order, ...\]) | Returns true for each element if all characters in the string are alphanumeric and there is at least one character, false otherwise. |\
| [`isdecimal`](https://numpy.org/doc/stable/reference/generated/numpy.char.isdecimal.html#numpy.char.isdecimal "numpy.char.isdecimal")<br>(x, /\[, out, where, casting, ...\]) | For each element, return True if there are only decimal characters in the element. |\
| [`isdigit`](https://numpy.org/doc/stable/reference/generated/numpy.char.isdigit.html#numpy.char.isdigit "numpy.char.isdigit")<br>(x, /\[, out, where, casting, order, ...\]) | Returns true for each element if all characters in the string are digits and there is at least one character, false otherwise. |\
| [`islower`](https://numpy.org/doc/stable/reference/generated/numpy.char.islower.html#numpy.char.islower "numpy.char.islower")<br>(x, /\[, out, where, casting, order, ...\]) | Returns true for each element if all cased characters in the string are lowercase and there is at least one cased character, false otherwise. |\
| [`isnumeric`](https://numpy.org/doc/stable/reference/generated/numpy.char.isnumeric.html#numpy.char.isnumeric "numpy.char.isnumeric")<br>(x, /\[, out, where, casting, ...\]) | For each element, return True if there are only numeric characters in the element. |\
| [`isspace`](https://numpy.org/doc/stable/reference/generated/numpy.char.isspace.html#numpy.char.isspace "numpy.char.isspace")<br>(x, /\[, out, where, casting, order, ...\]) | Returns true for each element if there are only whitespace characters in the string and there is at least one character, false otherwise. |\
| [`istitle`](https://numpy.org/doc/stable/reference/generated/numpy.char.istitle.html#numpy.char.istitle "numpy.char.istitle")<br>(x, /\[, out, where, casting, order, ...\]) | Returns true for each element if the element is a titlecased string and there is at least one character, false otherwise. |\
| [`isupper`](https://numpy.org/doc/stable/reference/generated/numpy.char.isupper.html#numpy.char.isupper "numpy.char.isupper")<br>(x, /\[, out, where, casting, order, ...\]) | Return true for each element if all cased characters in the string are uppercase and there is at least one character, false otherwise. |\
| [`rfind`](https://numpy.org/doc/stable/reference/generated/numpy.char.rfind.html#numpy.char.rfind "numpy.char.rfind")<br>(a, sub\[, start, end\]) | For each element, return the highest index in the string where substring `sub` is found, such that `sub` is contained in the range \[`start`, `end`). |\
| [`rindex`](https://numpy.org/doc/stable/reference/generated/numpy.char.rindex.html#numpy.char.rindex "numpy.char.rindex")<br>(a, sub\[, start, end\]) | Like [`rfind`](https://numpy.org/doc/stable/reference/generated/numpy.char.rfind.html#numpy.char.rfind "numpy.char.rfind")<br>, but raises [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)")<br> when the substring _sub_ is not found. |\
| [`startswith`](https://numpy.org/doc/stable/reference/generated/numpy.char.startswith.html#numpy.char.startswith "numpy.char.startswith")<br>(a, prefix\[, start, end\]) | Returns a boolean array which is _True_ where the string element in `a` starts with `prefix`, otherwise _False_. |\
| [`str_len`](https://numpy.org/doc/stable/reference/generated/numpy.char.str_len.html#numpy.char.str_len "numpy.char.str_len")<br>(x, /\[, out, where, casting, order, ...\]) | Returns the length of each element. |\
\
Convenience class[#](https://numpy.org/doc/stable/reference/routines.char.html#convenience-class "Link to this heading")\
\
-------------------------------------------------------------------------------------------------------------------------\
\
|     |     |\
| --- | --- |\
| [`array`](https://numpy.org/doc/stable/reference/generated/numpy.char.array.html#numpy.char.array "numpy.char.array")<br>(obj\[, itemsize, copy, unicode, order\]) | Create a [`chararray`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.html#numpy.char.chararray "numpy.char.chararray")<br>. |\
| [`asarray`](https://numpy.org/doc/stable/reference/generated/numpy.char.asarray.html#numpy.char.asarray "numpy.char.asarray")<br>(obj\[, itemsize, unicode, order\]) | Convert the input to a [`chararray`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.html#numpy.char.chararray "numpy.char.chararray")<br>, copying the data only if necessary. |\
| [`chararray`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.html#numpy.char.chararray "numpy.char.chararray")<br>(shape\[, itemsize, unicode, ...\]) | Provides a convenient view on arrays of string and unicode values. |\
\
On this page