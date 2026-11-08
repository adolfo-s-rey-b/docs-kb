### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/curses.ascii.html "curses.ascii — Utilities for ASCII characters")
     |
*   [previous](https://docs.python.org/3/library/fileinput.html "fileinput — Iterate over lines from multiple input streams")
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
*   [`curses` — Terminal handling for character-cell displays](https://docs.python.org/3/library/curses.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`curses` — Terminal handling for character-cell displays[¶](https://docs.python.org/3/library/curses.html#module-curses "Link to this heading")

================================================================================================================================================

**Source code:** [Lib/curses](https://github.com/python/cpython/tree/3.15/Lib/curses)

* * *

The `curses` module provides an interface to the curses library, the de-facto standard for portable advanced terminal handling.

While curses is most widely used in the Unix environment, versions are available for Windows, DOS, and possibly other systems as well. This extension module is designed to match the API of ncurses, an open-source curses library hosted on Linux and the BSD variants of Unix.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: not Android, not iOS, not WASI.

This module is not supported on [mobile platforms](https://docs.python.org/3/library/intro.html#mobile-availability)
 or [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability)
.

This is an [optional module](https://docs.python.org/3/glossary.html#term-optional-module)
. If it is missing from your copy of CPython, look for documentation from your distributor (that is, whoever provided Python to you). If you are the distributor, see [Requirements for optional modules](https://docs.python.org/3/using/configure.html#optional-module-requirements)
.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

Note

Whenever the documentation mentions a _character_ it can be specified as an integer, a one-character Unicode string or a one-byte byte string. An integer is the code of a single encoded byte, optionally combined with attributes and a color pair, as returned by [`window.inch()`](https://docs.python.org/3/library/curses.html#curses.window.inch "curses.window.inch")
.

Whenever the documentation mentions a _character string_ it can be specified as a Unicode string or a byte string.

Note

Whether curses may be used from several threads depends on the underlying library and how it was built. In many implementations, including the default build of ncurses, the screen state is shared and not thread-safe; since the blocking and refresh methods (such as [`getch()`](https://docs.python.org/3/library/curses.html#curses.window.getch "curses.window.getch")
 and [`refresh()`](https://docs.python.org/3/library/curses.html#curses.window.refresh "curses.window.refresh")
) release the [GIL](https://docs.python.org/3/glossary.html#term-GIL)
, unsynchronized use from several threads can then crash the interpreter. Serialize the calls.

See also

Module [`curses.ascii`](https://docs.python.org/3/library/curses.ascii.html#module-curses.ascii "curses.ascii: Constants and set-membership functions for ASCII characters.")

Utilities for working with ASCII characters, regardless of your locale settings.

Module [`curses.panel`](https://docs.python.org/3/library/curses.panel.html#module-curses.panel "curses.panel: A panel stack extension that adds depth to  curses windows.")

A panel stack extension that adds depth to curses windows.

Module [`curses.textpad`](https://docs.python.org/3/library/curses.html#module-curses.textpad "curses.textpad: Emacs-like input editing in a curses window.")

Editable text widget for curses supporting **Emacs**\-like bindings.

[Curses Programming with Python](https://docs.python.org/3/howto/curses.html#curses-howto)

Tutorial material on using curses with Python, by Andrew Kuchling and Eric Raymond.

Functions[¶](https://docs.python.org/3/library/curses.html#functions "Link to this heading")

---------------------------------------------------------------------------------------------

The module `curses` defines the following exception:

exception curses.error[¶](https://docs.python.org/3/library/curses.html#curses.error "Link to this definition")

Exception raised when a curses library function returns an error.

Note

Whenever _x_ or _y_ arguments to a function or a method are optional, they default to the current cursor location. Whenever _attr_ is optional, it defaults to [`A_NORMAL`](https://docs.python.org/3/library/curses.html#curses.A_NORMAL "curses.A_NORMAL")
.

The module `curses` defines the following functions:

curses.assume\_default\_colors(_fg_, _bg_, _/_)[¶](https://docs.python.org/3/library/curses.html#curses.assume_default_colors "Link to this definition")

Allow use of default values for colors on terminals supporting this feature. Use this to support transparency in your application.

*   Assign terminal default foreground/background colors to color number `-1`. So `init_pair(x, COLOR_RED, -1)` will initialize pair _x_ as red on default background and `init_pair(x, -1, COLOR_BLUE)` will initialize pair _x_ as default foreground on blue.
    
*   Change the definition of the color-pair `0` to `(fg, bg)`.
    

This is an ncurses extension.

Added in version 3.14.

curses.baudrate()[¶](https://docs.python.org/3/library/curses.html#curses.baudrate "Link to this definition")

Return the output speed of the terminal in bits per second. On software terminal emulators it will have a fixed high value. Included for historical reasons; in former times, it was used to write output loops for time delays and occasionally to change interfaces depending on the line speed.

curses.beep()[¶](https://docs.python.org/3/library/curses.html#curses.beep "Link to this definition")

Emit a short attention sound.

curses.can\_change\_color()[¶](https://docs.python.org/3/library/curses.html#curses.can_change_color "Link to this definition")

Return `True` or `False`, depending on whether the programmer can change the colors displayed by the terminal.

curses.cbreak()[¶](https://docs.python.org/3/library/curses.html#curses.cbreak "Link to this definition")

Enter cbreak mode. In cbreak mode (sometimes called “rare” mode) normal tty line buffering is turned off and characters are available to be read one by one. However, unlike raw mode, special characters (interrupt, quit, suspend, and flow control) retain their effects on the tty driver and calling program. Calling first [`raw()`](https://docs.python.org/3/library/curses.html#curses.raw "curses.raw")
 then `cbreak()` leaves the terminal in cbreak mode.

curses.color\_content(_color\_number_)[¶](https://docs.python.org/3/library/curses.html#curses.color_content "Link to this definition")

Return the intensity of the red, green, and blue (RGB) components in the color _color\_number_, which must be between `0` and `COLORS - 1`. Return a 3-tuple, containing the R,G,B values for the given color, which will be between `0` (no component) and `1000` (maximum amount of component). Raise an exception if the color is not supported.

curses.color\_pair(_pair\_number_)[¶](https://docs.python.org/3/library/curses.html#curses.color_pair "Link to this definition")

Return the attribute value for displaying text in the specified color pair. Only the first 256 color pairs are supported. This attribute value can be combined with [`A_STANDOUT`](https://docs.python.org/3/library/curses.html#curses.A_STANDOUT "curses.A_STANDOUT")
, [`A_REVERSE`](https://docs.python.org/3/library/curses.html#curses.A_REVERSE "curses.A_REVERSE")
, and the other `A_*` attributes. [`pair_number()`](https://docs.python.org/3/library/curses.html#curses.pair_number "curses.pair_number")
 is the counterpart to this function.

curses.curs\_set(_visibility_)[¶](https://docs.python.org/3/library/curses.html#curses.curs_set "Link to this definition")

Set the cursor state. _visibility_ can be set to `0`, `1`, or `2`, for invisible, normal, or very visible. If the terminal supports the visibility requested, return the previous cursor state; otherwise raise an exception. On many terminals, the “visible” mode is an underline cursor and the “very visible” mode is a block cursor.

curses.def\_prog\_mode()[¶](https://docs.python.org/3/library/curses.html#curses.def_prog_mode "Link to this definition")

Save the current terminal mode as the “program” mode, the mode when the running program is using curses. (Its counterpart is the “shell” mode, for when the program is not in curses.) Subsequent calls to [`reset_prog_mode()`](https://docs.python.org/3/library/curses.html#curses.reset_prog_mode "curses.reset_prog_mode")
 will restore this mode.

curses.def\_shell\_mode()[¶](https://docs.python.org/3/library/curses.html#curses.def_shell_mode "Link to this definition")

Save the current terminal mode as the “shell” mode, the mode when the running program is not using curses. (Its counterpart is the “program” mode, when the program is using curses capabilities.) Subsequent calls to [`reset_shell_mode()`](https://docs.python.org/3/library/curses.html#curses.reset_shell_mode "curses.reset_shell_mode")
 will restore this mode.

curses.delay\_output(_ms_)[¶](https://docs.python.org/3/library/curses.html#curses.delay_output "Link to this definition")

Insert an _ms_ millisecond pause in output.

curses.doupdate()[¶](https://docs.python.org/3/library/curses.html#curses.doupdate "Link to this definition")

Update the physical screen. The curses library keeps two data structures, one representing the current physical screen contents and a virtual screen representing the desired next state. The `doupdate()` function updates the physical screen to match the virtual screen.

The virtual screen may be updated by a [`noutrefresh()`](https://docs.python.org/3/library/curses.html#curses.window.noutrefresh "curses.window.noutrefresh")
 call after write operations such as [`addstr()`](https://docs.python.org/3/library/curses.html#curses.window.addstr "curses.window.addstr")
 have been performed on a window. The normal [`refresh()`](https://docs.python.org/3/library/curses.html#curses.window.refresh "curses.window.refresh")
 call is simply `noutrefresh()` followed by `doupdate()`; if you have to update multiple windows, you can speed performance and perhaps reduce screen flicker by issuing `noutrefresh()` calls on all windows, followed by a single `doupdate()`.

curses.echo()[¶](https://docs.python.org/3/library/curses.html#curses.echo "Link to this definition")

Enter echo mode. In echo mode, each character input is echoed to the screen as it is entered.

curses.endwin()[¶](https://docs.python.org/3/library/curses.html#curses.endwin "Link to this definition")

De-initialize the library, and return terminal to normal status.

curses.erasechar()[¶](https://docs.python.org/3/library/curses.html#curses.erasechar "Link to this definition")

Return the user’s current erase character as a one-byte bytes object. Under Unix operating systems this is a property of the controlling tty of the curses program, and is not set by the curses library itself.

curses.filter()[¶](https://docs.python.org/3/library/curses.html#curses.filter "Link to this definition")

The `filter()` routine, if used, must be called before [`initscr()`](https://docs.python.org/3/library/curses.html#curses.initscr "curses.initscr")
 is called. The effect is that, during the initialization, `LINES` is set to `1`; the capabilities `clear`, `cup`, `cud`, `cud1`, `cuu1`, `cuu`, `vpa` are disabled; and the `home` string is set to the value of `cr`. The effect is that the cursor is confined to the current line, and so are screen updates. This may be used for enabling character-at-a-time line editing without touching the rest of the screen.

curses.flash()[¶](https://docs.python.org/3/library/curses.html#curses.flash "Link to this definition")

Flash the screen. That is, change it to reverse-video and then change it back in a short interval. Some people prefer such as ‘visible bell’ to the audible attention signal produced by [`beep()`](https://docs.python.org/3/library/curses.html#curses.beep "curses.beep")
.

curses.flushinp()[¶](https://docs.python.org/3/library/curses.html#curses.flushinp "Link to this definition")

Flush all input buffers. This throws away any typeahead that has been typed by the user and has not yet been processed by the program.

curses.getmouse()[¶](https://docs.python.org/3/library/curses.html#curses.getmouse "Link to this definition")

After [`getch()`](https://docs.python.org/3/library/curses.html#curses.window.getch "curses.window.getch")
 returns [`KEY_MOUSE`](https://docs.python.org/3/library/curses.html#curses.KEY_MOUSE "curses.KEY_MOUSE")
 to signal a mouse event, this method should be called to retrieve the queued mouse event, represented as a 5-tuple `(id, x, y, z, bstate)`. _id_ is an ID value used to distinguish multiple devices, and _x_, _y_, _z_ are the event’s coordinates. (_z_ is currently unused.) _bstate_ is an integer value whose bits will be set to indicate the type of event, and will be the bitwise OR of one or more of the following constants, where _n_ is the button number from 1 to 5: [`BUTTONn_PRESSED`](https://docs.python.org/3/library/curses.html#curses.BUTTONn_PRESSED "curses.BUTTONn_PRESSED")
, [`BUTTONn_RELEASED`](https://docs.python.org/3/library/curses.html#curses.BUTTONn_RELEASED "curses.BUTTONn_RELEASED")
, [`BUTTONn_CLICKED`](https://docs.python.org/3/library/curses.html#curses.BUTTONn_CLICKED "curses.BUTTONn_CLICKED")
, [`BUTTONn_DOUBLE_CLICKED`](https://docs.python.org/3/library/curses.html#curses.BUTTONn_DOUBLE_CLICKED "curses.BUTTONn_DOUBLE_CLICKED")
, [`BUTTONn_TRIPLE_CLICKED`](https://docs.python.org/3/library/curses.html#curses.BUTTONn_TRIPLE_CLICKED "curses.BUTTONn_TRIPLE_CLICKED")
, [`BUTTON_SHIFT`](https://docs.python.org/3/library/curses.html#curses.BUTTON_SHIFT "curses.BUTTON_SHIFT")
, [`BUTTON_CTRL`](https://docs.python.org/3/library/curses.html#curses.BUTTON_CTRL "curses.BUTTON_CTRL")
, [`BUTTON_ALT`](https://docs.python.org/3/library/curses.html#curses.BUTTON_ALT "curses.BUTTON_ALT")
.

Changed in version 3.10: The `BUTTON5_*` constants are now exposed if they are provided by the underlying curses library.

curses.getsyx()[¶](https://docs.python.org/3/library/curses.html#curses.getsyx "Link to this definition")

Return the current coordinates of the virtual screen cursor as a tuple `(y, x)`. If [`leaveok`](https://docs.python.org/3/library/curses.html#curses.window.leaveok "curses.window.leaveok")
 is currently `True`, then return `(-1, -1)`.

curses.getwin(_file_)[¶](https://docs.python.org/3/library/curses.html#curses.getwin "Link to this definition")

Read window-related data stored in the file by an earlier [`window.putwin()`](https://docs.python.org/3/library/curses.html#curses.window.putwin "curses.window.putwin")
 call. The routine then creates and initializes a new window using that data, returning the new window object. The _file_ argument must be a file object opened for reading in binary mode.

curses.has\_colors()[¶](https://docs.python.org/3/library/curses.html#curses.has_colors "Link to this definition")

Return `True` if the terminal can display colors; otherwise, return `False`.

curses.has\_extended\_color\_support()[¶](https://docs.python.org/3/library/curses.html#curses.has_extended_color_support "Link to this definition")

Return `True` if the module supports extended colors; otherwise, return `False`. Extended color support allows more than 256 color pairs for terminals that support more than 16 colors (for example, xterm-256color).

Extended color support requires ncurses version 6.1 or later.

Added in version 3.10.

curses.has\_ic()[¶](https://docs.python.org/3/library/curses.html#curses.has_ic "Link to this definition")

Return `True` if the terminal has insert- and delete-character capabilities. This function is included for historical reasons only, as all modern software terminal emulators have such capabilities.

curses.has\_il()[¶](https://docs.python.org/3/library/curses.html#curses.has_il "Link to this definition")

Return `True` if the terminal has insert- and delete-line capabilities, or can simulate them using scrolling regions. This function is included for historical reasons only, as all modern software terminal emulators have such capabilities.

curses.has\_key(_ch_)[¶](https://docs.python.org/3/library/curses.html#curses.has_key "Link to this definition")

Take a key value _ch_, and return `True` if the current terminal type recognizes a key with that value.

curses.halfdelay(_tenths_)[¶](https://docs.python.org/3/library/curses.html#curses.halfdelay "Link to this definition")

Used for half-delay mode, which is similar to cbreak mode in that characters typed by the user are immediately available to the program. However, after blocking for _tenths_ tenths of seconds, if nothing has been typed, [`getch()`](https://docs.python.org/3/library/curses.html#curses.window.getch "curses.window.getch")
 returns `-1`, while [`getkey()`](https://docs.python.org/3/library/curses.html#curses.window.getkey "curses.window.getkey")
 and [`get_wch()`](https://docs.python.org/3/library/curses.html#curses.window.get_wch "curses.window.get_wch")
 raise [`curses.error`](https://docs.python.org/3/library/curses.html#curses.error "curses.error")
. The value of _tenths_ must be a number between `1` and `255`. Use [`nocbreak()`](https://docs.python.org/3/library/curses.html#curses.nocbreak "curses.nocbreak")
 to leave half-delay mode.

curses.init\_color(_color\_number_, _r_, _g_, _b_)[¶](https://docs.python.org/3/library/curses.html#curses.init_color "Link to this definition")

Change the definition of a color, taking the number of the color to be changed followed by three RGB values (for the amounts of red, green, and blue components). The value of _color\_number_ must be between `0` and `COLORS - 1`. Each of _r_, _g_, _b_, must be a value between `0` and `1000`. When `init_color()` is used, all occurrences of that color on the screen immediately change to the new definition. This function is a no-op on most terminals; it is active only if [`can_change_color()`](https://docs.python.org/3/library/curses.html#curses.can_change_color "curses.can_change_color")
 returns `True`.

curses.init\_pair(_pair\_number_, _fg_, _bg_)[¶](https://docs.python.org/3/library/curses.html#curses.init_pair "Link to this definition")

Change the definition of a color-pair. It takes three arguments: the number of the color-pair to be changed, the foreground color number, and the background color number. The value of _pair\_number_ must be between `1` and `COLOR_PAIRS - 1` (the `0` color pair can only be changed by [`use_default_colors()`](https://docs.python.org/3/library/curses.html#curses.use_default_colors "curses.use_default_colors")
 and [`assume_default_colors()`](https://docs.python.org/3/library/curses.html#curses.assume_default_colors "curses.assume_default_colors")
). The value of _fg_ and _bg_ arguments must be between `0` and `COLORS - 1`, or, after calling `use_default_colors()` or `assume_default_colors()`, `-1`. If the color-pair was previously initialized, the screen is refreshed and all occurrences of that color-pair are changed to the new definition.

curses.initscr()[¶](https://docs.python.org/3/library/curses.html#curses.initscr "Link to this definition")

Initialize the library. Return a [window](https://docs.python.org/3/library/curses.html#curses-window-objects)
 object which represents the whole screen.

See [`setupterm()`](https://docs.python.org/3/library/curses.html#curses.setupterm "curses.setupterm")
 for a caveat about calling it before this function.

Note

If there is an error opening the terminal, the underlying curses library may cause the interpreter to exit.

curses.intrflush(_flag_)[¶](https://docs.python.org/3/library/curses.html#curses.intrflush "Link to this definition")

If _flag_ is `True`, pressing an interrupt key (interrupt, break, or quit) will flush all output in the terminal driver queue. If _flag_ is `False`, no flushing is done.

curses.is\_term\_resized(_nlines_, _ncols_)[¶](https://docs.python.org/3/library/curses.html#curses.is_term_resized "Link to this definition")

Return `True` if [`resize_term()`](https://docs.python.org/3/library/curses.html#curses.resize_term "curses.resize_term")
 would modify the window structure, `False` otherwise.

curses.isendwin()[¶](https://docs.python.org/3/library/curses.html#curses.isendwin "Link to this definition")

Return `True` if [`endwin()`](https://docs.python.org/3/library/curses.html#curses.endwin "curses.endwin")
 has been called (that is, the curses library has been deinitialized).

curses.keyname(_k_)[¶](https://docs.python.org/3/library/curses.html#curses.keyname "Link to this definition")

Return the name of the key numbered _k_ as a bytes object. The name of a key generating printable ASCII character is the key’s character. The name of a control-key combination is a two-byte bytes object consisting of a caret (`b'^'`) followed by the corresponding printable ASCII character. The name of an alt-key combination (128–255) is a bytes object consisting of the prefix `b'M-'` followed by the name of the corresponding ASCII character.

Raise a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 if _k_ is negative.

curses.killchar()[¶](https://docs.python.org/3/library/curses.html#curses.killchar "Link to this definition")

Return the user’s current line kill character as a one-byte bytes object. Under Unix operating systems this is a property of the controlling tty of the curses program, and is not set by the curses library itself.

curses.longname()[¶](https://docs.python.org/3/library/curses.html#curses.longname "Link to this definition")

Return a bytes object containing the terminfo long name field describing the current terminal. The maximum length of a verbose description is 128 characters. It is defined only after the call to [`initscr()`](https://docs.python.org/3/library/curses.html#curses.initscr "curses.initscr")
.

curses.meta(_flag_)[¶](https://docs.python.org/3/library/curses.html#curses.meta "Link to this definition")

If _flag_ is `True`, allow 8-bit characters to be input. If _flag_ is `False`, allow only 7-bit chars.

curses.mouseinterval(_interval_)[¶](https://docs.python.org/3/library/curses.html#curses.mouseinterval "Link to this definition")

Set the maximum time in milliseconds that can elapse between press and release events in order for them to be recognized as a click, and return the previous interval value. The default value is 166 milliseconds, or one sixth of a second. Use a negative _interval_ to obtain the interval value without changing it.

curses.mousemask(_mousemask_)[¶](https://docs.python.org/3/library/curses.html#curses.mousemask "Link to this definition")

Set the mouse events to be reported, and return a tuple `(availmask, oldmask)`. _availmask_ indicates which of the specified mouse events can be reported; on complete failure it returns `0`. _oldmask_ is the previous value of the mouse event mask. If this function is never called, no mouse events are ever reported.

curses.napms(_ms_)[¶](https://docs.python.org/3/library/curses.html#curses.napms "Link to this definition")

Sleep for _ms_ milliseconds.

curses.newpad(_nlines_, _ncols_)[¶](https://docs.python.org/3/library/curses.html#curses.newpad "Link to this definition")

Create and return a pointer to a new pad data structure with the given number of lines and columns. Return a pad as a window object.

A pad is like a window, except that it is not restricted by the screen size, and is not necessarily associated with a particular part of the screen. Pads can be used when a large window is needed, and only a part of the window will be on the screen at one time. Automatic refreshes of pads (such as from scrolling or echoing of input) do not occur. The [`refresh()`](https://docs.python.org/3/library/curses.html#curses.window.refresh "curses.window.refresh")
 and [`noutrefresh()`](https://docs.python.org/3/library/curses.html#curses.window.noutrefresh "curses.window.noutrefresh")
 methods of a pad require 6 arguments to specify the part of the pad to be displayed and the location on the screen to be used for the display. The arguments are _pminrow_, _pmincol_, _sminrow_, _smincol_, _smaxrow_, _smaxcol_; the _p_ arguments refer to the upper-left corner of the pad region to be displayed and the _s_ arguments define a clipping box on the screen within which the pad region is to be displayed.

curses.newwin(_nlines_, _ncols_)[¶](https://docs.python.org/3/library/curses.html#curses.newwin "Link to this definition")

curses.newwin(_nlines_, _ncols_, _begin\_y_, _begin\_x_)

Return a new [window](https://docs.python.org/3/library/curses.html#curses-window-objects)
, whose left-upper corner is at `(begin_y, begin_x)`, and whose height/width is _nlines_/_ncols_.

By default, the window will extend from the specified position to the lower right corner of the screen.

curses.nl(_flag\=True_)[¶](https://docs.python.org/3/library/curses.html#curses.nl "Link to this definition")

Enter newline mode. This mode translates the return key into newline on input, and translates newline into return and line-feed on output. Newline mode is initially on.

If _flag_ is `False`, the effect is the same as calling [`nonl()`](https://docs.python.org/3/library/curses.html#curses.nonl "curses.nonl")
.

curses.nocbreak()[¶](https://docs.python.org/3/library/curses.html#curses.nocbreak "Link to this definition")

Leave cbreak mode. Return to normal “cooked” mode with line buffering.

curses.noecho()[¶](https://docs.python.org/3/library/curses.html#curses.noecho "Link to this definition")

Leave echo mode. Echoing of input characters is turned off.

curses.nonl()[¶](https://docs.python.org/3/library/curses.html#curses.nonl "Link to this definition")

Leave newline mode. Disable translation of return into newline on input, and disable low-level translation of newline into newline/return on output (but this does not change the behavior of `addch('\n')`, which always does the equivalent of return and line feed on the virtual screen). With translation off, curses can sometimes speed up vertical motion a little; also, it will be able to detect the return key on input.

curses.noqiflush()[¶](https://docs.python.org/3/library/curses.html#curses.noqiflush "Link to this definition")

When the `noqiflush()` routine is used, normal flush of input and output queues associated with the `INTR`, `QUIT` and `SUSP` characters will not be done. You may want to call `noqiflush()` in a signal handler if you want output to continue as though the interrupt had not occurred, after the handler exits.

curses.noraw()[¶](https://docs.python.org/3/library/curses.html#curses.noraw "Link to this definition")

Leave raw mode. Return to normal “cooked” mode with line buffering.

curses.pair\_content(_pair\_number_)[¶](https://docs.python.org/3/library/curses.html#curses.pair_content "Link to this definition")

Return a tuple `(fg, bg)` containing the colors for the requested color pair. The value of _pair\_number_ must be between `0` and `COLOR_PAIRS - 1`.

curses.pair\_number(_attr_)[¶](https://docs.python.org/3/library/curses.html#curses.pair_number "Link to this definition")

Return the number of the color-pair set by the attribute value _attr_. [`color_pair()`](https://docs.python.org/3/library/curses.html#curses.color_pair "curses.color_pair")
 is the counterpart to this function.

curses.putp(_str_)[¶](https://docs.python.org/3/library/curses.html#curses.putp "Link to this definition")

Equivalent to `tputs(str, 1, putchar)`; emit the value of a specified terminfo capability, a bytes object, for the current terminal. Note that the output of `putp()` always goes to standard output.

[`setupterm()`](https://docs.python.org/3/library/curses.html#curses.setupterm "curses.setupterm")
 (or [`initscr()`](https://docs.python.org/3/library/curses.html#curses.initscr "curses.initscr")
) must be called first.

curses.qiflush(\[_flag_\])[¶](https://docs.python.org/3/library/curses.html#curses.qiflush "Link to this definition")

If _flag_ is `False`, the effect is the same as calling [`noqiflush()`](https://docs.python.org/3/library/curses.html#curses.noqiflush "curses.noqiflush")
. If _flag_ is `True`, or no argument is provided, the queues will be flushed when these control characters are read.

curses.raw()[¶](https://docs.python.org/3/library/curses.html#curses.raw "Link to this definition")

Enter raw mode. In raw mode, normal line buffering and processing of interrupt, quit, suspend, and flow control keys are turned off; characters are presented to curses input functions one by one.

curses.reset\_prog\_mode()[¶](https://docs.python.org/3/library/curses.html#curses.reset_prog_mode "Link to this definition")

Restore the terminal to “program” mode, as previously saved by [`def_prog_mode()`](https://docs.python.org/3/library/curses.html#curses.def_prog_mode "curses.def_prog_mode")
.

curses.reset\_shell\_mode()[¶](https://docs.python.org/3/library/curses.html#curses.reset_shell_mode "Link to this definition")

Restore the terminal to “shell” mode, as previously saved by [`def_shell_mode()`](https://docs.python.org/3/library/curses.html#curses.def_shell_mode "curses.def_shell_mode")
.

curses.resetty()[¶](https://docs.python.org/3/library/curses.html#curses.resetty "Link to this definition")

Restore the state of the terminal modes to what it was at the last call to [`savetty()`](https://docs.python.org/3/library/curses.html#curses.savetty "curses.savetty")
.

curses.resize\_term(_nlines_, _ncols_)[¶](https://docs.python.org/3/library/curses.html#curses.resize_term "Link to this definition")

Backend function used by [`resizeterm()`](https://docs.python.org/3/library/curses.html#curses.resizeterm "curses.resizeterm")
, performing most of the work; when resizing the windows, `resize_term()` blank-fills the areas that are extended. The calling application should fill in these areas with appropriate data. The `resize_term()` function attempts to resize all windows. However, due to the calling convention of pads, it is not possible to resize these without additional interaction with the application.

curses.resizeterm(_nlines_, _ncols_)[¶](https://docs.python.org/3/library/curses.html#curses.resizeterm "Link to this definition")

Resize the standard and current windows to the specified dimensions, and adjusts other bookkeeping data used by the curses library that record the window dimensions (in particular the SIGWINCH handler).

curses.savetty()[¶](https://docs.python.org/3/library/curses.html#curses.savetty "Link to this definition")

Save the current state of the terminal modes in a buffer, usable by [`resetty()`](https://docs.python.org/3/library/curses.html#curses.resetty "curses.resetty")
.

curses.get\_escdelay()[¶](https://docs.python.org/3/library/curses.html#curses.get_escdelay "Link to this definition")

Retrieves the value set by [`set_escdelay()`](https://docs.python.org/3/library/curses.html#curses.set_escdelay "curses.set_escdelay")
.

Added in version 3.9.

curses.set\_escdelay(_ms_)[¶](https://docs.python.org/3/library/curses.html#curses.set_escdelay "Link to this definition")

Sets the number of milliseconds to wait after reading an escape character, to distinguish between an individual escape character entered on the keyboard from escape sequences sent by cursor and function keys.

Added in version 3.9.

curses.get\_tabsize()[¶](https://docs.python.org/3/library/curses.html#curses.get_tabsize "Link to this definition")

Retrieves the value set by [`set_tabsize()`](https://docs.python.org/3/library/curses.html#curses.set_tabsize "curses.set_tabsize")
.

Added in version 3.9.

curses.set\_tabsize(_size_)[¶](https://docs.python.org/3/library/curses.html#curses.set_tabsize "Link to this definition")

Sets the number of columns used by the curses library when converting a tab character to spaces as it adds the tab to a window.

Added in version 3.9.

curses.setsyx(_y_, _x_)[¶](https://docs.python.org/3/library/curses.html#curses.setsyx "Link to this definition")

Set the virtual screen cursor to _y_, _x_. If _y_ and _x_ are both `-1`, then [`leaveok`](https://docs.python.org/3/library/curses.html#curses.window.leaveok "curses.window.leaveok")
 is set `True`.

curses.setupterm(_term\=None_, _fd\=\-1_)[¶](https://docs.python.org/3/library/curses.html#curses.setupterm "Link to this definition")

Initialize the terminal. _term_ is a string giving the terminal name, or `None`; if omitted or `None`, the value of the `TERM` environment variable will be used. _fd_ is the file descriptor to which any initialization sequences will be sent; if not supplied or `-1`, the file descriptor for `sys.stdout` will be used.

Raise a [`curses.error`](https://docs.python.org/3/library/curses.html#curses.error "curses.error")
 if the terminal could not be found or its terminfo database entry could not be read. If the terminal has already been initialized, this function has no effect.

Note

Calling [`initscr()`](https://docs.python.org/3/library/curses.html#curses.initscr "curses.initscr")
 after `setupterm()` leaks the terminal that `setupterm()` allocated: the curses library keeps only a single current terminal and does not free the previously allocated one.

curses.start\_color()[¶](https://docs.python.org/3/library/curses.html#curses.start_color "Link to this definition")

Must be called if the programmer wants to use colors, and before any other color manipulation routine is called. It is good practice to call this routine right after [`initscr()`](https://docs.python.org/3/library/curses.html#curses.initscr "curses.initscr")
.

`start_color()` initializes eight basic colors (black, red, green, yellow, blue, magenta, cyan, and white), and two global variables in the `curses` module, [`COLORS`](https://docs.python.org/3/library/curses.html#curses.COLORS "curses.COLORS")
 and [`COLOR_PAIRS`](https://docs.python.org/3/library/curses.html#curses.COLOR_PAIRS "curses.COLOR_PAIRS")
, containing the maximum number of colors and color-pairs the terminal can support. It also restores the colors on the terminal to the values they had when the terminal was just turned on.

curses.termattrs()[¶](https://docs.python.org/3/library/curses.html#curses.termattrs "Link to this definition")

Return a logical OR of all video attributes supported by the terminal. This information is useful when a curses program needs complete control over the appearance of the screen.

curses.termname()[¶](https://docs.python.org/3/library/curses.html#curses.termname "Link to this definition")

Return the name of the terminal in use, as a bytes object. This is the name passed to [`setupterm()`](https://docs.python.org/3/library/curses.html#curses.setupterm "curses.setupterm")
, or the value of the `TERM` environment variable if none was given. Some curses libraries truncate it to 14 characters.

curses.tigetflag(_capname_)[¶](https://docs.python.org/3/library/curses.html#curses.tigetflag "Link to this definition")

Return the value of the Boolean capability corresponding to the terminfo capability name _capname_ as an integer. Return the value `-1` if _capname_ is not a Boolean capability, or `0` if it is canceled or absent from the terminal description.

[`setupterm()`](https://docs.python.org/3/library/curses.html#curses.setupterm "curses.setupterm")
 (or [`initscr()`](https://docs.python.org/3/library/curses.html#curses.initscr "curses.initscr")
) must be called first.

curses.tigetnum(_capname_)[¶](https://docs.python.org/3/library/curses.html#curses.tigetnum "Link to this definition")

Return the value of the numeric capability corresponding to the terminfo capability name _capname_ as an integer. Return the value `-2` if _capname_ is not a numeric capability, or `-1` if it is canceled or absent from the terminal description.

[`setupterm()`](https://docs.python.org/3/library/curses.html#curses.setupterm "curses.setupterm")
 (or [`initscr()`](https://docs.python.org/3/library/curses.html#curses.initscr "curses.initscr")
) must be called first.

curses.tigetstr(_capname_)[¶](https://docs.python.org/3/library/curses.html#curses.tigetstr "Link to this definition")

Return the value of the string capability corresponding to the terminfo capability name _capname_ as a bytes object. Return `None` if _capname_ is not a terminfo “string capability”, or is canceled or absent from the terminal description.

[`setupterm()`](https://docs.python.org/3/library/curses.html#curses.setupterm "curses.setupterm")
 (or [`initscr()`](https://docs.python.org/3/library/curses.html#curses.initscr "curses.initscr")
) must be called first.

curses.tparm(_str_\[, _..._\])[¶](https://docs.python.org/3/library/curses.html#curses.tparm "Link to this definition")

Instantiate the bytes object _str_ with the supplied parameters, where _str_ should be a parameterized byte string obtained from the terminfo database. For example, `tparm(tigetstr("cup"), 5, 3)` could result in `b'\033[6;4H'`, the exact result depending on terminal type. Up to nine integer parameters may be supplied.\
\
[`setupterm()`](https://docs.python.org/3/library/curses.html#curses.setupterm "curses.setupterm")\
 (or [`initscr()`](https://docs.python.org/3/library/curses.html#curses.initscr "curses.initscr")\
) must be called first.\
\
curses.typeahead(_fd_)[¶](https://docs.python.org/3/library/curses.html#curses.typeahead "Link to this definition")\
\
Specify that the file descriptor _fd_ be used for typeahead checking. If _fd_ is `-1`, then no typeahead checking is done.\
\
The curses library does “line-breakout optimization” by looking for typeahead periodically while updating the screen. If input is found, and it is coming from a tty, the current update is postponed until refresh or doupdate is called again, allowing faster response to commands typed in advance. This function allows specifying a different file descriptor for typeahead checking.\
\
curses.unctrl(_ch_)[¶](https://docs.python.org/3/library/curses.html#curses.unctrl "Link to this definition")\
\
Return a bytes object which is a printable representation of the character _ch_; any attributes and color pair are ignored. Control characters are represented as a caret followed by the character, for example as `b'^C'`. Printing characters are left as they are.\
\
curses.ungetch(_ch_)[¶](https://docs.python.org/3/library/curses.html#curses.ungetch "Link to this definition")\
\
Push _ch_ so the next [`getch()`](https://docs.python.org/3/library/curses.html#curses.window.getch "curses.window.getch")\
 will return it.\
\
_ch_ may be an integer (a key code or the code of an encoded byte), a byte, or a string of length 1 which encodes to a single byte.\
\
Note\
\
Only one _ch_ can be pushed before `getch()` is called.\
\
curses.update\_lines\_cols()[¶](https://docs.python.org/3/library/curses.html#curses.update_lines_cols "Link to this definition")\
\
Update the [`LINES`](https://docs.python.org/3/library/curses.html#curses.LINES "curses.LINES")\
 and [`COLS`](https://docs.python.org/3/library/curses.html#curses.COLS "curses.COLS")\
 module variables. Useful for detecting manual screen resize.\
\
Added in version 3.5.\
\
curses.unget\_wch(_ch_)[¶](https://docs.python.org/3/library/curses.html#curses.unget_wch "Link to this definition")\
\
Push _ch_ so the next [`get_wch()`](https://docs.python.org/3/library/curses.html#curses.window.get_wch "curses.window.get_wch")\
 will return it.\
\
_ch_ may be an integer (a character code, not a key code) or a string of length 1.\
\
Note\
\
Only one _ch_ can be pushed before `get_wch()` is called.\
\
Added in version 3.3.\
\
curses.ungetmouse(_id_, _x_, _y_, _z_, _bstate_)[¶](https://docs.python.org/3/library/curses.html#curses.ungetmouse "Link to this definition")\
\
Push a [`KEY_MOUSE`](https://docs.python.org/3/library/curses.html#curses.KEY_MOUSE "curses.KEY_MOUSE")\
 event onto the input queue, associating the given state data with it.\
\
curses.use\_env(_flag_)[¶](https://docs.python.org/3/library/curses.html#curses.use_env "Link to this definition")\
\
If used, this function should be called before [`initscr()`](https://docs.python.org/3/library/curses.html#curses.initscr "curses.initscr")\
 or newterm are called. When _flag_ is `False`, the values of lines and columns specified in the terminfo database will be used, even if environment variables `LINES` and `COLUMNS` (used by default) are set, or if curses is running in a window (in which case default behavior would be to use the window size if `LINES` and `COLUMNS` are not set).\
\
curses.use\_default\_colors()[¶](https://docs.python.org/3/library/curses.html#curses.use_default_colors "Link to this definition")\
\
Equivalent to `assume_default_colors(-1, -1)`.\
\
curses.wrapper(_func_, _/_, _\*args_, _\*\*kwargs_)[¶](https://docs.python.org/3/library/curses.html#curses.wrapper "Link to this definition")\
\
Initialize curses and call another callable object, _func_, which should be the rest of your curses-using application. If the application raises an exception, this function will restore the terminal to a sane state before re-raising the exception and generating a traceback. The callable object _func_ is then passed the main window ‘stdscr’ as its first argument, followed by any other arguments passed to `wrapper()`. Before calling _func_, `wrapper()` turns on cbreak mode, turns off echo, enables the terminal keypad, and initializes colors if the terminal has color support. On exit (whether normally or by exception) it restores cooked mode, turns on echo, and disables the terminal keypad.\
\
Window objects[¶](https://docs.python.org/3/library/curses.html#window-objects "Link to this heading")\
\
-------------------------------------------------------------------------------------------------------\
\
class curses.window[¶](https://docs.python.org/3/library/curses.html#curses.window "Link to this definition")\
\
Window objects, as returned by [`initscr()`](https://docs.python.org/3/library/curses.html#curses.initscr "curses.initscr")\
 and [`newwin()`](https://docs.python.org/3/library/curses.html#curses.newwin "curses.newwin")\
 above, have the following methods and attributes:\
\
window.addch(_ch_\[, _attr_\])[¶](https://docs.python.org/3/library/curses.html#curses.window.addch "Link to this definition")\
\
window.addch(_y_, _x_, _ch_\[, _attr_\])\
\
Paint character _ch_ at `(y, x)` with attributes _attr_, overwriting any character previously painted at that location. By default, the character position and attributes are the current settings for the window object.\
\
Note\
\
Writing outside the window, subwindow, or pad raises a [`curses.error`](https://docs.python.org/3/library/curses.html#curses.error "curses.error")\
. Attempting to write to the lower-right corner of a window, subwindow, or pad will cause an exception to be raised after the character is printed.\
\
window.addnstr(_str_, _n_\[, _attr_\])[¶](https://docs.python.org/3/library/curses.html#curses.window.addnstr "Link to this definition")\
\
window.addnstr(_y_, _x_, _str_, _n_\[, _attr_\])\
\
Paint at most _n_ characters of the character string _str_ at `(y, x)` with attributes _attr_, overwriting anything previously on the display.\
\
window.addstr(_str_\[, _attr_\])[¶](https://docs.python.org/3/library/curses.html#curses.window.addstr "Link to this definition")\
\
window.addstr(_y_, _x_, _str_\[, _attr_\])\
\
Paint the character string _str_ at `(y, x)` with attributes _attr_, overwriting anything previously on the display.\
\
Note\
\
*   Writing outside the window, subwindow, or pad raises [`curses.error`](https://docs.python.org/3/library/curses.html#curses.error "curses.error")\
    . Attempting to write to the lower-right corner of a window, subwindow, or pad will cause an exception to be raised after the string is printed.\
    \
*   A bug in ncurses, the backend for this Python module, could cause segfaults when resizing windows. This was fixed in ncurses-6.1-20190511. If you are stuck with an earlier ncurses, you can avoid triggering it by not calling `addstr()` with a _str_ that has embedded newlines; instead, call `addstr()` separately for each line.\
    \
\
window.attroff(_attr_)[¶](https://docs.python.org/3/library/curses.html#curses.window.attroff "Link to this definition")\
\
Remove attribute _attr_ from the “background” set applied to all writes to the current window.\
\
window.attron(_attr_)[¶](https://docs.python.org/3/library/curses.html#curses.window.attron "Link to this definition")\
\
Add attribute _attr_ to the “background” set applied to all writes to the current window.\
\
window.attrset(_attr_)[¶](https://docs.python.org/3/library/curses.html#curses.window.attrset "Link to this definition")\
\
Set the “background” set of attributes to _attr_. This set is initially `0` (no attributes).\
\
window.bkgd(_ch_\[, _attr_\])[¶](https://docs.python.org/3/library/curses.html#curses.window.bkgd "Link to this definition")\
\
Set the background property of the window to the character _ch_, with attributes _attr_. The change is then applied to every character position in that window:\
\
*   The attribute of every character in the window is changed to the new background attribute.\
    \
*   Wherever the former background character appears, it is changed to the new background character.\
    \
\
window.bkgdset(_ch_\[, _attr_\])[¶](https://docs.python.org/3/library/curses.html#curses.window.bkgdset "Link to this definition")\
\
Set the window’s background. A window’s background consists of a character and any combination of attributes. The attribute part of the background is combined (OR’ed) with all non-blank characters that are written into the window. Both the character and attribute parts of the background are combined with the blank characters. The background becomes a property of the character and moves with the character through any scrolling and insert/delete line/character operations.\
\
window.border(\[_ls_\[, _rs_\[, _ts_\[, _bs_\[, _tl_\[, _tr_\[, _bl_\[, _br_\]\]\]\]\]\]\]\])[¶](https://docs.python.org/3/library/curses.html#curses.window.border "Link to this definition")\
\
Draw a border around the edges of the window. Each parameter specifies the character to use for a specific part of the border; see the table below for more details.\
\
Note\
\
A `0` value for any parameter will cause the default character to be used for that parameter. Keyword parameters can _not_ be used. The defaults are listed in this table:\
\
| Parameter | Description | Default value |\
| --- | --- | --- |\
| _ls_ | Left side | [`ACS_VLINE`](https://docs.python.org/3/library/curses.html#curses.ACS_VLINE "curses.ACS_VLINE") |\
| _rs_ | Right side | [`ACS_VLINE`](https://docs.python.org/3/library/curses.html#curses.ACS_VLINE "curses.ACS_VLINE") |\
| _ts_ | Top | [`ACS_HLINE`](https://docs.python.org/3/library/curses.html#curses.ACS_HLINE "curses.ACS_HLINE") |\
| _bs_ | Bottom | [`ACS_HLINE`](https://docs.python.org/3/library/curses.html#curses.ACS_HLINE "curses.ACS_HLINE") |\
| _tl_ | Upper-left corner | [`ACS_ULCORNER`](https://docs.python.org/3/library/curses.html#curses.ACS_ULCORNER "curses.ACS_ULCORNER") |\
| _tr_ | Upper-right corner | [`ACS_URCORNER`](https://docs.python.org/3/library/curses.html#curses.ACS_URCORNER "curses.ACS_URCORNER") |\
| _bl_ | Bottom-left corner | [`ACS_LLCORNER`](https://docs.python.org/3/library/curses.html#curses.ACS_LLCORNER "curses.ACS_LLCORNER") |\
| _br_ | Bottom-right corner | [`ACS_LRCORNER`](https://docs.python.org/3/library/curses.html#curses.ACS_LRCORNER "curses.ACS_LRCORNER") |\
\
window.box(\[_vertch_, _horch_\])[¶](https://docs.python.org/3/library/curses.html#curses.window.box "Link to this definition")\
\
Similar to [`border()`](https://docs.python.org/3/library/curses.html#curses.window.border "curses.window.border")\
, but both _ls_ and _rs_ are _vertch_ and both _ts_ and _bs_ are _horch_. The default corner characters are always used by this function.\
\
window.chgat(_attr_)[¶](https://docs.python.org/3/library/curses.html#curses.window.chgat "Link to this definition")\
\
window.chgat(_num_, _attr_)\
\
window.chgat(_y_, _x_, _attr_)\
\
window.chgat(_y_, _x_, _num_, _attr_)\
\
Set the attributes of _num_ characters at the current cursor position, or at position `(y, x)` if supplied. If _num_ is not given or is `-1`, the attribute will be set on all the characters to the end of the line. This function moves cursor to position `(y, x)` if supplied. The changed line will be touched using the [`touchline()`](https://docs.python.org/3/library/curses.html#curses.window.touchline "curses.window.touchline")\
 method so that the contents will be redisplayed by the next window refresh.\
\
window.clear()[¶](https://docs.python.org/3/library/curses.html#curses.window.clear "Link to this definition")\
\
Like [`erase()`](https://docs.python.org/3/library/curses.html#curses.window.erase "curses.window.erase")\
, but also cause the whole window to be repainted upon next call to [`refresh()`](https://docs.python.org/3/library/curses.html#curses.window.refresh "curses.window.refresh")\
.\
\
window.clearok(_flag_)[¶](https://docs.python.org/3/library/curses.html#curses.window.clearok "Link to this definition")\
\
If _flag_ is `True`, the next call to [`refresh()`](https://docs.python.org/3/library/curses.html#curses.window.refresh "curses.window.refresh")\
 will clear the window completely.\
\
window.clrtobot()[¶](https://docs.python.org/3/library/curses.html#curses.window.clrtobot "Link to this definition")\
\
Erase from cursor to the end of the window: all lines below the cursor are deleted, and then the equivalent of [`clrtoeol()`](https://docs.python.org/3/library/curses.html#curses.window.clrtoeol "curses.window.clrtoeol")\
 is performed.\
\
window.clrtoeol()[¶](https://docs.python.org/3/library/curses.html#curses.window.clrtoeol "Link to this definition")\
\
Erase from cursor to the end of the line.\
\
window.cursyncup()[¶](https://docs.python.org/3/library/curses.html#curses.window.cursyncup "Link to this definition")\
\
Update the current cursor position of all the ancestors of the window to reflect the current cursor position of the window.\
\
window.delch(\[_y_, _x_\])[¶](https://docs.python.org/3/library/curses.html#curses.window.delch "Link to this definition")\
\
Delete the character under the cursor, or at `(y, x)` if specified. All characters to the right on the same line are shifted one position left.\
\
window.deleteln()[¶](https://docs.python.org/3/library/curses.html#curses.window.deleteln "Link to this definition")\
\
Delete the line under the cursor. All following lines are moved up by one line.\
\
window.derwin(_begin\_y_, _begin\_x_)[¶](https://docs.python.org/3/library/curses.html#curses.window.derwin "Link to this definition")\
\
window.derwin(_nlines_, _ncols_, _begin\_y_, _begin\_x_)\
\
An abbreviation for “derive window”, `derwin()` is the same as calling [`subwin()`](https://docs.python.org/3/library/curses.html#curses.window.subwin "curses.window.subwin")\
, except that _begin\_y_ and _begin\_x_ are relative to the origin of the window, rather than relative to the entire screen. Return a window object for the derived window.\
\
window.echochar(_ch_\[, _attr_\])[¶](https://docs.python.org/3/library/curses.html#curses.window.echochar "Link to this definition")\
\
Add character _ch_ with attribute _attr_, and immediately call [`refresh()`](https://docs.python.org/3/library/curses.html#curses.window.refresh "curses.window.refresh")\
 on the window.\
\
window.enclose(_y_, _x_)[¶](https://docs.python.org/3/library/curses.html#curses.window.enclose "Link to this definition")\
\
Test whether the given pair of screen-relative character-cell coordinates are enclosed by the given window, returning `True` or `False`. It is useful for determining what subset of the screen windows enclose the location of a mouse event.\
\
Changed in version 3.10: Previously it returned `1` or `0` instead of `True` or `False`.\
\
window.encoding[¶](https://docs.python.org/3/library/curses.html#curses.window.encoding "Link to this definition")\
\
Encoding used to encode the string arguments of the methods and to decode their results on a build without wide-character support. The encoding attribute is inherited from the parent window when a subwindow is created, for example with [`window.subwin()`](https://docs.python.org/3/library/curses.html#curses.window.subwin "curses.window.subwin")\
. By default, current locale encoding is used (see [`locale.getencoding()`](https://docs.python.org/3/library/locale.html#locale.getencoding "locale.getencoding")\
).\
\
Added in version 3.3.\
\
window.erase()[¶](https://docs.python.org/3/library/curses.html#curses.window.erase "Link to this definition")\
\
Clear the window.\
\
window.getbegyx()[¶](https://docs.python.org/3/library/curses.html#curses.window.getbegyx "Link to this definition")\
\
Return a tuple `(y, x)` of coordinates of upper-left corner.\
\
window.getbkgd()[¶](https://docs.python.org/3/library/curses.html#curses.window.getbkgd "Link to this definition")\
\
Return the given window’s current background character/attribute pair. Its components can be extracted like those of [`inch()`](https://docs.python.org/3/library/curses.html#curses.window.inch "curses.window.inch")\
.\
\
window.getch(\[_y_, _x_\])[¶](https://docs.python.org/3/library/curses.html#curses.window.getch "Link to this definition")\
\
Read a key press, after moving the cursor to _y_, _x_ if specified, and return it as an integer. The window is refreshed first if it is not a pad and was modified since the last refresh. Wait until a key is pressed, or return `-1` if the read is non-blocking or times out (see [`nodelay()`](https://docs.python.org/3/library/curses.html#curses.window.nodelay "curses.window.nodelay")\
 and [`timeout()`](https://docs.python.org/3/library/curses.html#curses.window.timeout "curses.window.timeout")\
).\
\
An ordinary key is returned as the code of a single byte of its encoding in the current locale, so a character encoded with several bytes takes several calls. For example, in a UTF-8 locale `'é'` is read as `195`, then `169`. Use [`get_wch()`](https://docs.python.org/3/library/curses.html#curses.window.get_wch "curses.window.get_wch")\
 to read it as a single character.\
\
In keypad mode (see [`keypad()`](https://docs.python.org/3/library/curses.html#curses.window.keypad "curses.window.keypad")\
) function keys and other special keys are returned as one of the [KEY\_\* constants](https://docs.python.org/3/library/curses.html#curses-key-constants)\
, which cannot be mistaken for an ordinary key. Otherwise, or if their escape sequence does not arrive in time (see [`notimeout()`](https://docs.python.org/3/library/curses.html#curses.window.notimeout "curses.window.notimeout")\
 and [`set_escdelay()`](https://docs.python.org/3/library/curses.html#curses.set_escdelay "curses.set_escdelay")\
), their bytes are returned one at a time.\
\
In echo mode (see [`echo()`](https://docs.python.org/3/library/curses.html#curses.echo "curses.echo")\
) the key is added to the window as by [`addch()`](https://docs.python.org/3/library/curses.html#curses.window.addch "curses.window.addch")\
; special keys are not echoed.\
\
window.get\_wch(\[_y_, _x_\])[¶](https://docs.python.org/3/library/curses.html#curses.window.get_wch "Link to this definition")\
\
Read a key press, after moving the cursor to _y_, _x_ if specified, and return it as a one-character [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")\
. The window is refreshed first if it is not a pad and was modified since the last refresh. Wait until a key is pressed, or raise [`error`](https://docs.python.org/3/library/curses.html#curses.error "curses.error")\
 if the read is non-blocking or times out (see [`nodelay()`](https://docs.python.org/3/library/curses.html#curses.window.nodelay "curses.window.nodelay")\
 and [`timeout()`](https://docs.python.org/3/library/curses.html#curses.window.timeout "curses.window.timeout")\
).\
\
In keypad mode (see [`keypad()`](https://docs.python.org/3/library/curses.html#curses.window.keypad "curses.window.keypad")\
) function keys and other special keys are returned as one of the [KEY\_\* constants](https://docs.python.org/3/library/curses.html#curses-key-constants)\
, an integer. Otherwise, or if their escape sequence does not arrive in time (see [`notimeout()`](https://docs.python.org/3/library/curses.html#curses.window.notimeout "curses.window.notimeout")\
 and [`set_escdelay()`](https://docs.python.org/3/library/curses.html#curses.set_escdelay "curses.set_escdelay")\
), their characters are returned one at a time.\
\
In echo mode (see [`echo()`](https://docs.python.org/3/library/curses.html#curses.echo "curses.echo")\
) the key is added to the window as by [`addch()`](https://docs.python.org/3/library/curses.html#curses.window.addch "curses.window.addch")\
; special keys are not echoed.\
\
Added in version 3.3.\
\
window.getkey(\[_y_, _x_\])[¶](https://docs.python.org/3/library/curses.html#curses.window.getkey "Link to this definition")\
\
Read a key press as [`getch()`](https://docs.python.org/3/library/curses.html#curses.window.getch "curses.window.getch")\
 does, but return it as a [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")\
: an ordinary key as a one-character string, the byte decoded as Latin-1, and a special key as its name, such as `'KEY_UP'` (see [`keyname()`](https://docs.python.org/3/library/curses.html#curses.keyname "curses.keyname")\
). Raise [`error`](https://docs.python.org/3/library/curses.html#curses.error "curses.error")\
 instead of returning `-1` if there is no input.\
\
window.getmaxyx()[¶](https://docs.python.org/3/library/curses.html#curses.window.getmaxyx "Link to this definition")\
\
Return a tuple `(y, x)` of the height and width of the window.\
\
window.getparyx()[¶](https://docs.python.org/3/library/curses.html#curses.window.getparyx "Link to this definition")\
\
Return the beginning coordinates of this window relative to its parent window as a tuple `(y, x)`. Return `(-1, -1)` if this window has no parent.\
\
window.getstr()[¶](https://docs.python.org/3/library/curses.html#curses.window.getstr "Link to this definition")\
\
window.getstr(_n_)\
\
window.getstr(_y_, _x_)\
\
window.getstr(_y_, _x_, _n_)\
\
Read a line of input from the user, with primitive line editing capacity, after moving the cursor to _y_, _x_ if specified. Return it as a bytes object, in the encoding of the current locale and without the terminating newline. At most _n_ bytes are read; _n_ defaults to and cannot exceed 2047.\
\
Changed in version 3.14: The maximum value for _n_ was increased from 1023 to 2047.\
\
window.getyx()[¶](https://docs.python.org/3/library/curses.html#curses.window.getyx "Link to this definition")\
\
Return a tuple `(y, x)` of current cursor position relative to the window’s upper-left corner.\
\
window.hline(_ch_, _n_\[, _attr_\])[¶](https://docs.python.org/3/library/curses.html#curses.window.hline "Link to this definition")\
\
window.hline(_y_, _x_, _ch_, _n_\[, _attr_\])\
\
Display a horizontal line starting at `(y, x)` with length _n_ consisting of the character _ch_ with attributes _attr_. The line stops at the right edge of the window if fewer than _n_ cells are available.\
\
window.idcok(_flag_)[¶](https://docs.python.org/3/library/curses.html#curses.window.idcok "Link to this definition")\
\
If _flag_ is `False`, curses no longer considers using the hardware insert/delete character feature of the terminal; if _flag_ is `True`, use of character insertion and deletion is enabled. When curses is first initialized, use of character insert/delete is enabled by default.\
\
window.idlok(_flag_)[¶](https://docs.python.org/3/library/curses.html#curses.window.idlok "Link to this definition")\
\
If _flag_ is `True`, `curses` will try to use hardware line editing facilities. Otherwise, curses will not use them.\
\
window.immedok(_flag_)[¶](https://docs.python.org/3/library/curses.html#curses.window.immedok "Link to this definition")\
\
If _flag_ is `True`, any change in the window image automatically causes the window to be refreshed; you no longer have to call [`refresh()`](https://docs.python.org/3/library/curses.html#curses.window.refresh "curses.window.refresh")\
 yourself. However, it may degrade performance considerably, due to repeated calls to wrefresh. This option is disabled by default.\
\
window.inch(\[_y_, _x_\])[¶](https://docs.python.org/3/library/curses.html#curses.window.inch "Link to this definition")\
\
Return the character at the given position in the window. The bottom 8 bits are the character proper and the upper bits are the attributes; extract them with the [`A_CHARTEXT`](https://docs.python.org/3/library/curses.html#curses.A_CHARTEXT "curses.A_CHARTEXT")\
 and [`A_ATTRIBUTES`](https://docs.python.org/3/library/curses.html#curses.A_ATTRIBUTES "curses.A_ATTRIBUTES")\
 bit-masks, and the color pair with [`pair_number()`](https://docs.python.org/3/library/curses.html#curses.pair_number "curses.pair_number")\
. The character byte is the locale-encoded byte of the cell’s character, consistent with [`instr()`](https://docs.python.org/3/library/curses.html#curses.window.instr "curses.window.instr")\
. On a wide-character build, a character that does not fit in a single byte in the current locale has a character byte of `0`; use `instr()` to read such characters.\
\
window.insch(_ch_\[, _attr_\])[¶](https://docs.python.org/3/library/curses.html#curses.window.insch "Link to this definition")\
\
window.insch(_y_, _x_, _ch_\[, _attr_\])\
\
Insert character _ch_ with attributes _attr_ before the character under the cursor, or at `(y, x)` if specified. All characters to the right of the cursor are shifted one position right, with the rightmost character on the line being lost. The cursor position does not change (after moving to _y_, _x_, if specified).\
\
window.insdelln(_nlines_)[¶](https://docs.python.org/3/library/curses.html#curses.window.insdelln "Link to this definition")\
\
Insert _nlines_ lines into the specified window above the current line. The _nlines_ bottom lines are lost. For negative _nlines_, delete _nlines_ lines starting with the one under the cursor, and move the remaining lines up. The bottom _nlines_ lines are cleared. The current cursor position remains the same.\
\
window.insertln()[¶](https://docs.python.org/3/library/curses.html#curses.window.insertln "Link to this definition")\
\
Insert a blank line under the cursor. All following lines are moved down by one line.\
\
window.insnstr(_str_, _n_\[, _attr_\])[¶](https://docs.python.org/3/library/curses.html#curses.window.insnstr "Link to this definition")\
\
window.insnstr(_y_, _x_, _str_, _n_\[, _attr_\])\
\
Insert a character string (as many characters as will fit on the line) before the character under the cursor, up to _n_ characters. If _n_ is negative, the entire string is inserted. All characters to the right of the cursor are shifted right, with the rightmost characters on the line being lost. The cursor position does not change (after moving to _y_, _x_, if specified).\
\
window.insstr(_str_\[, _attr_\])[¶](https://docs.python.org/3/library/curses.html#curses.window.insstr "Link to this definition")\
\
window.insstr(_y_, _x_, _str_\[, _attr_\])\
\
Insert a character string (as many characters as will fit on the line) before the character under the cursor. All characters to the right of the cursor are shifted right, with the rightmost characters on the line being lost. The cursor position does not change (after moving to _y_, _x_, if specified).\
\
window.instr(\[_n_\])[¶](https://docs.python.org/3/library/curses.html#curses.window.instr "Link to this definition")\
\
window.instr(_y_, _x_\[, _n_\])\
\
Read the text of the window from the current cursor position, or from _y_, _x_ if specified, to the end of the line, and return it as a bytes object, in the encoding of the current locale. Attributes and color pairs are stripped. At most _n_ bytes are read; _n_ defaults to and cannot exceed 2047.\
\
Changed in version 3.14: The maximum value for _n_ was increased from 1023 to 2047.\
\
window.is\_linetouched(_line_)[¶](https://docs.python.org/3/library/curses.html#curses.window.is_linetouched "Link to this definition")\
\
Return `True` if the specified line was modified since the last call to [`refresh()`](https://docs.python.org/3/library/curses.html#curses.window.refresh "curses.window.refresh")\
; otherwise return `False`. Raise a [`curses.error`](https://docs.python.org/3/library/curses.html#curses.error "curses.error")\
 exception if _line_ is not valid for the given window.\
\
window.is\_wintouched()[¶](https://docs.python.org/3/library/curses.html#curses.window.is_wintouched "Link to this definition")\
\
Return `True` if the specified window was modified since the last call to [`refresh()`](https://docs.python.org/3/library/curses.html#curses.window.refresh "curses.window.refresh")\
; otherwise return `False`.\
\
window.keypad(_flag_)[¶](https://docs.python.org/3/library/curses.html#curses.window.keypad "Link to this definition")\
\
If _flag_ is `True`, escape sequences generated by some keys (keypad, function keys) will be interpreted by `curses`. If _flag_ is `False`, escape sequences will be left as is in the input stream. Keypad mode is disabled by default, but [`wrapper()`](https://docs.python.org/3/library/curses.html#curses.wrapper "curses.wrapper")\
 enables it for the main window.\
\
window.leaveok(_flag_)[¶](https://docs.python.org/3/library/curses.html#curses.window.leaveok "Link to this definition")\
\
If _flag_ is `True`, cursor is left where it is on update, instead of being at “cursor position.” This reduces cursor movement where possible.\
\
If _flag_ is `False`, cursor will always be at “cursor position” after an update.\
\
window.move(_new\_y_, _new\_x_)[¶](https://docs.python.org/3/library/curses.html#curses.window.move "Link to this definition")\
\
Move cursor to `(new_y, new_x)`.\
\
window.mvderwin(_y_, _x_)[¶](https://docs.python.org/3/library/curses.html#curses.window.mvderwin "Link to this definition")\
\
Move the window inside its parent window. The screen-relative parameters of the window are not changed. This routine is used to display different parts of the parent window at the same physical position on the screen.\
\
window.mvwin(_new\_y_, _new\_x_)[¶](https://docs.python.org/3/library/curses.html#curses.window.mvwin "Link to this definition")\
\
Move the window so its upper-left corner is at `(new_y, new_x)`.\
\
Moving the window so that any part of it would be off the screen is an error: the window is not moved and [`curses.error`](https://docs.python.org/3/library/curses.html#curses.error "curses.error")\
 is raised.\
\
window.nodelay(_flag_)[¶](https://docs.python.org/3/library/curses.html#curses.window.nodelay "Link to this definition")\
\
If _flag_ is `True`, [`getch()`](https://docs.python.org/3/library/curses.html#curses.window.getch "curses.window.getch")\
 will be non-blocking.\
\
window.notimeout(_flag_)[¶](https://docs.python.org/3/library/curses.html#curses.window.notimeout "Link to this definition")\
\
If _flag_ is `True`, escape sequences will not be timed out.\
\
If _flag_ is `False`, after a few milliseconds, an escape sequence will not be interpreted, and will be left in the input stream as is.\
\
window.noutrefresh()[¶](https://docs.python.org/3/library/curses.html#curses.window.noutrefresh "Link to this definition")\
\
window.noutrefresh(_pminrow_, _pmincol_, _sminrow_, _smincol_, _smaxrow_, _smaxcol_)\
\
Mark for refresh but wait. This function updates the data structure representing the desired state of the window, but does not force an update of the physical screen. To accomplish that, call [`doupdate()`](https://docs.python.org/3/library/curses.html#curses.doupdate "curses.doupdate")\
.\
\
The 6 arguments can only be specified, and are then required, when the window is a pad created with [`newpad()`](https://docs.python.org/3/library/curses.html#curses.newpad "curses.newpad")\
; they have the same meaning as for [`refresh()`](https://docs.python.org/3/library/curses.html#curses.window.refresh "curses.window.refresh")\
.\
\
window.overlay(_destwin_\[, _sminrow_, _smincol_, _dminrow_, _dmincol_, _dmaxrow_, _dmaxcol_\])[¶](https://docs.python.org/3/library/curses.html#curses.window.overlay "Link to this definition")\
\
Overlay the window on top of _destwin_. The windows need not be the same size, only the overlapping region is copied. This copy is non-destructive, which means that the current background character does not overwrite the old contents of _destwin_.\
\
To get fine-grained control over the copied region, the second form of `overlay()` can be used. _sminrow_ and _smincol_ are the upper-left coordinates of the source window, and the other variables mark a rectangle in the destination window.\
\
window.overwrite(_destwin_\[, _sminrow_, _smincol_, _dminrow_, _dmincol_, _dmaxrow_, _dmaxcol_\])[¶](https://docs.python.org/3/library/curses.html#curses.window.overwrite "Link to this definition")\
\
Overwrite the window on top of _destwin_. The windows need not be the same size, in which case only the overlapping region is copied. This copy is destructive, which means that the current background character overwrites the old contents of _destwin_.\
\
To get fine-grained control over the copied region, the second form of `overwrite()` can be used. _sminrow_ and _smincol_ are the upper-left coordinates of the source window, the other variables mark a rectangle in the destination window.\
\
window.putwin(_file_)[¶](https://docs.python.org/3/library/curses.html#curses.window.putwin "Link to this definition")\
\
Write all data associated with the window into the provided file object. This information can be later retrieved using the [`getwin()`](https://docs.python.org/3/library/curses.html#curses.getwin "curses.getwin")\
 function.\
\
window.redrawln(_beg_, _num_)[¶](https://docs.python.org/3/library/curses.html#curses.window.redrawln "Link to this definition")\
\
Indicate that the _num_ screen lines, starting at line _beg_, are corrupted and should be completely redrawn on the next [`refresh()`](https://docs.python.org/3/library/curses.html#curses.window.refresh "curses.window.refresh")\
 call.\
\
window.redrawwin()[¶](https://docs.python.org/3/library/curses.html#curses.window.redrawwin "Link to this definition")\
\
Touch the entire window, causing it to be completely redrawn on the next [`refresh()`](https://docs.python.org/3/library/curses.html#curses.window.refresh "curses.window.refresh")\
 call.\
\
window.refresh(\[_pminrow_, _pmincol_, _sminrow_, _smincol_, _smaxrow_, _smaxcol_\])[¶](https://docs.python.org/3/library/curses.html#curses.window.refresh "Link to this definition")\
\
Update the display immediately (sync actual screen with previous drawing/deleting methods).\
\
The 6 arguments can only be specified, and are then required, when the window is a pad created with [`newpad()`](https://docs.python.org/3/library/curses.html#curses.newpad "curses.newpad")\
. The additional parameters are needed to indicate what part of the pad and screen are involved. _pminrow_ and _pmincol_ specify the upper-left corner of the rectangle to be displayed in the pad. _sminrow_, _smincol_, _smaxrow_, and _smaxcol_ specify the edges of the rectangle to be displayed on the screen. The lower-right corner of the rectangle to be displayed in the pad is calculated from the screen coordinates, since the rectangles must be the same size. Both rectangles must be entirely contained within their respective structures. Negative values of _pminrow_, _pmincol_, _sminrow_, or _smincol_ are treated as if they were zero.\
\
window.resize(_nlines_, _ncols_)[¶](https://docs.python.org/3/library/curses.html#curses.window.resize "Link to this definition")\
\
Reallocate storage for a curses window to adjust its dimensions to the specified values. If either dimension is larger than the current values, the window’s data is filled with blanks that have the current background rendition (as set by [`bkgdset()`](https://docs.python.org/3/library/curses.html#curses.window.bkgdset "curses.window.bkgdset")\
) merged into them.\
\
window.scroll(\[_lines\=1_\])[¶](https://docs.python.org/3/library/curses.html#curses.window.scroll "Link to this definition")\
\
Scroll the screen or scrolling region. Scroll upward by _lines_ lines if _lines_ is positive, or downward if it is negative. Raise [`curses.error`](https://docs.python.org/3/library/curses.html#curses.error "curses.error")\
 unless scrolling has been enabled for the window with [`scrollok()`](https://docs.python.org/3/library/curses.html#curses.window.scrollok "curses.window.scrollok")\
.\
\
window.scrollok(_flag_)[¶](https://docs.python.org/3/library/curses.html#curses.window.scrollok "Link to this definition")\
\
Control what happens when the cursor of a window is moved off the edge of the window or scrolling region, either as a result of a newline action on the bottom line, or typing the last character of the last line. If _flag_ is `False`, the cursor is left on the bottom line. If _flag_ is `True`, the window is scrolled up one line. Note that in order to get the physical scrolling effect on the terminal, it is also necessary to call [`idlok()`](https://docs.python.org/3/library/curses.html#curses.window.idlok "curses.window.idlok")\
.\
\
window.setscrreg(_top_, _bottom_)[¶](https://docs.python.org/3/library/curses.html#curses.window.setscrreg "Link to this definition")\
\
Set the scrolling region from line _top_ to line _bottom_. All scrolling actions will take place in this region.\
\
window.standend()[¶](https://docs.python.org/3/library/curses.html#curses.window.standend "Link to this definition")\
\
Turn off the standout attribute. On some terminals this has the side effect of turning off all attributes.\
\
window.standout()[¶](https://docs.python.org/3/library/curses.html#curses.window.standout "Link to this definition")\
\
Turn on attribute _A\_STANDOUT_.\
\
window.subpad(_begin\_y_, _begin\_x_)[¶](https://docs.python.org/3/library/curses.html#curses.window.subpad "Link to this definition")\
\
window.subpad(_nlines_, _ncols_, _begin\_y_, _begin\_x_)\
\
Return a sub-pad, whose upper-left corner is at `(begin_y, begin_x)`, and whose width/height is _ncols_/_nlines_. The coordinates are relative to the parent pad (unlike [`subwin()`](https://docs.python.org/3/library/curses.html#curses.window.subwin "curses.window.subwin")\
, which uses screen coordinates). This method is only available for pads created with [`newpad()`](https://docs.python.org/3/library/curses.html#curses.newpad "curses.newpad")\
.\
\
window.subwin(_begin\_y_, _begin\_x_)[¶](https://docs.python.org/3/library/curses.html#curses.window.subwin "Link to this definition")\
\
window.subwin(_nlines_, _ncols_, _begin\_y_, _begin\_x_)\
\
Return a sub-window, whose upper-left corner is at the screen-relative coordinates `(begin_y, begin_x)`, and whose width/height is _ncols_/_nlines_.\
\
By default, the sub-window will extend from the specified position to the lower right corner of the window.\
\
window.syncdown()[¶](https://docs.python.org/3/library/curses.html#curses.window.syncdown "Link to this definition")\
\
Touch each location in the window that has been touched in any of its ancestor windows. This routine is called by [`refresh()`](https://docs.python.org/3/library/curses.html#curses.window.refresh "curses.window.refresh")\
, so it should almost never be necessary to call it manually.\
\
window.syncok(_flag_)[¶](https://docs.python.org/3/library/curses.html#curses.window.syncok "Link to this definition")\
\
If _flag_ is `True`, then [`syncup()`](https://docs.python.org/3/library/curses.html#curses.window.syncup "curses.window.syncup")\
 is called automatically whenever there is a change in the window.\
\
window.syncup()[¶](https://docs.python.org/3/library/curses.html#curses.window.syncup "Link to this definition")\
\
Touch all locations in ancestors of the window that have been changed in the window.\
\
window.timeout(_delay_)[¶](https://docs.python.org/3/library/curses.html#curses.window.timeout "Link to this definition")\
\
Set blocking or non-blocking read behavior for the window. If _delay_ is negative, blocking read is used (which will wait indefinitely for input). If _delay_ is zero, then non-blocking read is used, and [`getch()`](https://docs.python.org/3/library/curses.html#curses.window.getch "curses.window.getch")\
 will return `-1` if no input is waiting. If _delay_ is positive, then `getch()` will block for _delay_ milliseconds, and return `-1` if there is still no input at the end of that time.\
\
window.touchline(_start_, _count_\[, _changed_\])[¶](https://docs.python.org/3/library/curses.html#curses.window.touchline "Link to this definition")\
\
Pretend _count_ lines have been changed, starting with line _start_. If _changed_ is supplied, it specifies whether the affected lines are marked as having been changed (_changed_`=True`) or unchanged (_changed_`=False`).\
\
window.touchwin()[¶](https://docs.python.org/3/library/curses.html#curses.window.touchwin "Link to this definition")\
\
Pretend the whole window has been changed, for purposes of drawing optimizations.\
\
window.untouchwin()[¶](https://docs.python.org/3/library/curses.html#curses.window.untouchwin "Link to this definition")\
\
Mark all lines in the window as unchanged since the last call to [`refresh()`](https://docs.python.org/3/library/curses.html#curses.window.refresh "curses.window.refresh")\
.\
\
window.vline(_ch_, _n_\[, _attr_\])[¶](https://docs.python.org/3/library/curses.html#curses.window.vline "Link to this definition")\
\
window.vline(_y_, _x_, _ch_, _n_\[, _attr_\])\
\
Display a vertical line starting at `(y, x)` with length _n_ consisting of the character _ch_ with attributes _attr_.\
\
Constants[¶](https://docs.python.org/3/library/curses.html#constants "Link to this heading")\
\
---------------------------------------------------------------------------------------------\
\
The `curses` module defines the following data members:\
\
curses.ERR[¶](https://docs.python.org/3/library/curses.html#curses.ERR "Link to this definition")\
\
Some curses routines that return an integer, such as [`getch()`](https://docs.python.org/3/library/curses.html#curses.window.getch "curses.window.getch")\
, return [`ERR`](https://docs.python.org/3/library/curses.html#curses.ERR "curses.ERR")\
 upon failure.\
\
curses.OK[¶](https://docs.python.org/3/library/curses.html#curses.OK "Link to this definition")\
\
Some curses routines that return an integer, such as [`napms()`](https://docs.python.org/3/library/curses.html#curses.napms "curses.napms")\
, return [`OK`](https://docs.python.org/3/library/curses.html#curses.OK "curses.OK")\
 upon success.\
\
curses.version[¶](https://docs.python.org/3/library/curses.html#curses.version "Link to this definition")\
\
A bytes object representing the current version of the module.\
\
curses.ncurses\_version[¶](https://docs.python.org/3/library/curses.html#curses.ncurses_version "Link to this definition")\
\
A named tuple containing the three components of the ncurses library version: _major_, _minor_, and _patch_. All values are integers. The components can also be accessed by name, so `curses.ncurses_version[0]` is equivalent to `curses.ncurses_version.major` and so on.\
\
Availability: if the ncurses library is used.\
\
Added in version 3.8.\
\
curses.COLORS[¶](https://docs.python.org/3/library/curses.html#curses.COLORS "Link to this definition")\
\
The maximum number of colors the terminal can support. It is defined only after the call to [`start_color()`](https://docs.python.org/3/library/curses.html#curses.start_color "curses.start_color")\
.\
\
curses.COLOR\_PAIRS[¶](https://docs.python.org/3/library/curses.html#curses.COLOR_PAIRS "Link to this definition")\
\
The maximum number of color pairs the terminal can support. It is defined only after the call to [`start_color()`](https://docs.python.org/3/library/curses.html#curses.start_color "curses.start_color")\
.\
\
curses.COLS[¶](https://docs.python.org/3/library/curses.html#curses.COLS "Link to this definition")\
\
The width of the screen, that is, the number of columns. It is defined only after the call to [`initscr()`](https://docs.python.org/3/library/curses.html#curses.initscr "curses.initscr")\
. Updated by [`update_lines_cols()`](https://docs.python.org/3/library/curses.html#curses.update_lines_cols "curses.update_lines_cols")\
, [`resizeterm()`](https://docs.python.org/3/library/curses.html#curses.resizeterm "curses.resizeterm")\
 and [`resize_term()`](https://docs.python.org/3/library/curses.html#curses.resize_term "curses.resize_term")\
.\
\
curses.LINES[¶](https://docs.python.org/3/library/curses.html#curses.LINES "Link to this definition")\
\
The height of the screen, that is, the number of lines. It is defined only after the call to [`initscr()`](https://docs.python.org/3/library/curses.html#curses.initscr "curses.initscr")\
. Updated by [`update_lines_cols()`](https://docs.python.org/3/library/curses.html#curses.update_lines_cols "curses.update_lines_cols")\
, [`resizeterm()`](https://docs.python.org/3/library/curses.html#curses.resizeterm "curses.resizeterm")\
 and [`resize_term()`](https://docs.python.org/3/library/curses.html#curses.resize_term "curses.resize_term")\
.\
\
Some constants are available to specify character cell attributes. The exact constants available are system dependent.\
\
| Attribute | Meaning |\
| --- | --- |\
| curses.A\_ALTCHARSET[¶](https://docs.python.org/3/library/curses.html#curses.A_ALTCHARSET "Link to this definition") | Alternate character set mode |\
| curses.A\_BLINK[¶](https://docs.python.org/3/library/curses.html#curses.A_BLINK "Link to this definition") | Blink mode |\
| curses.A\_BOLD[¶](https://docs.python.org/3/library/curses.html#curses.A_BOLD "Link to this definition") | Bold mode |\
| curses.A\_DIM[¶](https://docs.python.org/3/library/curses.html#curses.A_DIM "Link to this definition") | Dim mode |\
| curses.A\_INVIS[¶](https://docs.python.org/3/library/curses.html#curses.A_INVIS "Link to this definition") | Invisible or blank mode |\
| curses.A\_ITALIC[¶](https://docs.python.org/3/library/curses.html#curses.A_ITALIC "Link to this definition") | Italic mode |\
| curses.A\_NORMAL[¶](https://docs.python.org/3/library/curses.html#curses.A_NORMAL "Link to this definition") | Normal attribute |\
| curses.A\_PROTECT[¶](https://docs.python.org/3/library/curses.html#curses.A_PROTECT "Link to this definition") | Protected mode |\
| curses.A\_REVERSE[¶](https://docs.python.org/3/library/curses.html#curses.A_REVERSE "Link to this definition") | Reverse background and foreground colors |\
| curses.A\_STANDOUT[¶](https://docs.python.org/3/library/curses.html#curses.A_STANDOUT "Link to this definition") | Standout mode |\
| curses.A\_UNDERLINE[¶](https://docs.python.org/3/library/curses.html#curses.A_UNDERLINE "Link to this definition") | Underline mode |\
| curses.A\_HORIZONTAL[¶](https://docs.python.org/3/library/curses.html#curses.A_HORIZONTAL "Link to this definition") | Horizontal highlight |\
| curses.A\_LEFT[¶](https://docs.python.org/3/library/curses.html#curses.A_LEFT "Link to this definition") | Left highlight |\
| curses.A\_LOW[¶](https://docs.python.org/3/library/curses.html#curses.A_LOW "Link to this definition") | Low highlight |\
| curses.A\_RIGHT[¶](https://docs.python.org/3/library/curses.html#curses.A_RIGHT "Link to this definition") | Right highlight |\
| curses.A\_TOP[¶](https://docs.python.org/3/library/curses.html#curses.A_TOP "Link to this definition") | Top highlight |\
| curses.A\_VERTICAL[¶](https://docs.python.org/3/library/curses.html#curses.A_VERTICAL "Link to this definition") | Vertical highlight |\
\
Added in version 3.7: `A_ITALIC` was added.\
\
Several constants are available to extract corresponding attributes returned by some methods.\
\
| Bit-mask | Meaning |\
| --- | --- |\
| curses.A\_ATTRIBUTES[¶](https://docs.python.org/3/library/curses.html#curses.A_ATTRIBUTES "Link to this definition") | Bit-mask to extract attributes |\
| curses.A\_CHARTEXT[¶](https://docs.python.org/3/library/curses.html#curses.A_CHARTEXT "Link to this definition") | Bit-mask to extract a character |\
| curses.A\_COLOR[¶](https://docs.python.org/3/library/curses.html#curses.A_COLOR "Link to this definition") | Bit-mask to extract color-pair field information |\
\
Keys are referred to by integer constants with names starting with `KEY_`. The exact keycaps available are system dependent.\
\
| Key constant | Key |\
| --- | --- |\
| curses.KEY\_MIN[¶](https://docs.python.org/3/library/curses.html#curses.KEY_MIN "Link to this definition") | Minimum key value |\
| curses.KEY\_BREAK[¶](https://docs.python.org/3/library/curses.html#curses.KEY_BREAK "Link to this definition") | Break key (unreliable) |\
| curses.KEY\_DOWN[¶](https://docs.python.org/3/library/curses.html#curses.KEY_DOWN "Link to this definition") | Down-arrow |\
| curses.KEY\_UP[¶](https://docs.python.org/3/library/curses.html#curses.KEY_UP "Link to this definition") | Up-arrow |\
| curses.KEY\_LEFT[¶](https://docs.python.org/3/library/curses.html#curses.KEY_LEFT "Link to this definition") | Left-arrow |\
| curses.KEY\_RIGHT[¶](https://docs.python.org/3/library/curses.html#curses.KEY_RIGHT "Link to this definition") | Right-arrow |\
| curses.KEY\_HOME[¶](https://docs.python.org/3/library/curses.html#curses.KEY_HOME "Link to this definition") | Home key (upward+left arrow) |\
| curses.KEY\_BACKSPACE[¶](https://docs.python.org/3/library/curses.html#curses.KEY_BACKSPACE "Link to this definition") | Backspace (unreliable) |\
| curses.KEY\_F0[¶](https://docs.python.org/3/library/curses.html#curses.KEY_F0 "Link to this definition") | Function keys. Up to 64 function keys are supported. |\
| curses.KEY\_Fn[¶](https://docs.python.org/3/library/curses.html#curses.KEY_Fn "Link to this definition") | Value of function key _n_ |\
| curses.KEY\_DL[¶](https://docs.python.org/3/library/curses.html#curses.KEY_DL "Link to this definition") | Delete line |\
| curses.KEY\_IL[¶](https://docs.python.org/3/library/curses.html#curses.KEY_IL "Link to this definition") | Insert line |\
| curses.KEY\_DC[¶](https://docs.python.org/3/library/curses.html#curses.KEY_DC "Link to this definition") | Delete character |\
| curses.KEY\_IC[¶](https://docs.python.org/3/library/curses.html#curses.KEY_IC "Link to this definition") | Insert char or enter insert mode |\
| curses.KEY\_EIC[¶](https://docs.python.org/3/library/curses.html#curses.KEY_EIC "Link to this definition") | Exit insert char mode |\
| curses.KEY\_CLEAR[¶](https://docs.python.org/3/library/curses.html#curses.KEY_CLEAR "Link to this definition") | Clear screen |\
| curses.KEY\_EOS[¶](https://docs.python.org/3/library/curses.html#curses.KEY_EOS "Link to this definition") | Clear to end of screen |\
| curses.KEY\_EOL[¶](https://docs.python.org/3/library/curses.html#curses.KEY_EOL "Link to this definition") | Clear to end of line |\
| curses.KEY\_SF[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SF "Link to this definition") | Scroll 1 line forward |\
| curses.KEY\_SR[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SR "Link to this definition") | Scroll 1 line backward (reverse) |\
| curses.KEY\_NPAGE[¶](https://docs.python.org/3/library/curses.html#curses.KEY_NPAGE "Link to this definition") | Next page |\
| curses.KEY\_PPAGE[¶](https://docs.python.org/3/library/curses.html#curses.KEY_PPAGE "Link to this definition") | Previous page |\
| curses.KEY\_STAB[¶](https://docs.python.org/3/library/curses.html#curses.KEY_STAB "Link to this definition") | Set tab |\
| curses.KEY\_CTAB[¶](https://docs.python.org/3/library/curses.html#curses.KEY_CTAB "Link to this definition") | Clear tab |\
| curses.KEY\_CATAB[¶](https://docs.python.org/3/library/curses.html#curses.KEY_CATAB "Link to this definition") | Clear all tabs |\
| curses.KEY\_ENTER[¶](https://docs.python.org/3/library/curses.html#curses.KEY_ENTER "Link to this definition") | Enter or send (unreliable) |\
| curses.KEY\_SRESET[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SRESET "Link to this definition") | Soft (partial) reset (unreliable) |\
| curses.KEY\_RESET[¶](https://docs.python.org/3/library/curses.html#curses.KEY_RESET "Link to this definition") | Reset or hard reset (unreliable) |\
| curses.KEY\_PRINT[¶](https://docs.python.org/3/library/curses.html#curses.KEY_PRINT "Link to this definition") | Print |\
| curses.KEY\_LL[¶](https://docs.python.org/3/library/curses.html#curses.KEY_LL "Link to this definition") | Home down or bottom (lower left) |\
| curses.KEY\_A1[¶](https://docs.python.org/3/library/curses.html#curses.KEY_A1 "Link to this definition") | Upper left of keypad |\
| curses.KEY\_A3[¶](https://docs.python.org/3/library/curses.html#curses.KEY_A3 "Link to this definition") | Upper right of keypad |\
| curses.KEY\_B2[¶](https://docs.python.org/3/library/curses.html#curses.KEY_B2 "Link to this definition") | Center of keypad |\
| curses.KEY\_C1[¶](https://docs.python.org/3/library/curses.html#curses.KEY_C1 "Link to this definition") | Lower left of keypad |\
| curses.KEY\_C3[¶](https://docs.python.org/3/library/curses.html#curses.KEY_C3 "Link to this definition") | Lower right of keypad |\
| curses.KEY\_BTAB[¶](https://docs.python.org/3/library/curses.html#curses.KEY_BTAB "Link to this definition") | Back tab |\
| curses.KEY\_BEG[¶](https://docs.python.org/3/library/curses.html#curses.KEY_BEG "Link to this definition") | Beg (beginning) |\
| curses.KEY\_CANCEL[¶](https://docs.python.org/3/library/curses.html#curses.KEY_CANCEL "Link to this definition") | Cancel |\
| curses.KEY\_CLOSE[¶](https://docs.python.org/3/library/curses.html#curses.KEY_CLOSE "Link to this definition") | Close |\
| curses.KEY\_COMMAND[¶](https://docs.python.org/3/library/curses.html#curses.KEY_COMMAND "Link to this definition") | Cmd (command) |\
| curses.KEY\_COPY[¶](https://docs.python.org/3/library/curses.html#curses.KEY_COPY "Link to this definition") | Copy |\
| curses.KEY\_CREATE[¶](https://docs.python.org/3/library/curses.html#curses.KEY_CREATE "Link to this definition") | Create |\
| curses.KEY\_END[¶](https://docs.python.org/3/library/curses.html#curses.KEY_END "Link to this definition") | End |\
| curses.KEY\_EXIT[¶](https://docs.python.org/3/library/curses.html#curses.KEY_EXIT "Link to this definition") | Exit |\
| curses.KEY\_FIND[¶](https://docs.python.org/3/library/curses.html#curses.KEY_FIND "Link to this definition") | Find |\
| curses.KEY\_HELP[¶](https://docs.python.org/3/library/curses.html#curses.KEY_HELP "Link to this definition") | Help |\
| curses.KEY\_MARK[¶](https://docs.python.org/3/library/curses.html#curses.KEY_MARK "Link to this definition") | Mark |\
| curses.KEY\_MESSAGE[¶](https://docs.python.org/3/library/curses.html#curses.KEY_MESSAGE "Link to this definition") | Message |\
| curses.KEY\_MOVE[¶](https://docs.python.org/3/library/curses.html#curses.KEY_MOVE "Link to this definition") | Move |\
| curses.KEY\_NEXT[¶](https://docs.python.org/3/library/curses.html#curses.KEY_NEXT "Link to this definition") | Next |\
| curses.KEY\_OPEN[¶](https://docs.python.org/3/library/curses.html#curses.KEY_OPEN "Link to this definition") | Open |\
| curses.KEY\_OPTIONS[¶](https://docs.python.org/3/library/curses.html#curses.KEY_OPTIONS "Link to this definition") | Options |\
| curses.KEY\_PREVIOUS[¶](https://docs.python.org/3/library/curses.html#curses.KEY_PREVIOUS "Link to this definition") | Prev (previous) |\
| curses.KEY\_REDO[¶](https://docs.python.org/3/library/curses.html#curses.KEY_REDO "Link to this definition") | Redo |\
| curses.KEY\_REFERENCE[¶](https://docs.python.org/3/library/curses.html#curses.KEY_REFERENCE "Link to this definition") | Ref (reference) |\
| curses.KEY\_REFRESH[¶](https://docs.python.org/3/library/curses.html#curses.KEY_REFRESH "Link to this definition") | Refresh |\
| curses.KEY\_REPLACE[¶](https://docs.python.org/3/library/curses.html#curses.KEY_REPLACE "Link to this definition") | Replace |\
| curses.KEY\_RESTART[¶](https://docs.python.org/3/library/curses.html#curses.KEY_RESTART "Link to this definition") | Restart |\
| curses.KEY\_RESUME[¶](https://docs.python.org/3/library/curses.html#curses.KEY_RESUME "Link to this definition") | Resume |\
| curses.KEY\_SAVE[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SAVE "Link to this definition") | Save |\
| curses.KEY\_SBEG[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SBEG "Link to this definition") | Shifted Beg (beginning) |\
| curses.KEY\_SCANCEL[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SCANCEL "Link to this definition") | Shifted Cancel |\
| curses.KEY\_SCOMMAND[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SCOMMAND "Link to this definition") | Shifted Command |\
| curses.KEY\_SCOPY[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SCOPY "Link to this definition") | Shifted Copy |\
| curses.KEY\_SCREATE[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SCREATE "Link to this definition") | Shifted Create |\
| curses.KEY\_SDC[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SDC "Link to this definition") | Shifted Delete char |\
| curses.KEY\_SDL[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SDL "Link to this definition") | Shifted Delete line |\
| curses.KEY\_SELECT[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SELECT "Link to this definition") | Select |\
| curses.KEY\_SEND[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SEND "Link to this definition") | Shifted End |\
| curses.KEY\_SEOL[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SEOL "Link to this definition") | Shifted Clear line |\
| curses.KEY\_SEXIT[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SEXIT "Link to this definition") | Shifted Exit |\
| curses.KEY\_SFIND[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SFIND "Link to this definition") | Shifted Find |\
| curses.KEY\_SHELP[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SHELP "Link to this definition") | Shifted Help |\
| curses.KEY\_SHOME[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SHOME "Link to this definition") | Shifted Home |\
| curses.KEY\_SIC[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SIC "Link to this definition") | Shifted Input |\
| curses.KEY\_SLEFT[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SLEFT "Link to this definition") | Shifted Left arrow |\
| curses.KEY\_SMESSAGE[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SMESSAGE "Link to this definition") | Shifted Message |\
| curses.KEY\_SMOVE[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SMOVE "Link to this definition") | Shifted Move |\
| curses.KEY\_SNEXT[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SNEXT "Link to this definition") | Shifted Next |\
| curses.KEY\_SOPTIONS[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SOPTIONS "Link to this definition") | Shifted Options |\
| curses.KEY\_SPREVIOUS[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SPREVIOUS "Link to this definition") | Shifted Prev |\
| curses.KEY\_SPRINT[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SPRINT "Link to this definition") | Shifted Print |\
| curses.KEY\_SREDO[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SREDO "Link to this definition") | Shifted Redo |\
| curses.KEY\_SREPLACE[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SREPLACE "Link to this definition") | Shifted Replace |\
| curses.KEY\_SRIGHT[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SRIGHT "Link to this definition") | Shifted Right arrow |\
| curses.KEY\_SRSUME[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SRSUME "Link to this definition") | Shifted Resume |\
| curses.KEY\_SSAVE[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SSAVE "Link to this definition") | Shifted Save |\
| curses.KEY\_SSUSPEND[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SSUSPEND "Link to this definition") | Shifted Suspend |\
| curses.KEY\_SUNDO[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SUNDO "Link to this definition") | Shifted Undo |\
| curses.KEY\_SUSPEND[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SUSPEND "Link to this definition") | Suspend |\
| curses.KEY\_UNDO[¶](https://docs.python.org/3/library/curses.html#curses.KEY_UNDO "Link to this definition") | Undo |\
| curses.KEY\_MOUSE[¶](https://docs.python.org/3/library/curses.html#curses.KEY_MOUSE "Link to this definition") | Mouse event has occurred |\
| curses.KEY\_RESIZE[¶](https://docs.python.org/3/library/curses.html#curses.KEY_RESIZE "Link to this definition") | Terminal resize event |\
| curses.KEY\_MAX[¶](https://docs.python.org/3/library/curses.html#curses.KEY_MAX "Link to this definition") | Maximum key value |\
\
On VT100s and their software emulations, such as X terminal emulators, there are normally at least four function keys ([`KEY_F1`](https://docs.python.org/3/library/curses.html#curses.KEY_Fn "curses.KEY_Fn")\
, `KEY_F2`, `KEY_F3`, `KEY_F4`) available, and the arrow keys mapped to [`KEY_UP`](https://docs.python.org/3/library/curses.html#curses.KEY_UP "curses.KEY_UP")\
, [`KEY_DOWN`](https://docs.python.org/3/library/curses.html#curses.KEY_DOWN "curses.KEY_DOWN")\
, [`KEY_LEFT`](https://docs.python.org/3/library/curses.html#curses.KEY_LEFT "curses.KEY_LEFT")\
 and [`KEY_RIGHT`](https://docs.python.org/3/library/curses.html#curses.KEY_RIGHT "curses.KEY_RIGHT")\
 in the obvious way. If your machine has a PC keyboard, it is safe to expect arrow keys and twelve function keys (older PC keyboards may have only ten function keys); also, the following keypad mappings are standard:\
\
| Keycap | Constant |\
| --- | --- |\
| Insert | KEY\_IC |\
| Delete | KEY\_DC |\
| Home | KEY\_HOME |\
| End | KEY\_END |\
| Page Up | KEY\_PPAGE |\
| Page Down | KEY\_NPAGE |\
\
The following table lists characters from the alternate character set. These are inherited from the VT100 terminal, and will generally be available on software emulations such as X terminals. When there is no graphic available, curses falls back on a crude printable ASCII approximation.\
\
Note\
\
These are available only after [`initscr()`](https://docs.python.org/3/library/curses.html#curses.initscr "curses.initscr")\
 has been called.\
\
| ACS code | Meaning |\
| --- | --- |\
| curses.ACS\_BBSS[¶](https://docs.python.org/3/library/curses.html#curses.ACS_BBSS "Link to this definition") | alternate name for upper-right corner |\
| curses.ACS\_BLOCK[¶](https://docs.python.org/3/library/curses.html#curses.ACS_BLOCK "Link to this definition") | solid square block |\
| curses.ACS\_BOARD[¶](https://docs.python.org/3/library/curses.html#curses.ACS_BOARD "Link to this definition") | board of squares |\
| curses.ACS\_BSBS[¶](https://docs.python.org/3/library/curses.html#curses.ACS_BSBS "Link to this definition") | alternate name for horizontal line |\
| curses.ACS\_BSSB[¶](https://docs.python.org/3/library/curses.html#curses.ACS_BSSB "Link to this definition") | alternate name for upper-left corner |\
| curses.ACS\_BSSS[¶](https://docs.python.org/3/library/curses.html#curses.ACS_BSSS "Link to this definition") | alternate name for top tee |\
| curses.ACS\_BTEE[¶](https://docs.python.org/3/library/curses.html#curses.ACS_BTEE "Link to this definition") | bottom tee |\
| curses.ACS\_BULLET[¶](https://docs.python.org/3/library/curses.html#curses.ACS_BULLET "Link to this definition") | bullet |\
| curses.ACS\_CKBOARD[¶](https://docs.python.org/3/library/curses.html#curses.ACS_CKBOARD "Link to this definition") | checker board (stipple) |\
| curses.ACS\_DARROW[¶](https://docs.python.org/3/library/curses.html#curses.ACS_DARROW "Link to this definition") | arrow pointing down |\
| curses.ACS\_DEGREE[¶](https://docs.python.org/3/library/curses.html#curses.ACS_DEGREE "Link to this definition") | degree symbol |\
| curses.ACS\_DIAMOND[¶](https://docs.python.org/3/library/curses.html#curses.ACS_DIAMOND "Link to this definition") | diamond |\
| curses.ACS\_GEQUAL[¶](https://docs.python.org/3/library/curses.html#curses.ACS_GEQUAL "Link to this definition") | greater-than-or-equal-to |\
| curses.ACS\_HLINE[¶](https://docs.python.org/3/library/curses.html#curses.ACS_HLINE "Link to this definition") | horizontal line |\
| curses.ACS\_LANTERN[¶](https://docs.python.org/3/library/curses.html#curses.ACS_LANTERN "Link to this definition") | lantern symbol |\
| curses.ACS\_LARROW[¶](https://docs.python.org/3/library/curses.html#curses.ACS_LARROW "Link to this definition") | left arrow |\
| curses.ACS\_LEQUAL[¶](https://docs.python.org/3/library/curses.html#curses.ACS_LEQUAL "Link to this definition") | less-than-or-equal-to |\
| curses.ACS\_LLCORNER[¶](https://docs.python.org/3/library/curses.html#curses.ACS_LLCORNER "Link to this definition") | lower-left corner |\
| curses.ACS\_LRCORNER[¶](https://docs.python.org/3/library/curses.html#curses.ACS_LRCORNER "Link to this definition") | lower-right corner |\
| curses.ACS\_LTEE[¶](https://docs.python.org/3/library/curses.html#curses.ACS_LTEE "Link to this definition") | left tee |\
| curses.ACS\_NEQUAL[¶](https://docs.python.org/3/library/curses.html#curses.ACS_NEQUAL "Link to this definition") | not-equal sign |\
| curses.ACS\_PI[¶](https://docs.python.org/3/library/curses.html#curses.ACS_PI "Link to this definition") | letter pi |\
| curses.ACS\_PLMINUS[¶](https://docs.python.org/3/library/curses.html#curses.ACS_PLMINUS "Link to this definition") | plus-or-minus sign |\
| curses.ACS\_PLUS[¶](https://docs.python.org/3/library/curses.html#curses.ACS_PLUS "Link to this definition") | big plus sign |\
| curses.ACS\_RARROW[¶](https://docs.python.org/3/library/curses.html#curses.ACS_RARROW "Link to this definition") | right arrow |\
| curses.ACS\_RTEE[¶](https://docs.python.org/3/library/curses.html#curses.ACS_RTEE "Link to this definition") | right tee |\
| curses.ACS\_S1[¶](https://docs.python.org/3/library/curses.html#curses.ACS_S1 "Link to this definition") | scan line 1 |\
| curses.ACS\_S3[¶](https://docs.python.org/3/library/curses.html#curses.ACS_S3 "Link to this definition") | scan line 3 |\
| curses.ACS\_S7[¶](https://docs.python.org/3/library/curses.html#curses.ACS_S7 "Link to this definition") | scan line 7 |\
| curses.ACS\_S9[¶](https://docs.python.org/3/library/curses.html#curses.ACS_S9 "Link to this definition") | scan line 9 |\
| curses.ACS\_SBBS[¶](https://docs.python.org/3/library/curses.html#curses.ACS_SBBS "Link to this definition") | alternate name for lower-right corner |\
| curses.ACS\_SBSB[¶](https://docs.python.org/3/library/curses.html#curses.ACS_SBSB "Link to this definition") | alternate name for vertical line |\
| curses.ACS\_SBSS[¶](https://docs.python.org/3/library/curses.html#curses.ACS_SBSS "Link to this definition") | alternate name for right tee |\
| curses.ACS\_SSBB[¶](https://docs.python.org/3/library/curses.html#curses.ACS_SSBB "Link to this definition") | alternate name for lower-left corner |\
| curses.ACS\_SSBS[¶](https://docs.python.org/3/library/curses.html#curses.ACS_SSBS "Link to this definition") | alternate name for bottom tee |\
| curses.ACS\_SSSB[¶](https://docs.python.org/3/library/curses.html#curses.ACS_SSSB "Link to this definition") | alternate name for left tee |\
| curses.ACS\_SSSS[¶](https://docs.python.org/3/library/curses.html#curses.ACS_SSSS "Link to this definition") | alternate name for crossover or big plus |\
| curses.ACS\_STERLING[¶](https://docs.python.org/3/library/curses.html#curses.ACS_STERLING "Link to this definition") | pound sterling |\
| curses.ACS\_TTEE[¶](https://docs.python.org/3/library/curses.html#curses.ACS_TTEE "Link to this definition") | top tee |\
| curses.ACS\_UARROW[¶](https://docs.python.org/3/library/curses.html#curses.ACS_UARROW "Link to this definition") | up arrow |\
| curses.ACS\_ULCORNER[¶](https://docs.python.org/3/library/curses.html#curses.ACS_ULCORNER "Link to this definition") | upper-left corner |\
| curses.ACS\_URCORNER[¶](https://docs.python.org/3/library/curses.html#curses.ACS_URCORNER "Link to this definition") | upper-right corner |\
| curses.ACS\_VLINE[¶](https://docs.python.org/3/library/curses.html#curses.ACS_VLINE "Link to this definition") | vertical line |\
\
The following table lists mouse button constants used by [`getmouse()`](https://docs.python.org/3/library/curses.html#curses.getmouse "curses.getmouse")\
:\
\
| Mouse button constant | Meaning |\
| --- | --- |\
| curses.BUTTONn\_PRESSED[¶](https://docs.python.org/3/library/curses.html#curses.BUTTONn_PRESSED "Link to this definition") | Mouse button _n_ pressed |\
| curses.BUTTONn\_RELEASED[¶](https://docs.python.org/3/library/curses.html#curses.BUTTONn_RELEASED "Link to this definition") | Mouse button _n_ released |\
| curses.BUTTONn\_CLICKED[¶](https://docs.python.org/3/library/curses.html#curses.BUTTONn_CLICKED "Link to this definition") | Mouse button _n_ clicked |\
| curses.BUTTONn\_DOUBLE\_CLICKED[¶](https://docs.python.org/3/library/curses.html#curses.BUTTONn_DOUBLE_CLICKED "Link to this definition") | Mouse button _n_ double clicked |\
| curses.BUTTONn\_TRIPLE\_CLICKED[¶](https://docs.python.org/3/library/curses.html#curses.BUTTONn_TRIPLE_CLICKED "Link to this definition") | Mouse button _n_ triple clicked |\
| curses.BUTTON\_SHIFT[¶](https://docs.python.org/3/library/curses.html#curses.BUTTON_SHIFT "Link to this definition") | Shift was down during button state change |\
| curses.BUTTON\_CTRL[¶](https://docs.python.org/3/library/curses.html#curses.BUTTON_CTRL "Link to this definition") | Control was down during button state change |\
| curses.BUTTON\_ALT[¶](https://docs.python.org/3/library/curses.html#curses.BUTTON_ALT "Link to this definition") | Alt was down during button state change |\
\
Changed in version 3.10: The `BUTTON5_*` constants are now exposed if they are provided by the underlying curses library.\
\
The following table lists the predefined colors:\
\
| Constant | Color |\
| --- | --- |\
| curses.COLOR\_BLACK[¶](https://docs.python.org/3/library/curses.html#curses.COLOR_BLACK "Link to this definition") | Black |\
| curses.COLOR\_BLUE[¶](https://docs.python.org/3/library/curses.html#curses.COLOR_BLUE "Link to this definition") | Blue |\
| curses.COLOR\_CYAN[¶](https://docs.python.org/3/library/curses.html#curses.COLOR_CYAN "Link to this definition") | Cyan (light greenish blue) |\
| curses.COLOR\_GREEN[¶](https://docs.python.org/3/library/curses.html#curses.COLOR_GREEN "Link to this definition") | Green |\
| curses.COLOR\_MAGENTA[¶](https://docs.python.org/3/library/curses.html#curses.COLOR_MAGENTA "Link to this definition") | Magenta (purplish red) |\
| curses.COLOR\_RED[¶](https://docs.python.org/3/library/curses.html#curses.COLOR_RED "Link to this definition") | Red |\
| curses.COLOR\_WHITE[¶](https://docs.python.org/3/library/curses.html#curses.COLOR_WHITE "Link to this definition") | White |\
| curses.COLOR\_YELLOW[¶](https://docs.python.org/3/library/curses.html#curses.COLOR_YELLOW "Link to this definition") | Yellow |\
\
`curses.textpad` — Text input widget for curses programs[¶](https://docs.python.org/3/library/curses.html#module-curses.textpad "Link to this heading")\
\
========================================================================================================================================================\
\
The `curses.textpad` module provides a [`Textbox`](https://docs.python.org/3/library/curses.html#curses.textpad.Textbox "curses.textpad.Textbox")\
 class that handles elementary text editing in a curses window, supporting a set of keybindings resembling those of Emacs (thus, also of Netscape Navigator, BBedit 6.x, FrameMaker, and many other programs). The module also provides a rectangle-drawing function useful for framing text boxes or for other purposes.\
\
The module `curses.textpad` defines the following function:\
\
curses.textpad.rectangle(_win_, _uly_, _ulx_, _lry_, _lrx_)[¶](https://docs.python.org/3/library/curses.html#curses.textpad.rectangle "Link to this definition")\
\
Draw a rectangle. The first argument must be a window object; the remaining arguments are coordinates relative to that window. The second and third arguments are the y and x coordinates of the upper-left corner of the rectangle to be drawn; the fourth and fifth arguments are the y and x coordinates of the lower-right corner. The rectangle will be drawn using VT100/IBM PC forms characters on terminals that make this possible (including xterm and most other software terminal emulators). Otherwise it will be drawn with ASCII dashes, vertical bars, and plus signs.\
\
Textbox objects[¶](https://docs.python.org/3/library/curses.html#textbox-objects "Link to this heading")\
\
---------------------------------------------------------------------------------------------------------\
\
You can instantiate a [`Textbox`](https://docs.python.org/3/library/curses.html#curses.textpad.Textbox "curses.textpad.Textbox")\
 object as follows:\
\
class curses.textpad.Textbox(_win_, _insert\_mode\=False_)[¶](https://docs.python.org/3/library/curses.html#curses.textpad.Textbox "Link to this definition")\
\
Return a textbox widget object. The _win_ argument should be a curses [window](https://docs.python.org/3/library/curses.html#curses-window-objects)\
 object in which the textbox is to be contained. If _insert\_mode_ is true, the textbox inserts typed characters, shifting existing text to the right, rather than overwriting it. The edit cursor of the textbox is initially located at the upper-left corner of the containing window, with coordinates `(0, 0)`. The instance’s [`stripspaces`](https://docs.python.org/3/library/curses.html#curses.textpad.Textbox.stripspaces "curses.textpad.Textbox.stripspaces")\
 flag is initially on.\
\
`Textbox` objects have the following methods:\
\
edit(_validate\=None_)[¶](https://docs.python.org/3/library/curses.html#curses.textpad.Textbox.edit "Link to this definition")\
\
This is the entry point you will normally use. It accepts editing keystrokes until one of the termination keystrokes is entered. If _validate_ is supplied, it must be a function. It will be called for each keystroke entered with the keystroke as a parameter; command dispatch is done on the result. If it returns a false value, the keystroke is ignored. This method returns the window contents as a string; whether blanks in the window are included is affected by the [`stripspaces`](https://docs.python.org/3/library/curses.html#curses.textpad.Textbox.stripspaces "curses.textpad.Textbox.stripspaces")\
 attribute.\
\
do\_command(_ch_)[¶](https://docs.python.org/3/library/curses.html#curses.textpad.Textbox.do_command "Link to this definition")\
\
Process a single command keystroke. Returns `1` to continue editing, or `0` if a termination keystroke was processed. Here are the supported special keystrokes:\
\
| Keystroke | Action |\
| --- | --- |\
| Control\-A | Go to left edge of window. |\
| Control\-B | Cursor left, wrapping to previous line if appropriate. |\
| Control\-D | Delete character under cursor. |\
| Control\-E | Go to right edge (stripspaces off) or end of line (stripspaces on). |\
| Control\-F | Cursor right, wrapping to next line when appropriate. |\
| Control\-G | Terminate, returning the window contents. |\
| Control\-H | Delete character backward. |\
| Control\-J | Terminate if the window is 1 line, otherwise move to the start of the next line. |\
| Control\-K | If line is blank, delete it, otherwise clear to end of line. |\
| Control\-L | Refresh screen. |\
| Control\-N | Cursor down; move down one line. |\
| Control\-O | Insert a blank line at cursor location. |\
| Control\-P | Cursor up; move up one line. |\
\
Move operations do nothing if the cursor is at an edge where the movement is not possible. The following synonyms are supported where possible:\
\
| Constant | Keystroke |\
| --- | --- |\
| [`KEY_LEFT`](https://docs.python.org/3/library/curses.html#curses.KEY_LEFT "curses.KEY_LEFT") | Control\-B |\
| [`KEY_RIGHT`](https://docs.python.org/3/library/curses.html#curses.KEY_RIGHT "curses.KEY_RIGHT") | Control\-F |\
| [`KEY_UP`](https://docs.python.org/3/library/curses.html#curses.KEY_UP "curses.KEY_UP") | Control\-P |\
| [`KEY_DOWN`](https://docs.python.org/3/library/curses.html#curses.KEY_DOWN "curses.KEY_DOWN") | Control\-N |\
| [`KEY_BACKSPACE`](https://docs.python.org/3/library/curses.html#curses.KEY_BACKSPACE "curses.KEY_BACKSPACE") | Control\-h |\
\
All other keystrokes are treated as a command to insert the given character and move right (with line wrapping).\
\
gather()[¶](https://docs.python.org/3/library/curses.html#curses.textpad.Textbox.gather "Link to this definition")\
\
Return the window contents as a string; whether blanks in the window are included is affected by the [`stripspaces`](https://docs.python.org/3/library/curses.html#curses.textpad.Textbox.stripspaces "curses.textpad.Textbox.stripspaces")\
 member.\
\
stripspaces[¶](https://docs.python.org/3/library/curses.html#curses.textpad.Textbox.stripspaces "Link to this definition")\
\
This attribute is a flag which controls the interpretation of blanks in the window. When it is on, trailing blanks on each line are ignored; any cursor motion that would land the cursor on a trailing blank goes to the end of that line instead, and trailing blanks are stripped when the window contents are gathered.\
\
### [Table of Contents](https://docs.python.org/3/contents.html)\
\
*   [`curses` — Terminal handling for character-cell displays](https://docs.python.org/3/library/curses.html#)\
    *   [Functions](https://docs.python.org/3/library/curses.html#functions)\
        \
    *   [Window objects](https://docs.python.org/3/library/curses.html#window-objects)\
        \
    *   [Constants](https://docs.python.org/3/library/curses.html#constants)\
        \
*   [`curses.textpad` — Text input widget for curses programs](https://docs.python.org/3/library/curses.html#module-curses.textpad)\
    *   [Textbox objects](https://docs.python.org/3/library/curses.html#textbox-objects)\
        \
\
#### Previous topic\
\
[`fileinput` — Iterate over lines from multiple input streams](https://docs.python.org/3/library/fileinput.html "previous chapter")\
\
#### Next topic\
\
[`curses.ascii` — Utilities for ASCII characters](https://docs.python.org/3/library/curses.ascii.html "next chapter")\
\
### This page\
\
*   [Report a bug](https://docs.python.org/3/bugs.html)\
    \
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=curses+%E2%80%94+Terminal+handling+for+character-cell+displays&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fcurses.html&pagesource=library%2Fcurses.rst)\
    \
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/curses.rst?plain=1)\
    \
\
«\
\
### Navigation\
\
*   [index](https://docs.python.org/3/genindex.html "General Index")\
    \
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")\
     |\
*   [next](https://docs.python.org/3/library/curses.ascii.html "curses.ascii — Utilities for ASCII characters")\
     |\
*   [previous](https://docs.python.org/3/library/fileinput.html "fileinput — Iterate over lines from multiple input streams")\
     |\
*   ![Python logo](https://docs.python.org/3/_static/py.svg)\
*   [Python](https://www.python.org/)\
     »\
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文\
    \
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6\
    \
\
*   [3.15.2 documentation](https://docs.python.org/3/index.html)\
     »\
*   [The Python standard library](https://docs.python.org/3/library/index.html)\
     »\
*   [Command-line interface libraries](https://docs.python.org/3/library/cmdlinelibs.html)\
     »\
*   [`curses` — Terminal handling for character-cell displays](https://docs.python.org/3/library/curses.html)\
    \
*    \
    \
    |\
*   Theme Auto Light Dark |