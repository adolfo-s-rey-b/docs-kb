[Skip to main content](https://jupyterlab.readthedocs.io/en/stable/extension/identity.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [![jupyter.org](https://jupyterlab.readthedocs.io/en/stable/_static/jupyter_logo.svg)](https://jupyter.org/)
    
*   [GitHub](https://github.com/jupyterlab/jupyterlab)
    
*   [Discourse](https://discourse.jupyter.org/c/jupyterlab/17)
    
*   [Zulip](https://jupyter.zulipchat.com/#narrow/channel/469762-jupyterlab)
    

Identity[#](https://jupyterlab.readthedocs.io/en/stable/extension/identity.html#identity "Link to this heading")

=================================================================================================================

Starting with JupyterLab v3.6, user identity builds on top of the `IdentityProvider` and the endpoint `/api/me` introduced in Jupyter Server v2 as part of the authentication. The `/api/me` endpoint returns a dictionary with the user’s identity and their permissions. Please check out its [documentation](https://jupyter-server.readthedocs.io/en/latest/operators/security.html#identity-model)
 to know more about the identity model implemented in Jupyter Server.

The user identity API was included in JupyterLab as part of the service package by adding a new service called [`UserManager`](https://jupyterlab.readthedocs.io/en/stable/api/classes/services.UserManager-1.html)
 to the [`ServiceManager`](https://jupyterlab.readthedocs.io/en/stable/api/classes/services.ServiceManager-1.html)
. This new service periodically requests the user identity to the `/api/me` endpoint and keeps the information in memory until the next request. Nevertheless, it is always possible to refresh the information manually by calling the `refreshUser` method. Once the service is ready, it is possible to access the user’s identity through the property `identity` or listen for changes by subscribing to the signal `userChanged`.

**Example:**

const extension: JupyterFrontEndPlugin<void\> \= {
  id: 'jupyterlab-extension',
  autoStart: true,
  activate: (app: JupyterFrontEnd) \=> {
    const user \= app.serviceManager.user;
    user.ready.then(() \=> {
      console.debug('Identity:', user.identity);
      console.debug('Permissions:', user.permissions);
    });
  }
};

Copy to clipboard

[Edit on GitHub](https://github.com/jupyterlab/jupyterlab/edit/4.6.x/docs/source/extension/identity.md)

[Show Source](https://jupyterlab.readthedocs.io/en/stable/_sources/extension/identity.md.txt)