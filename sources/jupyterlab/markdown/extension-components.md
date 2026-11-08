[Skip to main content](https://jupyterlab.readthedocs.io/en/stable/extension/components.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [![jupyter.org](https://jupyterlab.readthedocs.io/en/stable/_static/jupyter_logo.svg)](https://jupyter.org/)
    
*   [GitHub](https://github.com/jupyterlab/jupyterlab)
    
*   [Discourse](https://discourse.jupyter.org/c/jupyterlab/17)
    
*   [Zulip](https://jupyter.zulipchat.com/#narrow/channel/469762-jupyterlab)
    

[![Sponsored: Union AI](https://media.ethicalads.io/images/2026/09/ENVIRONMENTS_240X180.jpg)](https://server.ethicalads.io/proxy/click/11029/01a1b9a3-faf9-7cf1-bab4-339fac49aadf/)

[**Accelerate your agentic workflows.** Set dependencies and environment in Python with Union.ai. **Try free.**](https://server.ethicalads.io/proxy/click/11029/01a1b9a3-faf9-7cf1-bab4-339fac49aadf/)

_[Ad by EthicalAds](https://www.ethicalads.io/?ref=rtd-sidebar)
_   ·   [ℹ️](https://www.ethicalads.io/advertisers/topics/data-science/?ref=rtd-sidebar-buy-ads)

Using JupyterLab components[#](https://jupyterlab.readthedocs.io/en/stable/extension/components.html#using-jupyterlab-components "Link to this heading")

=========================================================================================================================================================

JupyterLab is built with many re-usable components that are independently [published on npm](https://www.npmjs.com/search?q=%40jupyterlab)
. JupyterLab itself assembles these components together to provide a full, IDE-like experience. However, developers are encouraged to use these to bring to life their own visions of what a computational environment should look like.

The JupyterLab repository has [many examples](https://github.com/jupyterlab/jupyterlab/tree/4.6.x/examples)
 to get you started.

The `examples` directory contains:

*   several stand-alone examples (`console`, `filebrowser`, `notebook`, `terminal`)
    
*   a more complex example (`app`).
    

Installation instructions for the examples are found in the project’s README.

After installing the jupyter notebook server 4.2+, follow the steps for installing the development version of JupyterLab. To build the examples, enter from the `jupyterlab` repo root directory:

jlpm build:examples

Copy to clipboard

To run a particular example, navigate to the example’s subdirectory in the `examples` directory and enter:

python main.py

Copy to clipboard

Dissecting the ‘filebrowser’ example[#](https://jupyterlab.readthedocs.io/en/stable/extension/components.html#dissecting-the-filebrowser-example "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The filebrowser example provides a stand-alone implementation of a filebrowser. Here’s what the filebrowser’s user interface looks like:

![filebrowser user interface](https://jupyterlab.readthedocs.io/en/stable/_images/filebrowser_example.png)

Let’s take a closer look at the source code in `examples/filebrowser`.

### Directory structure of ‘filebrowser’ example[#](https://jupyterlab.readthedocs.io/en/stable/extension/components.html#directory-structure-of-filebrowser-example "Link to this heading")

The filebrowser in `examples/filebrowser` is comprised by a handful of files and the `src` directory:

![filebrowser source code](https://jupyterlab.readthedocs.io/en/stable/_images/filebrowser_source.png)

The filebrowser example has two key source files:

*   `src/index.ts`: the TypeScript file that defines the functionality
    
*   `main.py`: the Python file that enables the example to be run
    

Reviewing the source code of each file will help you see the role that each file plays in the stand-alone filebrowser example.

On this page

[Edit on GitHub](https://github.com/jupyterlab/jupyterlab/edit/4.6.x/docs/source/extension/components.md)

[Show Source](https://jupyterlab.readthedocs.io/en/stable/_sources/extension/components.md.txt)