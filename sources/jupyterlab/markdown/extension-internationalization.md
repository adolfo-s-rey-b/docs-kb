[Skip to main content](https://jupyterlab.readthedocs.io/en/stable/extension/internationalization.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [![jupyter.org](https://jupyterlab.readthedocs.io/en/stable/_static/jupyter_logo.svg)](https://jupyter.org/)
    
*   [GitHub](https://github.com/jupyterlab/jupyterlab)
    
*   [Discourse](https://discourse.jupyter.org/c/jupyterlab/17)
    
*   [Zulip](https://jupyter.zulipchat.com/#narrow/channel/469762-jupyterlab)
    

Internationalization and Localization[#](https://jupyterlab.readthedocs.io/en/stable/extension/internationalization.html#internationalization-and-localization "Link to this heading")

=======================================================================================================================================================================================

To internationalize your extension, the following tasks are required:

Note

Please read carefully the [Rules](https://jupyterlab.readthedocs.io/en/stable/extension/internationalization.html#internationalization-rules)
 as they are strong constraints for internationalization to work.

1.  Add the token [`ITranslator`](https://jupyterlab.readthedocs.io/en/stable/api/interfaces/translation.ITranslator.html)
     from `@jupyterlab/translation` package to your plugin dependencies.
    

const extension: JupyterFrontEndPlugin<void\> \= {
  id: 'jupyterlab-extension',
  autoStart: true,
  requires: \[ITranslator\],
  activate: (app: JupyterFrontEnd, translator: ITranslator) \=> {}
};

Copy to clipboard

2.  Get the translation bundle from the domain on which your extension is translated.
    

const trans \= translator.load('my\_domain');

Copy to clipboard

Note

A good practice is to use your extension named using only letters, numbers and `_` characters.

Domain are normalized by replacing `-` with `_` characters.

3.  Wraps all translatable strings with one of the [gettext functions](https://jupyterlab.readthedocs.io/en/stable/api/modules/translation.html#translationbundle)
    .
    

Examples:

this.\_trans.\_\_('String to be translated');
this.\_trans.\_\_('%1 is argument of a translated string', adjective);
this.\_trans.\_n('Singular string for %1', 'Plural string for %1', n);

Copy to clipboard

You could also look at the following pull requests on the [spellchecker extension](https://github.com/jupyterlab-contrib/spellchecker/pull/84/files)
.

4.  Create and publish the translation for your extension.
    

There are two options: you can either add your extension to the JupyterLab [language packs](https://github.com/jupyterlab/language-packs/#adding-a-new-extension)
 or you can create a python package to distribute your extension translation (see below).

Create translation python package[#](https://jupyterlab.readthedocs.io/en/stable/extension/internationalization.html#create-translation-python-package "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

JupyterLab follows Gettext’s approach for translation. Gettext extracts strings from source code, and compiles them with provided translation (find more about it in the [Python documentation](https://docs.python.org/3/library/gettext.html#internationalizing-your-programs-and-modules)
).

By using [jupyterlab-translate](https://github.com/jupyterlab/jupyterlab-translate)
, you can extract, update, and compile your translation.

After that, you must include your compiled translation (.json, .mo) to your python package. This can be done by adding the entry point to your `pyproject.toml`:

\[project.entry-points."jupyterlab.locale"\]
jupyterlab\_some\_package \= "jupyterlab\_some\_package"

Copy to clipboard

With modern build backends (e.g. [hatchling](https://hatch.pypa.io/)
), compiled translation files inside the package directory are included automatically. If your backend requires explicit listing, add the patterns to your build configuration; for example with hatchling:

\[tool.hatch.build.targets.wheel\]
include \= \[\
    "jupyterlab\_some\_package/\*\*/\*.json",\
    "jupyterlab\_some\_package/\*\*/\*.mo",\
\]

Copy to clipboard

Note

An example is available in the [server test](https://github.com/jupyterlab/jupyterlab_server/tree/main/tests/translations/jupyterlab-some-package)

Settings translation[#](https://jupyterlab.readthedocs.io/en/stable/extension/internationalization.html#settings-translation "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------

Settings schema can also be translated. The translatable strings are extracted using regex selectors on JSON path. By default, the following selectors are used:

*   `title`: Settings title
    
*   `description`: Settings description
    
*   `properties/.*/title`: Property titles
    
*   `properties/.*/description`: Property descriptions
    
*   `definitions/.*/properties/.*/title`: Property titles in definitions
    
*   `definitions/.*/properties/.*/description`: Property descriptions in definitions
    
*   `jupyter\.lab\.setting-icon-label`: Settings icon label in JupyterLab
    
*   `jupyter\.lab\.menus/.*/label`: Menu label in JupyterLab
    
*   `jupyter\.lab\.toolbars/.*/label`: Toolbar item label in JupyterLab
    

Those selectors can be configured using the `jupyter.lab.internationalization` key in the schema. The following example will pick the default value for `myprop` property:

"jupyter.lab.internationalization": {
    "selectors": \[\
        "properties/myprop/default",\
    \],
    "domain": "my\_jlab\_extension"
}

Copy to clipboard

In the example above, a specific domain in which the translations are defined is also specified (here `my_jlab_extension`). If no domain is specified, it defaults to `jupyterlab`.

Rules[#](https://jupyterlab.readthedocs.io/en/stable/extension/internationalization.html#rules "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

In order for the strings to be extracted from the code, the following rules must be followed.

*   Domain name are normalized by replacing `-` to `_`
    
*   Translation bundle variable must be one of:
    
    *   `trans`
        
    *   `this.trans`
        
    *   `this._trans`
        
    *   `this.props.trans`
        
    *   `props.trans`
        

Examples that work:

trans.\_\_('This translatable string will be found');
this.trans.\_\_('This translatable string will be found');
this.\_trans.\_\_('This translatable string will be found');
this.props.trans.\_\_('This translatable string will be found');
props.trans.\_\_('This translatable string will be found');

Copy to clipboard

Examples that will **not** work:

translator.\_\_("This translatable string WON'T be found");
\_\_("This translatable string WON'T be found");
this.\_\_("This translatable string WON'T be found");

Copy to clipboard

To fix this issue, alter your variable to use an accepted name:

const trans \= translator;
trans.\_\_('This translatable string will be found');

Copy to clipboard

*   String must be passed directly to the function; don’t use variables or constants
    

Example that will **not** work:

const errorMessage \= "This translatable string WON'T be found";
trans.\_\_(errorMessage);

Copy to clipboard

To fix this issue, pass the string directly:

trans.\_\_('This translatable string will be found');

Copy to clipboard

On this page

[Edit on GitHub](https://github.com/jupyterlab/jupyterlab/edit/4.6.x/docs/source/extension/internationalization.md)

[Show Source](https://jupyterlab.readthedocs.io/en/stable/_sources/extension/internationalization.md.txt)