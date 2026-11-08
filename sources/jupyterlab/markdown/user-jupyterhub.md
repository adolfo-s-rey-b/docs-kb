[Skip to main content](https://jupyterlab.readthedocs.io/en/stable/user/jupyterhub.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [![jupyter.org](https://jupyterlab.readthedocs.io/en/stable/_static/jupyter_logo.svg)](https://jupyter.org/)
    
*   [GitHub](https://github.com/jupyterlab/jupyterlab)
    
*   [Discourse](https://discourse.jupyter.org/c/jupyterlab/17)
    
*   [Zulip](https://jupyter.zulipchat.com/#narrow/channel/469762-jupyterlab)
    

JupyterLab on JupyterHub[#](https://jupyterlab.readthedocs.io/en/stable/user/jupyterhub.html#jupyterlab-on-jupyterhub "Link to this heading")

==============================================================================================================================================

JupyterLab works out of the box with JupyterHub 1.0+, and can even run side by side with the classic Notebook.

When JupyterLab is deployed with JupyterHub it will show additional menu items in the File menu that allow the user to log out or go to the JupyterHub control panel.

Use JupyterLab by Default[#](https://jupyterlab.readthedocs.io/en/stable/user/jupyterhub.html#use-jupyterlab-by-default "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------

If you install JupyterLab on a system running JupyterHub, it will immediately be available at the `/lab` URL, but users will still be directed to the classic Notebook (`/tree`) by default. To change the user’s default user interface to JupyterLab, set the following configuration option in your `jupyterhub_config.py` file:

c.Spawner.default\_url \= "/lab"

Copy to clipboard

Example Configuration[#](https://jupyterlab.readthedocs.io/en/stable/user/jupyterhub.html#example-configuration "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

For a fully-configured example of using JupyterLab with JupyterHub, see the [jupyterhub-deploy-teaching](https://github.com/jupyterhub/jupyterhub-deploy-teaching)
 repository.

On this page

[Edit on GitHub](https://github.com/jupyterlab/jupyterlab/edit/4.6.x/docs/source/user/jupyterhub.md)

[Show Source](https://jupyterlab.readthedocs.io/en/stable/_sources/user/jupyterhub.md.txt)