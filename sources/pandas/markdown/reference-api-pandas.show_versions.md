[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.show_versions.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.show\_versions[#](https://pandas.pydata.org/docs/reference/api/pandas.show_versions.html#pandas-show-versions "Link to this heading")

=============================================================================================================================================

pandas.show\_versions(_as\_json\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/util/_print_versions.py#L89-L158)
[#](https://pandas.pydata.org/docs/reference/api/pandas.show_versions.html#pandas.show_versions "Link to this definition")

Provide useful information, important for bug reports.

It comprises info about hosting operation system, pandas version, and versions of other installed relative packages.

Parameters:

**as\_json**str or bool, default False

*   If False, outputs info in a human readable form to the console.
    
*   If str, it will be considered as a path to a file. Info will be written to that file in JSON format.
    
*   If True, outputs info in JSON format to the console.
    

See also

[`get_option`](https://pandas.pydata.org/docs/reference/api/pandas.get_option.html#pandas.get_option "pandas.get_option")

Retrieve the value of the specified option.

[`set_option`](https://pandas.pydata.org/docs/reference/api/pandas.set_option.html#pandas.set_option "pandas.set_option")

Set the value of the specified option or options.

Examples

\>>> pd.show\_versions()
Your output may look something like this:
INSTALLED VERSIONS
\------------------
commit           : 37ea63d540fd27274cad6585082c91b1283f963d
python           : 3.10.6.final.0
python-bits      : 64
OS               : Linux
OS-release       : 5.10.102.1-microsoft-standard-WSL2
Version          : #1 SMP Wed Mar 2 00:30:59 UTC 2022
machine          : x86\_64
processor        : x86\_64
byteorder        : little
LC\_ALL           : None
LANG             : en\_GB.UTF-8
LOCALE           : en\_GB.UTF-8
pandas           : 2.0.1
numpy            : 1.24.3
...

Copy to clipboard

On this page