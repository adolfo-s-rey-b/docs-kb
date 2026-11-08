[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.LockDraw.html#main-content)

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
    

matplotlib.widgets.LockDraw[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.LockDraw.html#matplotlib-widgets-lockdraw "Link to this heading")

==============================================================================================================================================================

class matplotlib.widgets.LockDraw[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L29-L64)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.LockDraw.html#matplotlib.widgets.LockDraw "Link to this definition")

Some widgets, like the cursor, draw onto the canvas, and this is not desirable under all circumstances, like when the toolbar is in zoom-to-rect mode and drawing a rectangle. To avoid this, a widget can acquire a canvas' lock with `canvas.widgetlock(widget)` before drawing on the canvas; this will prevent other widgets from doing so at the same time (if they also try to acquire the lock first).

\_\_init\_\_()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L39-L40)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.LockDraw.html#matplotlib.widgets.LockDraw.__init__ "Link to this definition")

Methods

|     |     |
| --- | --- |
| [`__init__`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.LockDraw.html#matplotlib.widgets.LockDraw.__init__ "matplotlib.widgets.LockDraw.__init__")<br>() |     |
| [`available`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.LockDraw.html#matplotlib.widgets.LockDraw.available "matplotlib.widgets.LockDraw.available")<br>(o) | Return whether drawing is available to _o_. |
| [`isowner`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.LockDraw.html#matplotlib.widgets.LockDraw.isowner "matplotlib.widgets.LockDraw.isowner")<br>(o) | Return whether _o_ owns this lock. |
| [`locked`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.LockDraw.html#matplotlib.widgets.LockDraw.locked "matplotlib.widgets.LockDraw.locked")<br>() | Return whether the lock is currently held by an owner. |
| [`release`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.LockDraw.html#matplotlib.widgets.LockDraw.release "matplotlib.widgets.LockDraw.release")<br>(o) | Release the lock from _o_. |

available(_o_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L54-L56)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.LockDraw.html#matplotlib.widgets.LockDraw.available "Link to this definition")

Return whether drawing is available to _o_.

isowner(_o_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L58-L60)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.LockDraw.html#matplotlib.widgets.LockDraw.isowner "Link to this definition")

Return whether _o_ owns this lock.

locked()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L62-L64)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.LockDraw.html#matplotlib.widgets.LockDraw.locked "Link to this definition")

Return whether the lock is currently held by an owner.

release(_o_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L48-L52)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.LockDraw.html#matplotlib.widgets.LockDraw.release "Link to this definition")

Release the lock from _o_.

On this page