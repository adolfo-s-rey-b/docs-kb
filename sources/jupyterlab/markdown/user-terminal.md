[Skip to main content](https://jupyterlab.readthedocs.io/en/stable/user/terminal.html#main-content)

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

Terminals[#](https://jupyterlab.readthedocs.io/en/stable/user/terminal.html#terminals "Link to this heading")

==============================================================================================================

JupyterLab terminals provide full support for system shells (bash, tcsh, etc.) on Mac/Linux and PowerShell on Windows. You can run anything in your system shell with a terminal, including programs such as vim or emacs. The terminals run on the system where the Jupyter server is running, with the privileges of your user. Thus, if JupyterLab is installed on your local machine, the JupyterLab terminals will run there.

![JupyterLab with an open terminal in the main document area.](https://jupyterlab.readthedocs.io/en/stable/_images/terminal-layout.png)

To open a new terminal, click the `+` button in the file browser and select the terminal in the new Launcher tab:

Closing a terminal tab will leave it running on the server, but you can re-open it using the Running tab in the left sidebar:

Copy/Paste[#](https://jupyterlab.readthedocs.io/en/stable/user/terminal.html#copy-paste "Link to this heading")

----------------------------------------------------------------------------------------------------------------

For macOS users, `Cmd+C` and `Cmd+V` work as usual.

For Windows users using `PowerShell`, `Ctrl+Insert` and `Shift+Insert` work as usual.

To use the native browser Copy/Paste menu, hold `Shift` and right click to bring up the context menu (note: this may not work in all browsers).

For non-macOS users, JupyterLab will interpret `Ctrl+C` as a copy if there is text selected. In addition, `Ctrl+V` will be interpreted as a paste command unless the `pasteWithCtrlV` setting is disabled. One may want to disable `pasteWithCtrlV` if the shortcut is needed for something else such as the vi editor.

For anyone using a \*nix shell, the default `Ctrl+Shift+C` conflicts with the default shortcut for toggling the command palette (`apputils:activate-command-palette`). If desired, that shortcut can be changed by editing the keyboard shortcuts in settings. Using `Ctrl+Shift+V` for paste works as usual.

On this page

[Edit on GitHub](https://github.com/jupyterlab/jupyterlab/edit/4.6.x/docs/source/user/terminal.md)

[Show Source](https://jupyterlab.readthedocs.io/en/stable/_sources/user/terminal.md.txt)