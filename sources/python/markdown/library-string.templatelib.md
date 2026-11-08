### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/re.html "re — Regular expression operations")
     |
*   [previous](https://docs.python.org/3/library/string.html "string — Common string operations")
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
*   [Text Processing Services](https://docs.python.org/3/library/text.html)
     »
*   [`string.templatelib` — Support for template string literals](https://docs.python.org/3/library/string.templatelib.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`string.templatelib` — Support for template string literals[¶](https://docs.python.org/3/library/string.templatelib.html#module-string.templatelib "Link to this heading")

===========================================================================================================================================================================

**Source code:** [Lib/string/templatelib.py](https://github.com/python/cpython/tree/3.15/Lib/string/templatelib.py)

* * *

See also

*   [Format strings](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)
    
*   [Template string literal (t-string) syntax](https://docs.python.org/3/reference/lexical_analysis.html#t-strings)
    
*   [**PEP 750**](https://peps.python.org/pep-0750/)
    

Template strings[¶](https://docs.python.org/3/library/string.templatelib.html#template-strings "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

Added in version 3.14.

Template strings are a mechanism for custom string processing. They have the full flexibility of Python’s [f-strings](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)
, but return a [`Template`](https://docs.python.org/3/library/string.templatelib.html#string.templatelib.Template "string.templatelib.Template")
 instance that gives access to the static and interpolated (in curly brackets) parts of a string _before_ they are combined.

To write a t-string, use a `'t'` prefix instead of an `'f'`, like so:

Copy

\>>> pi \= 3.14
\>>> t't-strings are new in Python {pi!s}!'
Template(
   strings=('t-strings are new in Python ', '!'),
   interpolations=(Interpolation(3.14, 'pi', 's', ''),)
)

Types[¶](https://docs.python.org/3/library/string.templatelib.html#types "Link to this heading")

-------------------------------------------------------------------------------------------------

class string.templatelib.Template[¶](https://docs.python.org/3/library/string.templatelib.html#string.templatelib.Template "Link to this definition")

The `Template` class describes the contents of a template string. It is immutable, meaning that attributes of a template cannot be reassigned.

The most common way to create a `Template` instance is to use the [template string literal syntax](https://docs.python.org/3/reference/lexical_analysis.html#t-strings)
. This syntax is identical to that of [f-strings](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)
, except that it uses a `t` prefix in place of an `f`:

Copy

\>>> cheese \= 'Red Leicester'
\>>> template \= t"We're fresh out of {cheese}, sir."
\>>> type(template)
<class 'string.templatelib.Template'>

Templates are stored as sequences of literal [`strings`](https://docs.python.org/3/library/string.templatelib.html#string.templatelib.Template.strings "string.templatelib.Template.strings")
 and dynamic [`interpolations`](https://docs.python.org/3/library/string.templatelib.html#string.templatelib.Template.interpolations "string.templatelib.Template.interpolations")
. A [`values`](https://docs.python.org/3/library/string.templatelib.html#string.templatelib.Template.values "string.templatelib.Template.values")
 attribute holds the values of the interpolations:

Copy

\>>> cheese \= 'Camembert'
\>>> template \= t'Ah! We do have {cheese}.'
\>>> template.strings
('Ah! We do have ', '.')
\>>> template.interpolations
(Interpolation('Camembert', ...),)
\>>> template.values
('Camembert',)

The `strings` tuple has one more element than `interpolations` and `values`; the interpolations “belong” between the strings. This may be easier to understand when tuples are aligned

Copy

template.strings:  ('Ah! We do have ',              '.')
template.values:   (                   'Camembert',    )

Attributes

strings: [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "str")\
, ...\][¶](https://docs.python.org/3/library/string.templatelib.html#string.templatelib.Template.strings "Link to this definition")

A [`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")
 of the static strings in the template.

Copy

\>>> cheese \= 'Camembert'
\>>> template \= t'Ah! We do have {cheese}.'
\>>> template.strings
('Ah! We do have ', '.')

Empty strings _are_ included in the tuple:

Copy

\>>> response \= 'We do have '
\>>> cheese \= 'Camembert'
\>>> template \= t'Ah! {response}{cheese}.'
\>>> template.strings
('Ah! ', '', '.')

The `strings` tuple is never empty, and always contains one more string than the `interpolations` and `values` tuples:

Copy

\>>> t''.strings
('',)
\>>> t''.values
()
\>>> t'{'cheese'}'.strings
('', '')
\>>> t'{'cheese'}'.values
('cheese',)

interpolations: [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")
\[[Interpolation](https://docs.python.org/3/library/string.templatelib.html#string.templatelib.Interpolation "string.templatelib.Interpolation")\
, ...\][¶](https://docs.python.org/3/library/string.templatelib.html#string.templatelib.Template.interpolations "Link to this definition")

A [`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")
 of the interpolations in the template.

Copy

\>>> cheese \= 'Camembert'
\>>> template \= t'Ah! We do have {cheese}.'
\>>> template.interpolations
(Interpolation('Camembert', 'cheese', None, ''),)

The `interpolations` tuple may be empty and always contains one fewer values than the `strings` tuple:

Copy

\>>> t'Red Leicester'.interpolations
()

values: [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")
\[[object](https://docs.python.org/3/builtins/functions.html#object "object")\
, ...\][¶](https://docs.python.org/3/library/string.templatelib.html#string.templatelib.Template.values "Link to this definition")

A tuple of all interpolated values in the template.

Copy

\>>> cheese \= 'Camembert'
\>>> template \= t'Ah! We do have {cheese}.'
\>>> template.values
('Camembert',)

The `values` tuple always has the same length as the `interpolations` tuple. It is always equivalent to `tuple(i.value for i in template.interpolations)`.

Methods

\_\_new\_\_(_\*args: [str](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 | [Interpolation](https://docs.python.org/3/library/string.templatelib.html#string.templatelib.Interpolation "string.templatelib.Interpolation")
_)[¶](https://docs.python.org/3/library/string.templatelib.html#string.templatelib.Template.__new__ "Link to this definition")

While literal syntax is the most common way to create a `Template`, it is also possible to create them directly using the constructor:

Copy

\>>> from string.templatelib import Interpolation, Template
\>>> cheese \= 'Camembert'
\>>> template \= Template(
...     'Ah! We do have ', Interpolation(cheese, 'cheese'), '.'
... )
\>>> list(template)
\['Ah! We do have ', Interpolation('Camembert', 'cheese', None, ''), '.'\]

If multiple strings are passed consecutively, they will be concatenated into a single value in the [`strings`](https://docs.python.org/3/library/string.templatelib.html#string.templatelib.Template.strings "string.templatelib.Template.strings")
 attribute. For example, the following code creates a `Template` with a single final string:

Copy

\>>> from string.templatelib import Template
\>>> template \= Template('Ah! We do have ', 'Camembert', '.')
\>>> template.strings
('Ah! We do have Camembert.',)

If multiple interpolations are passed consecutively, they will be treated as separate interpolations and an empty string will be inserted between them. For example, the following code creates a template with empty placeholders in the [`strings`](https://docs.python.org/3/library/string.templatelib.html#string.templatelib.Template.strings "string.templatelib.Template.strings")
 attribute:

Copy

\>>> from string.templatelib import Interpolation, Template
\>>> template \= Template(
...     Interpolation('Camembert', 'cheese'),
...     Interpolation('.', 'punctuation'),
... )
\>>> template.strings
('', '', '')

iter(template)

Iterate over the template, yielding each non-empty string and [`Interpolation`](https://docs.python.org/3/library/string.templatelib.html#string.templatelib.Interpolation "string.templatelib.Interpolation")
 in the correct order:

Copy

\>>> cheese \= 'Camembert'
\>>> list(t'Ah! We do have {cheese}.')
\['Ah! We do have ', Interpolation('Camembert', 'cheese', None, ''), '.'\]

Caution

Empty strings are **not** included in the iteration:

Copy

\>>> response \= 'We do have '
\>>> cheese \= 'Camembert'
\>>> list(t'Ah! {response}{cheese}.')
\['Ah! ',\
 Interpolation('We do have ', 'response', None, ''),\
 Interpolation('Camembert', 'cheese', None, ''),\
 '.'\]

template + other

template += other

Concatenate this template with another, returning a new `Template` instance:

Copy

\>>> cheese \= 'Camembert'
\>>> list(t'Ah! ' + t'We do have {cheese}.')
\['Ah! We do have ', Interpolation('Camembert', 'cheese', None, ''), '.'\]

Concatenating a `Template` and a `str` is **not** supported. This is because it is unclear whether the string should be treated as a static string or an interpolation. If you want to concatenate a `Template` with a string, you should either wrap the string directly in a `Template` (to treat it as a static string) or use an `Interpolation` (to treat it as dynamic):

Copy

\>>> from string.templatelib import Interpolation, Template
\>>> template \= t'Ah! '
\>>> \# Treat 'We do have ' as a static string
\>>> template += Template('We do have ')
\>>> \# Treat cheese as an interpolation
\>>> cheese \= 'Camembert'
\>>> template += Template(Interpolation(cheese, 'cheese'))
\>>> list(template)
\['Ah! We do have ', Interpolation('Camembert', 'cheese', None, '')\]

class string.templatelib.Interpolation[¶](https://docs.python.org/3/library/string.templatelib.html#string.templatelib.Interpolation "Link to this definition")

The `Interpolation` type represents an expression inside a template string. It is immutable, meaning that attributes of an interpolation cannot be reassigned.

Interpolations support pattern matching, allowing you to match against their attributes with the [match statement](https://docs.python.org/3/reference/compound_stmts.html#match)
:

Copy

\>>> from string.templatelib import Interpolation
\>>> interpolation \= t'{1. + 2.:.2f}'.interpolations\[0\]
\>>> interpolation
Interpolation(3.0, '1. + 2.', None, '.2f')
\>>> match interpolation:
...     case Interpolation(value, expression, conversion, format\_spec):
...         print(value, expression, conversion, format\_spec, sep\=' | ')
...
3.0 | 1. + 2. | None | .2f

Interpolations are [generic](https://docs.python.org/3/library/typing.html#generics)
 over the types of their values.

Attributes

value: [object](https://docs.python.org/3/builtins/functions.html#object "object")
[¶](https://docs.python.org/3/library/string.templatelib.html#string.templatelib.Interpolation.value "Link to this definition")

The evaluated value of the interpolation.

Copy

\>>> t'{1 + 2}'.interpolations\[0\].value
3

expression: [str](https://docs.python.org/3/builtins/stdtypes.html#str "str")
[¶](https://docs.python.org/3/library/string.templatelib.html#string.templatelib.Interpolation.expression "Link to this definition")

For interpolations created by t-string literals, `expression` is the expression text found inside the curly brackets (`{` & `}`), including any whitespace, excluding the curly brackets themselves, and ending before the first `!`, `:`, or `=` if any is present. For manually created interpolations, `expression` is the arbitrary string provided when constructing the interpolation instance.

We recommend using valid Python expressions or the empty string for the `expression` field of manually created `Interpolation` instances, although this is not enforced at runtime.

Copy

\>>> t'{1 + 2}'.interpolations\[0\].expression
'1 + 2'

conversion: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")
\['a', 'r', 's'\] | [None](https://docs.python.org/3/builtins/constants.html#None "None")
[¶](https://docs.python.org/3/library/string.templatelib.html#string.templatelib.Interpolation.conversion "Link to this definition")

The conversion to apply to the value, or `None`.

The `conversion` is the optional conversion to apply to the value:

Copy

\>>> t'{1 + 2!a}'.interpolations\[0\].conversion
'a'

Note

Unlike f-strings, where conversions are applied automatically, the expected behavior with t-strings is that code that _processes_ the `Template` will decide how to interpret and whether to apply the `conversion`. For convenience, the [`convert()`](https://docs.python.org/3/library/string.templatelib.html#string.templatelib.convert "string.templatelib.convert")
 function can be used to mimic f-string conversion semantics.

format\_spec: [str](https://docs.python.org/3/builtins/stdtypes.html#str "str")
[¶](https://docs.python.org/3/library/string.templatelib.html#string.templatelib.Interpolation.format_spec "Link to this definition")

The format specification to apply to the value.

The `format_spec` is an optional, arbitrary string used as the format specification to present the value:

Copy

\>>> t'{1 + 2:.2f}'.interpolations\[0\].format\_spec
'.2f'

Note

Unlike f-strings, where format specifications are applied automatically via the [`format()`](https://docs.python.org/3/builtins/functions.html#format "format")
 protocol, the expected behavior with t-strings is that code that _processes_ the interpolation will decide how to interpret and whether to apply the format specification. As a result, `format_spec` values in interpolations can be arbitrary strings, including those that do not conform to the `format()` protocol.

Methods

\_\_new\_\_(_value: [object](https://docs.python.org/3/builtins/functions.html#object "object")
_, _expression: [str](https://docs.python.org/3/builtins/stdtypes.html#str "str")
_, _conversion: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")
\['a', 'r', 's'\] | [None](https://docs.python.org/3/builtins/constants.html#None "None")
 \= None_, _format\_spec: [str](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 \= ''_)[¶](https://docs.python.org/3/library/string.templatelib.html#string.templatelib.Interpolation.__new__ "Link to this definition")

Create a new `Interpolation` object from component parts.

Parameters:

*   **value** – The evaluated, in-scope result of the interpolation.
    
*   **expression** – The text of a valid Python expression, or an empty string.
    
*   **conversion** – The [conversion](https://docs.python.org/3/library/string.html#formatstrings)
     to be used, one of `None`, `'a'`, `'r'`, or `'s'`.
    
*   **format\_spec** – An optional, arbitrary string used as the [format specification](https://docs.python.org/3/library/string.html#formatspec)
     to present the value.
    

Helper functions[¶](https://docs.python.org/3/library/string.templatelib.html#helper-functions "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

string.templatelib.convert(_obj_, _/_, _conversion_)[¶](https://docs.python.org/3/library/string.templatelib.html#string.templatelib.convert "Link to this definition")

Applies formatted string literal [conversion](https://docs.python.org/3/library/string.html#formatstrings-conversion)
 semantics to the given object _obj_. This is frequently useful for custom template string processing logic.

Three conversion flags are currently supported:

*   `'s'` which calls [`str()`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
     on the value (like `!s`),
    
*   `'r'` which calls [`repr()`](https://docs.python.org/3/builtins/functions.html#repr "repr")
     (like `!r`), and
    
*   `'a'` which calls [`ascii()`](https://docs.python.org/3/builtins/functions.html#ascii "ascii")
     (like `!a`).
    

If the conversion flag is `None`, _obj_ is returned unchanged.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`string.templatelib` — Support for template string literals](https://docs.python.org/3/library/string.templatelib.html#)
    *   [Template strings](https://docs.python.org/3/library/string.templatelib.html#template-strings)
        
    *   [Types](https://docs.python.org/3/library/string.templatelib.html#types)
        
    *   [Helper functions](https://docs.python.org/3/library/string.templatelib.html#helper-functions)
        

#### Previous topic

[`string` — Common string operations](https://docs.python.org/3/library/string.html "previous chapter")

#### Next topic

[`re` — Regular expression operations](https://docs.python.org/3/library/re.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=string.templatelib+%E2%80%94+Support+for+template+string+literals&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fstring.templatelib.html&pagesource=library%2Fstring.templatelib.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/string.templatelib.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/re.html "re — Regular expression operations")
     |
*   [previous](https://docs.python.org/3/library/string.html "string — Common string operations")
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
*   [Text Processing Services](https://docs.python.org/3/library/text.html)
     »
*   [`string.templatelib` — Support for template string literals](https://docs.python.org/3/library/string.templatelib.html)
    
*    
    
    |
*   Theme Auto Light Dark |