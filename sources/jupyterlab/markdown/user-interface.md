[Skip to main content](https://jupyterlab.readthedocs.io/en/stable/user/interface.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [![jupyter.org](https://jupyterlab.readthedocs.io/en/stable/_static/jupyter_logo.svg)](https://jupyter.org/)
    
*   [GitHub](https://github.com/jupyterlab/jupyterlab)
    
*   [Discourse](https://discourse.jupyter.org/c/jupyterlab/17)
    
*   [Zulip](https://jupyter.zulipchat.com/#narrow/channel/469762-jupyterlab)
    

[![Sponsored: Union AI](https://media.ethicalads.io/images/2026/09/ENVIRONMENTS_240X180.jpg)](https://server.ethicalads.io/proxy/click/11029/01a1b9a4-e6db-7ef3-9998-9f564317c5b3/)

[**Accelerate your agentic workflows.** Set dependencies and environment in Python with Union.ai. **Try free.**](https://server.ethicalads.io/proxy/click/11029/01a1b9a4-e6db-7ef3-9998-9f564317c5b3/)

_[Ad by EthicalAds](https://www.ethicalads.io/?ref=rtd-sidebar)
_   ·   [ℹ️](https://www.ethicalads.io/advertisers/topics/data-science/?ref=rtd-sidebar-buy-ads)

The JupyterLab Interface[#](https://jupyterlab.readthedocs.io/en/stable/user/interface.html#the-jupyterlab-interface "Link to this heading")

=============================================================================================================================================

JupyterLab provides flexible building blocks for interactive, exploratory computing. While JupyterLab has many features found in traditional integrated development environments (IDEs), it remains focused on interactive, exploratory computing.

The JupyterLab interface consists of a [main work area](https://jupyterlab.readthedocs.io/en/stable/user/interface.html#main-area)
 containing tabs of documents and activities, a collapsible [left sidebar](https://jupyterlab.readthedocs.io/en/stable/user/interface.html#left-sidebar)
, and a [menu bar](https://jupyterlab.readthedocs.io/en/stable/user/interface.html#menu-bar)
. The left sidebar contains a [file browser](https://jupyterlab.readthedocs.io/en/stable/user/files.html#working-with-files)
, the [list of running kernels and terminals](https://jupyterlab.readthedocs.io/en/stable/user/commands.html#running)
, the [command palette](https://jupyterlab.readthedocs.io/en/stable/user/commands.html#commands)
, the [notebook cell tools inspector](https://jupyterlab.readthedocs.io/en/stable/user/commands.html#notebook)
, and the [tabs list](https://jupyterlab.readthedocs.io/en/stable/user/interface.html#tabs)
.

![A screenshot of the default JupyterLab interface. The main work area is in the middle. There is also a left sidebar and a top menu bar.](https://jupyterlab.readthedocs.io/en/stable/_images/interface-jupyterlab.png)

JupyterLab sessions always reside in a [workspace](https://jupyterlab.readthedocs.io/en/stable/user/workspaces.html#workspaces)
. Workspaces contain the state of JupyterLab: the files that are currently open, the layout of the application areas and tabs, etc. Workspaces can be saved on the server with [named workspace URLs](https://jupyterlab.readthedocs.io/en/stable/user/urls.html#url-workspaces)
 or [using workspace commands](https://jupyterlab.readthedocs.io/en/stable/user/workspaces.html#workspaces-gui)
 available in the menu and sidebar. To learn more about URLs in JupyterLab, visit [JupyterLab URLs](https://jupyterlab.readthedocs.io/en/stable/user/urls.html#urls)
.

In the user interface, the current workspace can be changed using the workspace selector widget located in the top bar.

To enable the workspace selector, use the main menu: View → Appearance → Show Workspace Indicator.

Menu Bar[#](https://jupyterlab.readthedocs.io/en/stable/user/interface.html#menu-bar "Link to this heading")

-------------------------------------------------------------------------------------------------------------

The menu bar at the top of JupyterLab has top-level menus that expose actions available in JupyterLab with their keyboard shortcuts. The default menus are:

*   **File**: actions related to files and folders
    
*   **Edit**: actions related to editing documents and other activities
    
*   **View**: actions that alter the appearance of JupyterLab
    
*   **Run**: actions for running code in different activities such as notebooks and code consoles
    
*   **Kernel**: actions for managing kernels, which are separate processes for running code
    
*   **Tabs**: a list of the open documents and activities in the dock panel
    
*   **Settings**: common settings and an advanced settings editor
    
*   **Help**: a list of JupyterLab and kernel help links
    

[JupyterLab extensions](https://jupyterlab.readthedocs.io/en/stable/user/extensions.html#user-extensions)
 can also create new top-level menus in the menu bar.

Left and Right Sidebar[#](https://jupyterlab.readthedocs.io/en/stable/user/interface.html#left-and-right-sidebar "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------

The left sidebar contains a number of commonly-used tabs including:

*   a file browser,
    
*   a list of tabs in the main work and of running kernels and terminals,
    
*   the command palette (in 3.0+ moved to a modal window accessible with a [keyboard shortcut](https://jupyterlab.readthedocs.io/en/stable/user/commands.html#access-palette)
    ),
    
*   the [table of contents](https://jupyterlab.readthedocs.io/en/stable/user/commands.html#toc)
    ,
    
*   the [extension manager](https://jupyterlab.readthedocs.io/en/stable/user/extensions.html#extension-manager)
    .
    

![The left JupyterLab sidebar showing a variety of files in the file browser.](https://jupyterlab.readthedocs.io/en/stable/_images/interface-left.png)

The right sidebar contains:

*   the property inspector (active in notebooks),
    
*   the [debugger](https://jupyterlab.readthedocs.io/en/stable/user/commands.html#debugger)
    .
    

![The right JupyterLab sidebar showing the property inspector.](https://jupyterlab.readthedocs.io/en/stable/_images/interface-right.png)

The column that allows to switch between tabs is called Activity Bar in JupyterLab.

The sidebars can be collapsed or expanded by selecting “Show Left Sidebar” or “Show Right Sidebar” in the View menu or by clicking on the active sidebar tab:

The tabs can be moved between the left sidebar, the right sidebar, the [main work area](https://jupyterlab.readthedocs.io/en/stable/user/interface.html#main-area)
, and the down area from the [context menu](https://jupyterlab.readthedocs.io/en/stable/user/interface.html#context-menus-rightclick)
.

JupyterLab extensions can add additional panels to the sidebars.

Main Work Area[#](https://jupyterlab.readthedocs.io/en/stable/user/interface.html#main-work-area "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

The main work area in JupyterLab enables you to arrange documents (notebooks, text files, etc.) and other activities (terminals, code consoles, etc.) into panels of tabs that can be resized or subdivided. Drag a tab to the center of a tab panel to move the tab to the panel. Subdivide a tab panel by dragging a tab to the left, right, top, or bottom of the panel:

The work area has a single current activity. The tab for the current activity is marked with a colored top border (blue by default).

Tabs and Simple Interface Mode[#](https://jupyterlab.readthedocs.io/en/stable/user/interface.html#tabs-and-simple-interface-mode "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------

The Tabs panel in the left sidebar lists the open documents or activities in the main work area:

![The tabs panel in JupyterLab with a list of sample documents.](https://jupyterlab.readthedocs.io/en/stable/_images/interface-tabs.png)

The same information is also available in the Tabs menu:

![The tabs menu in JupyterLab with a list of sample documents.](https://jupyterlab.readthedocs.io/en/stable/_images/interface-tabs-menu.png)

It is often useful to focus on a single document or activity without closing other tabs in the main work area. Simple Interface mode enables this, while making it easy to return to your multi-activity layout in the main work area. Toggle Simple Interface mode using the View menu:

When you leave Simple Interface mode, the original layout of the main area is restored.

Searching[#](https://jupyterlab.readthedocs.io/en/stable/user/interface.html#searching "Link to this heading")

---------------------------------------------------------------------------------------------------------------

JupyterLab has an advanced built-in search plugin for finding text within a notebook or other document, which uses the `Ctrl+F` (`Cmd+F` for macOS) shortcut by default.

Your browser’s `find` function will give unexpected results because it doesn’t have access to the full content of a document (by default), but you can still use your browser find function from the browser menu if you want, or you can disable the built-in search shortcut using the Advanced Settings Editor.

Alternatively, you can disable windowed notebook rendering to expose the full document content to the browser at the expense of performance.

Context Menus[#](https://jupyterlab.readthedocs.io/en/stable/user/interface.html#context-menus "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

Many parts of JupyterLab, such as notebooks, text files, code consoles, and tabs, have context menus that can be accessed by right-clicking on the element:

The browser’s native context menu can be accessed by holding down `Shift` and right-clicking:

Keyboard Shortcuts[#](https://jupyterlab.readthedocs.io/en/stable/user/interface.html#keyboard-shortcuts "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

As in the classic Notebook, you can navigate the user interface through keyboard shortcuts. You can find and customize the current list of keyboard shortcuts by selecting the Advanced Settings Editor item in the Settings menu, then selecting Keyboard Shortcuts in the Settings tab.

To define a custom keyboard shortcut which runs more than one command, add a keyboard shortcut for `apputils:run-all-enabled` command in Keyboard Shortcuts advanced settings. The commands you wish to run are passed in the `args` argument as a list of strings:

{
  "shortcuts": \[\
    {\
      "command": "apputils:run-all-enabled",\
      "keys": \["Accel T"\],\
      "args": {\
        "commands": \["docmanager:save", "application:close"\]\
      },\
      "selector": "body"\
    }\
  \]
}

Copy to clipboard

In this example `docmanager:save` and `application:close` commands are mapped to `Accel T`. The commands are run in succession when you use the shortcut.

### Markdown editing shortcuts[#](https://jupyterlab.readthedocs.io/en/stable/user/interface.html#markdown-editing-shortcuts "Link to this heading")

When editing markdown cells, you can use Ctrl+B (Cmd+B on macOS) to toggle bold formatting. Select text in a markdown cell and press Ctrl+B to wrap it with `**` for bold formatting. Pressing Ctrl+B again on already bold text (text wrapped with `**`) will remove the bold formatting.

You can also customize the [text editor](https://jupyterlab.readthedocs.io/en/stable/user/file_editor.html#file-editor)
 to use vim, emacs, or Sublime Text keyboard maps by using the Text Editor Key Map submenu in the Settings menu:

On this page

[Edit on GitHub](https://github.com/jupyterlab/jupyterlab/edit/4.6.x/docs/source/user/interface.md)

[Show Source](https://jupyterlab.readthedocs.io/en/stable/_sources/user/interface.md.txt)