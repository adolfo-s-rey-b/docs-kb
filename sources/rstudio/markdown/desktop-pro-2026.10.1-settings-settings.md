**Documentation Version**

You are viewing version **2026.10.1**. [Verify that this is the latest version](https://docs.posit.co/supported-versions/rstudio.html)
.

Copy for LLM View as Markdown

Settings
========

All of the settings file locations described in this section conform to the [XDG Base Directory Specification](https://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html)
. They are configurable using environment variables:

|     |     |     |     |     |
| --- | --- | --- | --- | --- |    
| User | Windows | `%APPDATA%\RStudio` | `XDG_CONFIG_HOME` | `RSTUDIO_CONFIG_HOME` |
| System | Windows | `%PROGRAMDATA%\RStudio` | `XDG_CONFIG_DIRS` | `RSTUDIO_CONFIG_DIR` |
| User | Unix | `~/.config/rstudio` | `XDG_CONFIG_HOME` | `RSTUDIO_CONFIG_HOME` |
| System | Unix | `/etc/rstudio` | `XDG_CONFIG_DIRS` | `RSTUDIO_CONFIG_DIR` |

Here, and in the rest of this section, “Unix” refers to both Linux and macOS.

In accordance with the _Base Directory Specification_, the XDG environment variables specify the location of the `rstudio` folder. For example, to store system-wide preference configuration in `/var/config/rstudio/rstudio-prefs.json`, you would set the `XDG_CONFIG_DIRS` variable to the value `/var/config`.

If specified, the RStudio variables take precedence over the XDG variables. These variables specify a specific directory (not a base directory). For example, to store system-wide preferences in `/var/config/settings/rstudio-prefs.json`, you would set the `RSTUDIO_CONFIG_DIR` variable to the value `/var/config/settings`.

Back to top