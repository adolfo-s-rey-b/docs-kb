[Skip to main content](https://jupyterlab.readthedocs.io/en/stable/user/urls.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [![jupyter.org](https://jupyterlab.readthedocs.io/en/stable/_static/jupyter_logo.svg)](https://jupyter.org/)
    
*   [GitHub](https://github.com/jupyterlab/jupyterlab)
    
*   [Discourse](https://discourse.jupyter.org/c/jupyterlab/17)
    
*   [Zulip](https://jupyter.zulipchat.com/#narrow/channel/469762-jupyterlab)
    

JupyterLab URLs[#](https://jupyterlab.readthedocs.io/en/stable/user/urls.html#jupyterlab-urls "Link to this heading")

======================================================================================================================

Like the classic notebook, JupyterLab provides a way for users to copy URLs that open a specific notebook or file. Additionally, JupyterLab URLs are an advanced part of the user interface that allows for managing workspaces. These two functions – file paths and workspaces – can be [combined in URLs that open a specific file in a specific workspace](https://jupyterlab.readthedocs.io/en/stable/user/urls.html#url-combine)
.

File Navigation with `/tree`[#](https://jupyterlab.readthedocs.io/en/stable/user/urls.html#file-navigation-with-tree "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------

JupyterLab’s file navigation URLs adopts the nomenclature of the classic notebook; these URLs are `/tree` URLs:

http(s)://<server:port>/<lab-location>/lab/tree/path/to/notebook.ipynb

Copy to clipboard

By default, the file browser will navigate to the folder containing the requested file. This behavior can be changed with the optional `file-browser-path` query parameter:

http(s)://<server:port>/<lab-location>/lab/tree/path/to/notebook.ipynb?file-browser-path=/

Copy to clipboard

Entering the above URL will show the workspace root folder instead of the `/path/to/` folder in the file browser.

Linking Notebook Sections[#](https://jupyterlab.readthedocs.io/en/stable/user/urls.html#linking-notebook-sections "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------

To create an URL which will scroll to a specific heading in the notebook append a hash (`#`) followed by the heading text with spaces replaced by minus characters (`-`), for example:

/lab/tree/path/to/notebook.ipynb?#my-heading

Copy to clipboard

To get a link for a specific heading, hover over it in a rendered markdown cell until you see a pilcrow mark (`¶`) which will contain the desired anchor link:

![A markdown cell with pilcrow mark (¶) which serves as an anchor link and is placed after a heading](https://jupyterlab.readthedocs.io/en/stable/_images/notebook-heading-anchor-link.png)

Note

Currently disambiguation of headings with identical text is not supported.

JupyterLab experimentally supports scrolling to a specified cell by identifier using `#cell-id=<cell-id>` Fragment Identification Syntax.

/lab/tree/path/to/notebook.ipynb?#cell-id=my-cell-id

Copy to clipboard

Note

The `cell-id` fragment locator is not part of a formal Jupyter standard and subject to change. To leave feedback, please comment in the discussion: [nbformat#317](https://github.com/jupyter/nbformat/issues/317)
.

Managing Workspaces (URL)[#](https://jupyterlab.readthedocs.io/en/stable/user/urls.html#managing-workspaces-url "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

JupyterLab sessions always reside in a workspace. Workspaces contain the state of JupyterLab: the files that are currently open, the layout of the application areas and tabs, etc. When the page is refreshed, the workspace is restored.

The default workspace does not have a name and resides at the primary `/lab` URL:

http(s)://<server:port>/<lab-location>/lab

Copy to clipboard

All other workspaces have a name that is part of the URL:

http(s)://<server:port>/<lab-location>/lab/workspaces/foo

Copy to clipboard

Workspaces save their state on the server and can be shared between multiple users (or browsers) as long as they have access to the same server.

A workspace should only be open in a single browser tab at a time. If JupyterLab detects that a workspace is being opened multiple times simultaneously, it will prompt for a new workspace name.

Cloning Workspaces[#](https://jupyterlab.readthedocs.io/en/stable/user/urls.html#cloning-workspaces "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

You can copy the contents of a workspace into another workspace with the `clone` url parameter.

To copy the contents of the workspace `foo` into the workspace `bar`:

http(s)://<server:port>/<lab-location>/lab/workspaces/bar?clone=foo

Copy to clipboard

To copy the contents of the default workspace into the workspace `foo`:

http(s)://<server:port>/<lab-location>/lab/workspaces/foo?clone

Copy to clipboard

To copy the contents of the workspace `foo` into the default workspace:

http(s)://<server:port>/<lab-location>/lab?clone=foo

Copy to clipboard

Resetting a Workspace[#](https://jupyterlab.readthedocs.io/en/stable/user/urls.html#resetting-a-workspace "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

Use the `reset` url parameter to clear a workspace of its contents.

To reset the contents of the workspace `foo`:

http(s)://<server:port>/<lab-location>/lab/workspaces/foo?reset

Copy to clipboard

To reset the contents of the default workspace:

http(s)://<server:port>/<lab-location>/lab/workspaces/lab?reset

Copy to clipboard

Combining URL Functions[#](https://jupyterlab.readthedocs.io/en/stable/user/urls.html#combining-url-functions "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------

These URL functions can be used separately, as above, or in combination.

To reset the workspace `foo` and load a specific notebook afterward:

http(s)://<server:port>/<lab-location>/lab/workspaces/foo/tree/path/to/notebook.ipynb?reset

Copy to clipboard

To clone the contents of the workspace `bar` into the workspace `foo` and load a notebook afterward:

http(s)://<server:port>/<lab-location>/lab/workspaces/foo/tree/path/to/notebook.ipynb?clone=bar

Copy to clipboard

To reset the contents of the default workspace and load a notebook:

http(s)://<server:port>/<lab-location>/lab/tree/path/to/notebook.ipynb?reset

Copy to clipboard

On this page

[Edit on GitHub](https://github.com/jupyterlab/jupyterlab/edit/4.6.x/docs/source/user/urls.md)

[Show Source](https://jupyterlab.readthedocs.io/en/stable/_sources/user/urls.md.txt)