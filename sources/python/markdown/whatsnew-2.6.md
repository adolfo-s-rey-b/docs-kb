### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/whatsnew/2.5.html "What’s New in Python 2.5")
     |
*   [previous](https://docs.python.org/3/whatsnew/2.7.html "What’s New in Python 2.7")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [What’s New in Python](https://docs.python.org/3/whatsnew/index.html)
     »
*   [What’s New in Python 2.6](https://docs.python.org/3/whatsnew/2.6.html)
    
*    
    
    |
*   Theme Auto Light Dark |

What’s New in Python 2.6[¶](https://docs.python.org/3/whatsnew/2.6.html#what-s-new-in-python-2-6 "Link to this heading")

=========================================================================================================================

Author:

A.M. Kuchling (amk at amk.ca)

This article explains the new features in Python 2.6, released on October 1, 2008. The release schedule is described in [**PEP 361**](https://peps.python.org/pep-0361/)
.

The major theme of Python 2.6 is preparing the migration path to Python 3.0, a major redesign of the language. Whenever possible, Python 2.6 incorporates new features and syntax from 3.0 while remaining compatible with existing code by not removing older features or syntax. When it’s not possible to do that, Python 2.6 tries to do what it can, adding compatibility functions in a `future_builtins` module and a `-3` switch to warn about usages that will become unsupported in 3.0.

Some significant new packages have been added to the standard library, such as the [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing "multiprocessing: Process-based parallelism.")
 and [`json`](https://docs.python.org/3/library/json.html#module-json "json: Encode and decode the JSON format.")
 modules, but there aren’t many new features that aren’t related to Python 3.0 in some way.

Python 2.6 also sees a number of improvements and bugfixes throughout the source. A search through the change logs finds there were 259 patches applied and 612 bugs fixed between Python 2.5 and 2.6. Both figures are likely to be underestimates.

This article doesn’t attempt to provide a complete specification of the new features, but instead provides a convenient overview. For full details, you should refer to the documentation for Python 2.6. If you want to understand the rationale for the design and implementation, refer to the PEP for a particular new feature. Whenever possible, “What’s New in Python” links to the bug/patch item for each change.

Python 3.0[¶](https://docs.python.org/3/whatsnew/2.6.html#python-3-0 "Link to this heading")

---------------------------------------------------------------------------------------------

The development cycle for Python versions 2.6 and 3.0 was synchronized, with the alpha and beta releases for both versions being made on the same days. The development of 3.0 has influenced many features in 2.6.

Python 3.0 is a far-ranging redesign of Python that breaks compatibility with the 2.x series. This means that existing Python code will need some conversion in order to run on Python 3.0. However, not all the changes in 3.0 necessarily break compatibility. In cases where new features won’t cause existing code to break, they’ve been backported to 2.6 and are described in this document in the appropriate place. Some of the 3.0-derived features are:

*   A [`__complex__()`](https://docs.python.org/3/reference/datamodel.html#object.__complex__ "object.__complex__")
     method for converting objects to a complex number.
    
*   Alternate syntax for catching exceptions: `except TypeError as exc`.
    
*   The addition of [`functools.reduce()`](https://docs.python.org/3/library/functools.html#functools.reduce "functools.reduce")
     as a synonym for the built-in `reduce()` function.
    

Python 3.0 adds several new built-in functions and changes the semantics of some existing builtins. Functions that are new in 3.0 such as [`bin()`](https://docs.python.org/3/builtins/functions.html#bin "bin")
 have simply been added to Python 2.6, but existing builtins haven’t been changed; instead, the `future_builtins` module has versions with the new 3.0 semantics. Code written to be compatible with 3.0 can do `from future_builtins import hex, map` as necessary.

A new command-line switch, `-3`, enables warnings about features that will be removed in Python 3.0. You can run code with this switch to see how much work will be necessary to port code to 3.0. The value of this switch is available to Python code as the boolean variable `sys.py3kwarning`, and to C extension code as `Py_Py3kWarningFlag`.

See also

The 3_xxx_ series of PEPs, which contains proposals for Python 3.0. [**PEP 3000**](https://peps.python.org/pep-3000/)
 describes the development process for Python 3.0. Start with [**PEP 3100**](https://peps.python.org/pep-3100/)
 that describes the general goals for Python 3.0, and then explore the higher-numbered PEPs that propose specific features.

Changes to the Development Process[¶](https://docs.python.org/3/whatsnew/2.6.html#changes-to-the-development-process "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------

While 2.6 was being developed, the Python development process underwent two significant changes: we switched from SourceForge’s issue tracker to a customized Roundup installation, and the documentation was converted from LaTeX to reStructuredText.

### New Issue Tracker: Roundup[¶](https://docs.python.org/3/whatsnew/2.6.html#new-issue-tracker-roundup "Link to this heading")

For a long time, the Python developers had been growing increasingly annoyed by SourceForge’s bug tracker. SourceForge’s hosted solution doesn’t permit much customization; for example, it wasn’t possible to customize the life cycle of issues.

The infrastructure committee of the Python Software Foundation therefore posted a call for issue trackers, asking volunteers to set up different products and import some of the bugs and patches from SourceForge. Four different trackers were examined: [Jira](https://www.atlassian.com/software/jira/)
, [Launchpad](https://launchpad.net/)
, [Roundup](https://roundup.sourceforge.io/)
, and [Trac](https://trac.edgewall.org/)
. The committee eventually settled on Jira and Roundup as the two candidates. Jira is a commercial product that offers no-cost hosted instances to free-software projects; Roundup is an open-source project that requires volunteers to administer it and a server to host it.

After posting a call for volunteers, a new Roundup installation was set up at [https://bugs.python.org](https://bugs.python.org/)
. One installation of Roundup can host multiple trackers, and this server now also hosts issue trackers for Jython and for the Python web site. It will surely find other uses in the future. Where possible, this edition of “What’s New in Python” links to the bug/patch item for each change.

Hosting of the Python bug tracker is kindly provided by [Upfront Systems](https://upfrontsoftware.co.za/)
 of Stellenbosch, South Africa. Martin von Löwis put a lot of effort into importing existing bugs and patches from SourceForge; his scripts for this import operation are at `https://svn.python.org/view/tracker/importer/` and may be useful to other projects wishing to move from SourceForge to Roundup.

See also

[https://bugs.python.org](https://bugs.python.org/)

The Python bug tracker.

[https://bugs.jython.org](https://bugs.jython.org/)
:

The Jython bug tracker.

[https://roundup.sourceforge.io/](https://roundup.sourceforge.io/)

Roundup downloads and documentation.

[https://svn.python.org/view/tracker/importer/](https://svn.python.org/view/tracker/importer/)

Martin von Löwis’s conversion scripts.

### New Documentation Format: reStructuredText Using Sphinx[¶](https://docs.python.org/3/whatsnew/2.6.html#new-documentation-format-restructuredtext-using-sphinx "Link to this heading")

The Python documentation was written using LaTeX since the project started around 1989. In the 1980s and early 1990s, most documentation was printed out for later study, not viewed online. LaTeX was widely used because it provided attractive printed output while remaining straightforward to write once the basic rules of the markup were learned.

Today LaTeX is still used for writing publications destined for printing, but the landscape for programming tools has shifted. We no longer print out reams of documentation; instead, we browse through it online and HTML has become the most important format to support. Unfortunately, converting LaTeX to HTML is fairly complicated and Fred L. Drake Jr., the long-time Python documentation editor, spent a lot of time maintaining the conversion process. Occasionally people would suggest converting the documentation into SGML and later XML, but performing a good conversion is a major task and no one ever committed the time required to finish the job.

During the 2.6 development cycle, Georg Brandl put a lot of effort into building a new toolchain for processing the documentation. The resulting package is called Sphinx, and is available from [https://www.sphinx-doc.org/](https://www.sphinx-doc.org/)
.

Sphinx concentrates on HTML output, producing attractively styled and modern HTML; printed output is still supported through conversion to LaTeX. The input format is reStructuredText, a markup syntax supporting custom extensions and directives that is commonly used in the Python community.

Sphinx is a standalone package that can be used for writing, and almost two dozen other projects ([listed on the Sphinx web site](https://www.sphinx-doc.org/en/master/examples.html)
) have adopted Sphinx as their documentation tool.

See also

[Documenting Python](https://devguide.python.org/documenting/)

Describes how to write for Python’s documentation.

[Sphinx](https://www.sphinx-doc.org/)

Documentation and code for the Sphinx toolchain.

[Docutils](https://docutils.sourceforge.io/)

The underlying reStructuredText parser and toolset.

PEP 343: The ‘with’ statement[¶](https://docs.python.org/3/whatsnew/2.6.html#pep-343-the-with-statement "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

The previous version, Python 2.5, added the ‘[`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
’ statement as an optional feature, to be enabled by a `from __future__ import with_statement` directive. In 2.6 the statement no longer needs to be specially enabled; this means that `with` is now always a keyword. The rest of this section is a copy of the corresponding section from the “What’s New in Python 2.5” document; if you’re familiar with the ‘`with`’ statement from Python 2.5, you can skip this section.

The ‘[`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
’ statement clarifies code that previously would use `try...finally` blocks to ensure that clean-up code is executed. In this section, I’ll discuss the statement as it will commonly be used. In the next section, I’ll examine the implementation details and show how to write objects for use with this statement.

The ‘[`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
’ statement is a control-flow structure whose basic structure is:

Copy

with expression \[as variable\]:
    with\-block

The expression is evaluated, and it should result in an object that supports the context management protocol (that is, has [`__enter__()`](https://docs.python.org/3/reference/datamodel.html#object.__enter__ "object.__enter__")
 and [`__exit__()`](https://docs.python.org/3/reference/datamodel.html#object.__exit__ "object.__exit__")
 methods).

The object’s [`__enter__()`](https://docs.python.org/3/reference/datamodel.html#object.__enter__ "object.__enter__")
 is called before _with-block_ is executed and therefore can run set-up code. It also may return a value that is bound to the name _variable_, if given. (Note carefully that _variable_ is _not_ assigned the result of _expression_.)

After execution of the _with-block_ is finished, the object’s [`__exit__()`](https://docs.python.org/3/reference/datamodel.html#object.__exit__ "object.__exit__")
 method is called, even if the block raised an exception, and can therefore run clean-up code.

Some standard Python objects now support the context management protocol and can be used with the ‘[`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
’ statement. File objects are one example:

Copy

with open('/etc/passwd', 'r') as f:
    for line in f:
        print line
        ... more processing code ...

After this statement has executed, the file object in _f_ will have been automatically closed, even if the [`for`](https://docs.python.org/3/reference/compound_stmts.html#for)
 loop raised an exception part-way through the block.

Note

In this case, _f_ is the same object created by [`open()`](https://docs.python.org/3/builtins/functions.html#open "open")
, because [`__enter__()`](https://docs.python.org/3/reference/datamodel.html#object.__enter__ "object.__enter__")
 returns _self_.

The [`threading`](https://docs.python.org/3/library/threading.html#module-threading "threading: Thread-based parallelism.")
 module’s locks and condition variables also support the ‘[`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
’ statement:

Copy

lock \= threading.Lock()
with lock:
    \# Critical section of code
    ...

The lock is acquired before the block is executed and always released once the block is complete.

The [`localcontext()`](https://docs.python.org/3/library/decimal.html#decimal.localcontext "decimal.localcontext")
 function in the [`decimal`](https://docs.python.org/3/library/decimal.html#module-decimal "decimal: Implementation of the General Decimal Arithmetic Specification.")
 module makes it easy to save and restore the current decimal context, which encapsulates the desired precision and rounding characteristics for computations:

Copy

from decimal import Decimal, Context, localcontext

\# Displays with default precision of 28 digits
v \= Decimal('578')
print v.sqrt()

with localcontext(Context(prec\=16)):
    \# All code in this block uses a precision of 16 digits.
    \# The original context is restored on exiting the block.
    print v.sqrt()

### Writing Context Managers[¶](https://docs.python.org/3/whatsnew/2.6.html#writing-context-managers "Link to this heading")

Under the hood, the ‘[`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
’ statement is fairly complicated. Most people will only use ‘`with`’ in company with existing objects and don’t need to know these details, so you can skip the rest of this section if you like. Authors of new objects will need to understand the details of the underlying implementation and should keep reading.

A high-level explanation of the context management protocol is:

*   The expression is evaluated and should result in an object called a “context manager”. The context manager must have [`__enter__()`](https://docs.python.org/3/reference/datamodel.html#object.__enter__ "object.__enter__")
     and [`__exit__()`](https://docs.python.org/3/reference/datamodel.html#object.__exit__ "object.__exit__")
     methods.
    
*   The context manager’s [`__enter__()`](https://docs.python.org/3/reference/datamodel.html#object.__enter__ "object.__enter__")
     method is called. The value returned is assigned to _VAR_. If no `as VAR` clause is present, the value is simply discarded.
    
*   The code in _BLOCK_ is executed.
    
*   If _BLOCK_ raises an exception, the context manager’s [`__exit__()`](https://docs.python.org/3/reference/datamodel.html#object.__exit__ "object.__exit__")
     method is called with three arguments, the exception details (`type, value, traceback`, the same values returned by [`sys.exc_info()`](https://docs.python.org/3/library/sys.html#sys.exc_info "sys.exc_info")
    , which can also be `None` if no exception occurred). The method’s return value controls whether an exception is re-raised: any false value re-raises the exception, and `True` will result in suppressing it. You’ll only rarely want to suppress the exception, because if you do the author of the code containing the ‘[`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
    ’ statement will never realize anything went wrong.
    
*   If _BLOCK_ didn’t raise an exception, the [`__exit__()`](https://docs.python.org/3/reference/datamodel.html#object.__exit__ "object.__exit__")
     method is still called, but _type_, _value_, and _traceback_ are all `None`.
    

Let’s think through an example. I won’t present detailed code but will only sketch the methods necessary for a database that supports transactions.

(For people unfamiliar with database terminology: a set of changes to the database are grouped into a transaction. Transactions can be either committed, meaning that all the changes are written into the database, or rolled back, meaning that the changes are all discarded and the database is unchanged. See any database textbook for more information.)

Let’s assume there’s an object representing a database connection. Our goal will be to let the user write code like this:

Copy

db\_connection \= DatabaseConnection()
with db\_connection as cursor:
    cursor.execute('insert into ...')
    cursor.execute('delete from ...')
    \# ... more operations ...

The transaction should be committed if the code in the block runs flawlessly or rolled back if there’s an exception. Here’s the basic interface for `DatabaseConnection` that I’ll assume:

Copy

class DatabaseConnection:
    \# Database interface
    def cursor(self):
        "Returns a cursor object and starts a new transaction"
    def commit(self):
        "Commits current transaction"
    def rollback(self):
        "Rolls back current transaction"

The [`__enter__()`](https://docs.python.org/3/reference/datamodel.html#object.__enter__ "object.__enter__")
 method is pretty easy, having only to start a new transaction. For this application the resulting cursor object would be a useful result, so the method will return it. The user can then add `as cursor` to their ‘[`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
’ statement to bind the cursor to a variable name.

Copy

class DatabaseConnection:
    ...
    def \_\_enter\_\_(self):
        \# Code to start a new transaction
        cursor \= self.cursor()
        return cursor

The [`__exit__()`](https://docs.python.org/3/reference/datamodel.html#object.__exit__ "object.__exit__")
 method is the most complicated because it’s where most of the work has to be done. The method has to check if an exception occurred. If there was no exception, the transaction is committed. The transaction is rolled back if there was an exception.

In the code below, execution will just fall off the end of the function, returning the default value of `None`. `None` is false, so the exception will be re-raised automatically. If you wished, you could be more explicit and add a [`return`](https://docs.python.org/3/reference/simple_stmts.html#return)
 statement at the marked location.

Copy

class DatabaseConnection:
    ...
    def \_\_exit\_\_(self, type, value, tb):
        if tb is None:
            \# No exception, so commit
            self.commit()
        else:
            \# Exception occurred, so rollback.
            self.rollback()
            \# return False

### The contextlib module[¶](https://docs.python.org/3/whatsnew/2.6.html#the-contextlib-module "Link to this heading")

The [`contextlib`](https://docs.python.org/3/library/contextlib.html#module-contextlib "contextlib: Utilities for with-statement contexts.")
 module provides some functions and a decorator that are useful when writing objects for use with the ‘[`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
’ statement.

The decorator is called [`@contextmanager`](https://docs.python.org/3/library/contextlib.html#contextlib.contextmanager "contextlib.contextmanager")
, and lets you write a single generator function instead of defining a new class. The generator should yield exactly one value. The code up to the [`yield`](https://docs.python.org/3/reference/simple_stmts.html#yield)
 will be executed as the [`__enter__()`](https://docs.python.org/3/reference/datamodel.html#object.__enter__ "object.__enter__")
 method, and the value yielded will be the method’s return value that will get bound to the variable in the ‘[`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
’ statement’s `as` clause, if any. The code after the `yield` will be executed in the [`__exit__()`](https://docs.python.org/3/reference/datamodel.html#object.__exit__ "object.__exit__")
 method. Any exception raised in the block will be raised by the `yield` statement.

Using this decorator, our database example from the previous section could be written as:

Copy

from contextlib import contextmanager

@contextmanager
def db\_transaction(connection):
    cursor \= connection.cursor()
    try:
        yield cursor
    except:
        connection.rollback()
        raise
    else:
        connection.commit()

db \= DatabaseConnection()
with db\_transaction(db) as cursor:
    ...

The [`contextlib`](https://docs.python.org/3/library/contextlib.html#module-contextlib "contextlib: Utilities for with-statement contexts.")
 module also has a `nested(mgr1, mgr2, ...)` function that combines a number of context managers so you don’t need to write nested ‘[`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
’ statements. In this example, the single ‘`with`’ statement both starts a database transaction and acquires a thread lock:

Copy

lock \= threading.Lock()
with nested (db\_transaction(db), lock) as (cursor, locked):
    ...

Finally, the [`closing()`](https://docs.python.org/3/library/contextlib.html#contextlib.closing "contextlib.closing")
 function returns its argument so that it can be bound to a variable, and calls the argument’s `.close()` method at the end of the block.

Copy

import urllib, sys
from contextlib import closing

with closing(urllib.urlopen('http://www.yahoo.com')) as f:
    for line in f:
        sys.stdout.write(line)

See also

[**PEP 343**](https://peps.python.org/pep-0343/)
 - The “with” statement

PEP written by Guido van Rossum and Nick Coghlan; implemented by Mike Bland, Guido van Rossum, and Neal Norwitz. The PEP shows the code generated for a ‘[`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
’ statement, which can be helpful in learning how the statement works.

The documentation for the [`contextlib`](https://docs.python.org/3/library/contextlib.html#module-contextlib "contextlib: Utilities for with-statement contexts.")
 module.

PEP 366: Explicit Relative Imports From a Main Module[¶](https://docs.python.org/3/whatsnew/2.6.html#pep-366-explicit-relative-imports-from-a-main-module "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Python’s [`-m`](https://docs.python.org/3/using/cmdline.html#cmdoption-m)
 switch allows running a module as a script. When you ran a module that was located inside a package, relative imports didn’t work correctly.

The fix for Python 2.6 adds a [`module.__package__`](https://docs.python.org/3/reference/datamodel.html#module.__package__ "module.__package__")
 attribute. When this attribute is present, relative imports will be relative to the value of this attribute instead of the [`__name__`](https://docs.python.org/3/reference/datamodel.html#module.__name__ "module.__name__")
 attribute.

PEP 302-style importers can then set [`__package__`](https://docs.python.org/3/reference/datamodel.html#module.__package__ "module.__package__")
 as necessary. The [`runpy`](https://docs.python.org/3/library/runpy.html#module-runpy "runpy: Locate and run Python modules without importing them first.")
 module that implements the [`-m`](https://docs.python.org/3/using/cmdline.html#cmdoption-m)
 switch now does this, so relative imports will now work correctly in scripts running from inside a package.

PEP 370: Per-user `site-packages` Directory[¶](https://docs.python.org/3/whatsnew/2.6.html#pep-370-per-user-site-packages-directory "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------

When you run Python, the module search path `sys.path` usually includes a directory whose path ends in `"site-packages"`. This directory is intended to hold locally installed packages available to all users using a machine or a particular site installation.

Python 2.6 introduces a convention for user-specific site directories. The directory varies depending on the platform:

*   Unix and Mac OS X: `~/.local/`
    
*   Windows: `%APPDATA%/Python`
    

Within this directory, there will be version-specific subdirectories, such as `lib/python2.6/site-packages` on Unix/Mac OS and `Python26/site-packages` on Windows.

If you don’t like the default directory, it can be overridden by an environment variable. [`PYTHONUSERBASE`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONUSERBASE)
 sets the root directory used for all Python versions supporting this feature. On Windows, the directory for application-specific data can be changed by setting the `APPDATA` environment variable. You can also modify the `site.py` file for your Python installation.

The feature can be disabled entirely by running Python with the [`-s`](https://docs.python.org/3/using/cmdline.html#cmdoption-s)
 option or setting the [`PYTHONNOUSERSITE`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONNOUSERSITE)
 environment variable.

See also

[**PEP 370**](https://peps.python.org/pep-0370/)
 - Per-user `site-packages` Directory

PEP written and implemented by Christian Heimes.

PEP 371: The `multiprocessing` Package[¶](https://docs.python.org/3/whatsnew/2.6.html#pep-371-the-multiprocessing-package "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------

The new [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing "multiprocessing: Process-based parallelism.")
 package lets Python programs create new processes that will perform a computation and return a result to the parent. The parent and child processes can communicate using queues and pipes, synchronize their operations using locks and semaphores, and can share simple arrays of data.

The [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing "multiprocessing: Process-based parallelism.")
 module started out as an exact emulation of the [`threading`](https://docs.python.org/3/library/threading.html#module-threading "threading: Thread-based parallelism.")
 module using processes instead of threads. That goal was discarded along the path to Python 2.6, but the general approach of the module is still similar. The fundamental class is the [`Process`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process "multiprocessing.Process")
, which is passed a callable object and a collection of arguments. The [`start()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.start "multiprocessing.Process.start")
 method sets the callable running in a subprocess, after which you can call the [`is_alive()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.is_alive "multiprocessing.Process.is_alive")
 method to check whether the subprocess is still running and the [`join()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.join "multiprocessing.Process.join")
 method to wait for the process to exit.

Here’s a simple example where the subprocess will calculate a factorial. The function doing the calculation is written strangely so that it takes significantly longer when the input argument is a multiple of 4.

Copy

import time
from multiprocessing import Process, Queue

def factorial(queue, N):
    "Compute a factorial."
    \# If N is a multiple of 4, this function will take much longer.
    if (N % 4) \== 0:
        time.sleep(.05 \* N/4)

    \# Calculate the result
    fact \= 1L
    for i in range(1, N+1):
        fact \= fact \* i

    \# Put the result on the queue
    queue.put(fact)

if \_\_name\_\_ \== '\_\_main\_\_':
    queue \= Queue()

    N \= 5

    p \= Process(target\=factorial, args\=(queue, N))
    p.start()
    p.join()

    result \= queue.get()
    print 'Factorial', N, '=', result

A [`Queue`](https://docs.python.org/3/library/queue.html#queue.Queue "queue.Queue")
 is used to communicate the result of the factorial. The `Queue` object is stored in a global variable. The child process will use the value of the variable when the child was created; because it’s a `Queue`, parent and child can use the object to communicate. (If the parent were to change the value of the global variable, the child’s value would be unaffected, and vice versa.)

Two other classes, [`Pool`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool "multiprocessing.pool.Pool")
 and [`Manager`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Manager "multiprocessing.Manager")
, provide higher-level interfaces. `Pool` will create a fixed number of worker processes, and requests can then be distributed to the workers by calling [`apply()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.apply "multiprocessing.pool.Pool.apply")
 or [`apply_async()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.apply_async "multiprocessing.pool.Pool.apply_async")
 to add a single request, and [`map()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.map "multiprocessing.pool.Pool.map")
 or [`map_async()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.map_async "multiprocessing.pool.Pool.map_async")
 to add a number of requests. The following code uses a `Pool` to spread requests across 5 worker processes and retrieve a list of results:

Copy

from multiprocessing import Pool

def factorial(N, dictionary):
    "Compute a factorial."
    ...
p \= Pool(5)
result \= p.map(factorial, range(1, 1000, 10))
for v in result:
    print v

This produces the following output:

Copy

1
39916800
51090942171709440000
8222838654177922817725562880000000
33452526613163807108170062053440751665152000000000
...

The other high-level interface, the [`Manager`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Manager "multiprocessing.Manager")
 class, creates a separate server process that can hold master copies of Python data structures. Other processes can then access and modify these data structures using proxy objects. The following example creates a shared dictionary by calling the [`dict()`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
 method; the worker processes then insert values into the dictionary. (Locking is not done for you automatically, which doesn’t matter in this example. `Manager`’s methods also include [`Lock()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.SyncManager.Lock "multiprocessing.managers.SyncManager.Lock")
, [`RLock()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.SyncManager.RLock "multiprocessing.managers.SyncManager.RLock")
, and [`Semaphore()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.SyncManager.Semaphore "multiprocessing.managers.SyncManager.Semaphore")
 to create shared locks.)

Copy

import time
from multiprocessing import Pool, Manager

def factorial(N, dictionary):
    "Compute a factorial."
    \# Calculate the result
    fact \= 1L
    for i in range(1, N+1):
        fact \= fact \* i

    \# Store result in dictionary
    dictionary\[N\] \= fact

if \_\_name\_\_ \== '\_\_main\_\_':
    p \= Pool(5)
    mgr \= Manager()
    d \= mgr.dict()         \# Create shared dictionary

    \# Run tasks using the pool
    for N in range(1, 1000, 10):
        p.apply\_async(factorial, (N, d))

    \# Mark pool as closed -- no more tasks can be added.
    p.close()

    \# Wait for tasks to exit
    p.join()

    \# Output results
    for k, v in sorted(d.items()):
        print k, v

This will produce the output:

Copy

1 1
11 39916800
21 51090942171709440000
31 8222838654177922817725562880000000
41 33452526613163807108170062053440751665152000000000
51 15511187532873822802242430164693032110632597200169861120000...

See also

The documentation for the [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing "multiprocessing: Process-based parallelism.")
 module.

[**PEP 371**](https://peps.python.org/pep-0371/)
 - Addition of the multiprocessing package

PEP written by Jesse Noller and Richard Oudkerk; implemented by Richard Oudkerk and Jesse Noller.

PEP 3101: Advanced String Formatting[¶](https://docs.python.org/3/whatsnew/2.6.html#pep-3101-advanced-string-formatting "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------

In Python 3.0, the `%` operator is supplemented by a more powerful string formatting method, [`format()`](https://docs.python.org/3/builtins/functions.html#format "format")
. Support for the [`str.format()`](https://docs.python.org/3/builtins/stdtypes.html#str.format "str.format")
 method has been backported to Python 2.6.

In 2.6, both 8-bit and Unicode strings have a `.format()` method that treats the string as a template and takes the arguments to be formatted. The formatting template uses curly brackets (`{`, `}`) as special characters:

Copy

\>>> \# Substitute positional argument 0 into the string.
\>>> "User ID: {0}".format("root")
'User ID: root'
\>>> \# Use the named keyword arguments
\>>> "User ID: {uid}   Last seen: {last\_login}".format(
...    uid\="root",
...    last\_login \= "5 Mar 2008 07:20")
'User ID: root   Last seen: 5 Mar 2008 07:20'

Curly brackets can be escaped by doubling them:

Copy

\>>> "Empty dict: {{}}".format()
"Empty dict: {}"

Field names can be integers indicating positional arguments, such as `{0}`, `{1}`, etc. or names of keyword arguments. You can also supply compound field names that read attributes or access dictionary keys:

Copy

\>>> import sys
\>>> print 'Platform: {0.platform}\\nPython version: {0.version}'.format(sys)
Platform: darwin
Python version: 2.6a1+ (trunk:61261M, Mar  5 2008, 20:29:41)
\[GCC 4.0.1 (Apple Computer, Inc. build 5367)\]'

\>>> import mimetypes
\>>> 'Content-type: {0\[.mp4\]}'.format(mimetypes.types\_map)
'Content-type: video/mp4'

Note that when using dictionary-style notation such as `[.mp4]`, you don’t need to put any quotation marks around the string; it will look up the value using `.mp4` as the key. Strings beginning with a number will be converted to an integer. You can’t write more complicated expressions inside a format string.

So far we’ve shown how to specify which field to substitute into the resulting string. The precise formatting used is also controllable by adding a colon followed by a format specifier. For example:

Copy

\>>> \# Field 0: left justify, pad to 15 characters
\>>> \# Field 1: right justify, pad to 6 characters
\>>> fmt \= '{0:15} ${1:>6}'
\>>> fmt.format('Registration', 35)
'Registration    $    35'
\>>> fmt.format('Tutorial', 50)
'Tutorial        $    50'
\>>> fmt.format('Banquet', 125)
'Banquet         $   125'

Format specifiers can reference other fields through nesting:

Copy

\>>> fmt \= '{0:{1}}'
\>>> width \= 15
\>>> fmt.format('Invoice #1234', width)
'Invoice #1234  '
\>>> width \= 35
\>>> fmt.format('Invoice #1234', width)
'Invoice #1234                      '

The alignment of a field within the desired width can be specified:

| Character | Effect |
| --- | --- |
| < (default) | Left-align |
| \>  | Right-align |
| ^   | Center |
| \=  | (For numeric types only) Pad after the sign. |

Format specifiers can also include a presentation type, which controls how the value is formatted. For example, floating-point numbers can be formatted as a general number or in exponential notation:

Copy

\>>> '{0:g}'.format(3.75)
'3.75'
\>>> '{0:e}'.format(3.75)
'3.750000e+00'

A variety of presentation types are available. Consult the 2.6 documentation for a [complete list](https://docs.python.org/3/library/string.html#formatstrings)
; here’s a sample:

|     |     |
| --- | --- |
| `b` | Binary. Outputs the number in base 2. |
| `c` | Character. Converts the integer to the corresponding Unicode character before printing. |
| `d` | Decimal Integer. Outputs the number in base 10. |
| `o` | Octal format. Outputs the number in base 8. |
| `x` | Hex format. Outputs the number in base 16, using lower-case letters for the digits above 9. |
| `e` | Exponent notation. Prints the number in scientific notation using the letter ‘e’ to indicate the exponent. |
| `g` | General format. This prints the number as a fixed-point number, unless the number is too large, in which case it switches to ‘e’ exponent notation. |
| `n` | Number. This is the same as ‘g’ (for floats) or ‘d’ (for integers), except that it uses the current locale setting to insert the appropriate number separator characters. |
| `%` | Percentage. Multiplies the number by 100 and displays in fixed (‘f’) format, followed by a percent sign. |

Classes and types can define a [`__format__()`](https://docs.python.org/3/reference/datamodel.html#object.__format__ "object.__format__")
 method to control how they’re formatted. It receives a single argument, the format specifier:

Copy

def \_\_format\_\_(self, format\_spec):
    if isinstance(format\_spec, unicode):
        return unicode(str(self))
    else:
        return str(self)

There’s also a [`format()`](https://docs.python.org/3/builtins/functions.html#format "format")
 builtin that will format a single value. It calls the type’s [`__format__()`](https://docs.python.org/3/reference/datamodel.html#object.__format__ "object.__format__")
 method with the provided specifier:

Copy

\>>> format(75.6564, '.2f')
'75.66'

See also

[Format string syntax](https://docs.python.org/3/library/string.html#formatstrings)

The reference documentation for format fields.

[**PEP 3101**](https://peps.python.org/pep-3101/)
 - Advanced String Formatting

PEP written by Talin. Implemented by Eric Smith.

PEP 3105: `print` As a Function[¶](https://docs.python.org/3/whatsnew/2.6.html#pep-3105-print-as-a-function "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------

The `print` statement becomes the [`print()`](https://docs.python.org/3/builtins/functions.html#print "print")
 function in Python 3.0. Making `print()` a function makes it possible to replace the function by doing `def print(...)` or importing a new function from somewhere else.

Python 2.6 has a `__future__` import that removes `print` as language syntax, letting you use the functional form instead. For example:

Copy

\>>> from \_\_future\_\_ import print\_function
\>>> print('# of entries', len(dictionary), file\=sys.stderr)

The signature of the new function is:

Copy

def print(\*args, sep\=' ', end\='\\n', file\=None)

The parameters are:

*   _args_: positional arguments whose values will be printed out.
    
*   _sep_: the separator, which will be printed between arguments.
    
*   _end_: the ending text, which will be printed after all of the arguments have been output.
    
*   _file_: the file object to which the output will be sent.
    

See also

[**PEP 3105**](https://peps.python.org/pep-3105/)
 - Make print a function

PEP written by Georg Brandl.

PEP 3110: Exception-Handling Changes[¶](https://docs.python.org/3/whatsnew/2.6.html#pep-3110-exception-handling-changes "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------

One error that Python programmers occasionally make is writing the following code:

Copy

try:
    ...
except TypeError, ValueError:  \# Wrong!
    ...

The author is probably trying to catch both [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 and [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 exceptions, but this code actually does something different: it will catch `TypeError` and bind the resulting exception object to the local name `"ValueError"`. The `ValueError` exception will not be caught at all. The correct code specifies a tuple of exceptions:

Copy

try:
    ...
except (TypeError, ValueError):
    ...

This error happens because the use of the comma here is ambiguous: does it indicate two different nodes in the parse tree, or a single node that’s a tuple?

Python 3.0 makes this unambiguous by replacing the comma with the word “as”. To catch an exception and store the exception object in the variable `exc`, you must write:

Copy

try:
    ...
except TypeError as exc:
    ...

Python 3.0 will only support the use of “as”, and therefore interprets the first example as catching two different exceptions. Python 2.6 supports both the comma and “as”, so existing code will continue to work. We therefore suggest using “as” when writing new Python code that will only be executed with 2.6.

See also

[**PEP 3110**](https://peps.python.org/pep-3110/)
 - Catching Exceptions in Python 3000

PEP written and implemented by Collin Winter.

PEP 3112: Byte Literals[¶](https://docs.python.org/3/whatsnew/2.6.html#pep-3112-byte-literals "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

Python 3.0 adopts Unicode as the language’s fundamental string type and denotes 8-bit literals differently, either as `b'string'` or using a [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 constructor. For future compatibility, Python 2.6 adds `bytes` as a synonym for the [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 type, and it also supports the `b''` notation.

The 2.6 [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 differs from 3.0’s [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 type in various ways; most notably, the constructor is completely different. In 3.0, `bytes([65, 66, 67])` is 3 elements long, containing the bytes representing `ABC`; in 2.6, `bytes([65, 66, 67])` returns the 12-byte string representing the [`str()`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 of the list.

The primary use of [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 in 2.6 will be to write tests of object type such as `isinstance(x, bytes)`. This will help the 2to3 converter, which can’t tell whether 2.x code intends strings to contain either characters or 8-bit bytes; you can now use either `bytes` or [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 to represent your intention exactly, and the resulting code will also be correct in Python 3.0.

There’s also a `__future__` import that causes all string literals to become Unicode strings. This means that `\u` escape sequences can be used to include Unicode characters:

Copy

from \_\_future\_\_ import unicode\_literals

s \= ('\\u751f\\u3080\\u304e\\u3000\\u751f\\u3054'
     '\\u3081\\u3000\\u751f\\u305f\\u307e\\u3054')

print len(s)               \# 12 Unicode characters

At the C level, Python 3.0 will rename the existing 8-bit string type, called `PyStringObject` in Python 2.x, to [`PyBytesObject`](https://docs.python.org/3/c-api/bytes.html#c.PyBytesObject "PyBytesObject")
. Python 2.6 uses `#define` to support using the names [`PyBytesObject()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytesObject "PyBytesObject")
, [`PyBytes_Check()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_Check "PyBytes_Check")
, [`PyBytes_FromStringAndSize()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_FromStringAndSize "PyBytes_FromStringAndSize")
, and all the other functions and macros used with strings.

Instances of the [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 type are immutable just as strings are. A new [`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")
 type stores a mutable sequence of bytes:

Copy

\>>> bytearray(\[65, 66, 67\])
bytearray(b'ABC')
\>>> b \= bytearray(u'\\u21ef\\u3244', 'utf-8')
\>>> b
bytearray(b'\\xe2\\x87\\xaf\\xe3\\x89\\x84')
\>>> b\[0\] \= '\\xe3'
\>>> b
bytearray(b'\\xe3\\x87\\xaf\\xe3\\x89\\x84')
\>>> unicode(str(b), 'utf-8')
u'\\u31ef \\u3244'

Byte arrays support most of the methods of string types, such as [`startswith()`](https://docs.python.org/3/builtins/stdtypes.html#bytearray.startswith "bytearray.startswith")
/[`endswith()`](https://docs.python.org/3/builtins/stdtypes.html#bytearray.endswith "bytearray.endswith")
, [`find()`](https://docs.python.org/3/builtins/stdtypes.html#bytearray.find "bytearray.find")
/[`rfind()`](https://docs.python.org/3/builtins/stdtypes.html#bytearray.rfind "bytearray.rfind")
, and some of the methods of lists, such as [`append()`](https://docs.python.org/3/builtins/stdtypes.html#bytearray.append "bytearray.append")
, [`pop()`](https://docs.python.org/3/builtins/stdtypes.html#bytearray.pop "bytearray.pop")
, and [`reverse()`](https://docs.python.org/3/builtins/stdtypes.html#bytearray.reverse "bytearray.reverse")
.

Copy

\>>> b \= bytearray('ABC')
\>>> b.append('d')
\>>> b.append(ord('e'))
\>>> b
bytearray(b'ABCde')

There’s also a corresponding C API, with [`PyByteArray_FromObject()`](https://docs.python.org/3/c-api/bytearray.html#c.PyByteArray_FromObject "PyByteArray_FromObject")
, [`PyByteArray_FromStringAndSize()`](https://docs.python.org/3/c-api/bytearray.html#c.PyByteArray_FromStringAndSize "PyByteArray_FromStringAndSize")
, and various other functions.

See also

[**PEP 3112**](https://peps.python.org/pep-3112/)
 - Bytes literals in Python 3000

PEP written by Jason Orendorff; backported to 2.6 by Christian Heimes.

PEP 3116: New I/O Library[¶](https://docs.python.org/3/whatsnew/2.6.html#pep-3116-new-i-o-library "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

Python’s built-in file objects support a number of methods, but file-like objects don’t necessarily support all of them. Objects that imitate files usually support `read()` and `write()`, but they may not support `readline()`, for example. Python 3.0 introduces a layered I/O library in the [`io`](https://docs.python.org/3/library/io.html#module-io "io: Core tools for working with streams.")
 module that separates buffering and text-handling features from the fundamental read and write operations.

There are three levels of abstract base classes provided by the [`io`](https://docs.python.org/3/library/io.html#module-io "io: Core tools for working with streams.")
 module:

*   [`RawIOBase`](https://docs.python.org/3/library/io.html#io.RawIOBase "io.RawIOBase")
     defines raw I/O operations: [`read()`](https://docs.python.org/3/library/io.html#io.RawIOBase.read "io.RawIOBase.read")
    , [`readinto()`](https://docs.python.org/3/library/io.html#io.RawIOBase.readinto "io.RawIOBase.readinto")
    , [`write()`](https://docs.python.org/3/library/io.html#io.RawIOBase.write "io.RawIOBase.write")
    , [`seek()`](https://docs.python.org/3/library/io.html#io.IOBase.seek "io.IOBase.seek")
    , [`tell()`](https://docs.python.org/3/library/io.html#io.IOBase.tell "io.IOBase.tell")
    , [`truncate()`](https://docs.python.org/3/library/io.html#io.IOBase.truncate "io.IOBase.truncate")
    , and [`close()`](https://docs.python.org/3/library/io.html#io.IOBase.close "io.IOBase.close")
    . Most of the methods of this class will often map to a single system call. There are also [`readable()`](https://docs.python.org/3/library/io.html#io.IOBase.readable "io.IOBase.readable")
    , [`writable()`](https://docs.python.org/3/library/io.html#io.IOBase.writable "io.IOBase.writable")
    , and [`seekable()`](https://docs.python.org/3/library/io.html#io.IOBase.seekable "io.IOBase.seekable")
     methods for determining what operations a given object will allow.
    
    Python 3.0 has concrete implementations of this class for files and sockets, but Python 2.6 hasn’t restructured its file and socket objects in this way.
    
*   [`BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase")
     is an abstract base class that buffers data in memory to reduce the number of system calls used, making I/O processing more efficient. It supports all of the methods of [`RawIOBase`](https://docs.python.org/3/library/io.html#io.RawIOBase "io.RawIOBase")
    , and adds a [`raw`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.raw "io.BufferedIOBase.raw")
     attribute holding the underlying raw object.
    
    There are five concrete classes implementing this ABC. [`BufferedWriter`](https://docs.python.org/3/library/io.html#io.BufferedWriter "io.BufferedWriter")
     and [`BufferedReader`](https://docs.python.org/3/library/io.html#io.BufferedReader "io.BufferedReader")
     are for objects that support write-only or read-only usage that have a [`seek()`](https://docs.python.org/3/library/io.html#io.IOBase.seek "io.IOBase.seek")
     method for random access. [`BufferedRandom`](https://docs.python.org/3/library/io.html#io.BufferedRandom "io.BufferedRandom")
     objects support read and write access upon the same underlying stream, and [`BufferedRWPair`](https://docs.python.org/3/library/io.html#io.BufferedRWPair "io.BufferedRWPair")
     is for objects such as TTYs that have both read and write operations acting upon unconnected streams of data. The [`BytesIO`](https://docs.python.org/3/library/io.html#io.BytesIO "io.BytesIO")
     class supports reading, writing, and seeking over an in-memory buffer.
    
*   [`TextIOBase`](https://docs.python.org/3/library/io.html#io.TextIOBase "io.TextIOBase")
    : Provides functions for reading and writing strings (remember, strings will be Unicode in Python 3.0), and supporting [universal newlines](https://docs.python.org/3/glossary.html#term-universal-newlines)
    . `TextIOBase` defines the [`readline()`](https://docs.python.org/3/library/readline.html#module-readline "readline: GNU readline support for Python.")
     method and supports iteration upon objects.
    
    There are two concrete implementations. [`TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper")
     wraps a buffered I/O object, supporting all of the methods for text I/O and adding a [`buffer`](https://docs.python.org/3/library/io.html#io.TextIOBase.buffer "io.TextIOBase.buffer")
     attribute for access to the underlying object. [`StringIO`](https://docs.python.org/3/library/io.html#io.StringIO "io.StringIO")
     simply buffers everything in memory without ever writing anything to disk.
    
    (In Python 2.6, [`io.StringIO`](https://docs.python.org/3/library/io.html#io.StringIO "io.StringIO")
     is implemented in pure Python, so it’s pretty slow. You should therefore stick with the existing `StringIO` module or `cStringIO` for now. At some point Python 3.0’s [`io`](https://docs.python.org/3/library/io.html#module-io "io: Core tools for working with streams.")
     module will be rewritten into C for speed, and perhaps the C implementation will be backported to the 2.x releases.)
    

In Python 2.6, the underlying implementations haven’t been restructured to build on top of the [`io`](https://docs.python.org/3/library/io.html#module-io "io: Core tools for working with streams.")
 module’s classes. The module is being provided to make it easier to write code that’s forward-compatible with 3.0, and to save developers the effort of writing their own implementations of buffering and text I/O.

See also

[**PEP 3116**](https://peps.python.org/pep-3116/)
 - New I/O

PEP written by Daniel Stutzbach, Mike Verdone, and Guido van Rossum. Code by Guido van Rossum, Georg Brandl, Walter Doerwald, Jeremy Hylton, Martin von Löwis, Tony Lownds, and others.

PEP 3118: Revised Buffer Protocol[¶](https://docs.python.org/3/whatsnew/2.6.html#pep-3118-revised-buffer-protocol "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------

The buffer protocol is a C-level API that lets Python types exchange pointers into their internal representations. A memory-mapped file can be viewed as a buffer of characters, for example, and this lets another module such as [`re`](https://docs.python.org/3/library/re.html#module-re "re: Regular expression operations.")
 treat memory-mapped files as a string of characters to be searched.

The primary users of the buffer protocol are numeric-processing packages such as NumPy, which expose the internal representation of arrays so that callers can write data directly into an array instead of going through a slower API. This PEP updates the buffer protocol in light of experience from NumPy development, adding a number of new features such as indicating the shape of an array or locking a memory region.

The most important new C API function is `PyObject_GetBuffer(PyObject *obj, Py_buffer *view, int flags)`, which takes an object and a set of flags, and fills in the `Py_buffer` structure with information about the object’s memory representation. Objects can use this operation to lock memory in place while an external caller could be modifying the contents, so there’s a corresponding `PyBuffer_Release(Py_buffer *view)` to indicate that the external caller is done.

The _flags_ argument to [`PyObject_GetBuffer()`](https://docs.python.org/3/c-api/buffer.html#c.PyObject_GetBuffer "PyObject_GetBuffer")
 specifies constraints upon the memory returned. Some examples are:

*   [`PyBUF_WRITABLE`](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_WRITABLE "PyBUF_WRITABLE")
     indicates that the memory must be writable.
    
*   `PyBUF_LOCK` requests a read-only or exclusive lock on the memory.
    
*   [`PyBUF_C_CONTIGUOUS`](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_C_CONTIGUOUS "PyBUF_C_CONTIGUOUS")
     and [`PyBUF_F_CONTIGUOUS`](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_F_CONTIGUOUS "PyBUF_F_CONTIGUOUS")
     requests a C-contiguous (last dimension varies the fastest) or Fortran-contiguous (first dimension varies the fastest) array layout.
    

Two new argument codes for [`PyArg_ParseTuple()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple "PyArg_ParseTuple")
, `s*` and `z*`, return locked buffer objects for a parameter.

See also

[**PEP 3118**](https://peps.python.org/pep-3118/)
 - Revising the buffer protocol

PEP written by Travis Oliphant and Carl Banks; implemented by Travis Oliphant.

PEP 3119: Abstract Base Classes[¶](https://docs.python.org/3/whatsnew/2.6.html#pep-3119-abstract-base-classes "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------

Some object-oriented languages such as Java support interfaces, declaring that a class has a given set of methods or supports a given access protocol. Abstract Base Classes (or ABCs) are an equivalent feature for Python. The ABC support consists of an [`abc`](https://docs.python.org/3/library/abc.html#module-abc "abc: Abstract base classes according to :pep:`3119`.")
 module containing a metaclass called [`ABCMeta`](https://docs.python.org/3/library/abc.html#abc.ABCMeta "abc.ABCMeta")
, special handling of this metaclass by the [`isinstance()`](https://docs.python.org/3/builtins/functions.html#isinstance "isinstance")
 and [`issubclass()`](https://docs.python.org/3/builtins/functions.html#issubclass "issubclass")
 builtins, and a collection of basic ABCs that the Python developers think will be widely useful. Future versions of Python will probably add more ABCs.

Let’s say you have a particular class and wish to know whether it supports dictionary-style access. The phrase “dictionary-style” is vague, however. It probably means that accessing items with `obj[1]` works. Does it imply that setting items with `obj[2] = value` works? Or that the object will have `keys()`, `values()`, and `items()` methods? What about the iterative variants such as `iterkeys()`? ``copy`and :meth:()``!update\`? Iterating over the object with `iter()`?

The Python 2.6 [`collections`](https://docs.python.org/3/library/collections.html#module-collections "collections: Container datatypes")
 module includes a number of different ABCs that represent these distinctions. `Iterable` indicates that a class defines [`__iter__()`](https://docs.python.org/3/reference/datamodel.html#object.__iter__ "object.__iter__")
, and `Container` means the class defines a [`__contains__()`](https://docs.python.org/3/reference/datamodel.html#object.__contains__ "object.__contains__")
 method and therefore supports `x in y` expressions. The basic dictionary interface of getting items, setting items, and `keys()`, `values()`, and `items()`, is defined by the `MutableMapping` ABC.

You can derive your own classes from a particular ABC to indicate they support that ABC’s interface:

Copy

import collections

class Storage(collections.MutableMapping):
    ...

Alternatively, you could write the class without deriving from the desired ABC and instead register the class by calling the ABC’s [`register()`](https://docs.python.org/3/library/abc.html#abc.ABCMeta.register "abc.ABCMeta.register")
 method:

Copy

import collections

class Storage:
    ...

collections.MutableMapping.register(Storage)

For classes that you write, deriving from the ABC is probably clearer. The [`register()`](https://docs.python.org/3/library/abc.html#abc.ABCMeta.register "abc.ABCMeta.register")
 method is useful when you’ve written a new ABC that can describe an existing type or class, or if you want to declare that some third-party class implements an ABC. For example, if you defined a `PrintableType` ABC, it’s legal to do:

Copy

\# Register Python's types
PrintableType.register(int)
PrintableType.register(float)
PrintableType.register(str)

Classes should obey the semantics specified by an ABC, but Python can’t check this; it’s up to the class author to understand the ABC’s requirements and to implement the code accordingly.

To check whether an object supports a particular interface, you can now write:

Copy

def func(d):
    if not isinstance(d, collections.MutableMapping):
        raise ValueError("Mapping object expected, not %r" % d)

Don’t feel that you must now begin writing lots of checks as in the above example. Python has a strong tradition of duck-typing, where explicit type-checking is never done and code simply calls methods on an object, trusting that those methods will be there and raising an exception if they aren’t. Be judicious in checking for ABCs and only do it where it’s absolutely necessary.

You can write your own ABCs by using `abc.ABCMeta` as the metaclass in a class definition:

Copy

from abc import ABCMeta, abstractmethod

class Drawable():
    \_\_metaclass\_\_ \= ABCMeta

    @abstractmethod
    def draw(self, x, y, scale\=1.0):
        pass

    def draw\_doubled(self, x, y):
        self.draw(x, y, scale\=2.0)

class Square(Drawable):
    def draw(self, x, y, scale):
        ...

In the `Drawable` ABC above, the `draw_doubled()` method renders the object at twice its size and can be implemented in terms of other methods described in `Drawable`. Classes implementing this ABC therefore don’t need to provide their own implementation of `draw_doubled()`, though they can do so. An implementation of `draw()` is necessary, though; the ABC can’t provide a useful generic implementation.

You can apply the [`@abstractmethod`](https://docs.python.org/3/library/abc.html#abc.abstractmethod "abc.abstractmethod")
 decorator to methods such as `draw()` that must be implemented; Python will then raise an exception for classes that don’t define the method. Note that the exception is only raised when you actually try to create an instance of a subclass lacking the method:

Copy

\>>> class Circle(Drawable):
...     pass
...
\>>> c \= Circle()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't instantiate abstract class Circle with abstract methods draw
\>>>

Abstract data attributes can be declared using the `@abstractproperty` decorator:

Copy

from abc import abstractproperty
...

@abstractproperty
def readonly(self):
   return self.\_x

Subclasses must then define a `readonly` property.

See also

[**PEP 3119**](https://peps.python.org/pep-3119/)
 - Introducing Abstract Base Classes

PEP written by Guido van Rossum and Talin. Implemented by Guido van Rossum. Backported to 2.6 by Benjamin Aranguren, with Alex Martelli.

PEP 3127: Integer Literal Support and Syntax[¶](https://docs.python.org/3/whatsnew/2.6.html#pep-3127-integer-literal-support-and-syntax "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------

Python 3.0 changes the syntax for octal (base-8) integer literals, prefixing them with “0o” or “0O” instead of a leading zero, and adds support for binary (base-2) integer literals, signalled by a “0b” or “0B” prefix.

Python 2.6 doesn’t drop support for a leading 0 signalling an octal number, but it does add support for “0o” and “0b”:

Copy

\>>> 0o21, 2\*8 + 1
(17, 17)
\>>> 0b101111
47

The [`oct()`](https://docs.python.org/3/builtins/functions.html#oct "oct")
 builtin still returns numbers prefixed with a leading zero, and a new [`bin()`](https://docs.python.org/3/builtins/functions.html#bin "bin")
 builtin returns the binary representation for a number:

Copy

\>>> oct(42)
'052'
\>>> future\_builtins.oct(42)
'0o52'
\>>> bin(173)
'0b10101101'

The [`int()`](https://docs.python.org/3/builtins/functions.html#int "int")
 and `long()` builtins will now accept the “0o” and “0b” prefixes when base-8 or base-2 are requested, or when the _base_ argument is zero (signalling that the base used should be determined from the string):

Copy

\>>> int ('0o52', 0)
42
\>>> int('1101', 2)
13
\>>> int('0b1101', 2)
13
\>>> int('0b1101', 0)
13

See also

[**PEP 3127**](https://peps.python.org/pep-3127/)
 - Integer Literal Support and Syntax

PEP written by Patrick Maupin; backported to 2.6 by Eric Smith.

PEP 3129: Class Decorators[¶](https://docs.python.org/3/whatsnew/2.6.html#pep-3129-class-decorators "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

Decorators have been extended from functions to classes. It’s now legal to write:

Copy

@foo
@bar
class A:
  pass

This is equivalent to:

Copy

class A:
  pass

A \= foo(bar(A))

See also

[**PEP 3129**](https://peps.python.org/pep-3129/)
 - Class Decorators

PEP written by Collin Winter.

PEP 3141: A Type Hierarchy for Numbers[¶](https://docs.python.org/3/whatsnew/2.6.html#pep-3141-a-type-hierarchy-for-numbers "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------

Python 3.0 adds several abstract base classes for numeric types inspired by Scheme’s numeric tower. These classes were backported to 2.6 as the [`numbers`](https://docs.python.org/3/library/numbers.html#module-numbers "numbers: Numeric abstract base classes (Complex, Real, Integral, etc.).")
 module.

The most general ABC is [`Number`](https://docs.python.org/3/library/numbers.html#numbers.Number "numbers.Number")
. It defines no operations at all, and only exists to allow checking if an object is a number by doing `isinstance(obj, Number)`.

[`Complex`](https://docs.python.org/3/library/numbers.html#numbers.Complex "numbers.Complex")
 is a subclass of [`Number`](https://docs.python.org/3/library/numbers.html#numbers.Number "numbers.Number")
. Complex numbers can undergo the basic operations of addition, subtraction, multiplication, division, and exponentiation, and you can retrieve the real and imaginary parts and obtain a number’s conjugate. Python’s built-in complex type is an implementation of `Complex`.

[`Real`](https://docs.python.org/3/library/numbers.html#numbers.Real "numbers.Real")
 further derives from [`Complex`](https://docs.python.org/3/library/numbers.html#numbers.Complex "numbers.Complex")
, and adds operations that only work on real numbers: [`floor()`](https://docs.python.org/3/library/math.html#math.floor "math.floor")
, [`trunc()`](https://docs.python.org/3/library/math.html#math.trunc "math.trunc")
, rounding, taking the remainder mod N, floor division, and comparisons.

[`Rational`](https://docs.python.org/3/library/numbers.html#numbers.Rational "numbers.Rational")
 numbers derive from [`Real`](https://docs.python.org/3/library/numbers.html#numbers.Real "numbers.Real")
, have [`numerator`](https://docs.python.org/3/library/numbers.html#numbers.Rational.numerator "numbers.Rational.numerator")
 and [`denominator`](https://docs.python.org/3/library/numbers.html#numbers.Rational.denominator "numbers.Rational.denominator")
 properties, and can be converted to floats. Python 2.6 adds a simple rational-number class, [`Fraction`](https://docs.python.org/3/library/fractions.html#fractions.Fraction "fractions.Fraction")
, in the [`fractions`](https://docs.python.org/3/library/fractions.html#module-fractions "fractions: Rational numbers.")
 module. (It’s called `Fraction` instead of `Rational` to avoid a name clash with `numbers.Rational`.)

[`Integral`](https://docs.python.org/3/library/numbers.html#numbers.Integral "numbers.Integral")
 numbers derive from [`Rational`](https://docs.python.org/3/library/numbers.html#numbers.Rational "numbers.Rational")
, and can be shifted left and right with `<<` and `>>`, combined using bitwise operations such as `&` and `|`, and can be used as array indexes and slice boundaries.

In Python 3.0, the PEP slightly redefines the existing builtins [`round()`](https://docs.python.org/3/builtins/functions.html#round "round")
, [`math.floor()`](https://docs.python.org/3/library/math.html#math.floor "math.floor")
, [`math.ceil()`](https://docs.python.org/3/library/math.html#math.ceil "math.ceil")
, and adds a new one, [`math.trunc()`](https://docs.python.org/3/library/math.html#math.trunc "math.trunc")
, that’s been backported to Python 2.6. `math.trunc()` rounds toward zero, returning the closest [`Integral`](https://docs.python.org/3/library/numbers.html#numbers.Integral "numbers.Integral")
 that’s between the function’s argument and zero.

See also

[**PEP 3141**](https://peps.python.org/pep-3141/)
 - A Type Hierarchy for Numbers

PEP written by Jeffrey Yasskin.

[Scheme’s numerical tower](https://www.gnu.org/software/guile/manual/html_node/Numerical-Tower.html#Numerical-Tower)
, from the Guile manual.

[Scheme’s number datatypes](https://conservatory.scheme.org/schemers/Documents/Standards/R5RS/HTML/r5rs-Z-H-9.html#%_sec_6.2)
 from the R5RS Scheme specification.

### The [`fractions`](https://docs.python.org/3/library/fractions.html#module-fractions "fractions: Rational numbers.")
 Module[¶](https://docs.python.org/3/whatsnew/2.6.html#the-fractions-module "Link to this heading")

To fill out the hierarchy of numeric types, the [`fractions`](https://docs.python.org/3/library/fractions.html#module-fractions "fractions: Rational numbers.")
 module provides a rational-number class. Rational numbers store their values as a numerator and denominator forming a fraction, and can exactly represent numbers such as `2/3` that floating-point numbers can only approximate.

The [`Fraction`](https://docs.python.org/3/library/fractions.html#fractions.Fraction "fractions.Fraction")
 constructor takes two [`Integral`](https://docs.python.org/3/library/numbers.html#numbers.Integral "numbers.Integral")
 values that will be the numerator and denominator of the resulting fraction.

Copy

\>>> from fractions import Fraction
\>>> a \= Fraction(2, 3)
\>>> b \= Fraction(2, 5)
\>>> float(a), float(b)
(0.66666666666666663, 0.40000000000000002)
\>>> a+b
Fraction(16, 15)
\>>> a/b
Fraction(5, 3)

For converting floating-point numbers to rationals, the float type now has an [`as_integer_ratio()`](https://docs.python.org/3/builtins/stdtypes.html#float.as_integer_ratio "float.as_integer_ratio")
 method that returns the numerator and denominator for a fraction that evaluates to the same floating-point value:

Copy

\>>> (2.5) .as\_integer\_ratio()
(5, 2)
\>>> (3.1415) .as\_integer\_ratio()
(7074029114692207L, 2251799813685248L)
\>>> (1./3) .as\_integer\_ratio()
(6004799503160661L, 18014398509481984L)

Note that values that can only be approximated by floating-point numbers, such as 1./3, are not simplified to the number being approximated; the fraction attempts to match the floating-point value **exactly**.

The [`fractions`](https://docs.python.org/3/library/fractions.html#module-fractions "fractions: Rational numbers.")
 module is based upon an implementation by Sjoerd Mullender that was in Python’s `Demo/classes/` directory for a long time. This implementation was significantly updated by Jeffrey Yasskin.

Other Language Changes[¶](https://docs.python.org/3/whatsnew/2.6.html#other-language-changes "Link to this heading")

---------------------------------------------------------------------------------------------------------------------

Some smaller changes made to the core Python language are:

*   Directories and zip archives containing a `__main__.py` file can now be executed directly by passing their name to the interpreter. The directory or zip archive is automatically inserted as the first entry in sys.path. (Suggestion and initial patch by Andy Chu, subsequently revised by Phillip J. Eby and Nick Coghlan; [bpo-1739468](https://bugs.python.org/issue?@action=redirect&bpo=1739468)
    .)
    
*   The [`hasattr()`](https://docs.python.org/3/builtins/functions.html#hasattr "hasattr")
     function was catching and ignoring all errors, under the assumption that they meant a [`__getattr__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattr__ "object.__getattr__")
     method was failing somehow and the return value of `hasattr()` would therefore be `False`. This logic shouldn’t be applied to [`KeyboardInterrupt`](https://docs.python.org/3/builtins/exceptions.html#KeyboardInterrupt "KeyboardInterrupt")
     and [`SystemExit`](https://docs.python.org/3/builtins/exceptions.html#SystemExit "SystemExit")
    , however; Python 2.6 will no longer discard such exceptions when `hasattr()` encounters them. (Fixed by Benjamin Peterson; [bpo-2196](https://bugs.python.org/issue?@action=redirect&bpo=2196)
    .)
    
*   When calling a function using the `**` syntax to provide keyword arguments, you are no longer required to use a Python dictionary; any mapping will now work:
    
    Copy
    
    \>>> def f(\*\*kw):
    ...    print sorted(kw)
    ...
    \>>> ud\=UserDict.UserDict()
    \>>> ud\['a'\] \= 1
    \>>> ud\['b'\] \= 'string'
    \>>> f(\*\*ud)
    \['a', 'b'\]
    
    (Contributed by Alexander Belopolsky; [bpo-1686487](https://bugs.python.org/issue?@action=redirect&bpo=1686487)
    .)
    
    It’s also become legal to provide keyword arguments after a `*args` argument to a function call.
    
    Copy
    
    \>>> def f(\*args, \*\*kw):
    ...     print args, kw
    ...
    \>>> f(1,2,3, \*(4,5,6), keyword\=13)
    (1, 2, 3, 4, 5, 6) {'keyword': 13}
    
    Previously this would have been a syntax error. (Contributed by Amaury Forgeot d’Arc; [bpo-3473](https://bugs.python.org/issue?@action=redirect&bpo=3473)
    .)
    
*   A new builtin, `next(iterator, [default])` returns the next item from the specified iterator. If the _default_ argument is supplied, it will be returned if _iterator_ has been exhausted; otherwise, the [`StopIteration`](https://docs.python.org/3/builtins/exceptions.html#StopIteration "StopIteration")
     exception will be raised. (Backported in [bpo-2719](https://bugs.python.org/issue?@action=redirect&bpo=2719)
    .)
    
*   Tuples now have [`index()`](https://docs.python.org/3/builtins/stdtypes.html#tuple.index "tuple.index")
     and [`count()`](https://docs.python.org/3/builtins/stdtypes.html#tuple.count "tuple.count")
     methods matching the list type’s [`index()`](https://docs.python.org/3/builtins/stdtypes.html#list.index "list.index")
     and [`count()`](https://docs.python.org/3/builtins/stdtypes.html#list.count "list.count")
     methods:
    
    Copy
    
    \>>> t \= (0,1,2,3,4,0,1,2)
    \>>> t.index(3)
    3
    \>>> t.count(0)
    2
    
    (Contributed by Raymond Hettinger)
    
*   The built-in types now have improved support for extended slicing syntax, accepting various combinations of `(start, stop, step)`. Previously, the support was partial and certain corner cases wouldn’t work. (Implemented by Thomas Wouters.)
    
*   Properties now have three decorators, [`@getter`](https://docs.python.org/3/builtins/functions.html#property.getter "property.getter")
    , [`@setter`](https://docs.python.org/3/builtins/functions.html#property.setter "property.setter")
     and [`@deleter`](https://docs.python.org/3/builtins/functions.html#property.deleter "property.deleter")
    , that are decorators providing useful shortcuts for adding a getter, setter or deleter function to an existing property. You would use them like this:
    
    Copy
    
    class C(object):
        @property
        def x(self):
            return self.\_x
    
        @x.setter
        def x(self, value):
            self.\_x \= value
    
        @x.deleter
        def x(self):
            del self.\_x
    
    class D(C):
        @C.x.getter
        def x(self):
            return self.\_x \* 2
    
        @x.setter
        def x(self, value):
            self.\_x \= value / 2
    
*   Several methods of the built-in set types now accept multiple iterables: [`intersection()`](https://docs.python.org/3/builtins/stdtypes.html#set.intersection "set.intersection")
    , [`intersection_update()`](https://docs.python.org/3/builtins/stdtypes.html#set.intersection_update "set.intersection_update")
    , [`union()`](https://docs.python.org/3/builtins/stdtypes.html#set.union "set.union")
    , [`update()`](https://docs.python.org/3/builtins/stdtypes.html#set.update "set.update")
    , [`difference()`](https://docs.python.org/3/builtins/stdtypes.html#set.difference "set.difference")
     and [`difference_update()`](https://docs.python.org/3/builtins/stdtypes.html#set.difference_update "set.difference_update")
    .
    
    Copy
    
    \>>> s\=set('1234567890')
    \>>> s.intersection('abc123', 'cdf246')  \# Intersection between all inputs
    set(\['2'\])
    \>>> s.difference('246', '789')
    set(\['1', '0', '3', '5'\])
    
    (Contributed by Raymond Hettinger.)
    
*   Many floating-point features were added. The [`float()`](https://docs.python.org/3/builtins/functions.html#float "float")
     function will now turn the string `nan` into an IEEE 754 Not A Number value, and `+inf` and `-inf` into positive or negative infinity. This works on any platform with IEEE 754 semantics. (Contributed by Christian Heimes; [bpo-1635](https://bugs.python.org/issue?@action=redirect&bpo=1635)
    .)
    
    Other functions in the [`math`](https://docs.python.org/3/library/math.html#module-math "math: Mathematical functions (sin() etc.).")
     module, [`isinf()`](https://docs.python.org/3/library/math.html#math.isinf "math.isinf")
     and [`isnan()`](https://docs.python.org/3/library/math.html#math.isnan "math.isnan")
    , return true if their floating-point argument is infinite or Not A Number. ([bpo-1640](https://bugs.python.org/issue?@action=redirect&bpo=1640)
    )
    
    Conversion functions were added to convert floating-point numbers into hexadecimal strings ([bpo-3008](https://bugs.python.org/issue?@action=redirect&bpo=3008)
    ). These functions convert floats to and from a string representation without introducing rounding errors from the conversion between decimal and binary. Floats have a [`hex()`](https://docs.python.org/3/builtins/functions.html#hex "hex")
     method that returns a string representation, and the `float.fromhex()` method converts a string back into a number:
    
    Copy
    
    \>>> a \= 3.75
    \>>> a.hex()
    '0x1.e000000000000p+1'
    \>>> float.fromhex('0x1.e000000000000p+1')
    3.75
    \>>> b\=1./3
    \>>> b.hex()
    '0x1.5555555555555p-2'
    
*   A numerical nicety: when creating a complex number from two floats on systems that support signed zeros (-0 and +0), the [`complex()`](https://docs.python.org/3/builtins/functions.html#complex "complex")
     constructor will now preserve the sign of the zero. (Fixed by Mark T. Dickinson; [bpo-1507](https://bugs.python.org/issue?@action=redirect&bpo=1507)
    .)
    
*   Classes that inherit a [`__hash__()`](https://docs.python.org/3/reference/datamodel.html#object.__hash__ "object.__hash__")
     method from a parent class can set `__hash__ = None` to indicate that the class isn’t hashable. This will make `hash(obj)` raise a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
     and the class will not be indicated as implementing the `Hashable` ABC.
    
    You should do this when you’ve defined a `__cmp__()` or [`__eq__()`](https://docs.python.org/3/reference/datamodel.html#object.__eq__ "object.__eq__")
     method that compares objects by their value rather than by identity. All objects have a default hash method that uses `id(obj)` as the hash value. There’s no tidy way to remove the [`__hash__()`](https://docs.python.org/3/reference/datamodel.html#object.__hash__ "object.__hash__")
     method inherited from a parent class, so assigning `None` was implemented as an override. At the C level, extensions can set `tp_hash` to [`PyObject_HashNotImplemented()`](https://docs.python.org/3/c-api/object.html#c.PyObject_HashNotImplemented "PyObject_HashNotImplemented")
    . (Fixed by Nick Coghlan and Amaury Forgeot d’Arc; [bpo-2235](https://bugs.python.org/issue?@action=redirect&bpo=2235)
    .)
    
*   The [`GeneratorExit`](https://docs.python.org/3/builtins/exceptions.html#GeneratorExit "GeneratorExit")
     exception now subclasses [`BaseException`](https://docs.python.org/3/builtins/exceptions.html#BaseException "BaseException")
     instead of [`Exception`](https://docs.python.org/3/builtins/exceptions.html#Exception "Exception")
    . This means that an exception handler that does `except Exception:` will not inadvertently catch `GeneratorExit`. (Contributed by Chad Austin; [bpo-1537](https://bugs.python.org/issue?@action=redirect&bpo=1537)
    .)
    
*   Generator objects now have a `gi_code` attribute that refers to the original code object backing the generator. (Contributed by Collin Winter; [bpo-1473257](https://bugs.python.org/issue?@action=redirect&bpo=1473257)
    .)
    
*   The [`compile()`](https://docs.python.org/3/builtins/functions.html#compile "compile")
     built-in function now accepts keyword arguments as well as positional parameters. (Contributed by Thomas Wouters; [bpo-1444529](https://bugs.python.org/issue?@action=redirect&bpo=1444529)
    .)
    
*   The [`complex()`](https://docs.python.org/3/builtins/functions.html#complex "complex")
     constructor now accepts strings containing parenthesized complex numbers, meaning that `complex(repr(cplx))` will now round-trip values. For example, `complex('(3+4j)')` now returns the value (3+4j). ([bpo-1491866](https://bugs.python.org/issue?@action=redirect&bpo=1491866)
    )
    
*   The string [`translate()`](https://docs.python.org/3/builtins/stdtypes.html#str.translate "str.translate")
     method now accepts `None` as the translation table parameter, which is treated as the identity transformation. This makes it easier to carry out operations that only delete characters. (Contributed by Bengt Richter and implemented by Raymond Hettinger; [bpo-1193128](https://bugs.python.org/issue?@action=redirect&bpo=1193128)
    .)
    
*   The built-in [`dir()`](https://docs.python.org/3/builtins/functions.html#dir "dir")
     function now checks for a [`__dir__()`](https://docs.python.org/3/reference/datamodel.html#object.__dir__ "object.__dir__")
     method on the objects it receives. This method must return a list of strings containing the names of valid attributes for the object, and lets the object control the value that `dir()` produces. Objects that have [`__getattr__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattr__ "object.__getattr__")
     or [`__getattribute__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattribute__ "object.__getattribute__")
     methods can use this to advertise pseudo-attributes they will honor. ([bpo-1591665](https://bugs.python.org/issue?@action=redirect&bpo=1591665)
    )
    
*   Instance method objects have new attributes for the object and function comprising the method; the new synonym for `im_self` is [`__self__`](https://docs.python.org/3/reference/datamodel.html#method.__self__ "method.__self__")
    , and `im_func` is also available as [`__func__`](https://docs.python.org/3/reference/datamodel.html#method.__func__ "method.__func__")
    . The old names are still supported in Python 2.6, but are gone in 3.0.
    
*   An obscure change: when you use the [`locals()`](https://docs.python.org/3/builtins/functions.html#locals "locals")
     function inside a [`class`](https://docs.python.org/3/reference/compound_stmts.html#class)
     statement, the resulting dictionary no longer returns free variables. (Free variables, in this case, are variables referenced in the `class` statement that aren’t attributes of the class.)
    

### Optimizations[¶](https://docs.python.org/3/whatsnew/2.6.html#optimizations "Link to this heading")

*   The [`warnings`](https://docs.python.org/3/library/warnings.html#module-warnings "warnings: Issue warning messages and control their disposition.")
     module has been rewritten in C. This makes it possible to invoke warnings from the parser, and may also make the interpreter’s startup faster. (Contributed by Neal Norwitz and Brett Cannon; [bpo-1631171](https://bugs.python.org/issue?@action=redirect&bpo=1631171)
    .)
    
*   Type objects now have a cache of methods that can reduce the work required to find the correct method implementation for a particular class; once cached, the interpreter doesn’t need to traverse base classes to figure out the right method to call. The cache is cleared if a base class or the class itself is modified, so the cache should remain correct even in the face of Python’s dynamic nature. (Original optimization implemented by Armin Rigo, updated for Python 2.6 by Kevin Jacobs; [bpo-1700288](https://bugs.python.org/issue?@action=redirect&bpo=1700288)
    .)
    
    By default, this change is only applied to types that are included with the Python core. Extension modules may not necessarily be compatible with this cache, so they must explicitly add [`Py_TPFLAGS_HAVE_VERSION_TAG`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_VERSION_TAG "Py_TPFLAGS_HAVE_VERSION_TAG")
     to the module’s `tp_flags` field to enable the method cache. (To be compatible with the method cache, the extension module’s code must not directly access and modify the `tp_dict` member of any of the types it implements. Most modules don’t do this, but it’s impossible for the Python interpreter to determine that. See [bpo-1878](https://bugs.python.org/issue?@action=redirect&bpo=1878)
     for some discussion.)
    
*   Function calls that use keyword arguments are significantly faster by doing a quick pointer comparison, usually saving the time of a full string comparison. (Contributed by Raymond Hettinger, after an initial implementation by Antoine Pitrou; [bpo-1819](https://bugs.python.org/issue?@action=redirect&bpo=1819)
    .)
    
*   All of the functions in the [`struct`](https://docs.python.org/3/library/struct.html#module-struct "struct: Interpret bytes as packed binary data.")
     module have been rewritten in C, thanks to work at the Need For Speed sprint. (Contributed by Raymond Hettinger.)
    
*   Some of the standard built-in types now set a bit in their type objects. This speeds up checking whether an object is a subclass of one of these types. (Contributed by Neal Norwitz.)
    
*   Unicode strings now use faster code for detecting whitespace and line breaks; this speeds up the [`split()`](https://docs.python.org/3/builtins/stdtypes.html#str.split "str.split")
     method by about 25% and [`splitlines()`](https://docs.python.org/3/builtins/stdtypes.html#str.splitlines "str.splitlines")
     by 35%. (Contributed by Antoine Pitrou.) Memory usage is reduced by using pymalloc for the Unicode string’s data.
    
*   The `with` statement now stores the [`__exit__()`](https://docs.python.org/3/reference/datamodel.html#object.__exit__ "object.__exit__")
     method on the stack, producing a small speedup. (Implemented by Jeffrey Yasskin.)
    
*   To reduce memory usage, the garbage collector will now clear internal free lists when garbage-collecting the highest generation of objects. This may return memory to the operating system sooner.
    

### Interpreter Changes[¶](https://docs.python.org/3/whatsnew/2.6.html#interpreter-changes "Link to this heading")

Two command-line options have been reserved for use by other Python implementations. The `-J` switch has been reserved for use by Jython for Jython-specific options, such as switches that are passed to the underlying JVM. [`-X`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
 has been reserved for options specific to a particular implementation of Python such as CPython, Jython, or IronPython. If either option is used with Python 2.6, the interpreter will report that the option isn’t currently used.

Python can now be prevented from writing `.pyc` or `.pyo` files by supplying the [`-B`](https://docs.python.org/3/using/cmdline.html#cmdoption-B)
 switch to the Python interpreter, or by setting the [`PYTHONDONTWRITEBYTECODE`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONDONTWRITEBYTECODE)
 environment variable before running the interpreter. This setting is available to Python programs as the `sys.dont_write_bytecode` variable, and Python code can change the value to modify the interpreter’s behaviour. (Contributed by Neal Norwitz and Georg Brandl.)

The encoding used for standard input, output, and standard error can be specified by setting the [`PYTHONIOENCODING`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONIOENCODING)
 environment variable before running the interpreter. The value should be a string in the form `<encoding>` or `<encoding>:<errorhandler>`. The _encoding_ part specifies the encoding’s name, e.g. `utf-8` or `latin-1`; the optional _errorhandler_ part specifies what to do with characters that can’t be handled by the encoding, and should be one of “error”, “ignore”, or “replace”. (Contributed by Martin von Löwis.)

New and Improved Modules[¶](https://docs.python.org/3/whatsnew/2.6.html#new-and-improved-modules "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

As in every release, Python’s standard library received a number of enhancements and bug fixes. Here’s a partial list of the most notable changes, sorted alphabetically by module name. Consult the `Misc/NEWS` file in the source tree for a more complete list of changes, or look through the Subversion logs for all the details.

*   The `asyncore` and `asynchat` modules are being actively maintained again, and a number of patches and bugfixes were applied. (Maintained by Josiah Carlson; see [bpo-1736190](https://bugs.python.org/issue?@action=redirect&bpo=1736190)
     for one patch.)
    
*   The `bsddb` module also has a new maintainer, Jesús Cea Avión, and the package is now available as a standalone package. The web page for the package is [www.jcea.es/programacion/pybsddb.htm](https://www.jcea.es/programacion/pybsddb.htm)
    . The plan is to remove the package from the standard library in Python 3.0, because its pace of releases is much more frequent than Python’s.
    
    The `bsddb.dbshelve` module now uses the highest pickling protocol available, instead of restricting itself to protocol 1. (Contributed by W. Barnes.)
    
*   The `cgi` module will now read variables from the query string of an HTTP POST request. This makes it possible to use form actions with URLs that include query strings such as “/cgi-bin/add.py?category=1”. (Contributed by Alexandre Fiori and Nubis; [bpo-1817](https://bugs.python.org/issue?@action=redirect&bpo=1817)
    .)
    
    The [`parse_qs()`](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.parse_qs "urllib.parse.parse_qs")
     and [`parse_qsl()`](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.parse_qsl "urllib.parse.parse_qsl")
     functions have been relocated from the `cgi` module to the [`urlparse`](https://docs.python.org/3/library/urllib.parse.html#module-urllib.parse "urllib.parse: Parse URLs into or assemble them from components.")
     module. The versions still available in the `cgi` module will trigger [`PendingDeprecationWarning`](https://docs.python.org/3/builtins/exceptions.html#PendingDeprecationWarning "PendingDeprecationWarning")
     messages in 2.6 ([bpo-600362](https://bugs.python.org/issue?@action=redirect&bpo=600362)
    ).
    
*   The [`cmath`](https://docs.python.org/3/library/cmath.html#module-cmath "cmath: Mathematical functions for complex numbers.")
     module underwent extensive revision, contributed by Mark Dickinson and Christian Heimes. Five new functions were added:
    
    *   [`polar()`](https://docs.python.org/3/library/cmath.html#cmath.polar "cmath.polar")
         converts a complex number to polar form, returning the modulus and argument of the complex number.
        
    *   [`rect()`](https://docs.python.org/3/library/cmath.html#cmath.rect "cmath.rect")
         does the opposite, turning a modulus, argument pair back into the corresponding complex number.
        
    *   [`phase()`](https://docs.python.org/3/library/cmath.html#cmath.phase "cmath.phase")
         returns the argument (also called the angle) of a complex number.
        
    *   [`isnan()`](https://docs.python.org/3/library/cmath.html#cmath.isnan "cmath.isnan")
         returns True if either the real or imaginary part of its argument is a NaN.
        
    *   [`isinf()`](https://docs.python.org/3/library/cmath.html#cmath.isinf "cmath.isinf")
         returns True if either the real or imaginary part of its argument is infinite.
        
    
    The revisions also improved the numerical soundness of the [`cmath`](https://docs.python.org/3/library/cmath.html#module-cmath "cmath: Mathematical functions for complex numbers.")
     module. For all functions, the real and imaginary parts of the results are accurate to within a few units of least precision (ulps) whenever possible. See [bpo-1381](https://bugs.python.org/issue?@action=redirect&bpo=1381)
     for the details. The branch cuts for [`asinh()`](https://docs.python.org/3/library/cmath.html#cmath.asinh "cmath.asinh")
    , [`atanh()`](https://docs.python.org/3/library/cmath.html#cmath.atanh "cmath.atanh")
    , and [`atan()`](https://docs.python.org/3/library/cmath.html#cmath.atan "cmath.atan")
     have also been corrected.
    
    The tests for the module have been greatly expanded; nearly 2000 new test cases exercise the algebraic functions.
    
    On IEEE 754 platforms, the [`cmath`](https://docs.python.org/3/library/cmath.html#module-cmath "cmath: Mathematical functions for complex numbers.")
     module now handles IEEE 754 special values and floating-point exceptions in a manner consistent with Annex ‘G’ of the C99 standard.
    
*   A new data type in the [`collections`](https://docs.python.org/3/library/collections.html#module-collections "collections: Container datatypes")
     module: `namedtuple(typename, fieldnames)` is a factory function that creates subclasses of the standard tuple whose fields are accessible by name as well as index. For example:
    
    Copy
    
    \>>> var\_type \= collections.namedtuple('variable',
    ...             'id name type size')
    \>>> \# Names are separated by spaces or commas.
    \>>> \# 'id, name, type, size' would also work.
    \>>> var\_type.\_fields
    ('id', 'name', 'type', 'size')
    
    \>>> var \= var\_type(1, 'frequency', 'int', 4)
    \>>> print var\[0\], var.id    \# Equivalent
    1 1
    \>>> print var\[2\], var.type  \# Equivalent
    int int
    \>>> var.\_asdict()
    {'size': 4, 'type': 'int', 'id': 1, 'name': 'frequency'}
    \>>> v2 \= var.\_replace(name\='amplitude')
    \>>> v2
    variable(id=1, name='amplitude', type='int', size=4)
    
    Several places in the standard library that returned tuples have been modified to return [`namedtuple()`](https://docs.python.org/3/library/collections.html#collections.namedtuple "collections.namedtuple")
     instances. For example, the [`decimal.Decimal.as_tuple()`](https://docs.python.org/3/library/decimal.html#decimal.Decimal.as_tuple "decimal.Decimal.as_tuple")
     method now returns a named tuple with `sign`, `digits`, and `exponent` fields.
    
    (Contributed by Raymond Hettinger.)
    
*   Another change to the [`collections`](https://docs.python.org/3/library/collections.html#module-collections "collections: Container datatypes")
     module is that the [`deque`](https://docs.python.org/3/library/collections.html#collections.deque "collections.deque")
     type now supports an optional _maxlen_ parameter; if supplied, the deque’s size will be restricted to no more than _maxlen_ items. Adding more items to a full deque causes old items to be discarded.
    
    Copy
    
    \>>> from collections import deque
    \>>> dq\=deque(maxlen\=3)
    \>>> dq
    deque(\[\], maxlen=3)
    \>>> dq.append(1); dq.append(2); dq.append(3)
    \>>> dq
    deque(\[1, 2, 3\], maxlen=3)
    \>>> dq.append(4)
    \>>> dq
    deque(\[2, 3, 4\], maxlen=3)
    
    (Contributed by Raymond Hettinger.)
    
*   The [`Cookie`](https://docs.python.org/3/library/http.cookies.html#module-http.cookies "http.cookies: Support for HTTP state management (cookies).")
     module’s [`Morsel`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel "http.cookies.Morsel")
     objects now support an [`httponly`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.httponly "http.cookies.Morsel.httponly")
     attribute. In some browsers. cookies with this attribute set cannot be accessed or manipulated by JavaScript code. (Contributed by Arvin Schnell; [bpo-1638033](https://bugs.python.org/issue?@action=redirect&bpo=1638033)
    .)
    
*   A new window method in the [`curses`](https://docs.python.org/3/library/curses.html#module-curses "curses: An interface to the curses library, providing portable terminal handling.")
     module, [`chgat()`](https://docs.python.org/3/library/curses.html#curses.window.chgat "curses.window.chgat")
    , changes the display attributes for a certain number of characters on a single line. (Contributed by Fabian Kreutz.)
    
    Copy
    
    \# Boldface text starting at y=0,x=21
    \# and affecting the rest of the line.
    stdscr.chgat(0, 21, curses.A\_BOLD)
    
    The [`Textbox`](https://docs.python.org/3/library/curses.html#curses.textpad.Textbox "curses.textpad.Textbox")
     class in the [`curses.textpad`](https://docs.python.org/3/library/curses.html#module-curses.textpad "curses.textpad: Emacs-like input editing in a curses window.")
     module now supports editing in insert mode as well as overwrite mode. Insert mode is enabled by supplying a true value for the _insert\_mode_ parameter when creating the `Textbox` instance.
    
*   The [`datetime`](https://docs.python.org/3/library/datetime.html#module-datetime "datetime: Basic date and time types.")
     module’s [`strftime()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strftime "datetime.datetime.strftime")
     methods now support a `%f` format code that expands to the number of microseconds in the object, zero-padded on the left to six places. (Contributed by Skip Montanaro; [bpo-1158](https://bugs.python.org/issue?@action=redirect&bpo=1158)
    .)
    
*   The [`decimal`](https://docs.python.org/3/library/decimal.html#module-decimal "decimal: Implementation of the General Decimal Arithmetic Specification.")
     module was updated to version 1.66 of [the General Decimal Specification](https://speleotrove.com/decimal/decarith.html)
    . New features include some methods for some basic mathematical functions such as [`exp()`](https://docs.python.org/3/library/decimal.html#decimal.Decimal.exp "decimal.Decimal.exp")
     and [`log10()`](https://docs.python.org/3/library/decimal.html#decimal.Decimal.log10 "decimal.Decimal.log10")
    :
    
    Copy
    
    \>>> Decimal(1).exp()
    Decimal("2.718281828459045235360287471")
    \>>> Decimal("2.7182818").ln()
    Decimal("0.9999999895305022877376682436")
    \>>> Decimal(1000).log10()
    Decimal("3")
    
    The [`as_tuple()`](https://docs.python.org/3/library/decimal.html#decimal.Decimal.as_tuple "decimal.Decimal.as_tuple")
     method of [`Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "decimal.Decimal")
     objects now returns a named tuple with `sign`, `digits`, and `exponent` fields.
    
    (Implemented by Facundo Batista and Mark Dickinson. Named tuple support added by Raymond Hettinger.)
    
*   The [`difflib`](https://docs.python.org/3/library/difflib.html#module-difflib "difflib: Helpers for computing differences between objects.")
     module’s [`SequenceMatcher`](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher "difflib.SequenceMatcher")
     class now returns named tuples representing matches, with `a`, `b`, and `size` attributes. (Contributed by Raymond Hettinger.)
    
*   An optional `timeout` parameter, specifying a timeout measured in seconds, was added to the [`ftplib.FTP`](https://docs.python.org/3/library/ftplib.html#ftplib.FTP "ftplib.FTP")
     class constructor as well as the [`connect()`](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.connect "ftplib.FTP.connect")
     method. (Added by Facundo Batista.) Also, the `FTP` class’s [`storbinary()`](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.storbinary "ftplib.FTP.storbinary")
     and [`storlines()`](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.storlines "ftplib.FTP.storlines")
     now take an optional _callback_ parameter that will be called with each block of data after the data has been sent. (Contributed by Phil Schwartz; [bpo-1221598](https://bugs.python.org/issue?@action=redirect&bpo=1221598)
    .)
    
*   The `reduce()` built-in function is also available in the [`functools`](https://docs.python.org/3/library/functools.html#module-functools "functools: Higher-order functions and operations on callable objects.")
     module. In Python 3.0, the builtin has been dropped and [`reduce()`](https://docs.python.org/3/library/functools.html#functools.reduce "functools.reduce")
     is only available from `functools`; currently there are no plans to drop the builtin in the 2.x series. (Patched by Christian Heimes; [bpo-1739906](https://bugs.python.org/issue?@action=redirect&bpo=1739906)
    .)
    
*   When possible, the [`getpass`](https://docs.python.org/3/library/getpass.html#module-getpass "getpass: Portable reading of passwords and retrieval of the userid.")
     module will now use `/dev/tty` to print a prompt message and read the password, falling back to standard error and standard input. If the password may be echoed to the terminal, a warning is printed before the prompt is displayed. (Contributed by Gregory P. Smith.)
    
*   The [`glob.glob()`](https://docs.python.org/3/library/glob.html#glob.glob "glob.glob")
     function can now return Unicode filenames if a Unicode path was used and Unicode filenames are matched within the directory. ([bpo-1001604](https://bugs.python.org/issue?@action=redirect&bpo=1001604)
    )
    
*   A new function in the [`heapq`](https://docs.python.org/3/library/heapq.html#module-heapq "heapq: Heap queue algorithm (a.k.a. priority queue).")
     module, `merge(iter1, iter2, ...)`, takes any number of iterables returning data in sorted order, and returns a new generator that returns the contents of all the iterators, also in sorted order. For example:
    
    Copy
    
    \>>> list(heapq.merge(\[1, 3, 5, 9\], \[2, 8, 16\]))
    \[1, 2, 3, 5, 8, 9, 16\]
    
    Another new function, `heappushpop(heap, item)`, pushes _item_ onto _heap_, then pops off and returns the smallest item. This is more efficient than making a call to [`heappush()`](https://docs.python.org/3/library/heapq.html#heapq.heappush "heapq.heappush")
     and then [`heappop()`](https://docs.python.org/3/library/heapq.html#heapq.heappop "heapq.heappop")
    .
    
    [`heapq`](https://docs.python.org/3/library/heapq.html#module-heapq "heapq: Heap queue algorithm (a.k.a. priority queue).")
     is now implemented to only use less-than comparison, instead of the less-than-or-equal comparison it previously used. This makes `heapq`’s usage of a type match the [`list.sort()`](https://docs.python.org/3/builtins/stdtypes.html#list.sort "list.sort")
     method. (Contributed by Raymond Hettinger.)
    
*   An optional `timeout` parameter, specifying a timeout measured in seconds, was added to the [`httplib.HTTPConnection`](https://docs.python.org/3/library/http.client.html#http.client.HTTPConnection "http.client.HTTPConnection")
     and [`HTTPSConnection`](https://docs.python.org/3/library/http.client.html#http.client.HTTPSConnection "http.client.HTTPSConnection")
     class constructors. (Added by Facundo Batista.)
    
*   Most of the [`inspect`](https://docs.python.org/3/library/inspect.html#module-inspect "inspect: Extract information and source code from live objects.")
     module’s functions, such as `getmoduleinfo()` and `getargs()`, now return named tuples. In addition to behaving like tuples, the elements of the return value can also be accessed as attributes. (Contributed by Raymond Hettinger.)
    
    Some new functions in the module include [`isgenerator()`](https://docs.python.org/3/library/inspect.html#inspect.isgenerator "inspect.isgenerator")
    , [`isgeneratorfunction()`](https://docs.python.org/3/library/inspect.html#inspect.isgeneratorfunction "inspect.isgeneratorfunction")
    , and [`isabstract()`](https://docs.python.org/3/library/inspect.html#inspect.isabstract "inspect.isabstract")
    .
    
*   The [`itertools`](https://docs.python.org/3/library/itertools.html#module-itertools "itertools: Functions creating iterators for efficient looping.")
     module gained several new functions.
    
    `izip_longest(iter1, iter2, ...[, fillvalue])` makes tuples from each of the elements; if some of the iterables are shorter than others, the missing values are set to _fillvalue_. For example:
    
    Copy
    
    \>>> tuple(itertools.izip\_longest(\[1,2,3\], \[1,2,3,4,5\]))
    ((1, 1), (2, 2), (3, 3), (None, 4), (None, 5))
    
    `product(iter1, iter2, ..., [repeat=N])` returns the Cartesian product of the supplied iterables, a set of tuples containing every possible combination of the elements returned from each iterable.
    
    Copy
    
    \>>> list(itertools.product(\[1,2,3\], \[4,5,6\]))
    \[(1, 4), (1, 5), (1, 6),\
     (2, 4), (2, 5), (2, 6),\
     (3, 4), (3, 5), (3, 6)\]
    
    The optional _repeat_ keyword argument is used for taking the product of an iterable or a set of iterables with themselves, repeated _N_ times. With a single iterable argument, _N_\-tuples are returned:
    
    Copy
    
    \>>> list(itertools.product(\[1,2\], repeat\=3))
    \[(1, 1, 1), (1, 1, 2), (1, 2, 1), (1, 2, 2),\
     (2, 1, 1), (2, 1, 2), (2, 2, 1), (2, 2, 2)\]
    
    With two iterables, _2N_\-tuples are returned.
    
    Copy
    
    \>>> list(itertools.product(\[1,2\], \[3,4\], repeat\=2))
    \[(1, 3, 1, 3), (1, 3, 1, 4), (1, 3, 2, 3), (1, 3, 2, 4),\
     (1, 4, 1, 3), (1, 4, 1, 4), (1, 4, 2, 3), (1, 4, 2, 4),\
     (2, 3, 1, 3), (2, 3, 1, 4), (2, 3, 2, 3), (2, 3, 2, 4),\
     (2, 4, 1, 3), (2, 4, 1, 4), (2, 4, 2, 3), (2, 4, 2, 4)\]
    
    `combinations(iterable, r)` returns sub-sequences of length _r_ from the elements of _iterable_.
    
    Copy
    
    \>>> list(itertools.combinations('123', 2))
    \[('1', '2'), ('1', '3'), ('2', '3')\]
    \>>> list(itertools.combinations('123', 3))
    \[('1', '2', '3')\]
    \>>> list(itertools.combinations('1234', 3))
    \[('1', '2', '3'), ('1', '2', '4'),\
     ('1', '3', '4'), ('2', '3', '4')\]
    
    `permutations(iter[, r])` returns all the permutations of length _r_ of the iterable’s elements. If _r_ is not specified, it will default to the number of elements produced by the iterable.
    
    Copy
    
    \>>> list(itertools.permutations(\[1,2,3,4\], 2))
    \[(1, 2), (1, 3), (1, 4),\
     (2, 1), (2, 3), (2, 4),\
     (3, 1), (3, 2), (3, 4),\
     (4, 1), (4, 2), (4, 3)\]
    
    `itertools.chain(*iterables)` is an existing function in [`itertools`](https://docs.python.org/3/library/itertools.html#module-itertools "itertools: Functions creating iterators for efficient looping.")
     that gained a new constructor in Python 2.6. `itertools.chain.from_iterable(iterable)` takes a single iterable that should return other iterables. [`chain()`](https://docs.python.org/3/library/itertools.html#itertools.chain "itertools.chain")
     will then return all the elements of the first iterable, then all the elements of the second, and so on.
    
    Copy
    
    \>>> list(itertools.chain.from\_iterable(\[\[1,2,3\], \[4,5,6\]\]))
    \[1, 2, 3, 4, 5, 6\]
    
    (All contributed by Raymond Hettinger.)
    
*   The [`logging`](https://docs.python.org/3/library/logging.html#module-logging "logging: Flexible event logging system for applications.")
     module’s [`FileHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.FileHandler "logging.FileHandler")
     class and its subclasses [`WatchedFileHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.WatchedFileHandler "logging.handlers.WatchedFileHandler")
    , [`RotatingFileHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.RotatingFileHandler "logging.handlers.RotatingFileHandler")
    , and [`TimedRotatingFileHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.TimedRotatingFileHandler "logging.handlers.TimedRotatingFileHandler")
     now have an optional _delay_ parameter to their constructors. If _delay_ is true, opening of the log file is deferred until the first [`emit()`](https://docs.python.org/3/library/logging.handlers.html#logging.FileHandler.emit "logging.FileHandler.emit")
     call is made. (Contributed by Vinay Sajip.)
    
    [`TimedRotatingFileHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.TimedRotatingFileHandler "logging.handlers.TimedRotatingFileHandler")
     also has a _utc_ constructor parameter. If the argument is true, UTC time will be used in determining when midnight occurs and in generating filenames; otherwise local time will be used.
    
*   Several new functions were added to the [`math`](https://docs.python.org/3/library/math.html#module-math "math: Mathematical functions (sin() etc.).")
     module:
    
    *   [`isinf()`](https://docs.python.org/3/library/math.html#math.isinf "math.isinf")
         and [`isnan()`](https://docs.python.org/3/library/math.html#math.isnan "math.isnan")
         determine whether a given float is a (positive or negative) infinity or a NaN (Not a Number), respectively.
        
    *   [`copysign()`](https://docs.python.org/3/library/math.html#math.copysign "math.copysign")
         copies the sign bit of an IEEE 754 number, returning the absolute value of _x_ combined with the sign bit of _y_. For example, `math.copysign(1, -0.0)` returns -1.0. (Contributed by Christian Heimes.)
        
    *   [`factorial()`](https://docs.python.org/3/library/math.html#math.factorial "math.factorial")
         computes the factorial of a number. (Contributed by Raymond Hettinger; [bpo-2138](https://bugs.python.org/issue?@action=redirect&bpo=2138)
        .)
        
    *   [`fsum()`](https://docs.python.org/3/library/math.html#math.fsum "math.fsum")
         adds up the stream of numbers from an iterable, and is careful to avoid loss of precision through using partial sums. (Contributed by Jean Brouwers, Raymond Hettinger, and Mark Dickinson; [bpo-2819](https://bugs.python.org/issue?@action=redirect&bpo=2819)
        .)
        
    *   [`acosh()`](https://docs.python.org/3/library/math.html#math.acosh "math.acosh")
        , [`asinh()`](https://docs.python.org/3/library/math.html#math.asinh "math.asinh")
         and [`atanh()`](https://docs.python.org/3/library/math.html#math.atanh "math.atanh")
         compute the inverse hyperbolic functions.
        
    *   [`log1p()`](https://docs.python.org/3/library/math.html#math.log1p "math.log1p")
         returns the natural logarithm of _1+x_ (base _e_).
        
    *   [`trunc()`](https://docs.python.org/3/library/math.html#math.trunc "math.trunc")
         rounds a number toward zero, returning the closest [`Integral`](https://docs.python.org/3/library/numbers.html#numbers.Integral "numbers.Integral")
         that’s between the function’s argument and zero. Added as part of the backport of [PEP 3141’s type hierarchy for numbers](https://docs.python.org/3/whatsnew/2.6.html#pep-3141)
        .
        
*   The [`math`](https://docs.python.org/3/library/math.html#module-math "math: Mathematical functions (sin() etc.).")
     module has been improved to give more consistent behaviour across platforms, especially with respect to handling of floating-point exceptions and IEEE 754 special values.
    
    Whenever possible, the module follows the recommendations of the C99 standard about 754’s special values. For example, `sqrt(-1.)` should now give a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
     across almost all platforms, while `sqrt(float('NaN'))` should return a NaN on all IEEE 754 platforms. Where Annex ‘F’ of the C99 standard recommends signaling ‘divide-by-zero’ or ‘invalid’, Python will raise `ValueError`. Where Annex ‘F’ of the C99 standard recommends signaling ‘overflow’, Python will raise [`OverflowError`](https://docs.python.org/3/builtins/exceptions.html#OverflowError "OverflowError")
    . (See [bpo-711019](https://bugs.python.org/issue?@action=redirect&bpo=711019)
     and [bpo-1640](https://bugs.python.org/issue?@action=redirect&bpo=1640)
    .)
    
    (Contributed by Christian Heimes and Mark Dickinson.)
    
*   [`mmap`](https://docs.python.org/3/library/mmap.html#mmap.mmap "mmap.mmap")
     objects now have a [`rfind()`](https://docs.python.org/3/library/mmap.html#mmap.mmap.rfind "mmap.mmap.rfind")
     method that searches for a substring beginning at the end of the string and searching backwards. The [`find()`](https://docs.python.org/3/library/mmap.html#mmap.mmap.find "mmap.mmap.find")
     method also gained an _end_ parameter giving an index at which to stop searching. (Contributed by John Lenton.)
    
*   The [`operator`](https://docs.python.org/3/library/operator.html#module-operator "operator: Functions corresponding to the standard operators.")
     module gained a [`methodcaller()`](https://docs.python.org/3/library/operator.html#operator.methodcaller "operator.methodcaller")
     function that takes a name and an optional set of arguments, returning a callable that will call the named function on any arguments passed to it. For example:
    
    Copy
    
    \>>> \# Equivalent to lambda s: s.replace('old', 'new')
    \>>> replacer \= operator.methodcaller('replace', 'old', 'new')
    \>>> replacer('old wine in old bottles')
    'new wine in new bottles'
    
    (Contributed by Georg Brandl, after a suggestion by Gregory Petrosyan.)
    
    The [`attrgetter()`](https://docs.python.org/3/library/operator.html#operator.attrgetter "operator.attrgetter")
     function now accepts dotted names and performs the corresponding attribute lookups:
    
    Copy
    
    \>>> inst\_name \= operator.attrgetter(
    ...        '\_\_class\_\_.\_\_name\_\_')
    \>>> inst\_name('')
    'str'
    \>>> inst\_name(help)
    '\_Helper'
    
    (Contributed by Georg Brandl, after a suggestion by Barry Warsaw.)
    
*   The [`os`](https://docs.python.org/3/library/os.html#module-os "os: Miscellaneous operating system interfaces.")
     module now wraps several new system calls. `fchmod(fd, mode)` and `fchown(fd, uid, gid)` change the mode and ownership of an opened file, and `lchmod(path, mode)` changes the mode of a symlink. (Contributed by Georg Brandl and Christian Heimes.)
    
    [`chflags()`](https://docs.python.org/3/library/os.html#os.chflags "os.chflags")
     and [`lchflags()`](https://docs.python.org/3/library/os.html#os.lchflags "os.lchflags")
     are wrappers for the corresponding system calls (where they’re available), changing the flags set on a file. Constants for the flag values are defined in the [`stat`](https://docs.python.org/3/library/stat.html#module-stat "stat: Utilities for interpreting the results of os.stat(), os.lstat() and os.fstat().")
     module; some possible values include [`UF_IMMUTABLE`](https://docs.python.org/3/library/stat.html#stat.UF_IMMUTABLE "stat.UF_IMMUTABLE")
     to signal the file may not be changed and [`UF_APPEND`](https://docs.python.org/3/library/stat.html#stat.UF_APPEND "stat.UF_APPEND")
     to indicate that data can only be appended to the file. (Contributed by M. Levinson.)
    
    `os.closerange(low, high)` efficiently closes all file descriptors from _low_ to _high_, ignoring any errors and not including _high_ itself. This function is now used by the [`subprocess`](https://docs.python.org/3/library/subprocess.html#module-subprocess "subprocess: Subprocess management.")
     module to make starting processes faster. (Contributed by Georg Brandl; [bpo-1663329](https://bugs.python.org/issue?@action=redirect&bpo=1663329)
    .)
    
*   The `os.environ` object’s `clear()` method will now unset the environment variables using [`os.unsetenv()`](https://docs.python.org/3/library/os.html#os.unsetenv "os.unsetenv")
     in addition to clearing the object’s keys. (Contributed by Martin Horcicka; [bpo-1181](https://bugs.python.org/issue?@action=redirect&bpo=1181)
    .)
    
*   The [`os.walk()`](https://docs.python.org/3/library/os.html#os.walk "os.walk")
     function now has a `followlinks` parameter. If set to True, it will follow symlinks pointing to directories and visit the directory’s contents. For backward compatibility, the parameter’s default value is false. Note that the function can fall into an infinite recursion if there’s a symlink that points to a parent directory. ([bpo-1273829](https://bugs.python.org/issue?@action=redirect&bpo=1273829)
    )
    
*   In the [`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path "os.path: Operations on pathnames.")
     module, the [`splitext()`](https://docs.python.org/3/library/os.path.html#os.path.splitext "os.path.splitext")
     function has been changed to not split on leading period characters. This produces better results when operating on Unix’s dot-files. For example, `os.path.splitext('.ipython')` now returns `('.ipython', '')` instead of `('', '.ipython')`. ([bpo-1115886](https://bugs.python.org/issue?@action=redirect&bpo=1115886)
    )
    
    A new function, `os.path.relpath(path, start='.')`, returns a relative path from the `start` path, if it’s supplied, or from the current working directory to the destination `path`. (Contributed by Richard Barran; [bpo-1339796](https://bugs.python.org/issue?@action=redirect&bpo=1339796)
    .)
    
    On Windows, [`os.path.expandvars()`](https://docs.python.org/3/library/os.path.html#os.path.expandvars "os.path.expandvars")
     will now expand environment variables given in the form “%var%”, and “~user” will be expanded into the user’s home directory path. (Contributed by Josiah Carlson; [bpo-957650](https://bugs.python.org/issue?@action=redirect&bpo=957650)
    .)
    
*   The Python debugger provided by the [`pdb`](https://docs.python.org/3/library/pdb.html#module-pdb "pdb: The Python debugger for interactive interpreters.")
     module gained a new command: “run” restarts the Python program being debugged and can optionally take new command-line arguments for the program. (Contributed by Rocky Bernstein; [bpo-1393667](https://bugs.python.org/issue?@action=redirect&bpo=1393667)
    .)
    
*   The [`pdb.post_mortem()`](https://docs.python.org/3/library/pdb.html#pdb.post_mortem "pdb.post_mortem")
     function, used to begin debugging a traceback, will now use the traceback returned by [`sys.exc_info()`](https://docs.python.org/3/library/sys.html#sys.exc_info "sys.exc_info")
     if no traceback is supplied. (Contributed by Facundo Batista; [bpo-1106316](https://bugs.python.org/issue?@action=redirect&bpo=1106316)
    .)
    
*   The [`pickletools`](https://docs.python.org/3/library/pickletools.html#module-pickletools "pickletools: Contains extensive comments about the pickle protocols and pickle-machine opcodes, as well as some useful functions.")
     module now has an [`optimize()`](https://docs.python.org/3/library/pickletools.html#pickletools.optimize "pickletools.optimize")
     function that takes a string containing a pickle and removes some unused opcodes, returning a shorter pickle that contains the same data structure. (Contributed by Raymond Hettinger.)
    
*   A [`get_data()`](https://docs.python.org/3/library/pkgutil.html#pkgutil.get_data "pkgutil.get_data")
     function was added to the [`pkgutil`](https://docs.python.org/3/library/pkgutil.html#module-pkgutil "pkgutil: Utilities for the import system.")
     module that returns the contents of resource files included with an installed Python package. For example:
    
    Copy
    
    \>>> import pkgutil
    \>>> print pkgutil.get\_data('test', 'exception\_hierarchy.txt')
    BaseException
     +-- SystemExit
     +-- KeyboardInterrupt
     +-- GeneratorExit
     +-- Exception
          +-- StopIteration
          +-- StandardError
     ...
    
    (Contributed by Paul Moore; [bpo-2439](https://bugs.python.org/issue?@action=redirect&bpo=2439)
    .)
    
*   The `pyexpat` module’s `Parser` objects now allow setting their `buffer_size` attribute to change the size of the buffer used to hold character data. (Contributed by Achim Gaedke; [bpo-1137](https://bugs.python.org/issue?@action=redirect&bpo=1137)
    .)
    
*   The [`queue`](https://docs.python.org/3/library/queue.html#module-queue "queue: A synchronized queue class.")
     module now provides queue variants that retrieve entries in different orders. The [`PriorityQueue`](https://docs.python.org/3/library/queue.html#queue.PriorityQueue "queue.PriorityQueue")
     class stores queued items in a heap and retrieves them in priority order, and [`LifoQueue`](https://docs.python.org/3/library/queue.html#queue.LifoQueue "queue.LifoQueue")
     retrieves the most recently added entries first, meaning that it behaves like a stack. (Contributed by Raymond Hettinger.)
    
*   The [`random`](https://docs.python.org/3/library/random.html#module-random "random: Generate pseudo-random numbers with various common distributions.")
     module’s [`Random`](https://docs.python.org/3/library/random.html#random.Random "random.Random")
     objects can now be pickled on a 32-bit system and unpickled on a 64-bit system, and vice versa. Unfortunately, this change also means that Python 2.6’s `Random` objects can’t be unpickled correctly on earlier versions of Python. (Contributed by Shawn Ligocki; [bpo-1727780](https://bugs.python.org/issue?@action=redirect&bpo=1727780)
    .)
    
    The new `triangular(low, high, mode)` function returns random numbers following a triangular distribution. The returned values are between _low_ and _high_, not including _high_ itself, and with _mode_ as the most frequently occurring value in the distribution. (Contributed by Wladmir van der Laan and Raymond Hettinger; [bpo-1681432](https://bugs.python.org/issue?@action=redirect&bpo=1681432)
    .)
    
*   Long regular expression searches carried out by the [`re`](https://docs.python.org/3/library/re.html#module-re "re: Regular expression operations.")
     module will check for signals being delivered, so time-consuming searches can now be interrupted. (Contributed by Josh Hoyt and Ralf Schmitt; [bpo-846388](https://bugs.python.org/issue?@action=redirect&bpo=846388)
    .)
    
    The regular expression module is implemented by compiling bytecodes for a tiny regex-specific virtual machine. Untrusted code could create malicious strings of bytecode directly and cause crashes, so Python 2.6 includes a verifier for the regex bytecode. (Contributed by Guido van Rossum from work for Google App Engine; [bpo-3487](https://bugs.python.org/issue?@action=redirect&bpo=3487)
    .)
    
*   The [`rlcompleter`](https://docs.python.org/3/library/rlcompleter.html#module-rlcompleter "rlcompleter: Python identifier completion, suitable for the GNU readline library.")
     module’s [`complete()`](https://docs.python.org/3/library/rlcompleter.html#rlcompleter.Completer.complete "rlcompleter.Completer.complete")
     method will now ignore exceptions triggered while evaluating a name. (Fixed by Lorenz Quack; [bpo-2250](https://bugs.python.org/issue?@action=redirect&bpo=2250)
    .)
    
*   The [`sched`](https://docs.python.org/3/library/sched.html#module-sched "sched: General purpose event scheduler.")
     module’s [`scheduler`](https://docs.python.org/3/library/sched.html#sched.scheduler "sched.scheduler")
     instances now have a read-only [`queue`](https://docs.python.org/3/library/queue.html#module-queue "queue: A synchronized queue class.")
     attribute that returns the contents of the scheduler’s queue, represented as a list of named tuples with the fields `(time, priority, action, argument)`. (Contributed by Raymond Hettinger; [bpo-1861](https://bugs.python.org/issue?@action=redirect&bpo=1861)
    .)
    
*   The [`select`](https://docs.python.org/3/library/select.html#module-select "select: Wait for I/O completion on multiple streams.")
     module now has wrapper functions for the Linux `epoll()` and BSD `kqueue()` system calls. [`modify()`](https://docs.python.org/3/library/select.html#select.poll.modify "select.poll.modify")
     method was added to the existing `poll` objects; `pollobj.modify(fd, eventmask)` takes a file descriptor or file object and an event mask, modifying the recorded event mask for that file. (Contributed by Christian Heimes; [bpo-1657](https://bugs.python.org/issue?@action=redirect&bpo=1657)
    .)
    
*   The [`shutil.copytree()`](https://docs.python.org/3/library/shutil.html#shutil.copytree "shutil.copytree")
     function now has an optional _ignore_ argument that takes a callable object. This callable will receive each directory path and a list of the directory’s contents, and returns a list of names that will be ignored, not copied.
    
    The [`shutil`](https://docs.python.org/3/library/shutil.html#module-shutil "shutil: High-level file operations, including copying.")
     module also provides an [`ignore_patterns()`](https://docs.python.org/3/library/shutil.html#shutil.ignore_patterns "shutil.ignore_patterns")
     function for use with this new parameter. `ignore_patterns()` takes an arbitrary number of glob-style patterns and returns a callable that will ignore any files and directories that match any of these patterns. The following example copies a directory tree, but skips both `.svn` directories and Emacs backup files, which have names ending with ‘~’:
    
    Copy
    
    shutil.copytree('Doc/library', '/tmp/library',
                    ignore\=shutil.ignore\_patterns('\*~', '.svn'))
    
    (Contributed by Tarek Ziadé; [bpo-2663](https://bugs.python.org/issue?@action=redirect&bpo=2663)
    .)
    
*   Integrating signal handling with GUI handling event loops like those used by Tkinter or GTk+ has long been a problem; most software ends up polling, waking up every fraction of a second to check if any GUI events have occurred. The [`signal`](https://docs.python.org/3/library/signal.html#module-signal "signal: Set handlers for asynchronous events.")
     module can now make this more efficient. Calling `signal.set_wakeup_fd(fd)` sets a file descriptor to be used; when a signal is received, a byte is written to that file descriptor. There’s also a C-level function, [`PySignal_SetWakeupFd()`](https://docs.python.org/3/c-api/exceptions.html#c.PySignal_SetWakeupFd "PySignal_SetWakeupFd")
    , for setting the descriptor.
    
    Event loops will use this by opening a pipe to create two descriptors, one for reading and one for writing. The writable descriptor will be passed to [`set_wakeup_fd()`](https://docs.python.org/3/library/signal.html#signal.set_wakeup_fd "signal.set_wakeup_fd")
    , and the readable descriptor will be added to the list of descriptors monitored by the event loop via `select()` or `poll()`. On receiving a signal, a byte will be written and the main event loop will be woken up, avoiding the need to poll.
    
    (Contributed by Adam Olsen; [bpo-1583](https://bugs.python.org/issue?@action=redirect&bpo=1583)
    .)
    
    The [`siginterrupt()`](https://docs.python.org/3/library/signal.html#signal.siginterrupt "signal.siginterrupt")
     function is now available from Python code, and allows changing whether signals can interrupt system calls or not. (Contributed by Ralf Schmitt.)
    
    The [`setitimer()`](https://docs.python.org/3/library/signal.html#signal.setitimer "signal.setitimer")
     and [`getitimer()`](https://docs.python.org/3/library/signal.html#signal.getitimer "signal.getitimer")
     functions have also been added (where they’re available). `setitimer()` allows setting interval timers that will cause a signal to be delivered to the process after a specified time, measured in wall-clock time, consumed process time, or combined process+system time. (Contributed by Guilherme Polo; [bpo-2240](https://bugs.python.org/issue?@action=redirect&bpo=2240)
    .)
    
*   The [`smtplib`](https://docs.python.org/3/library/smtplib.html#module-smtplib "smtplib: SMTP protocol client (requires sockets).")
     module now supports SMTP over SSL thanks to the addition of the [`SMTP_SSL`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP_SSL "smtplib.SMTP_SSL")
     class. This class supports an interface identical to the existing [`SMTP`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP "smtplib.SMTP")
     class. (Contributed by Monty Taylor.) Both class constructors also have an optional `timeout` parameter that specifies a timeout for the initial connection attempt, measured in seconds. (Contributed by Facundo Batista.)
    
    An implementation of the LMTP protocol ([**RFC 2033**](https://datatracker.ietf.org/doc/html/rfc2033.html)
    ) was also added to the module. LMTP is used in place of SMTP when transferring e-mail between agents that don’t manage a mail queue. (LMTP implemented by Leif Hedstrom; [bpo-957003](https://bugs.python.org/issue?@action=redirect&bpo=957003)
    .)
    
    [`smtplib.SMTP.starttls()`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.starttls "smtplib.SMTP.starttls")
     now complies with [**RFC 3207**](https://datatracker.ietf.org/doc/html/rfc3207.html)
     and forgets any knowledge obtained from the server not obtained from the TLS negotiation itself. (Patch contributed by Bill Fenner; [bpo-829951](https://bugs.python.org/issue?@action=redirect&bpo=829951)
    .)
    
*   The [`socket`](https://docs.python.org/3/library/socket.html#module-socket "socket: Low-level networking interface.")
     module now supports TIPC ([https://tipc.sourceforge.net/](https://tipc.sourceforge.net/)
    ), a high-performance non-IP-based protocol designed for use in clustered environments. TIPC addresses are 4- or 5-tuples. (Contributed by Alberto Bertogli; [bpo-1646](https://bugs.python.org/issue?@action=redirect&bpo=1646)
    .)
    
    A new function, [`create_connection()`](https://docs.python.org/3/library/socket.html#socket.create_connection "socket.create_connection")
    , takes an address and connects to it using an optional timeout value, returning the connected socket object. This function also looks up the address’s type and connects to it using IPv4 or IPv6 as appropriate. Changing your code to use `create_connection()` instead of `socket(socket.AF_INET, ...)` may be all that’s required to make your code work with IPv6.
    
*   The base classes in the [`SocketServer`](https://docs.python.org/3/library/socketserver.html#module-socketserver "socketserver: A framework for network servers.")
     module now support calling a [`handle_timeout()`](https://docs.python.org/3/library/socketserver.html#socketserver.BaseServer.handle_timeout "socketserver.BaseServer.handle_timeout")
     method after a span of inactivity specified by the server’s [`timeout`](https://docs.python.org/3/library/socketserver.html#socketserver.BaseServer.timeout "socketserver.BaseServer.timeout")
     attribute. (Contributed by Michael Pomraning.) The [`serve_forever()`](https://docs.python.org/3/library/socketserver.html#socketserver.BaseServer.serve_forever "socketserver.BaseServer.serve_forever")
     method now takes an optional poll interval measured in seconds, controlling how often the server will check for a shutdown request. (Contributed by Pedro Werneck and Jeffrey Yasskin; [bpo-742598](https://bugs.python.org/issue?@action=redirect&bpo=742598)
    , [bpo-1193577](https://bugs.python.org/issue?@action=redirect&bpo=1193577)
    .)
    
*   The [`sqlite3`](https://docs.python.org/3/library/sqlite3.html#module-sqlite3 "sqlite3: A DB-API 2.0 implementation using SQLite 3.x.")
     module, maintained by Gerhard Häring, has been updated from version 2.3.2 in Python 2.5 to version 2.4.1.
    
*   The [`struct`](https://docs.python.org/3/library/struct.html#module-struct "struct: Interpret bytes as packed binary data.")
     module now supports the C99 \_Bool type, using the format character `'?'`. (Contributed by David Remahl.)
    
*   The [`Popen`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen")
     objects provided by the [`subprocess`](https://docs.python.org/3/library/subprocess.html#module-subprocess "subprocess: Subprocess management.")
     module now have [`terminate()`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.terminate "subprocess.Popen.terminate")
    , [`kill()`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.kill "subprocess.Popen.kill")
    , and [`send_signal()`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.send_signal "subprocess.Popen.send_signal")
     methods. On Windows, `send_signal()` only supports the [`SIGTERM`](https://docs.python.org/3/library/signal.html#signal.SIGTERM "signal.SIGTERM")
     signal, and all these methods are aliases for the Win32 API function `TerminateProcess()`. (Contributed by Christian Heimes.)
    
*   A new variable in the [`sys`](https://docs.python.org/3/library/sys.html#module-sys "sys: Access system-specific parameters and functions.")
     module, [`float_info`](https://docs.python.org/3/library/sys.html#sys.float_info "sys.float_info")
    , is an object containing information derived from the `float.h` file about the platform’s floating-point support. Attributes of this object include [`mant_dig`](https://docs.python.org/3/library/sys.html#sys.float_info.mant_dig "sys.float_info.mant_dig")
     (number of digits in the mantissa), [`epsilon`](https://docs.python.org/3/library/sys.html#sys.float_info.epsilon "sys.float_info.epsilon")
     (smallest difference between 1.0 and the next largest value representable), and several others. (Contributed by Christian Heimes; [bpo-1534](https://bugs.python.org/issue?@action=redirect&bpo=1534)
    .)
    
    Another new variable, [`dont_write_bytecode`](https://docs.python.org/3/library/sys.html#sys.dont_write_bytecode "sys.dont_write_bytecode")
    , controls whether Python writes any `.pyc` or `.pyo` files on importing a module. If this variable is true, the compiled files are not written. The variable is initially set on start-up by supplying the [`-B`](https://docs.python.org/3/using/cmdline.html#cmdoption-B)
     switch to the Python interpreter, or by setting the [`PYTHONDONTWRITEBYTECODE`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONDONTWRITEBYTECODE)
     environment variable before running the interpreter. Python code can subsequently change the value of this variable to control whether bytecode files are written or not. (Contributed by Neal Norwitz and Georg Brandl.)
    
    Information about the command-line arguments supplied to the Python interpreter is available by reading attributes of a named tuple available as `sys.flags`. For example, the [`verbose`](https://docs.python.org/3/library/sys.html#sys.flags.verbose "sys.flags.verbose")
     attribute is true if Python was executed in verbose mode, [`debug`](https://docs.python.org/3/library/sys.html#sys.flags.debug "sys.flags.debug")
     is true in debugging mode, etc. These attributes are all read-only. (Contributed by Christian Heimes.)
    
    A new function, [`getsizeof()`](https://docs.python.org/3/library/sys.html#sys.getsizeof "sys.getsizeof")
    , takes a Python object and returns the amount of memory used by the object, measured in bytes. Built-in objects return correct results; third-party extensions may not, but can define a `__sizeof__()` method to return the object’s size. (Contributed by Robert Schuppenies; [bpo-2898](https://bugs.python.org/issue?@action=redirect&bpo=2898)
    .)
    
    It’s now possible to determine the current profiler and tracer functions by calling [`sys.getprofile()`](https://docs.python.org/3/library/sys.html#sys.getprofile "sys.getprofile")
     and [`sys.gettrace()`](https://docs.python.org/3/library/sys.html#sys.gettrace "sys.gettrace")
    . (Contributed by Georg Brandl; [bpo-1648](https://bugs.python.org/issue?@action=redirect&bpo=1648)
    .)
    
*   The [`tarfile`](https://docs.python.org/3/library/tarfile.html#module-tarfile "tarfile: Read and write tar-format archive files.")
     module now supports POSIX.1-2001 (pax) tarfiles in addition to the POSIX.1-1988 (ustar) and GNU tar formats that were already supported. The default format is GNU tar; specify the `format` parameter to open a file using a different format:
    
    Copy
    
    tar \= tarfile.open("output.tar", "w",
                       format\=tarfile.PAX\_FORMAT)
    
    The new `encoding` and `errors` parameters specify an encoding and an error handling scheme for character conversions. `'strict'`, `'ignore'`, and `'replace'` are the three standard ways Python can handle errors,; `'utf-8'` is a special value that replaces bad characters with their UTF-8 representation. (Character conversions occur because the PAX format supports Unicode filenames, defaulting to UTF-8 encoding.)
    
    The [`tarfile.TarFile.add()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.add "tarfile.TarFile.add")
     method now accepts an `exclude` argument that’s a function that can be used to exclude certain filenames from an archive. The function must take a filename and return true if the file should be excluded or false if it should be archived. The function is applied to both the name initially passed to `add()` and to the names of files in recursively added directories.
    
    (All changes contributed by Lars Gustäbel).
    
*   An optional `timeout` parameter was added to the `telnetlib.Telnet` class constructor, specifying a timeout measured in seconds. (Added by Facundo Batista.)
    
*   The [`tempfile.NamedTemporaryFile`](https://docs.python.org/3/library/tempfile.html#tempfile.NamedTemporaryFile "tempfile.NamedTemporaryFile")
     class usually deletes the temporary file it created when the file is closed. This behaviour can now be changed by passing `delete=False` to the constructor. (Contributed by Damien Miller; [bpo-1537850](https://bugs.python.org/issue?@action=redirect&bpo=1537850)
    .)
    
    A new class, [`SpooledTemporaryFile`](https://docs.python.org/3/library/tempfile.html#tempfile.SpooledTemporaryFile "tempfile.SpooledTemporaryFile")
    , behaves like a temporary file but stores its data in memory until a maximum size is exceeded. On reaching that limit, the contents will be written to an on-disk temporary file. (Contributed by Dustin J. Mitchell.)
    
    The [`NamedTemporaryFile`](https://docs.python.org/3/library/tempfile.html#tempfile.NamedTemporaryFile "tempfile.NamedTemporaryFile")
     and [`SpooledTemporaryFile`](https://docs.python.org/3/library/tempfile.html#tempfile.SpooledTemporaryFile "tempfile.SpooledTemporaryFile")
     classes both work as context managers, so you can write `with tempfile.NamedTemporaryFile() as tmp: ...`. (Contributed by Alexander Belopolsky; [bpo-2021](https://bugs.python.org/issue?@action=redirect&bpo=2021)
    .)
    
*   The [`test.test_support`](https://docs.python.org/3/library/test.html#module-test.support "test.support: Support for Python's regression test suite.")
     module gained a number of context managers useful for writing tests. [`EnvironmentVarGuard()`](https://docs.python.org/3/library/test.html#test.support.os_helper.EnvironmentVarGuard "test.support.os_helper.EnvironmentVarGuard")
     is a context manager that temporarily changes environment variables and automatically restores them to their old values.
    
    Another context manager, `TransientResource`, can surround calls to resources that may or may not be available; it will catch and ignore a specified list of exceptions. For example, a network test may ignore certain failures when connecting to an external web site:
    
    Copy
    
    with test\_support.TransientResource(IOError,
                                    errno\=errno.ETIMEDOUT):
        f \= urllib.urlopen('https://sf.net')
        ...
    
    Finally, [`check_warnings()`](https://docs.python.org/3/library/test.html#test.support.warnings_helper.check_warnings "test.support.warnings_helper.check_warnings")
     resets the [`warnings`](https://docs.python.org/3/library/warnings.html#module-warnings "warnings: Issue warning messages and control their disposition.")
     module’s warning filters and returns an object that will record all warning messages triggered ([bpo-3781](https://bugs.python.org/issue?@action=redirect&bpo=3781)
    ):
    
    Copy
    
    with test\_support.check\_warnings() as wrec:
        warnings.simplefilter("always")
        \# ... code that triggers a warning ...
        assert str(wrec.message) \== "function is outdated"
        assert len(wrec.warnings) \== 1, "Multiple warnings raised"
    
    (Contributed by Brett Cannon.)
    
*   The [`textwrap`](https://docs.python.org/3/library/textwrap.html#module-textwrap "textwrap: Text wrapping and filling")
     module can now preserve existing whitespace at the beginnings and ends of the newly created lines by specifying `drop_whitespace=False` as an argument:
    
    Copy
    
    \>>> S \= """This  sentence  has a bunch   of
    ...   extra   whitespace."""
    \>>> print textwrap.fill(S, width\=15)
    This  sentence
    has a bunch
    of    extra
    whitespace.
    \>>> print textwrap.fill(S, drop\_whitespace\=False, width\=15)
    This  sentence
      has a bunch
       of    extra
       whitespace.
    \>>>
    
    (Contributed by Dwayne Bailey; [bpo-1581073](https://bugs.python.org/issue?@action=redirect&bpo=1581073)
    .)
    
*   The [`threading`](https://docs.python.org/3/library/threading.html#module-threading "threading: Thread-based parallelism.")
     module API is being changed to use properties such as [`daemon`](https://docs.python.org/3/library/threading.html#threading.Thread.daemon "threading.Thread.daemon")
     instead of `setDaemon()` and `isDaemon()` methods, and some methods have been renamed to use underscores instead of camel-case; for example, the `activeCount()` method is renamed to [`active_count()`](https://docs.python.org/3/library/threading.html#threading.active_count "threading.active_count")
    . Both the 2.6 and 3.0 versions of the module support the same properties and renamed methods, but don’t remove the old methods. No date has been set for the deprecation of the old APIs in Python 3.x; the old APIs won’t be removed in any 2.x version. (Carried out by several people, most notably Benjamin Peterson.)
    
    The [`threading`](https://docs.python.org/3/library/threading.html#module-threading "threading: Thread-based parallelism.")
     module’s [`Thread`](https://docs.python.org/3/library/threading.html#threading.Thread "threading.Thread")
     objects gained an [`ident`](https://docs.python.org/3/library/threading.html#threading.Thread.ident "threading.Thread.ident")
     property that returns the thread’s identifier, a nonzero integer. (Contributed by Gregory P. Smith; [bpo-2871](https://bugs.python.org/issue?@action=redirect&bpo=2871)
    .)
    
*   The [`timeit`](https://docs.python.org/3/library/timeit.html#module-timeit "timeit: Measure the execution time of small code snippets.")
     module now accepts callables as well as strings for the statement being timed and for the setup code. Two convenience functions were added for creating [`Timer`](https://docs.python.org/3/library/timeit.html#timeit.Timer "timeit.Timer")
     instances: `repeat(stmt, setup, timer, repeat, number)` and `timeit(stmt, setup, timer, number)` create an instance and call the corresponding method. (Contributed by Erik Demaine; [bpo-1533909](https://bugs.python.org/issue?@action=redirect&bpo=1533909)
    .)
    
*   The [`tkinter`](https://docs.python.org/3/library/tkinter.html#module-tkinter "tkinter: Interface to Tcl/Tk for graphical user interfaces")
     module now accepts lists and tuples for options, separating the elements by spaces before passing the resulting value to Tcl/Tk. (Contributed by Guilherme Polo; [bpo-2906](https://bugs.python.org/issue?@action=redirect&bpo=2906)
    .)
    
*   The [`turtle`](https://docs.python.org/3/library/turtle.html#module-turtle "turtle: An educational framework for simple graphics applications")
     module for turtle graphics was greatly enhanced by Gregor Lingl. New features in the module include:
    
    *   Better animation of turtle movement and rotation.
        
    *   Control over turtle movement using the new [`delay()`](https://docs.python.org/3/library/turtle.html#turtle.delay "turtle.delay")
        , [`tracer()`](https://docs.python.org/3/library/turtle.html#turtle.tracer "turtle.tracer")
        , and [`speed()`](https://docs.python.org/3/library/turtle.html#turtle.speed "turtle.speed")
         methods.
        
    *   The ability to set new shapes for the turtle, and to define a new coordinate system.
        
    *   Turtles now have an [`undo()`](https://docs.python.org/3/library/turtle.html#turtle.undo "turtle.undo")
         method that can roll back actions.
        
    *   Simple support for reacting to input events such as mouse and keyboard activity, making it possible to write simple games.
        
    *   A `turtle.cfg` file can be used to customize the starting appearance of the turtle’s screen.
        
    *   The module’s docstrings can be replaced by new docstrings that have been translated into another language.
        
    
    ([bpo-1513695](https://bugs.python.org/issue?@action=redirect&bpo=1513695)
    )
    
*   An optional `timeout` parameter was added to the [`urllib.urlopen`](https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen "urllib.request.urlopen")
     function and the `urllib.ftpwrapper` class constructor, as well as the `urllib2.urlopen` function. The parameter specifies a timeout measured in seconds. For example:
    
    Copy
    
    \>>> u \= urllib2.urlopen("http://slow.example.com",
    ...                     timeout\=3)
    Traceback (most recent call last):
      ...
    urllib2.URLError: <urlopen error timed out>
    \>>>
    
    (Added by Facundo Batista.)
    
*   The Unicode database provided by the [`unicodedata`](https://docs.python.org/3/library/unicodedata.html#module-unicodedata "unicodedata: Access the Unicode Database.")
     module has been updated to version 5.1.0. (Updated by Martin von Löwis; [bpo-3811](https://bugs.python.org/issue?@action=redirect&bpo=3811)
    .)
    
*   The [`warnings`](https://docs.python.org/3/library/warnings.html#module-warnings "warnings: Issue warning messages and control their disposition.")
     module’s [`formatwarning()`](https://docs.python.org/3/library/warnings.html#warnings.formatwarning "warnings.formatwarning")
     and [`showwarning()`](https://docs.python.org/3/library/warnings.html#warnings.showwarning "warnings.showwarning")
     gained an optional _line_ argument that can be used to supply the line of source code. (Added as part of [bpo-1631171](https://bugs.python.org/issue?@action=redirect&bpo=1631171)
    , which re-implemented part of the `warnings` module in C code.)
    
    A new function, [`catch_warnings()`](https://docs.python.org/3/library/warnings.html#warnings.catch_warnings "warnings.catch_warnings")
    , is a context manager intended for testing purposes that lets you temporarily modify the warning filters and then restore their original values ([bpo-3781](https://bugs.python.org/issue?@action=redirect&bpo=3781)
    ).
    
*   The XML-RPC [`SimpleXMLRPCServer`](https://docs.python.org/3/library/xmlrpc.server.html#xmlrpc.server.SimpleXMLRPCServer "xmlrpc.server.SimpleXMLRPCServer")
     and [`DocXMLRPCServer`](https://docs.python.org/3/library/xmlrpc.server.html#xmlrpc.server.DocXMLRPCServer "xmlrpc.server.DocXMLRPCServer")
     classes can now be prevented from immediately opening and binding to their socket by passing `False` as the _bind\_and\_activate_ constructor parameter. This can be used to modify the instance’s [`allow_reuse_address`](https://docs.python.org/3/library/socketserver.html#socketserver.BaseServer.allow_reuse_address "socketserver.BaseServer.allow_reuse_address")
     attribute before calling the [`server_bind()`](https://docs.python.org/3/library/socketserver.html#socketserver.BaseServer.server_bind "socketserver.BaseServer.server_bind")
     and [`server_activate()`](https://docs.python.org/3/library/socketserver.html#socketserver.BaseServer.server_activate "socketserver.BaseServer.server_activate")
     methods to open the socket and begin listening for connections. (Contributed by Peter Parente; [bpo-1599845](https://bugs.python.org/issue?@action=redirect&bpo=1599845)
    .)
    
    [`SimpleXMLRPCServer`](https://docs.python.org/3/library/xmlrpc.server.html#xmlrpc.server.SimpleXMLRPCServer "xmlrpc.server.SimpleXMLRPCServer")
     also has a `_send_traceback_header` attribute; if true, the exception and formatted traceback are returned as HTTP headers “X-Exception” and “X-Traceback”. This feature is for debugging purposes only and should not be used on production servers because the tracebacks might reveal passwords or other sensitive information. (Contributed by Alan McIntyre as part of his project for Google’s Summer of Code 2007.)
    
*   The [`xmlrpclib`](https://docs.python.org/3/library/xmlrpc.client.html#module-xmlrpc.client "xmlrpc.client: XML-RPC client access.")
     module no longer automatically converts [`datetime.date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date")
     and [`datetime.time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time")
     to the [`xmlrpclib.DateTime`](https://docs.python.org/3/library/xmlrpc.client.html#xmlrpc.client.DateTime "xmlrpc.client.DateTime")
     type; the conversion semantics were not necessarily correct for all applications. Code using `xmlrpclib` should convert `date` and `time` instances. ([bpo-1330538](https://bugs.python.org/issue?@action=redirect&bpo=1330538)
    ) The code can also handle dates before 1900 (contributed by Ralf Schmitt; [bpo-2014](https://bugs.python.org/issue?@action=redirect&bpo=2014)
    ) and 64-bit integers represented by using `<i8>` in XML-RPC responses (contributed by Riku Lindblad; [bpo-2985](https://bugs.python.org/issue?@action=redirect&bpo=2985)
    ).
    
*   The [`zipfile`](https://docs.python.org/3/library/zipfile.html#module-zipfile "zipfile: Read and write ZIP-format archive files.")
     module’s [`ZipFile`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile "zipfile.ZipFile")
     class now has [`extract()`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.extract "zipfile.ZipFile.extract")
     and [`extractall()`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.extractall "zipfile.ZipFile.extractall")
     methods that will unpack a single file or all the files in the archive to the current directory, or to a specified directory:
    
    Copy
    
    z \= zipfile.ZipFile('python-251.zip')
    
    \# Unpack a single file, writing it relative
    \# to the /tmp directory.
    z.extract('Python/sysmodule.c', '/tmp')
    
    \# Unpack all the files in the archive.
    z.extractall()
    
    (Contributed by Alan McIntyre; [bpo-467924](https://bugs.python.org/issue?@action=redirect&bpo=467924)
    .)
    
    The [`open()`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.open "zipfile.ZipFile.open")
    , [`read()`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.read "zipfile.ZipFile.read")
     and [`extract()`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.extract "zipfile.ZipFile.extract")
     methods can now take either a filename or a [`ZipInfo`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo "zipfile.ZipInfo")
     object. This is useful when an archive accidentally contains a duplicated filename. (Contributed by Graham Horler; [bpo-1775025](https://bugs.python.org/issue?@action=redirect&bpo=1775025)
    .)
    
    Finally, [`zipfile`](https://docs.python.org/3/library/zipfile.html#module-zipfile "zipfile: Read and write ZIP-format archive files.")
     now supports using Unicode filenames for archived files. (Contributed by Alexey Borzenkov; [bpo-1734346](https://bugs.python.org/issue?@action=redirect&bpo=1734346)
    .)
    

### The [`ast`](https://docs.python.org/3/library/ast.html#module-ast "ast: Abstract Syntax Tree classes and manipulation.")
 module[¶](https://docs.python.org/3/whatsnew/2.6.html#the-ast-module "Link to this heading")

The [`ast`](https://docs.python.org/3/library/ast.html#module-ast "ast: Abstract Syntax Tree classes and manipulation.")
 module provides an Abstract Syntax Tree representation of Python code, and Armin Ronacher contributed a set of helper functions that perform a variety of common tasks. These will be useful for HTML templating packages, code analyzers, and similar tools that process Python code.

The [`parse()`](https://docs.python.org/3/library/ast.html#ast.parse "ast.parse")
 function takes an expression and returns an AST. The [`dump()`](https://docs.python.org/3/library/ast.html#ast.dump "ast.dump")
 function outputs a representation of a tree, suitable for debugging:

Copy

import ast

t \= ast.parse("""
d = {}
for i in 'abcdefghijklm':
    d\[i + i\] = ord(i) - ord('a') + 1
print d
""")
print ast.dump(t)

This outputs a deeply nested tree:

Copy

Module(body\=\[\
  Assign(targets\=\[\
    Name(id\='d', ctx\=Store())\
   \], value\=Dict(keys\=\[\], values\=\[\]))\
  For(target\=Name(id\='i', ctx\=Store()),\
      iter\=Str(s\='abcdefghijklm'), body\=\[\
    Assign(targets\=\[\
      Subscript(value\=\
        Name(id\='d', ctx\=Load()),\
          slice\=\
          Index(value\=\
            BinOp(left\=Name(id\='i', ctx\=Load()), op\=Add(),\
             right\=Name(id\='i', ctx\=Load()))), ctx\=Store())\
     \], value\=\
     BinOp(left\=\
      BinOp(left\=\
       Call(func\=\
        Name(id\='ord', ctx\=Load()), args\=\[\
          Name(id\='i', ctx\=Load())\
         \], keywords\=\[\], starargs\=None, kwargs\=None),\
       op\=Sub(), right\=Call(func\=\
        Name(id\='ord', ctx\=Load()), args\=\[\
          Str(s\='a')\
         \], keywords\=\[\], starargs\=None, kwargs\=None)),\
       op\=Add(), right\=Num(n\=1)))\
    \], orelse\=\[\])\
   Print(dest\=None, values\=\[\
     Name(id\='d', ctx\=Load())\
   \], nl\=True)\
 \])

The [`literal_eval()`](https://docs.python.org/3/library/ast.html#ast.literal_eval "ast.literal_eval")
 method takes a string or an AST representing a literal expression, parses and evaluates it, and returns the resulting value. A literal expression is a Python expression containing only strings, numbers, dictionaries, etc. but no statements or function calls. If you need to evaluate an expression but cannot accept the security risk of using an [`eval()`](https://docs.python.org/3/builtins/functions.html#eval "eval")
 call, `literal_eval()` will handle it safely:

Copy

\>>> literal \= '("a", "b", {2:4, 3:8, 1:2})'
\>>> print ast.literal\_eval(literal)
('a', 'b', {1: 2, 2: 4, 3: 8})
\>>> print ast.literal\_eval('"a" + "b"')
Traceback (most recent call last):
  ...
ValueError: malformed string

The module also includes [`NodeVisitor`](https://docs.python.org/3/library/ast.html#ast.NodeVisitor "ast.NodeVisitor")
 and [`NodeTransformer`](https://docs.python.org/3/library/ast.html#ast.NodeTransformer "ast.NodeTransformer")
 classes for traversing and modifying an AST, and functions for common transformations such as changing line numbers.

### The `future_builtins` module[¶](https://docs.python.org/3/whatsnew/2.6.html#the-future-builtins-module "Link to this heading")

Python 3.0 makes many changes to the repertoire of built-in functions, and most of the changes can’t be introduced in the Python 2.x series because they would break compatibility. The `future_builtins` module provides versions of these built-in functions that can be imported when writing 3.0-compatible code.

The functions in this module currently include:

*   `ascii(obj)`: equivalent to [`repr()`](https://docs.python.org/3/builtins/functions.html#repr "repr")
    . In Python 3.0, `repr()` will return a Unicode string, while [`ascii()`](https://docs.python.org/3/builtins/functions.html#ascii "ascii")
     will return a pure ASCII bytestring.
    
*   `filter(predicate, iterable)`, `map(func, iterable1, ...)`: the 3.0 versions return iterators, unlike the 2.x builtins which return lists.
    
*   `hex(value)`, `oct(value)`: instead of calling the `__hex__()` or `__oct__()` methods, these versions will call the [`__index__()`](https://docs.python.org/3/reference/datamodel.html#object.__index__ "object.__index__")
     method and convert the result to hexadecimal or octal. [`oct()`](https://docs.python.org/3/builtins/functions.html#oct "oct")
     will use the new `0o` notation for its result.
    

### The [`json`](https://docs.python.org/3/library/json.html#module-json "json: Encode and decode the JSON format.")
 module: JavaScript Object Notation[¶](https://docs.python.org/3/whatsnew/2.6.html#the-json-module-javascript-object-notation "Link to this heading")

The new [`json`](https://docs.python.org/3/library/json.html#module-json "json: Encode and decode the JSON format.")
 module supports the encoding and decoding of Python types in JSON (Javascript Object Notation). JSON is a lightweight interchange format often used in web applications. For more information about JSON, see [http://www.json.org](http://www.json.org/)
.

[`json`](https://docs.python.org/3/library/json.html#module-json "json: Encode and decode the JSON format.")
 comes with support for decoding and encoding most built-in Python types. The following example encodes and decodes a dictionary:

Copy

\>>> import json
\>>> data \= {"spam": "foo", "parrot": 42}
\>>> in\_json \= json.dumps(data) \# Encode the data
\>>> in\_json
'{"parrot": 42, "spam": "foo"}'
\>>> json.loads(in\_json) \# Decode into a Python object
{"spam": "foo", "parrot": 42}

It’s also possible to write your own decoders and encoders to support more types. Pretty-printing of the JSON strings is also supported.

[`json`](https://docs.python.org/3/library/json.html#module-json "json: Encode and decode the JSON format.")
 (originally called simplejson) was written by Bob Ippolito.

### The [`plistlib`](https://docs.python.org/3/library/plistlib.html#module-plistlib "plistlib: Generate and parse Apple plist files.")
 module: A Property-List Parser[¶](https://docs.python.org/3/whatsnew/2.6.html#the-plistlib-module-a-property-list-parser "Link to this heading")

The `.plist` format is commonly used on Mac OS X to store basic data types (numbers, strings, lists, and dictionaries) by serializing them into an XML-based format. It resembles the XML-RPC serialization of data types.

Despite being primarily used on Mac OS X, the format has nothing Mac-specific about it and the Python implementation works on any platform that Python supports, so the [`plistlib`](https://docs.python.org/3/library/plistlib.html#module-plistlib "plistlib: Generate and parse Apple plist files.")
 module has been promoted to the standard library.

Using the module is simple:

Copy

import sys
import plistlib
import datetime as dt

\# Create data structure
data\_struct \= dict(lastAccessed\=dt.datetime.now(),
                   version\=1,
                   categories\=('Personal','Shared','Private'))

\# Create string containing XML.
plist\_str \= plistlib.writePlistToString(data\_struct)
new\_struct \= plistlib.readPlistFromString(plist\_str)
print data\_struct
print new\_struct

\# Write data structure to a file and read it back.
plistlib.writePlist(data\_struct, '/tmp/customizations.plist')
new\_struct \= plistlib.readPlist('/tmp/customizations.plist')

\# read/writePlist accepts file-like objects as well as paths.
plistlib.writePlist(data\_struct, sys.stdout)

### ctypes Enhancements[¶](https://docs.python.org/3/whatsnew/2.6.html#ctypes-enhancements "Link to this heading")

Thomas Heller continued to maintain and enhance the [`ctypes`](https://docs.python.org/3/library/ctypes.html#module-ctypes "ctypes: A foreign function library for Python.")
 module.

[`ctypes`](https://docs.python.org/3/library/ctypes.html#module-ctypes "ctypes: A foreign function library for Python.")
 now supports a [`c_bool`](https://docs.python.org/3/library/ctypes.html#ctypes.c_bool "ctypes.c_bool")
 datatype that represents the C99 `bool` type. (Contributed by David Remahl; [bpo-1649190](https://bugs.python.org/issue?@action=redirect&bpo=1649190)
.)

The [`ctypes`](https://docs.python.org/3/library/ctypes.html#module-ctypes "ctypes: A foreign function library for Python.")
 string, buffer and array types have improved support for extended slicing syntax, where various combinations of `(start, stop, step)` are supplied. (Implemented by Thomas Wouters.)

All [`ctypes`](https://docs.python.org/3/library/ctypes.html#module-ctypes "ctypes: A foreign function library for Python.")
 data types now support [`from_buffer()`](https://docs.python.org/3/library/ctypes.html#ctypes._CData.from_buffer "ctypes._CData.from_buffer")
 and [`from_buffer_copy()`](https://docs.python.org/3/library/ctypes.html#ctypes._CData.from_buffer_copy "ctypes._CData.from_buffer_copy")
 methods that create a ctypes instance based on a provided buffer object. `from_buffer_copy()` copies the contents of the object, while `from_buffer()` will share the same memory area.

A new calling convention tells [`ctypes`](https://docs.python.org/3/library/ctypes.html#module-ctypes "ctypes: A foreign function library for Python.")
 to clear the `errno` or Win32 LastError variables at the outset of each wrapped call. (Implemented by Thomas Heller; [bpo-1798](https://bugs.python.org/issue?@action=redirect&bpo=1798)
.)

You can now retrieve the Unix `errno` variable after a function call. When creating a wrapped function, you can supply `use_errno=True` as a keyword parameter to the `DLL` function and then call the module-level methods [`set_errno()`](https://docs.python.org/3/library/ctypes.html#ctypes.set_errno "ctypes.set_errno")
 and [`get_errno()`](https://docs.python.org/3/library/ctypes.html#ctypes.get_errno "ctypes.get_errno")
 to set and retrieve the error value.

The Win32 LastError variable is similarly supported by the `DLL`, [`OleDLL()`](https://docs.python.org/3/library/ctypes.html#ctypes.OleDLL "ctypes.OleDLL")
, and [`WinDLL()`](https://docs.python.org/3/library/ctypes.html#ctypes.WinDLL "ctypes.WinDLL")
 functions. You supply `use_last_error=True` as a keyword parameter and then call the module-level methods [`set_last_error()`](https://docs.python.org/3/library/ctypes.html#ctypes.set_last_error "ctypes.set_last_error")
 and [`get_last_error()`](https://docs.python.org/3/library/ctypes.html#ctypes.get_last_error "ctypes.get_last_error")
.

The [`byref()`](https://docs.python.org/3/library/ctypes.html#ctypes.byref "ctypes.byref")
 function, used to retrieve a pointer to a ctypes instance, now has an optional _offset_ parameter that is a byte count that will be added to the returned pointer.

### Improved SSL Support[¶](https://docs.python.org/3/whatsnew/2.6.html#improved-ssl-support "Link to this heading")

Bill Janssen made extensive improvements to Python 2.6’s support for the Secure Sockets Layer by adding a new module, [`ssl`](https://docs.python.org/3/library/ssl.html#module-ssl "ssl: TLS/SSL wrapper for socket objects")
, that’s built atop the [OpenSSL](https://www.openssl.org/)
 library. This new module provides more control over the protocol negotiated, the X.509 certificates used, and has better support for writing SSL servers (as opposed to clients) in Python. The existing SSL support in the [`socket`](https://docs.python.org/3/library/socket.html#module-socket "socket: Low-level networking interface.")
 module hasn’t been removed and continues to work, though it will be removed in Python 3.0.

To use the new module, you must first create a TCP connection in the usual way and then pass it to the `ssl.wrap_socket()` function. It’s possible to specify whether a certificate is required, and to obtain certificate info by calling the [`getpeercert()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.getpeercert "ssl.SSLSocket.getpeercert")
 method.

See also

The documentation for the [`ssl`](https://docs.python.org/3/library/ssl.html#module-ssl "ssl: TLS/SSL wrapper for socket objects")
 module.

Deprecations and Removals[¶](https://docs.python.org/3/whatsnew/2.6.html#deprecations-and-removals "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

*   String exceptions have been removed. Attempting to use them raises a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
    .
    
*   Changes to the [`Exception`](https://docs.python.org/3/builtins/exceptions.html#Exception "Exception")
     interface as dictated by [**PEP 352**](https://peps.python.org/pep-0352/)
     continue to be made. For 2.6, the `message` attribute is being deprecated in favor of the [`args`](https://docs.python.org/3/builtins/exceptions.html#BaseException.args "BaseException.args")
     attribute.
    
*   (3.0-warning mode) Python 3.0 will feature a reorganized standard library that will drop many outdated modules and rename others. Python 2.6 running in 3.0-warning mode will warn about these modules when they are imported.
    
    The list of deprecated modules is: `audiodev`, `bgenlocations`, `buildtools`, `bundlebuilder`, `Canvas`, `compiler`, `dircache`, `dl`, `fpformat`, `gensuitemodule`, `ihooks`, `imageop`, `imgfile`, `linuxaudiodev`, `mhlib`, `mimetools`, `multifile`, `new`, `pure`, `statvfs`, `sunaudiodev`, `test.testall`, and `toaiff`.
    
*   The `gopherlib` module has been removed.
    
*   The `MimeWriter` module and `mimify` module have been deprecated; use the [`email`](https://docs.python.org/3/library/email.html#module-email "email: Package supporting the parsing, manipulating, and generating email messages.")
     package instead.
    
*   The `md5` module has been deprecated; use the [`hashlib`](https://docs.python.org/3/library/hashlib.html#module-hashlib "hashlib: Secure hash and message digest algorithms.")
     module instead.
    
*   The `posixfile` module has been deprecated; [`fcntl.lockf()`](https://docs.python.org/3/library/fcntl.html#fcntl.lockf "fcntl.lockf")
     provides better locking.
    
*   The `popen2` module has been deprecated; use the [`subprocess`](https://docs.python.org/3/library/subprocess.html#module-subprocess "subprocess: Subprocess management.")
     module.
    
*   The `rgbimg` module has been removed.
    
*   The `sets` module has been deprecated; it’s better to use the built-in [`set`](https://docs.python.org/3/builtins/stdtypes.html#set "set")
     and [`frozenset`](https://docs.python.org/3/builtins/stdtypes.html#frozenset "frozenset")
     types.
    
*   The `sha` module has been deprecated; use the [`hashlib`](https://docs.python.org/3/library/hashlib.html#module-hashlib "hashlib: Secure hash and message digest algorithms.")
     module instead.
    

Build and C API Changes[¶](https://docs.python.org/3/whatsnew/2.6.html#build-and-c-api-changes "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

Changes to Python’s build process and to the C API include:

*   Python now must be compiled with C89 compilers (after 19 years!). This means that the Python source tree has dropped its own implementations of `memmove()` and `strerror()`, which are in the C89 standard library.
    
*   Python 2.6 can be built with Microsoft Visual Studio 2008 (version 9.0), and this is the new default compiler. See the `PCbuild` directory for the build files. (Implemented by Christian Heimes.)
    
*   On Mac OS X, Python 2.6 can be compiled as a 4-way universal build. The **configure** script can take a `--with-universal-archs=[32-bit|64-bit|all]` switch, controlling whether the binaries are built for 32-bit architectures (x86, PowerPC), 64-bit (x86-64 and PPC-64), or both. (Contributed by Ronald Oussoren.)
    
*   A new function added in Python 2.6.6, `PySys_SetArgvEx()`, sets the value of `sys.argv` and can optionally update `sys.path` to include the directory containing the script named by `sys.argv[0]` depending on the value of an _updatepath_ parameter.
    
    This function was added to close a security hole for applications that embed Python. The old function, `PySys_SetArgv()`, would always update `sys.path`, and sometimes it would add the current directory. This meant that, if you ran an application embedding Python in a directory controlled by someone else, attackers could put a Trojan-horse module in the directory (say, a file named `os.py`) that your application would then import and run.
    
    If you maintain a C/C++ application that embeds Python, check whether you’re calling `PySys_SetArgv()` and carefully consider whether the application should be using `PySys_SetArgvEx()` with _updatepath_ set to false. Note that using this function will break compatibility with Python versions 2.6.5 and earlier; if you have to continue working with earlier versions, you can leave the call to `PySys_SetArgv()` alone and call `PyRun_SimpleString("sys.path.pop(0)\n")` afterwards to discard the first `sys.path` component.
    
    Security issue reported as [**CVE 2008-5983**](https://www.cve.org/CVERecord?id=CVE-2008-5983)
    ; discussed in [gh-50003](https://github.com/python/cpython/issues/50003)
    , and fixed by Antoine Pitrou.
    
*   The BerkeleyDB module now has a C API object, available as `bsddb.db.api`. This object can be used by other C extensions that wish to use the `bsddb` module for their own purposes. (Contributed by Duncan Grisby.)
    
*   The new buffer interface, previously described in [the PEP 3118 section](https://docs.python.org/3/whatsnew/2.6.html#pep-3118-revised-buffer-protocol)
    , adds [`PyObject_GetBuffer()`](https://docs.python.org/3/c-api/buffer.html#c.PyObject_GetBuffer "PyObject_GetBuffer")
     and [`PyBuffer_Release()`](https://docs.python.org/3/c-api/buffer.html#c.PyBuffer_Release "PyBuffer_Release")
    , as well as a few other functions.
    
*   Python’s use of the C stdio library is now thread-safe, or at least as thread-safe as the underlying library is. A long-standing potential bug occurred if one thread closed a file object while another thread was reading from or writing to the object. In 2.6 file objects have a reference count, manipulated by the `PyFile_IncUseCount()` and `PyFile_DecUseCount()` functions. File objects can’t be closed unless the reference count is zero. `PyFile_IncUseCount()` should be called while the GIL is still held, before carrying out an I/O operation using the `FILE *` pointer, and `PyFile_DecUseCount()` should be called immediately after the GIL is re-acquired. (Contributed by Antoine Pitrou and Gregory P. Smith.)
    
*   Importing modules simultaneously in two different threads no longer deadlocks; it will now raise an [`ImportError`](https://docs.python.org/3/builtins/exceptions.html#ImportError "ImportError")
    . A new API function, `PyImport_ImportModuleNoBlock()`, will look for a module in `sys.modules` first, then try to import it after acquiring an import lock. If the import lock is held by another thread, an `ImportError` is raised. (Contributed by Christian Heimes.)
    
*   Several functions return information about the platform’s floating-point support. [`PyFloat_GetMax()`](https://docs.python.org/3/c-api/float.html#c.PyFloat_GetMax "PyFloat_GetMax")
     returns the maximum representable floating-point value, and [`PyFloat_GetMin()`](https://docs.python.org/3/c-api/float.html#c.PyFloat_GetMin "PyFloat_GetMin")
     returns the minimum positive value. [`PyFloat_GetInfo()`](https://docs.python.org/3/c-api/float.html#c.PyFloat_GetInfo "PyFloat_GetInfo")
     returns an object containing more information from the `float.h` file, such as `"mant_dig"` (number of digits in the mantissa), `"epsilon"` (smallest difference between 1.0 and the next largest value representable), and several others. (Contributed by Christian Heimes; [bpo-1534](https://bugs.python.org/issue?@action=redirect&bpo=1534)
    .)
    
*   C functions and methods that use [`PyComplex_AsCComplex()`](https://docs.python.org/3/c-api/complex.html#c.PyComplex_AsCComplex "PyComplex_AsCComplex")
     will now accept arguments that have a [`__complex__()`](https://docs.python.org/3/reference/datamodel.html#object.__complex__ "object.__complex__")
     method. In particular, the functions in the [`cmath`](https://docs.python.org/3/library/cmath.html#module-cmath "cmath: Mathematical functions for complex numbers.")
     module will now accept objects with this method. This is a backport of a Python 3.0 change. (Contributed by Mark Dickinson; [bpo-1675423](https://bugs.python.org/issue?@action=redirect&bpo=1675423)
    .)
    
*   Python’s C API now includes two functions for case-insensitive string comparisons, `PyOS_stricmp(char*, char*)` and `PyOS_strnicmp(char*, char*, Py_ssize_t)`. (Contributed by Christian Heimes; [bpo-1635](https://bugs.python.org/issue?@action=redirect&bpo=1635)
    .)
    
*   Many C extensions define their own little macro for adding integers and strings to the module’s dictionary in the `init*` function. Python 2.6 finally defines standard macros for adding values to a module, [`PyModule_AddStringMacro`](https://docs.python.org/3/c-api/module.html#c.PyModule_AddStringMacro "PyModule_AddStringMacro")
     and [`PyModule_AddIntMacro()`](https://docs.python.org/3/c-api/module.html#c.PyModule_AddIntMacro "PyModule_AddIntMacro")
    . (Contributed by Christian Heimes.)
    
*   Some macros were renamed in both 3.0 and 2.6 to make it clearer that they are macros, not functions. `Py_Size()` became [`Py_SIZE()`](https://docs.python.org/3/c-api/structures.html#c.Py_SIZE "Py_SIZE")
    , `Py_Type()` became [`Py_TYPE()`](https://docs.python.org/3/c-api/structures.html#c.Py_TYPE "Py_TYPE")
    , and `Py_Refcnt()` became [`Py_REFCNT()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_REFCNT "Py_REFCNT")
    . The mixed-case macros are still available in Python 2.6 for backward compatibility. ([bpo-1629](https://bugs.python.org/issue?@action=redirect&bpo=1629)
    )
    
*   Distutils now places C extensions it builds in a different directory when running on a debug version of Python. (Contributed by Collin Winter; [bpo-1530959](https://bugs.python.org/issue?@action=redirect&bpo=1530959)
    .)
    
*   Several basic data types, such as integers and strings, maintain internal free lists of objects that can be re-used. The data structures for these free lists now follow a naming convention: the variable is always named `free_list`, the counter is always named `numfree`, and a macro `Py<typename>_MAXFREELIST` is always defined.
    
*   A new Makefile target, “make patchcheck”, prepares the Python source tree for making a patch: it fixes trailing whitespace in all modified `.py` files, checks whether the documentation has been changed, and reports whether the `Misc/ACKS` and `Misc/NEWS` files have been updated. (Contributed by Brett Cannon.)
    
    Another new target, “make profile-opt”, compiles a Python binary using GCC’s profile-guided optimization. It compiles Python with profiling enabled, runs the test suite to obtain a set of profiling results, and then compiles using these results for optimization. (Contributed by Gregory P. Smith.)
    

### Port-Specific Changes: Windows[¶](https://docs.python.org/3/whatsnew/2.6.html#port-specific-changes-windows "Link to this heading")

*   The support for Windows 95, 98, ME and NT4 has been dropped. Python 2.6 requires at least Windows 2000 SP4.
    
*   The new default compiler on Windows is Visual Studio 2008 (version 9.0). The build directories for Visual Studio 2003 (version 7.1) and 2005 (version 8.0) were moved into the PC/ directory. The new `PCbuild` directory supports cross compilation for X64, debug builds and Profile Guided Optimization (PGO). PGO builds are roughly 10% faster than normal builds. (Contributed by Christian Heimes with help from Amaury Forgeot d’Arc and Martin von Löwis.)
    
*   The [`msvcrt`](https://docs.python.org/3/library/msvcrt.html#module-msvcrt "msvcrt: Miscellaneous useful routines from the MS VC++ runtime.")
     module now supports both the normal and wide char variants of the console I/O API. The [`getwch()`](https://docs.python.org/3/library/msvcrt.html#msvcrt.getwch "msvcrt.getwch")
     function reads a keypress and returns a Unicode value, as does the [`getwche()`](https://docs.python.org/3/library/msvcrt.html#msvcrt.getwche "msvcrt.getwche")
     function. The [`putwch()`](https://docs.python.org/3/library/msvcrt.html#msvcrt.putwch "msvcrt.putwch")
     function takes a Unicode character and writes it to the console. (Contributed by Christian Heimes.)
    
*   [`os.path.expandvars()`](https://docs.python.org/3/library/os.path.html#os.path.expandvars "os.path.expandvars")
     will now expand environment variables in the form “%var%”, and “~user” will be expanded into the user’s home directory path. (Contributed by Josiah Carlson; [bpo-957650](https://bugs.python.org/issue?@action=redirect&bpo=957650)
    .)
    
*   The [`socket`](https://docs.python.org/3/library/socket.html#module-socket "socket: Low-level networking interface.")
     module’s socket objects now have an [`ioctl()`](https://docs.python.org/3/library/socket.html#socket.socket.ioctl "socket.socket.ioctl")
     method that provides a limited interface to the `WSAIoctl()` system interface.
    
*   The [`_winreg`](https://docs.python.org/3/library/winreg.html#module-winreg "winreg: Routines and objects for manipulating the Windows registry.")
     module now has a function, [`ExpandEnvironmentStrings()`](https://docs.python.org/3/library/winreg.html#winreg.ExpandEnvironmentStrings "winreg.ExpandEnvironmentStrings")
    , that expands environment variable references such as `%NAME%` in an input string. The handle objects provided by this module now support the context protocol, so they can be used in [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
     statements. (Contributed by Christian Heimes.)
    
    [`_winreg`](https://docs.python.org/3/library/winreg.html#module-winreg "winreg: Routines and objects for manipulating the Windows registry.")
     also has better support for x64 systems, exposing the [`DisableReflectionKey()`](https://docs.python.org/3/library/winreg.html#winreg.DisableReflectionKey "winreg.DisableReflectionKey")
    , [`EnableReflectionKey()`](https://docs.python.org/3/library/winreg.html#winreg.EnableReflectionKey "winreg.EnableReflectionKey")
    , and [`QueryReflectionKey()`](https://docs.python.org/3/library/winreg.html#winreg.QueryReflectionKey "winreg.QueryReflectionKey")
     functions, which enable and disable registry reflection for 32-bit processes running on 64-bit systems. ([bpo-1753245](https://bugs.python.org/issue?@action=redirect&bpo=1753245)
    )
    
*   The `msilib` module’s `Record` object gained `GetInteger()` and `GetString()` methods that return field values as an integer or a string. (Contributed by Floris Bruynooghe; [bpo-2125](https://bugs.python.org/issue?@action=redirect&bpo=2125)
    .)
    

### Port-Specific Changes: Mac OS X[¶](https://docs.python.org/3/whatsnew/2.6.html#port-specific-changes-mac-os-x "Link to this heading")

*   When compiling a framework build of Python, you can now specify the framework name to be used by providing the `--with-framework-name=` option to the **configure** script.
    
*   The `macfs` module has been removed. This in turn required the `macostools.touched()` function to be removed because it depended on the `macfs` module. ([bpo-1490190](https://bugs.python.org/issue?@action=redirect&bpo=1490190)
    )
    
*   Many other Mac OS modules have been deprecated and will be removed in Python 3.0: `_builtinSuites`, `aepack`, `aetools`, `aetypes`, `applesingle`, `appletrawmain`, `appletrunner`, `argvemulator`, `Audio_mac`, `autoGIL`, `Carbon`, `cfmfile`, `CodeWarrior`, `ColorPicker`, `EasyDialogs`, `Explorer`, `Finder`, `FrameWork`, `findertools`, `ic`, `icglue`, `icopen`, `macerrors`, `MacOS`, `macfs`, `macostools`, `macresource`, `MiniAEFrame`, `Nav`, `Netscape`, `OSATerminology`, `pimp`, `PixMapWrapper`, `StdSuites`, `SystemEvents`, `Terminal`, and `terminalcommand`.
    

### Port-Specific Changes: IRIX[¶](https://docs.python.org/3/whatsnew/2.6.html#port-specific-changes-irix "Link to this heading")

A number of old IRIX-specific modules were deprecated and will be removed in Python 3.0: `al` and `AL`, `cd`, `cddb`, `cdplayer`, `CL` and `cl`, `DEVICE`, `ERRNO`, `FILE`, `FL` and `fl`, `flp`, `fm`, `GET`, `GLWS`, `GL` and `gl`, `IN`, `IOCTL`, `jpeg`, `panelparser`, `readcd`, `SV` and `sv`, `torgb`, `videoreader`, and `WAIT`.

Porting to Python 2.6[¶](https://docs.python.org/3/whatsnew/2.6.html#porting-to-python-2-6 "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

This section lists previously described changes and other bugfixes that may require changes to your code:

*   Classes that aren’t supposed to be hashable should set `__hash__ = None` in their definitions to indicate the fact.
    
*   String exceptions have been removed. Attempting to use them raises a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
    .
    
*   The `__init__()` method of [`collections.deque`](https://docs.python.org/3/library/collections.html#collections.deque "collections.deque")
     now clears any existing contents of the deque before adding elements from the iterable. This change makes the behavior match `list.__init__()`.
    
*   [`object.__init__()`](https://docs.python.org/3/reference/datamodel.html#object.__init__ "object.__init__")
     previously accepted arbitrary arguments and keyword arguments, ignoring them. In Python 2.6, this is no longer allowed and will result in a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
    . This will affect `__init__()` methods that end up calling the corresponding method on [`object`](https://docs.python.org/3/builtins/functions.html#object "object")
     (perhaps through using [`super()`](https://docs.python.org/3/builtins/functions.html#super "super")
    ). See [bpo-1683368](https://bugs.python.org/issue?@action=redirect&bpo=1683368)
     for discussion.
    
*   The [`Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "decimal.Decimal")
     constructor now accepts leading and trailing whitespace when passed a string. Previously it would raise an [`InvalidOperation`](https://docs.python.org/3/library/decimal.html#decimal.InvalidOperation "decimal.InvalidOperation")
     exception. On the other hand, the [`create_decimal()`](https://docs.python.org/3/library/decimal.html#decimal.Context.create_decimal "decimal.Context.create_decimal")
     method of [`Context`](https://docs.python.org/3/library/decimal.html#decimal.Context "decimal.Context")
     objects now explicitly disallows extra whitespace, raising a `ConversionSyntax` exception.
    
*   Due to an implementation accident, if you passed a file path to the built-in [`__import__()`](https://docs.python.org/3/builtins/functions.html#import__ "__import__")
     function, it would actually import the specified file. This was never intended to work, however, and the implementation now explicitly checks for this case and raises an [`ImportError`](https://docs.python.org/3/builtins/exceptions.html#ImportError "ImportError")
    .
    
*   C API: the [`PyImport_Import()`](https://docs.python.org/3/c-api/import.html#c.PyImport_Import "PyImport_Import")
     and [`PyImport_ImportModule()`](https://docs.python.org/3/c-api/import.html#c.PyImport_ImportModule "PyImport_ImportModule")
     functions now default to absolute imports, not relative imports. This will affect C extensions that import other modules.
    
*   C API: extension data types that shouldn’t be hashable should define their `tp_hash` slot to [`PyObject_HashNotImplemented()`](https://docs.python.org/3/c-api/object.html#c.PyObject_HashNotImplemented "PyObject_HashNotImplemented")
    .
    
*   The [`socket`](https://docs.python.org/3/library/socket.html#module-socket "socket: Low-level networking interface.")
     module exception [`socket.error`](https://docs.python.org/3/library/socket.html#socket.error "socket.error")
     now inherits from [`IOError`](https://docs.python.org/3/builtins/exceptions.html#IOError "IOError")
    . Previously it wasn’t a subclass of `StandardError` but now it is, through `IOError`. (Implemented by Gregory P. Smith; [bpo-1706815](https://bugs.python.org/issue?@action=redirect&bpo=1706815)
    .)
    
*   The [`xmlrpclib`](https://docs.python.org/3/library/xmlrpc.client.html#module-xmlrpc.client "xmlrpc.client: XML-RPC client access.")
     module no longer automatically converts [`datetime.date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date")
     and [`datetime.time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time")
     to the [`xmlrpclib.DateTime`](https://docs.python.org/3/library/xmlrpc.client.html#xmlrpc.client.DateTime "xmlrpc.client.DateTime")
     type; the conversion semantics were not necessarily correct for all applications. Code using `xmlrpclib` should convert `date` and `time` instances. ([bpo-1330538](https://bugs.python.org/issue?@action=redirect&bpo=1330538)
    )
    
*   (3.0-warning mode) The [`Exception`](https://docs.python.org/3/builtins/exceptions.html#Exception "Exception")
     class now warns when accessed using slicing or index access; having `Exception` behave like a tuple is being phased out.
    
*   (3.0-warning mode) inequality comparisons between two dictionaries or two objects that don’t implement comparison methods are reported as warnings. `dict1 == dict2` still works, but `dict1 < dict2` is being phased out.
    
    Comparisons between cells, which are an implementation detail of Python’s scoping rules, also cause warnings because such comparisons are forbidden entirely in 3.0.
    

For applications that embed Python:

*   The `PySys_SetArgvEx()` function was added in Python 2.6.6, letting applications close a security hole when the existing `PySys_SetArgv()` function was used. Check whether you’re calling `PySys_SetArgv()` and carefully consider whether the application should be using `PySys_SetArgvEx()` with _updatepath_ set to false.
    

Acknowledgements[¶](https://docs.python.org/3/whatsnew/2.6.html#acknowledgements "Link to this heading")

---------------------------------------------------------------------------------------------------------

The author would like to thank the following people for offering suggestions, corrections and assistance with various drafts of this article: Georg Brandl, Steve Brown, Nick Coghlan, Ralph Corderoy, Jim Jewett, Kent Johnson, Chris Lambacher, Martin Michlmayr, Antoine Pitrou, Brian Warner.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [What’s New in Python 2.6](https://docs.python.org/3/whatsnew/2.6.html#)
    *   [Python 3.0](https://docs.python.org/3/whatsnew/2.6.html#python-3-0)
        
    *   [Changes to the Development Process](https://docs.python.org/3/whatsnew/2.6.html#changes-to-the-development-process)
        *   [New Issue Tracker: Roundup](https://docs.python.org/3/whatsnew/2.6.html#new-issue-tracker-roundup)
            
        *   [New Documentation Format: reStructuredText Using Sphinx](https://docs.python.org/3/whatsnew/2.6.html#new-documentation-format-restructuredtext-using-sphinx)
            
    *   [PEP 343: The ‘with’ statement](https://docs.python.org/3/whatsnew/2.6.html#pep-343-the-with-statement)
        *   [Writing Context Managers](https://docs.python.org/3/whatsnew/2.6.html#writing-context-managers)
            
        *   [The contextlib module](https://docs.python.org/3/whatsnew/2.6.html#the-contextlib-module)
            
    *   [PEP 366: Explicit Relative Imports From a Main Module](https://docs.python.org/3/whatsnew/2.6.html#pep-366-explicit-relative-imports-from-a-main-module)
        
    *   [PEP 370: Per-user `site-packages` Directory](https://docs.python.org/3/whatsnew/2.6.html#pep-370-per-user-site-packages-directory)
        
    *   [PEP 371: The `multiprocessing` Package](https://docs.python.org/3/whatsnew/2.6.html#pep-371-the-multiprocessing-package)
        
    *   [PEP 3101: Advanced String Formatting](https://docs.python.org/3/whatsnew/2.6.html#pep-3101-advanced-string-formatting)
        
    *   [PEP 3105: `print` As a Function](https://docs.python.org/3/whatsnew/2.6.html#pep-3105-print-as-a-function)
        
    *   [PEP 3110: Exception-Handling Changes](https://docs.python.org/3/whatsnew/2.6.html#pep-3110-exception-handling-changes)
        
    *   [PEP 3112: Byte Literals](https://docs.python.org/3/whatsnew/2.6.html#pep-3112-byte-literals)
        
    *   [PEP 3116: New I/O Library](https://docs.python.org/3/whatsnew/2.6.html#pep-3116-new-i-o-library)
        
    *   [PEP 3118: Revised Buffer Protocol](https://docs.python.org/3/whatsnew/2.6.html#pep-3118-revised-buffer-protocol)
        
    *   [PEP 3119: Abstract Base Classes](https://docs.python.org/3/whatsnew/2.6.html#pep-3119-abstract-base-classes)
        
    *   [PEP 3127: Integer Literal Support and Syntax](https://docs.python.org/3/whatsnew/2.6.html#pep-3127-integer-literal-support-and-syntax)
        
    *   [PEP 3129: Class Decorators](https://docs.python.org/3/whatsnew/2.6.html#pep-3129-class-decorators)
        
    *   [PEP 3141: A Type Hierarchy for Numbers](https://docs.python.org/3/whatsnew/2.6.html#pep-3141-a-type-hierarchy-for-numbers)
        *   [The `fractions` Module](https://docs.python.org/3/whatsnew/2.6.html#the-fractions-module)
            
    *   [Other Language Changes](https://docs.python.org/3/whatsnew/2.6.html#other-language-changes)
        *   [Optimizations](https://docs.python.org/3/whatsnew/2.6.html#optimizations)
            
        *   [Interpreter Changes](https://docs.python.org/3/whatsnew/2.6.html#interpreter-changes)
            
    *   [New and Improved Modules](https://docs.python.org/3/whatsnew/2.6.html#new-and-improved-modules)
        *   [The `ast` module](https://docs.python.org/3/whatsnew/2.6.html#the-ast-module)
            
        *   [The `future_builtins` module](https://docs.python.org/3/whatsnew/2.6.html#the-future-builtins-module)
            
        *   [The `json` module: JavaScript Object Notation](https://docs.python.org/3/whatsnew/2.6.html#the-json-module-javascript-object-notation)
            
        *   [The `plistlib` module: A Property-List Parser](https://docs.python.org/3/whatsnew/2.6.html#the-plistlib-module-a-property-list-parser)
            
        *   [ctypes Enhancements](https://docs.python.org/3/whatsnew/2.6.html#ctypes-enhancements)
            
        *   [Improved SSL Support](https://docs.python.org/3/whatsnew/2.6.html#improved-ssl-support)
            
    *   [Deprecations and Removals](https://docs.python.org/3/whatsnew/2.6.html#deprecations-and-removals)
        
    *   [Build and C API Changes](https://docs.python.org/3/whatsnew/2.6.html#build-and-c-api-changes)
        *   [Port-Specific Changes: Windows](https://docs.python.org/3/whatsnew/2.6.html#port-specific-changes-windows)
            
        *   [Port-Specific Changes: Mac OS X](https://docs.python.org/3/whatsnew/2.6.html#port-specific-changes-mac-os-x)
            
        *   [Port-Specific Changes: IRIX](https://docs.python.org/3/whatsnew/2.6.html#port-specific-changes-irix)
            
    *   [Porting to Python 2.6](https://docs.python.org/3/whatsnew/2.6.html#porting-to-python-2-6)
        
    *   [Acknowledgements](https://docs.python.org/3/whatsnew/2.6.html#acknowledgements)
        

#### Previous topic

[What’s New in Python 2.7](https://docs.python.org/3/whatsnew/2.7.html "previous chapter")

#### Next topic

[What’s New in Python 2.5](https://docs.python.org/3/whatsnew/2.5.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=What%E2%80%99s+New+in+Python+2.6&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fwhatsnew%2F2.6.html&pagesource=whatsnew%2F2.6.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/whatsnew/2.6.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/whatsnew/2.5.html "What’s New in Python 2.5")
     |
*   [previous](https://docs.python.org/3/whatsnew/2.7.html "What’s New in Python 2.7")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [What’s New in Python](https://docs.python.org/3/whatsnew/index.html)
     »
*   [What’s New in Python 2.6](https://docs.python.org/3/whatsnew/2.6.html)
    
*    
    
    |
*   Theme Auto Light Dark |