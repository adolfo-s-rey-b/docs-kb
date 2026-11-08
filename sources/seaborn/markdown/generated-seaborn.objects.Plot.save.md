 

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

seaborn.objects.Plot.save[#](https://seaborn.pydata.org/generated/seaborn.objects.Plot.save.html#seaborn-objects-plot-save "Permalink to this heading")

========================================================================================================================================================

Plot.save(_loc_, _\*\*kwargs_)[#](https://seaborn.pydata.org/generated/seaborn.objects.Plot.save.html#seaborn.objects.Plot.save "Permalink to this definition")

Compile the plot and write it to a buffer or file on disk.

Parameters:

**loc**str, path, or buffer

Location on disk to save the figure, or a buffer to write into.

**kwargs**

Other keyword arguments are passed through to [`matplotlib.figure.Figure.savefig()`](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.Figure.savefig "(in Matplotlib v3.8.2)")
.