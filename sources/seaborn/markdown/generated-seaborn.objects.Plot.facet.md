 

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

seaborn.objects.Plot.facet[#](https://seaborn.pydata.org/generated/seaborn.objects.Plot.facet.html#seaborn-objects-plot-facet "Permalink to this heading")

===========================================================================================================================================================

Plot.facet(_col\=None_, _row\=None_, _order\=None_, _wrap\=None_)[#](https://seaborn.pydata.org/generated/seaborn.objects.Plot.facet.html#seaborn.objects.Plot.facet "Permalink to this definition")

Produce subplots with conditional subsets of the data.

Parameters:

**col, row**data vectors or identifiers

Variables used to define subsets along the columns and/or rows of the grid. Can be references to the global data source passed in the constructor.

**order**list of strings, or dict with dimensional keys

Define the order of the faceting variables.

**wrap**int

When using only `col` or `row`, wrap subplots across a two-dimensional grid with this many subplots on the faceting dimension.

Examples

Assigning a faceting variable will create multiple subplots and plot subsets of the data on each of them:

p \= so.Plot(penguins, "bill\_length\_mm", "bill\_depth\_mm").add(so.Dots())
p.facet("species")

Copy to clipboard

[![../_images/objects.Plot.facet_2_0.png](https://seaborn.pydata.org/_images/objects.Plot.facet_2_0.png)](https://seaborn.pydata.org/_images/objects.Plot.facet_2_0.png)

Multiple faceting variables can be defined to create a two-dimensional grid:

p.facet("species", "sex")

Copy to clipboard

[![../_images/objects.Plot.facet_4_0.png](https://seaborn.pydata.org/_images/objects.Plot.facet_4_0.png)](https://seaborn.pydata.org/_images/objects.Plot.facet_4_0.png)

Facet variables can be provided as references to the global plot data or as vectors:

p.facet(penguins\["island"\])

Copy to clipboard

[![../_images/objects.Plot.facet_6_0.png](https://seaborn.pydata.org/_images/objects.Plot.facet_6_0.png)](https://seaborn.pydata.org/_images/objects.Plot.facet_6_0.png)

With a single faceting variable, arrange the facets or limit to a subset by passing a list of levels to `order`:

p.facet("species", order\=\["Gentoo", "Adelie"\])

Copy to clipboard

[![../_images/objects.Plot.facet_8_0.png](https://seaborn.pydata.org/_images/objects.Plot.facet_8_0.png)](https://seaborn.pydata.org/_images/objects.Plot.facet_8_0.png)

With multiple variables, pass `order` as a dictionary:

p.facet("species", "sex", order\={"col": \["Gentoo", "Adelie"\], "row": \["Female", "Male"\]})

Copy to clipboard

[![../_images/objects.Plot.facet_10_0.png](https://seaborn.pydata.org/_images/objects.Plot.facet_10_0.png)](https://seaborn.pydata.org/_images/objects.Plot.facet_10_0.png)

When the faceting variable has multiple levels, you can `wrap` it to distribute subplots across both dimensions:

p \= so.Plot(diamonds, x\="carat", y\="price").add(so.Dots())
p.facet("color", wrap\=4)

Copy to clipboard

[![../_images/objects.Plot.facet_12_0.png](https://seaborn.pydata.org/_images/objects.Plot.facet_12_0.png)](https://seaborn.pydata.org/_images/objects.Plot.facet_12_0.png)

Wrapping works only when there is a single variable, but you can wrap in either direction:

p.facet(row\="color", wrap\=2)

Copy to clipboard

[![../_images/objects.Plot.facet_14_0.png](https://seaborn.pydata.org/_images/objects.Plot.facet_14_0.png)](https://seaborn.pydata.org/_images/objects.Plot.facet_14_0.png)

Use [`Plot.share()`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.share.html#seaborn.objects.Plot.share "seaborn.objects.Plot.share")
 to specify whether facets should be scaled the same way:

p.facet("clarity", wrap\=3).share(x\=False)

Copy to clipboard

[![../_images/objects.Plot.facet_16_0.png](https://seaborn.pydata.org/_images/objects.Plot.facet_16_0.png)](https://seaborn.pydata.org/_images/objects.Plot.facet_16_0.png)

Use [`Plot.label()`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.label.html#seaborn.objects.Plot.label "seaborn.objects.Plot.label")
 to tweak the titles:

p.facet("color").label(title\="{} grade".format)

Copy to clipboard

[![../_images/objects.Plot.facet_18_0.png](https://seaborn.pydata.org/_images/objects.Plot.facet_18_0.png)](https://seaborn.pydata.org/_images/objects.Plot.facet_18_0.png)