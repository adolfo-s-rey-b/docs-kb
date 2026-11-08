[Skip to main content](https://jupyterlab.readthedocs.io/en/stable/user/export.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [![jupyter.org](https://jupyterlab.readthedocs.io/en/stable/_static/jupyter_logo.svg)](https://jupyter.org/)
    
*   [GitHub](https://github.com/jupyterlab/jupyterlab)
    
*   [Discourse](https://discourse.jupyter.org/c/jupyterlab/17)
    
*   [Zulip](https://jupyter.zulipchat.com/#narrow/channel/469762-jupyterlab)
    

[![Sponsored: Union AI](https://media.ethicalads.io/images/2026/09/REUSABLE_CONTAINERS_240X180.jpg)](https://server.ethicalads.io/proxy/click/11031/01a1b9a4-b110-7cc2-aded-a1f7822010ad/)

[**Scale and accelerate your AI inference.** Reuse containers across tasks on Union.ai. **Drop cold starts**](https://server.ethicalads.io/proxy/click/11031/01a1b9a4-b110-7cc2-aded-a1f7822010ad/)

_[Ad by EthicalAds](https://www.ethicalads.io/?ref=rtd-sidebar)
_   ·   [ℹ️](https://www.ethicalads.io/advertisers/topics/data-science/?ref=rtd-sidebar-buy-ads)

Exporting Notebooks[#](https://jupyterlab.readthedocs.io/en/stable/user/export.html#exporting-notebooks "Link to this heading")

================================================================================================================================

JupyterLab allows you to export your jupyter notebook files (`.ipynb`) into other file formats such as:

*   AsciiDoc `.asciidoc`
    
*   HTML `.html`
    
*   LaTeX `.tex`
    
*   Markdown `.md`
    
*   PDF `.pdf`
    
*   ReStructured Text `.rst`
    
*   Executable Script `.py`
    
*   Reveal.js Slides `.html`
    

To access these options, while a notebook is open, browse the File menu:

![../_images/exporting-menu.png](https://jupyterlab.readthedocs.io/en/stable/_images/exporting-menu.png)

When exporting to HTML, a dialog will prompt you to choose whether to sanitize the HTML output, i.e. escape tags. This sends a `sanitize_html` param to nbconvert.

Note: The exporting options depend on your nbconvert configuration. For more information visit the [official nbconvert documentation](https://nbconvert.readthedocs.io/en/latest/)
.

Reveal.js Slides[#](https://jupyterlab.readthedocs.io/en/stable/user/export.html#reveal-js-slides "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

In order to export your notebooks as [Reveal.js](https://github.com/hakimel/reveal.js)
 slides, follow these steps:

1.  Open a notebook by double clicking it in the [file browser](https://jupyterlab.readthedocs.io/en/stable/user/files.html#working-with-files)
    .
    
2.  Select Property inspector in the [right sidebar](https://jupyterlab.readthedocs.io/en/stable/user/interface.html#right-sidebar)
    .
    
3.  Select the slide type (Slide, Subslide, Fragment, Skip, Notes).
    

![../_images/exporting-slide-type.png](https://jupyterlab.readthedocs.io/en/stable/_images/exporting-slide-type.png)

4.  Activate another cell.
    
5.  Repeat 3 and 4 until you selected the slide type for all of your cells.
    

After completing these steps, browse the file menu and export as described in the [exporting notebooks](https://jupyterlab.readthedocs.io/en/stable/user/export.html#user-export)
 section. A `.html` file that you will be prompted to download.

If you don’t know how to navigate and interact with a Reveal.js presentation, visit the project’s [website](https://github.com/hakimel/reveal.js)
.

On this page

[Edit on GitHub](https://github.com/jupyterlab/jupyterlab/edit/4.6.x/docs/source/user/export.md)

[Show Source](https://jupyterlab.readthedocs.io/en/stable/_sources/user/export.md.txt)