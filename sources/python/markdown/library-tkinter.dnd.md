### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/tkinter.ttk.html "tkinter.ttk — Tk themed widgets")
     |
*   [previous](https://docs.python.org/3/library/tkinter.scrolledtext.html "tkinter.scrolledtext — Scrolled text widget")
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
*   [`tkinter.dnd` — Drag and drop support](https://docs.python.org/3/library/tkinter.dnd.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`tkinter.dnd` — Drag and drop support[¶](https://docs.python.org/3/library/tkinter.dnd.html#module-tkinter.dnd "Link to this heading")

=======================================================================================================================================

**Source code:** [Lib/tkinter/dnd.py](https://github.com/python/cpython/tree/3.15/Lib/tkinter/dnd.py)

* * *

Note

This is experimental and due to be deprecated when it is replaced with the Tk DND.

The `tkinter.dnd` module provides drag-and-drop support for objects within a single application, within the same window or between windows. To enable an object to be dragged, you must create an event binding for it that starts the drag-and-drop process. Typically, you bind a ButtonPress event to a callback function that you write (see [Bindings and events](https://docs.python.org/3/library/tkinter.html#bindings-and-events)
). The function should call [`dnd_start()`](https://docs.python.org/3/library/tkinter.dnd.html#tkinter.dnd.dnd_start "tkinter.dnd.dnd_start")
, where _source_ is the object to be dragged, and _event_ is the event that invoked the call (the argument to your callback function).

Selection of a target object occurs as follows:

1.  Top-down search of the area under the mouse for a target widget:
    
    *   the target widget should have a callable _dnd\_accept_ attribute;
        
    *   if _dnd\_accept_ is not present or returns `None`, the search moves to the parent widget;
        
    *   if no target widget is found, the target object is `None`.
        
2.  Call to `<old_target>.dnd_leave(source, event)`.
    
3.  Call to `<new_target>.dnd_enter(source, event)`.
    
4.  Call to `<target>.dnd_commit(source, event)` to notify of the drop.
    
5.  Call to `<source>.dnd_end(target, event)` to signal the end of drag-and-drop.
    

class tkinter.dnd.DndHandler(_source_, _event_)[¶](https://docs.python.org/3/library/tkinter.dnd.html#tkinter.dnd.DndHandler "Link to this definition")

The _DndHandler_ class handles drag-and-drop events tracking Motion and ButtonRelease events on the root of the event widget.

cancel(_event\=None_)[¶](https://docs.python.org/3/library/tkinter.dnd.html#tkinter.dnd.DndHandler.cancel "Link to this definition")

Cancel the drag-and-drop process.

finish(_event_, _commit\=0_)[¶](https://docs.python.org/3/library/tkinter.dnd.html#tkinter.dnd.DndHandler.finish "Link to this definition")

Execute end of drag-and-drop functions.

on\_motion(_event_)[¶](https://docs.python.org/3/library/tkinter.dnd.html#tkinter.dnd.DndHandler.on_motion "Link to this definition")

Inspect area below mouse for target objects while a drag is performed.

on\_release(_event_)[¶](https://docs.python.org/3/library/tkinter.dnd.html#tkinter.dnd.DndHandler.on_release "Link to this definition")

Signal end of drag when the release pattern is triggered.

tkinter.dnd.dnd\_start(_source_, _event_)[¶](https://docs.python.org/3/library/tkinter.dnd.html#tkinter.dnd.dnd_start "Link to this definition")

Factory function for the drag-and-drop process. Return the [`DndHandler`](https://docs.python.org/3/library/tkinter.dnd.html#tkinter.dnd.DndHandler "tkinter.dnd.DndHandler")
 instance managing the drag, or `None` if a drag could not be started.

See also

[Bindings and events](https://docs.python.org/3/library/tkinter.html#bindings-and-events)

#### Previous topic

[`tkinter.scrolledtext` — Scrolled text widget](https://docs.python.org/3/library/tkinter.scrolledtext.html "previous chapter")

#### Next topic

[`tkinter.ttk` — Tk themed widgets](https://docs.python.org/3/library/tkinter.ttk.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=tkinter.dnd+%E2%80%94+Drag+and+drop+support&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ftkinter.dnd.html&pagesource=library%2Ftkinter.dnd.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/tkinter.dnd.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/tkinter.ttk.html "tkinter.ttk — Tk themed widgets")
     |
*   [previous](https://docs.python.org/3/library/tkinter.scrolledtext.html "tkinter.scrolledtext — Scrolled text widget")
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
*   [`tkinter.dnd` — Drag and drop support](https://docs.python.org/3/library/tkinter.dnd.html)
    
*    
    
    |
*   Theme Auto Light Dark |