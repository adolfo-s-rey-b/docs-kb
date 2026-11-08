### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/using/android.html "6. Using Python on Android")
     |
*   [previous](https://docs.python.org/3/using/windows.html "4. Using Python on Windows")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python Setup and Usage](https://docs.python.org/3/using/index.html)
     »
*   [5\. Using Python on macOS](https://docs.python.org/3/using/mac.html)
    
*    
    
    |
*   Theme Auto Light Dark |

5\. Using Python on macOS[¶](https://docs.python.org/3/using/mac.html#using-python-on-macos "Link to this heading")

====================================================================================================================

This document aims to give an overview of macOS-specific behavior you should know about to get started with Python on Mac computers. Python on a Mac running macOS is very similar to Python on other Unix-derived platforms, but there are some differences in installation and some features.

There are various ways to obtain and install Python for macOS. Pre-built versions of the most recent versions of Python are available from a number of distributors. Much of this document describes use of the Pythons provided by the CPython release team for download from the [python.org website](https://www.python.org/downloads/)
. See [Alternative distributions](https://docs.python.org/3/using/mac.html#alternative-bundles)
 for some other options.

5.1. Using Python for macOS from `python.org`[¶](https://docs.python.org/3/using/mac.html#using-python-for-macos-from-python-org "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------

### 5.1.1. Installation steps[¶](https://docs.python.org/3/using/mac.html#installation-steps "Link to this heading")

For [current Python versions](https://www.python.org/downloads/)
 (other than those in `security` status), the release team produces a **Python for macOS** installer package for each new release. A list of available installers is provided on the [macOS downloads page](https://www.python.org/downloads/macos/)
. We recommend using the most recent supported Python version where possible. Current installers provide a [universal2 binary](https://en.wikipedia.org/wiki/Universal_binary)
 build of Python which runs natively on all Macs (Apple Silicon and Intel) that are supported by a wide range of macOS versions, currently typically from at least **macOS 10.15 Catalina** on.

The downloaded file is a standard macOS installer package file (`.pkg`). File integrity information (such as checksum, size, and Sigstore signature) for each file is included on the release download page. Installer packages and their contents are signed and notarized with `Python Software Foundation` Apple Developer ID certificates to meet [macOS Gatekeeper requirements](https://support.apple.com/en-us/102445)
.

For a default installation, double-click on the downloaded installer package file. This should launch the standard macOS Installer app and display the first of several installer steps.

![../_images/mac_installer_01_introduction.png](https://docs.python.org/3/_images/mac_installer_01_introduction.png)

Clicking on the **Continue** button brings up the **Read Me** for this installer. Besides other important information, the **Read Me** documents which Python version is going to be installed and on what versions of macOS it is supported. You may need to scroll through to read the whole file. By default, this **Read Me** will also be installed in `/Applications/Python 3.15/` and available to read anytime.

![../_images/mac_installer_02_readme.png](https://docs.python.org/3/_images/mac_installer_02_readme.png)

Clicking on **Continue** proceeds to display the license for Python and for other included software. You will then need to **Agree** to the license terms before proceeding to the next step. This license file will also be installed and available to be read later.

![../_images/mac_installer_03_license.png](https://docs.python.org/3/_images/mac_installer_03_license.png)

After the license terms are accepted, the next step is the **Installation Type** display. For most uses, the standard set of installation operations is appropriate.

![../_images/mac_installer_04_installation_type.png](https://docs.python.org/3/_images/mac_installer_04_installation_type.png)

By pressing the **Customize** button, you can choose to omit or select certain package components of the installer. Click on each package name to see a description of what it installs. For details of the optional free-threaded feature, which is installed by default, see [Installing free-threaded binaries](https://docs.python.org/3/using/mac.html#install-freethreaded-macos)
.

![../_images/mac_installer_05_custom_install.png](https://docs.python.org/3/_images/mac_installer_05_custom_install.png)

In either case, clicking **Install** will begin the install process by asking permission to install new software. A macOS user name with `Administrator` privilege is needed as the installed Python will be available to all users of the Mac.

When the installation is complete, the **Summary** window will appear.

![../_images/mac_installer_06_summary.png](https://docs.python.org/3/_images/mac_installer_06_summary.png)

Double-click on the **Install Certificates.command** icon or file in the `/Applications/Python 3.15/` window to complete the installation.

![../_images/mac_installer_07_applications.png](https://docs.python.org/3/_images/mac_installer_07_applications.png)

This will open a temporary **Terminal** shell window that will use the new Python to download and install SSL root certificates for its use.

![../_images/mac_installer_08_install_certificates.png](https://docs.python.org/3/_images/mac_installer_08_install_certificates.png)

If `Successfully installed certifi` and `update complete` appear in the terminal window, the installation is complete. Close this terminal window and the installer window.

A default install will include:

*   A `Python 3.15` folder in your `Applications` folder. In here you find **IDLE**, the development environment that is a standard part of official Python distributions; and **Python Launcher**, which handles double-clicking Python scripts from the macOS [Finder](https://support.apple.com/en-us/HT201732)
    .
    
*   A framework `/Library/Frameworks/Python.framework`, which includes the Python executable and libraries. The installer adds this location to your shell path. To uninstall Python, you can remove these three things. Symlinks to the Python executable are placed in `/usr/local/bin/`.
    

Note

Recent versions of macOS include a **python3** command in `/usr/bin/python3` that links to a usually older and incomplete version of Python provided by and for use by the Apple development tools, **Xcode** or the **Command Line Tools for Xcode**. You should never modify or attempt to delete this installation, as it is Apple-controlled and is used by Apple-provided or third-party software. If you choose to install a newer Python version from `python.org`, you will have two different but functional Python installations on your computer that can co-exist. The default installer options should ensure that its **python3** will be used instead of the system **python3**.

### 5.1.2. How to run a Python script[¶](https://docs.python.org/3/using/mac.html#how-to-run-a-python-script "Link to this heading")

There are two ways to invoke the Python interpreter. If you are familiar with using a Unix shell in a terminal window, you can invoke `python3.15` or `python3` optionally followed by one or more command line options (described in [Command line and environment](https://docs.python.org/3/using/cmdline.html#using-on-general)
). The Python tutorial also has a useful section on [using Python interactively from a shell](https://docs.python.org/3/tutorial/appendix.html#tut-interac)
.

You can also invoke the interpreter through an integrated development environment. [IDLE — Python editor and shell](https://docs.python.org/3/library/idle.html#idle)
 is a basic editor and interpreter environment which is included with the standard distribution of Python. **IDLE** includes a Help menu that allows you to access Python documentation. If you are completely new to Python, you can read the tutorial introduction in that document.

There are many other editors and IDEs available, see [Editors and IDEs](https://docs.python.org/3/using/editors.html#editors)
 for more information.

To run a Python script file from the terminal window, you can invoke the interpreter with the name of the script file:

> `python3.15` `myscript.py`

To run your script from the Finder, you can either:

*   Drag it to **Python Launcher**.
    
*   Select **Python Launcher** as the default application to open your script (or any `.py` script) through the Finder Info window and double-click it. **Python Launcher** has various preferences to control how your script is launched. Option-dragging allows you to change these for one invocation, or use its `Preferences` menu to change things globally.
    

Be aware that running the script directly from the macOS Finder might produce different results than when running from a terminal window as the script will not be run in the usual shell environment including any setting of environment variables in shell profiles. And, as with any other script or program, be certain of what you are about to run.

5.2. Alternative distributions[¶](https://docs.python.org/3/using/mac.html#alternative-distributions "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------

Besides the standard `python.org` for macOS installer, there are third-party distributions for macOS that may include additional functionality. Some popular distributions and their key features:

[ActivePython](https://www.activestate.com/products/python/)

Installer with multi-platform compatibility, documentation

[Anaconda](https://www.anaconda.com/download/)

Popular scientific modules (such as numpy, scipy, and pandas) and the `conda` package manager.

[Homebrew](https://brew.sh/)

Package manager for macOS including multiple versions of Python and many third-party Python-based packages (including numpy, scipy, and pandas).

[MacPorts](https://www.macports.org/)

Another package manager for macOS including multiple versions of Python and many third-party Python-based packages. May include pre-built versions of Python and many packages for older versions of macOS.

Note that distributions might not include the latest versions of Python or other libraries, and are not maintained or supported by the core Python team.

5.3. Installing additional Python packages[¶](https://docs.python.org/3/using/mac.html#installing-additional-python-packages "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------

Refer to the [Python Packaging User Guide](https://packaging.python.org/en/latest/tutorials/installing-packages/)
 for more information.

5.4. GUI programming[¶](https://docs.python.org/3/using/mac.html#gui-programming "Link to this heading")

---------------------------------------------------------------------------------------------------------

There are several options for building GUI applications on the Mac with Python.

The standard Python GUI toolkit is [`tkinter`](https://docs.python.org/3/library/tkinter.html#module-tkinter "tkinter: Interface to Tcl/Tk for graphical user interfaces")
, based on the cross-platform Tk toolkit ([https://www.tcl.tk](https://www.tcl.tk/)
). A macOS-native version of Tk is included with the installer.

_PyObjC_ is a Python binding to Apple’s Objective-C/Cocoa framework. Information on PyObjC is available from [pyobjc](https://pypi.org/project/pyobjc/)
.

A number of alternative macOS GUI toolkits are available including:

*   [PySide](https://www.qt.io/qt-for-python)
    : Official Python bindings to the [Qt GUI toolkit](https://wiki.qt.io/Qt_for_Python)
    .
    
*   [PyQt](https://riverbankcomputing.com/software/pyqt/)
    : Alternative Python bindings to Qt.
    
*   [Kivy](https://kivy.org/)
    : A cross-platform GUI toolkit that supports desktop and mobile platforms.
    
*   [Toga](https://toga.readthedocs.io/)
    : Part of the [BeeWare Project](https://beeware.org/)
    ; supports desktop, mobile, web and console apps.
    
*   [wxPython](https://wxpython.org/)
    : A cross-platform toolkit that supports desktop operating systems.
    
*   [Flet](https://flet.dev/)
    : A framework for building cross-platform desktop, mobile, and web applications in Python.
    

5.5. Advanced topics[¶](https://docs.python.org/3/using/mac.html#advanced-topics "Link to this heading")

---------------------------------------------------------------------------------------------------------

### 5.5.1. Installing free-threaded binaries[¶](https://docs.python.org/3/using/mac.html#installing-free-threaded-binaries "Link to this heading")

Added in version 3.13.

Changed in version 3.15: Free-threading support is now installed by default.

The `python.org` [Python for macOS](https://docs.python.org/3/using/mac.html#getting-and-installing-macpython)
 installer package installs, by default, an additional build of Python 3.15 that supports [free threading](https://docs.python.org/3/glossary.html#term-free-threading)
 (running with the [global interpreter lock](https://docs.python.org/3/glossary.html#term-global-interpreter-lock)
 disabled). Check the release page on `python.org` for possible updated information.

The free-threaded mode is working and continues to be improved, but there is some additional overhead in single-threaded workloads compared to the regular build. Additionally, third-party packages, in particular ones with an [extension module](https://docs.python.org/3/glossary.html#term-extension-module)
, may not be ready for use in a free-threaded build, and will re-enable the [GIL](https://docs.python.org/3/glossary.html#term-GIL)
. As of Python 3.15, free-threading support is installed by default. It is packaged as a separate install option, which can be deselected by clicking the **Customize** button on the **Installation Type** step of the installer as described above.

![../_images/mac_installer_09_custom_install_free_threaded.png](https://docs.python.org/3/_images/mac_installer_09_custom_install_free_threaded.png)

If the box next to the **Free-threaded Python** package name is checked (as it is by default), a separate `PythonT.framework` will also be installed alongside the normal `Python.framework` in `/Library/Frameworks`. This configuration allows a free-threaded Python 3.15 build to co-exist on your system with a traditional (GIL only) Python 3.15 build with minimal risk while installing or testing. This installation layout may change in future releases.

Known cautions and limitations:

*   The **UNIX command-line tools** package, which is selected by default, will install links in `/usr/local/bin` for `python3.15t`, the free-threaded interpreter, and `python3.15t-config`, a configuration utility which may be useful for package builders. Since `/usr/local/bin` is typically included in your shell `PATH`, in most cases no changes to your `PATH` environment variable should be needed to use `python3.15t`.
    
*   For this release, the **Shell profile updater** package and the `Update Shell Profile.command` in `/Applications/Python 3.15/` do not support the free-threaded package.
    
*   The free-threaded build and the traditional build have separate search paths and separate `site-packages` directories so, by default, if you need a package available in both builds, it may need to be installed in both. The free-threaded package will install a separate instance of **pip** for use with `python3.15t`.
    
    *   To install a package using **pip** without a **venv**:
        
        python3.15t -m pip install <package\_name>
        
*   When working with multiple Python environments, it is usually safest and easiest to [create and use virtual environments](https://docs.python.org/3/tutorial/venv.html#tut-venv)
    . This can avoid possible command name conflicts and confusion about which Python is in use:
    
    python3.15t -m venv <venv\_name>
    
    then **activate**.
    
*   To run a free-threaded version of IDLE:
    
    python3.15t -m idlelib
    
*   The interpreters in both builds respond to the same [PYTHON environment variables](https://docs.python.org/3/using/cmdline.html#using-on-envvars)
     which may have unexpected results, for example, if you have `PYTHONPATH` set in a shell profile. If necessary, there are [command line options](https://docs.python.org/3/using/cmdline.html#using-on-interface-options)
     like `-E` to ignore these environment variables.
    
*   The free-threaded build links to the third-party shared libraries, such as `OpenSSL` and `Tk`, installed in the traditional framework. This means that both builds also share one set of trust certificates as installed by the **Install Certificates.command** script, thus it only needs to be run once.
    
*   If you cannot depend on the link in `/usr/local/bin` pointing to the `python.org` free-threaded `python3.15t` (for example, if you want to install your own version there or some other distribution does), you can explicitly set your shell `PATH` environment variable to include the `PythonT` framework `bin` directory:
    
    export PATH="/Library/Frameworks/PythonT.framework/Versions/3.15/bin":"$PATH"
    
    The traditional framework installation by default does something similar, except for `Python.framework`. Be aware that having both framework `bin` directories in `PATH` can lead to confusion if there are duplicate names like `python3.15` in both; which one is actually used depends on the order they appear in `PATH`. The `which python3.x` or `which python3.xt` commands can show which path is being used. Using virtual environments can help avoid such ambiguities. Another option might be to create a shell **alias** to the desired interpreter, like:
    
    alias py3.15="/Library/Frameworks/Python.framework/Versions/3.15/bin/python3.15"
    alias py3.15t="/Library/Frameworks/PythonT.framework/Versions/3.15/bin/python3.15t"
    

### 5.5.2. Installing using the command line[¶](https://docs.python.org/3/using/mac.html#installing-using-the-command-line "Link to this heading")

If you want to use automation to install the `python.org` installer package (rather than by using the familiar macOS **Installer** GUI app), the macOS command line **installer** utility lets you select non-default options, too. If you are not familiar with **installer**, it can be somewhat cryptic (see **man installer** for more information). As an example, the following shell snippet shows one way to do it, using the `3.15.0b2` release and deselecting the free-threaded interpreter option:

RELEASE="python-3.15.0b2-macos11.pkg"

# download installer pkg
curl -O https://www.python.org/ftp/python/3.15.0/${RELEASE}

# create installer choicechanges to customize the install:
#    disable the PythonTFramework-3.15 package
#    while accepting the other defaults (install all other packages)
cat > ./choicechanges.plist <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<array>
        <dict>
                <key>attributeSetting</key>
                <integer>0</integer>
                <key>choiceAttribute</key>
                <string>selected</string>
                <key>choiceIdentifier</key>
                <string>org.python.Python.PythonTFramework-3.15</string>
        </dict>
</array>
</plist>
EOF

sudo installer -pkg ./${RELEASE} -applyChoiceChangesXML ./choicechanges.plist -target /

After a default install, you can test that both builds are available with something like:

$ # test that the free-threaded interpreter was installed if the Unix Command Tools package was enabled
$ /usr/local/bin/python3.15t -VV
Python 3.15.0b2 free-threading build (v3.15.0b2:3a83b172af, Jun  5 2024, 12:57:31) \[Clang 15.0.0 (clang-1500.3.9.4)\]
$ #    and the traditional interpreter
$ /usr/local/bin/python3.15 -VV
Python 3.15.0b2 (v3.15.0b2:3a83b172af, Jun  5 2024, 12:50:24) \[Clang 15.0.0 (clang-1500.3.9.4)\]
$ # test that they are also available without the prefix if /usr/local/bin is on $PATH
$ python3.15t -VV
Python 3.15.0b2 free-threading build (v3.15.0b2:3a83b172af, Jun  5 2024, 12:57:31) \[Clang 15.0.0 (clang-1500.3.9.4)\]
$ python3.15 -VV
Python 3.15.0b2 (v3.15.0b2:3a83b172af, Jun  5 2024, 12:50:24) \[Clang 15.0.0 (clang-1500.3.9.4)\]

Note

Current `python.org` installers only install to fixed locations like `/Library/Frameworks/`, `/Applications`, and `/usr/local/bin`. You cannot use the **installer** `-domain` option to install to other locations.

### 5.5.3. Distributing Python applications[¶](https://docs.python.org/3/using/mac.html#distributing-python-applications "Link to this heading")

A range of tools exist for converting your Python code into a standalone distributable application:

*   [py2app](https://pypi.org/project/py2app/)
    : Supports creating macOS `.app` bundles from a Python project.
    
*   [Briefcase](https://briefcase.readthedocs.io/)
    : Part of the [BeeWare Project](https://beeware.org/)
    ; a cross-platform packaging tool that supports creation of `.app` bundles on macOS, as well as managing signing and notarization.
    
*   [PyInstaller](https://pyinstaller.org/)
    : A cross-platform packaging tool that creates a single file or folder as a distributable artifact.
    

### 5.5.4. App Store compliance[¶](https://docs.python.org/3/using/mac.html#app-store-compliance "Link to this heading")

Apps submitted for distribution through the macOS App Store must pass Apple’s app review process. This process includes a set of automated validation rules that inspect the submitted application bundle for problematic code.

The Python standard library contains some code that is known to violate these automated rules. While these violations appear to be false positives, Apple’s review rules cannot be challenged. Therefore, it is necessary to modify the Python standard library for an app to pass App Store review.

The Python source tree contains [a patch file](https://github.com/python/cpython/tree/3.15/Mac/Resources/app-store-compliance.patch)
 that will remove all code that is known to cause issues with the App Store review process. This patch is applied automatically when CPython is configured with the [`--with-app-store-compliance`](https://docs.python.org/3/using/configure.html#cmdoption-with-app-store-compliance)
 option.

This patch is not normally required to use CPython on a Mac; nor is it required if you are distributing an app _outside_ the macOS App Store. It is _only_ required if you are using the macOS App Store as a distribution channel.

5.6. Other resources[¶](https://docs.python.org/3/using/mac.html#other-resources "Link to this heading")

---------------------------------------------------------------------------------------------------------

The [python.org Help page](https://www.python.org/about/help/)
 has links to many useful resources. The [Pythonmac-SIG mailing list](https://www.python.org/community/sigs/current/pythonmac-sig/)
 is another support resource specifically for Python users and developers on the Mac.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [5\. Using Python on macOS](https://docs.python.org/3/using/mac.html#)
    *   [5.1. Using Python for macOS from `python.org`](https://docs.python.org/3/using/mac.html#using-python-for-macos-from-python-org)
        *   [5.1.1. Installation steps](https://docs.python.org/3/using/mac.html#installation-steps)
            
        *   [5.1.2. How to run a Python script](https://docs.python.org/3/using/mac.html#how-to-run-a-python-script)
            
    *   [5.2. Alternative distributions](https://docs.python.org/3/using/mac.html#alternative-distributions)
        
    *   [5.3. Installing additional Python packages](https://docs.python.org/3/using/mac.html#installing-additional-python-packages)
        
    *   [5.4. GUI programming](https://docs.python.org/3/using/mac.html#gui-programming)
        
    *   [5.5. Advanced topics](https://docs.python.org/3/using/mac.html#advanced-topics)
        *   [5.5.1. Installing free-threaded binaries](https://docs.python.org/3/using/mac.html#installing-free-threaded-binaries)
            
        *   [5.5.2. Installing using the command line](https://docs.python.org/3/using/mac.html#installing-using-the-command-line)
            
        *   [5.5.3. Distributing Python applications](https://docs.python.org/3/using/mac.html#distributing-python-applications)
            
        *   [5.5.4. App Store compliance](https://docs.python.org/3/using/mac.html#app-store-compliance)
            
    *   [5.6. Other resources](https://docs.python.org/3/using/mac.html#other-resources)
        

#### Previous topic

[4\. Using Python on Windows](https://docs.python.org/3/using/windows.html "previous chapter")

#### Next topic

[6\. Using Python on Android](https://docs.python.org/3/using/android.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=5.+Using+Python+on+macOS&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fusing%2Fmac.html&pagesource=using%2Fmac.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/using/mac.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/using/android.html "6. Using Python on Android")
     |
*   [previous](https://docs.python.org/3/using/windows.html "4. Using Python on Windows")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python Setup and Usage](https://docs.python.org/3/using/index.html)
     »
*   [5\. Using Python on macOS](https://docs.python.org/3/using/mac.html)
    
*    
    
    |
*   Theme Auto Light Dark |