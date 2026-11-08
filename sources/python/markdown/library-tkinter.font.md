### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/dialog.html "Tkinter dialogs")
     |
*   [previous](https://docs.python.org/3/library/tkinter.colorchooser.html "tkinter.colorchooser — Color choosing dialog")
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
*   [Graphical user interfaces with Tk](https://docs.python.org/3/library/tk.html)
     »
*   [`tkinter.font` — Tkinter font wrapper](https://docs.python.org/3/library/tkinter.font.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`tkinter.font` — Tkinter font wrapper[¶](https://docs.python.org/3/library/tkinter.font.html#module-tkinter.font "Link to this heading")

=========================================================================================================================================

**Source code:** [Lib/tkinter/font.py](https://github.com/python/cpython/tree/3.15/Lib/tkinter/font.py)

* * *

The `tkinter.font` module provides the [`Font`](https://docs.python.org/3/library/tkinter.font.html#tkinter.font.Font "tkinter.font.Font")
 class for creating and using named fonts.

The different font weights and slants are:

tkinter.font.NORMAL[¶](https://docs.python.org/3/library/tkinter.font.html#tkinter.font.NORMAL "Link to this definition")

tkinter.font.BOLD[¶](https://docs.python.org/3/library/tkinter.font.html#tkinter.font.BOLD "Link to this definition")

tkinter.font.ITALIC[¶](https://docs.python.org/3/library/tkinter.font.html#tkinter.font.ITALIC "Link to this definition")

tkinter.font.ROMAN[¶](https://docs.python.org/3/library/tkinter.font.html#tkinter.font.ROMAN "Link to this definition")

class tkinter.font.Font(_root\=None_, _font\=None_, _name\=None_, _exists\=False_, _\*\*options_)[¶](https://docs.python.org/3/library/tkinter.font.html#tkinter.font.Font "Link to this definition")

The `Font` class represents a named font. _Font_ instances are given unique names and can be specified by their family, size, and style configuration. Named fonts are Tk’s method of creating and identifying fonts as a single object, rather than specifying a font by its attributes with each occurrence.

Changed in version 3.10: Two fonts now compare equal (`==`) only when both are `Font` instances with the same name belonging to the same Tcl interpreter.

arguments:

> _font_ - font specifier tuple (family, size, options)
> 
> _name_ - unique font name
> 
> _exists_ - self points to existing named font if true

additional keyword options (ignored if _font_ is specified):

> _family_ - font family, for example, Courier, Times
> 
> _size_ - font size
> 
> If _size_ is positive it is interpreted as size in points.
> 
> If _size_ is a negative number its absolute value is treated
> 
> as size in pixels.
> 
> _weight_ - font emphasis (NORMAL, BOLD)
> 
> _slant_ - ROMAN, ITALIC
> 
> _underline_ - font underlining (0 - none, 1 - underline)
> 
> _overstrike_ - font strikeout (0 - none, 1 - strikeout)

actual(_option\=None_, _displayof\=None_)[¶](https://docs.python.org/3/library/tkinter.font.html#tkinter.font.Font.actual "Link to this definition")

Return the actual attributes of the font, which may differ from the requested ones because of platform limitations. With no _option_, return a dictionary of all the attributes; if _option_ is given, return the value of that single attribute. The attributes are resolved on the display of the _displayof_ widget, or the main application window if it is not specified.

cget(_option_)[¶](https://docs.python.org/3/library/tkinter.font.html#tkinter.font.Font.cget "Link to this definition")

Retrieve an attribute of the font.

configure(_\*\*options_)[¶](https://docs.python.org/3/library/tkinter.font.html#tkinter.font.Font.configure "Link to this definition")

Modify one or more attributes of the font. With no arguments, return a dictionary of the current attributes.

[`config()`](https://docs.python.org/3/library/tkinter.font.html#tkinter.font.Font.config "tkinter.font.Font.config")
 is an alias of `configure()`.

copy()[¶](https://docs.python.org/3/library/tkinter.font.html#tkinter.font.Font.copy "Link to this definition")

Return a distinct copy of the current font: a new named font with the same attributes but a different name, which can be reconfigured independently of the original. If the current font wraps a font description, the copy is instead a named font with its resolved attributes.

measure(_text_, _displayof\=None_)[¶](https://docs.python.org/3/library/tkinter.font.html#tkinter.font.Font.measure "Link to this definition")

Return amount of space the text would occupy on the specified display when formatted in the current font, as an integer number of pixels. If no display is specified then the main application window is assumed.

metrics(_\*options_, _\*\*kw_)[¶](https://docs.python.org/3/library/tkinter.font.html#tkinter.font.Font.metrics "Link to this definition")

Return font-specific data. With no options, return a dictionary mapping each metric name to its integer value; if one option name is given, return that metric’s value as an integer. Options include:

_ascent_ - distance between baseline and highest point that a character of the font can occupy

_descent_ - distance between baseline and lowest point that a character of the font can occupy

_linespace_ - minimum vertical separation necessary between any two characters of the font that ensures no vertical overlap between lines.

_fixed_ - 1 if font is fixed-width else 0

tkinter.font.families(_root\=None_, _displayof\=None_)[¶](https://docs.python.org/3/library/tkinter.font.html#tkinter.font.families "Link to this definition")

Return a tuple of the names of the available font families.

tkinter.font.names(_root\=None_)[¶](https://docs.python.org/3/library/tkinter.font.html#tkinter.font.names "Link to this definition")

Return a tuple of the names of all the defined fonts.

tkinter.font.nametofont(_name_, _root\=None_)[¶](https://docs.python.org/3/library/tkinter.font.html#tkinter.font.nametofont "Link to this definition")

Return a [`Font`](https://docs.python.org/3/library/tkinter.font.html#tkinter.font.Font "tkinter.font.Font")
 representation of the existing named font _name_. _root_ is the widget whose Tcl interpreter owns the font; if omitted, the default root window is used.

Changed in version 3.10: The _root_ parameter was added.

#### Previous topic

[`tkinter.colorchooser` — Color choosing dialog](https://docs.python.org/3/library/tkinter.colorchooser.html "previous chapter")

#### Next topic

[Tkinter dialogs](https://docs.python.org/3/library/dialog.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=tkinter.font+%E2%80%94+Tkinter+font+wrapper&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ftkinter.font.html&pagesource=library%2Ftkinter.font.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/tkinter.font.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/dialog.html "Tkinter dialogs")
     |
*   [previous](https://docs.python.org/3/library/tkinter.colorchooser.html "tkinter.colorchooser — Color choosing dialog")
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
*   [Graphical user interfaces with Tk](https://docs.python.org/3/library/tk.html)
     »
*   [`tkinter.font` — Tkinter font wrapper](https://docs.python.org/3/library/tkinter.font.html)
    
*    
    
    |
*   Theme Auto Light Dark |