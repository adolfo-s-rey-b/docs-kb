### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/tkinter.messagebox.html "tkinter.messagebox — Tkinter message prompts")
     |
*   [previous](https://docs.python.org/3/library/tkinter.font.html "tkinter.font — Tkinter font wrapper")
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
*   [Tkinter dialogs](https://docs.python.org/3/library/dialog.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Tkinter dialogs[¶](https://docs.python.org/3/library/dialog.html#tkinter-dialogs "Link to this heading")

=========================================================================================================

`tkinter.simpledialog` — Standard Tkinter input dialogs[¶](https://docs.python.org/3/library/dialog.html#module-tkinter.simpledialog "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------

**Source code:** [Lib/tkinter/simpledialog.py](https://github.com/python/cpython/tree/3.15/Lib/tkinter/simpledialog.py)

* * *

The `tkinter.simpledialog` module contains convenience classes and functions for creating simple modal dialogs to get a value from the user.

tkinter.simpledialog.askfloat(_title_, _prompt_, _\*_, _initialvalue\=None_, _minvalue\=None_, _maxvalue\=None_, _parent\=None_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.simpledialog.askfloat "Link to this definition")

tkinter.simpledialog.askinteger(_title_, _prompt_, _\*_, _initialvalue\=None_, _minvalue\=None_, _maxvalue\=None_, _parent\=None_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.simpledialog.askinteger "Link to this definition")

tkinter.simpledialog.askstring(_title_, _prompt_, _\*_, _initialvalue\=None_, _show\=None_, _parent\=None_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.simpledialog.askstring "Link to this definition")

Prompt the user to enter a value of the desired type and return it, or `None` if the dialog is cancelled.

_title_ is the dialog title and _prompt_ the message shown above the entry. _initialvalue_ is the value initially placed in the entry. _parent_ is the window over which the dialog is shown. `askinteger()` and `askfloat()` also accept _minvalue_ and _maxvalue_, which bound the accepted value. `askstring()` also accepts _show_, a character used to mask the entered text, for example `'*'` to hide a password.

class tkinter.simpledialog.Dialog(_parent_, _title\=None_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.simpledialog.Dialog "Link to this definition")

The base class for custom dialogs. Instantiating it shows the dialog modally and returns once the user closes it; the entered value is then available in the `result` attribute.

result[¶](https://docs.python.org/3/library/dialog.html#tkinter.simpledialog.Dialog.result "Link to this definition")

The value produced by [`apply()`](https://docs.python.org/3/library/dialog.html#tkinter.simpledialog.Dialog.apply "tkinter.simpledialog.Dialog.apply")
, or `None` if the dialog was cancelled.

body(_master_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.simpledialog.Dialog.body "Link to this definition")

Override to construct the dialog’s interface and return the widget that should have initial focus.

buttonbox()[¶](https://docs.python.org/3/library/dialog.html#tkinter.simpledialog.Dialog.buttonbox "Link to this definition")

Default behaviour adds OK and Cancel buttons. Override for custom button layouts.

validate()[¶](https://docs.python.org/3/library/dialog.html#tkinter.simpledialog.Dialog.validate "Link to this definition")

Validate the data entered by the user. Return true if it is valid, in which case the dialog proceeds to [`apply()`](https://docs.python.org/3/library/dialog.html#tkinter.simpledialog.Dialog.apply "tkinter.simpledialog.Dialog.apply")
; return false to keep the dialog open. The default implementation always returns true; override it to check the input.

apply()[¶](https://docs.python.org/3/library/dialog.html#tkinter.simpledialog.Dialog.apply "Link to this definition")

Process the data entered by the user, for example by storing it in the `result` attribute. Called after [`validate()`](https://docs.python.org/3/library/dialog.html#tkinter.simpledialog.Dialog.validate "tkinter.simpledialog.Dialog.validate")
 succeeds and just before the dialog is destroyed. The default implementation does nothing; override it to act on or store the result.

destroy()[¶](https://docs.python.org/3/library/dialog.html#tkinter.simpledialog.Dialog.destroy "Link to this definition")

Destroy the dialog window, clearing the reference to the widget that had the initial focus.

class tkinter.simpledialog.SimpleDialog(_master_, _text\=''_, _buttons\=\[\]_, _default\=None_, _cancel\=None_, _title\=None_, _class\_\=None_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.simpledialog.SimpleDialog "Link to this definition")

A simple modal dialog that displays the message _text_ above a row of push buttons whose labels are given by _buttons_, and returns the index of the button the user presses. _default_ is the index of the button activated by the Return key, _cancel_ the index returned when the window is closed through the window manager, _title_ the window title, and _class\__ the Tk class name of the window.

go()[¶](https://docs.python.org/3/library/dialog.html#tkinter.simpledialog.SimpleDialog.go "Link to this definition")

Display the dialog, wait until the user presses a button or closes the window, and return the index of the chosen button.

`tkinter.filedialog` — File selection dialogs[¶](https://docs.python.org/3/library/dialog.html#module-tkinter.filedialog "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------

**Source code:** [Lib/tkinter/filedialog.py](https://github.com/python/cpython/tree/3.15/Lib/tkinter/filedialog.py)

* * *

The `tkinter.filedialog` module provides classes and factory functions for creating file/directory selection windows.

### Native load/save dialogs[¶](https://docs.python.org/3/library/dialog.html#native-load-save-dialogs "Link to this heading")

The following classes and functions provide file dialog windows that combine a native look-and-feel with configuration options to customize behaviour. The following keyword arguments are applicable to the classes and functions listed below:

> _parent_ - the window to place the dialog on top of
> 
> _title_ - the title of the window
> 
> _initialdir_ - the directory that the dialog starts in
> 
> _initialfile_ - the file selected upon opening of the dialog
> 
> _filetypes_ - a sequence of (label, pattern) tuples, ‘\*’ wildcard is allowed
> 
> _defaultextension_ - default extension to append to file (save dialogs)
> 
> _multiple_ - when true, selection of multiple items is allowed

**Static factory functions**

The below functions when called create a modal, native look-and-feel dialog, wait for the user’s selection, and return it. The exact return value depends on the function (see below); when the dialog is cancelled it is an empty string, an empty tuple or `None`. The precise type of this empty value may vary between platforms and Tk versions, so test the result for truth rather than comparing it with a specific value.

tkinter.filedialog.askopenfile(_mode\='r'_, _\*\*options_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.askopenfile "Link to this definition")

tkinter.filedialog.askopenfiles(_mode\='r'_, _\*\*options_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.askopenfiles "Link to this definition")

Create an [`Open`](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.Open "tkinter.filedialog.Open")
 dialog. `askopenfile()` returns the opened file object, or `None` if the dialog is cancelled. `askopenfiles()` returns a list of the opened file objects, or an empty tuple if cancelled. The files are opened in mode _mode_ (read-only `'r'` by default).

tkinter.filedialog.asksaveasfile(_mode\='w'_, _\*\*options_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.asksaveasfile "Link to this definition")

Create a [`SaveAs`](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.SaveAs "tkinter.filedialog.SaveAs")
 dialog and return the opened file object, or `None` if the dialog is cancelled. The file is opened in mode _mode_ (`'w'` by default).

tkinter.filedialog.askopenfilename(_\*\*options_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.askopenfilename "Link to this definition")

tkinter.filedialog.askopenfilenames(_\*\*options_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.askopenfilenames "Link to this definition")

Create an [`Open`](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.Open "tkinter.filedialog.Open")
 dialog. `askopenfilename()` returns the selected filename as a string, or an empty string if the dialog is cancelled. `askopenfilenames()` returns a tuple of the selected filenames, or an empty tuple if cancelled.

tkinter.filedialog.asksaveasfilename(_\*\*options_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.asksaveasfilename "Link to this definition")

Create a [`SaveAs`](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.SaveAs "tkinter.filedialog.SaveAs")
 dialog and return the selected filename as a string, or an empty string if the dialog is cancelled.

tkinter.filedialog.askdirectory(_\*\*options_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.askdirectory "Link to this definition")

Prompt the user to select a directory, and return its path as a string, or an empty string if the dialog is cancelled. Additional keyword option: _mustexist_ - if true, the user may only select an existing directory (false by default).

class tkinter.filedialog.Open(_master\=None_, _\*\*options_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.Open "Link to this definition")

class tkinter.filedialog.SaveAs(_master\=None_, _\*\*options_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.SaveAs "Link to this definition")

class tkinter.filedialog.Directory(_master\=None_, _\*\*options_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.Directory "Link to this definition")

The above three classes provide native dialog windows for loading and saving files and for selecting a directory.

**Convenience classes**

The below classes are used for creating file/directory windows from scratch. These do not emulate the native look-and-feel of the platform.

Note

The _FileDialog_ class should be subclassed for custom event handling and behaviour.

class tkinter.filedialog.FileDialog(_master_, _title\=None_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.FileDialog "Link to this definition")

Create a basic file selection dialog.

cancel\_command(_event\=None_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.FileDialog.cancel_command "Link to this definition")

Trigger the termination of the dialog window.

dirs\_double\_event(_event_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.FileDialog.dirs_double_event "Link to this definition")

Event handler for double-click event on directory.

dirs\_select\_event(_event_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.FileDialog.dirs_select_event "Link to this definition")

Event handler for click event on directory.

files\_double\_event(_event_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.FileDialog.files_double_event "Link to this definition")

Event handler for double-click event on file.

files\_select\_event(_event_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.FileDialog.files_select_event "Link to this definition")

Event handler for single-click event on file.

filter\_command(_event\=None_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.FileDialog.filter_command "Link to this definition")

Filter the files by directory.

get\_filter()[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.FileDialog.get_filter "Link to this definition")

Retrieve the file filter currently in use.

get\_selection()[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.FileDialog.get_selection "Link to this definition")

Retrieve the currently selected item.

go(_dir\_or\_file\=os.curdir_, _pattern\='\*'_, _default\=''_, _key\=None_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.FileDialog.go "Link to this definition")

Render dialog and start event loop.

ok\_event(_event_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.FileDialog.ok_event "Link to this definition")

Exit dialog returning current selection.

ok\_command()[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.FileDialog.ok_command "Link to this definition")

Called when the user confirms the current selection. The base implementation accepts the selection and closes the dialog; [`LoadFileDialog`](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.LoadFileDialog "tkinter.filedialog.LoadFileDialog")
 and [`SaveFileDialog`](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.SaveFileDialog "tkinter.filedialog.SaveFileDialog")
 override it to check the selection first.

quit(_how\=None_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.FileDialog.quit "Link to this definition")

Exit dialog returning filename, if any.

set\_filter(_dir_, _pat_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.FileDialog.set_filter "Link to this definition")

Set the file filter.

set\_selection(_file_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.FileDialog.set_selection "Link to this definition")

Update the current file selection to _file_.

class tkinter.filedialog.LoadFileDialog(_master_, _title\=None_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.LoadFileDialog "Link to this definition")

A subclass of FileDialog that creates a dialog window for selecting an existing file.

ok\_command()[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.LoadFileDialog.ok_command "Link to this definition")

Test that a file is provided and that the selection indicates an already existing file.

class tkinter.filedialog.SaveFileDialog(_master_, _title\=None_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.SaveFileDialog "Link to this definition")

A subclass of FileDialog that creates a dialog window for selecting a destination file.

ok\_command()[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.SaveFileDialog.ok_command "Link to this definition")

Test whether or not the selection points to a valid file that is not a directory. Confirmation is required if an already existing file is selected.

`tkinter.commondialog` — Dialog window templates[¶](https://docs.python.org/3/library/dialog.html#module-tkinter.commondialog "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------

**Source code:** [Lib/tkinter/commondialog.py](https://github.com/python/cpython/tree/3.15/Lib/tkinter/commondialog.py)

* * *

The `tkinter.commondialog` module provides the [`Dialog`](https://docs.python.org/3/library/dialog.html#tkinter.commondialog.Dialog "tkinter.commondialog.Dialog")
 class that is the base class for dialogs defined in other supporting modules.

class tkinter.commondialog.Dialog(_master\=None_, _\*\*options_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.commondialog.Dialog "Link to this definition")

show(_\*\*options_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.commondialog.Dialog.show "Link to this definition")

Render the Dialog window.

`tkinter.dialog` — Classic Tk dialog boxes[¶](https://docs.python.org/3/library/dialog.html#module-tkinter.dialog "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------

**Source code:** [Lib/tkinter/dialog.py](https://github.com/python/cpython/tree/3.15/Lib/tkinter/dialog.py)

* * *

The `tkinter.dialog` module provides a simple modal dialog box built on the classic (non-themed) Tk widgets.

tkinter.dialog.DIALOG\_ICON[¶](https://docs.python.org/3/library/dialog.html#tkinter.dialog.DIALOG_ICON "Link to this definition")

The name of a bitmap (`'questhead'`) suitable for use as the _bitmap_ of a [`Dialog`](https://docs.python.org/3/library/dialog.html#tkinter.dialog.Dialog "tkinter.dialog.Dialog")
.

class tkinter.dialog.Dialog(_master\=None_, _cnf\={}_, _\*\*kw_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.dialog.Dialog "Link to this definition")

Display a modal dialog box built from the classic (non-themed) Tk widgets and wait for the user to press one of its buttons. The options, given through _cnf_ or as keyword arguments, are all required: _title_ (the window title), _text_ (the message), _bitmap_ (the name of a bitmap icon, such as [`DIALOG_ICON`](https://docs.python.org/3/library/dialog.html#tkinter.dialog.DIALOG_ICON "tkinter.dialog.DIALOG_ICON")
), _default_ (the index of the default button) and _strings_ (the sequence of button labels). After construction, the `num` attribute holds the index of the button the user pressed.

destroy()[¶](https://docs.python.org/3/library/dialog.html#tkinter.dialog.Dialog.destroy "Link to this definition")

Do nothing. The dialog window is destroyed automatically before the constructor returns, so there is nothing left for this method to do.

See also

Modules [`tkinter.messagebox`](https://docs.python.org/3/library/tkinter.messagebox.html#module-tkinter.messagebox "tkinter.messagebox: Various types of alert dialogs")
, [Reading and writing files](https://docs.python.org/3/tutorial/inputoutput.html#tut-files)

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Tkinter dialogs](https://docs.python.org/3/library/dialog.html#)
    *   [`tkinter.simpledialog` — Standard Tkinter input dialogs](https://docs.python.org/3/library/dialog.html#module-tkinter.simpledialog)
        
    *   [`tkinter.filedialog` — File selection dialogs](https://docs.python.org/3/library/dialog.html#module-tkinter.filedialog)
        *   [Native load/save dialogs](https://docs.python.org/3/library/dialog.html#native-load-save-dialogs)
            
    *   [`tkinter.commondialog` — Dialog window templates](https://docs.python.org/3/library/dialog.html#module-tkinter.commondialog)
        
    *   [`tkinter.dialog` — Classic Tk dialog boxes](https://docs.python.org/3/library/dialog.html#module-tkinter.dialog)
        

#### Previous topic

[`tkinter.font` — Tkinter font wrapper](https://docs.python.org/3/library/tkinter.font.html "previous chapter")

#### Next topic

[`tkinter.messagebox` — Tkinter message prompts](https://docs.python.org/3/library/tkinter.messagebox.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Tkinter+dialogs&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fdialog.html&pagesource=library%2Fdialog.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/dialog.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/tkinter.messagebox.html "tkinter.messagebox — Tkinter message prompts")
     |
*   [previous](https://docs.python.org/3/library/tkinter.font.html "tkinter.font — Tkinter font wrapper")
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
*   [Tkinter dialogs](https://docs.python.org/3/library/dialog.html)
    
*    
    
    |
*   Theme Auto Light Dark |