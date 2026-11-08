[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.set_loglevel.html#main-content)

Back to top Ctrl+K

*   [Plot types](https://matplotlib.org/stable/plot_types/index.html)
    
*   [User guide](https://matplotlib.org/stable/users/index.html)
    
*   [Tutorials](https://matplotlib.org/stable/tutorials/index.html)
    
*   [Examples](https://matplotlib.org/stable/gallery/index.html)
    
*   [Reference](https://matplotlib.org/stable/api/index.html)
    
*   [Contribute](https://matplotlib.org/stable/devel/index.html)
    
*   [Releases](https://matplotlib.org/stable/users/release_notes.html)
    

Choose version

*   [Gitter](https://gitter.im/matplotlib/matplotlib "Gitter")
    
*   [Discourse](https://discourse.matplotlib.org/ "Discourse")
    
*   [GitHub](https://github.com/matplotlib/matplotlib "GitHub")
    

matplotlib.pyplot.set\_loglevel[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.set_loglevel.html#matplotlib-pyplot-set-loglevel "Link to this heading")

========================================================================================================================================================================

matplotlib.pyplot.set\_loglevel(_level_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L361-L363)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.set_loglevel.html#matplotlib.pyplot.set_loglevel "Link to this definition")

Configure Matplotlib's logging levels.

Matplotlib uses the standard library [`logging`](https://docs.python.org/3/library/logging.html#module-logging "(in Python v3.14)")
 framework under the root logger 'matplotlib'. This is a helper function to:

*   set Matplotlib's root logger level
    
*   set the root logger handler's level, creating the handler if it does not exist yet
    

Typically, one should call `set_loglevel("INFO")` or `set_loglevel("DEBUG")` to get additional debugging information.

Users or applications that are installing their own logging handlers may want to directly manipulate `logging.getLogger('matplotlib')` rather than use this function.

Parameters:

**level**{"NOTSET", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}

The log level as defined in [Python logging levels](https://docs.python.org/3/library/logging.html#logging-levels)
.

For backwards compatibility, the levels are case-insensitive, but the capitalized version is preferred in analogy to [`logging.Logger.setLevel`](https://docs.python.org/3/library/logging.html#logging.Logger.setLevel "(in Python v3.14)")
.

Notes

Note

This is equivalent to [`matplotlib.set_loglevel`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.set_loglevel "matplotlib.set_loglevel")
.

The first time this function is called, an additional handler is attached to Matplotlib's root handler; this handler is reused every time and this function simply manipulates the logger and handler's level.

On this page