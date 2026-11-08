*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue-interpolation-method#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue-interpolation-method#mdn-search)
    

`<hue-interpolation-method>` CSS type
=====================================

Baseline 2024

Newly available

Since June 2024, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue-interpolation-method#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<hue-interpolation-method>`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
 represents the algorithm used for interpolation between [`<hue>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue)
 values. The interpolation method specifies how to find a midpoint between two hue values based on a color wheel. It is used as a component of the [`<color-interpolation-method>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color-interpolation-method)
 data type.

When interpolating `<hue>` values, the hue interpolation algorithm defaults to [`shorter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue-interpolation-method#shorter)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue-interpolation-method#syntax)

------------------------------------------------------------------------------------------------------------

A `<hue-interpolation-method>` value consists of the name of a hue interpolation algorithm followed by a literal token `hue`:

shorter hue
longer hue
increasing hue
decreasing hue

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue-interpolation-method#values)

Any pair of hue angles correspond to two radii on the [color wheel](https://developer.mozilla.org/en-US/docs/Glossary/Color_wheel)
, which cut the circumference into two possible arcs for interpolation. Both arcs start at the first radius and end at the second radius, but one goes clockwise and the other goes counterclockwise.

**Note:** The following descriptions and illustrations are based on color wheels in which hue angles increase in a clockwise direction. Be aware that there are color wheels where an increase in angles will be a counterclockwise operation.

For a pair of hue angles `θ1` and `θ2` normalized to the range `[0deg, 360deg)`, there are four algorithms to determine which arc is used when interpolating from `θ1` to `θ2`:\
\
[`shorter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue-interpolation-method#shorter)\
\
Use the shorter arc. When the two radii coincide, the arc degenerates to a single point. When both arcs have the same lengths:\
\
*   If `θ1 < θ2`, use the clockwise arc;\
*   If `θ1 > θ2`, use the counterclockwise arc.\
\
| `θ1 = 45deg`, `θ2 = 135deg` | `θ1 = 135deg`, `θ2 = 45deg` |\
| --- | --- |\
| ![shorter with θ1 = 45deg and θ2 = 135deg](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue-interpolation-method/shorter_increasing.png) | ![shorter with θ1 = 135deg and θ2 = 45deg](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue-interpolation-method/shorter_decreasing.png) |\
\
[`longer`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue-interpolation-method#longer)\
\
Use the longer arc. When the two radii coincide:\
\
*   If `θ1 ≤ θ2`, the arc becomes the full circumference with a clockwise orientation.\
*   If `θ1 > θ2`, the arc becomes the full circumference with a counterclockwise orientation.\
\
When both arcs have the same lengths:\
\
*   If `θ1 < θ2`, use the clockwise arc;\
*   If `θ1 > θ2`, use the counterclockwise arc.\
\
| `θ1 = 45deg`, `θ2 = 135deg` | `θ1 = 135deg`, `θ2 = 45deg` |\
| --- | --- |\
| ![longer with θ1 = 45deg and θ2 = 135deg](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue-interpolation-method/longer_decreasing.png) | ![longer with θ1 = 135deg and θ2 = 45deg](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue-interpolation-method/longer_increasing.png) |\
\
[`increasing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue-interpolation-method#increasing)\
\
Use the clockwise arc. When the two radii coincide, the arc degenerates to a single point.\
\
| `θ1 = 45deg`, `θ2 = 135deg` | `θ1 = 135deg`, `θ2 = 45deg` |\
| --- | --- |\
| ![increasing with θ1 = 45deg and θ2 = 135deg](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue-interpolation-method/shorter_increasing.png) | ![increasing with θ1 = 135deg and θ2 = 45deg](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue-interpolation-method/longer_increasing.png) |\
\
[`decreasing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue-interpolation-method#decreasing)\
\
Use the counterclockwise arc. When the two radii coincide, the arc degenerates to a single point.\
\
| `θ1 = 45deg`, `θ2 = 135deg` | `θ1 = 135deg`, `θ2 = 45deg` |\
| --- | --- |\
| ![decreasing with θ1 = 45deg and θ2 = 135deg](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue-interpolation-method/longer_decreasing.png) | ![decreasing with θ1 = 135deg and θ2 = 45deg](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue-interpolation-method/shorter_decreasing.png) |\
\
As there are only two arcs to choose from, these algorithms are pairwise equivalent under certain circumstances. Specifically:\
\
*   If `0deg < θ2 - θ1 < 180deg` or `θ2 - θ1 < -180deg`, `shorter` and `increasing` are equivalent, whereas `longer` and `decreasing` are equivalent.\
*   If `-180deg < θ2 - θ1 < 0deg` or `θ2 - θ1 > 180deg`, `shorter` and `decreasing` are equivalent, whereas `longer` and `increasing` are equivalent.\
\
A notable feature of `increasing` and `decreasing` is that when the hue angle difference passes through `180deg` during transition or animation, the arc will not flip to the other side like `shorter` and `longer` do.\
\
[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue-interpolation-method#formal_syntax)\
\
--------------------------------------------------------------------------------------------------------------------------\
\
<hue-interpolation-method> =   \
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 shorter [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 longer [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 increasing [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 decreasing [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 hue    \
\
[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue-interpolation-method#examples)\
\
----------------------------------------------------------------------------------------------------------------\
\
### [Comparing hue interpolation algorithms](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue-interpolation-method#comparing_hue_interpolation_algorithms)\
\
The following example shows the effect of using different hue interpolation algorithms in a [`linear-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient)\
.\
\
#### HTML\
\
html\
\
    <div class="hsl">\
      <p>HSL</p>\
    </div>\
    <div class="hsl-increasing">\
      <p>HSL increasing</p>\
    </div>\
    <div class="hsl-decreasing">\
      <p>HSL decreasing</p>\
    </div>\
    <div class="hsl-shorter">\
      <p>HSL shorter</p>\
    </div>\
    <div class="hsl-longer">\
      <p>HSL longer</p>\
    </div>\
    <div class="hsl-named">\
      <p>HSL named</p>\
    </div>\
    <div class="hsl-named-longer">\
      <p>HSL named (longer)</p>\
    </div>\
    \
\
#### CSS\
\
    div {\
      border: 1px solid black;\
      height: 50px;\
      margin: 10px;\
      width: 90%;\
    }\
    p {\
      color: white;\
      margin: 6px;\
    }\
    \
    /* Fallback styles */\
    .hsl,\
    .hsl-shorter,\
    .hsl-named {\
      background: linear-gradient(\
        to right,\
        hsl(39 100% 50%),\
        hsl(46 100% 50%),\
        hsl(53 100% 50%),\
        hsl(60 100% 50%)\
      );\
    }\
    .hsl-increasing {\
      background: linear-gradient(\
        to right,\
        hsl(190 100% 50%),\
        hsl(225 100% 50%),\
        hsl(260 100% 50%),\
        hsl(295 100% 50%),\
        hsl(330 100% 50%),\
        hsl(365 100% 50%),\
        hsl(400 100% 50%),\
        hsl(435 100% 50%),\
        hsl(470 100% 50%),\
        hsl(505 100% 50%),\
        hsl(540 100% 50%)\
      );\
    }\
    .hsl-decreasing,\
    .hsl-longer,\
    .hsl-named-longer {\
      background: linear-gradient(\
        to right,\
        hsl(399 100% 50%),\
        hsl(368 100% 50%),\
        hsl(337 100% 50%),\
        hsl(307 100% 50%),\
        hsl(276 100% 50%),\
        hsl(245 100% 50%),\
        hsl(214 100% 50%),\
        hsl(183 100% 50%),\
        hsl(152 100% 50%),\
        hsl(122 100% 50%),\
        hsl(91 100% 50%),\
        hsl(60 100% 50%)\
      );\
    }\
    \
\
css\
\
    .hsl {\
      background: linear-gradient(\
        to right in hsl,\
        hsl(39deg 100% 50%),\
        hsl(60deg 100% 50%)\
      );\
    }\
    .hsl-increasing {\
      background: linear-gradient(\
        to right in hsl increasing hue,\
        hsl(190deg 100% 50%),\
        hsl(180deg 100% 50%)\
      );\
    }\
    .hsl-decreasing {\
      background: linear-gradient(\
        to right in hsl decreasing hue,\
        hsl(39deg 100% 50%),\
        hsl(60deg 100% 50%)\
      );\
    }\
    .hsl-shorter {\
      background: linear-gradient(\
        to right in hsl shorter hue,\
        hsl(39deg 100% 50%),\
        hsl(60deg 100% 50%)\
      );\
    }\
    .hsl-longer {\
      background: linear-gradient(\
        to right in hsl longer hue,\
        hsl(39deg 100% 50%),\
        hsl(60deg 100% 50%)\
      );\
    }\
    .hsl-named {\
      background: linear-gradient(to right in hsl, orange, yellow);\
    }\
    .hsl-named-longer {\
      background: linear-gradient(to right in hsl longer hue, orange, yellow);\
    }\
    \
\
#### Result\
\
[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue-interpolation-method#specifications)\
\
----------------------------------------------------------------------------------------------------------------------------\
\
| Specification |\
| --- |\
| [CSS Color Module Level 4  <br>\# hue-interpolation](https://drafts.csswg.org/css-color/#hue-interpolation) |\
\
[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue-interpolation-method#browser_compatibility)\
\
------------------------------------------------------------------------------------------------------------------------------------------\
\
[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue-interpolation-method#see_also)\
\
----------------------------------------------------------------------------------------------------------------\
\
*   [`<color-interpolation-method>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color-interpolation-method)\
    \
*   [`<hue>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue)\
     data type\
\
Help improve MDN\
----------------\
\
[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)\
\
This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue-interpolation-method/contributors.txt)\
.\
\
[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/hue-interpolation-method/index.md?plain=1 "Folder: en-us/web/css/reference/values/hue-interpolation-method (Opens in a new tab)")\
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fhue-interpolation-method&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fhue-interpolation-method%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fhue-interpolation-method%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fhue-interpolation-method%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc88e03530319b73272fd4f9a9f6ebe878f026004%0A*+Document+last+modified%3A+2026-04-20T01%3A40%3A53.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")