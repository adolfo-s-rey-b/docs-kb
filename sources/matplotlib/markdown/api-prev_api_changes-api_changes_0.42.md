[Skip to main content](https://matplotlib.org/stable/api/prev_api_changes/api_changes_0.42.html#main-content)

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
    

Changes for 0.42[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_0.42.html#changes-for-0-42 "Link to this heading")

======================================================================================================================================

\* Refactoring AxisText to be backend independent.  Text drawing and
  get\_window\_extent functionality will be moved to the Renderer.

\* backend\_bases.AxisTextBase is now text.Text module

\* All the erase and reset functionality removed from AxisText - not
  needed with double buffered drawing.  Ditto with state change.
  Text instances have a get\_prop\_tup method that returns a hashable
  tuple of text properties which you can use to see if text props
  have changed, e.g., by caching a font or layout instance in a dict
  with the prop tup as a key -- see RendererGTK.get\_pango\_layout in
  backend\_gtk for an example.

\* Text.\_get\_xy\_display renamed Text.get\_xy\_display

\* Artist set\_renderer and wash\_brushes methods removed

\* Moved Legend class from matplotlib.axes into matplotlib.legend

\* Moved Tick, XTick, YTick, Axis, XAxis, YAxis from matplotlib.axes
  to matplotlib.axis

\* moved process\_text\_args to matplotlib.text

\* After getting Text handled in a backend independent fashion, the
  import process is much cleaner since there are no longer cyclic
  dependencies

\* matplotlib.matlab.\_get\_current\_fig\_manager renamed to
  matplotlib.matlab.get\_current\_fig\_manager to allow user access to
  the GUI window attribute, e.g., figManager.window for GTK and
  figManager.frame for wx