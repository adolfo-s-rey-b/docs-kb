 

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

seaborn.objects.Line[#](https://seaborn.pydata.org/generated/seaborn.objects.Line.html#seaborn-objects-line "Permalink to this heading")

=========================================================================================================================================

_class_ seaborn.objects.Line(_artist\_kws=<factory>_, _color=<'C0'>_, _alpha=<1>_, _linewidth=<rc:lines.linewidth>_, _linestyle=<rc:lines.linestyle>_, _marker=<rc:lines.marker>_, _pointsize=<rc:lines.markersize>_, _fillcolor=<depend:color>_, _edgecolor=<depend:color>_, _edgewidth=<rc:lines.markeredgewidth>_)[#](https://seaborn.pydata.org/generated/seaborn.objects.Line.html#seaborn.objects.Line "Permalink to this definition")

A mark connecting data points with sorting along the orientation axis.

This mark defines the following properties:

[color](https://seaborn.pydata.org/tutorial/properties.html#color-property)
, [alpha](https://seaborn.pydata.org/tutorial/properties.html#alpha-property)
, [linewidth](https://seaborn.pydata.org/tutorial/properties.html#linewidth-property)
, [linestyle](https://seaborn.pydata.org/tutorial/properties.html#linestyle-property)
, [marker](https://seaborn.pydata.org/tutorial/properties.html#marker-property)
, [pointsize](https://seaborn.pydata.org/tutorial/properties.html#pointsize-property)
, [fillcolor](https://seaborn.pydata.org/tutorial/properties.html#color-property)
, [edgecolor](https://seaborn.pydata.org/tutorial/properties.html#color-property)
, [edgewidth](https://seaborn.pydata.org/tutorial/properties.html#edgewidth-property)

See also

[`Path`](https://seaborn.pydata.org/generated/seaborn.objects.Path.html#seaborn.objects.Path "seaborn.objects.Path")

A mark connecting data points in the order they appear.

[`Lines`](https://seaborn.pydata.org/generated/seaborn.objects.Lines.html#seaborn.objects.Lines "seaborn.objects.Lines")

A faster but less-flexible mark for drawing many lines.

Examples

The mark draws a connecting line between sorted observations:

so.Plot(dowjones, "Date", "Price").add(so.Line())

Copy to clipboard

[![../_images/objects.Line_1_0.png](https://seaborn.pydata.org/_images/objects.Line_1_0.png)](https://seaborn.pydata.org/_images/objects.Line_1_0.png)

Change the orientation to connect observations along the opposite axis (`orient="y"` is redundant here; the plot would detect that the date variable has a lower orientation priority than the price variable):

so.Plot(dowjones, x\="Price", y\="Date").add(so.Line(), orient\="y")

Copy to clipboard

[![../_images/objects.Line_3_0.png](https://seaborn.pydata.org/_images/objects.Line_3_0.png)](https://seaborn.pydata.org/_images/objects.Line_3_0.png)

To replicate the same line multiple times, assign a `group` variable (but consider using [`Lines`](https://seaborn.pydata.org/generated/seaborn.objects.Lines.html#seaborn.objects.Lines "seaborn.objects.Lines")
 here instead):

(
    fmri
    .query("region == 'parietal' and event == 'stim'")
    .pipe(so.Plot, "timepoint", "signal")
    .add(so.Line(color\=".2", linewidth\=1), group\="subject")
)

Copy to clipboard

[![../_images/objects.Line_5_0.png](https://seaborn.pydata.org/_images/objects.Line_5_0.png)](https://seaborn.pydata.org/_images/objects.Line_5_0.png)

When mapping variables to properties like `color` or `linestyle`, stat transforms are computed within each grouping:

p \= so.Plot(fmri, "timepoint", "signal", color\="region", linestyle\="event")
p.add(so.Line(), so.Agg())

Copy to clipboard

[![../_images/objects.Line_7_0.png](https://seaborn.pydata.org/_images/objects.Line_7_0.png)](https://seaborn.pydata.org/_images/objects.Line_7_0.png)

Combine with [`Band`](https://seaborn.pydata.org/generated/seaborn.objects.Band.html#seaborn.objects.Band "seaborn.objects.Band")
 to show an error bar:

(
    p
    .add(so.Line(), so.Agg())
    .add(so.Band(), so.Est(), group\="event")
)

Copy to clipboard

[![../_images/objects.Line_9_0.png](https://seaborn.pydata.org/_images/objects.Line_9_0.png)](https://seaborn.pydata.org/_images/objects.Line_9_0.png)

Add markers to indicate values where the data were sampled:

p.add(so.Line(marker\="o", edgecolor\="w"), so.Agg(), linestyle\=None)

Copy to clipboard

[![../_images/objects.Line_11_0.png](https://seaborn.pydata.org/_images/objects.Line_11_0.png)](https://seaborn.pydata.org/_images/objects.Line_11_0.png)