### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/unix.html "Unix-specific services")
     |
*   [previous](https://docs.python.org/3/library/winreg.html "winreg — Windows registry access")
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
*   [MS Windows Specific Services](https://docs.python.org/3/library/windows.html)
     »
*   [`winsound` — Sound-playing interface for Windows](https://docs.python.org/3/library/winsound.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`winsound` — Sound-playing interface for Windows[¶](https://docs.python.org/3/library/winsound.html#module-winsound "Link to this heading")

============================================================================================================================================

**Source code:** [PC/winsound.c](https://github.com/python/cpython/tree/3.15/PC/winsound.c)

* * *

The `winsound` module provides access to the basic sound-playing machinery provided by Windows platforms. It includes functions and several constants.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Windows.

Functions[¶](https://docs.python.org/3/library/winsound.html#functions "Link to this heading")

-----------------------------------------------------------------------------------------------

winsound.Beep(_frequency_, _duration_)[¶](https://docs.python.org/3/library/winsound.html#winsound.Beep "Link to this definition")

Beep the PC’s speaker. The _frequency_ parameter specifies frequency, in hertz, of the sound, and must be in the range 37 through 32,767. The _duration_ parameter specifies the number of milliseconds the sound should last. If the system is not able to beep the speaker, [`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "RuntimeError")
 is raised.

winsound.PlaySound(_sound_, _flags_)[¶](https://docs.python.org/3/library/winsound.html#winsound.PlaySound "Link to this definition")

Call the underlying `PlaySound()` function from the Platform API. The _sound_ parameter may be a filename, a system sound alias, audio data as a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
, or `None`. Its interpretation depends on the value of _flags_, which can be a bitwise ORed combination of the constants described below. If the _sound_ parameter is `None`, any currently playing waveform sound is stopped. If the system indicates an error, [`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "RuntimeError")
 is raised.

winsound.MessageBeep(_type\=MB\_OK_)[¶](https://docs.python.org/3/library/winsound.html#winsound.MessageBeep "Link to this definition")

Call the underlying `MessageBeep()` function from the Platform API. This plays a sound as specified in the registry. The _type_ argument specifies which sound to play; possible values are `-1`, `MB_ICONASTERISK`, `MB_ICONEXCLAMATION`, `MB_ICONHAND`, `MB_ICONQUESTION`, and `MB_OK`, all described below. The value `-1` produces a “simple beep”; this is the final fallback if a sound cannot be played otherwise. If the system indicates an error, [`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "RuntimeError")
 is raised.

Constants[¶](https://docs.python.org/3/library/winsound.html#constants "Link to this heading")

-----------------------------------------------------------------------------------------------

winsound.SND\_FILENAME[¶](https://docs.python.org/3/library/winsound.html#winsound.SND_FILENAME "Link to this definition")

The _sound_ parameter is the name of a WAV file. Do not use with [`SND_ALIAS`](https://docs.python.org/3/library/winsound.html#winsound.SND_ALIAS "winsound.SND_ALIAS")
.

winsound.SND\_ALIAS[¶](https://docs.python.org/3/library/winsound.html#winsound.SND_ALIAS "Link to this definition")

The _sound_ parameter is a sound association name from the registry. If the registry contains no such name, play the system default sound unless [`SND_NODEFAULT`](https://docs.python.org/3/library/winsound.html#winsound.SND_NODEFAULT "winsound.SND_NODEFAULT")
 is also specified. If no default sound is registered, raise [`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "RuntimeError")
. Do not use with [`SND_FILENAME`](https://docs.python.org/3/library/winsound.html#winsound.SND_FILENAME "winsound.SND_FILENAME")
.

All Win32 systems support at least the following; most systems support many more:

| [`PlaySound()`](https://docs.python.org/3/library/winsound.html#winsound.PlaySound "winsound.PlaySound")<br> _name_ | Corresponding Control Panel Sound name |
| --- | --- |
| `'SystemAsterisk'` | Asterisk |
| `'SystemExclamation'` | Exclamation |
| `'SystemExit'` | Exit Windows |
| `'SystemHand'` | Critical Stop |
| `'SystemQuestion'` | Question |

For example:

Copy

import winsound
\# Play Windows exit sound.
winsound.PlaySound("SystemExit", winsound.SND\_ALIAS)

\# Probably play Windows default sound, if any is registered (because
\# "\*" probably isn't the registered name of any sound).
winsound.PlaySound("\*", winsound.SND\_ALIAS)

winsound.SND\_LOOP[¶](https://docs.python.org/3/library/winsound.html#winsound.SND_LOOP "Link to this definition")

Play the sound repeatedly. The [`SND_ASYNC`](https://docs.python.org/3/library/winsound.html#winsound.SND_ASYNC "winsound.SND_ASYNC")
 flag must also be used to avoid blocking. Cannot be used with [`SND_MEMORY`](https://docs.python.org/3/library/winsound.html#winsound.SND_MEMORY "winsound.SND_MEMORY")
.

winsound.SND\_MEMORY[¶](https://docs.python.org/3/library/winsound.html#winsound.SND_MEMORY "Link to this definition")

The _sound_ parameter to [`PlaySound()`](https://docs.python.org/3/library/winsound.html#winsound.PlaySound "winsound.PlaySound")
 is a memory image of a WAV file, as a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
.

Note

This module does not support playing from a memory image asynchronously, so a combination of this flag and [`SND_ASYNC`](https://docs.python.org/3/library/winsound.html#winsound.SND_ASYNC "winsound.SND_ASYNC")
 will raise [`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "RuntimeError")
.

winsound.SND\_PURGE[¶](https://docs.python.org/3/library/winsound.html#winsound.SND_PURGE "Link to this definition")

Stop playing all instances of the specified sound.

Note

This flag is not supported on modern Windows platforms.

winsound.SND\_ASYNC[¶](https://docs.python.org/3/library/winsound.html#winsound.SND_ASYNC "Link to this definition")

Return immediately, allowing sounds to play asynchronously.

winsound.SND\_NODEFAULT[¶](https://docs.python.org/3/library/winsound.html#winsound.SND_NODEFAULT "Link to this definition")

If the specified sound cannot be found, do not play the system default sound.

winsound.SND\_NOSTOP[¶](https://docs.python.org/3/library/winsound.html#winsound.SND_NOSTOP "Link to this definition")

Do not interrupt sounds currently playing.

winsound.SND\_NOWAIT[¶](https://docs.python.org/3/library/winsound.html#winsound.SND_NOWAIT "Link to this definition")

Return immediately if the sound driver is busy.

Note

This flag is not supported on modern Windows platforms.

winsound.SND\_APPLICATION[¶](https://docs.python.org/3/library/winsound.html#winsound.SND_APPLICATION "Link to this definition")

The _sound_ parameter is an application-specific alias in the registry. This flag can be combined with the [`SND_ALIAS`](https://docs.python.org/3/library/winsound.html#winsound.SND_ALIAS "winsound.SND_ALIAS")
 flag to specify an application-defined sound alias.

winsound.SND\_SENTRY[¶](https://docs.python.org/3/library/winsound.html#winsound.SND_SENTRY "Link to this definition")

Triggers a SoundSentry event when the sound is played.

Added in version 3.14.

winsound.SND\_SYNC[¶](https://docs.python.org/3/library/winsound.html#winsound.SND_SYNC "Link to this definition")

The sound is played synchronously. This is the default behavior.

Added in version 3.14.

winsound.SND\_SYSTEM[¶](https://docs.python.org/3/library/winsound.html#winsound.SND_SYSTEM "Link to this definition")

Assign the sound to the audio session for system notification sounds.

Added in version 3.14.

winsound.MB\_ICONASTERISK[¶](https://docs.python.org/3/library/winsound.html#winsound.MB_ICONASTERISK "Link to this definition")

Play the `SystemDefault` sound.

winsound.MB\_ICONEXCLAMATION[¶](https://docs.python.org/3/library/winsound.html#winsound.MB_ICONEXCLAMATION "Link to this definition")

Play the `SystemExclamation` sound.

winsound.MB\_ICONHAND[¶](https://docs.python.org/3/library/winsound.html#winsound.MB_ICONHAND "Link to this definition")

Play the `SystemHand` sound.

winsound.MB\_ICONQUESTION[¶](https://docs.python.org/3/library/winsound.html#winsound.MB_ICONQUESTION "Link to this definition")

Play the `SystemQuestion` sound.

winsound.MB\_OK[¶](https://docs.python.org/3/library/winsound.html#winsound.MB_OK "Link to this definition")

Play the `SystemDefault` sound.

winsound.MB\_ICONERROR[¶](https://docs.python.org/3/library/winsound.html#winsound.MB_ICONERROR "Link to this definition")

Play the `SystemHand` sound.

Added in version 3.14.

winsound.MB\_ICONINFORMATION[¶](https://docs.python.org/3/library/winsound.html#winsound.MB_ICONINFORMATION "Link to this definition")

Play the `SystemDefault` sound.

Added in version 3.14.

winsound.MB\_ICONSTOP[¶](https://docs.python.org/3/library/winsound.html#winsound.MB_ICONSTOP "Link to this definition")

Play the `SystemHand` sound.

Added in version 3.14.

winsound.MB\_ICONWARNING[¶](https://docs.python.org/3/library/winsound.html#winsound.MB_ICONWARNING "Link to this definition")

Play the `SystemExclamation` sound.

Added in version 3.14.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`winsound` — Sound-playing interface for Windows](https://docs.python.org/3/library/winsound.html#)
    *   [Functions](https://docs.python.org/3/library/winsound.html#functions)
        
    *   [Constants](https://docs.python.org/3/library/winsound.html#constants)
        

#### Previous topic

[`winreg` — Windows registry access](https://docs.python.org/3/library/winreg.html "previous chapter")

#### Next topic

[Unix-specific services](https://docs.python.org/3/library/unix.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=winsound+%E2%80%94+Sound-playing+interface+for+Windows&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fwinsound.html&pagesource=library%2Fwinsound.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/winsound.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/unix.html "Unix-specific services")
     |
*   [previous](https://docs.python.org/3/library/winreg.html "winreg — Windows registry access")
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
*   [MS Windows Specific Services](https://docs.python.org/3/library/windows.html)
     »
*   [`winsound` — Sound-playing interface for Windows](https://docs.python.org/3/library/winsound.html)
    
*    
    
    |
*   Theme Auto Light Dark |