 

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

seaborn.objects.Dodge[#](https://seaborn.pydata.org/generated/seaborn.objects.Dodge.html#seaborn-objects-dodge "Permalink to this heading")

============================================================================================================================================

_class_ seaborn.objects.Dodge(_empty\='keep'_, _gap\=0_, _by\=None_)[#](https://seaborn.pydata.org/generated/seaborn.objects.Dodge.html#seaborn.objects.Dodge "Permalink to this definition")

Displacement and narrowing of overlapping marks along orientation axis.

Parameters:

**empty**{‘keep’, ‘drop’, ‘fill’}

**gap**float

Size of gap between dodged marks.

**by**list of variable names

Variables to apply the movement to, otherwise use all.

Examples

This transform modifies both the width and position (along the orientation axis) of marks that would otherwise overlap:

(
    so.Plot(tips, "day", color\="time")
    .add(so.Bar(), so.Count(), so.Dodge())
)

Copy to clipboard

[![../_images/objects.Dodge_1_0.png](https://seaborn.pydata.org/_images/objects.Dodge_1_0.png)](https://seaborn.pydata.org/_images/objects.Dodge_1_0.png)

By default, empty space may appear when variables are not fully crossed:

p \= so.Plot(tips, "day", color\="time")
p.add(so.Bar(), so.Count(), so.Dodge())

Copy to clipboard

[![../_images/objects.Dodge_3_0.png](https://seaborn.pydata.org/_images/objects.Dodge_3_0.png)](https://seaborn.pydata.org/_images/objects.Dodge_3_0.png)

The `empty` parameter handles this case; use it to fill out the space:

p.add(so.Bar(), so.Count(), so.Dodge(empty\="fill"))

Copy to clipboard

[![../_images/objects.Dodge_5_0.png](https://seaborn.pydata.org/_images/objects.Dodge_5_0.png)](https://seaborn.pydata.org/_images/objects.Dodge_5_0.png)

Or center the marks while using a consistent width:

p.add(so.Bar(), so.Count(), so.Dodge(empty\="drop"))

Copy to clipboard

[![../_images/objects.Dodge_7_0.png](https://seaborn.pydata.org/_images/objects.Dodge_7_0.png)](https://seaborn.pydata.org/_images/objects.Dodge_7_0.png)

Use `gap` to add a bit of spacing between dodged marks:

p \= so.Plot(tips, "day", "total\_bill", color\="sex")
p.add(so.Bar(), so.Agg("sum"), so.Dodge(gap\=.1))

Copy to clipboard

[![../_images/objects.Dodge_9_0.png](https://seaborn.pydata.org/_images/objects.Dodge_9_0.png)](https://seaborn.pydata.org/_images/objects.Dodge_9_0.png)

When multiple semantic variables are used, each distinct group will be dodged:

p.add(so.Dot(), so.Dodge(), fill\="smoker")

Copy to clipboard

[![../_images/objects.Dodge_11_0.png](https://seaborn.pydata.org/_images/objects.Dodge_11_0.png)](https://seaborn.pydata.org/_images/objects.Dodge_11_0.png)

Use `by` to dodge only a subset of variables:

p.add(so.Dot(), so.Dodge(by\=\["color"\]), fill\="smoker")

Copy to clipboard

[![../_images/objects.Dodge_13_0.png](https://seaborn.pydata.org/_images/objects.Dodge_13_0.png)](https://seaborn.pydata.org/_images/objects.Dodge_13_0.png)

When combining with other transforms (such as [`Jitter`](https://seaborn.pydata.org/generated/seaborn.objects.Jitter.html#seaborn.objects.Jitter "seaborn.objects.Jitter")
 or [`Stack`](https://seaborn.pydata.org/generated/seaborn.objects.Stack.html#seaborn.objects.Stack "seaborn.objects.Stack")
), be mindful of the order that they are applied in:

p.add(so.Dot(), so.Dodge(), so.Jitter())

Copy to clipboard

[![../_images/objects.Dodge_15_0.png](https://seaborn.pydata.org/_images/objects.Dodge_15_0.png)](https://seaborn.pydata.org/_images/objects.Dodge_15_0.png)