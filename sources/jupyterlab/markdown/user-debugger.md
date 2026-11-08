[Skip to main content](https://jupyterlab.readthedocs.io/en/stable/user/debugger.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [![jupyter.org](https://jupyterlab.readthedocs.io/en/stable/_static/jupyter_logo.svg)](https://jupyter.org/)
    
*   [GitHub](https://github.com/jupyterlab/jupyterlab)
    
*   [Discourse](https://discourse.jupyter.org/c/jupyterlab/17)
    
*   [Zulip](https://jupyter.zulipchat.com/#narrow/channel/469762-jupyterlab)
    

[![Sponsored: MongoDB](https://media.ethicalads.io/images/2026/07/cropped_99bRLm1.png)](https://server.ethicalads.io/proxy/click/10790/01a1b9a4-86be-7f41-89c5-7d7b4cb950a0/)

[Build smarter search with MongoDB Atlas — your vector database for AI apps. **Start free.**](https://server.ethicalads.io/proxy/click/10790/01a1b9a4-86be-7f41-89c5-7d7b4cb950a0/)

_[Ad by EthicalAds](https://www.ethicalads.io/?ref=rtd-sidebar)
_   ·   [ℹ️](https://www.ethicalads.io/advertisers/topics/data-science/?ref=rtd-sidebar-buy-ads)

Debugger[#](https://jupyterlab.readthedocs.io/en/stable/user/debugger.html#debugger "Link to this heading")

============================================================================================================

JupyterLab ships with a Debugger front-end by default.

This means that notebooks, code consoles and files can be debugged from JupyterLab directly!

Requirements[#](https://jupyterlab.readthedocs.io/en/stable/user/debugger.html#requirements "Link to this heading")

--------------------------------------------------------------------------------------------------------------------

For the debugger to be enabled and visible, a kernel with support for debugging is required.

Here is a list of kernels that are known to be supporting the Jupyter Debug Protocol:

*   [xeus-python](https://github.com/jupyter-xeus/xeus-python)
    : Jupyter kernel for the Python programming language
    
*   [xeus-robot](https://github.com/jupyter-xeus/xeus-robot)
    : Jupyter kernel for Robot Framework
    
*   [ipykernel](https://github.com/ipython/ipykernel)
    : IPython Kernel for Jupyter
    
*   [common-lisp-jupyter](https://github.com/yitzchak/common-lisp-jupyter)
    : Common Lisp Kernel for Jupyter
    

Other Jupyter Kernels can also support debugging and be compatible with the JupyterLab debugger by implementing the [Jupyter Debugger Protocol](https://jupyter-client.readthedocs.io/en/latest/messaging.html#debug-request)
.

If you know of other kernels with support for debugging, please open a PR to add them to this list.

Here is an example of how to install `ipykernel` and `xeus-python` in a new `conda` environment:

conda create \-n jupyterlab-debugger \-c conda-forge "jupyterlab>=3" "ipykernel>=6" xeus-python
conda activate jupyterlab-debugger

Copy to clipboard

Usage[#](https://jupyterlab.readthedocs.io/en/stable/user/debugger.html#usage "Link to this heading")

------------------------------------------------------------------------------------------------------

Here is a screencast to enable the debugger and set up breakpoints. The various steps are described more in depth below.

![A GIF showing how to enable the debugger within the kernel.](https://jupyterlab.readthedocs.io/en/stable/_images/step.gif)

### Use a kernel supporting debugger[#](https://jupyterlab.readthedocs.io/en/stable/user/debugger.html#use-a-kernel-supporting-debugger "Link to this heading")

First, you will need to check that the kernel supports debugging. If so, the _bug_ icon in the upper-right corner of the notebook will be enabled.

![../_images/debugger-kernel.png](https://jupyterlab.readthedocs.io/en/stable/_images/debugger-kernel.png)

### Debug code in notebook[#](https://jupyterlab.readthedocs.io/en/stable/user/debugger.html#debug-code-in-notebook "Link to this heading")

Now let’s enable the debugger for this notebook. The debugger can be enabled by toggling the _bug_ button on in the upper-right corner of the notebook:

![../_images/debugger-activate.png](https://jupyterlab.readthedocs.io/en/stable/_images/debugger-activate.png)

Once debugging has been enabled, we can set breakpoints and step into the code.

Let’s define a function that adds two elements:

def add(a, b):
   res \= a + b
   return res

Copy to clipboard

We can call the function and print the result:

result \= add(1, 2)
print(result)

Copy to clipboard

Now let’s go back to the first code cell and click on the gutter on line number 2 to add a breakpoint:

![../_images/debugger-breakpoint.png](https://jupyterlab.readthedocs.io/en/stable/_images/debugger-breakpoint.png)

Then let’s execute the second code cell by clicking on the \_Run\_ button:

![../_images/debugger-run.png](https://jupyterlab.readthedocs.io/en/stable/_images/debugger-run.png)

The execution stops where the breakpoint is set:

![../_images/debugger-stop-on-breakpoint.png](https://jupyterlab.readthedocs.io/en/stable/_images/debugger-stop-on-breakpoint.png)

### Explore the code state[#](https://jupyterlab.readthedocs.io/en/stable/user/debugger.html#explore-the-code-state "Link to this heading")

You can explore the code state with the debugger sidebar. It shows a variable explorer, a list of breakpoints, a list of kernel sources and enables navigating the call stack.

The sidebar may also include a source preview if “Show Sources in Main Area” setting is turned off.

![../_images/debugger-sidebar.png](https://jupyterlab.readthedocs.io/en/stable/_images/debugger-sidebar.png)

**Variables**

The variables panel lists the variables defined in the frame selected in the call stack. The drop down of its toolbar switches between the _Locals_ of that frame and the _Globals_ of the module it belongs to.

Variables can be explored using a tree view and a table view, which are toggled with the two buttons on the right of the toolbar. The tree view shows the value of each variable, and expanding an entry reveals the variables it contains:

![The variables panel in tree view, listing two variables and their values.](https://jupyterlab.readthedocs.io/en/stable/_images/debugger-variables.png)

The table view shows the type of each variable next to its value:

![The variables panel in table view, with a Name, a Type and a Value column.](https://jupyterlab.readthedocs.io/en/stable/_images/debugger-variables-table.png)

In the table view, double-clicking a variable which contains other variables - or choosing _Inspect Variable_ in its context menu - opens its contents as a table of their own in the main area:

![A notebook stopped on a breakpoint, with the items of a list shown in a table below it.](https://jupyterlab.readthedocs.io/en/stable/_images/debugger-variable-inspector.png)

Variables whose value is too large to read in the panel can be opened on their own. When the kernel supports it, hovering over a variable in the tree view reveals a magnifying glass button which renders the variable in the main area, using the same renderers as notebook outputs - so an image is displayed as an image, and a data frame as a table:

![A notebook stopped on a breakpoint, with the value of an image variable rendered in a panel below it.](https://jupyterlab.readthedocs.io/en/stable/_images/debugger-variable-renderer.png)

The panel refreshes as you step through the code, and is closed together with the document it was opened from. The same command is available as _Render Variable_ in the context menu of the variables panel, together with _Copy to Clipboard_, which copies the text representation of the value, and _Copy Variable to Globals_, which copies a local variable to the global scope of the kernel, where it remains reachable once the execution has resumed.

Kernels expose internal variables which are rarely of interest. The variables listed for the kernel in use in the **Variable filter** setting of the Debugger section of the Settings Editor are hidden from both views.

**Call stack**

You can step into the code, and continue the execution using the debug actions:

![../_images/debugger-callstack.png](https://jupyterlab.readthedocs.io/en/stable/_images/debugger-callstack.png)

**Breakpoints**

New breakpoints can be added and removed while the execution is stopped, and they will be shown in the list of breakpoints:

![../_images/debugger-breakpoints.png](https://jupyterlab.readthedocs.io/en/stable/_images/debugger-breakpoints.png)

**Source**

By default the source of the current file being debugged will show up in the main area in a read-only editor view. The auto-opened source view widget will auto-close when the debugger steps into another file, or when the debugging session ends.

![../_images/debugger-open-module.png](https://jupyterlab.readthedocs.io/en/stable/_images/debugger-open-module.png)

If you would like to keep the source view open for longer, you can manually open it by clicking on the file in the “Kernel Sources” panel as manually opened files will not auto-close.

If you prefer the source to show up in the sidebar instead, you can turn off the “Show Sources in Main Area” setting in the Settings Editor which will make it display as another panel:

![../_images/debugger-with-source-panel.png](https://jupyterlab.readthedocs.io/en/stable/_images/debugger-with-source-panel.png)

On this page

[Edit on GitHub](https://github.com/jupyterlab/jupyterlab/edit/4.6.x/docs/source/user/debugger.md)

[Show Source](https://jupyterlab.readthedocs.io/en/stable/_sources/user/debugger.md.txt)