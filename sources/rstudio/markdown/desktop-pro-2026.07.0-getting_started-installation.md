**Documentation Version**

You are viewing version **2026.07.0**. [Verify that this is the latest version](https://docs.posit.co/supported-versions/rstudio.html)
.

Copy for LLM View as Markdown

Installation[](https://docs.posit.co/ide/desktop-pro/2026.07.0/getting_started/installation.html#installation)

---------------------------------------------------------------------------------------------------------------

Note

The latest version of the installers are available in the [Direct Downloads](https://docs.posit.co/ide/desktop-pro/2026.07.0/getting_started/installation.html#direct-downloads)
 section below.

If you require a different version of RStudio Desktop, you can find previous versions on our [RStudio IDE / Workbench - Previous Versions](https://docs.posit.co/previous-versions/rstudio/)
 page.

### Microsoft Windows[](https://docs.posit.co/ide/desktop-pro/2026.07.0/getting_started/installation.html#microsoft-windows)

RStudio Pro for Windows requires a 64-bit edition of Microsoft Windows 10 or newer.

#### Installer[](https://docs.posit.co/ide/desktop-pro/2026.07.0/getting_started/installation.html#installer)

Download the self-extracting installer (.exe) and execute it. Follow the prompts in the setup wizard. Administrator access is required to complete the installation. The installer will create a shortcut for RStudio and an Add/Remove Programs entry for uninstall.

![](https://docs.posit.co/ide/desktop-pro/2026.07.0/images/setup-wizard.png)

RStudio Windows Setup Welcome Page

#### Zipfile Option[](https://docs.posit.co/ide/desktop-pro/2026.07.0/getting_started/installation.html#zipfile-option)

A zip file may be downloaded instead of the self-extracting installer. Download and extract the .zip to any location. RStudio may then be run directly from that location via `rstudio.exe` (in the `bin` folder).

### Mac[](https://docs.posit.co/ide/desktop-pro/2026.07.0/getting_started/installation.html#mac)

RStudio for Mac requires macOS 14 (Sonoma), or newer. Download the disk image (.dmg) and open it. Drag the RStudio icon to Applications then eject the disk image once complete. To uninstall, move RStudio from where it was installed to the trash.

![](https://docs.posit.co/ide/desktop-pro/2026.07.0/images/mac-image.png)

RStudio Pro Mac Disk Image Contents

#### Apple Silicon (Mac M1/M2)[](https://docs.posit.co/ide/desktop-pro/2026.07.0/getting_started/installation.html#apple-silicon-mac-m1m2)

If you are running RStudio on a Mac with Apple silicon, Rosetta 2 should be installed. RStudio warns you at startup if an existing Rosetta installation cannot be detected.

To install Rosetta 2 manually:

*   Ensure RStudio is closed, then
*   Open a Terminal and run the following command:

    /usr/sbin/softwareupdate --install-rosetta

Once you’ve installed Rosetta, reopen RStudio.

For more information regarding Rosetta 2 on Apple silicon, visit [Apple’s support documentation](https://support.apple.com/en-us/HT211861)
.

### Linux[](https://docs.posit.co/ide/desktop-pro/2026.07.0/getting_started/installation.html#linux)

RStudio produces binary packages targeting the following 64-bit Linux desktop distros. Download the appropriate package and install using system tools.

|     |     |
| --- | --- | 
| Ubuntu 20.04 LTS | deb |
| Ubuntu 22.04 LTS | deb |
| Ubuntu 24.04 LTS | deb |
| RHEL 8 | rpm |
| RHEL 9 | rpm |
| RHEL 10 | rpm |
| OpenSUSE/SLES 15 | rpm |

Linux desktop users may need to import [RStudio’s public code-signing key](https://posit.co/code-signing/)
 prior to installation, depending on the operating system’s security policy.

### Direct Downloads[](https://docs.posit.co/ide/desktop-pro/2026.07.0/getting_started/installation.html#direct-downloads)

Direct download links for RStudio Desktop Pro 2026.07.0, the version this documentation describes:

|     |     |
| --- | --- |
| Windows | [`RStudio-pro-2026.07.0-139.pro9.exe`](https://download1.rstudio.org/electron/windows/RStudio-pro-2026.07.0-139.pro9.exe) |
| Windows (zip archive) | [`RStudio-pro-2026.07.0-139.pro9.zip`](https://download1.rstudio.org/electron/windows/RStudio-pro-2026.07.0-139.pro9.zip) |
| macOS 13+ | [`RStudio-pro-2026.07.0-139.pro9.dmg`](https://download1.rstudio.org/electron/macos/RStudio-pro-2026.07.0-139.pro9.dmg) |
| Ubuntu 22 / 24, Debian 12 / 13 | [`rstudio-pro-2026.07.0-139.pro9-amd64.deb`](https://download1.rstudio.org/electron/jammy/amd64/rstudio-pro-2026.07.0-139.pro9-amd64.deb) |
| RHEL 9 / 10 | [`rstudio-pro-2026.07.0-139.pro9-x86_64.rpm`](https://download1.rstudio.org/electron/rhel9/x86_64/rstudio-pro-2026.07.0-139.pro9-x86_64.rpm) |

Back to top