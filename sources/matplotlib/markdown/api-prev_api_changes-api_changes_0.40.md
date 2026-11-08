[Skip to main content](https://matplotlib.org/stable/api/prev_api_changes/api_changes_0.40.html#main-content)

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
    

Changes for 0.40[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_0.40.html#changes-for-0-40 "Link to this heading")

======================================================================================================================================

\- Artist
    \* \_\_init\_\_ takes a DPI instance and a Bound2D instance which is
      the bounding box of the artist in display coords
    \* get\_window\_extent returns a Bound2D instance
    \* set\_size is removed; replaced by bbox and dpi
    \* the clip\_gc method is removed.  Artists now clip themselves with
      their box
    \* added \_clipOn boolean attribute.  If True, gc clip to bbox.

- AxisTextBase
    \* Initialized with a transx, transy which are Transform instances
    \* set\_drawing\_area removed
    \* get\_left\_right and get\_top\_bottom are replaced by get\_window\_extent

- Line2D Patches now take transx, transy
    \* Initialized with a transx, transy which are Transform instances

- Patches
   \* Initialized with a transx, transy which are Transform instances

- FigureBase attributes dpi is a DPI instance rather than scalar and
  new attribute bbox is a Bound2D in display coords, and I got rid
  of the left, width, height, etc... attributes.  These are now
  accessible as, for example, bbox.x.min is left, bbox.x.interval()
  is width, bbox.y.max is top, etc...

- GcfBase attribute pagesize renamed to figsize

- Axes
    \* removed figbg attribute
    \* added fig instance to \_\_init\_\_
    \* resizing is handled by figure call to resize.

- Subplot
    \* added fig instance to \_\_init\_\_

- Renderer methods for patches now take gcEdge and gcFace instances.
  gcFace=None takes the place of filled=False

- True and False symbols provided by cbook in a python2.3 compatible
  way

- new module transforms supplies Bound1D, Bound2D and Transform
  instances and more

- Changes to the MATLAB helpers API

  \* \_matlab\_helpers.GcfBase is renamed by Gcf.  Backends no longer
    need to derive from this class.  Instead, they provide a factory
    function new\_figure\_manager(num, figsize, dpi).  The destroy
    method of the GcfDerived from the backends is moved to the derived
    FigureManager.

  \* FigureManagerBase moved to backend\_bases

  \* Gcf.get\_all\_figwins renamed to Gcf.get\_all\_fig\_managers

Jeremy:

  Make sure to self.\_reset = False in AxisTextWX.\_set\_font.  This was
  something missing in my backend code.