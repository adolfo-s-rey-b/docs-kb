[Skip to main content](https://matplotlib.org/stable/api/backend_qt_api.html#main-content)

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
    

`matplotlib.backends.backend_qtagg`, `matplotlib.backends.backend_qtcairo`[#](https://matplotlib.org/stable/api/backend_qt_api.html#matplotlib-backends-backend-qtagg-matplotlib-backends-backend-qtcairo "Link to this heading")

==================================================================================================================================================================================================================================

**NOTE** These [Backends](https://matplotlib.org/stable/users/explain/figure/backends.html#backends)
 are not (auto) documented here, to avoid adding a dependency to building the docs.

Qt Bindings[#](https://matplotlib.org/stable/api/backend_qt_api.html#qt-bindings "Link to this heading")

---------------------------------------------------------------------------------------------------------

There are currently 2 actively supported Qt versions, Qt5 and Qt6, and two supported Python bindings per version -- [PyQt5](https://www.riverbankcomputing.com/static/Docs/PyQt5/)
 and [PySide2](https://doc.qt.io/qtforpython-5/contents.html)
 for Qt5 and [PyQt6](https://www.riverbankcomputing.com/static/Docs/PyQt6/)
 and [PySide6](https://doc.qt.io/qtforpython/contents.html)
 for Qt6 [\[1\]](https://matplotlib.org/stable/api/backend_qt_api.html#id5)
. Matplotlib's qtagg and qtcairo backends (`matplotlib.backends.backend_qtagg` and `matplotlib.backend.backend_qtcairo`) support all these bindings, with common parts factored out in the `matplotlib.backends.backend_qt` module.

At runtime, these backends select the actual binding used as follows:

1.  If a binding's `QtCore` subpackage is already imported, that binding is selected (the order for the check is `PyQt6`, `PySide6`, `PyQt5`, `PySide2`).
    
2.  If the [`QT_API`](https://matplotlib.org/stable/install/environment_variables_faq.html#envvar-QT_API)
     environment variable is set to one of "PyQt6", "PySide6", "PyQt5", "PySide2" (case-insensitive), that binding is selected. (See also the documentation on [Environment variables](https://matplotlib.org/stable/install/environment_variables_faq.html#environment-variables)
    .)
    
3.  Otherwise, the first available backend in the order `PyQt6`, `PySide6`, `PyQt5`, `PySide2` is selected.
    

In the past, Matplotlib used to have separate backends for each version of Qt (e.g. qt4agg/`matplotlib.backends.backend_qt4agg` and qt5agg/`matplotlib.backends.backend_qt5agg`). This scheme was dropped when support for Qt6 was added. For back-compatibility, qt5agg/`backend_qt5agg` and qt5cairo/`backend_qt5cairo` remain available; selecting one of these backends forces the use of a Qt5 binding. Their use is discouraged and `backend_qtagg` or `backend_qtcairo` should be preferred instead. However, these modules will not be deprecated until we drop support for Qt5.

While both PyQt and Qt for Python (aka PySide) closely mirror the underlying C++ API they are wrapping, they are not drop-in replacements for each other [\[2\]](https://matplotlib.org/stable/api/backend_qt_api.html#id6)
. To account for this, Matplotlib has an internal API compatibility layer in [`matplotlib.backends.qt_compat`](https://matplotlib.org/stable/api/backend_qt_api.html#module-matplotlib.backends.qt_compat "matplotlib.backends.qt_compat")
 which covers our needs. Despite being a public module, we do not consider this to be a stable user-facing API and it may change without warning [\[3\]](https://matplotlib.org/stable/api/backend_qt_api.html#id7)
.

On this page