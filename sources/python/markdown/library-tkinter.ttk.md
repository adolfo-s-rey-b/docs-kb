### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/idle.html "IDLE — Python editor and shell")
     |
*   [previous](https://docs.python.org/3/library/tkinter.dnd.html "tkinter.dnd — Drag and drop support")
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
*   [`tkinter.ttk` — Tk themed widgets](https://docs.python.org/3/library/tkinter.ttk.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`tkinter.ttk` — Tk themed widgets[¶](https://docs.python.org/3/library/tkinter.ttk.html#module-tkinter.ttk "Link to this heading")

===================================================================================================================================

**Source code:** [Lib/tkinter/ttk.py](https://github.com/python/cpython/tree/3.15/Lib/tkinter/ttk.py)

* * *

The `tkinter.ttk` module provides access to the Tk themed widget set, introduced in Tk 8.5. Its widgets adapt their appearance to the platform’s native theme, giving an application a better and more consistent look and feel than the classic [`tkinter`](https://docs.python.org/3/library/tkinter.html#module-tkinter "tkinter: Interface to Tcl/Tk for graphical user interfaces")
 widgets, whose appearance is fixed.

The basic idea for `tkinter.ttk` is to separate, to the extent possible, the code implementing a widget’s behavior from the code implementing its appearance.

Ttk widgets are used just like the classic [`tkinter`](https://docs.python.org/3/library/tkinter.html#module-tkinter "tkinter: Interface to Tcl/Tk for graphical user interfaces")
 widgets and share the same machinery: the widget hierarchy, the geometry managers, variable coupling and event binding. Those foundational concepts are covered in the `tkinter` documentation and are not repeated here.

Added in version 3.1.

See also

[Tk Widget Styling Support (TIP #48)](https://tip.tcl-lang.org/48.html)

The Tcl Improvement Proposal that introduced the themed widget styling engine.

Using Ttk[¶](https://docs.python.org/3/library/tkinter.ttk.html#using-ttk "Link to this heading")

--------------------------------------------------------------------------------------------------

To start using Ttk, import its module:

Copy

from tkinter import ttk

To override the basic Tk widgets, the import should follow the Tk import:

Copy

from tkinter import \*
from tkinter.ttk import \*

That code causes several `tkinter.ttk` widgets ([`Button`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Button "tkinter.ttk.Button")
, [`Checkbutton`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Checkbutton "tkinter.ttk.Checkbutton")
, [`Entry`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Entry "tkinter.ttk.Entry")
, [`Frame`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Frame "tkinter.ttk.Frame")
, [`Label`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Label "tkinter.ttk.Label")
, [`LabelFrame`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.LabelFrame "tkinter.ttk.LabelFrame")
, [`Menubutton`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Menubutton "tkinter.ttk.Menubutton")
, [`OptionMenu`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.OptionMenu "tkinter.ttk.OptionMenu")
, [`PanedWindow`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.PanedWindow "tkinter.ttk.PanedWindow")
, [`Radiobutton`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Radiobutton "tkinter.ttk.Radiobutton")
, [`Scale`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Scale "tkinter.ttk.Scale")
, [`Scrollbar`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Scrollbar "tkinter.ttk.Scrollbar")
 and [`Spinbox`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Spinbox "tkinter.ttk.Spinbox")
) to automatically replace the Tk widgets.

Note

Overriding the classic widgets with `from tkinter.ttk import *` is convenient for adapting existing code, but new code is usually clearer if it imports the module as `from tkinter import ttk` and refers to the themed widgets explicitly, such as `ttk.Button`.

This has the direct benefit of using the new widgets which gives a better look and feel across platforms; however, the replacement widgets are not completely compatible. The main difference is that widget options such as `fg`, `bg` and others related to widget styling are no longer present in Ttk widgets. Instead, use the [`ttk.Style`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Style "tkinter.ttk.Style")
 class for improved styling effects.

Ttk widgets[¶](https://docs.python.org/3/library/tkinter.ttk.html#ttk-widgets "Link to this heading")

------------------------------------------------------------------------------------------------------

Ttk comes with 18 widgets, twelve of which already existed in tkinter: [`Button`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Button "tkinter.ttk.Button")
, [`Checkbutton`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Checkbutton "tkinter.ttk.Checkbutton")
, [`Entry`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Entry "tkinter.ttk.Entry")
, [`Frame`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Frame "tkinter.ttk.Frame")
, [`Label`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Label "tkinter.ttk.Label")
, [`LabelFrame`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.LabelFrame "tkinter.ttk.LabelFrame")
, [`Menubutton`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Menubutton "tkinter.ttk.Menubutton")
, [`PanedWindow`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.PanedWindow "tkinter.ttk.PanedWindow")
, [`Radiobutton`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Radiobutton "tkinter.ttk.Radiobutton")
, [`Scale`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Scale "tkinter.ttk.Scale")
, [`Scrollbar`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Scrollbar "tkinter.ttk.Scrollbar")
, and [`Spinbox`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Spinbox "tkinter.ttk.Spinbox")
. The other six are new: [`Combobox`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Combobox "tkinter.ttk.Combobox")
, [`Notebook`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Notebook "tkinter.ttk.Notebook")
, [`Progressbar`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Progressbar "tkinter.ttk.Progressbar")
, [`Separator`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Separator "tkinter.ttk.Separator")
, [`Sizegrip`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Sizegrip "tkinter.ttk.Sizegrip")
 and [`Treeview`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview "tkinter.ttk.Treeview")
. All of them are subclasses of [`Widget`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Widget "tkinter.ttk.Widget")
.

Using the Ttk widgets gives the application an improved look and feel. As discussed above, there are differences in how the styling is coded.

Tk code:

Copy

l1 \= tkinter.Label(text\="Test", fg\="black", bg\="white")
l2 \= tkinter.Label(text\="Test", fg\="black", bg\="white")

Ttk code:

Copy

style \= ttk.Style()
style.configure("BW.TLabel", foreground\="black", background\="white")

l1 \= ttk.Label(text\="Test", style\="BW.TLabel")
l2 \= ttk.Label(text\="Test", style\="BW.TLabel")

For more information about [TtkStyling](https://docs.python.org/3/library/tkinter.ttk.html#ttkstyling)
, see the [`Style`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Style "tkinter.ttk.Style")
 class documentation.

Combobox[¶](https://docs.python.org/3/library/tkinter.ttk.html#combobox "Link to this heading")

------------------------------------------------------------------------------------------------

The [`ttk.Combobox`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Combobox "tkinter.ttk.Combobox")
 widget combines a text field with a pop-down list of values. This widget is a subclass of [`Entry`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Entry "tkinter.ttk.Entry")
.

Besides the methods inherited from [`Widget`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Widget "tkinter.ttk.Widget")
: [`cget()`](https://docs.python.org/3/library/tkinter.html#tkinter.Misc.cget "tkinter.Misc.cget")
, [`configure()`](https://docs.python.org/3/library/tkinter.html#tkinter.Misc.configure "tkinter.Misc.configure")
, [`identify()`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Widget.identify "tkinter.ttk.Widget.identify")
, [`instate()`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Widget.instate "tkinter.ttk.Widget.instate")
 and [`state()`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Widget.state "tkinter.ttk.Widget.state")
, and the following inherited from [`Entry`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Entry "tkinter.ttk.Entry")
: [`bbox()`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Entry.bbox "tkinter.ttk.Entry.bbox")
, [`delete()`](https://docs.python.org/3/library/tkinter.html#tkinter.Entry.delete "tkinter.Entry.delete")
, [`icursor()`](https://docs.python.org/3/library/tkinter.html#tkinter.Entry.icursor "tkinter.Entry.icursor")
, [`index()`](https://docs.python.org/3/library/tkinter.html#tkinter.Entry.index "tkinter.Entry.index")
, [`insert()`](https://docs.python.org/3/library/tkinter.html#tkinter.Entry.insert "tkinter.Entry.insert")
, [`selection*`](https://docs.python.org/3/library/tkinter.html#tkinter.Entry.selection_adjust "tkinter.Entry.selection_adjust")
, [`xview*`](https://docs.python.org/3/library/tkinter.html#tkinter.XView.xview "tkinter.XView.xview")
, it has some other methods, described at [`ttk.Combobox`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Combobox "tkinter.ttk.Combobox")
.

### Options[¶](https://docs.python.org/3/library/tkinter.ttk.html#options "Link to this heading")

This widget accepts the following specific options:

| Option | Description |
| --- | --- |
| exportselection | Boolean value. If set, the widget selection is linked to the X selection (which can be returned by invoking Misc.selection\_get, for example). |
| justify | Specifies how the text is aligned within the widget. One of “left”, “center”, or “right”. |
| height | Specifies the height of the pop-down listbox, in rows. |
| postcommand | A script (possibly registered with Misc.register) that is called immediately before displaying the values. It may specify which values to display. |
| state | One of “normal”, “readonly”, or “disabled”. In the “readonly” state, the value may not be edited directly, and the user can only select one of the values from the dropdown list. In the “normal” state, the text field is directly editable. In the “disabled” state, no interaction is possible. |
| textvariable | Specifies a name whose value is linked to the widget value. Whenever the value associated with that name changes, the widget value is updated, and vice versa. See [`tkinter.StringVar`](https://docs.python.org/3/library/tkinter.html#tkinter.StringVar "tkinter.StringVar")<br>. |
| values | Specifies the list of values to display in the drop-down listbox. |
| width | Specifies an integer value indicating the desired width of the entry window, in average-size characters of the widget’s font. |

Note

Tk 9.1 added the _locale_ option, which selects the locale used to determine word and character boundaries within the text (`"C"` by default).

### Virtual events[¶](https://docs.python.org/3/library/tkinter.ttk.html#virtual-events "Link to this heading")

The combobox widgets generates a **<<ComboboxSelected>>** virtual event when the user selects an element from the list of values.

### ttk.Combobox[¶](https://docs.python.org/3/library/tkinter.ttk.html#ttk-combobox "Link to this heading")

class tkinter.ttk.Combobox[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Combobox "Link to this definition")

current(_newindex\=None_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Combobox.current "Link to this definition")

If _newindex_ is specified, sets the combobox value to the element position _newindex_. Otherwise, returns the index of the current value or -1 if the current value is not in the values list.

get()[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Combobox.get "Link to this definition")

Returns the current value of the combobox.

set(_value_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Combobox.set "Link to this definition")

Sets the value of the combobox to _value_.

Spinbox[¶](https://docs.python.org/3/library/tkinter.ttk.html#spinbox "Link to this heading")

----------------------------------------------------------------------------------------------

The [`ttk.Spinbox`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Spinbox "tkinter.ttk.Spinbox")
 widget is a [`ttk.Entry`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Entry "tkinter.ttk.Entry")
 enhanced with increment and decrement arrows. It can be used for numbers or lists of string values. This widget is a subclass of `Entry`. Besides the methods inherited from [`Widget`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Widget "tkinter.ttk.Widget")
: [`cget()`](https://docs.python.org/3/library/tkinter.html#tkinter.Misc.cget "tkinter.Misc.cget")
, [`configure()`](https://docs.python.org/3/library/tkinter.html#tkinter.Misc.configure "tkinter.Misc.configure")
, [`identify()`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Widget.identify "tkinter.ttk.Widget.identify")
, [`instate()`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Widget.instate "tkinter.ttk.Widget.instate")
 and [`state()`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Widget.state "tkinter.ttk.Widget.state")
, and the following inherited from `Entry`: [`bbox()`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Entry.bbox "tkinter.ttk.Entry.bbox")
, [`delete()`](https://docs.python.org/3/library/tkinter.html#tkinter.Entry.delete "tkinter.Entry.delete")
, [`icursor()`](https://docs.python.org/3/library/tkinter.html#tkinter.Entry.icursor "tkinter.Entry.icursor")
, [`index()`](https://docs.python.org/3/library/tkinter.html#tkinter.Entry.index "tkinter.Entry.index")
, [`insert()`](https://docs.python.org/3/library/tkinter.html#tkinter.Entry.insert "tkinter.Entry.insert")
, [`xview*`](https://docs.python.org/3/library/tkinter.html#tkinter.XView.xview "tkinter.XView.xview")
, it has some other methods, described at `ttk.Spinbox`.

### Options[¶](https://docs.python.org/3/library/tkinter.ttk.html#id1 "Link to this heading")

This widget accepts the following specific options:

| Option | Description |
| --- | --- |
| from | Float value. If set, this is the minimum value to which the decrement button will decrement. Must be spelled as `from_` when used as an argument, since `from` is a Python keyword. |
| to  | Float value. If set, this is the maximum value to which the increment button will increment. |
| increment | Float value. Specifies the amount which the increment/decrement buttons change the value. Defaults to 1.0. |
| values | Sequence of string or float values. If specified, the increment/decrement buttons will cycle through the items in this sequence rather than incrementing or decrementing numbers. |
| wrap | Boolean value. If `True`, increment and decrement buttons will cycle from the `to` value to the `from` value or the `from` value to the `to` value, respectively. |
| format | String value. This specifies the format of numbers set by the increment/decrement buttons. It must be in the form “%W.Pf”, where W is the padded width of the value, P is the precision, and ‘%’ and ‘f’ are literal. |
| command | Python callable. Will be called with no arguments whenever either of the increment or decrement buttons are pressed. |

### Virtual events[¶](https://docs.python.org/3/library/tkinter.ttk.html#id2 "Link to this heading")

The spinbox widget generates an **<<Increment>>** virtual event when the user presses <Up>, and a **<<Decrement>>** virtual event when the user presses <Down>.

### ttk.Spinbox[¶](https://docs.python.org/3/library/tkinter.ttk.html#ttk-spinbox "Link to this heading")

class tkinter.ttk.Spinbox[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Spinbox "Link to this definition")

With a non-integer increment, see [numeric values and the locale](https://docs.python.org/3/library/tkinter.html#tkinter-numeric-locale)
.

Added in version 3.8.

get()[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Spinbox.get "Link to this definition")

Returns the current value of the spinbox.

set(_value_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Spinbox.set "Link to this definition")

Sets the value of the spinbox to _value_.

Notebook[¶](https://docs.python.org/3/library/tkinter.ttk.html#notebook "Link to this heading")

------------------------------------------------------------------------------------------------

Ttk Notebook widget manages a collection of windows and displays a single one at a time. Each child window is associated with a tab, which the user may select to change the currently displayed window.

### Options[¶](https://docs.python.org/3/library/tkinter.ttk.html#id3 "Link to this heading")

This widget accepts the following specific options:

| Option | Description |
| --- | --- |
| height | If present and greater than zero, specifies the desired height of the pane area (not including internal padding or tabs). Otherwise, the maximum height of all panes is used. |
| padding | Specifies the amount of extra space to add around the outside of the notebook. The padding is a list up to four length specifications left top right bottom. If fewer than four elements are specified, bottom defaults to top, right defaults to left, and top defaults to left. |
| width | If present and greater than zero, specified the desired width of the pane area (not including internal padding). Otherwise, the maximum width of all panes is used. |

### Tab options[¶](https://docs.python.org/3/library/tkinter.ttk.html#tab-options "Link to this heading")

There are also specific options for tabs:

| Option | Description |
| --- | --- |
| state | Either “normal”, “disabled” or “hidden”. If “disabled”, then the tab is not selectable. If “hidden”, then the tab is not shown. |
| sticky | Specifies how the child window is positioned within the pane area. Value is a string containing zero or more of the characters “n”, “s”, “e” or “w”. Each letter refers to a side (north, south, east or west) that the child window will stick to, as per the [`grid`](https://docs.python.org/3/library/tkinter.html#tkinter.Grid.grid "tkinter.Grid.grid")<br> geometry manager. |
| padding | Specifies the amount of extra space to add between the notebook and this pane. Syntax is the same as for the option padding used by this widget. |
| text | Specifies a text to be displayed in the tab. |
| image | Specifies an image to display in the tab. See the option image described in [`Widget`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Widget "tkinter.ttk.Widget")<br>. |
| compound | Specifies how to display the image relative to the text, in the case both options text and image are present. See [Label Options](https://docs.python.org/3/library/tkinter.ttk.html#label-options)<br> for legal values. |
| underline | Specifies the index (0-based) of a character to underline in the text string. The underlined character is used for mnemonic activation if [`Notebook.enable_traversal()`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Notebook.enable_traversal "tkinter.ttk.Notebook.enable_traversal")<br> is called. |

### Tab identifiers[¶](https://docs.python.org/3/library/tkinter.ttk.html#tab-identifiers "Link to this heading")

The tab\_id present in several methods of [`ttk.Notebook`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Notebook "tkinter.ttk.Notebook")
 may take any of the following forms:

*   An integer between zero and the number of tabs
    
*   The name of a child window
    
*   A positional specification of the form “@x,y”, which identifies the tab
    
*   The literal string “current”, which identifies the currently selected tab
    
*   The literal string “end”, which returns the number of tabs (only valid for [`Notebook.index()`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Notebook.index "tkinter.ttk.Notebook.index")
    )
    

### Virtual events[¶](https://docs.python.org/3/library/tkinter.ttk.html#id4 "Link to this heading")

This widget generates a **<<NotebookTabChanged>>** virtual event after a new tab is selected.

### ttk.Notebook[¶](https://docs.python.org/3/library/tkinter.ttk.html#ttk-notebook "Link to this heading")

class tkinter.ttk.Notebook[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Notebook "Link to this definition")

add(_child_, _\*\*kw_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Notebook.add "Link to this definition")

Adds a new tab to the notebook.

If window is currently managed by the notebook but hidden, it is restored to its previous position.

See [Tab Options](https://docs.python.org/3/library/tkinter.ttk.html#tab-options)
 for the list of available options.

forget(_tab\_id_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Notebook.forget "Link to this definition")

Removes the tab specified by _tab\_id_, unmaps and unmanages the associated window.

This shadows the inherited geometry-manager `forget()`; use [`pack_forget()`](https://docs.python.org/3/library/tkinter.html#tkinter.Pack.pack_forget "tkinter.Pack.pack_forget")
, [`grid_forget()`](https://docs.python.org/3/library/tkinter.html#tkinter.Grid.grid_forget "tkinter.Grid.grid_forget")
 or [`place_forget()`](https://docs.python.org/3/library/tkinter.html#tkinter.Place.place_forget "tkinter.Place.place_forget")
 to remove the widget itself from its manager.

hide(_tab\_id_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Notebook.hide "Link to this definition")

Hides the tab specified by _tab\_id_.

The tab will not be displayed, but the associated window remains managed by the notebook and its configuration remembered. Hidden tabs may be restored with the [`add()`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Notebook.add "tkinter.ttk.Notebook.add")
 command.

identify(_x_, _y_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Notebook.identify "Link to this definition")

Returns the name of the tab element at position _x_, _y_, or the empty string if none.

index(_tab\_id_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Notebook.index "Link to this definition")

Returns the numeric index of the tab specified by _tab\_id_, or the total number of tabs if _tab\_id_ is the string “end”.

insert(_pos_, _child_, _\*\*kw_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Notebook.insert "Link to this definition")

Inserts a pane at the specified position.

_pos_ is either the string “end”, an integer index, or the name of a managed child. If _child_ is already managed by the notebook, moves it to the specified position.

See [Tab Options](https://docs.python.org/3/library/tkinter.ttk.html#tab-options)
 for the list of available options.

select(_tab\_id\=None_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Notebook.select "Link to this definition")

Selects the specified _tab\_id_.

The associated child window will be displayed, and the previously selected window (if different) is unmapped. If _tab\_id_ is omitted, returns the widget name of the currently selected pane.

tab(_tab\_id_, _option\=None_, _\*\*kw_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Notebook.tab "Link to this definition")

Query or modify the options of the specific _tab\_id_.

If _kw_ is not given, returns a dictionary of the tab option values. If _option_ is specified, returns the value of that _option_. Otherwise, sets the options to the corresponding values.

tabs()[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Notebook.tabs "Link to this definition")

Returns a tuple of windows managed by the notebook.

enable\_traversal()[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Notebook.enable_traversal "Link to this definition")

Enable keyboard traversal for a toplevel window containing this notebook.

This will extend the bindings for the toplevel window containing the notebook as follows:

*   Control\-Tab: selects the tab following the currently selected one.
    
*   Shift\-Control\-Tab: selects the tab preceding the currently selected one.
    
*   Alt\-K: where _K_ is the mnemonic (underlined) character of any tab, will select that tab.
    

Multiple notebooks in a single toplevel may be enabled for traversal, including nested notebooks. However, notebook traversal only works properly if all panes are direct children of the notebook.

Progressbar[¶](https://docs.python.org/3/library/tkinter.ttk.html#progressbar "Link to this heading")

------------------------------------------------------------------------------------------------------

The [`ttk.Progressbar`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Progressbar "tkinter.ttk.Progressbar")
 widget shows the status of a long-running operation. It can operate in two modes: 1) the determinate mode which shows the amount completed relative to the total amount of work to be done and 2) the indeterminate mode which provides an animated display to let the user know that work is progressing.

### Options[¶](https://docs.python.org/3/library/tkinter.ttk.html#id5 "Link to this heading")

This widget accepts the following specific options:

| Option | Description |
| --- | --- |
| orient | One of “horizontal” or “vertical”. Specifies the orientation of the progress bar. |
| length | Specifies the length of the long axis of the progress bar (width if horizontal, height if vertical). |
| mode | One of “determinate” or “indeterminate”. |
| maximum | A number specifying the maximum value. Defaults to 100. |
| value | The current value of the progress bar. In “determinate” mode, this represents the amount of work completed. In “indeterminate” mode, it is interpreted as modulo _maximum_; that is, the progress bar completes one “cycle” when its value increases by _maximum_. |
| variable | A name which is linked to the option value. If specified, the value of the progress bar is automatically set to the value of this name whenever the latter is modified. |
| phase | Read-only option. The widget periodically increments the value of this option whenever its value is greater than 0 and, in determinate mode, less than maximum. This option may be used by the current theme to provide additional animation effects. |

### ttk.Progressbar[¶](https://docs.python.org/3/library/tkinter.ttk.html#ttk-progressbar "Link to this heading")

class tkinter.ttk.Progressbar[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Progressbar "Link to this definition")

start(_interval\=None_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Progressbar.start "Link to this definition")

Begin autoincrement mode: schedules a recurring timer event that calls [`Progressbar.step()`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Progressbar.step "tkinter.ttk.Progressbar.step")
 every _interval_ milliseconds. If omitted, _interval_ defaults to 50 milliseconds.

step(_amount\=None_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Progressbar.step "Link to this definition")

Increments the progress bar’s value by _amount_.

_amount_ defaults to 1.0 if omitted.

stop()[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Progressbar.stop "Link to this definition")

Stop autoincrement mode: cancels any recurring timer event initiated by [`Progressbar.start()`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Progressbar.start "tkinter.ttk.Progressbar.start")
 for this progress bar.

Separator[¶](https://docs.python.org/3/library/tkinter.ttk.html#separator "Link to this heading")

--------------------------------------------------------------------------------------------------

The [`ttk.Separator`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Separator "tkinter.ttk.Separator")
 widget displays a horizontal or vertical separator bar.

It has no other methods besides the ones inherited from [`ttk.Widget`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Widget "tkinter.ttk.Widget")
.

### Options[¶](https://docs.python.org/3/library/tkinter.ttk.html#id6 "Link to this heading")

This widget accepts the following specific option:

| Option | Description |
| --- | --- |
| orient | One of “horizontal” or “vertical”. Specifies the orientation of the separator. |

Sizegrip[¶](https://docs.python.org/3/library/tkinter.ttk.html#sizegrip "Link to this heading")

------------------------------------------------------------------------------------------------

The [`ttk.Sizegrip`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Sizegrip "tkinter.ttk.Sizegrip")
 widget (also known as a grow box) allows the user to resize the containing toplevel window by pressing and dragging the grip.

This widget has neither specific options nor specific methods, besides the ones inherited from [`ttk.Widget`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Widget "tkinter.ttk.Widget")
.

### Platform-specific notes[¶](https://docs.python.org/3/library/tkinter.ttk.html#platform-specific-notes "Link to this heading")

*   On macOS, toplevel windows automatically include a built-in size grip by default. Adding a [`Sizegrip`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Sizegrip "tkinter.ttk.Sizegrip")
     is harmless, since the built-in grip will just mask the widget.
    

### Bugs[¶](https://docs.python.org/3/library/tkinter.ttk.html#bugs "Link to this heading")

*   If the containing toplevel’s position was specified relative to the right or bottom of the screen (for example, ….), the [`Sizegrip`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Sizegrip "tkinter.ttk.Sizegrip")
     widget will not resize the window.
    
*   This widget supports only “southeast” resizing.
    

Treeview[¶](https://docs.python.org/3/library/tkinter.ttk.html#treeview "Link to this heading")

------------------------------------------------------------------------------------------------

The [`ttk.Treeview`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview "tkinter.ttk.Treeview")
 widget displays a hierarchical collection of items. Each item has a textual label, an optional image, and an optional list of data values. The data values are displayed in successive columns after the tree label.

The order in which data values are displayed may be controlled by setting the widget option `displaycolumns`. The tree widget can also display column headings. Columns may be accessed by number or symbolic names listed in the widget option columns. See [Column Identifiers](https://docs.python.org/3/library/tkinter.ttk.html#column-identifiers)
.

Each item is identified by a unique name. The widget will generate item IDs if they are not supplied by the caller. There is a distinguished root item, named `{}`. The root item itself is not displayed; its children appear at the top level of the hierarchy.

Each item also has a list of tags, which can be used to associate event bindings with individual items and control the appearance of the item.

The Treeview widget supports horizontal and vertical scrolling, according to the options described in [Scrollable Widget Options](https://docs.python.org/3/library/tkinter.ttk.html#scrollable-widget-options)
 and the methods [`Treeview.xview()`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.xview "tkinter.ttk.Treeview.xview")
 and [`Treeview.yview()`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.yview "tkinter.ttk.Treeview.yview")
.

### Options[¶](https://docs.python.org/3/library/tkinter.ttk.html#id7 "Link to this heading")

This widget accepts the following specific options:

| Option | Description |
| --- | --- |
| columns | A list of column identifiers, specifying the number of columns and their names. |
| displaycolumns | A list of column identifiers (either symbolic or integer indices) specifying which data columns are displayed and the order in which they appear, or the string “#all”. |
| height | Specifies the number of rows which should be visible. Note: the requested width is determined from the sum of the column widths. |
| padding | Specifies the internal padding for the widget. The padding is a list of up to four length specifications. |
| selectmode | Controls how the built-in class bindings manage the selection. One of “extended”, “browse” or “none”. If set to “extended” (the default), multiple items may be selected. If “browse”, only a single item will be selected at a time. If “none”, the selection will not be changed.<br><br>Note that the application code and tag bindings can set the selection however they wish, regardless of the value of this option. |
| show | A list containing zero or more of the following values, specifying which elements of the tree to display.<br><br>*   tree: display tree labels in column #0.<br>    <br>*   headings: display the heading row.<br>    <br><br>The default is “tree headings”, that is, show all elements.<br><br>**Note**: Column #0 always refers to the tree column, even if show=”tree” is not specified. |

Note

Tk 9.0 added several [`Treeview`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview "tkinter.ttk.Treeview")
 features. The _selectmode_ option gained the values `"single"` and `"multiple"`; the new widget options _selecttype_ (`"item"` or `"cell"` selection), _striped_ (zebra-striped rows), and _titlecolumns_ / _titleitems_ (columns or rows frozen against scrolling) were introduced; the column _separator_ option was added; and items gained a _hidden_ option. Tk 9.1 added the _rowheight_ and _headingheight_ options.

### Item options[¶](https://docs.python.org/3/library/tkinter.ttk.html#item-options "Link to this heading")

The following item options may be specified for items in the insert and item widget commands.

| Option | Description |
| --- | --- |
| text | The textual label to display for the item. |
| image | A Tk Image, displayed to the left of the label. |
| values | The list of values associated with the item.<br><br>Each item should have the same number of values as the widget option columns. If there are fewer values than columns, the remaining values are assumed empty. If there are more values than columns, the extra values are ignored. |
| open | `True`/`False` value indicating whether the item’s children should be displayed or hidden. |
| tags | A list of tags associated with this item. |

### Tag options[¶](https://docs.python.org/3/library/tkinter.ttk.html#tag-options "Link to this heading")

The following options may be specified on tags:

| Option | Description |
| --- | --- |
| foreground | Specifies the text foreground color. |
| background | Specifies the cell or item background color. |
| font | Specifies the font to use when drawing text. |
| image | Specifies the item image, in case the item’s image option is empty. |

### Column identifiers[¶](https://docs.python.org/3/library/tkinter.ttk.html#column-identifiers "Link to this heading")

Column identifiers take any of the following forms:

*   A symbolic name from the list of columns option.
    
*   An integer n, specifying the nth data column.
    
*   A string of the form #n, where n is an integer, specifying the nth display column.
    

Notes:

*   Item’s option values may be displayed in a different order than the order in which they are stored.
    
*   Column #0 always refers to the tree column, even if show=”tree” is not specified.
    

A data column number is an index into an item’s option values list; a display column number is the column number in the tree where the values are displayed. Tree labels are displayed in column #0. If option displaycolumns is not set, then data column n is displayed in column #n+1. Again, **column #0 always refers to the tree column**.

### Virtual events[¶](https://docs.python.org/3/library/tkinter.ttk.html#id8 "Link to this heading")

The Treeview widget generates the following virtual events.

| Event | Description |
| --- | --- |
| <<TreeviewSelect>> | Generated whenever the selection changes. |
| <<TreeviewOpen>> | Generated just before settings the focus item to open=True. |
| <<TreeviewClose>> | Generated just after setting the focus item to open=False. |

The [`Treeview.focus()`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.focus "tkinter.ttk.Treeview.focus")
 and [`Treeview.selection()`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.selection "tkinter.ttk.Treeview.selection")
 methods can be used to determine the affected item or items.

### ttk.Treeview[¶](https://docs.python.org/3/library/tkinter.ttk.html#ttk-treeview "Link to this heading")

class tkinter.ttk.Treeview[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview "Link to this definition")

bbox(_item_, _column\=None_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.bbox "Link to this definition")

Returns the bounding box (relative to the treeview widget’s window) of the specified _item_ in the form (x, y, width, height).

If _column_ is specified, returns the bounding box of that cell. If the _item_ is not visible (that is, if it is a descendant of a closed item or is scrolled offscreen), returns an empty string.

This shadows the inherited `Misc.bbox()`; use [`grid_bbox()`](https://docs.python.org/3/library/tkinter.html#tkinter.Misc.grid_bbox "tkinter.Misc.grid_bbox")
 for the grid bounding box.

get\_children(_item\=None_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.get_children "Link to this definition")

Returns a tuple of children belonging to _item_.

If _item_ is not specified, returns root children.

set\_children(_item_, _\*newchildren_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.set_children "Link to this definition")

Replaces _item_’s children with _newchildren_.

Children present in _item_ that are not present in _newchildren_ are detached from the tree. No items in _newchildren_ may be an ancestor of _item_. Note that not specifying _newchildren_ results in detaching _item_’s children.

column(_column_, _option\=None_, _\*\*kw_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.column "Link to this definition")

Query or modify the options for the specified _column_.

If _kw_ is not given, returns a dict of the column option values. If _option_ is specified then the value for that _option_ is returned. Otherwise, sets the options to the corresponding values.

The valid options/values are:

_id_

Returns the column name. This is a read-only option.

_anchor_: One of the standard Tk anchor values.

Specifies how the text in this column should be aligned with respect to the cell.

_minwidth_: width

The minimum width of the column in pixels. The treeview widget will not make the column any smaller than specified by this option when the widget is resized or the user drags a column.

_separator_: `True`/`False`

Specifies whether a column separator should be drawn to the right of the column.

_stretch_: `True`/`False`

Specifies whether the column’s width should be adjusted when the widget is resized.

_width_: width

The width of the column in pixels.

To configure the tree column, call this with column = “#0”

delete(_\*items_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.delete "Link to this definition")

Delete all specified _items_ and all their descendants.

The root item may not be deleted.

detach(_\*items_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.detach "Link to this definition")

Unlinks all of the specified _items_ from the tree.

The items and all of their descendants are still present, and may be reinserted at another point in the tree, but will not be displayed.

The root item may not be detached.

exists(_item_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.exists "Link to this definition")

Returns `True` if the specified _item_ is present in the tree, `False` otherwise.

focus(_item\=None_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.focus "Link to this definition")

If _item_ is specified, sets the focus item to _item_. Otherwise, returns the current focus item, or ‘’ if there is none.

This shadows the inherited `Misc.focus()`; use [`focus_set()`](https://docs.python.org/3/library/tkinter.html#tkinter.Misc.focus_set "tkinter.Misc.focus_set")
 to focus the widget itself.

heading(_column_, _option\=None_, _\*\*kw_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.heading "Link to this definition")

Query or modify the heading options for the specified _column_.

If _kw_ is not given, returns a dict of the heading option values. If _option_ is specified then the value for that _option_ is returned. Otherwise, sets the options to the corresponding values.

The valid options/values are:

_text_: text

The text to display in the column heading.

_image_: imageName

Specifies an image to display to the right of the column heading.

_anchor_: anchor

Specifies how the heading text should be aligned. One of the standard Tk anchor values.

_command_: callback

A callback to be invoked when the heading label is pressed.

To configure the tree column heading, call this with column = “#0”.

identify(_component_, _x_, _y_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.identify "Link to this definition")

Returns a description of the specified _component_ under the point given by _x_ and _y_, or the empty string if no such _component_ is present at that position.

identify\_row(_y_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.identify_row "Link to this definition")

Returns the item ID of the item at position _y_.

identify\_column(_x_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.identify_column "Link to this definition")

Returns the display column identifier of the cell at position _x_.

The tree column has ID #0.

identify\_region(_x_, _y_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.identify_region "Link to this definition")

Returns one of:

| region | meaning |
| --- | --- |
| heading | Tree heading area. |
| separator | Space between two columns headings. |
| tree | The tree area. |
| cell | A data cell. |

Availability: Tk 8.6.

identify\_element(_x_, _y_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.identify_element "Link to this definition")

Returns the element at position _x_, _y_.

Availability: Tk 8.6.

index(_item_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.index "Link to this definition")

Returns the integer index of _item_ within its parent’s list of children.

insert(_parent_, _index_, _iid\=None_, _\*\*kw_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert "Link to this definition")

Creates a new item and returns the item identifier of the newly created item.

_parent_ is the item ID of the parent item, or the empty string to create a new top-level item. _index_ is an integer, or the value “end”, specifying where in the list of parent’s children to insert the new item. If _index_ is less than or equal to zero, the new node is inserted at the beginning; if _index_ is greater than or equal to the current number of children, it is inserted at the end. If _iid_ is specified, it is used as the item identifier; _iid_ must not already exist in the tree. Otherwise, a new unique identifier is generated.

See [Item Options](https://docs.python.org/3/library/tkinter.ttk.html#item-options)
 for the list of available options.

item(_item_, _option\=None_, _\*\*kw_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.item "Link to this definition")

Query or modify the options for the specified _item_.

If no options are given, a dict with options/values for the item is returned. If _option_ is specified then the value for that option is returned. Otherwise, sets the options to the corresponding values as given by _kw_.

move(_item_, _parent_, _index_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.move "Link to this definition")

Moves _item_ to position _index_ in _parent_’s list of children.

It is illegal to move an item under one of its descendants. If _index_ is less than or equal to zero, _item_ is moved to the beginning; if greater than or equal to the number of children, it is moved to the end. If _item_ was detached it is reattached.

[`reattach()`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.reattach "tkinter.ttk.Treeview.reattach")
 is an alias of `move()`.

next(_item_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.next "Link to this definition")

Returns the identifier of _item_’s next sibling, or ‘’ if _item_ is the last child of its parent.

parent(_item_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.parent "Link to this definition")

Returns the ID of the parent of _item_, or ‘’ if _item_ is at the top level of the hierarchy.

prev(_item_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.prev "Link to this definition")

Returns the identifier of _item_’s previous sibling, or ‘’ if _item_ is the first child of its parent.

see(_item_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.see "Link to this definition")

Ensure that _item_ is visible.

Sets all of _item_’s ancestors open option to `True`, and scrolls the widget if necessary so that _item_ is within the visible portion of the tree.

selection()[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.selection "Link to this definition")

Returns a tuple of selected items.

Changed in version 3.8: `selection()` no longer takes arguments. For changing the selection state use the following selection methods.

selection\_set(_\*items_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.selection_set "Link to this definition")

_items_ becomes the new selection.

Changed in version 3.6: _items_ can be passed as separate arguments, not just as a single tuple.

selection\_add(_\*items_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.selection_add "Link to this definition")

Add _items_ to the selection.

Changed in version 3.6: _items_ can be passed as separate arguments, not just as a single tuple.

selection\_remove(_\*items_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.selection_remove "Link to this definition")

Remove _items_ from the selection.

Changed in version 3.6: _items_ can be passed as separate arguments, not just as a single tuple.

selection\_toggle(_\*items_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.selection_toggle "Link to this definition")

Toggle the selection state of each item in _items_.

Changed in version 3.6: _items_ can be passed as separate arguments, not just as a single tuple.

set(_item_, _column\=None_, _value\=None_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.set "Link to this definition")

With one argument, returns a dictionary of column/value pairs for the specified _item_. With two arguments, returns the current value of the specified _column_. With three arguments, sets the value of given _column_ in given _item_ to the specified _value_.

tag\_bind(_tagname_, _sequence\=None_, _callback\=None_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.tag_bind "Link to this definition")

Bind a callback for the given event _sequence_ to the tag _tagname_. When an event is delivered to an item, the callbacks for each of the item’s tags option are called.

tag\_configure(_tagname_, _option\=None_, _\*\*kw_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.tag_configure "Link to this definition")

Query or modify the options for the specified _tagname_.

If _kw_ is not given, returns a dict of the option settings for _tagname_. If _option_ is specified, returns the value for that _option_ for the specified _tagname_. Otherwise, sets the options to the corresponding values for the given _tagname_.

tag\_has(_tagname_, _item\=None_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.tag_has "Link to this definition")

If _item_ is specified, returns `True` if the specified _item_ has the given _tagname_ and `False` otherwise. Otherwise, returns a tuple of all items that have the specified tag.

Availability: Tk 8.6

xview(_\*args_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.xview "Link to this definition")

Query or modify horizontal position of the treeview.

yview(_\*args_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.yview "Link to this definition")

Query or modify vertical position of the treeview.

Ttk styling[¶](https://docs.python.org/3/library/tkinter.ttk.html#ttk-styling "Link to this heading")

------------------------------------------------------------------------------------------------------

Each widget in `ttk` is assigned a style, which specifies the set of elements making up the widget and how they are arranged, along with dynamic and default settings for element options. By default the style name is the same as the widget’s class name, but it may be overridden by the widget’s style option. If you don’t know the class name of a widget, use the method [`Misc.winfo_class`](https://docs.python.org/3/library/tkinter.html#tkinter.Misc.winfo_class "tkinter.Misc.winfo_class")
 (somewidget.winfo\_class()).

See also

[Introduction to the Tk theme engine](https://www.tcl-lang.org/man/tcl9.0/TkCmd/ttk_intro.html)

The `ttk::intro` man page explains how the theme engine works.

[The Tile Widget Set](https://tktable.sourceforge.net/tile/tile-tcl2004.pdf)

Joe English’s 2004 paper introducing the theme engine (then the separate _Tile_ extension), with diagrams of how elements and layouts make up a widget’s appearance.

class tkinter.ttk.Style[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Style "Link to this definition")

This class is used to manipulate the style database.

configure(_style_, _query\_opt\=None_, _\*\*kw_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Style.configure "Link to this definition")

Query or set the default value of the specified option(s) in _style_.

Each key in _kw_ is an option and each value is a string identifying the value for that option.

For example, to change every default button to be a flat button with some padding and a different background color:

Copy

from tkinter import ttk
import tkinter

root \= tkinter.Tk()

ttk.Style().configure("TButton", padding\=6, relief\="flat",
   background\="#ccc")

btn \= ttk.Button(text\="Sample")
btn.pack()

root.mainloop()

map(_style_, _query\_opt\=None_, _\*\*kw_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Style.map "Link to this definition")

Query or sets dynamic values of the specified option(s) in _style_.

Each key in _kw_ is an option and each value should be a list or a tuple (usually) containing statespecs grouped in tuples, lists, or some other preference. A statespec is a compound of one or more states and then a value.

An example may make it more understandable:

Copy

import tkinter
from tkinter import ttk

root \= tkinter.Tk()

style \= ttk.Style()
style.map("C.TButton",
    foreground\=\[('pressed', 'red'), ('active', 'blue')\],
    background\=\[('pressed', '!disabled', 'black'), ('active', 'white')\]
    )

colored\_btn \= ttk.Button(text\="Test", style\="C.TButton").pack()

root.mainloop()

Note that the order of the (states, value) sequences for an option does matter, if the order is changed to `[('active', 'blue'), ('pressed', 'red')]` in the foreground option, for example, the result would be a blue foreground when the widget were in active or pressed states.

When called to query the map (without specifying values to set), it returns a dictionary mapping each option to its list of statespecs.

Changed in version 3.10: The value returned when querying the map was corrected.

lookup(_style_, _option_, _state\=None_, _default\=None_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Style.lookup "Link to this definition")

Returns the value specified for _option_ in _style_.

If _state_ is specified, it is expected to be a sequence of one or more states. If the _default_ argument is set, it is used as a fallback value in case no specification for option is found.

To check what font a Button uses by default:

Copy

from tkinter import ttk

print(ttk.Style().lookup("TButton", "font"))

layout(_style_, _layoutspec\=None_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Style.layout "Link to this definition")

Define the widget layout for given _style_. If _layoutspec_ is omitted, return the layout specification for given style.

_layoutspec_, if specified, is expected to be a list or some other sequence type (excluding strings), where each item should be a tuple and the first item is the layout name and the second item should have the format described in [Layouts](https://docs.python.org/3/library/tkinter.ttk.html#layouts)
.

To understand the format, see the following example (it is not intended to do anything useful):

Copy

from tkinter import ttk
import tkinter

root \= tkinter.Tk()

style \= ttk.Style()
style.layout("TMenubutton", \[\
   ("Menubutton.background", None),\
   ("Menubutton.button", {"children":\
       \[("Menubutton.focus", {"children":\
           \[("Menubutton.padding", {"children":\
               \[("Menubutton.label", {"side": "left", "expand": 1})\]\
           })\]\
       })\]\
   }),\
\])

mbtn \= ttk.Menubutton(text\='Text')
mbtn.pack()
root.mainloop()

element\_create(_elementname_, _etype_, _\*args_, _\*\*kw_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Style.element_create "Link to this definition")

Create a new element in the current theme, of the given _etype_ which is expected to be either “image”, “from” or “vsapi”. The latter is only available in Tk 8.6 on Windows.

If “image” is used, _args_ should contain the default image name followed by statespec/value pairs (this is the imagespec), and _kw_ may have the following options:

border=padding

padding is a list of up to four integers, specifying the left, top, right, and bottom borders, respectively.

height=height

Specifies a minimum height for the element. If less than zero, the base image’s height is used as a default.

padding=padding

Specifies the element’s interior padding. Defaults to border’s value if not specified.

sticky=spec

Specifies how the image is placed within the final parcel. spec contains zero or more characters “n”, “s”, “w”, or “e”.

width=width

Specifies a minimum width for the element. If less than zero, the base image’s width is used as a default.

Example:

Copy

img1 \= tkinter.PhotoImage(master\=root, file\='button.png')
img2 \= tkinter.PhotoImage(master\=root, file\='button-pressed.png')
img3 \= tkinter.PhotoImage(master\=root, file\='button-active.png')
style \= ttk.Style(root)
style.element\_create('Button.button', 'image',
                     img1, ('pressed', img2), ('active', img3),
                     border\=(2, 4), sticky\='we')

If “from” is used as the value of _etype_, `element_create()` will clone an existing element. _args_ is expected to contain a themename, from which the element will be cloned, and optionally an element to clone from. If this element to clone from is not specified, an empty element will be used. _kw_ is discarded.

Example:

Copy

style \= ttk.Style(root)
style.element\_create('plain.background', 'from', 'default')

If “vsapi” is used as the value of _etype_, `element_create()` will create a new element in the current theme whose visual appearance is drawn using the Microsoft Visual Styles API which is responsible for the themed styles on Windows XP and Vista. _args_ is expected to contain the Visual Styles class and part as given in the Microsoft documentation followed by an optional sequence of tuples of ttk states and the corresponding Visual Styles API state value. _kw_ may have the following options:

padding=padding

Specify the element’s interior padding. _padding_ is a list of up to four integers specifying the left, top, right and bottom padding quantities respectively. If fewer than four elements are specified, bottom defaults to top, right defaults to left, and top defaults to left. In other words, a list of three numbers specify the left, vertical, and right padding; a list of two numbers specify the horizontal and the vertical padding; a single number specifies the same padding all the way around the widget. This option may not be mixed with any other options.

margins=padding

Specifies the elements exterior padding. _padding_ is a list of up to four integers specifying the left, top, right and bottom padding quantities respectively. This option may not be mixed with any other options.

width=width

Specifies the width for the element. If this option is set then the Visual Styles API will not be queried for the recommended size or the part. If this option is set then _height_ should also be set. The _width_ and _height_ options cannot be mixed with the _padding_ or _margins_ options.

height=height

Specifies the height of the element. See the comments for _width_.

Example:

Copy

style \= ttk.Style(root)
style.element\_create('pin', 'vsapi', 'EXPLORERBAR', 3, \[\
                     ('pressed', '!selected', 3),\
                     ('active', '!selected', 2),\
                     ('pressed', 'selected', 6),\
                     ('active', 'selected', 5),\
                     ('selected', 4),\
                     ('', 1)\])
style.layout('Explorer.Pin',
             \[('Explorer.Pin.pin', {'sticky': 'news'})\])
pin \= ttk.Checkbutton(style\='Explorer.Pin')
pin.pack(expand\=True, fill\='both')

Changed in version 3.13: Added support of the “vsapi” element factory.

element\_names()[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Style.element_names "Link to this definition")

Returns a tuple of elements defined in the current theme.

element\_options(_elementname_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Style.element_options "Link to this definition")

Returns a tuple of _elementname_’s options.

theme\_create(_themename_, _parent\=None_, _settings\=None_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Style.theme_create "Link to this definition")

Create a new theme.

It is an error if _themename_ already exists. If _parent_ is specified, the new theme will inherit styles, elements and layouts from the parent theme. If _settings_ are present they are expected to have the same syntax used for [`theme_settings()`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Style.theme_settings "tkinter.ttk.Style.theme_settings")
.

theme\_settings(_themename_, _settings_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Style.theme_settings "Link to this definition")

Temporarily sets the current theme to _themename_, apply specified _settings_ and then restore the previous theme.

Each key in _settings_ is a style and each value may contain the keys ‘configure’, ‘map’, ‘layout’ and ‘element create’ and they are expected to have the same format as specified by the methods [`Style.configure()`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Style.configure "tkinter.ttk.Style.configure")
, [`Style.map()`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Style.map "tkinter.ttk.Style.map")
, [`Style.layout()`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Style.layout "tkinter.ttk.Style.layout")
 and [`Style.element_create()`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Style.element_create "tkinter.ttk.Style.element_create")
 respectively.

As an example, let’s change the Combobox for the default theme a bit:

Copy

from tkinter import ttk
import tkinter

root \= tkinter.Tk()

style \= ttk.Style()
style.theme\_settings("default", {
   "TCombobox": {
       "configure": {"padding": 5},
       "map": {
           "background": \[("active", "green2"),\
                          ("!disabled", "green4")\],
           "fieldbackground": \[("!disabled", "green3")\],
           "foreground": \[("focus", "OliveDrab1"),\
                          ("!disabled", "OliveDrab2")\]
       }
   }
})

combo \= ttk.Combobox().pack()

root.mainloop()

theme\_names()[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Style.theme_names "Link to this definition")

Returns a tuple of all known themes.

theme\_use(_themename\=None_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Style.theme_use "Link to this definition")

If _themename_ is not given, returns the theme in use. Otherwise, sets the current theme to _themename_, refreshes all widgets and emits a <<ThemeChanged>> event.

### Layouts[¶](https://docs.python.org/3/library/tkinter.ttk.html#layouts "Link to this heading")

A layout can be just `None`, if it takes no options, or a dict of options specifying how to arrange the element. The layout mechanism uses a simplified version of the pack geometry manager: given an initial cavity, each element is allocated a parcel.

The valid options/values are:

_side_: whichside

Specifies which side of the cavity to place the element; one of top, right, bottom or left. If omitted, the element occupies the entire cavity.

_sticky_: nswe

Specifies where the element is placed inside its allocated parcel.

_unit_: 0 or 1

If set to 1, causes the element and all of its descendants to be treated as a single element for the purposes of [`Widget.identify()`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Widget.identify "tkinter.ttk.Widget.identify")
 et al. It’s used for things like scrollbar thumbs with grips.

_children_: \[sublayout… \]

Specifies a list of elements to place inside the element. Each element is a tuple (or other sequence type) where the first item is the layout name, and the other is a [Layout](https://docs.python.org/3/library/tkinter.ttk.html#layouts)
.

Additional widgets[¶](https://docs.python.org/3/library/tkinter.ttk.html#additional-widgets "Link to this heading")

--------------------------------------------------------------------------------------------------------------------

The following themed widgets complete the `tkinter.ttk` widget set. Each is the themed counterpart of the like-named classic [`tkinter`](https://docs.python.org/3/library/tkinter.html#module-tkinter "tkinter: Interface to Tcl/Tk for graphical user interfaces")
 widget and inherits the common methods of [`Widget`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Widget "tkinter.ttk.Widget")
.

class tkinter.ttk.Button(_master\=None_, _\*\*kw_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Button "Link to this definition")

Ttk `Button` widget, displays a textual label and/or image, and evaluates a command when pressed. It is the themed counterpart of [`tkinter.Button`](https://docs.python.org/3/library/tkinter.html#tkinter.Button "tkinter.Button")
 and inherits the common widget methods from [`Widget`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Widget "tkinter.ttk.Widget")
.

invoke()[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Button.invoke "Link to this definition")

Invoke the command associated with the button and return its result.

class tkinter.ttk.Checkbutton(_master\=None_, _\*\*kw_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Checkbutton "Link to this definition")

Ttk `Checkbutton` widget, used to control a boolean variable that is toggled on and off. It is the themed counterpart of [`tkinter.Checkbutton`](https://docs.python.org/3/library/tkinter.html#tkinter.Checkbutton "tkinter.Checkbutton")
 and inherits the common widget methods from [`Widget`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Widget "tkinter.ttk.Widget")
.

invoke()[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Checkbutton.invoke "Link to this definition")

Toggle the button between its selected and deselected states, invoke the command associated with the button, and return its result.

class tkinter.ttk.Entry(_master\=None_, _widget\=None_, _\*\*kw_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Entry "Link to this definition")

Ttk `Entry` widget, displays a one-line text string and allows the user to edit it. It is the themed counterpart of [`tkinter.Entry`](https://docs.python.org/3/library/tkinter.html#tkinter.Entry "tkinter.Entry")
 and inherits the common widget methods from [`Widget`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Widget "tkinter.ttk.Widget")
 as well as the editing methods from `tkinter.Entry`.

bbox(_index_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Entry.bbox "Link to this definition")

Return a tuple `(x, y, width, height)` giving the bounding box of the character at the given _index_.

This shadows the inherited `Misc.bbox()`; use [`grid_bbox()`](https://docs.python.org/3/library/tkinter.html#tkinter.Misc.grid_bbox "tkinter.Misc.grid_bbox")
 for the grid bounding box.

identify(_x_, _y_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Entry.identify "Link to this definition")

Return the name of the element under the point given by _x_ and _y_, or the empty string if no element is present at that location.

validate()[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Entry.validate "Link to this definition")

Force validation of the entry and return `True` if validation succeeded, and `False` otherwise.

class tkinter.ttk.Frame(_master\=None_, _\*\*kw_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Frame "Link to this definition")

Ttk `Frame` widget, a container used to group and lay out other widgets. It is the themed counterpart of [`tkinter.Frame`](https://docs.python.org/3/library/tkinter.html#tkinter.Frame "tkinter.Frame")
 and inherits the common widget methods from [`Widget`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Widget "tkinter.ttk.Widget")
.

class tkinter.ttk.Label(_master\=None_, _\*\*kw_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Label "Link to this definition")

Ttk `Label` widget, displays a textual label and/or image. It is the themed counterpart of [`tkinter.Label`](https://docs.python.org/3/library/tkinter.html#tkinter.Label "tkinter.Label")
 and inherits the common widget methods from [`Widget`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Widget "tkinter.ttk.Widget")
.

class tkinter.ttk.Labelframe(_master\=None_, _\*\*kw_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Labelframe "Link to this definition")

Ttk `Labelframe` widget, a container that draws a border and a title label around its contents. It is the themed counterpart of [`tkinter.LabelFrame`](https://docs.python.org/3/library/tkinter.html#tkinter.LabelFrame "tkinter.LabelFrame")
 and inherits the common widget methods from [`Widget`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Widget "tkinter.ttk.Widget")
.

class tkinter.ttk.Menubutton(_master\=None_, _\*\*kw_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Menubutton "Link to this definition")

Ttk `Menubutton` widget, displays a textual label and/or image, and pops up a menu when pressed. It is the themed counterpart of [`tkinter.Menubutton`](https://docs.python.org/3/library/tkinter.html#tkinter.Menubutton "tkinter.Menubutton")
 and inherits the common widget methods from [`Widget`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Widget "tkinter.ttk.Widget")
.

class tkinter.ttk.OptionMenu(_master_, _variable_, _default\=None_, _\*values_, _\*\*kwargs_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.OptionMenu "Link to this definition")

Ttk `OptionMenu` widget, a [`Menubutton`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Menubutton "tkinter.ttk.Menubutton")
 that pops up a menu of mutually exclusive choices. _variable_ is the variable that tracks the currently selected value, _default_ is the value to set initially, and _values_ are the entries to display in the menu. A _command_ keyword argument may be given to specify a callable that is invoked with the selected value whenever the selection changes; the _style_ keyword argument sets the style used by the underlying menubutton; the _direction_ keyword argument sets where the menu is posted relative to the menubutton (one of `'above'`, `'below'` (the default), `'left'`, `'right'` or `'flush'`); and the _name_ keyword argument sets the Tk widget name.

set\_menu(_default\=None_, _\*values_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.OptionMenu.set_menu "Link to this definition")

Replace the entries of the menu with _values_. If _default_ is given, also set it as the current value of the _variable_.

destroy()[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.OptionMenu.destroy "Link to this definition")

Destroy this widget and its associated menu.

Changed in version 3.14: Added support for the _name_ keyword argument.

class tkinter.ttk.Panedwindow(_master\=None_, _\*\*kw_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Panedwindow "Link to this definition")

Ttk `Panedwindow` widget, displays a number of subwindows stacked either vertically or horizontally. The user may adjust the relative sizes of the subwindows by dragging the sash between panes. It is the themed counterpart of [`tkinter.PanedWindow`](https://docs.python.org/3/library/tkinter.html#tkinter.PanedWindow "tkinter.PanedWindow")
 and inherits the common widget methods from [`Widget`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Widget "tkinter.ttk.Widget")
, as well as the `add()` and `panes()` methods from `tkinter.PanedWindow`.

insert(_pos_, _child_, _\*\*kw_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Panedwindow.insert "Link to this definition")

Insert a pane containing _child_ at the position _pos_. _pos_ is either the string `'end'`, an integer index, or the name of a managed subwindow. If _child_ is already managed by the paned window, move it to the specified position. Any keyword arguments set pane options.

forget(_child_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Panedwindow.forget "Link to this definition")

Remove _child_, which may be either an integer index or the name of a managed subwindow, from the panes.

This shadows the inherited geometry-manager `forget()`; use [`pack_forget()`](https://docs.python.org/3/library/tkinter.html#tkinter.Pack.pack_forget "tkinter.Pack.pack_forget")
, [`grid_forget()`](https://docs.python.org/3/library/tkinter.html#tkinter.Grid.grid_forget "tkinter.Grid.grid_forget")
 or [`place_forget()`](https://docs.python.org/3/library/tkinter.html#tkinter.Place.place_forget "tkinter.Place.place_forget")
 to remove the widget itself from its manager.

pane(_pane_, _option\=None_, _\*\*kw_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Panedwindow.pane "Link to this definition")

Query or modify the options of the specified _pane_, where _pane_ is either an integer index or the name of a managed subwindow. If no arguments are given, return a dictionary of the pane option values. If _option_ is specified, return the value of that option. Otherwise, set the options given as keyword arguments to their corresponding values.

sashpos(_index_, _newpos\=None_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Panedwindow.sashpos "Link to this definition")

If _newpos_ is specified, set the position of sash number _index_ and return its new position. This may adjust the positions of adjacent sashes to ensure that positions are monotonically increasing; positions are also constrained to be between 0 and the total size of the widget. If _newpos_ is omitted, return the current position of the sash.

class tkinter.ttk.Radiobutton(_master\=None_, _\*\*kw_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Radiobutton "Link to this definition")

Ttk `Radiobutton` widget, used as part of a group to control a single shared variable by selecting one of several mutually exclusive values. It is the themed counterpart of [`tkinter.Radiobutton`](https://docs.python.org/3/library/tkinter.html#tkinter.Radiobutton "tkinter.Radiobutton")
 and inherits the common widget methods from [`Widget`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Widget "tkinter.ttk.Widget")
.

invoke()[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Radiobutton.invoke "Link to this definition")

Set the option variable to the button’s value, select the button, invoke the command associated with the button, and return its result.

class tkinter.ttk.Scale(_master\=None_, _\*\*kw_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Scale "Link to this definition")

Ttk `Scale` widget, displays a slider that lets the user select a numeric value from a range by moving the slider along a trough. It is the themed counterpart of [`tkinter.Scale`](https://docs.python.org/3/library/tkinter.html#tkinter.Scale "tkinter.Scale")
 and inherits the common widget methods from [`Widget`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Widget "tkinter.ttk.Widget")
.

configure(_cnf\=None_, _\*\*kw_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Scale.configure "Link to this definition")

Modify or query the widget options, like [`Widget.configure`](https://docs.python.org/3/library/tkinter.html#tkinter.Misc.configure "tkinter.Misc.configure")
. In addition, this method clips the `from` and `to` values so that the current value stays within the range defined by them.

Changed in version 3.9: Now returns the configuration value, like [`Widget.configure`](https://docs.python.org/3/library/tkinter.html#tkinter.Misc.configure "tkinter.Misc.configure")
.

get(_x\=None_, _y\=None_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Scale.get "Link to this definition")

Return the current value of the scale. If _x_ and _y_ are given, return the value corresponding to the pixel coordinate _x_, _y_ instead.

class tkinter.ttk.Scrollbar(_master\=None_, _\*\*kw_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Scrollbar "Link to this definition")

Ttk `Scrollbar` widget, controls the viewport of an associated scrollable widget such as a [`Treeview`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview "tkinter.ttk.Treeview")
, [`Entry`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Entry "tkinter.ttk.Entry")
 or [`tkinter.Text`](https://docs.python.org/3/library/tkinter.html#tkinter.Text "tkinter.Text")
. It is the themed counterpart of [`tkinter.Scrollbar`](https://docs.python.org/3/library/tkinter.html#tkinter.Scrollbar "tkinter.Scrollbar")
 and inherits the common widget methods from [`Widget`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Widget "tkinter.ttk.Widget")
, as well as the `set()` and `get()` methods from `tkinter.Scrollbar`.

class tkinter.ttk.Separator(_master\=None_, _\*\*kw_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Separator "Link to this definition")

Ttk `Separator` widget, displays a horizontal or vertical separator line. It has no direct counterpart in [`tkinter`](https://docs.python.org/3/library/tkinter.html#module-tkinter "tkinter: Interface to Tcl/Tk for graphical user interfaces")
 and inherits the common widget methods from [`Widget`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Widget "tkinter.ttk.Widget")
.

class tkinter.ttk.Sizegrip(_master\=None_, _\*\*kw_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Sizegrip "Link to this definition")

Ttk `Sizegrip` widget, displays a grip that allows the user to resize the containing toplevel window by pressing and dragging the grip, typically placed in the bottom-right corner. It has no direct counterpart in [`tkinter`](https://docs.python.org/3/library/tkinter.html#module-tkinter "tkinter: Interface to Tcl/Tk for graphical user interfaces")
 and inherits the common widget methods from [`Widget`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Widget "tkinter.ttk.Widget")
.

class tkinter.ttk.LabeledScale(_master\=None_, _variable\=None_, _from\_\=0_, _to\=10_, _\*\*kw_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.LabeledScale "Link to this definition")

A [`Frame`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Frame "tkinter.ttk.Frame")
 containing a [`Scale`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Scale "tkinter.ttk.Scale")
 and a [`Label`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Label "tkinter.ttk.Label")
 that shows the scale’s current value. _variable_ is the [`IntVar`](https://docs.python.org/3/library/tkinter.html#tkinter.IntVar "tkinter.IntVar")
 tracked by the scale (one is created if it is not given), and _from\__ and _to_ define the range of the scale.

destroy()[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.LabeledScale.destroy "Link to this definition")

Destroy this widget and remove the trace callback registered on the associated variable.

class tkinter.ttk.LabelFrame(_master\=None_, _\*\*kw_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.LabelFrame "Link to this definition")

Alias of [`Labelframe`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Labelframe "tkinter.ttk.Labelframe")
, kept for naming compatibility with [`tkinter.LabelFrame`](https://docs.python.org/3/library/tkinter.html#tkinter.LabelFrame "tkinter.LabelFrame")
.

class tkinter.ttk.PanedWindow(_master\=None_, _\*\*kw_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.PanedWindow "Link to this definition")

Alias of [`Panedwindow`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Panedwindow "tkinter.ttk.Panedwindow")
, kept for naming compatibility with [`tkinter.PanedWindow`](https://docs.python.org/3/library/tkinter.html#tkinter.PanedWindow "tkinter.PanedWindow")
.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`tkinter.ttk` — Tk themed widgets](https://docs.python.org/3/library/tkinter.ttk.html#)
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
        

#### Previous topic

[`tkinter.dnd` — Drag and drop support](https://docs.python.org/3/library/tkinter.dnd.html "previous chapter")

#### Next topic

[IDLE — Python editor and shell](https://docs.python.org/3/library/idle.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=tkinter.ttk+%E2%80%94+Tk+themed+widgets&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ftkinter.ttk.html&pagesource=library%2Ftkinter.ttk.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/tkinter.ttk.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/idle.html "IDLE — Python editor and shell")
     |
*   [previous](https://docs.python.org/3/library/tkinter.dnd.html "tkinter.dnd — Drag and drop support")
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
*   [`tkinter.ttk` — Tk themed widgets](https://docs.python.org/3/library/tkinter.ttk.html)
    
*    
    
    |
*   Theme Auto Light Dark |