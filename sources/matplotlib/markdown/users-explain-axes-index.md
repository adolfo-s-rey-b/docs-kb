[Skip to main content](https://matplotlib.org/stable/users/explain/axes/index.html#main-content)

Back to top Ctrl+K

*   [Plot types](https://matplotlib.org/stable/plot_types/index.html)
    
*   [User guide](https://matplotlib.org/stable/users/index.html)
    
*   [Tutorials](https://matplotlib.org/stable/tutorials/index.html)
    
*   [Examples](https://matplotlib.org/stable/gallery/index.html)
    
*   [Reference](https://matplotlib.org/stable/api/index.html)
    
*   [Contribute](https://matplotlib.org/stable/devel/index.html)
    
*   [Releases](https://matplotlib.org/stable/users/release_notes.html)
    

Choose version

*   [Gitter](https://gitter.im/matplotlib/matplotlib "Gitter")
    
*   [Discourse](https://discourse.matplotlib.org/ "Discourse")
    
*   [GitHub](https://github.com/matplotlib/matplotlib "GitHub")
    

Axes and subplots[#](https://matplotlib.org/stable/users/explain/axes/index.html#axes-and-subplots "Link to this heading")

===========================================================================================================================

Matplotlib [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 are the gateway to creating your data visualizations. Once an Axes is placed on a figure there are many methods that can be used to add data to the Axes. An Axes typically has a pair of [`Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis")
 Artists that define the data coordinate system, and include methods to add annotations like x- and y-labels, titles, and legends.

([`Source code`](https://matplotlib.org/stable/_downloads/5f6b7652323f07a756c6cb043fceeaca/index-1.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/15e1523ba0f3c317ff0d534fd0a6ff50/index-1.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/4861d6343f66d8243a63681b3638c14a/index-1.png)
)

[![](https://matplotlib.org/stable/_images/users-explain-axes-index-1.2x.png)](https://matplotlib.org/stable/_images/users-explain-axes-index-1.2x.png)

*   [Introduction to Axes (or Subplots)](https://matplotlib.org/stable/users/explain/axes/axes_intro.html)
    *   [Creating Axes](https://matplotlib.org/stable/users/explain/axes/axes_intro.html#creating-axes)
        
    *   [Axes plotting methods](https://matplotlib.org/stable/users/explain/axes/axes_intro.html#axes-plotting-methods)
        
    *   [Axes labelling and annotation](https://matplotlib.org/stable/users/explain/axes/axes_intro.html#axes-labelling-and-annotation)
        
    *   [Axes limits, scales, and ticking](https://matplotlib.org/stable/users/explain/axes/axes_intro.html#axes-limits-scales-and-ticking)
        
    *   [Axes layout](https://matplotlib.org/stable/users/explain/axes/axes_intro.html#axes-layout)
        

*   [Arranging multiple Axes in a Figure](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html)
    
*   [Placing colorbars](https://matplotlib.org/stable/users/explain/axes/colorbar_placement.html)
    
*   [Axis autoscaling](https://matplotlib.org/stable/users/explain/axes/autoscale.html)
    

*   [Axis scales](https://matplotlib.org/stable/users/explain/axes/axes_scales.html)
    *   [loglog and semilogx/y](https://matplotlib.org/stable/users/explain/axes/axes_scales.html#loglog-and-semilogx-y)
        
    *   [Other built-in scales](https://matplotlib.org/stable/users/explain/axes/axes_scales.html#other-built-in-scales)
        
    *   [Optional arguments for scales](https://matplotlib.org/stable/users/explain/axes/axes_scales.html#optional-arguments-for-scales)
        
    *   [Arbitrary function scales](https://matplotlib.org/stable/users/explain/axes/axes_scales.html#arbitrary-function-scales)
        
    *   [What is a "scale"?](https://matplotlib.org/stable/users/explain/axes/axes_scales.html#what-is-a-scale)
        
*   [Axis ticks](https://matplotlib.org/stable/users/explain/axes/axes_ticks.html)
    *   [Manual location and formats](https://matplotlib.org/stable/users/explain/axes/axes_ticks.html#manual-location-and-formats)
        
    *   [Locators and Formatters](https://matplotlib.org/stable/users/explain/axes/axes_ticks.html#locators-and-formatters)
        
    *   [Styling ticks (tick parameters)](https://matplotlib.org/stable/users/explain/axes/axes_ticks.html#styling-ticks-tick-parameters)
        
    *   [Tick objects](https://matplotlib.org/stable/users/explain/axes/axes_ticks.html#tick-objects)
        
*   [Plotting dates and strings](https://matplotlib.org/stable/users/explain/axes/axes_units.html)
    *   [Date conversion](https://matplotlib.org/stable/users/explain/axes/axes_units.html#date-conversion)
        
    *   [String conversion: categorical plots](https://matplotlib.org/stable/users/explain/axes/axes_units.html#string-conversion-categorical-plots)
        
    *   [Determine converter, formatter, and locator on an axis](https://matplotlib.org/stable/users/explain/axes/axes_units.html#determine-converter-formatter-and-locator-on-an-axis)
        
    *   [More about "unit" support](https://matplotlib.org/stable/users/explain/axes/axes_units.html#more-about-unit-support)
        
*   [Legends](https://matplotlib.org/stable/users/explain/axes/legend_guide.html)
    *   [Controlling the legend entries](https://matplotlib.org/stable/users/explain/axes/legend_guide.html#controlling-the-legend-entries)
        
    *   [Creating artists specifically for adding to the legend (aka. Proxy artists)](https://matplotlib.org/stable/users/explain/axes/legend_guide.html#creating-artists-specifically-for-adding-to-the-legend-aka-proxy-artists)
        
    *   [Legend location](https://matplotlib.org/stable/users/explain/axes/legend_guide.html#legend-location)
        
    *   [Multiple legends on the same Axes](https://matplotlib.org/stable/users/explain/axes/legend_guide.html#multiple-legends-on-the-same-axes)
        
    *   [Legend handlers](https://matplotlib.org/stable/users/explain/axes/legend_guide.html#legend-handlers)
        
*   [Subplot mosaic](https://matplotlib.org/stable/users/explain/axes/mosaic.html)
    *   [String short-hand](https://matplotlib.org/stable/users/explain/axes/mosaic.html#string-short-hand)
        
    *   [Axes spanning multiple rows/columns](https://matplotlib.org/stable/users/explain/axes/mosaic.html#axes-spanning-multiple-rows-columns)
        
    *   [Controlling mosaic creation](https://matplotlib.org/stable/users/explain/axes/mosaic.html#controlling-mosaic-creation)
        
    *   [Controlling subplot creation](https://matplotlib.org/stable/users/explain/axes/mosaic.html#controlling-subplot-creation)
        
    *   [Nested list input](https://matplotlib.org/stable/users/explain/axes/mosaic.html#nested-list-input)
        
    *   [Axis sharing](https://matplotlib.org/stable/users/explain/axes/mosaic.html#axis-sharing)
        

*   [Constrained layout guide](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html)
    
*   [Tight layout guide (mildly discouraged)](https://matplotlib.org/stable/users/explain/axes/tight_layout_guide.html)