[Skip to main content](https://jupyterlab.readthedocs.io/en/stable/user/binder.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [![jupyter.org](https://jupyterlab.readthedocs.io/en/stable/_static/jupyter_logo.svg)](https://jupyter.org/)
    
*   [GitHub](https://github.com/jupyterlab/jupyterlab)
    
*   [Discourse](https://discourse.jupyter.org/c/jupyterlab/17)
    
*   [Zulip](https://jupyter.zulipchat.com/#narrow/channel/469762-jupyterlab)
    

JupyterLab on Binder[#](https://jupyterlab.readthedocs.io/en/stable/user/binder.html#jupyterlab-on-binder "Link to this heading")

==================================================================================================================================

Customize the layout[#](https://jupyterlab.readthedocs.io/en/stable/user/binder.html#customize-the-layout "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

A specific layout of JupyterLab can be saved as workspace to be restored later or to be shared with others.

To specify a workspace on Binder, you first need to export the layout you want to use. For that launch JupyterLab and arrange the application in the layout you prefer. Then you can export it through the menu `File -> Save Current Workspace As…`.

Now you need to copy that file in the Binder configuration folder and import it in the `postBuild` script. Assuming the binder workspace file is stored at `binder/workspace.jupyterlab-workspace`:

postBuild[#](https://jupyterlab.readthedocs.io/en/stable/user/binder.html#id1 "Link to this code")

#!/usr/bin/env bash
set \-eux

conda run \-n notebook jupyter lab workspaces import \--name default binder/workspace.jupyterlab-workspace

Copy to clipboard

Customize user settings[#](https://jupyterlab.readthedocs.io/en/stable/user/binder.html#customize-user-settings "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

To customize the user settings on a Binder instance, you can define a `overrides.json` that will contain a dictionary whose primary keys are the plugin ids and the values are the new settings.

For example to deactivate the announcements on Binder, you will have to override the following setting:

overrides.json[#](https://jupyterlab.readthedocs.io/en/stable/user/binder.html#id2 "Link to this code")

{
  "@jupyterlab/apputils-extension:notification": {
    "fetchNews": "false"
  }
}

Copy to clipboard

Then you will have to copy that file in a special folder:

postBuild[#](https://jupyterlab.readthedocs.io/en/stable/user/binder.html#id3 "Link to this code")

#!/usr/bin/env bash
set \-eux

mkdir \-p ${NB\_PYTHON\_PREFIX}/share/jupyter/lab/settings
cp overrides.json ${NB\_PYTHON\_PREFIX}/share/jupyter/lab/settings

Copy to clipboard

On this page

[Edit on GitHub](https://github.com/jupyterlab/jupyterlab/edit/4.6.x/docs/source/user/binder.md)

[Show Source](https://jupyterlab.readthedocs.io/en/stable/_sources/user/binder.md.txt)