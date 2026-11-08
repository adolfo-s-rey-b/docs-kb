### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/cmd.html "cmd — Support for line-oriented command interpreters")
     |
*   [previous](https://docs.python.org/3/library/curses.ascii.html "curses.ascii — Utilities for ASCII characters")
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
*   [Command-line interface libraries](https://docs.python.org/3/library/cmdlinelibs.html)
     »
*   [`curses.panel` — A panel stack extension for curses](https://docs.python.org/3/library/curses.panel.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`curses.panel` — A panel stack extension for curses[¶](https://docs.python.org/3/library/curses.panel.html#module-curses.panel "Link to this heading")

=======================================================================================================================================================

* * *

Panels are windows with the added feature of depth, so they can be stacked on top of each other, and only the visible portions of each window will be displayed. Panels can be added, moved up or down in the stack, and removed.

Functions[¶](https://docs.python.org/3/library/curses.panel.html#functions "Link to this heading")

---------------------------------------------------------------------------------------------------

The module `curses.panel` defines the following exception:

exception curses.panel.error[¶](https://docs.python.org/3/library/curses.panel.html#curses.panel.error "Link to this definition")

Exception raised when a curses panel library function returns an error.

The module `curses.panel` defines the following functions:

curses.panel.bottom\_panel()[¶](https://docs.python.org/3/library/curses.panel.html#curses.panel.bottom_panel "Link to this definition")

Returns the bottom panel in the panel stack.

curses.panel.new\_panel(_win_)[¶](https://docs.python.org/3/library/curses.panel.html#curses.panel.new_panel "Link to this definition")

Returns a panel object, associating it with the given window _win_ and placing the new panel on top of the panel stack. Be aware that you need to keep the returned panel object referenced explicitly. If you don’t, the panel object is garbage collected and removed from the panel stack.

curses.panel.top\_panel()[¶](https://docs.python.org/3/library/curses.panel.html#curses.panel.top_panel "Link to this definition")

Returns the top panel in the panel stack.

curses.panel.update\_panels()[¶](https://docs.python.org/3/library/curses.panel.html#curses.panel.update_panels "Link to this definition")

Updates the virtual screen after changes in the panel stack. This does not call [`curses.doupdate()`](https://docs.python.org/3/library/curses.html#curses.doupdate "curses.doupdate")
, so you’ll have to do this yourself.

Panel objects[¶](https://docs.python.org/3/library/curses.panel.html#panel-objects "Link to this heading")

-----------------------------------------------------------------------------------------------------------

class curses.panel.panel[¶](https://docs.python.org/3/library/curses.panel.html#curses.panel.panel "Link to this definition")

Panel objects, as returned by [`new_panel()`](https://docs.python.org/3/library/curses.panel.html#curses.panel.new_panel "curses.panel.new_panel")
 above, are windows with a stacking order. There’s always a window associated with a panel which determines the content, while the panel methods are responsible for the window’s depth in the panel stack.

Panel objects have the following methods:

panel.above()[¶](https://docs.python.org/3/library/curses.panel.html#curses.panel.panel.above "Link to this definition")

Returns the panel above the current panel.

panel.below()[¶](https://docs.python.org/3/library/curses.panel.html#curses.panel.panel.below "Link to this definition")

Returns the panel below the current panel.

panel.bottom()[¶](https://docs.python.org/3/library/curses.panel.html#curses.panel.panel.bottom "Link to this definition")

Push the panel to the bottom of the stack.

panel.hidden()[¶](https://docs.python.org/3/library/curses.panel.html#curses.panel.panel.hidden "Link to this definition")

Returns `True` if the panel is hidden (not visible), `False` otherwise.

panel.hide()[¶](https://docs.python.org/3/library/curses.panel.html#curses.panel.panel.hide "Link to this definition")

Hide the panel. This does not delete the object, it just makes the window on screen invisible.

panel.move(_y_, _x_)[¶](https://docs.python.org/3/library/curses.panel.html#curses.panel.panel.move "Link to this definition")

Move the panel to the screen coordinates `(y, x)`.

panel.replace(_win_)[¶](https://docs.python.org/3/library/curses.panel.html#curses.panel.panel.replace "Link to this definition")

Change the window associated with the panel to the window _win_.

panel.set\_userptr(_obj_)[¶](https://docs.python.org/3/library/curses.panel.html#curses.panel.panel.set_userptr "Link to this definition")

Set the panel’s user pointer to _obj_. This is used to associate an arbitrary piece of data with the panel, and can be any Python object.

panel.show()[¶](https://docs.python.org/3/library/curses.panel.html#curses.panel.panel.show "Link to this definition")

Display the panel (which might have been hidden), placing it on top of the panel stack.

panel.top()[¶](https://docs.python.org/3/library/curses.panel.html#curses.panel.panel.top "Link to this definition")

Push panel to the top of the stack.

panel.userptr()[¶](https://docs.python.org/3/library/curses.panel.html#curses.panel.panel.userptr "Link to this definition")

Returns the user pointer for the panel. This might be any Python object.

panel.window()[¶](https://docs.python.org/3/library/curses.panel.html#curses.panel.panel.window "Link to this definition")

Returns the window object associated with the panel.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`curses.panel` — A panel stack extension for curses](https://docs.python.org/3/library/curses.panel.html#)
    *   [Functions](https://docs.python.org/3/library/curses.panel.html#functions)
        
    *   [Panel objects](https://docs.python.org/3/library/curses.panel.html#panel-objects)
        

#### Previous topic

[`curses.ascii` — Utilities for ASCII characters](https://docs.python.org/3/library/curses.ascii.html "previous chapter")

#### Next topic

[`cmd` — Support for line-oriented command interpreters](https://docs.python.org/3/library/cmd.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=curses.panel+%E2%80%94+A+panel+stack+extension+for+curses&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fcurses.panel.html&pagesource=library%2Fcurses.panel.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/curses.panel.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/cmd.html "cmd — Support for line-oriented command interpreters")
     |
*   [previous](https://docs.python.org/3/library/curses.ascii.html "curses.ascii — Utilities for ASCII characters")
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
*   [Command-line interface libraries](https://docs.python.org/3/library/cmdlinelibs.html)
     »
*   [`curses.panel` — A panel stack extension for curses](https://docs.python.org/3/library/curses.panel.html)
    
*    
    
    |
*   Theme Auto Light Dark |