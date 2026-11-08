[Skip to main content](https://jupyterlab.readthedocs.io/en/stable/user/lsp.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [![jupyter.org](https://jupyterlab.readthedocs.io/en/stable/_static/jupyter_logo.svg)](https://jupyter.org/)
    
*   [GitHub](https://github.com/jupyterlab/jupyterlab)
    
*   [Discourse](https://discourse.jupyter.org/c/jupyterlab/17)
    
*   [Zulip](https://jupyter.zulipchat.com/#narrow/channel/469762-jupyterlab)
    

Language Server Protocol support[#](https://jupyterlab.readthedocs.io/en/stable/user/lsp.html#language-server-protocol-support "Link to this heading")

=======================================================================================================================================================

Warning

As of JupyterLab 4.2, there is no user-facing integration of Language Server Protocol (LSP); to take advantage of LSP you need to install an extension, such as [jupyterlab-lsp](https://jupyterlab-lsp.readthedocs.io/)
.

JupyterLab ships with components enabling extensions to handle and communicate with language servers.

The LSP service is disabled by default, it can be enabled by toggling the _Activate_ option in the _Language Servers_ section of the setting page. Enabling the service will not have any effect unless extensions providing integration with the editor (or other elements of JupyterLab UI) are installed.

Requirements[#](https://jupyterlab.readthedocs.io/en/stable/user/lsp.html#requirements "Link to this heading")

---------------------------------------------------------------------------------------------------------------

By default JupyterLab does not come with any language servers installed. For the list of LSP servers tested with `jupyter-lsp`, the jupyter-server extension which spawns and communicates with the servers, see the [documentation of the extension](https://jupyterlab-lsp.readthedocs.io/en/latest/Language%20Servers.html)
.

Settings[#](https://jupyterlab.readthedocs.io/en/stable/user/lsp.html#settings "Link to this heading")

-------------------------------------------------------------------------------------------------------

The settings for language servers can be found on the settings page of JupyterLab (_Settings > Settings Editor > Language Servers (Experimental)_).

*   **Activate**: this option allows users to enable or disable the LSP services.
    
*   **Language Server**: this section allows users to configure the installed language servers.
    

![../_images/settings.png](https://jupyterlab.readthedocs.io/en/stable/_images/settings.png)

Language servers setting page.[#](https://jupyterlab.readthedocs.io/en/stable/user/lsp.html#id1 "Link to this image")

Please note that this settings page will be replaced by a more sophisticated editor accessible under _Language Servers_ section when `jupyterlab-lsp` is installed.

On this page

[Edit on GitHub](https://github.com/jupyterlab/jupyterlab/edit/4.6.x/docs/source/user/lsp.md)

[Show Source](https://jupyterlab.readthedocs.io/en/stable/_sources/user/lsp.md.txt)