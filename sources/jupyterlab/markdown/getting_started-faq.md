[Skip to main content](https://jupyterlab.readthedocs.io/en/stable/getting_started/faq.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [![jupyter.org](https://jupyterlab.readthedocs.io/en/stable/_static/jupyter_logo.svg)](https://jupyter.org/)
    
*   [GitHub](https://github.com/jupyterlab/jupyterlab)
    
*   [Discourse](https://discourse.jupyter.org/c/jupyterlab/17)
    
*   [Zulip](https://jupyter.zulipchat.com/#narrow/channel/469762-jupyterlab)
    

Frequently Asked Questions (FAQ)[#](https://jupyterlab.readthedocs.io/en/stable/getting_started/faq.html#frequently-asked-questions-faq "Link to this heading")

================================================================================================================================================================

Below are some frequently asked questions. Click on a question to be directed to relevant information in our documentation or our GitHub repository.

General[#](https://jupyterlab.readthedocs.io/en/stable/getting_started/faq.html#general "Link to this heading")

----------------------------------------------------------------------------------------------------------------

*   [What is JupyterLab?](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html#overview)
    
*   [What will happen to the classic Jupyter Notebook?](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html#classic)
    
*   [Where is the official online documentation for JupyterLab?](https://jupyterlab.readthedocs.io/)
    
*   [How can you report a bug or issue?](https://jupyterlab.readthedocs.io/en/stable/getting_started/issue.html#issue)
    

Usage[#](https://jupyterlab.readthedocs.io/en/stable/getting_started/faq.html#usage "Link to this heading")

------------------------------------------------------------------------------------------------------------

### Notebook[#](https://jupyterlab.readthedocs.io/en/stable/getting_started/faq.html#notebook "Link to this heading")

My notebook is displaying cell outputs in an [iframe](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe)
. They are reset when scrolling back and forth.

> Since JupyterLab v4, notebook rendering is optimized to display only the cells needed. This has side effects with iframes.
> 
> The current workaround is to set the settings _Notebook_ => _Windowing mode_ to `defer` or `none`. It will negatively impact the performance of JupyterLab when opening long notebooks and/or lots of files.

My notebook injects customized CSS that results in unexpected scrolling issues (e.g. it fails to scroll to the active cell).

> Since JupyterLab v4, notebook rendering is optimized to display only the cells needed. It does not support changing element CSS [margin](https://developer.mozilla.org/en-US/docs/Web/CSS/margin)
>  (in particular for cells).
> 
> The workaround is to prefer injecting customized [padding](https://developer.mozilla.org/en-US/docs/Web/CSS/padding)
>  rather than _margin_. If you can not avoid changing the margins, you can set the settings _Notebook_ => _Windowing mode_ to `defer` or `none`. It will negatively impact the performance of JupyterLab when opening long notebooks and/or lots of files.

### Attributes Sanitization[#](https://jupyterlab.readthedocs.io/en/stable/getting_started/faq.html#attributes-sanitization "Link to this heading")

Why are `id` and `name` attributes removed from Markdown?

> JupyterLab sanitizes these attributes to prevent security risks like DOM clobbering attacks. For more details, see the [DOM Clobbering Prevention](https://cheatsheetseries.owasp.org/cheatsheets/DOM_Clobbering_Prevention_Cheat_Sheet.html)
>  guide. Additionally, see the related security advisory [CVE-2024-43805](https://github.com/jupyterlab/jupyterlab/security/advisories/GHSA-9q39-rmj3-p4r2)
> .
> 
> Workarounds: - Use headings in Markdown cells to create anchor points safely. - Optionally, enable the “Allow named properties” setting in **Settings** -> **Settings Editor** -> **Sanitizer** (not recommended for untrusted sources).

How JupyterLab handles anchor navigation?

> During sanitization, the id attributes of the DOM elements are replaced with `data-jupyter-id` attributes. When resolving an URL, if a fragment exists (e.g. `#my-id`), it will find and scroll to the element with the corresponding `data-jupyter-id`.

Tips and Tricks[#](https://jupyterlab.readthedocs.io/en/stable/getting_started/faq.html#tips-and-tricks "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

*   How do I start JupyterLab with a clean workspace every time?
    

Add `c.ServerApp.default_url = '/lab?reset'` to your `jupyter_server_config.py`. See [How to create a jupyter\_server\_config.py](https://jupyter-server.readthedocs.io/en/latest/users/configuration.html)
 for more information.

Development[#](https://jupyterlab.readthedocs.io/en/stable/getting_started/faq.html#development "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

*   [How can you contribute?](https://github.com/jupyterlab/jupyterlab/blob/4.6.x/CONTRIBUTING.md)
    
*   [How can you extend or customize JupyterLab?](https://jupyterlab.readthedocs.io/en/stable/user/extensions.html#user-extensions)
    
*   In the classic Notebook, I could use custom JavaScript outputted by a cell to programmatically control the Notebook. Can I do the same thing in JupyterLab?
    
    JupyterLab was built to support a wide variety of extensibility, including dynamic behavior based on notebook outputs. To access this extensibility, you should write a custom JupyterLab extension. If you would like trigger some behavior in response to the user executing some code in a notebook, you can output a custom mimetype ([MIME Renderer Plugins](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#mime-renderer-plugins)
    ). We currently don’t allow access to the JupyterLab API from the JavaScript renderer, because this would tie the kernel and the notebook output to JupyterLab and make it hard for other frontends to support it. For more discussion and potential alternative solutions, please see issues [#4623](https://github.com/jupyterlab/jupyterlab/issues/4623)
     and [#5789](https://github.com/jupyterlab/jupyterlab/issues/5789)
    .
    

Nightly releases[#](https://jupyterlab.readthedocs.io/en/stable/getting_started/faq.html#nightly-releases "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

The JupyterLab project does not publish nightly releases to PyPI.

However JupyterLab is built on CI for every commit on the `main` branch, and generates the wheel and source distributions as GitHub Action artifacts. These artifacts can be downloaded and installed locally.

To download the JupyterLab wheels from the latest commits on `main`:

*   Go to [Check Release GitHub Action page](https://github.com/jupyterlab/jupyterlab/actions/workflows/check-release.yml?query=branch%3Amain+is%3Asuccess)
    
*   Click on one of the workflow runs
    
*   Under the “Artifacts” section, click on `jupyterlab-releaser-dist-<build-number>` to download the archive
    
*   Locally, extract the archive
    
*   Install with `python -m pip install ./jupyterlab-x.y.z.whl`
    

Note

Downloading artifacts requires signing in to GitHub.

OS X Specific Issues[#](https://jupyterlab.readthedocs.io/en/stable/getting_started/faq.html#os-x-specific-issues "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------

### Holding down buttons does not produce repeated key press events[#](https://jupyterlab.readthedocs.io/en/stable/getting_started/faq.html#holding-down-buttons-does-not-produce-repeated-key-press-events "Link to this heading")

Recent version of OS X change the default behavior for holding down buttons: instead of giving a repeated key press, a Character Accents Popup occurs. For example, when in vim mode in the editor, holding down any of the navigation keys `h j k l` does not cause repeated movement as it normally does in a desktop terminal application.

To change this behavior _globally_ (including browsers like Safari, Firefox and Google Chrome) enter the following command into a terminal, then log out and back in:

defaults write NSGlobalDomain ApplePressAndHoldEnabled \-bool false

Copy to clipboard

To change this behavior back to standard use the following command, then log out and back in:

defaults write NSGlobalDomain ApplePressAndHoldEnabled \-bool true

Copy to clipboard

On this page

[Edit on GitHub](https://github.com/jupyterlab/jupyterlab/edit/4.6.x/docs/source/getting_started/faq.md)

[Show Source](https://jupyterlab.readthedocs.io/en/stable/_sources/getting_started/faq.md.txt)