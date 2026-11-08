 

 Ctrl+K

Site Navigation

*   [Installing](https://seaborn.pydata.org/installing.html)
    
*   [Gallery](https://seaborn.pydata.org/examples/index.html)
    
*   [Tutorial](https://seaborn.pydata.org/tutorial.html)
    
*   [API](https://seaborn.pydata.org/api.html)
    
*   [Releases](https://seaborn.pydata.org/whatsnew/index.html)
    
*   [Citing](https://seaborn.pydata.org/citing.html)
    
*   [FAQ](https://seaborn.pydata.org/faq.html)
    

*   [GitHub](https://github.com/mwaskom/seaborn "GitHub")
    
*   [StackOverflow](https://stackoverflow.com/tags/seaborn "StackOverflow")
    
*   [Twitter](https://twitter.com/michaelwaskom "Twitter")
    

On this page

seaborn.load\_dataset[#](https://seaborn.pydata.org/generated/seaborn.load_dataset.html#seaborn-load-dataset "Permalink to this heading")

==========================================================================================================================================

seaborn.load\_dataset(_name_, _cache\=True_, _data\_home\=None_, _\*\*kws_)[#](https://seaborn.pydata.org/generated/seaborn.load_dataset.html#seaborn.load_dataset "Permalink to this definition")

Load an example dataset from the online repository (requires internet).

This function provides quick access to a small number of example datasets that are useful for documenting seaborn or generating reproducible examples for bug reports. It is not necessary for normal usage.

Note that some of the datasets have a small amount of preprocessing applied to define a proper ordering for categorical variables.

Use [`get_dataset_names()`](https://seaborn.pydata.org/generated/seaborn.get_dataset_names.html#seaborn.get_dataset_names "seaborn.get_dataset_names")
 to see a list of available datasets.

Parameters:

**name**str

Name of the dataset (`{name}.csv` on [https://github.com/mwaskom/seaborn-data](https://github.com/mwaskom/seaborn-data)
).

**cache**boolean, optional

If True, try to load from the local cache first, and save to the cache if a download is required.

**data\_home**string, optional

The directory in which to cache data; see [`get_data_home()`](https://seaborn.pydata.org/generated/seaborn.get_data_home.html#seaborn.get_data_home "seaborn.get_data_home")
.

**kws**keys and values, optional

Additional keyword arguments are passed to passed through to [`pandas.read_csv()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html#pandas.read_csv "(in pandas v2.2.0)")
.

Returns:

**df**[`pandas.DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "(in pandas v2.2.0)")

Tabular data, possibly with some preprocessing applied.