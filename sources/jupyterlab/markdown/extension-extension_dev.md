[Skip to main content](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [![jupyter.org](https://jupyterlab.readthedocs.io/en/stable/_static/jupyter_logo.svg)](https://jupyter.org/)
    
*   [GitHub](https://github.com/jupyterlab/jupyterlab)
    
*   [Discourse](https://discourse.jupyter.org/c/jupyterlab/17)
    
*   [Zulip](https://jupyter.zulipchat.com/#narrow/channel/469762-jupyterlab)
    

Develop Extensions[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#develop-extensions "Link to this heading")

==========================================================================================================================================

The JupyterLab application is comprised of a core application object and a set of extensions. JupyterLab extensions provide nearly every function in JupyterLab, including notebooks, document editors and viewers, code consoles, terminals, themes, the file browser, contextual help system, debugger, and settings editor. Extensions even provide more fundamental parts of the application, such as the menu system, status bar, and the underlying communication mechanism with the server.

A JupyterLab extension is a package that contains a number of JupyterLab plugins. We will discuss how to write a plugin, then how to package together a set of plugins into a JupyterLab extension.

See the sections below for more detailed information, or browse the rest of this page for an overview.

*   [Common Extension Points](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html)
    
*   [Reusing JupyterLab UI](https://jupyterlab.readthedocs.io/en/stable/extension/ui_components.html)
    
*   [Using JupyterLab components](https://jupyterlab.readthedocs.io/en/stable/extension/components.html)
    
*   [Documents](https://jupyterlab.readthedocs.io/en/stable/extension/documents.html)
    
*   [Notebook](https://jupyterlab.readthedocs.io/en/stable/extension/notebook.html)
    
*   [React](https://jupyterlab.readthedocs.io/en/stable/extension/virtualdom.html)
    
*   [User Interface Helpers](https://jupyterlab.readthedocs.io/en/stable/extension/ui_helpers.html)
    
*   [Internationalization and Localization](https://jupyterlab.readthedocs.io/en/stable/extension/internationalization.html)
    
*   [Identity](https://jupyterlab.readthedocs.io/en/stable/extension/identity.html)
    
*   [Design Patterns](https://jupyterlab.readthedocs.io/en/stable/developer/patterns.html)
    
*   [CSS Patterns](https://jupyterlab.readthedocs.io/en/stable/developer/css.html)
    
*   [Extension Tutorial](https://jupyterlab.readthedocs.io/en/stable/extension/extension_tutorial.html)
    
*   [Targeting Multiple Applications](https://jupyterlab.readthedocs.io/en/stable/extension/extension_multiple_ui.html)
    
*   [Extension Migration Guide](https://jupyterlab.readthedocs.io/en/stable/extension/extension_migration.html)
    

Other resources[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#other-resources "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------

Before we get started, here are some resources for hands-on practice or more in-depth reference documentation.

### Tutorials[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#tutorials "Link to this heading")

Learn how to write JupyterLab extensions with these guides:

*   [Extension Tutorial](https://jupyterlab.readthedocs.io/en/stable/extension/extension_tutorial.html#extension-tutorial)
    : A tutorial to learn how to make a simple JupyterLab extension.
    
*   [JupyterLab Plugin Playground (JupyterLite)](https://jupyterlab-plugin-playground.readthedocs.io/en/latest/lite/lab/)
    : Prototype and test extension ideas directly in the browser.
    
*   [Making Extensions Compatible with Multiple Applications Tutorial](https://jupyterlab.readthedocs.io/en/stable/extension/extension_multiple_ui.html#multiple-ui-extensions)
     A tutorial for making extensions that work in both JupyterLab, Jupyter Notebook 7+ and more
    
*   The [JupyterLab Extension Examples Repository](https://github.com/jupyterlab/extension-examples)
    : A short tutorial series to learn how to develop extensions for JupyterLab by example.
    
*   [Common Extension Points](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#developer-extension-points)
    : A list of the most common JupyterLab extension points.
    
*   Another common pattern for extending JupyterLab document widgets with application plugins is covered in [Documents](https://jupyterlab.readthedocs.io/en/stable/extension/documents.html#documents)
    .
    

### Extension template[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#extension-template "Link to this heading")

We provide several templates to create JupyterLab extensions:

*   [extension-template](https://github.com/jupyterlab/extension-template)
    : Create a JupyterLab extension using [copier](https://copier.readthedocs.io/)
    
*   \[DEPRECATED\] [extension-cookiecutter-ts](https://github.com/jupyterlab/extension-cookiecutter-ts)
    : Create a JupyterLab extension using [cookiecutter](https://cookiecutter.readthedocs.io/)
     (use the copier template instead).
    

### API Reference Documentation[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#api-reference-documentation "Link to this heading")

Here is some autogenerated API documentation for JupyterLab and Lumino packages:

*   [JupyterLab API Documentation](https://jupyterlab.readthedocs.io/en/stable/developer/api.html)
    
*   [Lumino API Documentation](https://lumino.readthedocs.io/en/latest/api/index.html)
    

Overview of Extensions[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#overview-of-extensions "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------

A JupyterLab plugin is the basic unit of extensibility in JupyterLab. An extension is a package that contains one or more JupyterLab plugins. Extensions can be distributed in two ways:

*   A _prebuilt extension_ (since JupyterLab 3.0) distributes a bundle of JavaScript code prebuilt from a source extension that can be loaded into JupyterLab without rebuilding JupyterLab. In this case, the extension developer uses tools provided by JupyterLab to compile a source extension into a JavaScript bundle that includes the non-JupyterLab JavaScript dependencies, then distributes the resulting bundle in, for example, a Python pip or conda package. Installing a prebuilt extensions does not require Node.js.
    
*   \[DEPRECATED\] A _source extension_ is a JavaScript (npm) package that exports one or more plugins. Installing a source extension requires a user to rebuild JupyterLab. This rebuilding step requires Node.js and may take a lot of time and memory, so some users may not be able to install a source extension. However, the total size of the JupyterLab code delivered to a user’s browser may be reduced compared to using prebuilt extensions. See [Deduplication of Dependencies](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#deduplication)
     for the technical reasons for rebuilding JupyterLab when a source extension is installed.
    

An extension can be published both as a source extension on NPM and as a prebuilt extension (e.g., published as a Python package). In some cases, system administrators may even choose to install a prebuilt extension by directly copying the prebuilt bundle to an appropriate directory, circumventing the need to create a Python package. If a source extension and a prebuilt extension with the same name are installed in JupyterLab, the prebuilt extension takes precedence.

Because prebuilt extensions do not require a JupyterLab rebuild, they have a distinct advantage in multi-user systems where JupyterLab is installed at the system level. On such systems, only the system administrator has permissions to rebuild JupyterLab and install source extensions. Since prebuilt extensions can be installed at the per-user level, the per-environment level, or the system level, each user can have their own separate set of prebuilt extensions that are loaded dynamically in their browser on top of the system-wide JupyterLab.

Warning

Your extensions may break with new releases of JupyterLab. As noted in [Backwards Compatibility, Versions and Breaking Changes](https://jupyterlab.readthedocs.io/en/stable/developer/contributing.html#versioning-notes)
, JupyterLab development and release cycles follow semantic versioning, so we recommend planning your development process to account for possible future breaking changes that may disrupt users of your extensions. Consider documenting your maintenance plans to users in your project, or setting an upper bound on the version of JupyterLab your extension is compatible with in your project’s package metadata.

Tip

We recommend publishing prebuilt extensions in Python packages for user convenience.

Plugins[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#plugins "Link to this heading")

--------------------------------------------------------------------------------------------------------------------

A JupyterLab plugin is the basic unit of extensibility in JupyterLab. JupyterLab supports several types of plugins:

*   **Application plugins:** Application plugins are the fundamental building block of JupyterLab functionality. Application plugins interact with JupyterLab and other plugins by requiring services provided by other plugins, and optionally providing their own service to the system. Application plugins in core JupyterLab include the main menu system, the file browser, and the notebook, console, and file editor components.
    
*   **Mime renderer plugins:** Mime renderer plugins are simplified, restricted ways to extend JupyterLab to render custom mime data in notebooks and files. These plugins are automatically converted to equivalent application plugins by JupyterLab when they are loaded. Examples of mime renderer plugins that come in core JupyterLab are the pdf viewer, the JSON viewer, and the Vega viewer.
    
*   **Theme plugins:** Theme plugins provide a way to customize the appearance of JupyterLab by changing themeable values (i.e., CSS variable values) and providing additional fonts and graphics to JupyterLab. JupyterLab comes with light and dark theme plugins.
    

### Application Plugins[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#application-plugins "Link to this heading")

An application plugin is a JavaScript object with a number of metadata fields. A typical application plugin might look like this in TypeScript:

const plugin: JupyterFrontEndPlugin<MyToken\> \= {
  id: 'my-extension:plugin',
  description: 'Provides a new service.',
  autoStart: true,
  requires: \[ILabShell, ITranslator\],
  optional: \[ICommandPalette\],
  provides: MyToken,
  activate: activateFunction
};

Copy to clipboard

The `id` and `activate` fields are required and the other fields may be omitted. For more information about how to use the `requires`, `optional`, or `provides` fields, see [Plugins Interacting with Each Other](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#services)
.

*   `id` is a required unique string. The convention is to use the NPM extension package name, a colon, then a string identifying the plugin inside the extension, for example `my-extension:plugin`. JupyterLab treats the part before the first colon as the extension name when applying extension-level configuration such as enabling, disabling, deferring, or locking all plugins in that extension. The `jupyter/token-format` rule from [`@jupyter/eslint-plugin`](https://eslint-plugin.readthedocs.io/en/latest/rules/token-format/)
     can enforce the related `<package>:<TokenSymbol>` convention for token IDs used with `new Token(...)`.
    
*   `description` is an optional string. It allows to document the purpose of a plugin.
    
*   `autostart` indicates whether your plugin should be activated at application startup. Typically this should be `true`. If it is `false` or omitted, your plugin will be activated when any other plugin requests the token your plugin is providing.
    
*   `requires` and `optional` are lists of [tokens](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#tokens)
     corresponding to services other plugins provide. These services will be given as arguments to the `activate` function when the plugin is activated. If a `requires` service is not registered with JupyterLab, an error will be thrown and the plugin will not be activated.
    
*   `provides` is the [token](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#tokens)
     associated with the service your plugin is providing to the system. If your plugin does not provide a service to the system, omit this field and do not return a value from your `activate` function.
    
*   `activate` is the function called when your plugin is activated. The arguments are, in order, the [application object](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#application-object)
    , the services corresponding to the `requires` tokens, then the services corresponding to the `optional` tokens (or `null` if that particular `optional` token is not registered in the system). If a `provides` token is given, the return value of the `activate` function (or resolved return value if a promise is returned) will be registered as the service associated with the token.
    
*   `deactivate` is the optional deactivation method
    

For more information, see the API reference for [`JupyterFrontEndPlugin`](https://jupyterlab.readthedocs.io/en/stable/api/types/application.JupyterFrontEndPlugin.html)
.

#### Application Object[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#application-object "Link to this heading")

A Jupyter front-end application object is given to a plugin’s `activate` function as its first argument. The application object has a number of properties and methods for interacting with the application, including:

*   `commands` - an extensible registry used to add and execute commands in the application.
    
*   `docRegistry` - an extensible registry containing the document types that the application is able to read and render.
    
*   `restored` - a promise that is resolved when the application has finished loading.
    
*   `serviceManager` - low-level manager for talking to the Jupyter REST API.
    
*   `shell` - a generic Jupyter front-end shell instance, which holds the user interface for the application. See [Jupyter Front-End Shell](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#shell)
     for more details.
    

See the JupyterLab API reference documentation for the [`JupyterFrontEnd`](https://jupyterlab.readthedocs.io/en/stable/api/classes/application.JupyterFrontEnd-1.html)
 class for more details.

### Plugins Interacting with Each Other[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#plugins-interacting-with-each-other "Link to this heading")

_(The Provider-Consumer pattern is explained here)_

One of the foundational features of the JupyterLab plugin system is that application plugins can interact with other plugins by providing a service to the system and requiring services provided by other plugins. A service can be any JavaScript value, and typically is a JavaScript object with methods and data attributes. For example, the core plugin that supplies the JupyterLab main menu provides a [Main Menu](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#mainmenu)
 service object to the system with a method to add a new top-level menu and attributes to interact with existing top-level application menus.

In the following discussion, the plugin that is providing a service to the system is the _provider_ plugin, and the plugin that is requiring and using the service is the _consumer_ plugin. Note that these kinds of _provider_ and _consumer_ plugins are fundamental parts of JupyterLab’s Provider-Consumer pattern (which is a type of [dependency-injection](https://en.wikipedia.org/wiki/Dependency_injection)
 pattern).

#### Tokens[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#tokens "Link to this heading")

A service provided by a plugin is identified by a _token_, i.e., a concrete instance of the Lumino Token class. The provider plugin lists the token in its plugin metadata `provides` field, and returns the associated service from its `activate` function.

Consumer plugins import the token (for example, from the provider plugin’s extension JavaScript package, or from a third package exporting the token for both the provider and consumer) and list the token in their plugin metadata `requires` or `optional` fields. When JupyterLab instantiates the consumer plugin by calling its `activate` function, it will pass in the service associated with the token as an argument. If the service is not available (i.e., the token has not been registered with JupyterLab), then JupyterLab will either throw an error and not activate the consumer (if the token was listed in `requires`), or will set the corresponding `activate` argument to `null` (if the token was listed in `optional`). JupyterLab orders plugin activation to ensure that a provider of a service is activated before its consumers. A token can only be registered with the system once.

A consumer might list a token as `optional` when the service it identifies is not critical to the consumer, but would be nice to have if the service is available. For example, a consumer might list the status bar service as optional so that it can add an indicator to the status bar if it is available, but still make it possible for users running a customized JupyterLab distribution without a status bar to use the consumer plugin.

A token defined in TypeScript can also define a TypeScript interface for the service associated with the token. If a package using the token uses TypeScript, the service will be type-checked against this interface when the package is compiled to JavaScript.

Note

JupyterLab uses tokens to identify services (instead of strings, for example) to prevent conflicts between identifiers and to enable type checking when using TypeScript.

#### Publishing Tokens[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#publishing-tokens "Link to this heading")

Since consumers will need to import a token used by a provider, the token should be exported in a published JavaScript package. Tokens will need to be deduplicated in JupyterLab—see [Deduplication of Dependencies](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#deduplication)
 for more details.

A pattern in core JupyterLab is to create and export a token from a third package that both the provider and consumer extensions import, rather than defining the token in the provider’s package. This enables a user to swap out the provider extension for a different extension that provides the same token with an alternative service implementation. For example, the core JupyterLab `filebrowser` package exports a token representing the file browser service (enabling interactions with the file browser). The `filebrowser-extension` package contains a plugin that implements the file browser in JupyterLab and provides the file browser service to JupyterLab (identified with the token imported from the `filebrowser` package). Extensions in JupyterLab that want to interact with the filebrowser thus do not need to have a JavaScript dependency on the `filebrowser-extension` package, but only need to import the token from the `filebrowser` package. This pattern enables users to seamlessly change the file browser in JupyterLab by writing their own extension that imports the same token from the `filebrowser` package and provides it to the system with their own alternative file browser service.

### MIME Renderer Plugins[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#mime-renderer-plugins "Link to this heading")

MIME Renderer plugins are a convenience for creating a plugin that can render mime data in a notebook and files of the given mime type. MIME renderer plugins are more declarative and more restricted than standard plugins. A mime renderer plugin is an object with the fields listed in the [`IExtension`](https://jupyterlab.readthedocs.io/en/stable/api/interfaces/rendermime_interfaces.IRenderMime.IExtension.html)
 object.

JupyterLab has a [pdf mime renderer extension](https://github.com/jupyterlab/jupyterlab/tree/4.6.x/packages/pdf-extension)
, for example. In core JupyterLab, this is used to view pdf files and view pdf data mime data in a notebook.

We have a [MIME renderer example](https://github.com/jupyterlab/extension-examples/tree/master/mimerenderer)
 walking through creating a mime renderer extension which adds mp4 video rendering to JupyterLab. The [extension template](https://github.com/jupyterlab/extension-template)
 supports MIME renderer extensions.

The mime renderer can update its data by calling `.setData()` on the model it is given to render. This can be used for example to add a `png` representation of a dynamic figure, which will be picked up by a notebook model and added to the notebook document. When using [`IDocumentWidgetFactoryOptions`](https://jupyterlab.readthedocs.io/en/stable/api/interfaces/rendermime.IRenderMime.IDocumentWidgetFactoryOptions.html)
, you can update the document model by calling `.setData()` with updated data for the rendered MIME type. The document can then be saved by the user in the usual manner.

### Theme plugins[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#theme-plugins "Link to this heading")

A theme is a special application plugin that registers a theme with the `ThemeManager` service. Theme CSS assets are specially bundled in an extension (see [Theme path](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#themepath)
) so they can be unloaded or loaded as the theme is activated. Since CSS files referenced by the `style` or `styleModule` keys are automatically bundled and loaded on the page, the theme files should not be referenced by these keys.

The extension package containing the theme plugin must include all static assets that are referenced by `@import` in its theme CSS files. Local URLs can be used to reference files relative to the location of the referring sibling CSS files. For example `url('images/foo.png')` or `url('../foo/bar.css')` can be used to refer local files in the theme. Absolute URLs (starting with a `/`) or external URLs (e.g. `https:`) can be used to refer to external assets.

See the [JupyterLab Light Theme](https://github.com/jupyterlab/jupyterlab/tree/4.6.x/packages/theme-light-extension)
 for an example.

See the [TypeScript extension template](https://github.com/jupyterlab/extension-template)
 (choosing `theme` as `kind` ) for a quick start to developing a theme plugin.

### Service Manager Plugins[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#service-manager-plugins "Link to this heading")

Warning

This is an advanced topic. If you are new to JupyterLab extensions, you can skip this section.

The Service Manager is a core component of a JupyterLab application and the interface to the Jupyter Server REST API. Before JupyterLab 4.4.0, the Service Manager had to be created as a singleton object and passed when creating a JupyterLab application object. This was not convenient if some extensions needed to change the behavior of some of the core services provided by the Service Manager, as they would have to build a new JupyterLab application from scratch.

Added in version 4.4: The Service Manager is now itself a plugin which can be provided by a third-party extension using the :ts:variable:`services.IServiceManager` token. Its underlying services (such as the kernel manager and the contents manager) are also now available as plugins.

The Service Manager plugins can be provided by third-party extensions via the following tokens:

*   [`IConnectionStatus`](https://jupyterlab.readthedocs.io/en/stable/api/variables/services.IConnectionStatus-1.html)
    : The connection status service.
    
*   [`IContentsManager`](https://jupyterlab.readthedocs.io/en/stable/api/variables/services.IContentsManager.html)
    : The contents manager service, responsible for managing files and directories.
    
*   [`IDefaultDrive`](https://jupyterlab.readthedocs.io/en/stable/api/variables/services.IDefaultDrive.html)
    : The default drive service, responsible for providing the default drive in which the contents manager operates.
    
*   [`IServerSettings`](https://jupyterlab.readthedocs.io/en/stable/api/variables/services.IServerSettings.html)
    : The server settings service, defining a set of default server settings.
    
*   [`IEventManager`](https://jupyterlab.readthedocs.io/en/stable/api/variables/services.IEventManager.html)
    : The event manager service for emitting events that are broadcast by an event bus managed by Jupyter Server.
    
*   [`IKernelManager`](https://jupyterlab.readthedocs.io/en/stable/api/variables/services.IKernelManager.html)
    : The kernel manager service.
    
*   [`IKernelSpecManager`](https://jupyterlab.readthedocs.io/en/stable/api/variables/services.IKernelSpecManager.html)
    : The kernel spec manager service.
    
*   [`INbConvertManager`](https://jupyterlab.readthedocs.io/en/stable/api/variables/services.INbConvertManager.html)
    : The nbconvert manager service, used for exports in various formats.
    
*   [`ISessionManager`](https://jupyterlab.readthedocs.io/en/stable/api/variables/services.ISessionManager.html)
    : The session manager service.
    
*   [`ISettingManager`](https://jupyterlab.readthedocs.io/en/stable/api/variables/services.ISettingManager.html)
    : The setting manager service, for managing user settings.
    
*   [`ITerminalManager`](https://jupyterlab.readthedocs.io/en/stable/api/variables/services.ITerminalManager.html)
    : The terminal manager service.
    
*   [`IUserManager`](https://jupyterlab.readthedocs.io/en/stable/api/variables/services.IUserManager.html)
    : The user manager service.
    
*   [`IWorkspaceManager`](https://jupyterlab.readthedocs.io/en/stable/api/variables/services.IWorkspaceManager.html)
    : The workspace manager service, to interact with the workspace API.
    

The following example shows how you can provide a custom contents manager service, which logs the path of the requested content in the console:

import {
  Contents,
  ContentsManager,
  IContentsManager,
  ServiceManagerPlugin
} from '@jupyterlab/services';

class CustomContents extends ContentsManager {
  async get(
    path: string,
    options?: Contents.IFetchOptions
  ): Promise<Contents.IModel\> {
    console.log('CustomContents.get', path);
    return super.get(path, options);
  }
}

const plugin: ServiceManagerPlugin<IContentsManager\> \= {
  id: 'my-extension:contents-manager',
  autoStart: true,
  provides: IContentsManager,
  description: 'A JupyterLab extension providing a custom contents manager',
  activate: (\_: null): Contents.IManager \=> {
    return new CustomContents();
  }
};

export default plugin;

Copy to clipboard

Warning

Note the use of [`ServiceManagerPlugin`](https://jupyterlab.readthedocs.io/en/stable/api/types/services.ServiceManagerPlugin.html)
 to declare the plugin. `ServiceManagerPlugin` is different from [`JupyterFrontEndPlugin`](https://jupyterlab.readthedocs.io/en/stable/api/types/application.JupyterFrontEndPlugin.html)
 in that it provides a service manager plugin, which will be activated before the application is set. As a consequence, the first parameter of the `activate` function is `null`. `ServiceManagerPlugin<T>` is equivalent to `IPlugin<null, T>` where `T` is the service provided by the plugin.

Source Extensions[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#source-extensions "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

A source extension is a JavaScript (npm) package that exports one or more plugins. All JupyterLab extensions are developed as source extensions (for example, prebuilt extensions are built from source extensions).

A source extension has metadata in the `jupyterlab` field of its `package.json` file. The [JSON schema](https://github.com/jupyterlab/jupyter-builder/blob/main/src/metadata_schema.json)
 for the metadata is distributed in the `@jupyter/builder` package.

We will talk about each `jupyterlab` metadata field in `package.json` for source extensions below.

*   `extension`: [Application Plugins](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#main-entry-point)
    
*   `mimeExtension`: [MIME Renderer Plugins](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#mimeextension)
    
*   `themePath`: [Theme path](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#themepath)
    
*   `schemaDir`: [Plugin Settings](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#schemadir)
    
*   `disabledExtensions`: [Disabling other extensions](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#disabledextensions)
    
*   `sharedPackages`: [Deduplication of Dependencies](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#deduplication)
    
*   `discovery`: [Companion packages](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#ext-author-companion-packages)
    

A JupyterLab extension must have at least one of `jupyterlab.extension` or `jupyterlab.mimeExtension` set.

### Application Plugins[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#main-entry-point "Link to this heading")

The `jupyterlab.extension` field signifies that the package exports one or more JupyterLab application plugins. Set the value to `true` if the default export of the main package module (i.e., the file listed in the `main` key of `package.json`) is an application plugin or a list of application plugins. If your plugins are exported as default exports from a different module, set this to the relative path to the module (e.g., `"lib/foo"`). Example:

"jupyterlab": {
  "extension": true
}

Copy to clipboard

### MIME Renderer Plugins[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#mimeextension "Link to this heading")

The `jupyterlab.mimeExtension` field signifies that the package exports mime renderer plugins. Like the `jupyterlab.extension` field, the value can be a boolean (indicating a mime renderer plugin or list of mime renderer plugins is the default export from the `main` field), or a string, which is the relative path to the module exporting (as the default export) one or more mime renderer plugins.

### Theme path[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#theme-path "Link to this heading")

Theme plugin assets (e.g., CSS files) need to bundled separately from a typical application plugin’s assets so they can be loaded and unloaded as the theme is activated or deactivated. If an extension exports a theme plugin, it should give the relative path to the theme assets in the `jupyterlab.themePath` field:

"jupyterlab": {
  "extension": true,
  "themePath": "style/theme.css"
}

Copy to clipboard

An extension cannot bundle multiple theme plugins.

Ensure that the theme path files are included in the `files` metadata in `package.json`. If you want to use SCSS, SASS, or LESS files, you must compile them to CSS and point `jupyterlab.themePath` to the CSS files.

### Plugin Settings[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#plugin-settings "Link to this heading")

JupyterLab exposes a plugin settings system that can be used to provide default setting values and user overrides. A plugin’s settings are specified with a JSON schema file. The `jupyterlab.schemaDir` field in `package.json` gives the relative location of the directory containing plugin settings schema files.

The setting system relies on plugin ids following the convention `<source_package_name>:<plugin_name>`. The settings schema file for the plugin `plugin_name` is `<schemaDir>/<plugin_name>.json`.

For example, the JupyterLab `filebrowser-extension` package exports the `@jupyterlab/filebrowser-extension:browser` plugin. In the `package.json` for `@jupyterlab/filebrowser-extension`, we have:

"jupyterlab": {
  "schemaDir": "schema",
}

Copy to clipboard

The file browser setting schema file (which specifies some default keyboard shortcuts and other settings for the filebrowser) is located in `schema/browser.json` (see [here](https://github.com/jupyterlab/jupyterlab/blob/4.6.x/packages/filebrowser-extension/schema/browser.json)
).

See the [fileeditor-extension](https://github.com/jupyterlab/jupyterlab/tree/4.6.x/packages/fileeditor-extension)
 for another example of an extension that uses settings.

Please ensure that the schema files are included in the `files` metadata in `package.json`.

When declaring dependencies on JupyterLab packages, use the `^` operator before a package version so that the build system installs the newest patch or minor version for a given major version. For example, `^4.0.0` will install version 4.0.0, 4.0.1, 4.1.0, etc.

A system administrator or user can override default values provided in a plugin’s settings schema file with the [overrides.json](https://jupyterlab.readthedocs.io/en/stable/user/directories.html#overridesjson)
 file.

### Disabling other extensions[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#disabling-other-extensions "Link to this heading")

The `jupyterlab.disabledExtensions` field gives a list of extensions or plugins to disable when this extension is installed, with the same semantics as the `disabledExtensions` field of [page\_config.json](https://jupyterlab.readthedocs.io/en/stable/user/directories.html#page-configjson)
. This is useful if your extension overrides built-in extensions. For example, if an extension replaces the `@jupyterlab/filebrowser-extension:share-file` plugin to [override the “Copy Shareable Link”](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#copy-shareable-link)
 functionality in the file browser, it can automatically disable the `@jupyterlab/filebrowser-extension:share-file` plugin with:

"jupyterlab": {
  "disabledExtensions": \["@jupyterlab/filebrowser-extension:share-file"\]
}

Copy to clipboard

To disable all plugins in an extension, give the extension package name, e.g., `"@jupyterlab/filebrowser-extension"` in the above example.

### Deduplication of Dependencies[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#deduplication-of-dependencies "Link to this heading")

The `jupyterlab.sharedPackages` field controls how dependencies are bundled, shared, and deduplicated with prebuilt extensions.

One important concern and challenge in the JupyterLab extension system is deduplicating dependencies of extensions instead of having extensions use their own bundled copies of dependencies. For example, the Lumino widgets system on which JupyterLab relies for communication across the application requires all packages use the same copy of the `@lumino/widgets` package. [Tokens](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#tokens)
 identifying plugin services also need to be shared across the providers and consumers of the services, so dependencies that export tokens need to be deduplicated.

JupyterLab automatically deduplicates the entire dependency tree between source extensions when it rebuilds itself during a source extension installation. Deduplication between source and prebuilt extensions, or between prebuilt extensions themselves, is a more nuanced problem (for those curious about implementation details, this deduplication in JupyterLab is powered by the Rspack [module federation system](https://module-federation.io/)
). JupyterLab comes with a reasonable default strategy for deduplicating dependencies for prebuilt extensions. The `jupyterlab.sharedPackages` object in an extension’s `package.json` enables an extension author to modify the default deduplication strategy for a given dependency with three boolean options. The keys of this object are dependency package names, and the values are either `false` (signifying that dependency should not be shared/deduplicated), or objects with up to three fields:

*   `bundled`: if `true` (default), the dependency is bundled with the extension and is made available as one of the copies available to JupyterLab. If `false`, the dependency is not bundled with the extension, so the extension will use a version of the dependency from a different extension.
    
*   `singleton`: if `true`, the extension will always prefer to use the copy of the dependency that other extensions are using, rather than using the highest version available. The default is `false`.
    
*   `strictVersion`: if `true`, the extension will always make sure the copy of the dependency it is using satisfies the dependency version range it requires.
    

By default, JupyterLab deduplicates direct dependencies of prebuilt extensions with direct dependencies of other source and prebuilt extensions, choosing the highest version of a dependency available to JupyterLab. JupyterLab chooses reasonable default options when using tokens and services from core JupyterLab packages. We suggest the following `sharedPackages` configurations when using tokens provided by packages other than core JupyterLab packages (see [Plugins Interacting with Each Other](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#services)
 for more details about using tokens).

#### Providing a service[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#providing-a-service "Link to this heading")

When an extension (the “provider”) is providing a service identified by a token that is imported from a dependency `token-package`, the provider should configure the dependency as a singleton. This makes sure the provider is identifying the service with the same token that others are importing. If `token-package` is not a core package, it will be bundled with the provider and available for consumers to import if they [require the service](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#dedup-require-service)
.

"jupyterlab": {
  "sharedPackages": {
    "token-package": {
      "singleton": true
     }
   }
 }

Copy to clipboard

#### Requiring a service[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#requiring-a-service "Link to this heading")

When an extension (the “consumer”) is requiring a service provided by another extension (the “provider”), identified by a token imported from a package (the `token-package`, which may be the same as the provider), the consumer should configure the dependency `token-package` to be a singleton to ensure the consumer is getting the exact same token the provider is using to identify the service. Also, since the provider is providing a copy of `token-package`, the consumer can exclude it from its bundle.

"jupyterlab": {
  "sharedPackages": {
    "token-package": {
      "bundled": false,
      "singleton": true
     }
   }
 }

Copy to clipboard

#### Optionally using a service[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#optionally-using-a-service "Link to this heading")

When an extension (the “consumer”) is optionally using a service identified by a token imported from a package (the `token-package`), there is no guarantee that a provider is going to be available and bundling `token-package`. In this case, the consumer should only configure `token-package` to be a singleton:

"jupyterlab": {
  "sharedPackages": {
    "token-package": {
      "singleton": true
     }
   }
 }

Copy to clipboard

### Companion packages[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#companion-packages "Link to this heading")

If your extension depends on the presence of one or more packages in the kernel, or on a notebook server extension, you can add metadata to indicate this to the extension manager by adding metadata to your package.json file. The full options available are:

"jupyterlab": {
  "discovery": {
    "kernel": \[\
      {\
        "kernel\_spec": {\
          "language": "<regexp for matching kernel language>",\
          "display\_name": "<regexp for matching kernel display name>"   // optional\
        },\
        "base": {\
          "name": "<the name of the kernel package>"\
        },\
        "overrides": {   // optional\
          "<manager name, e.g. 'pip'>": {\
            "name": "<name of kernel package on pip, if it differs from base name>"\
          }\
        },\
        "managers": \[   // list of package managers that have your kernel package\
            "pip",\
            "conda"\
        \]\
      }\
    \],
    "server": {
      "base": {
        "name": "<the name of the server extension package>"
      },
      "overrides": {   // optional
        "<manager name, e.g. 'pip'>": {
          "name": "<name of server extension package on pip, if it differs from base name>"
        }
      },
      "managers": \[   // list of package managers that have your server extension package\
          "pip",\
          "conda"\
      \]
    }
  }
}

Copy to clipboard

A typical setup for e.g. a jupyter-widget based package will then be:

"keywords": \[\
    "jupyterlab-extension",\
    "jupyter",\
    "widgets",\
    "jupyterlab"\
\],
"jupyterlab": {
  "extension": true,
  "discovery": {
    "kernel": \[\
      {\
        "kernel\_spec": {\
          "language": "^python",\
        },\
        "base": {\
          "name": "myipywidgetspackage"\
        },\
        "managers": \[\
            "pip",\
            "conda"\
        \]\
      }\
    \]
  }
}

Copy to clipboard

Currently supported package managers are `pip` and `conda`.

### Extension CSS[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#extension-css "Link to this heading")

If your extension has a top-level `style` key in `package.json`, the CSS file it points to will be included on the page automatically.

A convention in JupyterLab for deduplicating CSS on the page is that if your extension has a top-level `styleModule` key in `package.json` giving a JavaScript module that can be imported, it will be imported (as a JavaScript module) instead of importing the `style` key CSS file as a CSS file.

Prebuilt Extensions[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#prebuilt-extensions "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------

### package.json metadata[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#package-json-metadata "Link to this heading")

In addition to the package metadata for [source extensions](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#source-extensions)
, prebuilt extensions have extra `jupyterlab` metadata.

*   `outputDir`: [Output Directory](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#outputdir)
    
*   `webpackConfig`: [Custom Rspack config](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#webpackconfig)
    

#### Output Directory[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#output-directory "Link to this heading")

When JupyterLab builds the prebuilt extension, it creates a directory of files which can then be copied into the [appropriate install location](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#distributing-prebuilt-extensions)
. The `jupyterlab.outputDir` field gives the relative path to the directory where these JavaScript and other files should be placed. A copy of the `package.json` file with additional build metadata will be put in the `outputDir` and the JavaScript and other files that will be served are put into the `static` subdirectory.

"jupyterlab": {
  "outputDir": "mypackage/labextension"
}

Copy to clipboard

#### Custom Rspack config[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#custom-rspack-config "Link to this heading")

Warning

This feature is _experimental_ and may change without notice since it exposes internal implementation details (namely Rspack). Be careful in using it, as a misconfiguration may break the prebuilt extension system.

The prebuilt extension system uses the Rspack [Module Federation System](https://module-federation.io/)
. Normally this is an implementation detail that prebuilt extension authors do not need to worry about, but occasionally extension authors will want to tweak the configuration used to build their extension to enable various features. Extension authors can specify a custom Rspack config file that will be merged with the Rspack config generated by the prebuilt extension system using the `jupyterlab.webpackConfig` field in `package.json`. The value should be the relative path to the config file:

"jupyterlab": {
  "webpackConfig": "./webpack.config.js"
}

Copy to clipboard

For historical reasons, the name is `webpackConfig` instead of `rspackConfig`. Rspack is largely compatible with webpack configuration options; see the Rspack [migration guide](https://rspack.rs/guide/migration/webpack)
. Custom Rspack configuration can be used to enable Rspack features, configure additional file loaders, and for many other things. Here is an example of a custom config that enables the [async WebAssembly experimental feature](https://rspack.rs/config/experiments#experimentsasyncwebassembly)
 of Rspack:

module.exports \= {
  experiments: {
    asyncWebAssembly: true
  }
};

Copy to clipboard

This custom config will be merged with the [prebuilt extension config](https://github.com/jupyterlab/jupyter-builder/blob/main/src/extensionConfig.ts)
 when building the prebuilt extension.

### Developing a prebuilt extension[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#developing-a-prebuilt-extension "Link to this heading")

Build a prebuilt extension using the `jupyter-builder build` command. This command uses dependency metadata from the active JupyterLab to produce a set of files from a source extension that comprise the prebuilt extension. The files include a main entry point `remoteEntry.<hash>.js`, dependencies bundled into JavaScript files, `package.json` (with some extra build metadata), as well as plugin settings and theme directory structures if needed.

While authoring a prebuilt extension, you can use the `jupyter-builder develop` command to create a link to your prebuilt output directory, similar to `pip install -e`:

jupyter\-builder develop . \--overwrite

Copy to clipboard

Then rebuilding your extension and refreshing JupyterLab in the browser should pick up changes in your prebuilt extension source code.

If using Windows, you may need to configure your operating system for the `develop` command described above to work, please see the note: [Important for Windows users](https://jupyterlab.readthedocs.io/en/stable/extension/extension_tutorial.html#important-for-windows-users)

If you are developing your prebuilt extension against the JupyterLab source repo, you can run JupyterLab with `jupyter lab --dev-mode --extensions-in-dev-mode` to have the development version of JupyterLab load prebuilt extensions. It would be best if you had in mind that the JupyterLab packages that your extension depends on may differ from those published; this means that your extension doesn’t build with JupyterLab dependencies from your node\_modules folder but those in JupyterLab source code.

If you are using TypeScript, the TypeScript compiler would complain because the dependencies of your extension may differ from those in JupyterLab. For that reason, you need to add to your `tsconfig.json` the path where to search for these dependencies by adding the option [paths](https://www.typescriptlang.org/tsconfig#paths)
:

{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@jupyterlab/\*": \["../jupyterlab/packages/\*"\],
      "\*": \["node\_modules/\*"\]
    }
  }
}

Copy to clipboard

When adding the path to find JupyterLab dependencies, it may cause troubles with other dependencies (like lumino or react) in your project because JupyterLab packages will take its dependencies from JupyterLab `node_modules` folder. In contrast, your packages will take them from your `node_modules` folder. To solve this problem, you’ll need to add the dependencies with conflicts to `resolutions` in your `package.json`. This way, both projects (JupyterLab and your extension) use the same version of the duplicated dependencies.

We provide a [extension template](https://github.com/jupyterlab/extension-template)
 that handles all of the scaffolding for an extension author, including the shipping of appropriate data files, so that when the user installs the package, the prebuilt extension ends up in `share/jupyter/labextensions`

### Distributing a prebuilt extension[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#distributing-a-prebuilt-extension "Link to this heading")

Prebuilt extensions can be distributed by any system that can copy the prebuilt assets into an appropriate location where JupyterLab can find them. The [official extension template](https://github.com/jupyterlab/extension-template)
 shows how to distribute prebuilt extensions via Python pip or conda packages. A system package manager, or even just an administrative script that copies directories, could be used as well.

To distribute a prebuilt extension, copy its [output directory](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#outputdir)
 to a location where JupyterLab will find it, typically `<sys-prefix>/share/jupyter/labextensions/<package-name>`, where `<package-name>` is the JavaScript package name in the `package.json`. For example, if your JavaScript package name is `@my-org/my-package`, then the appropriate directory would be `<sys-prefix>/share/jupyter/labextensions/@my-org/my-package`.

The JupyterLab server makes the `static/` files available via a `/labextensions/` server handler. The settings and themes handlers in the server also load settings and themes from the prebuilt extension directories. If a prebuilt extension has the same name as a source extension, the prebuilt extension is preferred.

#### Packaging Information[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#packaging-information "Link to this heading")

Since prebuilt extensions are distributed in many ways (Python pip packages, conda packages, and potentially in many other packaging systems), the prebuilt extension directory can include an extra file, `install.json`, that helps the user know how a prebuilt extension was installed and how to uninstall it. This file should be copied by the packaging system distributing the prebuilt extension into the top-level directory, for example `<sys-prefix>/share/jupyter/labextensions/<package-name>/install.json`.

This `install.json` file is used by JupyterLab to help a user know how to manage the extension. For example, `jupyter labextension list` includes information from this file, and `jupyter labextension uninstall` can print helpful uninstall instructions. Here is an example `install.json` file:

{
  "packageManager": "python",
  "packageName": "mypackage",
  "uninstallInstructions": "Use your Python package manager (pip, conda, etc.) to uninstall the package mypackage"
}

Copy to clipboard

*   `packageManager`: This is the package manager that was used to install the prebuilt extension, for example, `python`, `pip`, `conda`, `debian`, `system administrator`, etc.
    
*   `packageName`: This is the package name of the prebuilt extension in the package manager above, which may be different than the package name in `package.json`.
    
*   `uninstallInstructions`: This is a short block of text giving the user instructions for uninstalling the prebuilt extension. For example, it might instruct them to use a system package manager or talk to a system administrator.
    

#### PyPI Trove Classifiers[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#pypi-trove-classifiers "Link to this heading")

Extensions distributed as Python packages may declare additional metadata in the form of [trove classifiers](https://pypi.org/classifiers)
. These improve the browsing experience for users on [PyPI](https://pypi.org/search)
. While including the license, development status, Python versions supported, and other topic classifiers are useful for many audiences, the following classifiers are specific to Jupyter and JupyterLab.

Framework :: Jupyter
Framework :: Jupyter :: JupyterLab
Framework :: Jupyter :: JupyterLab :: 1
Framework :: Jupyter :: JupyterLab :: 2
Framework :: Jupyter :: JupyterLab :: 3
Framework :: Jupyter :: JupyterLab :: 4
Framework :: Jupyter :: JupyterLab :: Extensions
Framework :: Jupyter :: JupyterLab :: Extensions :: Mime Renderers
Framework :: Jupyter :: JupyterLab :: Extensions :: Prebuilt
Framework :: Jupyter :: JupyterLab :: Extensions :: Themes

Copy to clipboard

Include each relevant classifier (and its parents) to help describe what your package provides to prospective users in your `setup.py`, `setup.cfg`, or `pyproject.toml`. In particular `Framework :: Jupyter :: JupyterLab :: Extensions :: Prebuilt` is used by the extension manager to get the available extensions from PyPI.org.

Hint

For example, a theme, only compatible with JupyterLab 3, and distributed as a ready-to-run, prebuilt extension might look like:

\# setup.py
setup(
    \# the rest of the package's metadata
    \# ...
    classifiers\=\[\
        "Framework :: Jupyter",\
        "Framework :: Jupyter :: JupyterLab",\
        "Framework :: Jupyter :: JupyterLab :: 3",\
        "Framework :: Jupyter :: JupyterLab :: Extensions",\
        "Framework :: Jupyter :: JupyterLab :: Extensions :: Prebuilt",\
        "Framework :: Jupyter :: JupyterLab :: Extensions :: Themes",\
    \]
)

Copy to clipboard

This would be discoverable from, for example, a [PyPI search for theme extensions](https://pypi.org/search/?c=Framework+%3A%3A+Jupyter+%3A%3A+JupyterLab+%3A%3A+Extensions+%3A%3A+Themes)
.

Development workflow for source extensions[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#development-workflow-for-source-extensions "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Developing a source extension is deprecated. [Developing prebuilt extensions](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#prebuilt-dev-workflow)
 is usually much easier since they do not require rebuilding JupyterLab to see changes. If you need to develop a source extension, here are some tips for a development workflow.

While authoring a source extension, you can use the command:

jlpm   \# install npm package dependencies
jlpm build  \# optional build step if using TypeScript, babel, etc.
jupyter labextension install  \# install the current directory as an extension

Copy to clipboard

This causes the builder to re-install the source folder before building the application files. You can re-build at any time using `jupyter lab build` and it will reinstall these packages.

You can also link other local `npm` packages that you are working on simultaneously using `jupyter labextension link`; they will be re-installed but not considered as extensions. Local extensions and linked packages are included in `jupyter labextension list`.

When using local extensions and linked packages, you can run the command

jupyter lab \--watch

Copy to clipboard

This will cause the application to incrementally rebuild when one of the linked packages changes. Note that only compiled JavaScript files (and the CSS files) are watched by the Rspack process. This means that if your extension is in TypeScript you’ll have to run a `jlpm build` before the changes will be reflected in JupyterLab. To avoid this step you can also watch the TypeScript sources in your extension which is usually assigned to the `tsc -w` shortcut. If Rspack doesn’t seem to detect the changes, this can be related to [the number of available watches](https://github.com/webpack/docs/wiki/troubleshooting#not-enough-watchers)
.

Note that the application is built against **released** versions of the core JupyterLab extensions. You should specify the version using the `^` operator, such as `^4.0.0`, so that the build system can use newer minor and patch versions of a package with a particular major version. If your extension depends on JupyterLab packages, it should be compatible with the dependencies in the `jupyterlab/static/package.json` file. Note that building will always use the latest JavaScript packages that meet the dependency requirements of JupyterLab itself and any installed extensions. If you wish to test against a specific patch release of one of the core JupyterLab packages you can temporarily pin that requirement to a specific version in your own dependencies.

If you want to test a source extension against the unreleased versions of JupyterLab, you can run the command

jupyter lab \--watch \--splice-source

Copy to clipboard

This command will splice the local `packages` directory into the application directory, allowing you to build source extension(s) against the current development sources. To statically build spliced sources, use `jupyter lab build --splice-source`. Once a spliced build is created, any subsequent calls to `jupyter-builder build` will be in splice mode by default. A spliced build can be forced by calling `jupyter-builder build --splice-source`. Note that [developing a prebuilt extension](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#prebuilt-dev-workflow)
 against a development version of JupyterLab is generally much easier than source package building.

The package should export EMCAScript 6 compatible JavaScript. It can import CSS using the syntax `require('foo.css')`. The CSS files can also import CSS from other packages using the syntax `@import url('~foo/index.css')`, where `foo` is the name of the package.

The following file types are also supported (both in JavaScript and CSS): `json`, `html`, `jpg`, `png`, `gif`, `svg`, `js.map`, `woff2`, `ttf`, `eot`.

If your package uses any other file type it must be converted to one of the above types or [include a loader in the import statement](https://rspack.rs/api/loader-api/inline)
. If you include a loader, the loader must be importable at build time, so if it is not already installed by JupyterLab, you must add it as a dependency of your extension.

If your JavaScript is written in any other dialect than EMCAScript 6 (2015) it should be converted using an appropriate tool. You can use Rspack or Webpack to pre-build your extension to use any of it’s features not enabled in our build configuration. To build a compatible package, set `output.library.type` to `"commonjs2"` in your Webpack or Rspack configuration. (see [this](https://github.com/saulshanabrook/jupyterlab-webpack)
 example repo).

If you publish your extension on `npm.org`, users will be able to install it as simply `jupyter labextension install <foo>`, where `<foo>` is the name of the published `npm` package. You can alternatively provide a script that runs `jupyter labextension install` against a local folder path on the user’s machine or a provided tarball. Any valid `npm install` specifier can be used in `jupyter labextension install` (e.g. `foo@latest`, `bar@3.0.0.0`, `path/to/folder`, and `path/to/tar.gz`).

We encourage extension authors to add the [jupyterlab-extension GitHub topic](https://github.com/search?utf8=%E2%9C%93&q=topic%3Ajupyterlab-extension&type=Repositories)
 to any GitHub extension repository.

Testing your extension[#](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#testing-your-extension "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------

Note

We highly recommend using the [extension template](https://github.com/jupyterlab/extension-template)
 to set up tests configuration.

There are a number of helper functions in `testutils` in this repo (which is a public `npm` package called `@jupyterlab/testutils`) that can be used when writing tests for an extension. See `tests/test-application` for an example of the infrastructure needed to run tests.

If you are using [jest](https://jestjs.io/)
 to test your extension, you will need to transpile the jupyterlab packages to `commonjs` as they are using ES6 modules that `node` does not support.

To transpile jupyterlab packages, you need to install the following package:

jlpm add \--dev jest @types/jest ts-jest @babel/core@^7 @babel/preset-env@^7

Copy to clipboard

Then in `jest.config.js`, you will specify to use babel for js files and ignore all node modules except the ES6 modules:

const jestJupyterLab \= require('@jupyterlab/testutils/lib/jest-config');

const esModules \= \['@jupyterlab/'\].join('|');

const baseConfig \= jestJupyterLab(\_\_dirname);

module.exports \= {
  ...baseConfig,
  automock: false,
  collectCoverageFrom: \[\
    'src/\*\*/\*.{ts,tsx}',\
    '!src/\*\*/\*.d.ts',\
    '!src/\*\*/.ipynb\_checkpoints/\*'\
  \],
  coverageReporters: \['lcov', 'text'\],
  testRegex: 'src/.\*/.\*.spec.ts\[x\]?$',
  transformIgnorePatterns: \[\
    ...baseConfig.transformIgnorePatterns,\
    \`/node\_modules/(?!${esModules}).+\`\
  \]
};

Copy to clipboard

Finally, you will need to configure babel with a `babel.config.js` file containing:

module.exports \= require('@jupyterlab/testutils/lib/babel.config');

Copy to clipboard

On this page

[Edit on GitHub](https://github.com/jupyterlab/jupyterlab/edit/4.6.x/docs/source/extension/extension_dev.md)

[Show Source](https://jupyterlab.readthedocs.io/en/stable/_sources/extension/extension_dev.md.txt)