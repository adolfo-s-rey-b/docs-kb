### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/sys_path_init.html "The initialization of the sys.path module search path")
     |
*   [previous](https://docs.python.org/3/library/importlib.resources.abc.html "importlib.resources.abc – Abstract base classes for resources")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [The Python standard library](https://docs.python.org/3/library/index.html)
     »
*   [Importing Modules](https://docs.python.org/3/library/modules.html)
     »
*   [`importlib.metadata` – Accessing package metadata](https://docs.python.org/3/library/importlib.metadata.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`importlib.metadata` – Accessing package metadata[¶](https://docs.python.org/3/library/importlib.metadata.html#module-importlib.metadata "Link to this heading")

=================================================================================================================================================================

Added in version 3.8.

Changed in version 3.10: `importlib.metadata` is no longer provisional.

**Source code:** [Lib/importlib/metadata/\_\_init\_\_.py](https://github.com/python/cpython/tree/3.15/Lib/importlib/metadata/__init__.py)

`importlib.metadata` is a library that provides access to the metadata of an installed [Distribution Package](https://packaging.python.org/en/latest/glossary/#term-Distribution-Package)
, such as its entry points or its top-level names ([Import Package](https://packaging.python.org/en/latest/glossary/#term-Import-Package)
s, modules, if any). Built in part on Python’s import system, this library provides the entry point and metadata APIs that were previously exposed by the now-removed `pkg_resources` package. Along with [`importlib.resources`](https://docs.python.org/3/library/importlib.resources.html#module-importlib.resources "importlib.resources: Package resource reading, opening, and access")
, it supersedes `pkg_resources`.

`importlib.metadata` operates on third-party _distribution packages_ installed into Python’s `site-packages` directory via tools such as [pip](https://pypi.org/project/pip/)
. Specifically, it works with distributions with discoverable `dist-info` or `egg-info` directories, and metadata defined by the [Core metadata specifications](https://packaging.python.org/en/latest/specifications/core-metadata/#core-metadata)
.

Important

These are _not_ necessarily equivalent to or correspond 1:1 with the top-level _import package_ names that can be imported inside Python code. One _distribution package_ can contain multiple _import packages_ (and single modules), and one top-level _import package_ may map to multiple _distribution packages_ if it is a namespace package. You can use [packages\_distributions()](https://docs.python.org/3/library/importlib.metadata.html#package-distributions)
 to get a mapping between them.

By default, distribution metadata can live on the file system or in zip archives on [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
. Through an extension mechanism, the metadata can live almost anywhere.

See also

[https://importlib-metadata.readthedocs.io/](https://importlib-metadata.readthedocs.io/)

The documentation for `importlib_metadata`, which supplies a backport of `importlib.metadata`. This includes an [API reference](https://importlib-metadata.readthedocs.io/en/latest/api.html)
 for this module’s classes and functions, as well as a [migration guide](https://importlib-metadata.readthedocs.io/en/latest/migration.html)
 for existing users of `pkg_resources`.

Overview[¶](https://docs.python.org/3/library/importlib.metadata.html#overview "Link to this heading")

-------------------------------------------------------------------------------------------------------

Let’s say you wanted to get the version string for a [Distribution Package](https://packaging.python.org/en/latest/glossary/#term-Distribution-Package)
 you’ve installed using `pip`. We start by creating a virtual environment and installing something into it:

Copy

$ python \-m venv example
$ source example/bin/activate
(example) $ python \-m pip install wheel

You can get the version string for `wheel` by running the following:

Copy

(example) $ python
\>>> from importlib.metadata import version
\>>> version('wheel')
'0.32.3'

You can also get a collection of entry points selectable by properties of the EntryPoint (typically ‘group’ or ‘name’), such as `console_scripts`, `distutils.commands` and others. Each group contains a collection of [EntryPoint](https://docs.python.org/3/library/importlib.metadata.html#entry-points)
 objects.

You can get the [metadata for a distribution](https://docs.python.org/3/library/importlib.metadata.html#metadata)
:

Copy

\>>> from importlib.metadata import metadata
\>>> list(metadata('wheel'))
\['Metadata-Version', 'Name', 'Version', 'Summary', 'Home-page', 'Author', 'Author-email', 'Maintainer', 'Maintainer-email', 'License', 'Project-URL', 'Project-URL', 'Project-URL', 'Keywords', 'Platform', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Requires-Python', 'Provides-Extra', 'Requires-Dist', 'Requires-Dist'\]

You can also get a [distribution’s version number](https://docs.python.org/3/library/importlib.metadata.html#version)
, list its [constituent files](https://docs.python.org/3/library/importlib.metadata.html#files)
, and get a list of the distribution’s [Distribution requirements](https://docs.python.org/3/library/importlib.metadata.html#requirements)
.

exception importlib.metadata.PackageNotFoundError[¶](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.PackageNotFoundError "Link to this definition")

Subclass of [`ModuleNotFoundError`](https://docs.python.org/3/builtins/exceptions.html#ModuleNotFoundError "ModuleNotFoundError")
 raised by several functions in this module when queried for a distribution package which is not installed in the current Python environment.

exception importlib.metadata.MetadataNotFound[¶](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.MetadataNotFound "Link to this definition")

Subclass of [`FileNotFoundError`](https://docs.python.org/3/builtins/exceptions.html#FileNotFoundError "FileNotFoundError")
 raised when attempting to load metadata from a distribution folder that is empty or otherwise does not contain a metadata file.

Functional API[¶](https://docs.python.org/3/library/importlib.metadata.html#functional-api "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

This package provides the following functionality via its public API.

### Entry points[¶](https://docs.python.org/3/library/importlib.metadata.html#entry-points "Link to this heading")

importlib.metadata.entry\_points(_\*\*select\_params_)[¶](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.entry_points "Link to this definition")

Returns a [`EntryPoints`](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.EntryPoints "importlib.metadata.EntryPoints")
 instance describing entry points for the current environment. Any given keyword parameters are passed to the `select()` method for comparison to the attributes of the individual entry point definitions.

Note: to query for entry points based on `EntryPoint.dist` attribute, use [`Distribution.entry_points()`](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.Distribution.entry_points "importlib.metadata.Distribution.entry_points")
 instead (as different [`Distribution`](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.Distribution "importlib.metadata.Distribution")
 instances do not currently compare equal, even if they have the same attributes)

class importlib.metadata.EntryPoints[¶](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.EntryPoints "Link to this definition")

Details of a collection of installed entry points.

Also provides a `.groups` attribute that reports all identified entry point groups, and a `.names` attribute that reports all identified entry point names.

class importlib.metadata.EntryPoint[¶](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.EntryPoint "Link to this definition")

Details of an installed entry point.

Each `EntryPoint` instance has `.name`, `.group`, and `.value` attributes and a `.load()` method to resolve the value. There are also `.module`, `.attr`, and `.extras` attributes for getting the components of the `.value` attribute, and `.dist` for obtaining information regarding the distribution package that provides the entry point.

Query all entry points:

Copy

\>>> eps \= entry\_points()

The `entry_points()` function returns a `EntryPoints` object, a collection of all `EntryPoint` objects with `names` and `groups` attributes for convenience:

Copy

\>>> sorted(eps.groups)
\['console\_scripts', 'distutils.commands', 'distutils.setup\_keywords', 'egg\_info.writers', 'setuptools.installation'\]

`EntryPoints` has a `select()` method to select entry points matching specific properties. Select entry points in the `console_scripts` group:

Copy

\>>> scripts \= eps.select(group\='console\_scripts')

Equivalently, since `entry_points()` passes keyword arguments through to select:

Copy

\>>> scripts \= entry\_points(group\='console\_scripts')

Pick out a specific script named “wheel” (found in the wheel project):

Copy

\>>> 'wheel' in scripts.names
True
\>>> wheel \= scripts\['wheel'\]

Equivalently, query for that entry point during selection:

Copy

\>>> (wheel,) \= entry\_points(group\='console\_scripts', name\='wheel')
\>>> (wheel,) \= entry\_points().select(group\='console\_scripts', name\='wheel')

Inspect the resolved entry point:

Copy

\>>> wheel
EntryPoint(name='wheel', value='wheel.cli:main', group='console\_scripts')
\>>> wheel.module
'wheel.cli'
\>>> wheel.attr
'main'
\>>> wheel.extras
\[\]
\>>> main \= wheel.load()
\>>> main
<function main at 0x103528488>

The `group` and `name` are arbitrary values defined by the package author and usually a client will wish to resolve all entry points for a particular group. Read [the setuptools docs](https://setuptools.pypa.io/en/latest/userguide/entry_point.html)
 for more information on entry points, their definition, and usage.

Changed in version 3.12: The “selectable” entry points were introduced in `importlib_metadata` 3.6 and Python 3.10. Prior to those changes, `entry_points` accepted no parameters and always returned a dictionary of entry points, keyed by group. With `importlib_metadata` 5.0 and Python 3.12, `entry_points` always returns an `EntryPoints` object. See [backports.entry\_points\_selectable](https://pypi.org/project/backports.entry_points_selectable/)
 for compatibility options.

Changed in version 3.13: `EntryPoint` objects no longer present a tuple-like interface ([`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__")
).

### Distribution metadata[¶](https://docs.python.org/3/library/importlib.metadata.html#distribution-metadata "Link to this heading")

importlib.metadata.metadata(_distribution\_name_)[¶](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.metadata "Link to this definition")

Return the distribution metadata corresponding to the named distribution package as a [`PackageMetadata`](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.PackageMetadata "importlib.metadata.PackageMetadata")
 instance.

Raises [`PackageNotFoundError`](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.PackageNotFoundError "importlib.metadata.PackageNotFoundError")
 if the named distribution package is not installed in the current Python environment.

Raises [`MetadataNotFound`](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.MetadataNotFound "importlib.metadata.MetadataNotFound")
 if a distribution package is present but no METADATA file is present.

class importlib.metadata.PackageMetadata[¶](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.PackageMetadata "Link to this definition")

A concrete implementation of the [PackageMetadata protocol](https://importlib-metadata.readthedocs.io/en/latest/api.html#importlib_metadata.PackageMetadata)
.

In addition to providing the defined protocol methods and attributes, subscripting the instance is equivalent to calling the `get()` method.

Every [Distribution Package](https://packaging.python.org/en/latest/glossary/#term-Distribution-Package)
 includes some metadata, which you can extract using the `metadata()` function:

Copy

\>>> wheel\_metadata \= metadata('wheel')

The keys of the returned data structure name the metadata keywords, and the values are returned unparsed from the distribution metadata:

Copy

\>>> wheel\_metadata\['Requires-Python'\]
'>=2.7, !=3.0.\*, !=3.1.\*, !=3.2.\*, !=3.3.\*'

[`PackageMetadata`](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.PackageMetadata "importlib.metadata.PackageMetadata")
 also presents a `json` attribute that returns all the metadata in a JSON-compatible form per [**PEP 566**](https://peps.python.org/pep-0566/)
:

Copy

\>>> wheel\_metadata.json\['requires\_python'\]
'>=2.7, !=3.0.\*, !=3.1.\*, !=3.2.\*, !=3.3.\*'

The full set of available metadata is not described here. See the PyPA [Core metadata specification](https://packaging.python.org/en/latest/specifications/core-metadata/#core-metadata)
 for additional details.

Changed in version 3.15: Previously and incidentally, if a METADATA file was missing from a distribution, an empty `PackageMetadata` would be returned, indistinguishable from an empty METADATA file. Now, a missing METADATA file triggers a `MetadataNotFound` exception.

Changed in version 3.10: The `Description` is now included in the metadata when presented through the payload. Line continuation characters have been removed.

The `json` attribute was added.

### Distribution versions[¶](https://docs.python.org/3/library/importlib.metadata.html#distribution-versions "Link to this heading")

importlib.metadata.version(_distribution\_name_)[¶](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.version "Link to this definition")

Return the installed distribution package [version](https://packaging.python.org/en/latest/specifications/core-metadata/#version)
 for the named distribution package.

Raises [`PackageNotFoundError`](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.PackageNotFoundError "importlib.metadata.PackageNotFoundError")
 if the named distribution package is not installed in the current Python environment.

The `version()` function is the quickest way to get a [Distribution Package](https://packaging.python.org/en/latest/glossary/#term-Distribution-Package)
’s version number, as a string:

Copy

\>>> version('wheel')
'0.32.3'

### Distribution files[¶](https://docs.python.org/3/library/importlib.metadata.html#distribution-files "Link to this heading")

importlib.metadata.files(_distribution\_name_)[¶](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.files "Link to this definition")

Return the full set of files contained within the named distribution package as [`PackagePath`](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.PackagePath "importlib.metadata.PackagePath")
 instances.

Raises [`PackageNotFoundError`](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.PackageNotFoundError "importlib.metadata.PackageNotFoundError")
 if the named distribution package is not installed in the current Python environment.

Returns [`None`](https://docs.python.org/3/builtins/constants.html#None "None")
 if the distribution is found but the installation database records reporting the files associated with the distribution package are missing.

class importlib.metadata.PackagePath[¶](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.PackagePath "Link to this definition")

A [`pathlib.PurePath`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath "pathlib.PurePath")
 derived object with additional `dist`, `size`, and `hash` properties corresponding to the distribution package’s installation metadata for that file, also:

locate()[¶](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.PackagePath.locate "Link to this definition")

If possible, return the concrete [`SimplePath`](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.SimplePath "importlib.metadata.SimplePath")
 allowing to access data, or raise a [`NotImplementedError`](https://docs.python.org/3/builtins/exceptions.html#NotImplementedError "NotImplementedError")
 otherwise.

class importlib.metadata.SimplePath[¶](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.SimplePath "Link to this definition")

A protocol representing a minimal subset of [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path")
 that allows to check if it `exists()`, to traverse using `joinpath()` and `parent`, and to retrieve data using `read_text()` and `read_bytes()`.

The `files()` function takes a [Distribution Package](https://packaging.python.org/en/latest/glossary/#term-Distribution-Package)
 name and returns all of the files installed by this distribution. For example:

Copy

\>>> util \= \[p for p in files('wheel') if 'util.py' in str(p)\]\[0\]
\>>> util
PackagePath('wheel/util.py')
\>>> util.size
859
\>>> util.dist
<importlib.metadata.\_hooks.PathDistribution object at 0x101e0cef0>
\>>> util.hash
<FileHash mode: sha256 value: bYkw5oMccfazVCoYQwKkkemoVyMAFoR34mmKBx8R1NI>

Once you have the file, you can also read its contents:

Copy

\>>> print(util.read\_text())
import base64
import sys
...
def as\_bytes(s):
    if isinstance(s, text\_type):
        return s.encode('utf-8')
    return s

You can also use the `locate()` method to get the absolute path to the file:

Copy

\>>> util.locate()
PosixPath('/home/gustav/example/lib/site-packages/wheel/util.py')

In the case where the metadata file listing files (`RECORD` or `SOURCES.txt`) is missing, `files()` will return [`None`](https://docs.python.org/3/builtins/constants.html#None "None")
. The caller may wish to wrap calls to `files()` in [always\_iterable](https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.always_iterable)
 or otherwise guard against this condition if the target distribution is not known to have the metadata present.

### Distribution requirements[¶](https://docs.python.org/3/library/importlib.metadata.html#distribution-requirements "Link to this heading")

importlib.metadata.requires(_distribution\_name_)[¶](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.requires "Link to this definition")

Return the declared dependency specifiers for the named distribution package.

Raises [`PackageNotFoundError`](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.PackageNotFoundError "importlib.metadata.PackageNotFoundError")
 if the named distribution package is not installed in the current Python environment.

To get the full set of requirements for a [Distribution Package](https://packaging.python.org/en/latest/glossary/#term-Distribution-Package)
, use the `requires()` function:

Copy

\>>> requires('wheel')
\["pytest (>=3.0.0) ; extra == 'test'", "pytest-cov ; extra == 'test'"\]

### Mapping import to distribution packages[¶](https://docs.python.org/3/library/importlib.metadata.html#mapping-import-to-distribution-packages "Link to this heading")

importlib.metadata.packages\_distributions()[¶](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.packages_distributions "Link to this definition")

Return a mapping from the top level module and import package names found via [`sys.meta_path`](https://docs.python.org/3/library/sys.html#sys.meta_path "sys.meta_path")
 to the names of the distribution packages (if any) that provide the corresponding files.

To allow for namespace packages (which may have members provided by multiple distribution packages), each top level import name maps to a list of distribution names rather than mapping directly to a single name.

A convenience method to resolve the [Distribution Package](https://packaging.python.org/en/latest/glossary/#term-Distribution-Package)
 name (or names, in the case of a namespace package) that provide each importable top-level Python module or [Import Package](https://packaging.python.org/en/latest/glossary/#term-Import-Package)
:

Copy

\>>> packages\_distributions()
{'importlib\_metadata': \['importlib-metadata'\], 'yaml': \['PyYAML'\], 'jaraco': \['jaraco.classes', 'jaraco.functools'\], ...}

Some editable installs, [do not supply top-level names](https://github.com/pypa/packaging-problems/issues/609)
, and thus this function is not reliable with such installs.

Added in version 3.10.

Distributions[¶](https://docs.python.org/3/library/importlib.metadata.html#distributions "Link to this heading")

-----------------------------------------------------------------------------------------------------------------

While the module level API described above is the most common and convenient usage, all that information is accessible from the [`Distribution`](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.Distribution "importlib.metadata.Distribution")
 class. `Distribution` is an abstract object that represents the metadata for a Python [Distribution Package](https://packaging.python.org/en/latest/glossary/#term-Distribution-Package)
. Get the concrete `Distribution` subclass instance for an installed distribution package by calling the [`distribution()`](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.distribution "importlib.metadata.distribution")
 function:

Copy

\>>> from importlib.metadata import distribution
\>>> dist \= distribution('wheel')
\>>> type(dist)
<class 'importlib.metadata.PathDistribution'>

importlib.metadata.distribution(_distribution\_name_)[¶](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.distribution "Link to this definition")

Return a [`Distribution`](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.Distribution "importlib.metadata.Distribution")
 instance describing the named distribution package.

Raises [`PackageNotFoundError`](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.PackageNotFoundError "importlib.metadata.PackageNotFoundError")
 if the named distribution package is not installed in the current Python environment.

Thus, an alternative way to get e.g. the version number is through the [`Distribution.version`](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.Distribution.version "importlib.metadata.Distribution.version")
 attribute:

Copy

\>>> dist.version
'0.32.3'

The same applies for [`entry_points()`](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.entry_points "importlib.metadata.entry_points")
 and [`files()`](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.files "importlib.metadata.files")
.

class importlib.metadata.Distribution[¶](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.Distribution "Link to this definition")

Details of an installed distribution package.

Note: different `Distribution` instances do not currently compare equal, even if they relate to the same installed distribution and accordingly have the same attributes.

static at(_path_)[¶](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.Distribution.at "Link to this definition")

classmethod from\_name(_name_)[¶](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.Distribution.from_name "Link to this definition")

Return a `Distribution` instance at the given path or with the given name.

classmethod discover(_\*_, _context\=None_, _\*\*kwargs_)[¶](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.Distribution.discover "Link to this definition")

Returns an iterable of `Distribution` instances for all packages (see [distribution-discovery](https://docs.python.org/3/library/importlib.metadata.html#distribution-discovery)
).

The optional argument _context_ is a [`DistributionFinder.Context`](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.DistributionFinder.Context "importlib.metadata.DistributionFinder.Context")
 instance, used to modify the search for distributions. Alternatively, _kwargs_ may contain keyword arguments for constructing a new `DistributionFinder.Context`.

metadata: [PackageMetadata](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.PackageMetadata "importlib.metadata.PackageMetadata")
[¶](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.Distribution.metadata "Link to this definition")

Raises [`MetadataNotFound`](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.MetadataNotFound "importlib.metadata.MetadataNotFound")
 if the METADATA file is not present in the distribution.

There are all kinds of additional metadata available on `Distribution` instances as a [`PackageMetadata`](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.PackageMetadata "importlib.metadata.PackageMetadata")
 instance:

Copy

\>>> dist.metadata\['Requires-Python'\]
'>=2.7, !=3.0.\*, !=3.1.\*, !=3.2.\*, !=3.3.\*'
\>>> dist.metadata\['License'\]
'MIT'

The full set of available metadata is not described here. See the PyPA [Core metadata specification](https://packaging.python.org/en/latest/specifications/core-metadata/#core-metadata)
 for additional details.

name: [str](https://docs.python.org/3/builtins/stdtypes.html#str "str")
[¶](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.Distribution.name "Link to this definition")

requires: [list](https://docs.python.org/3/builtins/stdtypes.html#list "list")
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "str")\
\][¶](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.Distribution.requires "Link to this definition")

version: [str](https://docs.python.org/3/builtins/stdtypes.html#str "str")
[¶](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.Distribution.version "Link to this definition")

A few metadata fields are also available as shortcut properties.

Added in version 3.10: The `name` shortcut was added.

origin[¶](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.Distribution.origin "Link to this definition")

For editable packages, an `origin` property may present [**PEP 610**](https://peps.python.org/pep-0610/)
 metadata (for non-editable packages, `origin` is [`None`](https://docs.python.org/3/builtins/constants.html#None "None")
):

Copy

\>>> dist.origin.url
'file:///path/to/wheel-0.32.3.editable-py3-none-any.whl'

The `origin` object follows the [Direct URL Data Structure](https://packaging.python.org/en/latest/specifications/direct-url-data-structure/)
.

Added in version 3.13.

entry\_points: [EntryPoints](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.EntryPoints "importlib.metadata.EntryPoints")
[¶](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.Distribution.entry_points "Link to this definition")

The entry points provided by this distribution package.

files: [list](https://docs.python.org/3/builtins/stdtypes.html#list "list")
\[[PackagePath](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.PackagePath "importlib.metadata.PackagePath")\
\] | [None](https://docs.python.org/3/builtins/constants.html#None "None")
[¶](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.Distribution.files "Link to this definition")

All files contained in this distribution package. Like [`files()`](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.files "importlib.metadata.files")
, this returns [`None`](https://docs.python.org/3/builtins/constants.html#None "None")
 if there are no records.

The following two abstract methods need to be implemented when [implementing-custom-providers](https://docs.python.org/3/library/importlib.metadata.html#implementing-custom-providers)
:

locate\_file(_path_)[¶](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.Distribution.locate_file "Link to this definition")

Like `PackagePath.locate()`, return a [`SimplePath`](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.SimplePath "importlib.metadata.SimplePath")
 for the given path. Takes a [`os.PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "os.PathLike")
 or a [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
.

read\_text(_filename_)[¶](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.Distribution.read_text "Link to this definition")

A shortcut for `distribution.locate_file(filename).read_text()`.

Distribution Discovery[¶](https://docs.python.org/3/library/importlib.metadata.html#distribution-discovery "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------

By default, this package provides built-in support for discovery of metadata for file system and zip file [Distribution Package](https://packaging.python.org/en/latest/glossary/#term-Distribution-Package)
s. This metadata finder search defaults to `sys.path`, but varies slightly in how it interprets those values from how other import machinery does. In particular:

*   `importlib.metadata` does not honor [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
     objects on `sys.path`.
    
*   `importlib.metadata` will incidentally honor [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path")
     objects on `sys.path` even though such values will be ignored for imports.
    

class importlib.metadata.DistributionFinder[¶](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.DistributionFinder "Link to this definition")

A [`MetaPathFinder`](https://docs.python.org/3/library/importlib.html#importlib.abc.MetaPathFinder "importlib.abc.MetaPathFinder")
 subclass capable of discovering installed distributions.

Custom providers should implement this interface in order to supply metadata.

> class Context(_\*\*kwargs_)[¶](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.DistributionFinder.Context "Link to this definition")
> 
> A `Context` gives a custom provider a means to solicit additional details from the callers of distribution discovery functions like [`distributions()`](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.distributions "importlib.metadata.distributions")
>  or [`Distribution.discover()`](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.Distribution.discover "importlib.metadata.Distribution.discover")
>  beyond `.name` and `.path` when searching for distributions.
> 
> For example, a provider could expose suites of packages in either a “public” or “private” `realm`. A caller of distribution discovery functions may wish to query only for distributions in a particular realm and could call `distributions(realm="private")` to signal to the custom provider to only include distributions from that realm.
> 
> Each `DistributionFinder` must expect any parameters and should attempt to honor the canonical parameters defined below when appropriate.
> 
> See the section on [Implementing Custom Providers](https://docs.python.org/3/library/importlib.metadata.html#implementing-custom-providers)
>  for more details.
> 
> name[¶](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.DistributionFinder.Context.name "Link to this definition")
> 
> Specific name for which a distribution finder should match.
> 
> A `.name` of `None` matches all distributions.
> 
> path[¶](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.DistributionFinder.Context.path "Link to this definition")
> 
> A property providing the sequence of directory paths that a distribution finder should search.
> 
> Typically refers to Python installed package paths such as “site-packages” directories and defaults to [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
> .

importlib.metadata.distributions(_\*\*kwargs_)[¶](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.distributions "Link to this definition")

Returns an iterable of [`Distribution`](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.Distribution "importlib.metadata.Distribution")
 instances for all packages.

The _kwargs_ argument may contain either a keyword argument `context`, a [`DistributionFinder.Context`](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.DistributionFinder.Context "importlib.metadata.DistributionFinder.Context")
 instance, or pass keyword arguments for constructing a new `DistributionFinder.Context`. The `DistributionFinder.Context` is used to modify the search for distributions.

Implementing Custom Providers[¶](https://docs.python.org/3/library/importlib.metadata.html#implementing-custom-providers "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------

`importlib.metadata` address two API surfaces, one for _consumers_ and another for _providers_. Most users are consumers, consuming metadata provided by the packages. There are other use-cases, however, where users wish to expose metadata through some other mechanism, such as alongside a custom importer. Such a use case calls for a _custom provider_.

Because [Distribution Package](https://packaging.python.org/en/latest/glossary/#term-Distribution-Package)
 metadata is not available through [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
 searches, or package loaders directly, the metadata for a distribution is found through import system [finders](https://docs.python.org/3/reference/import.html#finders-and-loaders)
. To find a distribution package’s metadata, `importlib.metadata` queries the list of [meta path finders](https://docs.python.org/3/glossary.html#term-meta-path-finder)
 on [`sys.meta_path`](https://docs.python.org/3/library/sys.html#sys.meta_path "sys.meta_path")
.

The implementation has hooks integrated into the `PathFinder`, serving metadata for distribution packages found on the file system.

The abstract class [`importlib.abc.MetaPathFinder`](https://docs.python.org/3/library/importlib.html#importlib.abc.MetaPathFinder "importlib.abc.MetaPathFinder")
 defines the interface expected of finders by Python’s import system. `importlib.metadata` extends this protocol by looking for an optional `find_distributions` callable on the finders from [`sys.meta_path`](https://docs.python.org/3/library/sys.html#sys.meta_path "sys.meta_path")
 and presents this extended interface as the [`DistributionFinder`](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.DistributionFinder "importlib.metadata.DistributionFinder")
 abstract base class, which defines this abstract method:

Copy

@abc.abstractmethod
def find\_distributions(context\=DistributionFinder.Context()) \-> Iterable\[Distribution\]:
    """Return an iterable of all Distribution instances capable of
    loading the metadata for packages for the indicated \`\`context\`\`.
    """

The [`DistributionFinder.Context`](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.DistributionFinder.Context "importlib.metadata.DistributionFinder.Context")
 object provides [`path`](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.DistributionFinder.Context.path "importlib.metadata.DistributionFinder.Context.path")
 and [`name`](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.DistributionFinder.Context.name "importlib.metadata.DistributionFinder.Context.name")
 properties indicating the path to search and name to match and may supply other relevant context sought by the consumer.

In practice, to support finding distribution package metadata in locations other than the file system, subclass `Distribution` and implement the abstract methods. Then from a custom finder, return instances of this derived `Distribution` in the `find_distributions()` method.

### Example[¶](https://docs.python.org/3/library/importlib.metadata.html#example "Link to this heading")

Imagine a custom finder that loads Python modules from a database:

Copy

class DatabaseImporter(importlib.abc.MetaPathFinder):
    def \_\_init\_\_(self, db):
        self.db \= db

    def find\_spec(self, fullname, target\=None) \-> ModuleSpec:
        return self.db.spec\_from\_name(fullname)

sys.meta\_path.append(DatabaseImporter(connect\_db(...)))

That importer now presumably provides importable modules from a database, but it provides no metadata or entry points. For this custom importer to provide metadata, it would also need to implement [`DistributionFinder`](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.DistributionFinder "importlib.metadata.DistributionFinder")
:

Copy

from importlib.metadata import DistributionFinder

class DatabaseImporter(DistributionFinder):
    ...

    def find\_distributions(self, context\=DistributionFinder.Context()):
        query \= dict(name\=context.name) if context.name else {}
        for dist\_record in self.db.query\_distributions(query):
            yield DatabaseDistribution(dist\_record)

In this way, `query_distributions` would return records for each distribution served by the database matching the query. For example, if `requests-1.0` is in the database, `find_distributions` would yield a `DatabaseDistribution` for `Context(name='requests')` or `Context(name=None)`.

For the sake of simplicity, this example ignores `context.path`. The `path` attribute defaults to `sys.path` and is the set of import paths to be considered in the search. A `DatabaseImporter` could potentially function without any concern for a search path. Assuming the importer does no partitioning, the “path” would be irrelevant. In order to illustrate the purpose of `path`, the example would need to illustrate a more complex `DatabaseImporter` whose behavior varied depending on `sys.path`/`PYTHONPATH`. In that case, the `find_distributions` should honor the `context.path` and only yield `Distribution`s pertinent to that path.

`DatabaseDistribution`, then, would look something like:

Copy

class DatabaseDistribution(importlib.metadata.Distribution):
    def \_\_init\_\_(self, record):
        self.record \= record

    def read\_text(self, filename):
        """
        Read a file like "METADATA" for the current distribution.
        """
        if filename \== "METADATA":
            return f"""Name: {self.record.name}
Version: {self.record.version}
"""
        if filename \== "entry\_points.txt":
            return "\\n".join(
              f"""\[{ep.group}\]\\n{ep.name}\={ep.value}"""
              for ep in self.record.entry\_points)

    def locate\_file(self, path):
        raise RuntimeError("This distribution has no file system")

This basic implementation should provide metadata and entry points for packages served by the `DatabaseImporter`, assuming that the `record` supplies suitable `.name`, `.version`, and `.entry_points` attributes.

The `DatabaseDistribution` may also provide other metadata files, like `RECORD` (required for `Distribution.files`) or override the implementation of `Distribution.files`. See the source for more inspiration.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`importlib.metadata` – Accessing package metadata](https://docs.python.org/3/library/importlib.metadata.html#)
    *   [Overview](https://docs.python.org/3/library/importlib.metadata.html#overview)
        
    *   [Functional API](https://docs.python.org/3/library/importlib.metadata.html#functional-api)
        *   [Entry points](https://docs.python.org/3/library/importlib.metadata.html#entry-points)
            
        *   [Distribution metadata](https://docs.python.org/3/library/importlib.metadata.html#distribution-metadata)
            
        *   [Distribution versions](https://docs.python.org/3/library/importlib.metadata.html#distribution-versions)
            
        *   [Distribution files](https://docs.python.org/3/library/importlib.metadata.html#distribution-files)
            
        *   [Distribution requirements](https://docs.python.org/3/library/importlib.metadata.html#distribution-requirements)
            
        *   [Mapping import to distribution packages](https://docs.python.org/3/library/importlib.metadata.html#mapping-import-to-distribution-packages)
            
    *   [Distributions](https://docs.python.org/3/library/importlib.metadata.html#distributions)
        
    *   [Distribution Discovery](https://docs.python.org/3/library/importlib.metadata.html#distribution-discovery)
        
    *   [Implementing Custom Providers](https://docs.python.org/3/library/importlib.metadata.html#implementing-custom-providers)
        *   [Example](https://docs.python.org/3/library/importlib.metadata.html#example)
            

#### Previous topic

[`importlib.resources.abc` – Abstract base classes for resources](https://docs.python.org/3/library/importlib.resources.abc.html "previous chapter")

#### Next topic

[The initialization of the `sys.path` module search path](https://docs.python.org/3/library/sys_path_init.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=importlib.metadata+%E2%80%93+Accessing+package+metadata&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fimportlib.metadata.html&pagesource=library%2Fimportlib.metadata.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/importlib.metadata.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/sys_path_init.html "The initialization of the sys.path module search path")
     |
*   [previous](https://docs.python.org/3/library/importlib.resources.abc.html "importlib.resources.abc – Abstract base classes for resources")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [The Python standard library](https://docs.python.org/3/library/index.html)
     »
*   [Importing Modules](https://docs.python.org/3/library/modules.html)
     »
*   [`importlib.metadata` – Accessing package metadata](https://docs.python.org/3/library/importlib.metadata.html)
    
*    
    
    |
*   Theme Auto Light Dark |