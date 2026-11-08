[Skip to main content](https://jupyterlab.readthedocs.io/en/stable/user/directories.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [![jupyter.org](https://jupyterlab.readthedocs.io/en/stable/_static/jupyter_logo.svg)](https://jupyter.org/)
    
*   [GitHub](https://github.com/jupyterlab/jupyterlab)
    
*   [Discourse](https://discourse.jupyter.org/c/jupyterlab/17)
    
*   [Zulip](https://jupyter.zulipchat.com/#narrow/channel/469762-jupyterlab)
    

[![Sponsored: Union AI](https://media.ethicalads.io/images/2026/09/OOM_RETRY_240X180.jpg)](https://server.ethicalads.io/proxy/click/11030/01a1b9a4-80ba-7602-ac7e-62674abf9ea7/)

[**OOM? Retry with more.** Handle OOMs in Python. Retry with more memory on Union.ai. **Sign Up Now**](https://server.ethicalads.io/proxy/click/11030/01a1b9a4-80ba-7602-ac7e-62674abf9ea7/)

_[Ad by EthicalAds](https://www.ethicalads.io/?ref=rtd-sidebar)
_   ·   [ℹ️](https://www.ethicalads.io/advertisers/topics/data-science/?ref=rtd-sidebar-buy-ads)

Advanced Usage[#](https://jupyterlab.readthedocs.io/en/stable/user/directories.html#advanced-usage "Link to this heading")

===========================================================================================================================

JupyterLab manages several different locations for its data. These locations are shown by running `jupyter lab path`:

*   **Application Directory**: where JupyterLab stores the main build of JupyterLab with associated data, including extensions built into JupyterLab.
    
*   **User Settings Directory**: where JupyterLab stores user-level settings for JupyterLab extensions
    
*   **Workspaces Directory**: where JupyterLab stores workspaces
    

JupyterLab also honors **LabConfig Directories** directories for configuration data from the `labconfig` subdirectories of the Jupyter `config` directories in the Jupyter path hierarchy.

Additionally, JupyterLab can load dynamic federated (prebuilt) extensions, i.e., extensions that bundle their dependencies, from the `labextensions` subdirectories of the Jupyter `data` directories.

See the locations of these Jupyter config paths by running `jupyter --path`.

JupyterLab Build Process[#](https://jupyterlab.readthedocs.io/en/stable/user/directories.html#jupyterlab-build-process "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------

To rebuild the app directory, run `jupyter lab build`. By default, the `jupyter labextension install` command builds the application, so you typically do not need to call `build` directly.

Building consists of:

*   Populating the `staging/` directory using template files
    
*   Handling any locally installed packages
    
*   Ensuring all installed assets are available
    
*   Bundling the assets
    
*   Copying the bundled assets to the `static` directory
    

Note that building will always use the latest JavaScript packages that meet the dependency requirements of JupyterLab itself and any installed extensions. If you wish to run JupyterLab with the set of pinned requirements that was shipped with the Python package, you can launch as `jupyter lab --core-mode`.

The build process uses a specific `yarn` version with a default working combination of npm packages stored in a `yarn.lock` file shipped with JupyterLab.

### Disabling Rebuild Checks[#](https://jupyterlab.readthedocs.io/en/stable/user/directories.html#disabling-rebuild-checks "Link to this heading")

JupyterLab automatically checks to see if it needs to rebuild on startup. In some cases, such as automated testing, you may wish to disable the startup rebuild checks altogether. This can be achieved through setting `buildCheck` and `buildAvailable` in `jupyter_server_config.json` (or `.py` equivalent) in any of the `config` locations returned by `jupyter --paths`.

{
  "ServerApp": {
    "tornado\_settings": {
      "page\_config\_data": {
        "buildCheck": false,
        "buildAvailable": false
      }
    }
  }
}

Copy to clipboard

LabConfig Directories[#](https://jupyterlab.readthedocs.io/en/stable/user/directories.html#labconfig-directories "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------

For each config path `<jupyter_config_path>` listed in `jupyter --paths`, the `<jupyter_config_path>/labconfig` directory contains configuration data. This configuration data from all of these directories is combined into a single configuration, with priority order given by `jupyter --paths`.

The primary file used by JupyterLab is `page_config.json`. The `page_config.json` data is used to provide configuration data to the application environment.

The following configurations may be present in this file:

1.  `terminalsAvailable` identifies whether a terminal (i.e. `bash`/`tcsh` on Mac/Linux OR `PowerShell` on Windows) is available to be launched via the Launcher. (This configuration was predominantly required for Windows prior to PowerShell access being enabled in Jupyter Lab.) The value for this field is a Boolean: `true` or `false`.
    
2.  `disabledExtensions` controls which extensions should not load at all.
    
3.  `deferredExtensions` controls which extensions should not load until they are required by something, irrespective of whether they set `autoStart` to `true`.
    

The values for the `disabledExtensions` and `deferredExtensions` fields are objects with boolean values. The following sequence of checks are performed against the patterns in `disabledExtensions` and `deferredExtensions`.

*   If an identical string match occurs between a config value and a package name (e.g., `"@jupyterlab/apputils-extension"`), then the entire package is disabled (or deferred).
    
*   If the string value is compiled as a regular expression and tests positive against a package name (e.g., `"@jupyterlab/apputils*$"`), then the entire package is disabled (or deferred).
    
*   If an identical string match occurs between a config value and an individual plugin ID within a package (e.g., `"@jupyterlab/apputils-extension:settings`), then that specific plugin is disabled (or deferred).
    
*   If the string value is compiled as a regular expression and tests positive against an individual plugin ID within a package (e.g., `"@jupyterlab/apputils-extension:set.*$"`), then that specific plugin is disabled (or deferred).
    

An example `<jupyter_config_path>/labconfig/page_config.json` could look as follows:

{
  "disabledExtensions": {
    "@jupyterlab/notebook-extension": true,
    "@jupyterlab/apputils-extension:settings": true
  },
  "deferredExtensions": {
    "@jupyterlab/apputils-extension:set.\*$": true
  },
  "terminalsAvailable": false
}

Copy to clipboard

See [documentation on enabling and disabling extensions](https://jupyterlab.readthedocs.io/en/stable/user/extensions.html#enable-disable-config)
 for more information.

JupyterLab Application Directory[#](https://jupyterlab.readthedocs.io/en/stable/user/directories.html#jupyterlab-application-directory "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------

The application directory contains the main JupyterLab application files, including built assets, files for rebuilding JupyterLab, installed extensions and linked packages, etc.

By default, the application directory is at `<sys-prefix>/share/jupyter/lab`, where `<sys-prefix>` is the site-specific directory prefix of the current Python environment. You can query the current application path by running `jupyter lab path`. The application directory can be overridden using the `--app-dir` command-line option in any of the JupyterLab commands, or by setting the `JUPYTERLAB_DIR` environment variable.

We recommend users not install JupyterLab in a system location on Unix-like systems, because then the application directory will be read-only. Instead, use a conda environment or `pip install --user jupyterlab` so the application directory is writable by the user.

This directory location and semantics do _not_ follow the standard Jupyter config semantics because we need to build a single unified application, and the default config location for Jupyter is at the user level (user’s home directory). By explicitly using a sys-prefix directory, we can ensure better isolation in virtual environments.

The JupyterLab application directory contains the subdirectories `extensions`, `schemas`, `settings`, `staging`, `static`, and `themes`. In the rest of this section, we will explain each subdirectory.

### extensions[#](https://jupyterlab.readthedocs.io/en/stable/user/directories.html#extensions "Link to this heading")

The `extensions` directory has the packed tarballs for each of the installed extensions for the app. If the application directory is not the same as the `sys-prefix` directory, the extensions installed in the `sys-prefix` directory will be used in the app directory. If an extension is installed in the app directory that exists in the `sys-prefix` directory, it will shadow the `sys-prefix` version. Uninstalling an extension will first uninstall the shadowed extension, and then attempt to uninstall the `sys-prefix` version if called again. If the `sys-prefix` version cannot be uninstalled, its plugins can still be ignored using `ignoredPackages` metadata in `settings`.

### schemas[#](https://jupyterlab.readthedocs.io/en/stable/user/directories.html#schemas "Link to this heading")

The `schemas` directory contains [JSON Schemas](https://json-schema.org/)
 that describe the settings used by individual extensions. Users may edit these settings using the JupyterLab Advanced Settings Editor.

### settings[#](https://jupyterlab.readthedocs.io/en/stable/user/directories.html#settings "Link to this heading")

The `settings` directory inside the [JupyterLab Application directory](https://jupyterlab.readthedocs.io/en/stable/user/directories.html#application-directory)
 may contain `page_config.json`, `overrides.json`, and/or `build_config.json` files.

#### page\_config.json (deprecated)[#](https://jupyterlab.readthedocs.io/en/stable/user/directories.html#page-config-json-deprecated "Link to this heading")

This file is considered deprecated. This file can have similar data as the `page_config.json` file in the LabConfig Directories, except that `disabledExtensions` and `deferredExtensions` are given as arrays of strings.

An example of a `page_config.json` file is:

{
  "disabledExtensions": \["@jupyterlab/toc"\],
  "terminalsAvailable": false
}

Copy to clipboard

#### overrides.json[#](https://jupyterlab.readthedocs.io/en/stable/user/directories.html#overrides-json "Link to this heading")

You can override default values of the extension settings by defining new default values in an `overrides.json` file. For example, if you would like to override the default theme to be the dark theme, create an `overrides.json` file containing the following lines in the [application settings directory](https://jupyterlab.readthedocs.io/en/stable/user/directories.html#application-settings-directory)
 (for example, if the [JupyterLab Application Directory](https://jupyterlab.readthedocs.io/en/stable/user/directories.html#application-directory)
 is `<sys.prefix>/local/share/jupyter/lab`, create this file at `<sys.prefix>/local/share/jupyter/lab/settings/overrides.json`).

{
  "@jupyterlab/apputils-extension:themes": {
    "theme": "JupyterLab Dark"
  }
}

Copy to clipboard

JupyterLab also allows you to **export** and **import** an `overrides.json` file directly through the interface. You can generate an `overrides.json` file based on your current customized settings by clicking the **Export** button in the **Settings Editor**. Similarly, you can use the **Import** button to apply an existing `overrides.json` file. This makes it easier to back up, share, or reuse your configuration.

#### build\_config.json[#](https://jupyterlab.readthedocs.io/en/stable/user/directories.html#build-config-json "Link to this heading")

The `build_config.json` file is used to track the local directories that have been installed using `jupyter labextension install <directory>`, as well as core extensions that have been explicitly uninstalled. An example of a `build_config.json` file is:

{
  "uninstalled\_core\_extensions": \["@jupyterlab/markdownwidget-extension"\],
  "local\_extensions": {
    "@jupyterlab/python-tests": "/path/to/my/extension"
  }
}

Copy to clipboard

### staging and static[#](https://jupyterlab.readthedocs.io/en/stable/user/directories.html#staging-and-static "Link to this heading")

The `static` directory contains the assets that will be loaded by the JupyterLab application. The `staging` directory is used to create the build and then populate the `static` directory.

Running `jupyter lab` will attempt to run the `static` assets in the application directory if they exist. You can run `jupyter lab --core-mode` to load the core JupyterLab application from the installation directory (i.e., the application without any extensions) instead.

If JupyterLab is launched and the static assets are not present, it will display an error in the console and in the browser.

### themes[#](https://jupyterlab.readthedocs.io/en/stable/user/directories.html#themes "Link to this heading")

The `themes` directory contains assets (such as CSS and icons) for JupyterLab theme extensions.

JupyterLab User Settings Directory[#](https://jupyterlab.readthedocs.io/en/stable/user/directories.html#jupyterlab-user-settings-directory "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

The user settings directory contains the user-level settings for Jupyter extensions.

By default, the location is `$HOME/.jupyter/lab/user-settings/`, where `$HOME` is the user’s home directory. This folder is not in the JupyterLab application directory because these settings are typically shared across Python environments. The location can be modified using the `JUPYTERLAB_SETTINGS_DIR` environment variable.

[JSON5](https://json5.org/)
 files are automatically created in this folder recording the settings changes a user makes in the JupyterLab Advanced Settings Editor. The file names follow the pattern of `<extension_name>/<plugin_name>.jupyterlab-settings`. These values override the default values given by extensions, as well as the default overrides from the [overrides.json](https://jupyterlab.readthedocs.io/en/stable/user/directories.html#overridesjson)
 file in the application’s settings directory.

JupyterLab Workspaces Directory[#](https://jupyterlab.readthedocs.io/en/stable/user/directories.html#jupyterlab-workspaces-directory "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------

JupyterLab sessions always reside in a workspace. Workspaces contain the state of JupyterLab: the files that are currently open, the layout of the application areas and tabs, etc. When the page is refreshed, the workspace is restored.

By default, the location is `$HOME/.jupyter/lab/workspaces/`, where `$HOME` is the user’s home directory. This folder is not in the JupyterLab application directory, because these files are typically shared across Python environments. The location can be modified using the `JUPYTERLAB_WORKSPACES_DIR` environment variable.

These files can be imported and exported to create default “profiles”, using the [workspace command line tool](https://jupyterlab.readthedocs.io/en/stable/user/workspaces.html#workspaces-cli)
.

On this page

[Edit on GitHub](https://github.com/jupyterlab/jupyterlab/edit/4.6.x/docs/source/user/directories.md)

[Show Source](https://jupyterlab.readthedocs.io/en/stable/_sources/user/directories.md.txt)