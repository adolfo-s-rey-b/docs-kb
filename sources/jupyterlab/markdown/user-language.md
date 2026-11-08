[Skip to main content](https://jupyterlab.readthedocs.io/en/stable/user/language.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [![jupyter.org](https://jupyterlab.readthedocs.io/en/stable/_static/jupyter_logo.svg)](https://jupyter.org/)
    
*   [GitHub](https://github.com/jupyterlab/jupyterlab)
    
*   [Discourse](https://discourse.jupyter.org/c/jupyterlab/17)
    
*   [Zulip](https://jupyter.zulipchat.com/#narrow/channel/469762-jupyterlab)
    

[![Sponsored: Union AI](https://media.ethicalads.io/images/2026/09/OOM_RETRY_240X180.jpg)](https://server.ethicalads.io/proxy/click/11030/01a1b9a4-fa6a-7ab2-b90d-f9adc4656f8a/)

[**OOM? Retry with more.** Handle OOMs in Python. Retry with more memory on Union.ai. **Sign Up Now**](https://server.ethicalads.io/proxy/click/11030/01a1b9a4-fa6a-7ab2-b90d-f9adc4656f8a/)

_[Ad by EthicalAds](https://www.ethicalads.io/?ref=rtd-sidebar)
_   ·   [ℹ️](https://www.ethicalads.io/advertisers/topics/data-science/?ref=rtd-sidebar-buy-ads)

Localization and language[#](https://jupyterlab.readthedocs.io/en/stable/user/language.html#localization-and-language "Link to this heading")

==============================================================================================================================================

Staring with version 3.0, JupyterLab provides the ability to set the display language of the user interface.

Language packs[#](https://jupyterlab.readthedocs.io/en/stable/user/language.html#language-packs "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

To be able to provide a new display language, you will need to install a language pack.

Visit the [language packs repository](https://github.com/jupyterlab/language-packs/)
 for a list of available packs.

### Installing[#](https://jupyterlab.readthedocs.io/en/stable/user/language.html#installing "Link to this heading")

Language packs are identified by the four letter code of the language and variant they provide. For example, for Simplified Chinese the language pack code is `zh-CN` and you can install it with `conda` or `pip`.

If you use conda with conda-forge packages:

conda install \-c conda-forge jupyterlab-language-pack-zh-CN

Copy to clipboard

If you use Pip:

pip install jupyterlab-language-pack-zh-CN

Copy to clipboard

Changing the display language[#](https://jupyterlab.readthedocs.io/en/stable/user/language.html#changing-the-display-language "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------

To change the interface language, select the Settings menu and then select the desired language in the Language submenu.

The Language submenu will only list any previously installed language packs.

![../_images/language-settings.png](https://jupyterlab.readthedocs.io/en/stable/_images/language-settings.png)

Selecting the new language will prompt for confirmation.

![../_images/language-change.png](https://jupyterlab.readthedocs.io/en/stable/_images/language-change.png)

Once you accept, the browser will refresh and the interface will now be shown, for this example in Simplified Chinese.

![../_images/language-chinese.png](https://jupyterlab.readthedocs.io/en/stable/_images/language-chinese.png)

On this page

[Edit on GitHub](https://github.com/jupyterlab/jupyterlab/edit/4.6.x/docs/source/user/language.md)

[Show Source](https://jupyterlab.readthedocs.io/en/stable/_sources/user/language.md.txt)