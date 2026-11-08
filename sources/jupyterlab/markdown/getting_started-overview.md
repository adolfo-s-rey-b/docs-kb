[Skip to main content](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [![jupyter.org](https://jupyterlab.readthedocs.io/en/stable/_static/jupyter_logo.svg)](https://jupyter.org/)
    
*   [GitHub](https://github.com/jupyterlab/jupyterlab)
    
*   [Discourse](https://discourse.jupyter.org/c/jupyterlab/17)
    
*   [Zulip](https://jupyter.zulipchat.com/#narrow/channel/469762-jupyterlab)
    

[![Sponsored: MongoDB](https://media.ethicalads.io/images/2026/07/cropped.png)](https://server.ethicalads.io/proxy/click/10795/01a1b9a4-6141-7413-b391-360b07b1d430/)

[**MongoDB Atlas** is the vector database developers prefer. **Get started building for free.**](https://server.ethicalads.io/proxy/click/10795/01a1b9a4-6141-7413-b391-360b07b1d430/)

_[Ad by EthicalAds](https://www.ethicalads.io/?ref=rtd-sidebar)
_   ·   [ℹ️](https://www.ethicalads.io/advertisers/topics/data-science/?ref=rtd-sidebar-buy-ads)

Get Started[#](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html#get-started "Link to this heading")

=============================================================================================================================

[JupyterLab](https://jupyterlab.readthedocs.io/en/stable/)
 is a next-generation web-based user interface for [Project Jupyter](https://docs.jupyter.org/en/latest/)
.

![JupyterLab showing the file browser, notebook, and several other open files.](https://jupyterlab.readthedocs.io/en/stable/_images/interface-jupyterlab.png)

JupyterLab enables you to work with documents and activities such as [Jupyter notebooks](https://jupyterlab.readthedocs.io/en/stable/user/commands.html#notebook)
, text editors, terminals, and custom components in a flexible, integrated, and extensible manner. For a demonstration of JupyterLab and its features, you can view this video:

You can [arrange](https://jupyterlab.readthedocs.io/en/stable/user/interface.html#interface)
 multiple documents and activities side by side in the work area using tabs and splitters. Documents and activities integrate with each other, enabling new workflows for interactive computing, for example:

*   [Code Consoles](https://jupyterlab.readthedocs.io/en/stable/user/code_console.html#code-console)
     provide transient scratchpads for running code interactively, with full support for rich output. A code console can be linked to a notebook kernel as a computation log from the notebook, for example.
    
*   [Kernel-backed documents](https://jupyterlab.readthedocs.io/en/stable/user/documents_kernels.html#kernel-backed-documents)
     enable code in any text file (Markdown, Python, R, LaTeX, etc.) to be run interactively in any Jupyter kernel.
    
*   Notebook cell outputs can be [mirrored into their own tab](https://jupyterlab.readthedocs.io/en/stable/user/notebook.html#cell-output-mirror)
    , side by side with the notebook, enabling simple dashboards with interactive controls backed by a kernel.
    
*   Multiple views of documents with different editors or viewers enable live editing of documents reflected in other viewers. For example, it is easy to have live preview of [Markdown](https://jupyterlab.readthedocs.io/en/stable/user/file_formats.html#markdown)
    , [CSV](https://jupyterlab.readthedocs.io/en/stable/user/commands.html#csv)
    , or [Vega/Vega-Lite](https://jupyterlab.readthedocs.io/en/stable/user/file_formats.html#vega-lite)
     documents.
    

JupyterLab also offers a unified model for viewing and handling data formats. JupyterLab understands many file formats (images, CSV, JSON, Markdown, PDF, Vega, Vega-Lite, etc.) and can also display rich kernel output in these formats. See [File and Output Formats](https://jupyterlab.readthedocs.io/en/stable/user/file_formats.html#file-and-output-formats)
 for more information.

To navigate the user interface, JupyterLab offers [customizable keyboard shortcuts](https://jupyterlab.readthedocs.io/en/stable/user/commands.html#shortcuts)
.

JupyterLab [extensions](https://jupyterlab.readthedocs.io/en/stable/user/extensions.html#user-extensions)
 can customize or enhance any part of JupyterLab, including new themes, file editors, and custom components.

JupyterLab uses the same [notebook document format](https://nbformat.readthedocs.io/en/latest/)
 as the classic Jupyter Notebook.

What will happen to the Classic Notebook?[#](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html#what-will-happen-to-the-classic-notebook "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

As JupyterLab 4 development continues, and Notebook 7 development follows, Notebook 7 will eventually replace the classic Jupyter Notebook. Throughout this transition, the same notebook document format will be supported by both the classic Notebook, Notebook 7 and JupyterLab. As of JupyterLab 4, the Notebook web application, will no longer be installed alongside JupyterLab as it is no longer a JupyterLab dependency. To find out more about the future of the classic Jupyter Notebook in the ecosystem, visit the [Jupyter Notebook 7 documentation](https://jupyter-notebook.readthedocs.io/en/latest/migrate_to_notebook7.html)
.

*   [Installation](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html)
    *   [conda](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html#conda)
        
    *   [mamba](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html#mamba)
        
    *   [uv](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html#uv)
        
    *   [pip](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html#pip)
        
    *   [pipenv](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html#pipenv)
        
    *   [Docker](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html#docker)
        
    *   [Usage with JupyterHub](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html#usage-with-jupyterhub)
        
    *   [Usage with Jupyverse](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html#usage-with-jupyverse)
        
    *   [Supported browsers](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html#supported-browsers)
        
    *   [Installation problems](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html#installation-problems)
        
*   [Starting JupyterLab](https://jupyterlab.readthedocs.io/en/stable/getting_started/starting.html)
    
*   [Reporting an issue](https://jupyterlab.readthedocs.io/en/stable/getting_started/issue.html)
    *   [Diagnosing an Issue](https://jupyterlab.readthedocs.io/en/stable/getting_started/issue.html#diagnosing-an-issue)
        
    *   [Creating an issue](https://jupyterlab.readthedocs.io/en/stable/getting_started/issue.html#creating-an-issue)
        
*   [Frequently Asked Questions (FAQ)](https://jupyterlab.readthedocs.io/en/stable/getting_started/faq.html)
    *   [General](https://jupyterlab.readthedocs.io/en/stable/getting_started/faq.html#general)
        
    *   [Usage](https://jupyterlab.readthedocs.io/en/stable/getting_started/faq.html#usage)
        
    *   [Tips and Tricks](https://jupyterlab.readthedocs.io/en/stable/getting_started/faq.html#tips-and-tricks)
        
    *   [Development](https://jupyterlab.readthedocs.io/en/stable/getting_started/faq.html#development)
        
    *   [Nightly releases](https://jupyterlab.readthedocs.io/en/stable/getting_started/faq.html#nightly-releases)
        
    *   [OS X Specific Issues](https://jupyterlab.readthedocs.io/en/stable/getting_started/faq.html#os-x-specific-issues)
        
*   [JupyterLab Changelog](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html)
    *   [v4.6](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#v4-6)
        
    *   [v4.5](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#v4-5)
        
    *   [v4.4](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#v4-4)
        
    *   [v4.3](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#v4-3)
        
    *   [v4.2](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#v4-2)
        
    *   [v4.1](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#v4-1)
        
    *   [v4.0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#v4-0)
        
    *   [4.6.6](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id6)
        
    *   [4.6.5](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id7)
        
    *   [4.6.4](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id12)
        
    *   [4.6.3](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id17)
        
    *   [4.6.2](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id22)
        
    *   [4.6.1](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id28)
        
    *   [4.6.0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id34)
        
    *   [4.6.0rc1](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#rc1)
        
    *   [4.6.0rc0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#rc0)
        
    *   [4.6.0b1](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#b1)
        
    *   [4.6.0b0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#b0)
        
    *   [4.6.0a5](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#a5)
        
    *   [4.6.0a4](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#a4)
        
    *   [4.6.0a3](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#a3)
        
    *   [4.6.0a2](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#a2)
        
    *   [4.6.0a1](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#a1)
        
    *   [4.6.0a0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#a0)
        
    *   [4.5.0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id99)
        
    *   [4.5.0rc1](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id106)
        
    *   [4.5.0rc0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id111)
        
    *   [4.5.0b1](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id117)
        
    *   [4.5.0b0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id123)
        
    *   [4.5.0a4](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id128)
        
    *   [4.5.0a3](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id134)
        
    *   [4.5.0a2](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id141)
        
    *   [4.5.0a1](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id147)
        
    *   [4.5.0a0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id153)
        
    *   [4.4.1](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id159)
        
    *   [4.4.0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id163)
        
    *   [4.4.0rc1](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id170)
        
    *   [4.4.0rc0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id174)
        
    *   [4.4.0b2](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#b2)
        
    *   [4.4.0b1](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id184)
        
    *   [4.4.0b0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id190)
        
    *   [4.4.0a3](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id196)
        
    *   [4.4.0a2](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id202)
        
    *   [4.4.0a1](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id209)
        
    *   [4.4.0a0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id216)
        
    *   [4.3.0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id222)
        
    *   [4.3.0rc1](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id229)
        
    *   [4.3.0rc0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id235)
        
    *   [4.3.0b3](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#b3)
        
    *   [4.3.0b2](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id246)
        
    *   [4.3.0b1](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id252)
        
    *   [4.3.0b0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id258)
        
    *   [4.3.0a2](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id264)
        
    *   [4.3.0a1](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id270)
        
    *   [4.3.0a0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id277)
        
    *   [4.2.0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id283)
        
    *   [4.2.0rc0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id288)
        
    *   [4.2.0b3](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id294)
        
    *   [4.2.0b2](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id298)
        
    *   [4.2.0b1](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id304)
        
    *   [4.2.0b0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id311)
        
    *   [4.2.0a2](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id317)
        
    *   [4.2.0a1](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id324)
        
    *   [4.2.0a0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id330)
        
    *   [4.1.2](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id336)
        
    *   [4.1.1](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id341)
        
    *   [4.1.0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id346)
        
    *   [4.1.0rc1](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id354)
        
    *   [4.1.0rc0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id359)
        
    *   [4.1.0b2](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id364)
        
    *   [4.1.0b1](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id367)
        
    *   [4.1.0b0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id373)
        
    *   [4.1.0a4](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id381)
        
    *   [4.1.0a3](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id387)
        
    *   [4.1.0a2](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id394)
        
    *   [4.1.0a1](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id402)
        
    *   [4.0.2](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id408)
        
    *   [4.0.1](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id413)
        
    *   [4.0.0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id419)
        
    *   [4.0.0rc1](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id424)
        
    *   [v3.6](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#v3-6)
        
    *   [v3.5](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#v3-5)
        
    *   [3.5.0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id458)
        
    *   [v3.4](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#v3-4)
        
    *   [3.4.7](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id464)
        
    *   [3.4.6](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id468)
        
    *   [3.4.5](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id473)
        
    *   [3.4.4](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id479)
        
    *   [3.4.3](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id485)
        
    *   [3.4.2](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id492)
        
    *   [3.4.1](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id496)
        
    *   [3.4.0rc0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id501)
        
    *   [3.4.0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id508)
        
    *   [v3.3](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#v3-3)
        
    *   [3.3.4](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id515)
        
    *   [3.3.3](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id521)
        
    *   [3.3.2](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id527)
        
    *   [3.3.1](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id531)
        
    *   [3.3.0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id536)
        
    *   [v3.2](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#v3-2)
        
    *   [3.2.9](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id544)
        
    *   [3.2.8](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id549)
        
    *   [3.2.7](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id552)
        
    *   [3.2.6](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id553)
        
    *   [3.2.5](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id560)
        
    *   [3.2.4](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id565)
        
    *   [3.2.3](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id570)
        
    *   [3.2.2](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id575)
        
    *   [3.2.1](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id580)
        
    *   [3.2.0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id585)
        
    *   [v3.1](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#v3-1)
        
    *   [3.1.19](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id591)
        
    *   [3.1.18](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id595)
        
    *   [3.1.17](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id598)
        
    *   [3.1.16](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id601)
        
    *   [3.1.15](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id605)
        
    *   [3.1.14](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id606)
        
    *   [3.1.13](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id611)
        
    *   [3.1.12](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id618)
        
    *   [3.1.11](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id624)
        
    *   [3.1.10](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id629)
        
    *   [3.1.9](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id634)
        
    *   [3.1.8](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id638)
        
    *   [3.1.7](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id642)
        
    *   [3.1.6](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id647)
        
    *   [3.1.5](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id651)
        
    *   [3.1.2](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id654)
        
    *   [3.1.1](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id659)
        
    *   [3.1.0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#id664)
        
    *   [v3.0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#v3-0)
        
    *   [v2.2.x](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#v2-2-x)
        
    *   [v2.2.0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#v2-2-0)
        
    *   [v2.1.x](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#v2-1-x)
        
    *   [v2.1.0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#v2-1-0)
        
    *   [v2.0.2](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#v2-0-2)
        
    *   [v2.0.0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#v2-0-0)
        
    *   [v1.2.0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#v1-2-0)
        
    *   [v1.1.0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#v1-1-0)
        
    *   [v1.0.0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#v1-0-0)
        
    *   [v0.35.0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#v0-35-0)
        
    *   [v0.34.0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#v0-34-0)
        
    *   [v0.33.0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#v0-33-0)
        
    *   [Beta 2 (v0.32.0)](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#beta-2-v0-32-0)
        
    *   [Beta 1 (v0.31.0)](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#beta-1-v0-31-0)
        
    *   [v0.30.0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#v0-30-0)
        
    *   [v0.29.2](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#v0-29-2)
        
    *   [v0.29.0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#v0-29-0)
        
    *   [v0.28.0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#v0-28-0)
        
    *   [v0.27.0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#v0-27-0)
        
    *   [v0.26.0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#v0-26-0)
        
    *   [v0.25.0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#v0-25-0)
        
    *   [v0.24.0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#v0-24-0)
        
    *   [v0.23.0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#v0-23-0)
        
    *   [v0.22.0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#v0-22-0)
        
    *   [v0.20.0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#v0-20-0)
        
    *   [v0.19.0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#v0-19-0)
        
    *   [v0.18.0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#v0-18-0)
        
    *   [v0.17.0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#v0-17-0)
        
    *   [v0.16.0](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html#v0-16-0)
        
*   [JupyterLab Accessibility Statement](https://jupyterlab.readthedocs.io/en/stable/getting_started/accessibility.html)
    *   [Jupyter Notebook versus JupyterLab](https://jupyterlab.readthedocs.io/en/stable/getting_started/accessibility.html#jupyter-notebook-versus-jupyterlab)
        
    *   [Jupyter audits](https://jupyterlab.readthedocs.io/en/stable/getting_started/accessibility.html#jupyter-audits)
        
    *   [Accessibility Statement for JupyterLab](https://jupyterlab.readthedocs.io/en/stable/getting_started/accessibility.html#accessibility-statement-for-jupyterlab)
        
*   [Version lifecycle](https://jupyterlab.readthedocs.io/en/stable/getting_started/lifecycle.html)
    
*   [Privacy policies](https://jupyterlab.readthedocs.io/en/stable/privacy_policies.html)
    *   [Introduction](https://jupyterlab.readthedocs.io/en/stable/privacy_policies.html#introduction)
        
    *   [What information do we collect?](https://jupyterlab.readthedocs.io/en/stable/privacy_policies.html#what-information-do-we-collect)
        
    *   [Features using external services](https://jupyterlab.readthedocs.io/en/stable/privacy_policies.html#features-using-external-services)
        
    *   [External web services](https://jupyterlab.readthedocs.io/en/stable/privacy_policies.html#external-web-services)
        
    *   [Changes to policy](https://jupyterlab.readthedocs.io/en/stable/privacy_policies.html#changes-to-policy)
        

On this page

[Edit on GitHub](https://github.com/jupyterlab/jupyterlab/edit/4.6.x/docs/source/getting_started/overview.md)

[Show Source](https://jupyterlab.readthedocs.io/en/stable/_sources/getting_started/overview.md.txt)