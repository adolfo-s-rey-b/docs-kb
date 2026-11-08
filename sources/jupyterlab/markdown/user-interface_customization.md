[Skip to main content](https://jupyterlab.readthedocs.io/en/stable/user/interface_customization.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [![jupyter.org](https://jupyterlab.readthedocs.io/en/stable/_static/jupyter_logo.svg)](https://jupyter.org/)
    
*   [GitHub](https://github.com/jupyterlab/jupyterlab)
    
*   [Discourse](https://discourse.jupyter.org/c/jupyterlab/17)
    
*   [Zulip](https://jupyter.zulipchat.com/#narrow/channel/469762-jupyterlab)
    

[![Sponsored: Union AI](https://media.ethicalads.io/images/2026/09/REUSABLE_CONTAINERS_240X180.jpg)](https://server.ethicalads.io/proxy/click/11031/01a1b9a4-f11f-7492-8933-bc184f665a95/)

[**Scale and accelerate your AI inference.** Reuse containers across tasks on Union.ai. **Drop cold starts**](https://server.ethicalads.io/proxy/click/11031/01a1b9a4-f11f-7492-8933-bc184f665a95/)

_[Ad by EthicalAds](https://www.ethicalads.io/?ref=rtd-sidebar)
_   ·   [ℹ️](https://www.ethicalads.io/advertisers/topics/data-science/?ref=rtd-sidebar-buy-ads)

Interface Customization[#](https://jupyterlab.readthedocs.io/en/stable/user/interface_customization.html#interface-customization "Link to this heading")

=========================================================================================================================================================

Multiple elements in the JupyterLab interface are customizable to display new elements or hide default ones.

Layout[#](https://jupyterlab.readthedocs.io/en/stable/user/interface_customization.html#layout "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

The JupyterLab layout has two modes: the simple mode (or _single document_ mode) and the default mode (or _multiple documents_ mode). In both modes, the widgets are attached in one of the four area: the `left` or `right` sidebars, the `main` dock panel area or the `down` area.

The default positions of widgets can be overridden through the settings based on the type of widgets. The setting to modify is the _layout_ one in section _JupyterLab Shell_.

The available widget types and their default area is listed below

| Type | multiple | single |
| --- | --- | --- |
| Console | main | main |
| CSVTable | main | main |
| TSVTable | main | main |
| Editor | main | main |
| HTML Viewer | main | main |
| Image | main | main |
| Image (Text) | main | main |
| JSON | main | main |
| Markdown Preview | main | main |
| Notebook | main | main |
| Cloned Output | main | down |
| Linked Console | main | down |
| Inspector | main | down |
| PDF | main | main |
| Terminal | main | main |
| VDOM | main | main |
| Vega-Lite4 | main | main |
| Vega5 | main | main |
| Settings | main | main |
| Advanced Settings | main | main |
| Licenses | main | main |
| Debugger | right | right |
| Debugger Variables | main | main |
| Debugger Sources | main | main |
| Property Inspector | right | right |
| Extension Manager | left | left |
| File Browser | left | left |
| Sessions and Tabs | left | left |
| Table of Contents | left | left |
| Log Console | down | down |

"layout": {
  "single": {
    "Linked Console": { "area": "down" },
    "Inspector": { "area": "down" },
    "Cloned Output": { "area": "down" },
    // Add new terminals in the down area in simple mode
    "Terminal": { "area": "down" }
  },
  "multiple": {
    // Add new terminals in the right sidebar in default mode
    "Terminal": { "area": "right" }
  }
}

Copy to clipboard

The above example will result in the following changes:

![(Before Change) Default terminal position in "multiple" (default) mode](https://jupyterlab.readthedocs.io/en/stable/_images/default-terminal-position-single.png)

(Before Change) Default terminal position in “multiple” (default) mode[#](https://jupyterlab.readthedocs.io/en/stable/user/interface_customization.html#id3 "Link to this image")

![(After Change) Customized terminal position in "multiple" (default) mode](https://jupyterlab.readthedocs.io/en/stable/_images/customized-terminal-position-single.png)

(After Change) Customized terminal position in “multiple” (default) mode[#](https://jupyterlab.readthedocs.io/en/stable/user/interface_customization.html#id4 "Link to this image")

### Move open widgets[#](https://jupyterlab.readthedocs.io/en/stable/user/interface_customization.html#move-open-widgets "Link to this heading")

You can also move an open widget directly from its tab context menu. Right-click the widget tab in a sidebar, the main work area, or the down area, select **Move Widget To**, and choose the destination area.

![The Move Widget To submenu showing the available destination areas.](https://jupyterlab.readthedocs.io/en/stable/_images/move-widget-submenu.png)

The Move Widget To submenu lists the available destination areas.[#](https://jupyterlab.readthedocs.io/en/stable/user/interface_customization.html#id5 "Link to this image")

![The file browser moved from the left sidebar to the main work area.](https://jupyterlab.readthedocs.io/en/stable/_images/move-file-browser-main-area.png)

The file browser moved from the left sidebar to the main work area.[#](https://jupyterlab.readthedocs.io/en/stable/user/interface_customization.html#id6 "Link to this image")

![The sessions and tabs panel moved from the left sidebar to the down area.](https://jupyterlab.readthedocs.io/en/stable/_images/move-running-sessions-down-area.png)

The sessions and tabs panel moved from the left sidebar to the down area.[#](https://jupyterlab.readthedocs.io/en/stable/user/interface_customization.html#id7 "Link to this image")

Those changes are stored in the workspace layout, so they are restored when you reopen the same workspace. They do not change the type-based `layout` setting described above, which controls the default area for future widgets.

### Move accordion sections between panels[#](https://jupyterlab.readthedocs.io/en/stable/user/interface_customization.html#move-accordion-sections-between-panels "Link to this heading")

Individual accordion sections within a sidebar panel can be moved to another panel via the context menu.

1.  Right-click the section header (e.g. “OPEN TABS”) in the Running Sessions panel.
    
2.  Choose **Move to File Browser**.
    

![The Running Sessions sidebar context menu with the "Move to File Browser" option highlighted.](https://jupyterlab.readthedocs.io/en/stable/_images/sidebar-context-menu.png)

The section appears inside the File Browser, where it can be dragged to reorder it above or below the file listing. To move it back, right-click the section header and choose **Move back to Running Sessions**. The layout is saved and restored on reload.

Activity Bar Position[#](https://jupyterlab.readthedocs.io/en/stable/user/interface_customization.html#activity-bar-position "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------

The side activity bars (left and right) display the tabs of the widgets attached to the corresponding side area. By default, each activity bar is rendered vertically on the natural side of its area (left for the left area, right for the right area). You can move them to the top or bottom of their area to display the tabs horizontally.

The position is controlled by the `activityBarPosition` setting in the _JupyterLab Shell_ section. The available values are:

*   `side` (default): each activity bar stays on the natural side of its area
    
*   `top`: both activity bars are moved to the top of their respective area
    
*   `bottom`: both activity bars are moved to the bottom of their respective area
    

"activityBarPosition": "top"

Copy to clipboard

The same options are also available interactively from the _View_ → _Appearance_ → _Activity Bar Position_ menu.

The screenshots below illustrate the `top` and `bottom` positions:

![Activity bar positioned at the top of each side area](https://jupyterlab.readthedocs.io/en/stable/_images/customized-activity-bar-top.png)

Activity bar positioned at the top of each side area[#](https://jupyterlab.readthedocs.io/en/stable/user/interface_customization.html#id8 "Link to this image")

![Activity bar positioned at the bottom of each side area](https://jupyterlab.readthedocs.io/en/stable/_images/customized-activity-bar-bottom.png)

Activity bar positioned at the bottom of each side area[#](https://jupyterlab.readthedocs.io/en/stable/user/interface_customization.html#id9 "Link to this image")

Toolbars[#](https://jupyterlab.readthedocs.io/en/stable/user/interface_customization.html#toolbars "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

In addition to the toolbars attached to individual widgets, JupyterLab provides a TopBar extension point that allows extensions to add items to the application top bar area.

Lots of toolbars are customizable. Here is a mapping of the customizable toolbars and the associated setting.

*   Cell: _Cell Toolbar_ -> _toolbar_
    
*   CSV Viewer: _CSV Viewer_ -> _toolbar_
    
*   File Browser: _File Browser Widget_ -> _toolbar_
    
*   HTML Viewer: _HTML Viewer_ -> _toolbar_
    
*   Notebook panel: _Notebook Panel_ -> _toolbar_
    
*   Text Editor: _Text Editor_ -> _toolbar_
    
*   TSV Viewer: _TSV Viewer_ -> _toolbar_
    

Those settings are accessible through the interactive _Settings Editor_. But you may find more comfortable to use the _Advanced Settings Editor_ (accessible by clicking on _JSON Settings Editor_ button in the top right corner of the _Settings Editor_).

Your `toolbar` customization will be merged with the default menu bar definition (this is a different behavior as the other settings that are overriding the default settings). So to remove a default item, you will need to disable it. To do that, you will need to set the toolbar item `disabled` attribute to `true`; an item is uniquely identified by its `name` attribute.

"toolbar": \[\
  // Disable the restart and run all button\
  {\
    "name": "restart-and-run",\
    "disabled": true\
  },\
  // Add a new button to clear all cell outputs\
  {\
    "name": "clear-all-outputs",\
    "command": "notebook:clear-all-cell-outputs"\
  }\
\]

Copy to clipboard

The above example for the notebook panel, will results in the following changes:

![Default notebook toolbar](https://jupyterlab.readthedocs.io/en/stable/_images/default-notebook-toolbar.png)

Default notebook toolbar[#](https://jupyterlab.readthedocs.io/en/stable/user/interface_customization.html#id10 "Link to this image")

![Customized notebook toolbar](https://jupyterlab.readthedocs.io/en/stable/_images/customized-notebook-toolbar.png)

Customized notebook toolbar[#](https://jupyterlab.readthedocs.io/en/stable/user/interface_customization.html#id11 "Link to this image")

A toolbar is defined by a list of items. Each item must have an unique `name`. That name will create a toolbar item if it is associated with a special widget (e.g. the cell type toolbar selector). Otherwise it will require a `command` that will be triggered when clicking on a toolbar button (see the available [Commands list](https://jupyterlab.readthedocs.io/en/stable/user/commands.html#commands-list)
). The items are sorted by their `rank`.

Note

If you want to more advanced customization please refer to the [Toolbar item definition](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#toolbar-item)
.

Menu Bar[#](https://jupyterlab.readthedocs.io/en/stable/user/interface_customization.html#menu-bar "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

The top menu bar definition can be customized through the _Advanced Settings Editor_. You can access it by opening the _Settings Editor_ from the _Settings_ menu, then click on the _JSON Settings Editor_ in the top right corner.

In the _Advanced Settings Editor_, you will need to select the _Main Menu_ section in the left panel. Your `menus` customization will be merged with the default menu bar definition (this is a different behavior as the other settings that are overriding the default settings). So to remove a default entry, you will need to disable it. To do that, you will need to set the menu entry `disabled` attribute to `true`; an entry is uniquely identified by its `command` and `args` attributes.

New entries can be added to existing menus or you can create new menus.

"menus": \[\
  {\
    // Disable the Run menu\
    "id": "jp-mainmenu-run",\
    "disabled": true\
  },\
  {\
    // Move the Tabs menu to the end by changing its rank\
    "id": "jp-mainmenu-tabs",\
    "rank": 1100,\
    "items": \[\
        // Add a new entry in the Tabs menu\
        {\
            "command": "launcher:create",\
            "rank": 0\
        }\
    \]\
  },\
  {\
    // Disable the Open from Path entry in the File menu\
    "id": "jp-mainmenu-file",\
    "items": \[\
      {\
        "command": "filebrowser:open-path",\
        "disabled": true\
      }\
    \]\
  }\
\]

Copy to clipboard

The above example, will results in the following changes:

![Default menu bar](https://jupyterlab.readthedocs.io/en/stable/_images/default-menu-bar.png)

Default menu bar[#](https://jupyterlab.readthedocs.io/en/stable/user/interface_customization.html#id12 "Link to this image")

![Customized menu bar](https://jupyterlab.readthedocs.io/en/stable/_images/customized-menu-bar.png)

Customized menu bar[#](https://jupyterlab.readthedocs.io/en/stable/user/interface_customization.html#id13 "Link to this image")

The menu are identified by the following ids:

*   File menu: `jp-mainmenu-file`
    
    *   New file submenu: `jp-mainmenu-file-new`
        
*   Edit menu: `jp-mainmenu-edit`
    
*   View menu: `jp-mainmenu-view`
    
    *   Appearance submenu: `jp-mainmenu-view-appearance`
        
*   Run menu: `jp-mainmenu-run`
    
*   Kernel menu: `jp-mainmenu-kernel`
    
*   Tabs menu: `jp-mainmenu-tabs`
    
*   Settings menu: `jp-mainmenu-settings`
    
*   Help menu: `jp-mainmenu-help`
    

An entry can be any valid command available; see [Commands list](https://jupyterlab.readthedocs.io/en/stable/user/commands.html#commands-list)
. And the entries are sorted by their ranks.

Note

If you want to more advanced customization (e.g. changing the separators or sub-menus), please refer to the [Main Menu settings definition](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#mainmenu)
.

Context Menu[#](https://jupyterlab.readthedocs.io/en/stable/user/interface_customization.html#context-menu "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------

The context menu definition can be customized through the _Advanced Settings Editor_. You can access it by opening the _Settings Editor_ from the _Settings_ menu, then click on the _JSON Settings Editor_ in the top right corner.

In the _Advanced Settings Editor_, you will need to the select the _Application Context Menu_ section in the left panel. Your `contextMenu` customization will be merged with the default context menu definition (this is a different behavior as the other settings that are overriding the default settings). So to remove a default entry, you will need to disable it. To do that, you will need to set the menu entry `disabled` attribute to `true`; an entry is uniquely identified by its `command`, `selector` and `args` attributes.

New entries can be added to existing menus.

"contextMenu": \[\
  // Disable New notebook entry\
  {\
    "command": "notebook:create-new",\
    "selector": ".jp-DirListing-content",\
    "args": {\
      "isContextMenu": true\
    },\
    "disabled": true\
  },\
  // Add new entry on notebook file to export them as Markdown\
  {\
    "command": "notebook:export-to-format",\
    "selector": ".jp-DirListing-item\[data-file-type=\\"notebook\\"\]",\
    "rank": 3,\
    // Command arguments\
    "args": {\
      "format": "markdown",\
      "label": "Export as Markdown"\
    }\
  }\
\]

Copy to clipboard

The above example, will results in the following changes:

![Default context menu](https://jupyterlab.readthedocs.io/en/stable/_images/default-context-menu.png)

Default context menu[#](https://jupyterlab.readthedocs.io/en/stable/user/interface_customization.html#id14 "Link to this image")

![Customized context menu](https://jupyterlab.readthedocs.io/en/stable/_images/customized-context-menu.png)

Customized context menu[#](https://jupyterlab.readthedocs.io/en/stable/user/interface_customization.html#id15 "Link to this image")

An entry can be any valid command available; see [Commands list](https://jupyterlab.readthedocs.io/en/stable/user/commands.html#commands-list)
. And a CSS selector to define which elements will have that context menu entry. And the entries are sorted by their ranks.

Note

If you want to more advanced customization (e.g. changing the separators or sub-menus), please refer to the [Context Menu settings definition](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#context-menu)
.

### File Browser[#](https://jupyterlab.readthedocs.io/en/stable/user/interface_customization.html#file-browser "Link to this heading")

Users can add a “Open in Simple Mode” context menu option by adding the following to _Settings_ -> _Application Context Menu_ -> `contextMenu`

{
  "command": "filebrowser:open-browser-tab",
  "args": { "mode": "single-document" },
  "selector": ".jp-DirListing-item\[data-isdir=\\"false\\"\]",
  "rank": 1.6
}

Copy to clipboard

Applying Custom CSS[#](https://jupyterlab.readthedocs.io/en/stable/user/interface_customization.html#applying-custom-css "Link to this heading")

=================================================================================================================================================

To apply custom CSS, you can add a `/custom/custom.css` file in the jupyter `config` directory. You can find the path, `~/.jupyter`, to this directory by running `jupyter --paths`. There you can create a folder named `custom` and create a `custom.css` file within the folder.

Custom CSS is not loaded by default. In the jupyter configuration directory, the `~/.jupyter/custom/custom.css` file will not be loaded unless the the application is initialized with the `--custom-css` flag (`LabApp.custom_css` config).

Jupyter Styling[#](https://jupyterlab.readthedocs.io/en/stable/user/interface_customization.html#jupyter-styling "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------

You can use a custom CSS file to modify default Jupyter styling.

/\* Modify Jupyter Styles \*/

.lm-BoxPanel-child,
.jp-FileBrowser-Panel,
.lm-StackedPanel-child,
.jp-FileBrowser-toolbar {
  background-color: #aecad4 !important;
}

#top-panel-wrapper,
#jp-top-bar {
  background-color: #aecad4 !important;
}

#menu-panel-wrapper,
#jp-MainMenu,
#menu-panel {
  background-color: #aecad4 !important;
}

.jp-NotebookPanel-toolbar {
  background-color: #aecad4 !important;
}

.lm-MenuBar-content {
  color: #02484d;
}

.lm-TabBar-content,
.jp-DirListing-content,
.lm-MenuBar-content {
  font-size: small;
}

Copy to clipboard

![a screenshot custom jupyter styling](https://jupyterlab.readthedocs.io/en/stable/_images/custom-css-main.png)

Markdown Styling[#](https://jupyterlab.readthedocs.io/en/stable/user/interface_customization.html#markdown-styling "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------

Another potential application for custom CSS is styling markdown.

/\* Styling Markdown \*/

/\* Headings \*/
h1,
h2 {
  font-family: 'DejaVu Mono', sans-serif;
  font-weight: bold;
  text-shadow: 2px 2px 4px #000;
}

h1 {
  font-size: 22px;
  margin-bottom: 40px;
  color: #10929e;
  text-decoration: underline;
}

h2 {
  font-size: 48px;
  margin-bottom: 32px;
  color: #76b4be;
  text-transform: uppercase;
}

/\* Block Quotes \*/
blockquote {
  font-family: 'DejaVu Mono', serif;
  font-size: 16px;
  color: #19085c;
  border-left: 8px solid #effffc;
  background-color: #eafcff;
  padding: 20px;
}

/\* Lists \*/
ul,
ol {
  font-family: 'DejaVu Mono', sans-serif;
  font-size: 18px;
  color: #333;
  margin-bottom: 24px;
}

Copy to clipboard

![a screenshot of custom markdown styling](https://jupyterlab.readthedocs.io/en/stable/_images/custom-css-notebook-markdown.png)

Settings Editor Plugin Filtering[#](https://jupyterlab.readthedocs.io/en/stable/user/interface_customization.html#settings-editor-plugin-filtering "Link to this heading")

===========================================================================================================================================================================

The Settings Editor supports configurable filtering of plugins to hide specific plugins from the settings interface. This allows administrators and power users to hide complex or sensitive plugins while keeping them fully functional. The hidden plugins will remain accessible in the JSON Settings Editor.

Configuration Options[#](https://jupyterlab.readthedocs.io/en/stable/user/interface_customization.html#configuration-options "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------

### Via Settings UI[#](https://jupyterlab.readthedocs.io/en/stable/user/interface_customization.html#via-settings-ui "Link to this heading")

1.  Open JupyterLab Settings Editor (_Settings > Settings Editor_)
    
2.  Search for “Settings Editor Form UI”
    
3.  Find the “Additional plugins to skip in settings editor” field
    
4.  Add plugin IDs in the format `package:plugin`
    
5.  Save the settings
    

### Via overrides.json[#](https://jupyterlab.readthedocs.io/en/stable/user/interface_customization.html#via-overrides-json "Link to this heading")

Add the following to your `overrides.json` file:

{
  "@jupyterlab/settingeditor-extension:form-ui": {
    "toSkip": \["my-extension:plugin-to-hide", "another-extension:config-plugin"\]
  }
}

Copy to clipboard

Always Hidden Plugins[#](https://jupyterlab.readthedocs.io/en/stable/user/interface_customization.html#always-hidden-plugins "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------

The following plugins are hidden by default from the settings editor:

*   `@jupyterlab/application-extension:context-menu`
    
*   `@jupyterlab/mainmenu-extension:plugin`
    

Plugin ID Format[#](https://jupyterlab.readthedocs.io/en/stable/user/interface_customization.html#plugin-id-format "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------

Plugin IDs usually follow the format: `package-name:plugin-name`

For a complete list of core plugin IDs, see the [Core Plugins](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#core-tokens)
 documentation.

Alternatives[#](https://jupyterlab.readthedocs.io/en/stable/user/interface_customization.html#alternatives "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------

If you need to completely disable plugin functionality, consider:

*   Disabling extensions entirely via the Extension Manager
    
*   Using `page_config.json` to disable specific plugins
    
*   Using the command line: `jupyter labextension disable package-name:plugin-name`
    

On this page

[Edit on GitHub](https://github.com/jupyterlab/jupyterlab/edit/4.6.x/docs/source/user/interface_customization.md)

[Show Source](https://jupyterlab.readthedocs.io/en/stable/_sources/user/interface_customization.md.txt)