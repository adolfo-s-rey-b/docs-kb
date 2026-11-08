[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_file.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.datasets.fetch_file.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_file.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.datasets.fetch_file.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.datasets.fetch_file.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.datasets.fetch_file.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.datasets.fetch_file.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.datasets.fetch_file.html)

Collapse Sidebar Expand Sidebar

fetch\_file[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_file.html#fetch-file "Link to this heading")

=====================================================================================================================================

sklearn.datasets.fetch\_file(_url_, _folder\=None_, _local\_filename\=None_, _sha256\=None_, _n\_retries\=3_, _delay\=1_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/datasets/_base.py#L1587)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_file.html#sklearn.datasets.fetch_file "Link to this definition")

Fetch a file from the web if not already present in the local folder.

If the file already exists locally (and the SHA256 checksums match when provided), the path to the local file is returned without re-downloading.

Added in version 1.6.

Parameters:

**url**str

URL of the file to download.

**folder**str or Path, default=None

Directory to save the file to. If None, the file is downloaded in a folder with a name derived from the URL host name and path under scikit-learn data home folder.

**local\_filename**str, default=None

Name of the file to save. It must be a plain filename. A value holding a directory separator or a relative reference such as `".."`, raises `ValueError`. If None, the filename is inferred from the URL.

**sha256**str, default=None

SHA256 checksum of the file. If None, no checksum is verified.

**n\_retries**int, default=3

Number of retries when HTTP errors are encountered.

**delay**int, default=1

Number of seconds between retries.

Returns:

**file\_path**Path

Full path of the downloaded file.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_file.html#gallery-examples "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_time_series_lagged_features_thumb.png)

[Lagged features for time series forecasting](https://scikit-learn.org/stable/auto_examples/applications/plot_time_series_lagged_features.html)

Lagged features for time series forecasting

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_wikipedia_principal_eigenvector_thumb.png)

[Wikipedia principal eigenvector](https://scikit-learn.org/stable/auto_examples/applications/plot_wikipedia_principal_eigenvector.html)

Wikipedia principal eigenvector

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)