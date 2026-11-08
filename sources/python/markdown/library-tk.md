### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/tkinter.html "tkinter — Python interface to Tcl/Tk")
     |
*   [previous](https://docs.python.org/3/library/locale.html "locale — Internationalization services")
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
    
*    
    
    |
*   Theme Auto Light Dark |

Graphical user interfaces with Tk[¶](https://docs.python.org/3/library/tk.html#graphical-user-interfaces-with-tk "Link to this heading")

=========================================================================================================================================

Tk/Tcl has long been an integral part of Python. It provides a robust and platform independent windowing toolkit, that is available to Python programmers using the [`tkinter`](https://docs.python.org/3/library/tkinter.html#module-tkinter "tkinter: Interface to Tcl/Tk for graphical user interfaces")
 package, and its extension, the [`tkinter.ttk`](https://docs.python.org/3/library/tkinter.ttk.html#module-tkinter.ttk "tkinter.ttk: Tk themed widget set")
 module.

The [`tkinter`](https://docs.python.org/3/library/tkinter.html#module-tkinter "tkinter: Interface to Tcl/Tk for graphical user interfaces")
 package is a thin object-oriented layer on top of Tcl/Tk. To use `tkinter`, you don’t need to write Tcl code, but you will need to consult the Tk documentation, and occasionally the Tcl documentation. `tkinter` is a set of wrappers that implement the Tk widgets as Python classes.

[`tkinter`](https://docs.python.org/3/library/tkinter.html#module-tkinter "tkinter: Interface to Tcl/Tk for graphical user interfaces")
’s chief virtues are that it is fast, and that it usually comes bundled with Python. Although its standard documentation is weak, good material is available, which includes: references, tutorials, a book and others. `tkinter` is also famous for having an outdated look and feel, which has been vastly improved in Tk 8.5. Nevertheless, there are many other GUI libraries that you could be interested in. The Python wiki lists several alternative [GUI frameworks and tools](https://wiki.python.org/moin/GuiProgramming)
.

*   [`tkinter` — Python interface to Tcl/Tk](https://docs.python.org/3/library/tkinter.html)
    *   [Architecture](https://docs.python.org/3/library/tkinter.html#architecture)
        
    *   [Tkinter modules](https://docs.python.org/3/library/tkinter.html#tkinter-modules)
        
    *   [Tkinter life preserver](https://docs.python.org/3/library/tkinter.html#tkinter-life-preserver)
        *   [A Hello World program](https://docs.python.org/3/library/tkinter.html#a-hello-world-program)
            
        *   [Important Tk concepts](https://docs.python.org/3/library/tkinter.html#important-tk-concepts)
            
        *   [Understanding how Tkinter wraps Tcl/Tk](https://docs.python.org/3/library/tkinter.html#understanding-how-tkinter-wraps-tcl-tk)
            
        *   [How do I…? What option does…?](https://docs.python.org/3/library/tkinter.html#how-do-i-what-option-does)
            
        *   [Navigating the Tcl/Tk reference manual](https://docs.python.org/3/library/tkinter.html#navigating-the-tcl-tk-reference-manual)
            
    *   [Threading model](https://docs.python.org/3/library/tkinter.html#threading-model)
        
    *   [Handy reference](https://docs.python.org/3/library/tkinter.html#handy-reference)
        *   [Setting options](https://docs.python.org/3/library/tkinter.html#setting-options)
            
        *   [Geometry management](https://docs.python.org/3/library/tkinter.html#geometry-management)
            
        *   [Coupling widget variables](https://docs.python.org/3/library/tkinter.html#coupling-widget-variables)
            
        *   [The window manager](https://docs.python.org/3/library/tkinter.html#the-window-manager)
            
        *   [Tk option data types](https://docs.python.org/3/library/tkinter.html#tk-option-data-types)
            
        *   [Bindings and events](https://docs.python.org/3/library/tkinter.html#bindings-and-events)
            
        *   [The index parameter](https://docs.python.org/3/library/tkinter.html#the-index-parameter)
            
        *   [Images](https://docs.python.org/3/library/tkinter.html#images)
            
    *   [Reference](https://docs.python.org/3/library/tkinter.html#reference)
        *   [Base and mixin classes](https://docs.python.org/3/library/tkinter.html#base-and-mixin-classes)
            
        *   [Toplevel widgets](https://docs.python.org/3/library/tkinter.html#toplevel-widgets)
            
        *   [Widget classes](https://docs.python.org/3/library/tkinter.html#widget-classes)
            
        *   [Variable classes](https://docs.python.org/3/library/tkinter.html#variable-classes)
            
        *   [Image classes](https://docs.python.org/3/library/tkinter.html#image-classes)
            
        *   [Other classes](https://docs.python.org/3/library/tkinter.html#other-classes)
            
        *   [Module-level functions](https://docs.python.org/3/library/tkinter.html#module-level-functions)
            
        *   [File handlers](https://docs.python.org/3/library/tkinter.html#file-handlers)
            
        *   [Constants](https://docs.python.org/3/library/tkinter.html#constants)
            
*   [`tkinter.colorchooser` — Color choosing dialog](https://docs.python.org/3/library/tkinter.colorchooser.html)
    
*   [`tkinter.font` — Tkinter font wrapper](https://docs.python.org/3/library/tkinter.font.html)
    
*   [Tkinter dialogs](https://docs.python.org/3/library/dialog.html)
    *   [`tkinter.simpledialog` — Standard Tkinter input dialogs](https://docs.python.org/3/library/dialog.html#module-tkinter.simpledialog)
        
    *   [`tkinter.filedialog` — File selection dialogs](https://docs.python.org/3/library/dialog.html#module-tkinter.filedialog)
        *   [Native load/save dialogs](https://docs.python.org/3/library/dialog.html#native-load-save-dialogs)
            
    *   [`tkinter.commondialog` — Dialog window templates](https://docs.python.org/3/library/dialog.html#module-tkinter.commondialog)
        
    *   [`tkinter.dialog` — Classic Tk dialog boxes](https://docs.python.org/3/library/dialog.html#module-tkinter.dialog)
        
*   [`tkinter.messagebox` — Tkinter message prompts](https://docs.python.org/3/library/tkinter.messagebox.html)
    
*   [`tkinter.scrolledtext` — Scrolled text widget](https://docs.python.org/3/library/tkinter.scrolledtext.html)
    
*   [`tkinter.dnd` — Drag and drop support](https://docs.python.org/3/library/tkinter.dnd.html)
    
*   [`tkinter.ttk` — Tk themed widgets](https://docs.python.org/3/library/tkinter.ttk.html)
    *   [Using Ttk](https://docs.python.org/3/library/tkinter.ttk.html#using-ttk)
        
    *   [Ttk widgets](https://docs.python.org/3/library/tkinter.ttk.html#ttk-widgets)
        
    *   [Widget](https://docs.python.org/3/library/tkinter.ttk.html#widget)
        *   [Standard options](https://docs.python.org/3/library/tkinter.ttk.html#standard-options)
            
        *   [Scrollable widget options](https://docs.python.org/3/library/tkinter.ttk.html#scrollable-widget-options)
            
        *   [Label options](https://docs.python.org/3/library/tkinter.ttk.html#label-options)
            
        *   [Compatibility options](https://docs.python.org/3/library/tkinter.ttk.html#compatibility-options)
            
        *   [Widget states](https://docs.python.org/3/library/tkinter.ttk.html#widget-states)
            
        *   [ttk.Widget](https://docs.python.org/3/library/tkinter.ttk.html#ttk-widget)
            
    *   [Combobox](https://docs.python.org/3/library/tkinter.ttk.html#combobox)
        *   [Options](https://docs.python.org/3/library/tkinter.ttk.html#options)
            
        *   [Virtual events](https://docs.python.org/3/library/tkinter.ttk.html#virtual-events)
            
        *   [ttk.Combobox](https://docs.python.org/3/library/tkinter.ttk.html#ttk-combobox)
            
    *   [Spinbox](https://docs.python.org/3/library/tkinter.ttk.html#spinbox)
        *   [Options](https://docs.python.org/3/library/tkinter.ttk.html#id1)
            
        *   [Virtual events](https://docs.python.org/3/library/tkinter.ttk.html#id2)
            
        *   [ttk.Spinbox](https://docs.python.org/3/library/tkinter.ttk.html#ttk-spinbox)
            
    *   [Notebook](https://docs.python.org/3/library/tkinter.ttk.html#notebook)
        *   [Options](https://docs.python.org/3/library/tkinter.ttk.html#id3)
            
        *   [Tab options](https://docs.python.org/3/library/tkinter.ttk.html#tab-options)
            
        *   [Tab identifiers](https://docs.python.org/3/library/tkinter.ttk.html#tab-identifiers)
            
        *   [Virtual events](https://docs.python.org/3/library/tkinter.ttk.html#id4)
            
        *   [ttk.Notebook](https://docs.python.org/3/library/tkinter.ttk.html#ttk-notebook)
            
    *   [Progressbar](https://docs.python.org/3/library/tkinter.ttk.html#progressbar)
        *   [Options](https://docs.python.org/3/library/tkinter.ttk.html#id5)
            
        *   [ttk.Progressbar](https://docs.python.org/3/library/tkinter.ttk.html#ttk-progressbar)
            
    *   [Separator](https://docs.python.org/3/library/tkinter.ttk.html#separator)
        *   [Options](https://docs.python.org/3/library/tkinter.ttk.html#id6)
            
    *   [Sizegrip](https://docs.python.org/3/library/tkinter.ttk.html#sizegrip)
        *   [Platform-specific notes](https://docs.python.org/3/library/tkinter.ttk.html#platform-specific-notes)
            
        *   [Bugs](https://docs.python.org/3/library/tkinter.ttk.html#bugs)
            
    *   [Treeview](https://docs.python.org/3/library/tkinter.ttk.html#treeview)
        *   [Options](https://docs.python.org/3/library/tkinter.ttk.html#id7)
            
        *   [Item options](https://docs.python.org/3/library/tkinter.ttk.html#item-options)
            
        *   [Tag options](https://docs.python.org/3/library/tkinter.ttk.html#tag-options)
            
        *   [Column identifiers](https://docs.python.org/3/library/tkinter.ttk.html#column-identifiers)
            
        *   [Virtual events](https://docs.python.org/3/library/tkinter.ttk.html#id8)
            
        *   [ttk.Treeview](https://docs.python.org/3/library/tkinter.ttk.html#ttk-treeview)
            
    *   [Ttk styling](https://docs.python.org/3/library/tkinter.ttk.html#ttk-styling)
        *   [Layouts](https://docs.python.org/3/library/tkinter.ttk.html#layouts)
            
    *   [Additional widgets](https://docs.python.org/3/library/tkinter.ttk.html#additional-widgets)
        
*   [IDLE — Python editor and shell](https://docs.python.org/3/library/idle.html)
    *   [Menus](https://docs.python.org/3/library/idle.html#menus)
        *   [File menu (Shell and Editor)](https://docs.python.org/3/library/idle.html#file-menu-shell-and-editor)
            
        *   [Edit menu (Shell and Editor)](https://docs.python.org/3/library/idle.html#edit-menu-shell-and-editor)
            
        *   [Format menu (Editor window only)](https://docs.python.org/3/library/idle.html#format-menu-editor-window-only)
            
        *   [Run menu (Editor window only)](https://docs.python.org/3/library/idle.html#run-menu-editor-window-only)
            
        *   [Shell menu (Shell window only)](https://docs.python.org/3/library/idle.html#shell-menu-shell-window-only)
            
        *   [Debug menu (Shell window only)](https://docs.python.org/3/library/idle.html#debug-menu-shell-window-only)
            
        *   [Options menu (Shell and Editor)](https://docs.python.org/3/library/idle.html#options-menu-shell-and-editor)
            
        *   [Window menu (Shell and Editor)](https://docs.python.org/3/library/idle.html#window-menu-shell-and-editor)
            
        *   [Help menu (Shell and Editor)](https://docs.python.org/3/library/idle.html#help-menu-shell-and-editor)
            
        *   [Context menus](https://docs.python.org/3/library/idle.html#context-menus)
            
    *   [Editing and Navigation](https://docs.python.org/3/library/idle.html#editing-and-navigation)
        *   [Editor windows](https://docs.python.org/3/library/idle.html#editor-windows)
            
        *   [Key bindings](https://docs.python.org/3/library/idle.html#key-bindings)
            
        *   [Automatic indentation](https://docs.python.org/3/library/idle.html#automatic-indentation)
            
        *   [Search and Replace](https://docs.python.org/3/library/idle.html#search-and-replace)
            
        *   [Completions](https://docs.python.org/3/library/idle.html#completions)
            
        *   [Calltips](https://docs.python.org/3/library/idle.html#calltips)
            
        *   [Format block](https://docs.python.org/3/library/idle.html#format-block)
            
        *   [Code Context](https://docs.python.org/3/library/idle.html#code-context)
            
        *   [Shell window](https://docs.python.org/3/library/idle.html#shell-window)
            
        *   [Text colors](https://docs.python.org/3/library/idle.html#text-colors)
            
    *   [Startup and Code Execution](https://docs.python.org/3/library/idle.html#startup-and-code-execution)
        *   [Command-line usage](https://docs.python.org/3/library/idle.html#command-line-usage)
            
        *   [Startup failure](https://docs.python.org/3/library/idle.html#startup-failure)
            
        *   [Running user code](https://docs.python.org/3/library/idle.html#running-user-code)
            
        *   [User output in Shell](https://docs.python.org/3/library/idle.html#user-output-in-shell)
            
        *   [Developing tkinter applications](https://docs.python.org/3/library/idle.html#developing-tkinter-applications)
            
        *   [Running without a subprocess](https://docs.python.org/3/library/idle.html#running-without-a-subprocess)
            
    *   [Help and Preferences](https://docs.python.org/3/library/idle.html#help-and-preferences)
        *   [Help sources](https://docs.python.org/3/library/idle.html#help-sources)
            
        *   [Setting preferences](https://docs.python.org/3/library/idle.html#setting-preferences)
            
        *   [IDLE on macOS](https://docs.python.org/3/library/idle.html#idle-on-macos)
            
        *   [Extensions](https://docs.python.org/3/library/idle.html#extensions)
            
    *   [idlelib — implementation of IDLE application](https://docs.python.org/3/library/idle.html#module-idlelib)
        
*   [`turtle` — Turtle graphics](https://docs.python.org/3/library/turtle.html)
    *   [Tutorial](https://docs.python.org/3/library/turtle.html#tutorial)
        *   [Starting a turtle environment](https://docs.python.org/3/library/turtle.html#starting-a-turtle-environment)
            
        *   [Basic drawing](https://docs.python.org/3/library/turtle.html#basic-drawing)
            *   [Pen control](https://docs.python.org/3/library/turtle.html#pen-control)
                
            *   [The turtle’s position](https://docs.python.org/3/library/turtle.html#the-turtle-s-position)
                
        *   [Making algorithmic patterns](https://docs.python.org/3/library/turtle.html#making-algorithmic-patterns)
            
    *   [Reference](https://docs.python.org/3/library/turtle.html#reference)
        *   [Turtle methods and functions](https://docs.python.org/3/library/turtle.html#turtle-methods-and-functions)
            *   [Move and draw](https://docs.python.org/3/library/turtle.html#move-and-draw)
                
            *   [Tell Turtle’s state](https://docs.python.org/3/library/turtle.html#tell-turtle-s-state)
                
            *   [Settings for measurement](https://docs.python.org/3/library/turtle.html#settings-for-measurement)
                
            *   [Pen control](https://docs.python.org/3/library/turtle.html#id1)
                *   [Drawing state](https://docs.python.org/3/library/turtle.html#drawing-state)
                    
                *   [Color control](https://docs.python.org/3/library/turtle.html#color-control)
                    
                *   [Filling](https://docs.python.org/3/library/turtle.html#filling)
                    
                *   [More drawing control](https://docs.python.org/3/library/turtle.html#more-drawing-control)
                    
            *   [Turtle state](https://docs.python.org/3/library/turtle.html#turtle-state)
                *   [Visibility](https://docs.python.org/3/library/turtle.html#visibility)
                    
                *   [Appearance](https://docs.python.org/3/library/turtle.html#appearance)
                    
            *   [Using events](https://docs.python.org/3/library/turtle.html#using-events)
                
            *   [Special Turtle methods](https://docs.python.org/3/library/turtle.html#special-turtle-methods)
                
        *   [Screen methods and functions](https://docs.python.org/3/library/turtle.html#screen-methods-and-functions)
            *   [Window control](https://docs.python.org/3/library/turtle.html#window-control)
                
            *   [Animation control](https://docs.python.org/3/library/turtle.html#animation-control)
                
            *   [Using screen events](https://docs.python.org/3/library/turtle.html#using-screen-events)
                
            *   [Input methods](https://docs.python.org/3/library/turtle.html#input-methods)
                
            *   [Settings and special methods](https://docs.python.org/3/library/turtle.html#settings-and-special-methods)
                
            *   [Screen-only methods](https://docs.python.org/3/library/turtle.html#screen-only-methods)
                
        *   [Public classes](https://docs.python.org/3/library/turtle.html#public-classes)
            
        *   [Exceptions](https://docs.python.org/3/library/turtle.html#exceptions)
            
    *   [How-to guides](https://docs.python.org/3/library/turtle.html#how-to-guides)
        *   [How to automatically begin and end filling](https://docs.python.org/3/library/turtle.html#how-to-automatically-begin-and-end-filling)
            
        *   [How to use compound shapes](https://docs.python.org/3/library/turtle.html#how-to-use-compound-shapes)
            
        *   [How to use the `turtle` module namespace](https://docs.python.org/3/library/turtle.html#how-to-use-the-turtle-module-namespace)
            
        *   [How to use turtle graphics in a script](https://docs.python.org/3/library/turtle.html#how-to-use-turtle-graphics-in-a-script)
            
        *   [How to use object-oriented turtle graphics](https://docs.python.org/3/library/turtle.html#how-to-use-object-oriented-turtle-graphics)
            
        *   [How to use `help()`](https://docs.python.org/3/library/turtle.html#how-to-use-help)
            
        *   [Translation of docstrings into different languages](https://docs.python.org/3/library/turtle.html#translation-of-docstrings-into-different-languages)
            
        *   [How to configure Screen and Turtles](https://docs.python.org/3/library/turtle.html#how-to-configure-screen-and-turtles)
            
    *   [Explanation](https://docs.python.org/3/library/turtle.html#explanation)
        
    *   [`turtledemo` — Demo scripts](https://docs.python.org/3/library/turtle.html#module-turtledemo)
        

#### Previous topic

[`locale` — Internationalization services](https://docs.python.org/3/library/locale.html "previous chapter")

#### Next topic

[`tkinter` — Python interface to Tcl/Tk](https://docs.python.org/3/library/tkinter.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Graphical+user+interfaces+with+Tk&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ftk.html&pagesource=library%2Ftk.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/tk.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/tkinter.html "tkinter — Python interface to Tcl/Tk")
     |
*   [previous](https://docs.python.org/3/library/locale.html "locale — Internationalization services")
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
    
*    
    
    |
*   Theme Auto Light Dark |