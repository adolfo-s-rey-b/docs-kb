[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.install_repl_displayhook.html#main-content)

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
    

matplotlib.pyplot.install\_repl\_displayhook[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.install_repl_displayhook.html#matplotlib-pyplot-install-repl-displayhook "Link to this heading")

=============================================================================================================================================================================================================

matplotlib.pyplot.install\_repl\_displayhook()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L303-L344)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.install_repl_displayhook.html#matplotlib.pyplot.install_repl_displayhook "Link to this definition")

Connect to the display hook of the current shell.

The display hook gets called when the read-evaluate-print-loop (REPL) of the shell has finished the execution of a command. We use this callback to be able to automatically update a figure in interactive mode.

This works both with IPython and with vanilla python shells.

On this page