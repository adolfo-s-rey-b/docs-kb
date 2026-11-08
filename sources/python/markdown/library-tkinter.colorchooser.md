### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/tkinter.font.html "tkinter.font — Tkinter font wrapper")
     |
*   [previous](https://docs.python.org/3/library/tkinter.html "tkinter — Python interface to Tcl/Tk")
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
*   [`tkinter.colorchooser` — Color choosing dialog](https://docs.python.org/3/library/tkinter.colorchooser.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`tkinter.colorchooser` — Color choosing dialog[¶](https://docs.python.org/3/library/tkinter.colorchooser.html#module-tkinter.colorchooser "Link to this heading")

==================================================================================================================================================================

**Source code:** [Lib/tkinter/colorchooser.py](https://github.com/python/cpython/tree/3.15/Lib/tkinter/colorchooser.py)

* * *

The `tkinter.colorchooser` module provides the [`Chooser`](https://docs.python.org/3/library/tkinter.colorchooser.html#tkinter.colorchooser.Chooser "tkinter.colorchooser.Chooser")
 class as an interface to the native color picker dialog. `Chooser` implements a modal color choosing dialog window. The `Chooser` class inherits from the [`Dialog`](https://docs.python.org/3/library/dialog.html#tkinter.commondialog.Dialog "tkinter.commondialog.Dialog")
 class.

class tkinter.colorchooser.Chooser(_master\=None_, _\*\*options_)[¶](https://docs.python.org/3/library/tkinter.colorchooser.html#tkinter.colorchooser.Chooser "Link to this definition")

The class implementing the modal color-choosing dialog. Most applications use the [`askcolor()`](https://docs.python.org/3/library/tkinter.colorchooser.html#tkinter.colorchooser.askcolor "tkinter.colorchooser.askcolor")
 convenience function rather than instantiating this class directly.

tkinter.colorchooser.askcolor(_color\=None_, _\*\*options_)[¶](https://docs.python.org/3/library/tkinter.colorchooser.html#tkinter.colorchooser.askcolor "Link to this definition")

Show a modal color-choosing dialog and return the chosen color. _color_ is the color selected when the dialog opens. The return value is a tuple `((r, g, b), hexstr)`, where `r`, `g` and `b` are the red, green and blue components as integers in the range 0–255 and _hexstr_ is the equivalent Tk color string, such as `'#ff8000'`. If the user cancels the dialog, `(None, None)` is returned.

Changed in version 3.10: The RGB values in the returned color are now integers in the range 0–255 instead of floats.

See also

Module [`tkinter.commondialog`](https://docs.python.org/3/library/dialog.html#module-tkinter.commondialog "tkinter.commondialog: Tkinter base class for dialogs")

Tkinter standard dialog module

#### Previous topic

[`tkinter` — Python interface to Tcl/Tk](https://docs.python.org/3/library/tkinter.html "previous chapter")

#### Next topic

[`tkinter.font` — Tkinter font wrapper](https://docs.python.org/3/library/tkinter.font.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=tkinter.colorchooser+%E2%80%94+Color+choosing+dialog&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ftkinter.colorchooser.html&pagesource=library%2Ftkinter.colorchooser.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/tkinter.colorchooser.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/tkinter.font.html "tkinter.font — Tkinter font wrapper")
     |
*   [previous](https://docs.python.org/3/library/tkinter.html "tkinter — Python interface to Tcl/Tk")
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
*   [`tkinter.colorchooser` — Color choosing dialog](https://docs.python.org/3/library/tkinter.colorchooser.html)
    
*    
    
    |
*   Theme Auto Light Dark |