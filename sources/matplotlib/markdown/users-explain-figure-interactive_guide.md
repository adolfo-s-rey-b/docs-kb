[Skip to main content](https://matplotlib.org/stable/users/explain/figure/interactive_guide.html#main-content)

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
    

Interactive figures and asynchronous programming[#](https://matplotlib.org/stable/users/explain/figure/interactive_guide.html#interactive-figures-and-asynchronous-programming "Link to this heading")

=======================================================================================================================================================================================================

Matplotlib supports rich interactive figures by embedding figures into a GUI window. The basic interactions of panning and zooming in an Axes to inspect your data is available out-of-the-box. This is supported by a full mouse and keyboard event handling system that you can use to build sophisticated interactive graphs.

This guide is meant to be an introduction to the low-level details of how Matplotlib integration with a GUI event loop works. For a more practical introduction to the Matplotlib event API see [event handling system](https://matplotlib.org/stable/users/explain/figure/event_handling.html#event-handling)
, [Interactive Tutorial](https://github.com/matplotlib/interactive_tutorial)
, and [Interactive Applications using Matplotlib](http://www.amazon.com/Interactive-Applications-using-Matplotlib-Benjamin/dp/1783988843)
.

GUI events[#](https://matplotlib.org/stable/users/explain/figure/interactive_guide.html#gui-events "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

All GUI frameworks (Qt, Wx, Gtk, Tk, macOS, or web) have some method of capturing user interactions and passing them back to the application, but the exact details depend on the toolkit (for example callbacks in Tk or the `Signal` / `Slot` framework in Qt). The Matplotlib [backends](https://matplotlib.org/stable/users/explain/figure/backends.html#what-is-a-backend)
 encapsulate the details of the GUI frameworks and provide a framework-independent interface to GUI events through Matplotlib's [event handling system](https://matplotlib.org/stable/users/explain/figure/event_handling.html#event-handling)
. By connecting functions to the event handling system (see [`FigureCanvasBase.mpl_connect`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.mpl_connect "matplotlib.backend_bases.FigureCanvasBase.mpl_connect")
), you can interactively respond to user actions in a GUI toolkit agnostic way.

Event loops[#](https://matplotlib.org/stable/users/explain/figure/interactive_guide.html#event-loops "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------

Fundamentally, all user interaction (and networking) is implemented as an infinite loop waiting for events from the user (via the OS) and then doing something about it. For example, a minimal Read Evaluate Print Loop (REPL) is

exec\_count \= 0
while True:
    inp \= input(f"\[{exec\_count}\] > ")        \# Read
    ret \= eval(inp)                          \# Evaluate
    print(ret)                               \# Print
    exec\_count += 1                          \# Loop

This is missing many niceties (for example, it exits on the first exception!), but is representative of the event loops that underlie all terminals, GUIs, and servers [\[1\]](https://matplotlib.org/stable/users/explain/figure/interactive_guide.html#f1)
. In general the _Read_ step is waiting on some sort of I/O -- be it user input or the network -- while the _Evaluate_ and _Print_ are responsible for interpreting the input and then **doing** something about it.

In practice we interact with a framework that provides a mechanism to register callbacks to be run in response to specific events rather than directly implement the I/O loop [\[2\]](https://matplotlib.org/stable/users/explain/figure/interactive_guide.html#f2)
. For example "when the user clicks on this button, please run this function" or "when the user hits the 'z' key, please run this other function". This allows users to write reactive, event-driven, programs without having to delve into the nitty-gritty [\[3\]](https://matplotlib.org/stable/users/explain/figure/interactive_guide.html#f3)
 details of I/O. The core event loop is sometimes referred to as "the main loop" and is typically started, depending on the library, by methods with names like `exec`, `run`, or `start`.

Command prompt integration[#](https://matplotlib.org/stable/users/explain/figure/interactive_guide.html#command-prompt-integration "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------

So far, so good. We have the REPL (like the IPython terminal) that lets us interactively send code to the interpreter and get results back. We also have the GUI toolkit that runs an event loop waiting for user input and lets us register functions to be run when that happens. However, if we want to do both we have a problem: the prompt and the GUI event loop are both infinite loops and cannot run in parallel. In order for both the prompt and the GUI windows to be responsive we need a method to allow the loops to "timeshare" :

1.  **Blocking the prompt**: let the GUI main loop block the python process when you want interactive windows
    
2.  **Input hook integration**: let the CLI main loop block the python process and intermittently run the GUI loop
    
3.  **Full embedding**: fully embed python in the GUI (but this is basically writing a full application)
    

### Blocking the prompt[#](https://matplotlib.org/stable/users/explain/figure/interactive_guide.html#blocking-the-prompt "Link to this heading")

|     |     |
| --- | --- |
| [`pyplot.show`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show") | Display all open figures. |
| [`pyplot.pause`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pause.html#matplotlib.pyplot.pause "matplotlib.pyplot.pause") | Run the GUI event loop for _interval_ seconds. |
| [`backend_bases.FigureCanvasBase.start_event_loop`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.start_event_loop "matplotlib.backend_bases.FigureCanvasBase.start_event_loop") | Start a blocking event loop. |
| [`backend_bases.FigureCanvasBase.stop_event_loop`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.stop_event_loop "matplotlib.backend_bases.FigureCanvasBase.stop_event_loop") | Stop the current blocking event loop. |

The simplest solution is to start the GUI event loop and let it run exclusively, which results in responsive figure windows. However, the CLI event loop will not run, so that you cannot enter new commands. We call this "blocking" mode. (Your terminal may echo the typed characters, but they will not yet be processed by the CLI event loop because the Python interpreter is busy running the GUI event loop).

It is possible to stop the GUI event loop and return control to the CLI event loop. You can then use the prompt again, but any still open figure windows are non-responsive. Re-starting the GUI event loop will make these figure responsive again (and will process any queued up user interaction).

The typical command to show all figures and run the GUI event loop exclusively until all figures are closed is

plt.show()

Alternatively, you can start the GUI event loop for a fixed amount of time using [`pyplot.pause`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pause.html#matplotlib.pyplot.pause "matplotlib.pyplot.pause")
.

If you are not using [`pyplot`](https://matplotlib.org/stable/api/pyplot_summary.html#module-matplotlib.pyplot "matplotlib.pyplot")
 you can start and stop the event loops via [`FigureCanvasBase.start_event_loop`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.start_event_loop "matplotlib.backend_bases.FigureCanvasBase.start_event_loop")
 and [`FigureCanvasBase.stop_event_loop`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.stop_event_loop "matplotlib.backend_bases.FigureCanvasBase.stop_event_loop")
. However, in most contexts where you would not be using [`pyplot`](https://matplotlib.org/stable/api/pyplot_summary.html#module-matplotlib.pyplot "matplotlib.pyplot")
 you are embedding Matplotlib in a large GUI application and the GUI event loop should already be running for the application.

Away from the prompt, this technique can be very useful if you want to write a script that pauses for user interaction, or displays a figure between polling for additional data. See [Scripts and functions](https://matplotlib.org/stable/users/explain/figure/interactive_guide.html#interactive-scripts)
 for more details.

### Input hook integration[#](https://matplotlib.org/stable/users/explain/figure/interactive_guide.html#input-hook-integration "Link to this heading")

While running the GUI event loop in a blocking mode or explicitly handling UI events is useful, we can do better! We really want to be able to have a usable prompt **and** interactive figure windows.

We can do this using the "input hook" feature of the interactive prompt. This hook is called by the prompt as it waits for the user to type (even for a fast typist the prompt is mostly waiting for the human to think and move their fingers). Although the details vary between prompts the logic is roughly

1.  start to wait for keyboard input
    
2.  start the GUI event loop
    
3.  as soon as the user hits a key, exit the GUI event loop and handle the key
    
4.  repeat
    

This gives us the illusion of simultaneously having interactive GUI windows and an interactive prompt. Most of the time the GUI event loop is running, but as soon as the user starts typing the prompt takes over again.

This time-share technique only allows the event loop to run while python is otherwise idle and waiting for user input. If you want the GUI to be responsive during long running code it is necessary to periodically flush the GUI event queue as described in [Explicitly spinning the event loop](https://matplotlib.org/stable/users/explain/figure/interactive_guide.html#spin-event-loop)
. In this case it is your code, not the REPL, which is blocking the process so you need to handle the "time-share" manually. Conversely, a very slow figure draw will block the prompt until it finishes drawing.

Full embedding[#](https://matplotlib.org/stable/users/explain/figure/interactive_guide.html#full-embedding "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------

It is also possible to go the other direction and fully embed figures (and a [Python interpreter](https://docs.python.org/3/extending/embedding.html)
) in a rich native application. Matplotlib provides classes for each toolkit which can be directly embedded in GUI applications (this is how the built-in windows are implemented!). See [Embedding Matplotlib in graphical user interfaces](https://matplotlib.org/stable/gallery/user_interfaces/index.html#user-interfaces)
 for more details.

Scripts and functions[#](https://matplotlib.org/stable/users/explain/figure/interactive_guide.html#scripts-and-functions "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`backend_bases.FigureCanvasBase.flush_events`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.flush_events "matplotlib.backend_bases.FigureCanvasBase.flush_events") | Flush the GUI events for the figure. |
| [`backend_bases.FigureCanvasBase.draw_idle`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.draw_idle "matplotlib.backend_bases.FigureCanvasBase.draw_idle") | Request a widget redraw once control returns to the GUI event loop. |
| [`figure.Figure.ginput`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.ginput.html#matplotlib.figure.Figure.ginput "matplotlib.figure.Figure.ginput") | Blocking call to interact with a figure. |
| [`pyplot.ginput`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ginput.html#matplotlib.pyplot.ginput "matplotlib.pyplot.ginput") | Blocking call to interact with a figure. |
| [`pyplot.show`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show") | Display all open figures. |
| [`pyplot.pause`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pause.html#matplotlib.pyplot.pause "matplotlib.pyplot.pause") | Run the GUI event loop for _interval_ seconds. |

There are several use-cases for using interactive figures in scripts:

*   capture user input to steer the script
    
*   progress updates as a long running script progresses
    
*   streaming updates from a data source
    

### Blocking functions[#](https://matplotlib.org/stable/users/explain/figure/interactive_guide.html#blocking-functions "Link to this heading")

If you only need to collect points in an Axes you can use [`Figure.ginput`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.ginput.html#matplotlib.figure.Figure.ginput "matplotlib.figure.Figure.ginput")
. However if you have written some custom event handling or are using [`widgets`](https://matplotlib.org/stable/api/widgets_api.html#module-matplotlib.widgets "matplotlib.widgets")
 you will need to manually run the GUI event loop using the methods described [above](https://matplotlib.org/stable/users/explain/figure/interactive_guide.html#cp-block-the-prompt)
.

You can also use the methods described in [Blocking the prompt](https://matplotlib.org/stable/users/explain/figure/interactive_guide.html#cp-block-the-prompt)
 to suspend run the GUI event loop. Once the loop exits your code will resume. In general, any place you would use [`time.sleep`](https://docs.python.org/3/library/time.html#time.sleep "(in Python v3.14)")
 you can use [`pyplot.pause`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pause.html#matplotlib.pyplot.pause "matplotlib.pyplot.pause")
 instead with the added benefit of interactive figures.

For example, if you want to poll for data you could use something like

fig, ax \= plt.subplots()
ln, \= ax.plot(\[\], \[\])

while True:
    x, y \= get\_new\_data()
    ln.set\_data(x, y)
    plt.pause(1)

which would poll for new data and update the figure at 1Hz.

### Explicitly spinning the event loop[#](https://matplotlib.org/stable/users/explain/figure/interactive_guide.html#explicitly-spinning-the-event-loop "Link to this heading")

|     |     |
| --- | --- |
| [`backend_bases.FigureCanvasBase.flush_events`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.flush_events "matplotlib.backend_bases.FigureCanvasBase.flush_events") | Flush the GUI events for the figure. |
| [`backend_bases.FigureCanvasBase.draw_idle`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.draw_idle "matplotlib.backend_bases.FigureCanvasBase.draw_idle") | Request a widget redraw once control returns to the GUI event loop. |

If you have open windows that have pending UI events (mouse clicks, button presses, or draws) you can explicitly process those events by calling [`FigureCanvasBase.flush_events`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.flush_events "matplotlib.backend_bases.FigureCanvasBase.flush_events")
. This will run the GUI event loop until all UI events currently waiting have been processed. The exact behavior is backend-dependent but typically events on all figure are processed and only events waiting to be processed (not those added during processing) will be handled.

For example

import time
import matplotlib.pyplot as plt
import numpy as np
plt.ion()

fig, ax \= plt.subplots()
th \= np.linspace(0, 2\*np.pi, 512)
ax.set\_ylim(\-1.5, 1.5)

ln, \= ax.plot(th, np.sin(th))

def slow\_loop(N, ln):
    for j in range(N):
        time.sleep(.1)  \# to simulate some work
        ln.figure.canvas.flush\_events()

slow\_loop(100, ln)

While this will feel a bit laggy (as we are only processing user input every 100ms whereas 20-30ms is what feels "responsive") it will respond.

If you make changes to the plot and want it re-rendered you will need to call [`draw_idle`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.draw_idle "matplotlib.backend_bases.FigureCanvasBase.draw_idle")
 to request that the canvas be re-drawn. This method can be thought of _draw\_soon_ in analogy to [`asyncio.loop.call_soon`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.call_soon "(in Python v3.14)")
.

We can add this to our example above as

def slow\_loop(N, ln):
    for j in range(N):
        time.sleep(.1)  \# to simulate some work
        if j % 10:
            ln.set\_ydata(np.sin(((j // 10) % 5 \* th)))
            ln.figure.canvas.draw\_idle()

        ln.figure.canvas.flush\_events()

slow\_loop(100, ln)

The more frequently you call [`FigureCanvasBase.flush_events`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.flush_events "matplotlib.backend_bases.FigureCanvasBase.flush_events")
 the more responsive your figure will feel but at the cost of spending more resources on the visualization and less on your computation.

Stale artists[#](https://matplotlib.org/stable/users/explain/figure/interactive_guide.html#stale-artists "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

Artists (as of Matplotlib 1.5) have a **stale** attribute which is [`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)")
 if the internal state of the artist has changed since the last time it was rendered. By default the stale state is propagated up to the Artists parents in the draw tree, e.g., if the color of a [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 instance is changed, the [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 and [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 that contain it will also be marked as "stale". Thus, `fig.stale` will report if any artist in the figure has been modified and is out of sync with what is displayed on the screen. This is intended to be used to determine if `draw_idle` should be called to schedule a re-rendering of the figure.

Each artist has a `Artist.stale_callback` attribute which holds a callback with the signature

def callback(self: Artist, val: bool) \-> None:
   ...

which by default is set to a function that forwards the stale state to the artist's parent. If you wish to suppress a given artist from propagating set this attribute to None.

[`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 instances do not have a containing artist and their default callback is [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
. If you call [`pyplot.ion`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ion.html#matplotlib.pyplot.ion "matplotlib.pyplot.ion")
 and are not in `IPython` we will install a callback to invoke [`draw_idle`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.draw_idle "matplotlib.backend_bases.FigureCanvasBase.draw_idle")
 whenever the [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 becomes stale. In `IPython` we use the `'post_execute'` hook to invoke [`draw_idle`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.draw_idle "matplotlib.backend_bases.FigureCanvasBase.draw_idle")
 on any stale figures after having executed the user's input, but before returning the prompt to the user. If you are not using [`pyplot`](https://matplotlib.org/stable/api/pyplot_summary.html#module-matplotlib.pyplot "matplotlib.pyplot")
 you can use the callback `Figure.stale_callback` attribute to be notified when a figure has become stale.

Idle draw[#](https://matplotlib.org/stable/users/explain/figure/interactive_guide.html#draw-idle "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`backend_bases.FigureCanvasBase.draw`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.draw "matplotlib.backend_bases.FigureCanvasBase.draw") | Render the [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br>. |
| [`backend_bases.FigureCanvasBase.draw_idle`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.draw_idle "matplotlib.backend_bases.FigureCanvasBase.draw_idle") | Request a widget redraw once control returns to the GUI event loop. |
| [`backend_bases.FigureCanvasBase.flush_events`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.flush_events "matplotlib.backend_bases.FigureCanvasBase.flush_events") | Flush the GUI events for the figure. |

In almost all cases, we recommend using [`backend_bases.FigureCanvasBase.draw_idle`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.draw_idle "matplotlib.backend_bases.FigureCanvasBase.draw_idle")
 over [`backend_bases.FigureCanvasBase.draw`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.draw "matplotlib.backend_bases.FigureCanvasBase.draw")
. `draw` forces a rendering of the figure whereas `draw_idle` schedules a rendering the next time the GUI window is going to re-paint the screen. This improves performance by only rendering pixels that will be shown on the screen. If you want to be sure that the screen is updated as soon as possible do

fig.canvas.draw\_idle()
fig.canvas.flush\_events()

Threading[#](https://matplotlib.org/stable/users/explain/figure/interactive_guide.html#threading "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

Most GUI frameworks require that all updates to the screen, and hence their main event loop, run on the main thread. This makes pushing periodic updates of a plot to a background thread impossible. Although it seems backwards, it is typically easier to push your computations to a background thread and periodically update the figure on the main thread.

In general Matplotlib is not thread safe. If you are going to update [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 objects in one thread and draw from another you should make sure that you are locking in the critical sections.

Event loop integration mechanism[#](https://matplotlib.org/stable/users/explain/figure/interactive_guide.html#event-loop-integration-mechanism "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

### CPython / readline[#](https://matplotlib.org/stable/users/explain/figure/interactive_guide.html#cpython-readline "Link to this heading")

The Python C API provides a hook, [`PyOS_InputHook`](https://docs.python.org/3/c-api/veryhigh.html#c.PyOS_InputHook "(in Python v3.14)")
, to register a function to be run ("The function will be called when Python's interpreter prompt is about to become idle and wait for user input from the terminal."). This hook can be used to integrate a second event loop (the GUI event loop) with the python input prompt loop. The hook functions typically exhaust all pending events on the GUI event queue, run the main loop for a short fixed amount of time, or run the event loop until a key is pressed on stdin.

Interactive figures, even with Matplotlib in "interactive mode", may not work in REPL if an appropriate [`PyOS_InputHook`](https://docs.python.org/3/c-api/veryhigh.html#c.PyOS_InputHook "(in Python v3.14)")
 is not registered. This management is left to upstream libraries or downstream code -- either explicit user code or shell initialization -- in all toolkits but native macOS. Input hooks, and helpers to install them, are usually included with the Python bindings for GUI toolkits and may be registered on import. For the macOS native toolkit Matplotlib owns code that exposes the toolkit to Python and thus we register [`PyOS_InputHook`](https://docs.python.org/3/c-api/veryhigh.html#c.PyOS_InputHook "(in Python v3.14)")
 on GUI application initialization.

IPython also ships input hook functions for all of the GUI frameworks Matplotlib supports which can be installed via `%matplotlib`. This is the recommended method of integrating Matplotlib and a prompt.

### IPython / prompt\_toolkit[#](https://matplotlib.org/stable/users/explain/figure/interactive_guide.html#ipython-prompt-toolkit "Link to this heading")

With IPython >= 5.0 IPython has changed from using CPython's readline based prompt to a `prompt_toolkit` based prompt. `prompt_toolkit` has the same conceptual input hook, which is fed into `prompt_toolkit` via the `IPython.terminal.interactiveshell.TerminalInteractiveShell.inputhook()` method. The source for the `prompt_toolkit` input hooks lives at `IPython.terminal.pt_inputhooks`.

Footnotes

On this page