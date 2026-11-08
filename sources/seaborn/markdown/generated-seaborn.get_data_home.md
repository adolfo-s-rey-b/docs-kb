 

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

seaborn.get\_data\_home[#](https://seaborn.pydata.org/generated/seaborn.get_data_home.html#seaborn-get-data-home "Permalink to this heading")

==============================================================================================================================================

seaborn.get\_data\_home(_data\_home\=None_)[#](https://seaborn.pydata.org/generated/seaborn.get_data_home.html#seaborn.get_data_home "Permalink to this definition")

Return a path to the cache directory for example datasets.

This directory is used by [`load_dataset()`](https://seaborn.pydata.org/generated/seaborn.load_dataset.html#seaborn.load_dataset "seaborn.load_dataset")
.

If the `data_home` argument is not provided, it will use a directory specified by the `SEABORN_DATA` environment variable (if it exists) or otherwise default to an OS-appropriate user cache location.