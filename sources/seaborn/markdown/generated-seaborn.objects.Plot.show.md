 

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

seaborn.objects.Plot.show[#](https://seaborn.pydata.org/generated/seaborn.objects.Plot.show.html#seaborn-objects-plot-show "Permalink to this heading")

========================================================================================================================================================

Plot.show(_\*\*kwargs_)[#](https://seaborn.pydata.org/generated/seaborn.objects.Plot.show.html#seaborn.objects.Plot.show "Permalink to this definition")

Compile the plot and display it by hooking into pyplot.

Calling this method is not necessary to render a plot in notebook context, but it may be in other environments (e.g., in a terminal). After compiling the plot, it calls [`matplotlib.pyplot.show()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "(in Matplotlib v3.8.2)")
 (passing any keyword parameters).

Unlike other [`Plot`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.html#seaborn.objects.Plot "seaborn.objects.Plot")
 methods, there is no return value. This should be the last method you call when specifying a plot.