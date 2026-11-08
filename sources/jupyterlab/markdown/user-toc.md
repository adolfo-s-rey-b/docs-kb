[Skip to main content](https://jupyterlab.readthedocs.io/en/stable/user/toc.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [![jupyter.org](https://jupyterlab.readthedocs.io/en/stable/_static/jupyter_logo.svg)](https://jupyter.org/)
    
*   [GitHub](https://github.com/jupyterlab/jupyterlab)
    
*   [Discourse](https://discourse.jupyter.org/c/jupyterlab/17)
    
*   [Zulip](https://jupyter.zulipchat.com/#narrow/channel/469762-jupyterlab)
    

[![Sponsored: Union AI](https://media.ethicalads.io/images/2026/09/OOM_RETRY_240X180.jpg)](https://server.ethicalads.io/proxy/click/11030/01a1b9a4-fa6a-7ab2-b90d-f9adc4656f8a/)

[**OOM? Retry with more.** Handle OOMs in Python. Retry with more memory on Union.ai. **Sign Up Now**](https://server.ethicalads.io/proxy/click/11030/01a1b9a4-fa6a-7ab2-b90d-f9adc4656f8a/)

_[Ad by EthicalAds](https://www.ethicalads.io/?ref=rtd-sidebar)
_   ·   [ℹ️](https://www.ethicalads.io/advertisers/topics/data-science/?ref=rtd-sidebar-buy-ads)

Table Of Contents[#](https://jupyterlab.readthedocs.io/en/stable/user/toc.html#table-of-contents "Link to this heading")

=========================================================================================================================

The table of contents makes it easy to see and navigate the structure of a document.

A table of contents is auto-generated in the [left sidebar](https://jupyterlab.readthedocs.io/en/stable/user/interface.html#left-sidebar)
 when you have a notebook, markdown, latex or python files opened. The entries are clickable, and scroll the document to the heading in question.

In the sidebar panel, you can number headings, collapse sections, and navigate into the file.

Here is an animation showing the table of content use with a notebook:

![A GIF displaying how to use the table of contents feature within a notebook. It toggles which cells types are listed and toggles expanding and collapsing headings.](https://jupyterlab.readthedocs.io/en/stable/_images/toc.gif)

The table of contents will be automatically generated for your notebook by taking all the headings from your markdown cells. Each listed section will be linked to the actual section within your document.

Note

Markdown headings with a HTML tag that contains the class `jp-toc-ignore` will be ignored; e.g. `# Title <a class="jp-toc-ignore"></a>`.

Automatic section numbering will go through your Notebook and number your sections and subsection as designated by your headings. This means that if you’ve moved one or more big sections around several times, you won’t have to go through your document and renumber it, as well as all its subsections, yourself.

* * *

Automatic section numbering can be skipped for first-level headings (`h1`). You can toggle that option via the _More actions_ button in the table of contents toolbar. Here is an animation showing its use:

![A GIF showing how to toggle Automatic section numbering for headings within a notebook. Clicking the button instantly applies multilevel numbering to each heading.](https://jupyterlab.readthedocs.io/en/stable/_images/numberingH1.gif)

* * *

Context menus are added to those table of contents headings having notebook sections containing runnable code cells, and clicking the _Select and Run Cell(s) for this Heading_ option will make the cells run in notebook. Here is an animation showing its use:

![../_images/runcell.gif](https://jupyterlab.readthedocs.io/en/stable/_images/runcell.gif)

* * *

> Cell heading collapse state will be synchronized between the table of contents and notebook if the `syncCollapseState` attribute is set to `true` in the settings. If a heading is collapsed in the table of contents the notebook will also gets collapsed and similarly expanding cells in notebook will expand the table of contents. To activate that feature go to settings and click on Settings Editor and then go to Table of Contents section and in User Preferences check the `syncCollapseState` box. Here is an animation showing its use:

![../_images/syncCollapseState.gif](https://jupyterlab.readthedocs.io/en/stable/_images/syncCollapseState.gif)

* * *

The headings in the cell outputs get numbered by default in the table of contents and the notebook. This can be tuned by changing the settings `includeOutput` to `false`. To perform that go to settings and click on Settings Editor and then go to Table of Contents section and in User Preferences add unchecked `includeOutput` box. Here is an animation showing its use

![../_images/includeOutput.gif](https://jupyterlab.readthedocs.io/en/stable/_images/includeOutput.gif)

Settings[#](https://jupyterlab.readthedocs.io/en/stable/user/toc.html#settings "Link to this heading")

-------------------------------------------------------------------------------------------------------

The table of contents behavior can be modified via settings which can be set in JupyterLab’s settings editor.

*   **includeOutput** : Whether to list headings from the cell outputs or not.
    
*   **maximalDepth** : Maximal headings depth (default: 4).
    
*   **numberingH1** : Whether to number the first-level headings (`h1`) or not.
    
*   **numberHeaders** : Whether to number the headings or not.
    
*   **syncCollapseState** : Whether to synchronize the cell and the table of contents collapse state or not.
    
*   **baseNumbering** : Starting point for heading numbering (default: 1).
    

Note

Settings effects depend on the type of document.

On this page

[Edit on GitHub](https://github.com/jupyterlab/jupyterlab/edit/4.6.x/docs/source/user/toc.md)

[Show Source](https://jupyterlab.readthedocs.io/en/stable/_sources/user/toc.md.txt)