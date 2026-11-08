[Skip to main content](https://matplotlib.org/stable/gallery/user_interfaces/toolmanager_sgskip.html#main-content)

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
    

Note

[Go to the end](https://matplotlib.org/stable/gallery/user_interfaces/toolmanager_sgskip.html#sphx-glr-download-gallery-user-interfaces-toolmanager-sgskip-py)
 to download the full example code.

Tool Manager[#](https://matplotlib.org/stable/gallery/user_interfaces/toolmanager_sgskip.html#tool-manager "Link to this heading")

===================================================================================================================================

This example demonstrates how to

*   modify the Toolbar
    
*   create tools
    
*   add tools
    
*   remove tools
    

using [`matplotlib.backend_managers.ToolManager`](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager "matplotlib.backend_managers.ToolManager")
.

import matplotlib.pyplot as plt

from matplotlib.backend\_tools import [ToolBase](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolBase "matplotlib.backend_tools.ToolBase")
, [ToolToggleBase](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolToggleBase "matplotlib.backend_tools.ToolToggleBase")

[plt.rcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
\['toolbar'\] \= 'toolmanager'

class ListTools([ToolBase](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolBase "matplotlib.backend_tools.ToolBase")
):
    """List all the tools controlled by the \`ToolManager\`."""
    default\_keymap \= 'm'  \# keyboard shortcut
    description \= 'List Tools'

    def trigger(self, \*args, \*\*kwargs):
        print('\_' \* 80)
        fmt\_tool \= "{:12} {:45} {}".format
        print(fmt\_tool('Name (id)', 'Tool description', 'Keymap'))
        print('-' \* 80)
        tools \= self.toolmanager.tools
        for name in sorted(tools):
            if not tools\[name\].description:
                continue
            keys \= ', '.join(sorted(self.toolmanager.get\_tool\_keymap(name)))
            print(fmt\_tool(name, tools\[name\].description, keys))
        print('\_' \* 80)
        fmt\_active\_toggle \= "{!s:12} {!s:45}".format
        print("Active Toggle tools")
        print(fmt\_active\_toggle("Group", "Active"))
        print('-' \* 80)
        for group, active in self.toolmanager.active\_toggle.items():
            print(fmt\_active\_toggle(group, active))

class GroupHideTool([ToolToggleBase](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolToggleBase "matplotlib.backend_tools.ToolToggleBase")
):
    """Show lines with a given gid."""
    default\_keymap \= 'S'
    description \= 'Show by gid'
    default\_toggled \= True

    def \_\_init\_\_(self, \*args, gid, \*\*kwargs):
        self.gid \= gid
        super().\_\_init\_\_(\*args, \*\*kwargs)

    def enable(self, \*args):
        self.set\_lines\_visibility(True)

    def disable(self, \*args):
        self.set\_lines\_visibility(False)

    def set\_lines\_visibility(self, state):
        for ax in self.figure.get\_axes():
            for line in ax.get\_lines():
                if line.get\_gid() \== self.gid:
                    line.set\_visible(state)
        self.figure.canvas.draw()

fig \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(\[1, 2, 3\], gid\='mygroup')
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(\[2, 3, 4\], gid\='unknown')
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(\[3, 2, 1\], gid\='mygroup')

\# Add the custom tools that we created
fig.canvas.manager.toolmanager.add\_tool('List', ListTools)
fig.canvas.manager.toolmanager.add\_tool('Show', GroupHideTool, gid\='mygroup')

\# Add an existing tool to new group \`foo\`.
\# It can be added as many times as we want
fig.canvas.manager.toolbar.add\_tool('zoom', 'foo')

\# Remove the forward button
fig.canvas.manager.toolmanager.remove\_tool('forward')

\# To add a custom tool to the toolbar at specific location inside
\# the navigation group
fig.canvas.manager.toolbar.add\_tool('Show', 'navigation', 1)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: toolmanager_sgskip.ipynb`](https://matplotlib.org/stable/_downloads/499eb6b1efccd27db9210432c068429f/toolmanager_sgskip.ipynb)

[`Download Python source code: toolmanager_sgskip.py`](https://matplotlib.org/stable/_downloads/88202b665d8f6222af7a70d1737e6584/toolmanager_sgskip.py)

[`Download zipped: toolmanager_sgskip.zip`](https://matplotlib.org/stable/_downloads/7712dbade8bcd26b467cb0c2a2e9a283/toolmanager_sgskip.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)