[Skip to main content](https://jupyterlab.readthedocs.io/en/stable/user/completer.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [![jupyter.org](https://jupyterlab.readthedocs.io/en/stable/_static/jupyter_logo.svg)](https://jupyter.org/)
    
*   [GitHub](https://github.com/jupyterlab/jupyterlab)
    
*   [Discourse](https://discourse.jupyter.org/c/jupyterlab/17)
    
*   [Zulip](https://jupyter.zulipchat.com/#narrow/channel/469762-jupyterlab)
    

[![Sponsored: Union AI](https://media.ethicalads.io/images/2026/09/ENVIRONMENTS_240X180.jpg)](https://server.ethicalads.io/proxy/click/11029/01a1b9a4-92bc-7903-a938-dd8f00452ca1/)

[**Accelerate your agentic workflows.** Set dependencies and environment in Python with Union.ai. **Try free.**](https://server.ethicalads.io/proxy/click/11029/01a1b9a4-92bc-7903-a938-dd8f00452ca1/)

_[Ad by EthicalAds](https://www.ethicalads.io/?ref=rtd-sidebar)
_   ·   [ℹ️](https://www.ethicalads.io/advertisers/topics/data-science/?ref=rtd-sidebar-buy-ads)

Completer[#](https://jupyterlab.readthedocs.io/en/stable/user/completer.html#completer "Link to this heading")

===============================================================================================================

Two completer implementations are available in JupyterLab: code completer for tab-completion, and inline completer for inline (as-you-type) suggestions.

Both the code completer and inline completer can present completions from third-party providers when extensions with relevant (inline) completion providers are installed.

Code completer widget[#](https://jupyterlab.readthedocs.io/en/stable/user/completer.html#code-completer-widget "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

The code completer widget can be activated by pressing Tab in a non-empty line of a code cell.

![The completer widget listing the two functions starting with the typed prefix, with the first candidate selected.](https://jupyterlab.readthedocs.io/en/stable/_images/completer-widget.png)

To cycle completion candidates use:

*   Up/Down arrow keys or Tab/Shift + Tab for cycling one item at a time
    
*   Page Up/Page Down keys for jumping over multiple items at once
    

To accept the active completion candidate pressing Enter, or click on it with your mouse/pointer.

By default the completions will include the symbols (“tokens”) from the current editor (“context”), and any suggestions returned by the active kernel in response to `complete_request` message. You may be able to improve the relevance of completion suggestions by adjusting the configuration of the kernel of your choice.

### Automatic completion[#](https://jupyterlab.readthedocs.io/en/stable/user/completer.html#automatic-completion "Link to this heading")

By default the completer only shows up when invoked with Tab. To have it open on its own as you type, enable the **Enable autocompletion** setting in the **Code Completion** section of the Settings Editor (_Settings > Settings Editor > Code Completion_):

![The Enable autocompletion checkbox highlighted among the settings of the Code Completion section of the Settings Editor.](https://jupyterlab.readthedocs.io/en/stable/_images/completer-settings.png)

Once enabled, the completer is invoked after each character of a word that you type, as long as it is not already open. It is not invoked when deleting text, nor in documents which do not contain code, such as Markdown files.

The other settings of this section allow you to:

*   **Completion providers rank setting**: order the providers, the suggestions of the providers with a higher rank being shown first; a negative rank disables the provider
    
*   **Default timeout for a provider**: ignore the results of a provider which takes longer than the given number of milliseconds to answer
    
*   **Show the documentation panel**: see [Documentation panel](https://jupyterlab.readthedocs.io/en/stable/user/completer.html#documentation-panel)
     below
    
*   **Suppress when the inline completer is active**: avoid showing both completers at once by hiding the code completer while an inline suggestion is presented
    

### Documentation panel[#](https://jupyterlab.readthedocs.io/en/stable/user/completer.html#documentation-panel "Link to this heading")

The documentation panel presents additional information about the completion candidate. It can be enabled in Code Completer settings. By default this panel sends `inspect_request` to the active kernel and is therefore only available in notebooks and other documents with active session connected to a kernel that supports inspections.

![The completer widget with the documentation panel showing the signature and the docstring of the selected candidate.](https://jupyterlab.readthedocs.io/en/stable/_images/completer-documentation-panel.png)

Inline completer[#](https://jupyterlab.readthedocs.io/en/stable/user/completer.html#inline-completer "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------

JupyterLab 4.1+ includes an experimental inline completer, showing the suggestions as greyed out “ghost” text. Compared to the completer widget, the inline completer:

*   can present multi-line completions
    
*   is automatically invoked as you type
    
*   does not offer additional information such as type of documentation for the suggestions
    
*   can provide completions in both code and markdown cells (the default history provider only suggests in code cells)
    

![A line of code completed with greyed out ghost text taken from a previously executed cell.](https://jupyterlab.readthedocs.io/en/stable/_images/inline-completer-ghost-text.png)

The inline completer is disabled by default and can be enabled in the Settings Editor by enabling the History Provider.

### Enabling a provider[#](https://jupyterlab.readthedocs.io/en/stable/user/completer.html#enabling-a-provider "Link to this heading")

Inline suggestions come from inline completion providers. JupyterLab ships with a single provider, the **History provider**, which suggests the lines you previously executed in the kernel. Extensions can contribute others, for example [jupyterlite-ai](https://github.com/jupyterlite/ai)
 adds a provider which completes the code you are writing with an AI model of your choice.

Each provider has its own section in the **Inline Completer** settings (_Settings > Settings Editor > Inline Completer_), where the **Enabled** checkbox turns it on:

![The settings of the History provider in the Settings Editor, with its Enabled checkbox highlighted.](https://jupyterlab.readthedocs.io/en/stable/_images/inline-completer-settings.png)

The remaining settings of a provider control how often it is queried (**Debouncer delay**), how long to wait for its suggestions (**Timeout**), and whether it should also complete in the middle of a line (**Fill in middle on typing**).

### Accepting and cycling suggestions[#](https://jupyterlab.readthedocs.io/en/stable/user/completer.html#accepting-and-cycling-suggestions "Link to this heading")

The inline completer widget shows how many suggestions are available, and the shortcuts to browse them. By default it appears when hovering over the ghost text; set **Show widget** to _Always_ to keep it visible, or to _Never_ to hide it.

![The inline completer widget showing the number of suggestions and the shortcuts to cycle and accept them.](https://jupyterlab.readthedocs.io/en/stable/_images/inline-completer-widget.png)

The default shortcuts are:

*   Alt + \[ and Alt + \] to cycle between the suggestions
    
*   Tab or Alt + End to accept the current suggestion
    
*   Alt + \\ to request a suggestion explicitly
    

### Appearance[#](https://jupyterlab.readthedocs.io/en/stable/user/completer.html#appearance "Link to this heading")

The appearance of the ghost text is customizable. In the Settings Editor, under the **Inline Completer** section, enable the **Syntax Highlighting for Ghost Text** setting to apply the language’s syntax highlighting to suggestions, improving readability over the default gray text.

The editor can jump around while suggestions of different lengths come and go. The **Reserve lines for inline completion**, **Limit inline completion lines**, **Reserve space for the longest candidate** and **Editor resize delay** settings of the same section keep the editor height stable.

On this page

[Edit on GitHub](https://github.com/jupyterlab/jupyterlab/edit/4.6.x/docs/source/user/completer.md)

[Show Source](https://jupyterlab.readthedocs.io/en/stable/_sources/user/completer.md.txt)