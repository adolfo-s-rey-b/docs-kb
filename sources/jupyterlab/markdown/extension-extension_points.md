[Skip to main content](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [![jupyter.org](https://jupyterlab.readthedocs.io/en/stable/_static/jupyter_logo.svg)](https://jupyter.org/)
    
*   [GitHub](https://github.com/jupyterlab/jupyterlab)
    
*   [Discourse](https://discourse.jupyter.org/c/jupyterlab/17)
    
*   [Zulip](https://jupyter.zulipchat.com/#narrow/channel/469762-jupyterlab)
    

Common Extension Points[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#common-extension-points "Link to this heading")

=======================================================================================================================================================

Most of the component parts of JupyterLab are designed to be extensible, and they provide services that can be requested in extensions via tokens. A list of common core tokens that extension authors can request is given in [Core Plugins](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#core-tokens)
.

Following the list of core tokens is a guide for using some of JupyterLab’s most commonly-used extension points. However, it is not an exhaustive account of how to extend the application components, and more detailed descriptions of their public APIs may be found in the [JupyterLab API](https://jupyterlab.readthedocs.io/en/stable/developer/api.html)
 and [Lumino](https://lumino.readthedocs.io/)
 API documentation.

[Core Plugins](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#id6)
[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#core-plugins "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The core packages of JupyterLab provide the following plugins. They can be enabled or disabled using the command `jupyter labextension enable <plugin-id>` or `jupyter labextension disable <plugin-id>`.

*   `@jupyterlab/application-extension:commands`: Adds commands related to the shell.
    
*   `@jupyterlab/application-extension:context-menu`: Populates the context menu.
    
*   `@jupyterlab/application-extension:dirty`: Adds safeguard dialog when closing the browser tab with unsaved modifications.
    
*   `@jupyterlab/application-extension:faviconbusy`: Handles the favicon depending on the application status.
    
*   `@jupyterlab/application-extension:info`: Provides the application information.
    
*   `@jupyterlab/application-extension:layout`: Provides the shell layout restorer.
    
*   `@jupyterlab/application-extension:logo`: Sets the application logo.
    
*   `@jupyterlab/application-extension:main`: Initializes the application and provides the URL tree path handler.
    
*   `@jupyterlab/application-extension:mimedocument`: Provides a mime document widget tracker.
    
*   `@jupyterlab/application-extension:move-widget`: Adds commands and context menu items to move widgets between areas.
    
*   `@jupyterlab/application-extension:notfound`: Defines the behavior for not found URL (aka route).
    
*   `@jupyterlab/application-extension:paths`: Provides the application paths.
    
*   `@jupyterlab/application-extension:property-inspector`: Provides the property inspector.
    
*   `@jupyterlab/application-extension:router`: Provides the URL router
    
*   `@jupyterlab/application-extension:shell`: Provides the JupyterLab shell. It has an extended API compared to `app.shell`.
    
*   `@jupyterlab/application-extension:status`: Provides the application status.
    
*   `@jupyterlab/application-extension:top-bar`: Adds a toolbar to the top area (next to the main menu bar).
    
*   `@jupyterlab/application-extension:tree-resolver`: Provides the tree route resolver
    
*   `@jupyterlab/apputils-extension:announcements`: Add the announcement feature. It will fetch news on the internet and check for application updates.
    
*   `@jupyterlab/apputils-extension:kernel-status`: Provides the kernel status indicator model.
    
*   `@jupyterlab/apputils-extension:kernels-settings`: Reserves the name for kernel settings.
    
*   `@jupyterlab/apputils-extension:licenses-client`: The licenses client plugin for fetching licenses.
    
*   `@jupyterlab/apputils-extension:licenses-plugin`: Adds licenses reporting tools.
    
*   `@jupyterlab/apputils-extension:movable-section-registry`: Provides the movable section registry for panels that exchange moveable sections.
    
*   `@jupyterlab/apputils-extension:move-sections`: Enables moving sections between any registered source and target sidebars.
    
*   `@jupyterlab/apputils-extension:notification`: Add the notification center and its status indicator.
    
*   `@jupyterlab/apputils-extension:palette`: Provides the command palette.
    
*   `@jupyterlab/apputils-extension:palette-restorer`: Restores the command palette.
    
*   `@jupyterlab/apputils-extension:print`: Add the print capability
    
*   `@jupyterlab/apputils-extension:resolver`: Provides the window name resolver.
    
*   `@jupyterlab/apputils-extension:running-sessions-status`: Add the running sessions and terminals status bar item.
    
*   `@jupyterlab/apputils-extension:sanitizer`: Provides the HTML sanitizer.
    
*   `@jupyterlab/apputils-extension:sessionDialogs`: Provides the session context dialogs.
    
*   `@jupyterlab/apputils-extension:settings`: Provides the setting registry.
    
*   `@jupyterlab/apputils-extension:settings-connector`: Provides the settings connector.
    
*   `@jupyterlab/apputils-extension:splash`: Provides the splash screen.
    
*   `@jupyterlab/apputils-extension:state`: Provides the application state. It is stored per workspaces.
    
*   `@jupyterlab/apputils-extension:subshell-settings`: Kernel subshell settings.
    
*   `@jupyterlab/apputils-extension:themes`: Provides the theme manager.
    
*   `@jupyterlab/apputils-extension:themes-palette-menu`: Adds theme commands to the menu and the command palette.
    
*   `@jupyterlab/apputils-extension:toggle-header`: Adds a command to display the main area widget content header.
    
*   `@jupyterlab/apputils-extension:toolbar-registry`: Provides toolbar items registry.
    
*   `@jupyterlab/apputils-extension:utilityCommands`: Adds meta commands to run set of other commands.
    
*   `@jupyterlab/apputils-extension:workspaces`: Add workspace file type.
    
*   `@jupyterlab/audio-extension:plugin`: Adds a viewer for audio files
    
*   `@jupyterlab/cell-toolbar-extension:plugin`: Add the cells toolbar.
    
*   `@jupyterlab/celltags-extension:plugin`: Adds the cell tags editor.
    
*   `@jupyterlab/codemirror-extension:binding`: Register the CodeMirror extension factory binding the editor and the shared model.
    
*   `@jupyterlab/codemirror-extension:commands`: Registers commands acting on selected/active CodeMirror editor.
    
*   `@jupyterlab/codemirror-extension:extensions`: Provides the CodeMirror extension factory registry.
    
*   `@jupyterlab/codemirror-extension:languages`: Provides the CodeMirror languages registry.
    
*   `@jupyterlab/codemirror-extension:line-col-status`: Provides the code editor cursor position model.
    
*   `@jupyterlab/codemirror-extension:services`: Provides the service to instantiate CodeMirror editors.
    
*   `@jupyterlab/codemirror-extension:themes`: Provides the CodeMirror theme registry
    
*   `@jupyterlab/completer-extension:base-service`: Adds context and kernel completion providers.
    
*   `@jupyterlab/completer-extension:inline-completer`: Registers the inline completer factory; adds inline completer commands, shortcuts and settings.
    
*   `@jupyterlab/completer-extension:inline-completer-factory`: Provides a factory for inline completer.
    
*   `@jupyterlab/completer-extension:inline-history`: Adds inline completion provider suggesting code from execution history.
    
*   `@jupyterlab/completer-extension:manager`: Provides the completion provider manager.
    
*   `@jupyterlab/console-extension:cell-executor`: Provides the console cell executor.
    
*   `@jupyterlab/console-extension:completer`: Adds completion to the console.
    
*   `@jupyterlab/console-extension:cursor-position`: Adds the console to the code editor cursor position model.
    
*   `@jupyterlab/console-extension:factory`: Provides the console widget content factory.
    
*   `@jupyterlab/console-extension:foreign`: Add foreign handler of IOPub messages to the console.
    
*   `@jupyterlab/console-extension:kernel-status`: Adds the console to the kernel status indicator model.
    
*   `@jupyterlab/console-extension:tracker`: Provides the console widget tracker.
    
*   `@jupyterlab/csvviewer-extension:csv`: Adds viewer for CSV file types
    
*   `@jupyterlab/csvviewer-extension:tsv`: Adds viewer for TSV file types.
    
*   `@jupyterlab/debugger-extension:completions`: Provides debugger-based completions.
    
*   `@jupyterlab/debugger-extension:config`: Provides the debugger configuration
    
*   `@jupyterlab/debugger-extension:consoles`: Add debugger capability to the consoles.
    
*   `@jupyterlab/debugger-extension:debug-console`: Debugger console to enable evaluation in debugger context.
    
*   `@jupyterlab/debugger-extension:display-registry`: Provides the debugger display registry for cell/file display names.
    
*   `@jupyterlab/debugger-extension:files`: Adds debugger capabilities to files.
    
*   `@jupyterlab/debugger-extension:main`: Initialize the debugger user interface.
    
*   `@jupyterlab/debugger-extension:notebooks`: Adds debugger capability to notebooks and provides the debugger notebook handler.
    
*   `@jupyterlab/debugger-extension:service`: Provides the debugger service.
    
*   `@jupyterlab/debugger-extension:sidebar`: Provides the debugger sidebar.
    
*   `@jupyterlab/debugger-extension:source-viewer`: Initialize the debugger sources viewer.
    
*   `@jupyterlab/debugger-extension:sources`: Provides the source feature for debugging
    
*   `@jupyterlab/debugger-extension:variables`: Adds variables renderer and inspection in the debugger variable panel.
    
*   `@jupyterlab/docmanager-extension:contexts`: Adds the handling of opened documents dirty state.
    
*   `@jupyterlab/docmanager-extension:dialogs`: Provides default dialogs for document management operations.
    
*   `@jupyterlab/docmanager-extension:download`: Adds command to download files.
    
*   `@jupyterlab/docmanager-extension:manager`: Provides the document manager.
    
*   `@jupyterlab/docmanager-extension:open-browser-tab`: Adds command to open a browser tab.
    
*   `@jupyterlab/docmanager-extension:opener`: Provides the widget opener.
    
*   `@jupyterlab/docmanager-extension:path-status`: Adds a file path indicator in the status bar.
    
*   `@jupyterlab/docmanager-extension:plugin`: Adds commands and settings to the document manager.
    
*   `@jupyterlab/docmanager-extension:recents`: Provides a manager of recently opened and closed documents.
    
*   `@jupyterlab/docmanager-extension:saving-status`: Adds a saving status indicator.
    
*   `@jupyterlab/documentsearch-extension:labShellWidgetListener`: Active search on valid document
    
*   `@jupyterlab/documentsearch-extension:plugin`: Provides the document search registry.
    
*   `@jupyterlab/extensionmanager-extension:plugin`: Adds the extension manager plugin.
    
*   `@jupyterlab/filebrowser-extension:browser`: Set up the default file browser commands and state restoration
    
*   `@jupyterlab/filebrowser-extension:create-new-language-file`: Adds context menu entries for creating Python/R/Julia files
    
*   `@jupyterlab/filebrowser-extension:default-file-browser`: Provides the default file browser
    
*   `@jupyterlab/filebrowser-extension:download`: Adds the download file commands. Disabling this plugin will NOT disable downloading files from the server, if the user enters the appropriate download URLs.
    
*   `@jupyterlab/filebrowser-extension:factory`: Provides the file browser factory.
    
*   `@jupyterlab/filebrowser-extension:file-upload-status`: Adds a file upload status widget.
    
*   `@jupyterlab/filebrowser-extension:notify-upload`: Adds feature to auto-open supported files after upload
    
*   `@jupyterlab/filebrowser-extension:open-browser-tab`: Adds the open-in-new-browser-tab features.
    
*   `@jupyterlab/filebrowser-extension:open-url`: Adds the feature “Open files from remote URLs”.
    
*   `@jupyterlab/filebrowser-extension:open-with`: Adds the open-with feature allowing an user to pick the non-preferred document viewer.
    
*   `@jupyterlab/filebrowser-extension:settings`: Set up the default file browser settings
    
*   `@jupyterlab/filebrowser-extension:share-file`: Adds the “Copy Shareable Link” command; useful for JupyterHub deployment for example.
    
*   `@jupyterlab/filebrowser-extension:widget`: Adds the file browser to the application shell.
    
*   `@jupyterlab/fileeditor-extension:completer`: Adds the completer capability to the file editor.
    
*   `@jupyterlab/fileeditor-extension:cursor-position`: Adds a file editor cursor position status widget.
    
*   `@jupyterlab/fileeditor-extension:editor-syntax-status`: Adds a file editor syntax status widget.
    
*   `@jupyterlab/fileeditor-extension:language-server`: Adds Language Server capability to the file editor.
    
*   `@jupyterlab/fileeditor-extension:plugin`: Provides the file editor widget tracker.
    
*   `@jupyterlab/fileeditor-extension:search`: Adds search capability to the file editor.
    
*   `@jupyterlab/fileeditor-extension:tab-space-status`: Adds a file editor indentation status widget.
    
*   `@jupyterlab/fileeditor-extension:widget-factory`: Provides the factory for creating file editors.
    
*   `@jupyterlab/help-extension:about`: Adds a “About” dialog feature.
    
*   `@jupyterlab/help-extension:jupyter-forum`: Adds command to open the Jupyter Forum website.
    
*   `@jupyterlab/help-extension:licenses-commands`: Add licenses commands for backwards compatibility.
    
*   `@jupyterlab/help-extension:open`: Add command to open websites as panel or browser tab.
    
*   `@jupyterlab/help-extension:resources`: Adds menu entries to Jupyter reference documentation websites.
    
*   `@jupyterlab/htmlviewer-extension:plugin`: Adds HTML file viewer and provides its tracker.
    
*   `@jupyterlab/hub-extension:connectionlost`: Provides a service to be notified when the connection to the hub server is lost.
    
*   `@jupyterlab/hub-extension:menu`: Adds hub related commands to the menu.
    
*   `@jupyterlab/hub-extension:plugin`: Registers commands related to the hub server
    
*   `@jupyterlab/imageviewer-extension:plugin`: Adds image viewer and provide its tracker.
    
*   `@jupyterlab/inspector-extension:consoles`: Adds code introspection support to consoles.
    
*   `@jupyterlab/inspector-extension:inspector`: Provides the code introspection widget.
    
*   `@jupyterlab/inspector-extension:notebooks`: Adds code introspection to notebooks.
    
*   `@jupyterlab/javascript-extension:factory`: Adds renderer for JavaScript content.
    
*   `@jupyterlab/json-extension:factory`: Adds renderer for JSON content.
    
*   `@jupyterlab/json-lines-extension:factory`: Adds renderer for JSONLines content.
    
*   `@jupyterlab/launcher-extension:plugin`: Provides the launcher tab service.
    
*   `@jupyterlab/logconsole-extension:plugin`: Provides the logger registry.
    
*   `@jupyterlab/lsp-extension:code-extractor-manager`: Provides the code extractor manager.
    
*   `@jupyterlab/lsp-extension:feature`: Provides the language server feature manager.
    
*   `@jupyterlab/lsp-extension:plugin`: Provides the language server connection manager.
    
*   `@jupyterlab/lsp-extension:settings`: Provides the language server settings.
    
*   `@jupyterlab/lsp-extension:tracker`: Provides the tracker of `WidgetLSPAdapter`.
    
*   `@jupyterlab/mainmenu-extension:plugin`: Adds and provides the application main menu.
    
*   `@jupyterlab/mainmenu-extension:recents`: Adds sub-menu for opening recent documents to the File section of the main menu.
    
*   `@jupyterlab/markdownviewer-extension:plugin`: Adds markdown file viewer and provides its tracker.
    
*   `@jupyterlab/markedparser-extension:plugin`: Provides the Markdown parser.
    
*   `@jupyterlab/mathjax-extension:plugin`: Provides the LaTeX mathematical expression interpreter.
    
*   `@jupyterlab/mermaid-extension:context-commands`: Provides context menu commands for mermaid diagrams.
    
*   `@jupyterlab/mermaid-extension:core`: Provides the Mermaid manager.
    
*   `@jupyterlab/mermaid-extension:factory`: Provides a renderer for mermaid text-based diagrams.
    
*   `@jupyterlab/mermaid-extension:markdown`: Provides the Mermaid markdown renderer.
    
*   `@jupyterlab/metadataform-extension:metadataforms`: Provides the metadata form registry.
    
*   `@jupyterlab/notebook-extension:active-cell-tool`: Adds active cell field in the metadata editor tab.
    
*   `@jupyterlab/notebook-extension:cell-counter-status`: Adds a notebook cell counter status widget.
    
*   `@jupyterlab/notebook-extension:cell-executor`: Provides the notebook cell executor.
    
*   `@jupyterlab/notebook-extension:cloned-outputs`: Adds the clone output feature.
    
*   `@jupyterlab/notebook-extension:code-console`: Adds the notebook code consoles features.
    
*   `@jupyterlab/notebook-extension:completer`: Adds the code completion capability to notebooks.
    
*   `@jupyterlab/notebook-extension:copy-output`: Adds the copy cell outputs feature.
    
*   `@jupyterlab/notebook-extension:cursor-position`: Adds the notebook cursor position status.
    
*   `@jupyterlab/notebook-extension:execution-indicator`: Adds a notebook execution status widget.
    
*   `@jupyterlab/notebook-extension:export`: Adds the export notebook commands.
    
*   `@jupyterlab/notebook-extension:factory`: Provides the notebook and cell factory.
    
*   `@jupyterlab/notebook-extension:kernel-status`: Adds the notebook kernel status.
    
*   `@jupyterlab/notebook-extension:language-server`: Adds language server capability to the notebooks.
    
*   `@jupyterlab/notebook-extension:log-output`: Adds cell outputs log to the application logger.
    
*   `@jupyterlab/notebook-extension:metadata-editor`: Adds metadata form for full metadata editor.
    
*   `@jupyterlab/notebook-extension:mode-status`: Adds a notebook mode status widget.
    
*   `@jupyterlab/notebook-extension:open-with-no-kernel`: Adds the “Notebook (no kernel)” option to the Open With menu.
    
*   `@jupyterlab/notebook-extension:search`: Adds search capability to notebooks.
    
*   `@jupyterlab/notebook-extension:toc`: Adds table of content capability to the notebooks
    
*   `@jupyterlab/notebook-extension:tools`: Provides the notebook tools.
    
*   `@jupyterlab/notebook-extension:tracker`: Provides the notebook widget tracker.
    
*   `@jupyterlab/notebook-extension:trust-status`: Adds the notebook trusted status widget.
    
*   `@jupyterlab/notebook-extension:update-raw-mimetype`: Adds metadata form editor for raw cell mimetype.
    
*   `@jupyterlab/notebook-extension:widget-factory`: Provides the notebook widget factory.
    
*   `@jupyterlab/pdf-extension:factory`: Adds renderer for PDF content.
    
*   `@jupyterlab/pluginmanager-extension:plugin`: Enable or disable individual plugins.
    
*   `@jupyterlab/rendermime-extension:plugin`: Provides the render mime registry.
    
*   `@jupyterlab/running-extension:plugin`: Provides the running session managers.
    
*   `@jupyterlab/running-extension:recently-closed`: Adds recently closed documents list.
    
*   `@jupyterlab/running-extension:search-tabs`: Adds a widget to search open and closed tabs.
    
*   `@jupyterlab/running-extension:sidebar`: Provides the running session sidebar.
    
*   `@jupyterlab/services-extension:config-section-manager`: Provides the config section manager.
    
*   `@jupyterlab/services-extension:connection-status`: Provides the default connection status.
    
*   `@jupyterlab/services-extension:contents-manager`: The default contents manager plugin.
    
*   `@jupyterlab/services-extension:default-drive`: The default drive for the contents manager.
    
*   `@jupyterlab/services-extension:event-manager`: The event manager plugin.
    
*   `@jupyterlab/services-extension:kernel-manager`: The kernel manager plugin.
    
*   `@jupyterlab/services-extension:kernel-spec-manager`: The kernel spec manager plugin.
    
*   `@jupyterlab/services-extension:nbconvert-manager`: The nbconvert manager plugin.
    
*   `@jupyterlab/services-extension:server-settings`: The default server settings plugin.
    
*   `@jupyterlab/services-extension:service-manager`: The default service manager plugin.
    
*   `@jupyterlab/services-extension:session-manager`: The session manager plugin.
    
*   `@jupyterlab/services-extension:setting-manager`: The setting manager plugin.
    
*   `@jupyterlab/services-extension:terminal-manager`: The terminal manager plugin.
    
*   `@jupyterlab/services-extension:user-manager`: The user manager plugin.
    
*   `@jupyterlab/services-extension:workspace-manager`: The workspace manager plugin.
    
*   `@jupyterlab/settingeditor-extension:form-ui`: Adds the interactive settings editor and provides its tracker.
    
*   `@jupyterlab/settingeditor-extension:plugin`: Adds the JSON settings editor and provides its tracker.
    
*   `@jupyterlab/shortcuts-extension:shortcuts`: Adds the keyboard shortcuts editor.
    
*   `@jupyterlab/statusbar-extension:plugin`: Provides the application status bar.
    
*   `@jupyterlab/terminal-extension:open-folder-in-terminal`: Adds an “Open in Terminal” command for the file browser.
    
*   `@jupyterlab/terminal-extension:plugin`: Adds terminal and provides its tracker.
    
*   `@jupyterlab/theme-dark-extension:plugin`: Adds a dark theme.
    
*   `@jupyterlab/theme-dark-high-contrast-extension:plugin`: Adds a dark high contrast theme.
    
*   `@jupyterlab/theme-light-extension:plugin`: Adds a light theme.
    
*   `@jupyterlab/toc-extension:registry`: Provides the table of contents registry.
    
*   `@jupyterlab/toc-extension:tracker`: Adds the table of content widget and provides its tracker.
    
*   `@jupyterlab/tooltip-extension:consoles`: Adds the tooltip capability to consoles.
    
*   `@jupyterlab/tooltip-extension:files`: Adds the tooltip capability to file editors.
    
*   `@jupyterlab/tooltip-extension:manager`: Provides the tooltip manager.
    
*   `@jupyterlab/tooltip-extension:notebooks`: Adds the tooltip capability to notebooks.
    
*   `@jupyterlab/translation-extension:plugin`: Adds translation commands and settings.
    
*   `@jupyterlab/translation-extension:translator`: Provides the application translation object.
    
*   `@jupyterlab/translation-extension:translator-connector`: Provides the application translation connector.
    
*   `@jupyterlab/ui-components-extension:form-renderer-registry`: Provides the settings form renderer registry.
    
*   `@jupyterlab/ui-components-extension:labicon-manager`: Provides the icon manager.
    
*   `@jupyterlab/vega5-extension:factory`: Provides a renderer for Vega 5 and Vega-Lite 3 to 5 content.
    
*   `@jupyterlab/video-extension:plugin`: Adds a viewer for video files
    
*   `@jupyterlab/workspaces-extension:commands`: Add workspace commands.
    
*   `@jupyterlab/workspaces-extension:indicator`: Adds a workspace indicator element at topbar
    
*   `@jupyterlab/workspaces-extension:menu`: Populates “File” main menu with Workspaces submenu.
    
*   `@jupyterlab/workspaces-extension:model`: Provides a model for available workspaces.
    
*   `@jupyterlab/workspaces-extension:sidebar`: Populates running sidebar with workspaces.
    

[Core Tokens](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#id7)
[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#id1 "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The core packages of JupyterLab provide many services for plugins. The tokens for these services are listed here, along with short descriptions of when you might want to use the services in your extensions.

*   `@jupyterlab/application:IConnectionLost`: A service for invoking the dialog shown when JupyterLab has lost its connection to the server. Use this if, for some reason, you want to bring up the “connection lost” dialog under new circumstances.
    
*   `@jupyterlab/application:IConnectionStatus`: A service providing the application connection status.
    
*   `@jupyterlab/application:IInfo`: A service providing metadata about the current application, including disabled extensions and whether dev mode is enabled.
    
*   `@jupyterlab/application:ILabShell`: A service for interacting with the JupyterLab shell. The top-level `application` object also has a reference to the shell, but it has a restricted interface in order to be agnostic to different shell implementations on the application. Use this to get more detailed information about currently active widgets and layout state.
    
*   `@jupyterlab/application:ILabStatus`: A service for interacting with the application busy/dirty status. Use this if you want to set the application “busy” favicon, or to set the application “dirty” status, which asks the user for confirmation before leaving the application page.
    
*   `@jupyterlab/application:ILayoutRestorer`: A service providing application layout restoration functionality. Use this to have your activities restored across page loads.
    
*   `@jupyterlab/application:IMimeDocumentTracker`: A widget tracker for documents rendered using a mime renderer extension. Use this if you want to list and interact with documents rendered by such extensions.
    
*   `@jupyterlab/application:IPaths`: A service providing information about various URLs and server paths for the current application. Use this service if you want to assemble URLs to use the JupyterLab REST API.
    
*   `@jupyterlab/application:IRouter`: The URL router used by the application. Use this to add custom URL-routing for your extension (e.g., to invoke a command if the user navigates to a sub-path).
    
*   `@jupyterlab/application:ITreePathUpdater`: A service to update the tree path.
    
*   `@jupyterlab/application:ITreeResolver`: A service to resolve the tree path.
    
*   `@jupyterlab/apputils:ICommandPalette`: A service for the application command palette in the left panel. Use this to add commands to the palette.
    
*   `@jupyterlab/apputils:IKernelStatusModel`: A service to register kernel session provider to the kernel status indicator.
    
*   `@jupyterlab/apputils:ILicensesClient`: A service for fetching licenses.
    
*   `@jupyterlab/apputils:IMovableSectionRegistry`: A registry for panels that can exchange moveable sections.
    
*   `@jupyterlab/apputils:ISanitizer`: A service for sanitizing HTML strings.
    
*   `@jupyterlab/apputils:ISessionContextDialogs`: A service for handling the session dialogs.
    
*   `@jupyterlab/apputils:ISplashScreen`: A service for the splash screen for the application. Use this if you want to show the splash screen for your own purposes.
    
*   `@jupyterlab/apputils:IThemeManager`: A service for the theme manager for the application. This is used primarily in theme extensions to register new themes.
    
*   `@jupyterlab/apputils:IToolbarWidgetRegistry`: A registry for toolbar widgets. Require this if you want to build the toolbar dynamically from a data definition (stored in settings for example).
    
*   `@jupyterlab/apputils:IWindowResolver`: A service for a window resolver for the application. JupyterLab workspaces are given a name, which are determined using the window resolver. Require this if you want to use the name of the current workspace.
    
*   `@jupyterlab/codeeditor:IEditorServices`: A service for the text editor provider for the application. Use this to create new text editors and host them in your UI elements.
    
*   `@jupyterlab/codeeditor:IPositionModel`: A service to handle an code editor cursor position.
    
*   `@jupyterlab/codemirror:IEditorExtensionRegistry`: A registry for CodeMirror extension factories.
    
*   `@jupyterlab/codemirror:IEditorLanguageRegistry`: A registry for CodeMirror languages.
    
*   `@jupyterlab/codemirror:IEditorThemeRegistry`: A registry for CodeMirror theme.
    
*   `@jupyterlab/completer:ICompletionProviderManager`: A service for the completion providers management.
    
*   `@jupyterlab/completer:IInlineCompleterFactory`: A factory of inline completer widgets.
    
*   `@jupyterlab/console:IConsoleCellExecutor`: The console cell executor
    
*   `@jupyterlab/console:IConsoleTracker`: A widget tracker for code consoles. Use this if you want to be able to iterate over and interact with code consoles created by the application.
    
*   `@jupyterlab/console:IContentFactory`: A factory object that creates new code consoles. Use this if you want to create and host code consoles in your own UI elements.
    
*   `@jupyterlab/coreutils:ISettingConnector`: A service to connect to the settings endpoint.
    
*   `@jupyterlab/coreutils:ISettingRegistry`: A service for the JupyterLab settings system. Use this if you want to store settings for your application. See “schemaDir” for more information.
    
*   `@jupyterlab/coreutils:IStateDB`: A service for the JupyterLab state database. Use this if you want to store data that will persist across page loads. See “state database” for more information.
    
*   `@jupyterlab/debugger:IDebugger`: A debugger user interface.
    
*   `@jupyterlab/debugger:IDebuggerConfig`: A service to handle the debugger configuration.
    
*   `@jupyterlab/debugger:IDebuggerDisplayRegistry`: A service for registering display labels for cells/files in the debugger.
    
*   `@jupyterlab/debugger:IDebuggerHandler`: A service for handling notebook debugger.
    
*   `@jupyterlab/debugger:IDebuggerSidebar`: A service for the debugger sidebar.
    
*   `@jupyterlab/debugger:IDebuggerSourceViewer`: A debugger source viewer.
    
*   `@jupyterlab/debugger:IDebuggerSources`: A service to display sources in debug mode.
    
*   `@jupyterlab/docmanager:IDocumentManager`: A service for the manager for all documents used by the application. Use this if you want to open and close documents, create and delete files, and otherwise interact with the file system.
    
*   `@jupyterlab/docmanager:IDocumentManagerDialogs`: A service for displaying dialogs related to document management.
    
*   `@jupyterlab/docmanager:IDocumentWidgetOpener`: A service to open a widget.
    
*   `@jupyterlab/docmanager:IRecentsManager`: A service providing information about recently opened and closed documents
    
*   `@jupyterlab/documentsearch:ISearchProviderRegistry`: A service for a registry of search providers for the application. Plugins can register their UI elements with this registry to provide find/replace support.
    
*   `@jupyterlab/filebrowser:IDefaultFileBrowser`: A service for the default file browser.
    
*   `@jupyterlab/filebrowser:IDefaultFileBrowserRenderer`: A service for overriding the default file browser directory listing renderer.
    
*   `@jupyterlab/filebrowser:IFileBrowserCommands`: A token to ensure file browser commands are loaded.
    
*   `@jupyterlab/filebrowser:IFileBrowserFactory`: A factory object that creates file browsers. Use this if you want to create your own file browser (e.g., for a custom storage backend), or to interact with other file browsers that have been created by extensions.
    
*   `@jupyterlab/fileeditor:IEditorTracker`: A widget tracker for file editors. Use this if you want to be able to iterate over and interact with file editors created by the application.
    
*   `@jupyterlab/fileeditor:IEditorWidgetFactory`: A factory for creating file editors.
    
*   `@jupyterlab/htmlviewer:IHTMLViewerTracker`: A widget tracker for rendered HTML documents. Use this if you want to be able to iterate over and interact with HTML documents viewed by the application.
    
*   `@jupyterlab/imageviewer:IImageTracker`: A widget tracker for images. Use this if you want to be able to iterate over and interact with images viewed by the application.
    
*   `@jupyterlab/inspector:IInspector`: A service for adding contextual help to widgets (visible using “Show Contextual Help” from the Help menu). Use this to hook into the contextual help system in your extension.
    
*   `@jupyterlab/launcher:ILauncher`: A service for the application activity launcher. Use this to add your extension activities to the launcher panel.
    
*   `@jupyterlab/logconsole:ILoggerRegistry`: A service providing a logger infrastructure.
    
*   `@jupyterlab/lsp:ILSPCodeExtractorsManager`: Provides the code extractor manager. This token is required in your extension to register code extractor allowing the creation of multiple virtual document from an opened document.
    
*   `@jupyterlab/lsp:ILSPDocumentConnectionManager`: Provides the virtual documents and language server connections service.
    
*   `@jupyterlab/lsp:ILSPFeatureManager`: Provides the language server feature manager. This token is required to register new client capabilities.
    
*   `@jupyterlab/lsp:IWidgetLSPAdapterTracker`: Provides the WidgetLSPAdapter tracker. This token is required in your extension to track WidgetLSPAdapters.
    
*   `@jupyterlab/mainmenu:IMainMenu`: A service for the main menu bar for the application. Use this if you want to add your own menu items or provide implementations for standardized menu items for specific activities.
    
*   `@jupyterlab/markdownviewer:IMarkdownViewerTracker`: A widget tracker for markdown document viewers. Use this if you want to iterate over and interact with rendered markdown documents.
    
*   `@jupyterlab/mermaid:IMermaidManager`: a manager for rendering mermaid text-based diagrams
    
*   `@jupyterlab/mermaid:IMermaidMarkdown`: a manager for rendering mermaid text-based diagrams in markdown fenced code blocks
    
*   `@jupyterlab/metadataform:IMetadataFormProvider`: A service to register new metadata editor widgets.
    
*   `@jupyterlab/notebook:IContentFactory`: A factory object that creates new notebooks. Use this if you want to create and host notebooks in your own UI elements.
    
*   `@jupyterlab/notebook:INotebookCellExecutor`: The notebook cell executor
    
*   `@jupyterlab/notebook:INotebookTools`: A service for the “Notebook Tools” panel in the right sidebar. Use this to add your own functionality to the panel.
    
*   `@jupyterlab/notebook:INotebookTracker`: A widget tracker for notebooks. Use this if you want to be able to iterate over and interact with notebooks created by the application.
    
*   `@jupyterlab/notebook:INotebookWidgetFactory`: A service to create the notebook viewer.
    
*   `@jupyterlab/pluginmanager:IPluginManager`: A canary for plugin manager presence, with a method to open the plugin manager widget.
    
*   `@jupyterlab/property-inspector:IPropertyInspectorProvider`: A service to register new widgets in the property inspector side panel.
    
*   `@jupyterlab/rendermime:ILatexTypesetter`: A service for the LaTeX typesetter for the application. Use this if you want to typeset math in your extension.
    
*   `@jupyterlab/rendermime:IMarkdownParser`: A service for rendering markdown syntax as HTML content.
    
*   `@jupyterlab/rendermime:IRenderMimeRegistry`: A service for the rendermime registry for the application. Use this to create renderers for various mime-types in your extension. Many times it will be easier to create a “mime renderer extension” rather than using this service directly.
    
*   `@jupyterlab/rendermime:IUrlResolverFactory`: A factory for resolver of asset URLs.
    
*   `@jupyterlab/running:IRunningSessionManagers`: A service to add running session managers.
    
*   `@jupyterlab/running:IRunningSessionsSidebar`: A token allowing to modify the running sessions sidebar.
    
*   `@jupyterlab/services:IConfigSectionManager`: A service providing the config section manager.
    
*   `@jupyterlab/services:IContentsManager`: The contents manager token.
    
*   `@jupyterlab/services:IDefaultDrive`: The default drive for the contents manager.
    
*   `@jupyterlab/services:IEventManager`: The event manager token.
    
*   `@jupyterlab/services:IKernelManager`: The kernel manager token.
    
*   `@jupyterlab/services:IKernelSpecManager`: The kernel spec manager token.
    
*   `@jupyterlab/services:INbConvertManager`: The nbconvert manager token.
    
*   `@jupyterlab/services:IServerSettings`: The server settings for the application.
    
*   `@jupyterlab/services:IServiceManager`: The service manager for the application.
    
*   `@jupyterlab/services:ISessionManager`: The session manager token.
    
*   `@jupyterlab/services:ISettingManager`: The setting manager token.
    
*   `@jupyterlab/services:ITerminalManager`: The terminal manager token.
    
*   `@jupyterlab/services:IUserManager`: The user manager token.
    
*   `@jupyterlab/services:IWorkspaceManager`: The workspace manager token.
    
*   `@jupyterlab/settingeditor:IJSONSettingEditorTracker`: A widget tracker for the JSON setting editor. Use this if you want to be able to iterate over and interact with setting editors created by the application.
    
*   `@jupyterlab/settingeditor:ISettingEditorTracker`: A widget tracker for the interactive setting editor. Use this if you want to be able to iterate over and interact with setting editors created by the application.
    
*   `@jupyterlab/statusbar:IStatusBar`: A service for the status bar on the application. Use this if you want to add new status bar items.
    
*   `@jupyterlab/terminal:ITerminalTracker`: A widget tracker for terminals. Use this if you want to be able to iterate over and interact with terminals created by the application.
    
*   `@jupyterlab/toc:ITableOfContentsRegistry`: A service to register table of content factory.
    
*   `@jupyterlab/toc:ITableOfContentsTracker`: A widget tracker for table of contents.
    
*   `@jupyterlab/tooltip:ITooltipManager`: A service for the tooltip manager for the application. Use this to allow your extension to invoke a tooltip.
    
*   `@jupyterlab/translation:ITranslator`: A service to translate strings.
    
*   `@jupyterlab/translation:ITranslatorConnector`: A service to connect to the server translation endpoint.
    
*   `@jupyterlab/ui-components:IFormRendererRegistry`: A service for settings form renderer registration.
    
*   `@jupyterlab/ui-components:ILabIconManager`: A service to register and request icons.
    
*   `@jupyterlab/workspaces:IWorkspaceCommands`: Provides identifiers of workspace commands.
    
*   `@jupyterlab/workspaces:IWorkspacesModel`: Provides a model for available workspaces.
    

[Commands](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#id8)
[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#commands "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Add a Command to the Command Registry[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#add-a-command-to-the-command-registry "Link to this heading")

Perhaps the most common way to add functionality to JupyterLab is via commands. These are lightweight objects that include a function to execute combined with additional metadata, including how they are labeled and when they are to be enabled. The application has a single command registry, keyed by string command IDs, to which you can add your custom commands.

The commands added to the command registry can then be used to populate several of the JupyterLab user interface elements, including menus and the launcher.

Here is a sample block of code that adds a command to the application (given by `app`):

const commandID \= 'my-command';
let toggled \= false;

app.commands.addCommand(commandID, {
  label: 'My Cool Command',
  isEnabled: () \=> true,
  isVisible: () \=> true,
  isToggled: () \=> toggled,
  iconClass: 'some-css-icon-class',
  describedBy: {
    args: {
      type: 'object',
      properties: {
        text: {
          type: 'string',
          description: 'Optional text to log',
          default: ''
        },
        count: {
          type: 'number',
          description: 'Optional number of times to log the text',
          default: 1
        }
      }
    }
  },
  execute: args \=> {
    const text \= args?.text || '';
    const count \= args?.count || 1;
    for (let i \= 0; i < count; i++) {
      console.log(\`Executed ${commandID} with text: ${text}\`);
    }
  }
});

Copy to clipboard

This example adds a new command, which, when triggered, calls the `execute` function. `isEnabled` indicates whether the command is enabled, and determines whether renderings of it are greyed out. `isToggled` indicates whether to render a check mark next to the command. `isVisible` indicates whether to render the command at all. `iconClass` specifies a CSS class which can be used to display an icon next to renderings of the command. `describedBy` is an optional but recommended property that provides a JSON schema describing the command’s arguments, which is useful for documentation, tooling, and ensuring consistency in how the command is invoked.

Each of `isEnabled`, `isToggled`, and `isVisible` can be either a boolean value or a function that returns a boolean value, in case you want to do some logic in order to determine those conditions.

Likewise, each of `label` and `iconClass` can be either a string value or a function that returns a string value.

There are several more options which can be passed into the command registry when adding new commands. These are documented [here](https://lumino.readthedocs.io/en/latest/api/interfaces/commands.CommandRegistry.ICommandOptions.html)
.

After a command has been added to the application command registry you can add them to various places in the application user interface, where they will be rendered using the metadata you provided.

For example, you can add a button to the Notebook toolbar to run the command with the `CommandToolbarButtonComponent`.

### Add a Command to the Command Palette[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#add-a-command-to-the-command-palette "Link to this heading")

In order to add an existing, registered command to the command palette, you need to request the [`ICommandPalette`](https://jupyterlab.readthedocs.io/en/stable/api/interfaces/apputils.ICommandPalette.html)
 token in your extension. Here is an example showing how to add a command to the command palette (given by `palette`):

palette.addItem({
  command: commandID,
  category: 'my-category',
  args: {}
});

Copy to clipboard

The command ID is the same ID that you used when registering the command. You must also provide a `category`, which determines the subheading of the command palette in which to render the command. It can be a preexisting category (e.g., `'notebook'`), or a new one of your own choosing.

The `args` are a JSON object that will be passed into your command’s functions at render/execute time. You can use these to customize the behavior of your command depending on how it is invoked. For instance, you can pass in `args: { isPalette: true }`. Your command `label` function can then check the `args` it is provided for `isPalette`, and return a different label in that case. This can be useful to make a single command flexible enough to work in multiple contexts.

Note

Try this section in a browser playground:

1.  Click **Load Interactive Example**.
    
2.  In the playground editor toolbar (or command palette), run `Load Current File As Extension`.
    
3.  A notification appears; click **Open Command Palette**, then run `Extension Points Demo Command` from category `Common Extension Points`.
    

Interactive command registry + command palette example.

Load Interactive Example[JupyterLab](https://jupyterlab-plugin-playground.readthedocs.io/en/latest/lite/lab/index.html?hide=all#plugin=1.g.H4sIAAAAAAAAA4VUTW_bMAz9K5wvSgEnw67KUnRoOyA7bAGWW9ODajGpNlnSJDpIEOS_D5L81TTDfLFN8ZHvPdI-FXv0QVlT8E9l8VsZWfBiqzQWZbp9FzUWvFBG4mFGoSiLYBtfpVjtrCc4wbfGHQn9V28NPRpZXgZWutkpA2fYelsDu_uVj7V4-Sic06oSpKxh843ZmL7o8t7WtTByJTQS4b_QDSkdMrSyJhC41Ixf5_B5b5W8hQWcNgZASQ4MD4QmGjB1VhkK0yr3nUqsLc_VWBnTRUP2JwlPHMg3mGIe_zTKY-DwdEH4OWMqUntByGEinHvHqgSXs_ml3htY3GaWAFlYy2v5AIv_sSa722mMrkS4RoIckbCArdABk1_xTDg3a6FhJqRsSUz6ZmVHAkCLF9Qc2GPXG1apNzxgbaFFZqsSa-HiWDmwL1KizOOjVwRlCH0yBkHaKgAeRO00DlAV1pkvh0kyoqXfJ-ABqya5OvYpXoPQD-3jvDs854fzTa--NT8KXxLWk75OK58Ppo9kEe6sP3JgUbI1cOkHe9cnbt1bq1sBE9atMDeW1PbIRn7XGILYIQe2fsXOJFABPAp5nMHaQkBMlrZ1wTo03SSg3aTZ4CsdXSwXmqrCEIa4TZMKfGxk3PZ7bQPyvDLl6Khq05-GGIyx4235cYUSK9_mdi7H77E3pPt0-tV218FSBafFcZ21iapCQ2ycch5enq_tQno7p2HhIf19JG5Fo7t_ybw4_wVLvwTAJgUAAA "Open full JupyterLab view in a new tab")
 [Notebook v7](https://jupyterlab-plugin-playground.readthedocs.io/en/latest/lite/tree/index.html?hide=all#plugin=1.g.H4sIAAAAAAAAA4VUTW_bMAz9K5wvSgEnw67KUnRoOyA7bAGWW9ODajGpNlnSJDpIEOS_D5L81TTDfLFN8ZHvPdI-FXv0QVlT8E9l8VsZWfBiqzQWZbp9FzUWvFBG4mFGoSiLYBtfpVjtrCc4wbfGHQn9V28NPRpZXgZWutkpA2fYelsDu_uVj7V4-Sic06oSpKxh843ZmL7o8t7WtTByJTQS4b_QDSkdMrSyJhC41Ixf5_B5b5W8hQWcNgZASQ4MD4QmGjB1VhkK0yr3nUqsLc_VWBnTRUP2JwlPHMg3mGIe_zTKY-DwdEH4OWMqUntByGEinHvHqgSXs_ml3htY3GaWAFlYy2v5AIv_sSa722mMrkS4RoIckbCArdABk1_xTDg3a6FhJqRsSUz6ZmVHAkCLF9Qc2GPXG1apNzxgbaFFZqsSa-HiWDmwL1KizOOjVwRlCH0yBkHaKgAeRO00DlAV1pkvh0kyoqXfJ-ABqya5OvYpXoPQD-3jvDs854fzTa--NT8KXxLWk75OK58Ppo9kEe6sP3JgUbI1cOkHe9cnbt1bq1sBE9atMDeW1PbIRn7XGILYIQe2fsXOJFABPAp5nMHaQkBMlrZ1wTo03SSg3aTZ4CsdXSwXmqrCEIa4TZMKfGxk3PZ7bQPyvDLl6Khq05-GGIyx4235cYUSK9_mdi7H77E3pPt0-tV218FSBafFcZ21iapCQ2ycch5enq_tQno7p2HhIf19JG5Fo7t_ybw4_wVLvwTAJgUAAA "Open lightweight Notebook v7 view in a new tab")

Extension examples: command-palette.

Load Interactive Example[JupyterLab](https://jupyterlab-plugin-playground.readthedocs.io/en/latest/lite/lab/index.html?path=extension-examples%2Fcommand-palette%2Fsrc%2Findex.ts&hide=all "Open full JupyterLab view in a new tab")
 [Notebook v7](https://jupyterlab-plugin-playground.readthedocs.io/en/latest/lite/tree/index.html?path=extension-examples%2Fcommand-palette%2Fsrc%2Findex.ts&hide=all "Open lightweight Notebook v7 view in a new tab")

[Context Menu](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#id9)
[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#context-menu "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

JupyterLab has an application-wide context menu available as `app.contextMenu`. The application context menu is shown when the user right-clicks, and is populated with menu items that are most relevant to the thing that the user clicked.

The context menu system determines which items to show based on [CSS selectors](https://developer.mozilla.org/en-US/docs/Learn/CSS/Introduction_to_CSS/Selectors)
. It propagates up the DOM tree and tests whether a given HTML element matches the CSS selector provided by a given command.

Items can be added in the context menu in two ways:

1.  Using the settings - this is the preferred way as they are configurable by the user.
    
2.  Using the API - this is for advanced cases like dynamic menu or semantic items.
    

Here is an example showing how to add a command to the application context menu using the settings.

{
  "jupyter.lab.menus": {
    "context": \[\
      {\
        "command": "my-command",\
        "selector": ".jp-Notebook",\
        "rank": 500\
      }\
    \]
  }
}

Copy to clipboard

In this example, the command with id `my-command` is shown whenever the user right-clicks on a DOM element matching `.jp-Notebook` (that is to say, a notebook). The selector can be any valid CSS selector, and may target your own UI elements, or existing ones. A list of CSS selectors currently used by context menu commands is given in [Commonly used CSS selectors](https://jupyterlab.readthedocs.io/en/stable/developer/css.html#css-selectors)
.

Item must follow this definition:

      "context": {
        "title": "The application context menu.",
        "description": "List of context menu items.",
        "items": {
          "allOf": \[\
            {\
              "$ref": "#/definitions/menuItem"\
            },\
            {\
              "properties": {\
                "selector": {\
                  "description": "The CSS selector for the context menu item.",\
                  "type": "string"\
                }\
              }\
            }\
          \]
        },
        "type": "array",
        "default": \[\]
      }

Copy to clipboard

where `menuItem` definition is:

{
  "menuItem": {
    "properties": {
      "args": {
        "description": "Command arguments",
        "type": "object"
      },
      "command": {
        "description": "Command id",
        "type": "string"
      },
      "disabled": {
        "description": "Whether the item is disabled or not",
        "type": "boolean",
        "default": false
      },
      "type": {
        "description": "Item type",
        "type": "string",
        "enum": \[\
          "command",\
          "submenu",\
          "separator"\
        \],
        "default": "command"
      },
      "rank": {
        "description": "Item rank",
        "type": "number",
        "minimum": 0
      },
      "submenu": {
        "oneOf": \[\
          {\
            "$ref": "#/definitions/menu"\
          },\
          {\
            "type": "null"\
          }\
        \]
      }
    },
    "type": "object"
  }
}

Copy to clipboard

The same example using the API is shown below. See the Lumino [docs](https://lumino.readthedocs.io/en/latest/api/interfaces/widgets.ContextMenu.IItemOptions.html)
 for the item creation options.

app.contextMenu.addItem({
  command: commandID,
  selector: '.jp-Notebook'
});

Copy to clipboard

Extension examples: context-menu.

Load Interactive Example[JupyterLab](https://jupyterlab-plugin-playground.readthedocs.io/en/latest/lite/lab/index.html?path=extension-examples%2Fcontext-menu%2Fsrc%2Findex.ts&hide=menu&hide=statusbar "Open full JupyterLab view in a new tab")
 [Notebook v7](https://jupyterlab-plugin-playground.readthedocs.io/en/latest/lite/tree/index.html?path=extension-examples%2Fcontext-menu%2Fsrc%2Findex.ts&hide=menu&hide=statusbar "Open lightweight Notebook v7 view in a new tab")

If you don’t want JupyterLab’s custom context menu to appear for your element, because you have your own right click behavior that you want to trigger, you can add the `data-jp-suppress-context-menu` data attribute to any node to have it and its children not trigger it.

For example, if you are building a custom React element, it would look like this:

function MyElement(props: {}) {
  return (
    <div data\-jp\-suppress\-context\-menu\>
      <p\>Hi</p\>
      <p onContextMenu\={() \=> {console.log("right clicked")}}\>There</p\>
    </div\>
  )
}

Copy to clipboard

Alternatively, you can use a ‘contextmenu’ event listener and call `event.stopPropagation` to prevent the application context menu handler from being called (it is listening in the bubble phase on the `document`). At this point you could show your own Lumino [contextMenu](https://lumino.readthedocs.io/en/latest/api/modules/widgets.ContextMenu.html)
, or simply stop propagation and let the system context menu be shown. This would look something like the following in a `Widget` subclass:

// In \`onAfterAttach()\`
this.node.addEventListener('contextmenu', this);

// In \`handleEvent()\`
case 'contextmenu':
  event.stopPropagation();

Copy to clipboard

[Copy Shareable Link](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#id10)
[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#copy-shareable-link "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The file browser provides a context menu item “Copy Shareable Link”. The desired behavior will vary by deployment and the users it serves. The file browser supports overriding the behavior of this item.

import { IFileBrowserFactory } from '@jupyterlab/filebrowser';

import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

const shareFile: JupyterFrontEndPlugin<void\> \= {
  activate: activateShareFile,
  id: commandID,
  requires: \[IFileBrowserFactory\],
  autoStart: true
};

function activateShareFile(
  app: JupyterFrontEnd,
  factory: IFileBrowserFactory
): void {
  const { commands } \= app;
  const { tracker } \= factory;

  commands.addCommand('filebrowser:share-main', {
    execute: () \=> {
      const widget \= tracker.currentWidget;
      if (!widget) {
        return;
      }
      const path \= encodeURI(widget.selectedItems().next().path);
      // Do something with path.
    },
    isVisible: () \=>
      tracker.currentWidget &&
      Array.from(tracker.currentWidget.selectedItems()).length \=== 1,
    iconClass: 'jp-MaterialIcon jp-LinkIcon',
    label: 'Copy Shareable Link'
  });
}

Copy to clipboard

Note that an extension providing a replacement plugin like this must either [automatically disable](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#disabledextensions)
 the replaced core plugin or the user must disable the core plugin manually:

jupyter labextension disable @jupyterlab/filebrowser-extension:share-file

Copy to clipboard

[Icons](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#id11)
[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#icons "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

See [Reusing JupyterLab UI](https://jupyterlab.readthedocs.io/en/stable/extension/ui_components.html#ui-components)

[Keyboard Shortcuts](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#id12)
[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#keyboard-shortcuts "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

There are two ways of adding keyboard shortcuts in JupyterLab. If you don’t want the shortcuts to be user-configurable, you can add them directly to the application command registry:

app.commands.addKeyBinding({
  command: commandID,
  args: {},
  keys: \['Accel T'\],
  selector: '.jp-Notebook'
});

Copy to clipboard

In this example `my-command` command is mapped to `Accel T`, where `Accel` corresponds to `Cmd` on a Mac and `Ctrl` on Windows and Linux computers.

The behavior for keyboard shortcuts is very similar to that of the context menu: the shortcut handler propagates up the DOM tree from the focused element and tests each element against the registered selectors. If a match is found, then that command is executed with the provided `args`. Full documentation for the options for `addKeyBinding` can be found [here](https://lumino.readthedocs.io/en/latest/api/interfaces/commands.CommandRegistry.IKeyBindingOptions.html)
.

JupyterLab also provides integration with its settings system for keyboard shortcuts. Your extension can provide a settings schema with a `jupyter.lab.shortcuts` key, declaring default keyboard shortcuts for a command:

{
  "jupyter.lab.shortcuts": \[\
    {\
      "command": "my-command",\
      "keys": \["Accel T"\],\
      "selector": ".jp-mod-searchable"\
    }\
  \]
}

Copy to clipboard

Shortcuts added to the settings system will be editable by users.

From JupyterLab version 3.1 onwards, it is possible to execute multiple commands with a single shortcut. This requires you to define a keyboard shortcut for `apputils:run-all-enabled` command:

{
  "command": "apputils:run-all-enabled",
  "keys": \["Accel T"\],
  "args": {
    "commands": \["my-command-1", "my-command-2"\],
    "args": \[{}, {}\]
  },
  "selector": "body"
}

Copy to clipboard

In this example `my-command-1` and `my-command-2` are passed in `args` of `apputils:run-all-enabled` command as `commands` list. You can optionally pass the command arguments of `my-command-1` and `my-command-2` in `args` of `apputils:run-all-enabled` command as `args` list.

[Launcher](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#id13)
[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#launcher "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

As with menus, keyboard shortcuts, and the command palette, new items can be added to the application launcher via commands. You can do this by requesting the [`ILauncher`](https://jupyterlab.readthedocs.io/en/stable/api/interfaces/launcher.ILauncher-1.html)
 token in your extension:

launcher.add({
  command: commandID,
  category: 'Other',
  rank: 0
});

Copy to clipboard

In addition to providing a command ID, you also provide a category in which to put your item, (e.g. ‘Notebook’, or ‘Other’), as well as a rank to determine its position among other items.

Extension examples: launcher.

Load Interactive Example[JupyterLab](https://jupyterlab-plugin-playground.readthedocs.io/en/latest/lite/lab/index.html?path=extension-examples%2Flauncher%2Fsrc%2Findex.ts&hide=all "Open full JupyterLab view in a new tab")
 [Notebook v7](https://jupyterlab-plugin-playground.readthedocs.io/en/latest/lite/tree/index.html?path=extension-examples%2Flauncher%2Fsrc%2Findex.ts&hide=all "Open lightweight Notebook v7 view in a new tab")

[Jupyter Front-End Shell](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#id14)
[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#jupyter-front-end-shell "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The Jupyter front-end shell ([`IShell`](https://jupyterlab.readthedocs.io/en/stable/api/interfaces/application.JupyterFrontEnd.IShell.html)
) is used to add and interact with content in the application. The [`IShell`](https://jupyterlab.readthedocs.io/en/stable/api/interfaces/application.JupyterFrontEnd.IShell.html)
 interface provides an `add()` method for adding widgets to the application. In JupyterLab, the application shell consists of:

*   A `top` area for things like top-level toolbars and information.
    
*   A `menu` area for top-level menus, which is collapsed into the `top` area in multiple-document mode and put below it in single-document mode.
    
*   `left` and `right` sidebar areas for collapsible content.
    
*   A `main` work area for user activity.
    
*   A `down` area for information content; like log console, contextual help.
    
*   A `bottom` area for things like status bars.
    
*   A `header` area for custom elements.
    

### Top Area[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#top-area "Link to this heading")

The top area is intended to host most persistent user interface elements that span the whole session of a user. A toolbar named **TopBar** is available on the right of the main menu bar. For example, JupyterLab adds a user dropdown to that toolbar when started in `collaborative` mode.

See [generic toolbars](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#generic-toolbar)
 to see how to add a toolbar or a custom widget to a toolbar.

You can use a numeric rank to control the ordering of top bar items in the settings; see [Toolbar definitions](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#toolbar-settings-definition)
.

JupyterLab adds a spacer widget to the top bar at rank `50` by default. You can then use the following guidelines to place your items:

*   `rank <= 50` to place items to the left side in the top bar
    
*   `rank > 50` to place items to the right side in the top bar
    

### Left/Right Areas[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#left-right-areas "Link to this heading")

The left and right sidebar areas of JupyterLab are intended to host more persistent user interface elements than the main area. That being said, extension authors are free to add whatever components they like to these areas. The outermost-level of the object that you add is expected to be a Lumino `Widget`, but that can host any content you like (such as React components).

As an example, the following code executes an application command to a terminal widget and then adds the terminal to the right area:

app.commands
  .execute('terminal:create-new')
  .then((terminal: WidgetModuleType.Terminal) \=> {
    app.shell.add(terminal, 'right');
  });

Copy to clipboard

You can use a numeric rank to control the ordering of the left and right tabs:

app.shell.add(terminal, 'left', { rank: 600 });

Copy to clipboard

The recommended ranges for this rank are:

*   0-500: reserved for first-party JupyterLab extensions.
    
*   501-899: reserved for third-party extensions.
    
*   900: The default rank if none is specified.
    
*   1000: The JupyterLab extension manager.
    

#### Movable accordion sections[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#movable-accordion-sections "Link to this heading")

Sidebar panels can participate in the movable-sections system so users can relocate accordion sections between panels via the context menu. There are two roles — **source** (sections can be taken out) and **target** (sections can be dropped in). A panel can serve as both simultaneously.

Take [`IMovableSectionRegistry`](https://jupyterlab.readthedocs.io/en/stable/api/interfaces/apputils.IMovableSectionRegistry.html)
 as an **optional** dependency and register your panel:

import { IMovableSectionRegistry } from '@jupyterlab/apputils';

optional: \[IMovableSectionRegistry\];
activate: (app, registry: IMovableSectionRegistry | null) \=> {
  if (registry) {
    // Expose sections that can be moved out:
    registry.registerSource('@my-org/my-ext:panel', 'My Panel', myPanel);
    // Accept sections dropped in:
    registry.registerTarget('@my-org/my-ext:panel', 'My Panel', myPanel);
  }
};

Copy to clipboard

The label (second argument) appears in the context menu as “Move to My Panel” or “Move back to My Panel”.

**Source panels** must implement [`IMovableSectionSource`](https://jupyterlab.readthedocs.io/en/stable/api/interfaces/apputils.IMovableSectionSource.html)

**Target panels** must implement [`IMovableSectionDestination`](https://jupyterlab.readthedocs.io/en/stable/api/interfaces/apputils.IMovableSectionDestination.html)

[Main Menu](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#id15)
[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#main-menu "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

There are two ways to extend JupyterLab’s main menu.

1.  Using the settings - this is the preferred way as they are configurable by the user.
    
2.  Using the API - this is for advanced cases like dynamic menu or semantic items.
    

### Settings-defined menu[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#settings-defined-menu "Link to this heading")

JupyterLab provides integration with its settings system for menu definitions. Your extension can provide a settings schema with a `jupyter.lab.menus` key, declaring default menus. You don’t need to set anything in the TypeScript code (except the command definitions).

To add a new menu with your extension command:

{
  "jupyter.lab.menus": {
    "main": \[\
      {\
        "id": "jp-mainmenu-myextension",\
        "label": "My Menu",\
        "items": \[\
          {\
            "command": "my-command",\
            "rank": 500\
          }\
        \],\
        "rank": 100\
      }\
    \]
  }
}

Copy to clipboard

The menu item label will be set with the command label. For menus (and submenus), the label needs to be set explicitly with the `label` property.

Menu and item have a `rank` that will determine the elements order.

To add a new entry in an existing menu:

{
  "jupyter.lab.menus": {
    "main": \[\
      {\
        "id": "jp-mainmenu-file",\
        "items": \[\
          {\
            "command": "my-command",\
            "rank": 500\
          }\
        \]\
      }\
    \]
  }
}

Copy to clipboard

Here is the list of default menu ids:

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
    

The default main menu is defined in the `mainmenu-extension` package settings.

A menu must respect the following schema:

      "main": {
        "title": "Main menu entries",
        "description": "List of menu items to add to the main menubar.",
        "items": {
          "$ref": "#/definitions/menu"
        },
        "type": "array",
        "default": \[\]
      },

Copy to clipboard

And an item must follow:

{
  "menu": {
    "properties": {
      "disabled": {
        "description": "Whether the menu is disabled or not",
        "type": "boolean",
        "default": false
      },
      "icon": {
        "description": "Menu icon id",
        "type": "string"
      },
      "id": {
        "description": "Menu unique id",
        "oneOf": \[\
          {\
            "type": "string",\
            "enum": \[\
              "jp-menu-file",\
              "jp-menu-file-new",\
              "jp-menu-edit",\
              "jp-menu-help",\
              "jp-menu-kernel",\
              "jp-menu-run",\
              "jp-menu-settings",\
              "jp-menu-view",\
              "jp-menu-tabs"\
            \]\
          },\
          {\
            "type": "string",\
            "pattern": "\[a-z\]\[a-z0-9\\\\-\_\]+"\
          }\
        \]
      },
      "items": {
        "description": "Menu items",
        "type": "array",
        "items": {
          "$ref": "#/definitions/menuItem"
        }
      },
      "label": {
        "description": "Menu label",
        "type": "string"
      },
      "mnemonic": {
        "description": "Mnemonic index for the label",
        "type": "number",
        "minimum": \-1,
        "default": \-1
      },
      "rank": {
        "description": "Menu rank",
        "type": "number",
        "minimum": 0
      }
    },
    "required": \[\
      "id"\
    \],
    "type": "object"
  }
}

Copy to clipboard

Menus added to the settings system will be editable by users using the `mainmenu-extension` settings. In particular, they can be disabled at the item or the menu level by setting the property `disabled` to `true`.

### API-defined menu[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#api-defined-menu "Link to this heading")

To use the API, you should request the [`IMainMenu`](https://jupyterlab.readthedocs.io/en/stable/api/interfaces/mainmenu.IMainMenu-1.html)
 token for your extension.

There are three main ways to extend:

1.  You can add your own menu to the menu bar.
    
2.  You can add new commands to the existing menus.
    
3.  You can register your extension with one of the existing semantic menu items.
    

#### Adding a New Menu[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#adding-a-new-menu "Link to this heading")

To add a new menu to the menu bar, you need to create a new [Lumino menu](https://lumino.readthedocs.io/en/latest/api/classes/widgets.Menu-1.html)
.

You can then add commands to the menu in a similar way to the command palette, and add that menu to the main menu bar:

const menu \= new Menu({ commands: app.commands });
menu.addItem({
  command: commandID,
  args: {}
});

mainMenu.addMenu(menu, { rank: 40 });

Copy to clipboard

As with the command palette, you can optionally pass in `args` to customize the rendering and execution behavior of the command in the menu context.

#### Adding a New Command to an Existing Menu[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#adding-a-new-command-to-an-existing-menu "Link to this heading")

In many cases you will want to add your commands to the existing JupyterLab menus rather than creating a separate menu for your extension. Because the top-level JupyterLab menus are shared among many extensions, the API for adding items is slightly different. In this case, you provide a list of commands and a rank, and these commands will be displayed together in a separate group within an existing menu.

For instance, to add a command group with `firstCommandID` and `secondCommandID` to the File menu, you would do the following:

mainMenu.fileMenu.addGroup(
  \[\
    {\
      command: firstCommandID\
    },\
    {\
      command: secondCommandID\
    }\
  \],
  40 /\* rank \*/
);

Copy to clipboard

#### Registering a Semantic Menu Item[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#registering-a-semantic-menu-item "Link to this heading")

There are some commands in the JupyterLab menu system that are considered common and important enough that they are treated differently.

For instance, we anticipate that many activities may want to provide a command to close themselves and perform some cleanup operation (like closing a console and shutting down its kernel). Rather than having a proliferation of similar menu items for this common operation of “closing-and-cleanup”, we provide a single command that can adapt itself to this use case, which we term a “semantic menu item”. For this example, it is the File Menu `closeAndCleaners` set.

Here is an example of using the `closeAndCleaners` semantic menu item:

mainMenu.fileMenu.closeAndCleaners.add({
  id: 'notebook:close-and-shutdown',
  isEnabled: (w: Widget) \=> tracker.currentWidget !== null && tracker.has(w)
});

Copy to clipboard

In this example, `tracker` is a [Widget Tracker](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#widget-tracker)
, which allows the menu item to determine whether to delegate the menu command to your activity, and `id` is a the command identifier.

More examples for how to register semantic menu items are found throughout the JupyterLab code base. The available semantic menu items are:

*   [`IUndoer`](https://jupyterlab.readthedocs.io/en/stable/api/interfaces/mainmenu.IEditMenu.IUndoer.html)
    : an activity that knows how to undo and redo.
    
*   [`IClearer`](https://jupyterlab.readthedocs.io/en/stable/api/interfaces/mainmenu.IEditMenu.IClearer.html)
    : an activity that knows how to clear its content.
    
*   `IEditMenu.IGoToLiner`: an activity that knows how to jump to a given line.
    
*   `IFileMenu.ICloseAndCleaner`: an activity that knows how to close and clean up after itself.
    
*   `IFileMenu.IConsoleCreator`: an activity that knows how to create an attached code console for itself.
    
*   [`IKernelUser`](https://jupyterlab.readthedocs.io/en/stable/api/interfaces/mainmenu.IKernelMenu.IKernelUser.html)
    : an activity that can perform various kernel-related operations.
    
*   [`ICodeRunner`](https://jupyterlab.readthedocs.io/en/stable/api/interfaces/mainmenu.IRunMenu.ICodeRunner.html)
    : an activity that can run code from its content.
    
*   [`IEditorViewer`](https://jupyterlab.readthedocs.io/en/stable/api/interfaces/mainmenu.IViewMenu.IEditorViewer.html)
    : an activity that knows how to set various view-related options on a text editor that it owns.
    

[Status Bar](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#id16)
[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#status-bar "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

JupyterLab’s status bar is intended to show small pieces of contextual information. Like the left and right areas, it only expects a Lumino `Widget`, which might contain any kind of content. Since the status bar has limited space, you should endeavor to only add small widgets to it.

The following example shows how to place a status item that displays the current “busy” status for the application. This information is available from the [`ILabStatus`](https://jupyterlab.readthedocs.io/en/stable/api/interfaces/application.ILabStatus.html)
 token, which we reference by a variable named `labStatus`. We place the `statusWidget` in the middle of the status bar. When the `labStatus` busy state changes, we update the text content of the `statusWidget` to reflect that.

const statusWidget \= new Widget();
labStatus.busySignal.connect(() \=> {
  statusWidget.node.textContent \= labStatus.isBusy ? 'Busy' : 'Idle';
});
statusBar.registerStatusItem('lab-status', {
  align: 'middle',
  item: statusWidget
});

Copy to clipboard

[Toolbar Registry](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#id17)
[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#toolbar-registry "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

JupyterLab provides a [`IToolbarWidgetRegistry`](https://jupyterlab.readthedocs.io/en/stable/api/interfaces/apputils.IToolbarWidgetRegistry.html)
 to define and customize toolbar widgets from the settings, which is similar to that defining the context menu and the main menu bar.

### Document Widgets[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#document-widgets "Link to this heading")

A typical example is the notebook toolbar as in the snippet below:

function activatePlugin(
  app: JupyterFrontEnd,
  // ...
  toolbarRegistry: IToolbarWidgetRegistry | null,
  settingRegistry: ISettingRegistry | null
): NotebookWidgetFactory.IFactory {
  const { commands } \= app;
  let toolbarFactory:
    | ((widget: NotebookPanel) \=> DocumentRegistry.IToolbarItem\[\])
    | undefined;

  // Register notebook toolbar specific widgets
  if (toolbarRegistry) {
    toolbarRegistry.addFactory<NotebookPanel\>(FACTORY, 'cellType', panel \=>
      ToolbarItems.createCellTypeItem(panel, translator)
    );

    toolbarRegistry.addFactory<NotebookPanel\>(
      FACTORY,
      'kernelStatus',
      panel \=> Toolbar.createKernelStatusItem(panel.sessionContext, translator)
    );
    // etc...

    if (settingRegistry) {
      // Create the factory
      toolbarFactory \= createToolbarFactory(
        toolbarRegistry,
        settingRegistry,
        // Factory name
        FACTORY,
        // Setting id in which the toolbar items are defined
        '@jupyterlab/notebook-extension:panel',
        translator
      );
    }
  }

  const factory \= new NotebookWidgetFactory({
    name: FACTORY,
    fileTypes: \['notebook'\],
    modelName: 'notebook',
    defaultFor: \['notebook'\],
    // ...
    toolbarFactory,
    translator: translator
  });
  app.docRegistry.addWidgetFactory(factory);

Copy to clipboard

The registry `addFactory` method allows an extension to provide special widget for a unique pair (factory name, toolbar item name). Then the helper `createToolbarFactory` can be used to extract the toolbar definition from the settings and build the factory to pass to the widget factory.

The default toolbar items can be defined across multiple extensions by providing an entry in the `"jupyter.lab.toolbars"` mapping. For example for the notebook panel:

"jupyter.lab.toolbars": {
  "Notebook": \[ // Factory name\
    // Item with non-default widget - it must be registered within an extension\
    {\
      "name": "save", // Unique toolbar item name\
      "rank": 10 // Item rank\
    },\
    // Item with default button widget triggering a command\
    { "name": "insert", "command": "notebook:insert-cell-below", "rank": 20 },\
    { "name": "cut", "command": "notebook:cut-cell", "rank": 21 },\
    { "name": "copy", "command": "notebook:copy-cell", "rank": 22 },\
    { "name": "paste", "command": "notebook:paste-cell-below", "rank": 23 },\
    { "name": "run", "command": "runmenu:run", "rank": 30 },\
    { "name": "interrupt", "command": "kernelmenu:interrupt", "rank": 31 },\
    { "name": "restart", "command": "kernelmenu:restart", "rank": 32 },\
    {\
      "name": "restart-and-run",\
      "command": "notebook:restart-run-all",\
      "rank": 33 // The default rank is 50\
    },\
    { "name": "cellType", "rank": 40 },\
    // Horizontal spacer widget\
    { "name": "spacer", "type": "spacer", "rank": 100 },\
    { "name": "kernelName", "rank": 1000 },\
    { "name": "kernelStatus", "rank": 1001 }\
  \]
},
"jupyter.lab.transform": true,
"properties": {
  "toolbar": {
    "title": "Notebook panel toolbar items",
    "items": {
      "$ref": "#/definitions/toolbarItem"
    },
    "type": "array",
    "default": \[\]
  }
}

Copy to clipboard

The settings registry will merge those definitions from settings schema with any user-provided overrides (customizations) transparently and save them under the `toolbar` property in the final settings object. The `toolbar` list will be used to create the toolbar. Both the source settings schema and the final settings object are identified by the plugin ID passed to `createToolbarFactory`. The user can customize the toolbar by adding new items or overriding existing ones (like providing a different rank or adding `"disabled": true` to remove the item).

Note

You need to set `jupyter.lab.transform` to `true` in the plugin id that will gather all items.

**What are transforms?** The `jupyter.lab.transform` flag tells JupyterLab to wait for a transform function before loading the plugin. This allows dynamic modification of settings schemas, commonly used to merge toolbar/menu definitions from multiple extensions.

**Loading order pitfall**: Extensions providing transforms must register them early in activation, before dependent plugins load, otherwise those plugins will timeout waiting for the transform.

The current widget factories supporting the toolbar customization are:

*   `Notebook`: Notebook panel toolbar
    
*   `Cell`: Cell toolbar
    
*   `Editor`: Text editor toolbar
    
*   `HTML Viewer`: HTML Viewer toolbar
    
*   `CSVTable`: CSV (Comma Separated Value) Viewer toolbar
    
*   `TSVTable`: TSV (Tabulation Separated Value) Viewer toolbar
    

And the toolbar item must follow this definition:

{
  "toolbarItem": {
    "properties": {
      "name": {
        "title": "Unique name",
        "type": "string"
      },
      "args": {
        "title": "Command arguments",
        "type": "object"
      },
      "command": {
        "title": "Command id",
        "type": "string",
        "default": ""
      },
      "disabled": {
        "title": "Whether the item is ignored or not",
        "type": "boolean",
        "default": false
      },
      "icon": {
        "title": "Item icon id",
        "description": "If defined, it will override the command icon",
        "type": "string"
      },
      "label": {
        "title": "Item label",
        "description": "If defined, it will override the command label",
        "type": "string"
      },
      "caption": {
        "title": "Item caption",
        "description": "If defined, it will override the command caption",
        "type": "string"
      },
      "type": {
        "title": "Item type",
        "type": "string",
        "enum": \[\
          "command",\
          "spacer"\
        \]
      },
      "rank": {
        "title": "Item rank",
        "type": "number",
        "minimum": 0,
        "default": 50
      }
    },
    "required": \[\
      "name"\
    \],
    "additionalProperties": false,
    "type": "object"
  }
}

Copy to clipboard

### Generic Widget with Toolbar[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#generic-widget-with-toolbar "Link to this heading")

The logic detailed in the previous section can be used to customize any widgets with a toolbar.

The additional keys used in `jupyter.lab.toolbars` settings attributes are:

*   `Cell`: Cell toolbar
    
*   `FileBrowser`: Default file browser panel toolbar items
    
*   `TopBar`: Top area toolbar (right of the main menu bar)
    

Here is an example for enabling a toolbar on a widget:

function activatePlugin(
  app: JupyterFrontEnd,
  // ...
  toolbarRegistry: IToolbarWidgetRegistry,
  settingRegistry: ISettingRegistry
): void {

  const browser \= new FileBrowser();

  // Toolbar
  // - Define a custom toolbar item
  toolbarRegistry.addFactory(
    'FileBrowser', // Factory name
    'uploader',
    (browser: FileBrowser) \=>
      new Uploader({ model: browser.model, translator })
  );

  // - Link the widget toolbar and its definition from the settings
  setToolbar(
    browser, // This widget is the one passed to the toolbar item factory
    createToolbarFactory(
      toolbarRegistry,
      settings,
      'FileBrowser', // Factory name
      plugin.id,
      translator
    ),
    // You can explicitly pass the toolbar widget if it is not accessible as \`toolbar\` attribute
    // toolbar,
  );

Copy to clipboard

See [Toolbar definitions](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#toolbar-settings-definition)
 example on how to define the toolbar items in the settings.

[Widget Tracker](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#id18)
[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#widget-tracker "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Often extensions will want to interact with documents and activities created by other extensions. For instance, an extension may want to inject some text into a notebook cell, or set a custom keymap, or close all documents of a certain type. Actions like these are typically done by widget trackers. Extensions keep track of instances of their activities in instances of [`WidgetTracker`](https://jupyterlab.readthedocs.io/en/stable/api/classes/apputils.WidgetTracker-1.html)
 class, which are then provided as tokens so that other extensions may request them.

For instance, if you want to interact with notebooks, you should request the [`INotebookTracker`](https://jupyterlab.readthedocs.io/en/stable/api/interfaces/notebook.INotebookTracker.html)
 token. You can then use this tracker to iterate over, filter, and search all open notebooks. You can also use it to be notified via signals when notebooks are added and removed from the tracker.

Widget tracker tokens are provided for many activities in JupyterLab, including notebooks, consoles, text files, mime documents, and terminals. If you are adding your own activities to JupyterLab, you might consider providing a `WidgetTracker` token of your own, so that other extensions can make use of it.

[Completion Providers](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#id19)
[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#completion-providers "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Both code completer and inline completer can be extended by registering an (inline) completion provider on the completion manager provided by the [`ICompletionProviderManager`](https://jupyterlab.readthedocs.io/en/stable/api/interfaces/completer.ICompletionProviderManager.html)
 token.

### Code Completer[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#code-completer "Link to this heading")

A minimal code completion provider needs to implement the `fetch` and `isApplicable` methods, and define a unique `identifier` property, but the [`ICompletionProvider`](https://jupyterlab.readthedocs.io/en/stable/api/interfaces/completer.ICompletionProvider.html)
 interface allows for much more extensive customization of the completer.

import {
  CompletionHandler,
  ICompletionProviderManager,
  ICompletionContext,
  ICompletionProvider
} from '@jupyterlab/completer';

class MyProvider implements ICompletionProvider {
  readonly identifier \= 'my-provider';

  async isApplicable(context: ICompletionContext) {
    return true;
  }

  async fetch(
    request: CompletionHandler.IRequest,
    context: ICompletionContext
  ) {
    return {
      start: request.offset,
      end: request.offset,
      items: \[{ label: 'option 1' }, { label: 'option 2' }\]
    };
  }
}

const plugin: JupyterFrontEndPlugin<void\> \= {
  id: 'my-completer-extension:provider',
  autoStart: true,
  requires: \[ICompletionProviderManager\],
  activate: (
    app: JupyterFrontEnd,
    manager: ICompletionProviderManager
  ): void \=> {
    const provider \= new MyProvider();
    manager.registerProvider(provider);
  }
};

Copy to clipboard

A more detailed example is provided in the [extension-examples](https://github.com/jupyterlab/extension-examples/tree/main/completer)
 repository.

For an example of an extensively customised completion provider, see the [jupyterlab-lsp](https://github.com/jupyter-lsp/jupyterlab-lsp)
 extension.

### Inline Completer[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#inline-completer "Link to this heading")

A minimal inline completion provider extension would only implement the required method `fetch` and define `identifier` and `name` properties, but a number of additional fields can be used for enhanced functionality, such as streaming, see the [`IInlineCompletionProvider`](https://jupyterlab.readthedocs.io/en/stable/api/interfaces/completer.IInlineCompletionProvider.html)
 documentation.

import {
  CompletionHandler,
  ICompletionProviderManager,
  IInlineCompletionContext,
  IInlineCompletionProvider
} from '@jupyterlab/completer';

class MyInlineProvider implements IInlineCompletionProvider {
  readonly identifier \= 'my-provider';
  readonly name \= 'My provider';

  async fetch(
    request: CompletionHandler.IRequest,
    context: IInlineCompletionContext
  ) {
    return {
      items: \[{ insertText: 'suggestion 1' }, { insertText: 'suggestion 2' }\]
    };
  }
}

const plugin: JupyterFrontEndPlugin<void\> \= {
  id: 'my-completer-extension:inline-provider',
  autoStart: true,
  requires: \[ICompletionProviderManager\],
  activate: (
    app: JupyterFrontEnd,
    manager: ICompletionProviderManager
  ): void \=> {
    const provider \= new MyInlineProvider();
    manager.registerInlineProvider(provider);
  }
};

Copy to clipboard

For an example of an inline completion provider with streaming support, see [jupyterlab-transformers-completer](https://github.com/krassowski/jupyterlab-transformers-completer)
.

[State Database](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#id20)
[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#state-database "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The state database can be accessed by importing [`IStateDB`](https://jupyterlab.readthedocs.io/en/stable/api/interfaces/statedb.IStateDB.html)
 from `@jupyterlab/statedb` and adding it to the list of `requires` for a plugin:

const id \= 'foo-extension:IFoo';

const IFoo \= new Token<IFoo\>(id);

interface IFoo {}

class Foo implements IFoo {}

const plugin: JupyterFrontEndPlugin<IFoo\> \= {
  id,
  autoStart: true,
  requires: \[IStateDB\],
  provides: IFoo,
  activate: (app: JupyterFrontEnd, state: IStateDB): IFoo \=> {
    const foo \= new Foo();
    const key \= \`${id}:some-attribute\`;

    // Load the saved plugin state and apply it once the app
    // has finished restoring its former layout.
    Promise.all(\[state.fetch(key), app.restored\]).then((\[saved\]) \=> {
      /\* Update \`foo\` with \`saved\`. \*/
    });

    // Fulfill the plugin contract by returning an \`IFoo\`.
    return foo;
  }
};

Copy to clipboard

[Kernel Subshells](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#id21)
[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#kernel-subshells "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Kernel subshells enable concurrent code execution within kernels that support them. Subshells are separate threads of execution that allow interaction with a kernel while it’s busy executing long-running code, enabling non-blocking communication and parallel execution.

**Kernel Support**

Subshells are supported by:

*   **ipykernel 7.0.0+** (Python kernels) - Kernels advertise support via `supported_features: ['kernel subshells']` in kernel info replies
    
*   Other kernels implementing [JEP 91](https://jupyter.org/enhancement-proposals/kernel-subshells/)
    

**User Interface**

For user interface details, see [Subshell Consoles](https://jupyterlab.readthedocs.io/en/stable/user/documents_kernels.html#subshell-console)
.

**Extension Development**

Extension developers can use subshell functionality through the kernel service API:

import { INotebookTracker } from '@jupyterlab/notebook';

// Get the current kernel from a notebook
const current \= tracker.currentWidget;
if (!current) return;

const kernel \= current.sessionContext.session?.kernel;
if (!kernel) return;

// Check if kernel supports subshells
if (kernel.supportsSubshells) {
  // Create a new subshell
  const reply \= await kernel.requestCreateSubshell({}).done;
  const subshellId \= reply.content.subshell\_id;
  console.log(\`Created subshell: ${subshellId}\`);

  // List existing subshells
  const listReply \= await kernel.requestListSubshell({}).done;
  console.log(\`Active subshells: ${listReply.content.subshell\_id}\`);

  // Execute code in a specific subshell
  const future \= kernel.requestExecute(
    { code: 'print("Hello from subshell!")' },
    false, // disposeOnDone
    { subshell\_id: subshellId } // metadata
  );
  await future.done;

  // Delete a subshell when done
  await kernel.requestDeleteSubshell({ subshell\_id: subshellId }).done;
  console.log(\`Deleted subshell: ${subshellId}\`);
}

Copy to clipboard

For detailed specifications, see [JEP 91](https://jupyter.org/enhancement-proposals/kernel-subshells/)
.

[LSP Features](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#id22)
[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#lsp-features "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

JupyterLab provides an infrastructure to communicate with the language servers. If the LSP services are activated and users have language servers installed, JupyterLab will start the language servers for the language of the opened notebook or file.

Extension authors can access the virtual documents and the associated LSP connection of opened document by requiring the [`ILSPDocumentConnectionManager`](https://jupyterlab.readthedocs.io/en/stable/api/interfaces/lsp.ILSPDocumentConnectionManager.html)
 token from `@jupyterlab/lsp`.

Here is an example for making requests to the language server.

const plugin: JupyterFrontEndPlugin<void\> \= {
  id,
  autoStart: true,
  requires: \[ILSPDocumentConnectionManager\],
  activate: async (app: JupyterFrontEnd, manager: ILSPDocumentConnectionManager): Promise<void\> \=> {

    // Get the path to the opened notebook of file
    const path \= ...

    // Get the widget adapter of opened document
    const adapter \= manager.adapters.get(path);
    if (!adapter) {
      return
    }
    // Get the associated virtual document of the opened document
    const virtualDocument \= adapter.virtualDocument;

    // Get the LSP connection of the virtual document.
    const connection \= manager.connections.get(virtualDocument.uri);
    ...
    // Send completion request to the language server
    const response \= await connection.clientRequests\['textDocument/completion'\].request(params);
    ...
  }
};

Copy to clipboard

Occasionally, LSP extensions include a CodeMirror extension to modify the code editor. In those cases, you can follow this example:

const renamePlugin: JupyterFrontEndPlugin<void\> \= {
  id,
  autoStart: true,
  requires: \[\
    ILSPDocumentConnectionManager,\
    ILSPFeatureManager,\
    IWidgetLSPAdapterTracker\
  \],
  activate: (
    app: JupyterFrontEnd,
    connectionManager: ILSPDocumentConnectionManager,
    featureManager: ILSPFeatureManager,
    tracker: IWidgetLSPAdapterTracker
  ) \=> {
    const FEATURE\_ID \= 'rename\_symbol';
    const extensionFactory: EditorAdapter.ILSPEditorExtensionFactory \= {
      name: FEATURE\_ID,
      factory: options \=> {
        const { editor, widgetAdapter } \= options;

        // Get the editor
        const ceEditor: CodeEditor.IEditor | null \= editor.getEditor();
        if (!ceEditor) {
          return null;
        }

        // Get the associated virtual document of the opened document
        if (!widgetAdapter.virtualDocument) {
          return null;
        }

        // Get the LSP connection of the virtual document.
        const connection \= connectionManager.connections.get(
          widgetAdapter.virtualDocument.uri
        );
        if (!connection || !connection.provides('renameProvider')) {
          return null;
        }

        // Create a CodeMirror extension that listens for double click, gets the
        // selected code and makes a LSP request to rename it and prints the results.
        const ext \= EditorView.domEventHandlers({
          dblclick: (e, view) \=> {
            const range \= ceEditor.getSelection();
            const res \= connection.clientRequests\[\
              'textDocument/rename'\
            \].request({
              newName: 'test',
              position: {
                line: range.start.line,
                character: range.start.column
              },
              textDocument: { uri: widgetAdapter.virtualDocument!.uri }
            });

            res
              .then(value \=> {
                console.debug(value);
              })
              .catch(e \=> console.error);
          }
        });

        // Wrap the CodeMirror extension in the extension registry object.
        return EditorExtensionRegistry.createImmutableExtension(ext);
      }
    };

    // Register the extension with the LSP feature
    featureManager.register({
      id: FEATURE\_ID,
      extensionFactory
    });
  }
};

Copy to clipboard

[Content Provisioning](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#id23)
[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#content-provisioning "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The file system interactions can be customized by adding:

*   a content provider, selectively replacing the way in which content is fetched and synchronized
    
*   a drive, adding a new source of content, analogous to a physical hard drive
    

While both the content provider and drive are meant to provide custom implementations of the Contents API methods such as `get()` and `save()`, and optionally a custom `sharedModelFactory`, the intended use cases, and the way these are exposed in the user interface are different:

*   Drive:
    
    *   Use case: provision of additional content, not available on the default drive.
        
    *   UI: paths of files and directories from the drive are prefixed with the drive name and colon.
        
*   Content Provider:
    
    *   Use case: modification of the protocol used for data retrieval (e.g., streaming of the content, real-time collaboration), by extending the Contents API methods for files which already exist on one of the drives.
        
    *   UI: users will choose a widget factory with an associated content provider when selecting how to open a file using the “Open with” dropdown.
        

To register a custom drive, use the contents manager’s `addDrive` method. The drive needs to follow the [`IDrive`](https://jupyterlab.readthedocs.io/en/stable/api/interfaces/services.Contents.IDrive.html)
 interface. For drives that use a jupyter-server compliant REST API you may wish to extend or re-use the built-in [`Drive`](https://jupyterlab.readthedocs.io/en/stable/api/classes/services.Drive-1.html)
 class, as demonstrated below:

import { Drive, ServerConnection } from '@jupyterlab/services';

const customDrivePlugin: JupyterFrontEndPlugin<void\> \= {
  id: 'my-extension:custom-drive',
  autoStart: true,
  activate: (app: JupyterFrontEnd) \=> {
    const myDrive \= new Drive({
      apiEndpoint: 'api/contents',
      name: 'MyNetworkDrive',
      serverSettings: {
        baseUrl: 'https://your-jupyter-server.com'
        // ...
      } as ServerConnection.ISettings
    });
    app.serviceManager.contents.addDrive(myDrive);
  }
};

Copy to clipboard

To use a content provider, first register it on a drive (or multiple drives):

import {
  Contents,
  ContentsManager,
  RestContentProvider
} from '@jupyterlab/services';

interface IMyContentChunk {
  /\*\* URL allowing to fetch the content chunk \*/
  url: string;
}

interface CustomContentsModel extends Contents.IModel {
  /\*\*
   \* Specializes the content (which in \`Contents.IModel\` is just \`any\`).
   \*/
  content: IMyContentChunk\[\];
}

class CustomContentProvider extends RestContentProvider {
  async get(
    localPath: string,
    options?: Contents.IFetchOptions
  ): Promise<CustomContentsModel\> {
    // Customize the behaviour of the \`get\` action to fetch a list of
    // content chunks from a custom API endpoint instead of the \`get\`

    try {
      return getChunks(); // this method needs to be implemented
    } catch {
      // fall back to the REST API on errors:
      const model \= await super.get(localPath, options);
      return {
        ...model,
        content: \[\]
      };
    }
  }

  // ...
}

const customContentProviderPlugin: JupyterFrontEndPlugin<void\> \= {
  id: 'my-extension:custom-content-provider',
  autoStart: true,
  activate: (app: JupyterFrontEnd) \=> {
    const drive \= (app.serviceManager.contents as ContentsManager).defaultDrive;
    const registry \= drive?.contentProviderRegistry;
    if (!registry) {
      // If content provider is a non-essential feature and support for JupyterLab <4.4 is desired:
      console.error(
        'Cannot initialize content provider: no content provider registry.'
      );
      return;
    }
    const customContentProvider \= new CustomContentProvider({
      // These options are only required if extending the \`RestContentProvider\`.
      apiEndpoint: '/api/contents',
      serverSettings: app.serviceManager.serverSettings
    });
    registry.register('my-custom-provider', customContentProvider);
  }
};

Copy to clipboard

and then create and register a widget factory which will understand how to make use of your custom content provider:

class ExampleWidgetFactory extends ABCWidgetFactory<
  ExampleDocWidget,
  ExampleDocModel
\> {
  protected createNewWidget(
    context: DocumentRegistry.IContext<ExampleDocModel\>
  ): ExampleDocWidget {
    return new ExampleDocWidget({
      context,
      content: new ExamplePanel(context)
    });
  }
}

const widgetFactoryPlugin: JupyterFrontEndPlugin<void\> \= {
  id: 'my-extension:custom-widget-factory',
  autoStart: true,
  activate: (app: JupyterFrontEnd) \=> {
    const widgetFactory \= new ExampleWidgetFactory({
      name: FACTORY,
      modelName: 'example-model',
      fileTypes: \['example'\],
      defaultFor: \['example'\],
      // Instructs the document registry to use the custom provider
      // for context of widgets created with \`ExampleWidgetFactory\`.
      contentProviderId: 'my-custom-provider'
    });
    app.docRegistry.addWidgetFactory(widgetFactory);
  }
};

Copy to clipboard

Where `ExampleDocModel` can now expect the `CustomContentsModel` rather than `Contents.IModel`:

class ExampleDocModel implements DocumentRegistry.IModel {
  // ...

  fromJSON(chunks: IMyContentChunk\[\]): void {
    this.sharedModel.transact(() \=> {
      let i \= 0;
      for (const chunk of chunks) {
        const chunk \= fetch(chunk.url);
        this.sharedModel.set(\`chunk-${i}\`, chunk);
        i += 1;
      }
    });
  }

  fromString(data: string): void {
    const chunks \= JSON.parse(data) as IMyContentChunk\[\];
    return this.fromJSON(chunks);
  }
}

Copy to clipboard

For a complete example of a widget factory (although not using a content provider), see the [documents extension example](https://github.com/jupyterlab/extension-examples/tree/main/documents)
.

On this page

[Edit on GitHub](https://github.com/jupyterlab/jupyterlab/edit/4.6.x/docs/source/extension/extension_points.md)

[Show Source](https://jupyterlab.readthedocs.io/en/stable/_sources/extension/extension_points.md.txt)