[Skip to main content](https://jupyterlab.readthedocs.io/en/stable/user/announcements.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [![jupyter.org](https://jupyterlab.readthedocs.io/en/stable/_static/jupyter_logo.svg)](https://jupyter.org/)
    
*   [GitHub](https://github.com/jupyterlab/jupyterlab)
    
*   [Discourse](https://discourse.jupyter.org/c/jupyterlab/17)
    
*   [Zulip](https://jupyter.zulipchat.com/#narrow/channel/469762-jupyterlab)
    

Announcements[#](https://jupyterlab.readthedocs.io/en/stable/user/announcements.html#announcements "Link to this heading")

===========================================================================================================================

Your consent is required to get Jupyter news (this is an opt-in feature). Once you have answered the request, you can change your decision in the _Notification_ settings.

Configuration[#](https://jupyterlab.readthedocs.io/en/stable/user/announcements.html#configuration "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

The frontend plugin requesting the news and checking for the update is `@jupyterlab/apputils-extension:announcements`. It can be disabled as any plugin by executing in a terminal prior to start JupyterLab:

jupyter labextension disable "@jupyterlab/apputils-extension:announcements"

Copy to clipboard

### Check for updates[#](https://jupyterlab.readthedocs.io/en/stable/user/announcements.html#check-for-updates "Link to this heading")

You can also control whether to check for updates or not at two levels:

*   on the server side through a command-line option `--LabApp.check_for_updates_class="jupyterlab.NeverCheckForUpdate"`
    
*   on the frontend through the setting _checkForUpdates_ in the _Notification_ section.
    

You can also provide your own class to check for updates. The abstract class to implement is `jupyterlab.handlers.announcements.CheckForUpdateABC`.

### Jupyter news[#](https://jupyterlab.readthedocs.io/en/stable/user/announcements.html#jupyter-news "Link to this heading")

The news are fetched from a news feed. The URL can be customized to point to any [Atom feed](https://www.rfc-editor.org/rfc/rfc5023)
 using the command line option `--LabApp.news_url="<URL_TO_FEED_XML_FILE>"`.

Note

An entry in a custom feed is required to have the following tags: `title`, `id`, and `updated`. The following tags are also used but not required: `published`, `summary`, and at least one `link`.

Binder[#](https://jupyterlab.readthedocs.io/en/stable/user/announcements.html#binder "Link to this heading")

-------------------------------------------------------------------------------------------------------------

You will find how to deactivate those features on Binder at [JupyterLab on Binder](https://jupyterlab.readthedocs.io/en/stable/user/binder.html#binder)
.

On this page

[Edit on GitHub](https://github.com/jupyterlab/jupyterlab/edit/4.6.x/docs/source/user/announcements.md)

[Show Source](https://jupyterlab.readthedocs.io/en/stable/_sources/user/announcements.md.txt)