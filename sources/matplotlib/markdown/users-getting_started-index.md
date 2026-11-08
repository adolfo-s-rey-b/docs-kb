[Skip to main content](https://matplotlib.org/stable/users/getting_started/index.html#main-content)

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
    

Getting started[#](https://matplotlib.org/stable/users/getting_started/index.html#getting-started "Link to this heading")

==========================================================================================================================

Installation quick-start[#](https://matplotlib.org/stable/users/getting_started/index.html#installation-quick-start "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------

 pip

pip install matplotlib

 conda

conda install \-c conda-forge matplotlib

 pixi

pixi add matplotlib

 uv

uv add matplotlib

Warning

uv usually installs its own versions of Python from the python-build-standalone project, and only recent versions of those Python builds (August 2025) work properly with the `tkagg` backend for displaying plots in a window. Please make sure you are using uv 0.8.7 or newer (update with e.g. `uv self update`) and that your bundled Python installs are up to date (with `uv python upgrade --reinstall`). Alternatively, you can use one of the other [supported GUI frameworks](https://matplotlib.org/stable/install/dependencies.html#optional-dependencies)
, e.g.

uv add matplotlib pyside6

 other

[Install an official release](https://matplotlib.org/stable/install/index.html#install-official)

[Third-party distributions](https://matplotlib.org/stable/install/index.html#install-third-party)

[Install a nightly build](https://matplotlib.org/stable/install/index.html#install-nightly-build)

[Install from source](https://matplotlib.org/stable/install/index.html#install-source)

Draw a first plot[#](https://matplotlib.org/stable/users/getting_started/index.html#draw-a-first-plot "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

Here is a minimal example plot:

import matplotlib.pyplot as plt
import numpy as np

x \= np.linspace(0, 2 \* np.pi, 200)
y \= np.sin(x)

fig, ax \= plt.subplots()
ax.plot(x, y)
plt.show()

([`Source code`](https://matplotlib.org/stable/_downloads/33fdd7721ebf0a0381692a5848b85e3f/index-1.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/204d3ab65d82e7f8909502225bb5579e/index-1.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/643ceae5cb607472d92c85dde4ec5d08/index-1.png)
)

[![](https://matplotlib.org/stable/_images/users-getting_started-index-1.2x.png)](https://matplotlib.org/stable/_images/users-getting_started-index-1.2x.png)

If a plot does not show up please check [Troubleshooting](https://matplotlib.org/stable/devel/troubleshooting.html#troubleshooting-faq)
.

Where to go next[#](https://matplotlib.org/stable/users/getting_started/index.html#where-to-go-next "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

*   Check out [Plot types](https://matplotlib.org/stable/plot_types/index.html)
     to get an overview of the types of plots you can create with Matplotlib.
    
*   Learn Matplotlib from the ground up in the [Quick-start guide](https://matplotlib.org/stable/users/explain/quick_start.html#quick-start)
    .
    

On this page