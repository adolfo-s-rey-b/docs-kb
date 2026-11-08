 

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

seaborn.objects.Text[#](https://seaborn.pydata.org/generated/seaborn.objects.Text.html#seaborn-objects-text "Permalink to this heading")

=========================================================================================================================================

_class_ seaborn.objects.Text(_artist\_kws=<factory>_, _text=<''>_, _color=<'k'>_, _alpha=<1>_, _fontsize=<rc:font.size>_, _halign=<'center'>_, _valign=<'center\_baseline'>_, _offset=<4>_)[#](https://seaborn.pydata.org/generated/seaborn.objects.Text.html#seaborn.objects.Text "Permalink to this definition")

A textual mark to annotate or represent data values.

This mark defines the following properties:

[text](https://seaborn.pydata.org/tutorial/properties.html#property-property)
, [color](https://seaborn.pydata.org/tutorial/properties.html#color-property)
, [alpha](https://seaborn.pydata.org/tutorial/properties.html#alpha-property)
, [fontsize](https://seaborn.pydata.org/tutorial/properties.html#fontsize-property)
, [halign](https://seaborn.pydata.org/tutorial/properties.html#horizontalalignment-property)
, [valign](https://seaborn.pydata.org/tutorial/properties.html#verticalalignment-property)
, [offset](https://seaborn.pydata.org/tutorial/properties.html#offset-property)

Examples

Add text at x/y locations on the plot:

(
    so.Plot(glue, x\="SST-2", y\="MRPC", text\="Model")
    .add(so.Text())
)

Copy to clipboard

[![../_images/objects.Text_1_0.png](https://seaborn.pydata.org/_images/objects.Text_1_0.png)](https://seaborn.pydata.org/_images/objects.Text_1_0.png)

Add bar annotations, horizontally-aligned with `halign`:

(
    so.Plot(glue, x\="Average", y\="Model", text\="Average")
    .add(so.Bar())
    .add(so.Text(color\="w", halign\="right"))
)

Copy to clipboard

[![../_images/objects.Text_3_0.png](https://seaborn.pydata.org/_images/objects.Text_3_0.png)](https://seaborn.pydata.org/_images/objects.Text_3_0.png)

Fine-tune the alignment using `offset`:

(
    so.Plot(glue, x\="Average", y\="Model", text\="Average")
    .add(so.Bar())
    .add(so.Text(color\="w", halign\="right", offset\=6))
)

Copy to clipboard

[![../_images/objects.Text_5_0.png](https://seaborn.pydata.org/_images/objects.Text_5_0.png)](https://seaborn.pydata.org/_images/objects.Text_5_0.png)

Add text above dots, mapping the text color with a third variable:

(
    so.Plot(glue, x\="SST-2", y\="MRPC", color\="Encoder", text\="Model")
    .add(so.Dot())
    .add(so.Text(valign\="bottom"))

)

Copy to clipboard

[![../_images/objects.Text_7_0.png](https://seaborn.pydata.org/_images/objects.Text_7_0.png)](https://seaborn.pydata.org/_images/objects.Text_7_0.png)

Map the text alignment for better use of space:

(
    so.Plot(glue, x\="RTE", y\="MRPC", color\="Encoder", text\="Model")
    .add(so.Dot())
    .add(so.Text(), halign\="Encoder")
    .scale(halign\={"LSTM": "left", "Transformer": "right"})
)

Copy to clipboard

[![../_images/objects.Text_9_0.png](https://seaborn.pydata.org/_images/objects.Text_9_0.png)](https://seaborn.pydata.org/_images/objects.Text_9_0.png)

Use additional matplotlib parameters to control the appearance of the text:

(
    so.Plot(glue, x\="RTE", y\="MRPC", color\="Encoder", text\="Model")
    .add(so.Dot())
    .add(so.Text({"fontweight": "bold"}), halign\="Encoder")
    .scale(halign\={"LSTM": "left", "Transformer": "right"})
)

Copy to clipboard

[![../_images/objects.Text_11_0.png](https://seaborn.pydata.org/_images/objects.Text_11_0.png)](https://seaborn.pydata.org/_images/objects.Text_11_0.png)