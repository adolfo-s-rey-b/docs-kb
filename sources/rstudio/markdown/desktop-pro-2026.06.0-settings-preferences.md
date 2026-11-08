**Documentation Version**

You are viewing version **2026.06.0**. [Verify that this is the latest version](https://docs.posit.co/supported-versions/rstudio.html)
.

Copy for LLM View as Markdown

Preferences[](https://docs.posit.co/ide/desktop-pro/2026.06.0/settings/preferences.html#preferences)

-----------------------------------------------------------------------------------------------------

User preferences set in the RStudio IDE’s _Global Options_ dialog can also be set in the JSON file `rstudio-prefs.json`, located in the settings directory described above.

### Example[](https://docs.posit.co/ide/desktop-pro/2026.06.0/settings/preferences.html#example)

By default, RStudio Server asks to save the workspace after the R session ends, and it always loads the workspace when starting a new session. Some organizations prefer to disable this behavior in order to discourage users from accumulating too much ad-hoc state. To do so, set the following:

_%PROGRAMDATA%\\RStudio\\rstudio-prefs.json_

    {
        "save_workspace": "never",
        "load_workspace": false
    }

### Reference[](https://docs.posit.co/ide/desktop-pro/2026.06.0/settings/preferences.html#reference)

A full list of preferences and their possible values can be found in the [Posit Workbench Administration Guide](https://docs.posit.co/ide/server-pro/reference/session_user_settings.html)
. Ensure that you reference the version of the guide that matches your version of RStudio Desktop Pro, as options can change between versions.

Back to top