[Skip to main content](https://pandas.pydata.org/docs/getting_started/install.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/getting_started/install.html)
[3.1 (stable)](https://pandas.pydata.org/docs/getting_started/install.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/getting_started/install.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/getting_started/install.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/getting_started/install.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/getting_started/install.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/getting_started/install.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/getting_started/install.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/getting_started/install.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/getting_started/install.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/getting_started/install.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/getting_started/install.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/getting_started/install.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

Installation[#](https://pandas.pydata.org/docs/getting_started/install.html#installation "Link to this heading")

=================================================================================================================

The pandas development team officially distributes pandas for installation through the following methods:

*   Available on [conda-forge](https://anaconda.org/conda-forge/pandas)
     for installation with the conda package manager.
    
*   Available on [PyPI](https://pypi.org/project/pandas/)
     for installation with pip.
    
*   Available on [Github](https://github.com/pandas-dev/pandas)
     for installation from source.
    

Note

pandas may be installable from other sources besides the ones listed above, but they are **not** managed by the pandas development team.

Python version support[#](https://pandas.pydata.org/docs/getting_started/install.html#python-version-support "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------

See [Python support policy](https://pandas.pydata.org/docs/development/policies.html#policies-python-support)
.

Installing pandas[#](https://pandas.pydata.org/docs/getting_started/install.html#installing-pandas "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

### Installing with Conda[#](https://pandas.pydata.org/docs/getting_started/install.html#installing-with-conda "Link to this heading")

For users working with the [Conda](https://conda.io/en/latest/)
 package manager, pandas can be installed from the `conda-forge` channel.

conda install \-c conda-forge pandas

Copy to clipboard

To install the Conda package manager on your system, the [Miniforge distribution](https://github.com/conda-forge/miniforge?tab=readme-ov-file#install)
 is recommended.

Additionally, it is recommended to install and run pandas from a virtual environment.

conda create \-c conda-forge \-n name\_of\_my\_env python pandas
conda activate name\_of\_my\_env

Copy to clipboard

Tip

For users that are new to Python, the easiest way to install Python, pandas, and the packages that make up the [PyData](https://pydata.org/)
 stack such as [SciPy](https://scipy.org/)
, [NumPy](https://numpy.org/)
 and [Matplotlib](https://matplotlib.org/)
 is with [Anaconda](https://docs.anaconda.com/anaconda/install/)
, a cross-platform (Linux, macOS, Windows) Python distribution for data analytics and scientific computing.

However, pandas from Anaconda is **not** officially managed by the pandas development team.

### Installing with pip[#](https://pandas.pydata.org/docs/getting_started/install.html#installing-with-pip "Link to this heading")

For users working with the [pip](https://pip.pypa.io/en/stable/)
 package manager, pandas can be installed from [PyPI](https://pypi.org/project/pandas/)
.

pip install pandas

Copy to clipboard

pandas can also be installed with sets of optional dependencies to enable certain functionality. For example, to install pandas with the optional dependencies to read Excel files.

pip install "pandas\[excel\]"

Copy to clipboard

The full list of extras that can be installed can be found in the [dependency section.](https://pandas.pydata.org/docs/getting_started/install.html#install-optional-dependencies)

Additionally, it is recommended to install and run pandas from a virtual environment, for example, using the Python standard library’s [venv](https://docs.python.org/3/library/venv.html)

### Installing from source[#](https://pandas.pydata.org/docs/getting_started/install.html#installing-from-source "Link to this heading")

See the [contributing guide](https://pandas.pydata.org/docs/development/contributing.html#contributing)
 for complete instructions on building from the git source tree. Further, see [creating a development environment](https://pandas.pydata.org/docs/development/contributing_environment.html#contributing-environment)
 if you wish to create a pandas development environment.

### Installing the development version of pandas[#](https://pandas.pydata.org/docs/getting_started/install.html#installing-the-development-version-of-pandas "Link to this heading")

Installing the development version is the quickest way to:

*   Try a new feature that will be shipped in the next release (that is, a feature from a pull-request that was recently merged to the main branch).
    
*   Check whether a bug you encountered has been fixed since the last release.
    

The development version is usually uploaded daily to the scientific-python-nightly-wheels index from the PyPI registry of anaconda.org. You can install it by running.

pip install \--pre \--extra-index-url https://pypi.anaconda.org/scientific-python-nightly-wheels/simple pandas

Copy to clipboard

Note

You might be required to uninstall an existing version of pandas to install the development version.

pip uninstall pandas \-y

Copy to clipboard

Running the test suite[#](https://pandas.pydata.org/docs/getting_started/install.html#running-the-test-suite "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------

If pandas has been installed [from source](https://pandas.pydata.org/docs/getting_started/install.html#install-source)
, running `pytest pandas` will run all of pandas unit tests.

The unit tests can also be run from the pandas module itself with the [`test()`](https://pandas.pydata.org/docs/reference/api/pandas.test.html#pandas.test "pandas.test")
 function. The packages required to run the tests can be installed with `pip install "pandas[test]"`.

Note

Test failures are not necessarily indicative of a broken pandas installation.

Dependencies[#](https://pandas.pydata.org/docs/getting_started/install.html#dependencies "Link to this heading")

-----------------------------------------------------------------------------------------------------------------

### Required dependencies[#](https://pandas.pydata.org/docs/getting_started/install.html#required-dependencies "Link to this heading")

pandas requires the following dependencies.

| Package | Minimum supported version |
| --- | --- |
| [NumPy](https://numpy.org/) | 2.0.2 |
| [python-dateutil](https://dateutil.readthedocs.io/en/stable/) | 2.9.0 |
| [tzdata](https://pypi.org/project/tzdata/)<br> \* | /   |

\* `tzdata` is only required on Windows and Pyodide (Emscripten).

Generally, the minimum supported version is ~2 years old from the release date of a major or minor pandas version.

### Optional dependencies[#](https://pandas.pydata.org/docs/getting_started/install.html#optional-dependencies "Link to this heading")

pandas has many optional dependencies that are only used for specific methods. For example, [`pandas.read_hdf()`](https://pandas.pydata.org/docs/reference/api/pandas.read_hdf.html#pandas.read_hdf "pandas.read_hdf")
 requires the `pytables` package, while [`DataFrame.to_markdown()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_markdown.html#pandas.DataFrame.to_markdown "pandas.DataFrame.to_markdown")
 requires the `tabulate` package. If the optional dependency is not installed, pandas will raise an `ImportError` when the method requiring that dependency is called.

With pip, optional pandas dependencies can be installed or managed in a file (e.g. requirements.txt or pyproject.toml) as optional extras (e.g. `pandas[performance, aws]`). All optional dependencies can be installed with `pandas[all]`, and specific sets of dependencies are listed in the sections below.

Generally, the minimum supported version is ~1 years old from the release date of a major or minor pandas version. Older versions of optional dependencies may still work, but they are not tested or considered supported.

#### Performance dependencies (recommended)[#](https://pandas.pydata.org/docs/getting_started/install.html#performance-dependencies-recommended "Link to this heading")

Note

You are highly encouraged to install these libraries, as they provide speed improvements, especially when working with large data sets.

Installable with `pip install "pandas[performance]"`

| Dependency | Minimum Version | pip extra | Notes |
| --- | --- | --- | --- |
| [numexpr](https://github.com/pydata/numexpr) | 2.11.0 | performance | Accelerates certain numerical operations by using multiple cores as well as smart chunking and caching to achieve large speedups |
| [bottleneck](https://github.com/pydata/bottleneck) | 1.5.0 | performance | Accelerates certain types of `nan` by using specialized cython routines to achieve large speedup. |
| [numba](https://github.com/numba/numba) | 0.61.2 | performance | Alternative execution engine for operations that accept `engine="numba"` using a JIT compiler that translates Python functions to optimized machine code using the LLVM compiler. |

#### Visualization[#](https://pandas.pydata.org/docs/getting_started/install.html#visualization "Link to this heading")

Installable with `pip install "pandas[plot, output-formatting]"`.

| Dependency | Minimum Version | pip extra | Notes |
| --- | --- | --- | --- |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 3.10.5 | plot | Plotting library |
| [Jinja2](https://github.com/pallets/jinja) | 3.1.6 | output-formatting | Conditional formatting with DataFrame.style |
| [tabulate](https://github.com/astanin/python-tabulate) | 0.9.0 | output-formatting | Printing in Markdown-friendly format (see [tabulate](https://github.com/astanin/python-tabulate)<br>) |

#### Computation[#](https://pandas.pydata.org/docs/getting_started/install.html#computation "Link to this heading")

Installable with `pip install "pandas[computation]"`.

| Dependency | Minimum Version | pip extra | Notes |
| --- | --- | --- | --- |
| [SciPy](https://github.com/scipy/scipy) | 1.16.1 | computation | Miscellaneous statistical functions |
| [xarray](https://github.com/pydata/xarray) | 2025.7.1 | computation | pandas-like API for N-dimensional data |

#### Excel files[#](https://pandas.pydata.org/docs/getting_started/install.html#excel-files "Link to this heading")

Installable with `pip install "pandas[excel]"`.

| Dependency | Minimum Version | pip extra | Notes |
| --- | --- | --- | --- |
| [xlrd](https://github.com/python-excel/xlrd) | 2.0.2 | excel | Reading for xls files (deprecated; use python-calamine) |
| [xlsxwriter](https://github.com/jmcnamara/XlsxWriter) | 3.2.5 | excel | Writing for xlsx files |
| [openpyxl](https://openpyxl.readthedocs.io/en/stable/) | 3.1.5 | excel | Reading / writing for Excel 2010 xlsx/xlsm/xltx/xltm files |
| [pyxlsb](https://github.com/willtrnr/pyxlsb) | 1.0.10 | excel | Reading for xlsb files (deprecated; use python-calamine) |
| [python-calamine](https://github.com/dimastbk/python-calamine) | 0.4.0 | excel | Reading for xls/xlsx/xlsm/xlsb/xla/xlam/ods files |
| [odfpy](https://github.com/eea/odfpy) | 1.4.1 | excel | Reading / writing for OpenDocument 1.2 files |

#### HTML[#](https://pandas.pydata.org/docs/getting_started/install.html#html "Link to this heading")

Installable with `pip install "pandas[html]"`.

| Dependency | Minimum Version | pip extra | Notes |
| --- | --- | --- | --- |
| [BeautifulSoup4](https://github.com/wention/BeautifulSoup4) | 4.13.4 | html | HTML parser for read\_html |
| [html5lib](https://github.com/html5lib/html5lib-python) | 1.1 | html | HTML parser for read\_html |
| [lxml](https://github.com/lxml/lxml) | 6.0.0 | html | HTML parser for read\_html |

One of the following combinations of libraries is needed to use the top-level [`read_html()`](https://pandas.pydata.org/docs/reference/api/pandas.read_html.html#pandas.read_html "pandas.read_html")
 function:

*   [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup)
     and [html5lib](https://github.com/html5lib/html5lib-python)
    
*   [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup)
     and [lxml](https://lxml.de/)
    
*   [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup)
     and [html5lib](https://github.com/html5lib/html5lib-python)
     and [lxml](https://lxml.de/)
    
*   Only [lxml](https://lxml.de/)
    , although see [HTML Table Parsing](https://pandas.pydata.org/docs/user_guide/io.html#io-html-gotchas)
     for reasons as to why you should probably **not** take this approach.
    

Warning

*   if you install [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup)
     you must install either [lxml](https://lxml.de/)
     or [html5lib](https://github.com/html5lib/html5lib-python)
     or both. [`read_html()`](https://pandas.pydata.org/docs/reference/api/pandas.read_html.html#pandas.read_html "pandas.read_html")
     will **not** work with _only_ [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup)
     installed.
    
*   You are highly encouraged to read [HTML Table Parsing gotchas](https://pandas.pydata.org/docs/user_guide/io.html#io-html-gotchas)
    . It explains issues surrounding the installation and usage of the above three libraries.
    

#### XML[#](https://pandas.pydata.org/docs/getting_started/install.html#xml "Link to this heading")

Installable with `pip install "pandas[xml]"`.

| Dependency | Minimum Version | pip extra | Notes |
| --- | --- | --- | --- |
| [lxml](https://github.com/lxml/lxml) | 6.0.0 | xml | XML parser for read\_xml and tree builder for to\_xml |

#### SQL databases[#](https://pandas.pydata.org/docs/getting_started/install.html#sql-databases "Link to this heading")

Traditional drivers are installable with `pip install "pandas[postgresql, mysql, sql-other]"`

| Dependency | Minimum Version | pip extra | Notes |
| --- | --- | --- | --- |
| [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy) | 2.0.42 | postgresql, mysql, sql-other | SQL support for databases other than sqlite |
| [psycopg2](https://github.com/psycopg/psycopg2) | 2.9.10 | postgresql | PostgreSQL engine for sqlalchemy |
| [pymysql](https://github.com/PyMySQL/PyMySQL) | 1.1.1 | mysql | MySQL engine for sqlalchemy |
| [adbc-driver-postgresql](https://github.com/apache/arrow-adbc) | 1.7.0 | postgresql | ADBC Driver for PostgreSQL |
| [adbc-driver-sqlite](https://github.com/apache/arrow-adbc) | 1.7.0 | sql-other | ADBC Driver for SQLite |

#### Other data sources[#](https://pandas.pydata.org/docs/getting_started/install.html#other-data-sources "Link to this heading")

Installable with `pip install "pandas[hdf5, parquet, iceberg, feather, spss, excel]"`

| Dependency | Minimum Version | pip extra | Notes |
| --- | --- | --- | --- |
| [PyTables](https://github.com/PyTables/PyTables) | 3.10.2 | hdf5 | HDF5-based reading / writing |
| [zlib](https://github.com/madler/zlib) |     | hdf5 | Compression for HDF5 |
| [fastparquet](https://github.com/dask/fastparquet) | 2024.11.0 |     | Parquet reading / writing (pyarrow is default) |
| [pyarrow](https://github.com/apache/arrow) | 16.0.0 | parquet, feather | Parquet, ORC, and feather reading / writing |
| [PyIceberg](https://py.iceberg.apache.org/) | 0.9.1 | iceberg | Apache Iceberg reading / writing |
| [pyreadstat](https://github.com/Roche/pyreadstat) | 1.3.0 | spss | SPSS files (.sav) reading |
| [odfpy](https://github.com/eea/odfpy) | 1.4.1 | excel | Open document format (.odf, .ods, .odt) reading / writing |

Warning

*   If you want to use [`read_orc()`](https://pandas.pydata.org/docs/reference/api/pandas.read_orc.html#pandas.read_orc "pandas.read_orc")
    , it is highly recommended to install pyarrow using conda. [`read_orc()`](https://pandas.pydata.org/docs/reference/api/pandas.read_orc.html#pandas.read_orc "pandas.read_orc")
     may fail if pyarrow was installed from pypi, and [`read_orc()`](https://pandas.pydata.org/docs/reference/api/pandas.read_orc.html#pandas.read_orc "pandas.read_orc")
     is not compatible with Windows OS.
    

#### Access data in the cloud[#](https://pandas.pydata.org/docs/getting_started/install.html#access-data-in-the-cloud "Link to this heading")

Installable with `pip install "pandas[fss, aws, gcp]"`

| Dependency | Minimum Version | pip extra | Notes |
| --- | --- | --- | --- |
| [fsspec](https://github.com/fsspec) | 2025.7.0 | fss, gcp, aws | Handling files aside from simple local and HTTP (required dependency of s3fs, gcsfs). |
| [gcsfs](https://github.com/fsspec/gcsfs) | 2025.7.0 | gcp | Google Cloud Storage access |
| [s3fs](https://github.com/fsspec/s3fs) | 2025.7.0 | aws | Amazon S3 access |

#### Clipboard[#](https://pandas.pydata.org/docs/getting_started/install.html#clipboard "Link to this heading")

Installable with `pip install "pandas[clipboard]"`.

| Dependency | Minimum Version | pip extra | Notes |
| --- | --- | --- | --- |
| [PyQt5](https://pypi.org/project/PyQt5/) | 5.15.11 | clipboard | Clipboard I/O |
| [qtpy](https://github.com/spyder-ide/qtpy) | 2.4.3 | clipboard | Clipboard I/O |

Note

Depending on operating system, system-level packages may need to installed. For clipboard to operate on Linux one of the CLI tools `xclip` or `xsel` must be installed on your system.

#### Compression[#](https://pandas.pydata.org/docs/getting_started/install.html#compression "Link to this heading")

Installable with `pip install "pandas[compression]"`

| Dependency | Minimum Version | pip extra | Notes |
| --- | --- | --- | --- |
| [Zstandard](https://github.com/facebook/zstd) | 0.23.0 | compression | Zstandard compression |

#### Timezone[#](https://pandas.pydata.org/docs/getting_started/install.html#timezone "Link to this heading")

Installable with `pip install "pandas[timezone]"`

| Dependency | Minimum Version | pip extra | Notes |
| --- | --- | --- | --- |
| [pytz](https://github.com/stub42/pytz) | 2020.1 | timezone | Alternative timezone library to `zoneinfo`. |

On this page