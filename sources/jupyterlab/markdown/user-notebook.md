[Skip to main content](https://jupyterlab.readthedocs.io/en/stable/user/notebook.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [![jupyter.org](https://jupyterlab.readthedocs.io/en/stable/_static/jupyter_logo.svg)](https://jupyter.org/)
    
*   [GitHub](https://github.com/jupyterlab/jupyterlab)
    
*   [Discourse](https://discourse.jupyter.org/c/jupyterlab/17)
    
*   [Zulip](https://jupyter.zulipchat.com/#narrow/channel/469762-jupyterlab)
    

[![Sponsored: MongoDB](https://media.ethicalads.io/images/2023/07/mongodb-codedark-240x180.png)](https://server.ethicalads.io/proxy/click/10792/01a1b9a5-0ae1-7512-b9ca-6faa0100ab7a/)

[**Simplify infrastructure** with MongoDB Atlas, the leading modern database](https://server.ethicalads.io/proxy/click/10792/01a1b9a5-0ae1-7512-b9ca-6faa0100ab7a/)

_[Ad by EthicalAds](https://www.ethicalads.io/?ref=rtd-sidebar)
_   ·   [ℹ️](https://www.ethicalads.io/advertisers/topics/data-science/?ref=rtd-sidebar-buy-ads)

Notebooks[#](https://jupyterlab.readthedocs.io/en/stable/user/notebook.html#notebooks "Link to this heading")

==============================================================================================================

Jupyter notebooks are documents that combine live runnable code with narrative text (Markdown), equations (LaTeX), images, interactive visualizations and other rich output:

![JupyterLab with notebook titled Data.ipynb open. This notebook has text, code, an imported CSV, and an interactive map all in one.](https://jupyterlab.readthedocs.io/en/stable/_images/notebook-ui.png)

**Jupyter notebooks (.ipynb files) are fully supported in JupyterLab.** The [notebook document format](https://nbformat.readthedocs.io/en/latest/)
 used in JupyterLab is the same as in the classic Jupyter Notebook. Your existing notebooks should open correctly in JupyterLab. If they don’t, please open an issue on our [GitHub issues](https://github.com/jupyterlab/jupyterlab/issues)
 page.

Create a notebook by clicking the `+` button in the file browser and then selecting a kernel in the new Launcher tab:

A new file is created with a default name. Rename a file by right-clicking on its name in the file browser and selecting “Rename” from the context menu:

The user interface for notebooks in JupyterLab closely follows that of the classic Jupyter Notebook. The keyboard shortcuts of the classic Notebook continue to work (with command and edit mode). However, a number of new things are possible with notebooks in JupyterLab.

Edit Mode vs Command Mode[#](https://jupyterlab.readthedocs.io/en/stable/user/notebook.html#edit-mode-vs-command-mode "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------

JupyterLab notebooks operate in two primary modes: **Edit Mode** and **Command Mode**.

**Edit Mode**

*   Used to edit the contents of a cell.
    
*   Activated by pressing Enter on a selected cell.
    
*   A blue cell border indicates Edit Mode.
    
*   Keyboard input affects the cell contents.
    

**Command Mode**

*   Used to perform notebook-level actions such as running cells, adding cells, or changing cell types.
    
*   Activated by pressing Esc when not editing text.
    
*   A gray cell border indicates Command Mode.
    
*   Keyboard shortcuts act on entire cells rather than their contents.
    

Pressing Esc exits Edit Mode, while pressing Enter enters Edit Mode on the selected cell.

Working with Cells[#](https://jupyterlab.readthedocs.io/en/stable/user/notebook.html#working-with-cells "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

Drag and drop cells to rearrange your notebook:

Drag cells between notebooks to quickly copy content:

Create multiple synchronized views of a single notebook:

Collapse and expand code and output using the View menu or the blue collapser button on left of each cell:

Enable scrolling for long outputs by right-clicking on a cell and selecting “Enable Scrolling for Outputs”:

Create a new synchronized view of a cell’s output:

Tab completion (activated with the `Tab` key) can now include additional information about the types of the matched items:

Note: IPython 6.3.1 has temporarily disabled type annotations. To re-enable them, add `c.Completer.use_jedi = True` to an [ipython\_config.py](https://ipython.readthedocs.io/en/stable/development/config.html)
 file.

The tooltip (activated with `Shift Tab`) contains additional information about objects:

You can connect a [code console](https://jupyterlab.readthedocs.io/en/stable/user/code_console.html#code-console)
 to a notebook kernel to have a log of computations done in the kernel, in the order in which they were done. The attached code console also provides a place to interactively inspect kernel state without changing the notebook. Right-click on a notebook and select “New Console for Notebook”:

You can iterate through the kernel history in a document cell using `Alt Up-Arrow` and `Alt Down-Arrow`. To use this feature, enable kernel history access in the notebook settings.

Cell Toolbar[#](https://jupyterlab.readthedocs.io/en/stable/user/notebook.html#cell-toolbar "Link to this heading")

--------------------------------------------------------------------------------------------------------------------

In each cell, there is a toolbar that provides quick access to commonly-used functions, if there is enough room to display it on the first line.

If you would like to disable the cell toolbar, open the Settings Editor, choose the Cell Toolbar in the left panel, and uncheck “Show cell toolbar”.

Administrators can turn off the cell toolbar by disabling its extension, by running:

jupyter labextension disable @jupyterlab/cell-toolbar-extension

Copy to clipboard

on the command line. Administrators can turn it back on by running:

jupyter labextension enable @jupyterlab/cell-toolbar-extension

Copy to clipboard

Trust[#](https://jupyterlab.readthedocs.io/en/stable/user/notebook.html#trust "Link to this heading")

------------------------------------------------------------------------------------------------------

JavaScript and HTML in notebooks created on other machines are not trusted, which results in sanitization of HTML and interactive outputs not being displayed until the notebook is explicitly trusted.

The trust status of the active notebook is indicated by a shield icon in the status bar; a checkmark (![../_images/notebook-trusted.png](https://jupyterlab.readthedocs.io/en/stable/_images/notebook-trusted.png)) in the shield indicates a trusted notebook while a cross (![../_images/notebook-not-trusted.png](https://jupyterlab.readthedocs.io/en/stable/_images/notebook-not-trusted.png)) indicates an untrusted notebook. To trust a notebook (and render any blocked outputs) use the `Trust Notebook` command available in the [command palette](https://jupyterlab.readthedocs.io/en/stable/user/commands.html#commands)
.

JupyterLab follows the Jupyter Notebook’s [Security Model](https://jupyter-server.readthedocs.io/en/stable/operators/security.html#our-security-model)
 where any output generated by the current user is trusted, with following implementation details of relevance to advanced users:

1.  manually re-running a non-trusted cell will mark it as trusted,
    
2.  if any of the code cells is not trusted, the entire notebook is considered not trusted and none of the outputs will be trusted upon reopening it (while it is unusual to see a notebook with a single untrusted cell, this can occur when copy-pasting cells from an untrusted notebook),
    
3.  only code cells can be trusted; the Markdown cells are always sanitised.
    

Plotting and Visualization[#](https://jupyterlab.readthedocs.io/en/stable/user/notebook.html#plotting-and-visualization "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------

JupyterLab supports data visualization using libraries like matplotlib, plotly, and others.

**Static Plots with IPython Kernel**

For static plots in JupyterLab with IPython kernel, simply import and use your plotting library of choice - no magic commands are needed:

import matplotlib.pyplot as plt

plt.plot(\[1, 2, 3, 4\])
plt.ylabel('some numbers')
plt.show()

Copy to clipboard

Note

Unlike classic Jupyter Notebook, JupyterLab with IPython kernel displays matplotlib plots automatically without requiring `%matplotlib inline`.

**Interactive Plots, Widgets or Plotting with Other Kernels**

Interactive plots, widgets, or plotting with other kernels may require additional packages to be installed and sometimes a magic command or other kernel native instructions (please refer to the respective library documentation). Common options include:

**Python:**

*   [ipywidgets](https://ipywidgets.readthedocs.io/)
     - Interactive widgets for Jupyter notebooks
    
*   [ipympl](https://github.com/matplotlib/ipympl)
     - Interactive matplotlib backend
    
*   [plotly](https://plotly.com/python/getting-started/#jupyterlab-support)
     - Interactive plotting library
    
*   [bokeh](https://docs.bokeh.org/en/latest/docs/user_guide/output/jupyter.html)
     - Interactive visualization library
    
*   [altair](https://altair-viz.github.io/)
     - Declarative visualization library
    

**R:**

*   [ggplot2](https://ggplot2.tidyverse.org/)
     - Grammar of graphics for R
    

### Mermaid diagrams[#](https://jupyterlab.readthedocs.io/en/stable/user/notebook.html#mermaid-diagrams "Link to this heading")

JupyterLab includes built-in support for rendering Mermaid diagrams in Markdown cells.

Mermaid diagrams can be added using fenced code blocks with the `mermaid` language identifier:

\`\`\`mermaid
graph TD
  A --> B
\`\`\`

Copy to clipboard

which renders as:

Mermaid support is bundled with JupyterLab and does not require installing an additional extension.

Mermaid diagrams are rendered automatically in Markdown cells in notebooks opened in JupyterLab. The diagram source remains visible when editing the Markdown cell.

Paste code cells without output[#](https://jupyterlab.readthedocs.io/en/stable/user/notebook.html#paste-code-cells-without-output "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------

When **Paste code cells without output** is enabled in **Settings → JupyterLab Notebook** (or **Settings → Notebook**), pasting code cells inserts only the cell content, not the outputs. This is useful when you want pasted code to reflect only what was written, without carrying over previous run results.

On this page

[Edit on GitHub](https://github.com/jupyterlab/jupyterlab/edit/4.6.x/docs/source/user/notebook.md)

[Show Source](https://jupyterlab.readthedocs.io/en/stable/_sources/user/notebook.md.txt)