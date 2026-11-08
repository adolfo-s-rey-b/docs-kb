### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/using/configure.html "3. Configure Python")
     |
*   [previous](https://docs.python.org/3/using/cmdline.html "1. Command line and environment")
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
*   [2\. Using Python on Unix platforms](https://docs.python.org/3/using/unix.html)
    
*    
    
    |
*   Theme Auto Light Dark |

2\. Using Python on Unix platforms[¶](https://docs.python.org/3/using/unix.html#using-python-on-unix-platforms "Link to this heading")

=======================================================================================================================================

2.1. Getting and installing the latest version of Python[¶](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### 2.1.1. On Linux[¶](https://docs.python.org/3/using/unix.html#on-linux "Link to this heading")

Python comes preinstalled on most Linux distributions, and is available as a package on all others. However there are certain features you might want to use that are not available on your distro’s package. You can compile the latest version of Python from source.

In the event that the latest version of Python doesn’t come preinstalled and isn’t in the repositories as well, you can make packages for your own distro. Have a look at the following links:

See also

[https://www.debian.org/doc/manuals/maint-guide/first.en.html](https://www.debian.org/doc/manuals/maint-guide/first.en.html)

for Debian users

[https://en.opensuse.org/Portal:Packaging](https://en.opensuse.org/Portal:Packaging)

for OpenSuse users

[https://docs.fedoraproject.org/en-US/package-maintainers/Packaging\_Tutorial\_GNU\_Hello/](https://docs.fedoraproject.org/en-US/package-maintainers/Packaging_Tutorial_GNU_Hello/)

for Fedora users

[https://slackbook.org/html/package-management-making-packages.html](https://slackbook.org/html/package-management-making-packages.html)

for Slackware users

#### 2.1.1.1. Installing IDLE[¶](https://docs.python.org/3/using/unix.html#installing-idle "Link to this heading")

In some cases, IDLE might not be included in your Python installation.

*   For Debian and Ubuntu users:
    
    Copy
    
    sudo apt update
    sudo apt install idle
    
*   For Fedora, RHEL, and CentOS users:
    
    Copy
    
    sudo dnf install python3-idle
    
*   For SUSE and OpenSUSE users:
    
    Copy
    
    sudo zypper install python3-idle
    
*   For Alpine Linux users:
    
    Copy
    
    sudo apk add python3-idle
    

### 2.1.2. On FreeBSD and OpenBSD[¶](https://docs.python.org/3/using/unix.html#on-freebsd-and-openbsd "Link to this heading")

*   FreeBSD users, to add the package use:
    
    Copy
    
    pkg install python3
    
*   OpenBSD users, to add the package use:
    
    Copy
    
    pkg\_add \-r python
    
    pkg\_add ftp://ftp.openbsd.org/pub/OpenBSD/4.2/packages/<insert your architecture here>/python-<version>.tgz
    
    For example i386 users get the 2.5.1 version of Python using:
    
    Copy
    
    pkg\_add ftp://ftp.openbsd.org/pub/OpenBSD/4.2/packages/i386/python-2.5.1p2.tgz
    

2.2. Building Python[¶](https://docs.python.org/3/using/unix.html#building-python "Link to this heading")

----------------------------------------------------------------------------------------------------------

See also

If you want to contribute to CPython, refer to the [devguide](https://devguide.python.org/getting-started/setup-building/)
, which includes build instructions and other tips on setting up environment.

If you want to compile CPython yourself, first thing you should do is get the [source](https://www.python.org/downloads/source/)
. You can download either the latest release’s source or grab a fresh [clone](https://devguide.python.org/setup/#get-the-source-code)
. You will also need to install the [build requirements](https://docs.python.org/3/using/configure.html#build-requirements)
.

The build process consists of the usual commands:

Copy

./configure
make
make install

[Configuration options](https://docs.python.org/3/using/configure.html#configure-options)
 and caveats for specific Unix platforms are extensively documented in the [README.rst](https://github.com/python/cpython/tree/3.15/README.rst)
 file in the root of the Python source tree.

Warning

`make install` can overwrite or masquerade the `python3` binary. `make altinstall` is therefore recommended instead of `make install` since it only installs `_exec_prefix_/bin/python_version_`.

2.3. Python-related paths and files[¶](https://docs.python.org/3/using/unix.html#python-related-paths-and-files "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

These are subject to difference depending on local installation conventions; [`prefix`](https://docs.python.org/3/using/configure.html#cmdoption-prefix)
 and [`exec_prefix`](https://docs.python.org/3/using/configure.html#cmdoption-exec-prefix)
 are installation-dependent and should be interpreted as for GNU software; they may be the same.

For example, on most Linux systems, the default for both is `/usr`.

| File/directory | Meaning |
| --- | --- |
| `_exec_prefix_/bin/python3` | Recommended location of the interpreter. |
| `_prefix_/lib/python_version_`, `_exec_prefix_/lib/python_version_` | Recommended locations of the directories containing the standard modules. |
| `_prefix_/include/python_version_`, `_exec_prefix_/include/python_version_` | Recommended locations of the directories containing the include files needed for developing Python extensions and embedding the interpreter. |

2.4. Miscellaneous[¶](https://docs.python.org/3/using/unix.html#miscellaneous "Link to this heading")

------------------------------------------------------------------------------------------------------

To easily use Python scripts on Unix, you need to make them executable, e.g. with

Copy

$ chmod +x script

and put an appropriate Shebang line at the top of the script. A good choice is usually

Copy

#!/usr/bin/env python3

which searches for the Python interpreter in the whole `PATH`. However, some Unices may not have the **env** command, so you may need to hardcode `/usr/bin/python3` as the interpreter path.

To use shell commands in your Python scripts, look at the [`subprocess`](https://docs.python.org/3/library/subprocess.html#module-subprocess "subprocess: Subprocess management.")
 module.

2.5. Custom OpenSSL[¶](https://docs.python.org/3/using/unix.html#custom-openssl "Link to this heading")

--------------------------------------------------------------------------------------------------------

1.  To use your vendor’s OpenSSL configuration and system trust store, locate the directory with `openssl.cnf` file or symlink in `/etc`. On most distribution the file is either in `/etc/ssl` or `/etc/pki/tls`. The directory should also contain a `cert.pem` file and/or a `certs` directory.
    
    Copy
    
    $ find /etc/ \-name openssl.cnf \-printf "%h\\n"
    /etc/ssl
    
2.  Download, build, and install OpenSSL. Make sure you use `install_sw` and not `install`. The `install_sw` target does not override `openssl.cnf`.
    
    Copy
    
    $ curl \-O https://www.openssl.org/source/openssl-VERSION.tar.gz
    $ tar xzf openssl-VERSION.tar.gz
    $ pushd openssl-VERSION
    $ ./config \\
        \--prefix\=/usr/local/custom-openssl \\
        \--libdir\=lib \\
        \--openssldir\=/etc/ssl
    $ make \-j1 depend
    $ make \-j8
    $ make install\_sw
    $ popd
    
3.  Build Python with custom OpenSSL (see the configure `--with-openssl` and `--with-openssl-rpath` options)
    
    Copy
    
    $ pushd python-3.x.x
    $ ./configure \-C \\
        \--with-openssl\=/usr/local/custom-openssl \\
        \--with-openssl-rpath\=auto \\
        \--prefix\=/usr/local/python-3.x.x
    $ make \-j8
    $ make altinstall
    

Note

Patch releases of OpenSSL have a backwards compatible ABI. You don’t need to recompile Python to update OpenSSL. It’s sufficient to replace the custom OpenSSL installation with a newer version.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [2\. Using Python on Unix platforms](https://docs.python.org/3/using/unix.html#)
    *   [2.1. Getting and installing the latest version of Python](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)
        *   [2.1.1. On Linux](https://docs.python.org/3/using/unix.html#on-linux)
            *   [2.1.1.1. Installing IDLE](https://docs.python.org/3/using/unix.html#installing-idle)
                
        *   [2.1.2. On FreeBSD and OpenBSD](https://docs.python.org/3/using/unix.html#on-freebsd-and-openbsd)
            
    *   [2.2. Building Python](https://docs.python.org/3/using/unix.html#building-python)
        
    *   [2.3. Python-related paths and files](https://docs.python.org/3/using/unix.html#python-related-paths-and-files)
        
    *   [2.4. Miscellaneous](https://docs.python.org/3/using/unix.html#miscellaneous)
        
    *   [2.5. Custom OpenSSL](https://docs.python.org/3/using/unix.html#custom-openssl)
        

#### Previous topic

[1\. Command line and environment](https://docs.python.org/3/using/cmdline.html "previous chapter")

#### Next topic

[3\. Configure Python](https://docs.python.org/3/using/configure.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=2.+Using+Python+on+Unix+platforms&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fusing%2Funix.html&pagesource=using%2Funix.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/using/unix.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/using/configure.html "3. Configure Python")
     |
*   [previous](https://docs.python.org/3/using/cmdline.html "1. Command line and environment")
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
*   [2\. Using Python on Unix platforms](https://docs.python.org/3/using/unix.html)
    
*    
    
    |
*   Theme Auto Light Dark |