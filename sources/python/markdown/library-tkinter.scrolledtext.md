### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/tkinter.dnd.html "tkinter.dnd — Drag and drop support")
     |
*   [previous](https://docs.python.org/3/library/tkinter.messagebox.html "tkinter.messagebox — Tkinter message prompts")
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
*   [`tkinter.scrolledtext` — Scrolled text widget](https://docs.python.org/3/library/tkinter.scrolledtext.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`tkinter.scrolledtext` — Scrolled text widget[¶](https://docs.python.org/3/library/tkinter.scrolledtext.html#module-tkinter.scrolledtext "Link to this heading")

=================================================================================================================================================================

**Source code:** [Lib/tkinter/scrolledtext.py](https://github.com/python/cpython/tree/3.15/Lib/tkinter/scrolledtext.py)

* * *

The `tkinter.scrolledtext` module provides a class of the same name which implements a basic text widget which has a vertical scroll bar configured to do the “right thing.” Using the [`ScrolledText`](https://docs.python.org/3/library/tkinter.scrolledtext.html#tkinter.scrolledtext.ScrolledText "tkinter.scrolledtext.ScrolledText")
 class is a lot easier than setting up a text widget and scroll bar directly.

The text widget and scrollbar are packed together in a [`Frame`](https://docs.python.org/3/library/tkinter.html#tkinter.Frame "tkinter.Frame")
, and the methods of the [`Pack`](https://docs.python.org/3/library/tkinter.html#tkinter.Pack "tkinter.Pack")
, [`Grid`](https://docs.python.org/3/library/tkinter.html#tkinter.Grid "tkinter.Grid")
 and [`Place`](https://docs.python.org/3/library/tkinter.html#tkinter.Place "tkinter.Place")
 geometry managers are acquired from the `Frame` object. This allows the [`ScrolledText`](https://docs.python.org/3/library/tkinter.scrolledtext.html#tkinter.scrolledtext.ScrolledText "tkinter.scrolledtext.ScrolledText")
 widget to be used directly to achieve most normal geometry management behavior.

Should more specific control be necessary, the following attributes are available:

class tkinter.scrolledtext.ScrolledText(_master\=None_, _\*\*kw_)[¶](https://docs.python.org/3/library/tkinter.scrolledtext.html#tkinter.scrolledtext.ScrolledText "Link to this definition")

frame[¶](https://docs.python.org/3/library/tkinter.scrolledtext.html#tkinter.scrolledtext.ScrolledText.frame "Link to this definition")

The frame which surrounds the text and scroll bar widgets.

vbar[¶](https://docs.python.org/3/library/tkinter.scrolledtext.html#tkinter.scrolledtext.ScrolledText.vbar "Link to this definition")

The scroll bar widget.

#### Previous topic

[`tkinter.messagebox` — Tkinter message prompts](https://docs.python.org/3/library/tkinter.messagebox.html "previous chapter")

#### Next topic

[`tkinter.dnd` — Drag and drop support](https://docs.python.org/3/library/tkinter.dnd.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=tkinter.scrolledtext+%E2%80%94+Scrolled+text+widget&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ftkinter.scrolledtext.html&pagesource=library%2Ftkinter.scrolledtext.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/tkinter.scrolledtext.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/tkinter.dnd.html "tkinter.dnd — Drag and drop support")
     |
*   [previous](https://docs.python.org/3/library/tkinter.messagebox.html "tkinter.messagebox — Tkinter message prompts")
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
*   [`tkinter.scrolledtext` — Scrolled text widget](https://docs.python.org/3/library/tkinter.scrolledtext.html)
    
*    
    
    |
*   Theme Auto Light Dark |