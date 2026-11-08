[Skip to main content](https://jupyterlab.readthedocs.io/en/stable/getting_started/starting.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [![jupyter.org](https://jupyterlab.readthedocs.io/en/stable/_static/jupyter_logo.svg)](https://jupyter.org/)
    
*   [GitHub](https://github.com/jupyterlab/jupyterlab)
    
*   [Discourse](https://discourse.jupyter.org/c/jupyterlab/17)
    
*   [Zulip](https://jupyter.zulipchat.com/#narrow/channel/469762-jupyterlab)
    

Starting JupyterLab[#](https://jupyterlab.readthedocs.io/en/stable/getting_started/starting.html#starting-jupyterlab "Link to this heading")

=============================================================================================================================================

Start JupyterLab using:

jupyter lab

Copy to clipboard

JupyterLab will open automatically in your browser.

If your notebook files are not in the current directory, you can pass your working directory path as argument when starting JupyterLab. Avoid running it from your root volume (e.g. `C:\` on Windows or `/` on Linux) to limit the risk of modifying system files.

Example:

#Windows Example
jupyter lab \--notebook-dir\=E:/ \--preferred-dir E:/Documents/Somewhere/Else
#Linux Example
jupyter lab \--notebook-dir\=/var/ \--preferred-dir /var/www/html/example-app/

Copy to clipboard

You may access JupyterLab by entering the notebook server’s [URL](https://jupyterlab.readthedocs.io/en/stable/user/urls.html#urls)
 into the browser. JupyterLab sessions always reside in a [workspace](https://jupyterlab.readthedocs.io/en/stable/user/workspaces.html#workspaces)
. The default workspace is the main `/lab` URL:

http(s)://<server:port>/<lab-location>/lab

Copy to clipboard

Like the classic notebook, JupyterLab provides a way for users to copy URLs that [open a specific notebook or file](https://jupyterlab.readthedocs.io/en/stable/user/urls.html#url-tree)
. Additionally, JupyterLab URLs are an advanced part of the user interface that allows for managing [workspaces](https://jupyterlab.readthedocs.io/en/stable/user/urls.html#url-workspaces)
. To learn more about URLs in JupyterLab, visit [JupyterLab URLs](https://jupyterlab.readthedocs.io/en/stable/user/urls.html#urls)
.

JupyterLab runs on top of Jupyter Server, so see the [security section](https://jupyter-server.readthedocs.io/en/latest/operators/security.html)
 of Jupyter Server’s documentation for security-related information.

[Edit on GitHub](https://github.com/jupyterlab/jupyterlab/edit/4.6.x/docs/source/getting_started/starting.md)

[Show Source](https://jupyterlab.readthedocs.io/en/stable/_sources/getting_started/starting.md.txt)