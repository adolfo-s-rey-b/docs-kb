### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/using/ios.html "7. Using Python on iOS")
     |
*   [previous](https://docs.python.org/3/using/mac.html "5. Using Python on macOS")
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
*   [6\. Using Python on Android](https://docs.python.org/3/using/android.html)
    
*    
    
    |
*   Theme Auto Light Dark |

6\. Using Python on Android[¶](https://docs.python.org/3/using/android.html#using-python-on-android "Link to this heading")

============================================================================================================================

Python on Android is unlike Python on desktop platforms. On a desktop platform, Python is generally installed as a system resource that can be used by any user of that computer. Users then interact with Python by running a **python** executable and entering commands at an interactive prompt, or by running a Python script.

On Android, there is no concept of installing as a system resource. The only unit of software distribution is an “app”. There is also no console where you could run a **python** executable, or interact with a Python REPL.

As a result, the only way you can use Python on Android is in embedded mode – that is, by writing a native Android application, embedding a Python interpreter using `libpython`, and invoking Python code using the [Python embedding API](https://docs.python.org/3/extending/embedding.html#embedding)
. The full Python interpreter, the standard library, and all your Python code is then packaged into your app for its own private use.

The Python standard library has some notable omissions and restrictions on Android. See the [API availability guide](https://docs.python.org/3/library/intro.html#mobile-availability)
 for details.

6.1. Adding Python to an Android app[¶](https://docs.python.org/3/using/android.html#adding-python-to-an-android-app "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------

Most app developers should use one of the following tools, which will provide a much easier experience:

*   [Briefcase](https://briefcase.beeware.org/)
    , from the BeeWare project
    
*   [Buildozer](https://buildozer.readthedocs.io/)
    , from the Kivy project
    
*   [Chaquopy](https://chaquo.com/chaquopy)
    
*   [Flet](https://flet.dev/)
    
*   [pyqtdeploy](https://www.riverbankcomputing.com/static/Docs/pyqtdeploy/)
    
*   [Termux](https://termux.dev/en/)
    

If you’re sure you want to do all of this manually, read on. You can use the [testbed app](https://github.com/python/cpython/tree/3.15/Platforms/Android/testbed)
 as a guide; each step below contains a link to the relevant file.

*   First, acquire a build of Python for Android:
    
    *   The easiest way is to download an Android release from [python.org](https://www.python.org/downloads/android/)
        . The `prefix` directory mentioned below is at the top level of the package.
        
    *   Or if you want to build it yourself, follow the instructions in [Platforms/Android/README.md](https://github.com/python/cpython/tree/3.15/Platforms/Android/README.md)
        . The `prefix` directory will be created under `cross-build/_HOST_`.
        
*   Add code to your [build.gradle](https://github.com/python/cpython/tree/3.15/Platforms/Android/testbed/app/build.gradle.kts)
     file to copy the following items into your project. All except your own Python code can be copied from `prefix/lib`:
    
    *   In your JNI libraries:
        
        *   `libpython*.*.so`
            
        *   `lib*_python.so` (external libraries such as OpenSSL)
            
    *   In your assets:
        
        *   `python*.*` (the Python standard library)
            
        *   `python*.*/site-packages` (your own Python code)
            
*   Add code to your app to [extract the assets to the filesystem](https://github.com/python/cpython/tree/3.15/Platforms/Android/testbed/app/src/main/java/org/python/testbed/MainActivity.kt)
    .
    
*   Add code to your app to [start Python in embedded mode](https://github.com/python/cpython/tree/3.15/Platforms/Android/testbed/app/src/main/c/main_activity.c)
    . This will need to be C code called via JNI.
    

6.2. Building a Python package for Android[¶](https://docs.python.org/3/using/android.html#building-a-python-package-for-android "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------

Python packages can be built for Android as wheels and released on PyPI. The recommended tool for doing this is [cibuildwheel](https://cibuildwheel.pypa.io/en/stable/platforms/#android)
, which automates all the details of setting up a cross-compilation environment, building the wheel, and testing it on an emulator.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [6\. Using Python on Android](https://docs.python.org/3/using/android.html#)
    *   [6.1. Adding Python to an Android app](https://docs.python.org/3/using/android.html#adding-python-to-an-android-app)
        
    *   [6.2. Building a Python package for Android](https://docs.python.org/3/using/android.html#building-a-python-package-for-android)
        

#### Previous topic

[5\. Using Python on macOS](https://docs.python.org/3/using/mac.html "previous chapter")

#### Next topic

[7\. Using Python on iOS](https://docs.python.org/3/using/ios.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=6.+Using+Python+on+Android&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fusing%2Fandroid.html&pagesource=using%2Fandroid.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/using/android.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/using/ios.html "7. Using Python on iOS")
     |
*   [previous](https://docs.python.org/3/using/mac.html "5. Using Python on macOS")
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
*   [6\. Using Python on Android](https://docs.python.org/3/using/android.html)
    
*    
    
    |
*   Theme Auto Light Dark |