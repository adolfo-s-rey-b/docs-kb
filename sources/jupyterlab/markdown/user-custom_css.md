[Skip to main content](https://jupyterlab.readthedocs.io/en/stable/user/custom_css.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [![jupyter.org](https://jupyterlab.readthedocs.io/en/stable/_static/jupyter_logo.svg)](https://jupyter.org/)
    
*   [GitHub](https://github.com/jupyterlab/jupyterlab)
    
*   [Discourse](https://discourse.jupyter.org/c/jupyterlab/17)
    
*   [Zulip](https://jupyter.zulipchat.com/#narrow/channel/469762-jupyterlab)
    

[![Sponsored: MongoDB](https://media.ethicalads.io/images/2026/07/cropped_99bRLm1.png)](https://server.ethicalads.io/proxy/click/10790/01a1b9a4-98ea-7a22-8623-b88cbe660822/)

[Build smarter search with MongoDB Atlas — your vector database for AI apps. **Start free.**](https://server.ethicalads.io/proxy/click/10790/01a1b9a4-98ea-7a22-8623-b88cbe660822/)

_[Ad by EthicalAds](https://www.ethicalads.io/?ref=rtd-sidebar)
_   ·   [ℹ️](https://www.ethicalads.io/advertisers/topics/data-science/?ref=rtd-sidebar-buy-ads)

Applying Custom CSS[#](https://jupyterlab.readthedocs.io/en/stable/user/custom_css.html#applying-custom-css "Link to this heading")

====================================================================================================================================

To apply custom CSS, you can add a `/custom/custom.css` file in the jupyter `config` directory. You can find the path, `~/.jupyter`, to this directory by running `jupyter --paths`. There you can create a folder named `custom` and create a `custom.css` file within the folder.

Custom CSS is not loaded by default. In the jupyter configuration directory, the `~/.jupyter/custom/custom.css` file will not be loaded unless the the application is initialized with the `--custom-css` flag (`LabApp.custom_css` config).

Jupyter Styling[#](https://jupyterlab.readthedocs.io/en/stable/user/custom_css.html#jupyter-styling "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

You can use a custom CSS file to modify default Jupyter styling.

/\* Modify Jupyter Styles \*/

.lm-BoxPanel-child,
.jp-FileBrowser-Panel,
.lm-StackedPanel-child,
.jp-FileBrowser-toolbar {
  background-color: #aecad4 !important;
}

#top-panel-wrapper,
#jp-top-bar {
  background-color: #aecad4 !important;
}

#menu-panel-wrapper,
#jp-MainMenu,
#menu-panel {
  background-color: #aecad4 !important;
}

.jp-NotebookPanel-toolbar {
  background-color: #aecad4 !important;
}

.lm-MenuBar-content {
  color: #02484d;
}

.lm-TabBar-content,
.jp-DirListing-content,
.lm-MenuBar-content {
  font-size: small;
}

Copy to clipboard

![a screenshot custom jupyter styling](https://jupyterlab.readthedocs.io/en/stable/_images/custom-css-main.png)

Markdown Styling[#](https://jupyterlab.readthedocs.io/en/stable/user/custom_css.html#markdown-styling "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

Another potential application for custom CSS is styling markdown.

/\* Styling Markdown \*/

/\* Headings \*/
h1,
h2 {
  font-family: 'DejaVu Mono', sans-serif;
  font-weight: bold;
  text-shadow: 2px 2px 4px #000;
}

h1 {
  font-size: 22px;
  margin-bottom: 40px;
  color: #10929e;
  text-decoration: underline;
}

h2 {
  font-size: 48px;
  margin-bottom: 32px;
  color: #76b4be;
  text-transform: uppercase;
}

/\* Block Quotes \*/
blockquote {
  font-family: 'DejaVu Mono', serif;
  font-size: 16px;
  color: #19085c;
  border-left: 8px solid #effffc;
  background-color: #eafcff;
  padding: 20px;
}

/\* Lists \*/
ul,
ol {
  font-family: 'DejaVu Mono', sans-serif;
  font-size: 18px;
  color: #333;
  margin-bottom: 24px;
}

Copy to clipboard

![a screenshot of custom markdown styling](https://jupyterlab.readthedocs.io/en/stable/_images/custom-css-notebook-markdown.png)

On this page

[Edit on GitHub](https://github.com/jupyterlab/jupyterlab/edit/4.6.x/docs/source/user/custom_css.md)

[Show Source](https://jupyterlab.readthedocs.io/en/stable/_sources/user/custom_css.md.txt)