[Skip to main content](https://jupyterlab.readthedocs.io/en/stable/user/documents_kernels.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [![jupyter.org](https://jupyterlab.readthedocs.io/en/stable/_static/jupyter_logo.svg)](https://jupyter.org/)
    
*   [GitHub](https://github.com/jupyterlab/jupyterlab)
    
*   [Discourse](https://discourse.jupyter.org/c/jupyterlab/17)
    
*   [Zulip](https://jupyter.zulipchat.com/#narrow/channel/469762-jupyterlab)
    

[![Sponsored: MongoDB](https://media.ethicalads.io/images/2026/07/cropped.png)](https://server.ethicalads.io/proxy/click/10795/01a1b9a4-abb2-75c2-9d31-dc413bc905a3/)

[**MongoDB Atlas** is the vector database developers prefer. **Get started building for free.**](https://server.ethicalads.io/proxy/click/10795/01a1b9a4-abb2-75c2-9d31-dc413bc905a3/)

_[Ad by EthicalAds](https://www.ethicalads.io/?ref=rtd-sidebar)
_   ·   [ℹ️](https://www.ethicalads.io/advertisers/topics/data-science/?ref=rtd-sidebar-buy-ads)

Documents and Kernels[#](https://jupyterlab.readthedocs.io/en/stable/user/documents_kernels.html#documents-and-kernels "Link to this heading")

===============================================================================================================================================

In the Jupyter architecture, kernels are separate processes started by the server that run your code in different programming languages and environments. JupyterLab enables you to connect any open text file to a [code console and kernel](https://jupyterlab.readthedocs.io/en/stable/user/code_console.html#code-console)
. This means you can easily run code from the text file in the kernel interactively.

Right-click on a document and select “Create Console for Editor”:

Once the code console is open, send a single line of code or select a block of code and send it to the code console by hitting `Shift Enter`:

In a Markdown document, `Shift Enter` will automatically detect if the cursor is within a code block, and run the entire block if there is no selection:

_Any_ text file (Markdown, Python, R, LaTeX, C++, etc.) in a text file editor can be connected to a code console and kernel in this manner.

Subshell Consoles[#](https://jupyterlab.readthedocs.io/en/stable/user/documents_kernels.html#subshell-consoles "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

For kernels that support subshells (such as Python kernels with ipykernel 7.0.0+), you can create a subshell console to run code concurrently with the main notebook execution.

**Creating a Subshell Console:**

1.  **Command Palette**: Press `Ctrl+Shift+C` (`Cmd+Shift+C` on Mac) and search for “New Subshell Console for Notebook”
    
2.  **Context Menu**: Right-click in a notebook and select “New Subshell Console for Notebook” (only appears if kernel supports subshells)
    

**Verifying Subshell Functionality:**

Use the `%subshell` magic command in Python kernels:

%subshell

Copy to clipboard

This displays:

*   **subshell id**: `None` for main shell, or a unique ID for subshells
    
*   **subshell list**: Array of active subshell IDs
    

**Practical Example:**

1.  In your main notebook, start a long-running computation:
    
    import time
    for i in range(100):
        print(f"Main shell: {i}")
        time.sleep(1)
    
    Copy to clipboard
    
2.  While this runs, create a subshell console and execute:
    
    print("This runs concurrently!")
    %subshell  \# Shows this subshell's ID
    
    Copy to clipboard
    
3.  The subshell executes immediately without waiting for the main shell to finish.
    

**Communication Settings**

Configure how widget communications use subshells via Settings → Advanced Settings → Kernel:

*   `disabled`: No subshells for communications
    
*   `perCommTarget`: One subshell per communication target (default)
    
*   `perComm`: One subshell per communication (can create many subshells)
    

On this page

[Edit on GitHub](https://github.com/jupyterlab/jupyterlab/edit/4.6.x/docs/source/user/documents_kernels.md)

[Show Source](https://jupyterlab.readthedocs.io/en/stable/_sources/user/documents_kernels.md.txt)