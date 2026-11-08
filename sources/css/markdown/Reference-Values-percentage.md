*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage#mdn-search)
    

`<percentage>` CSS type
=======================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<percentage>`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
 represents a percentage value. It is often used to define a size as relative to an element's parent object. Numerous properties can use percentages, such as [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
, [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
, [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
, [`padding`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding)
, and [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
.

**Note:** Only calculated values can be inherited. Thus, even if a percentage value is used on the parent property, a real value (such as a width in pixels for a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 value) will be accessible on the inherited property, not the percentage value.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage#syntax)

----------------------------------------------------------------------------------------------

The `<percentage>` data type consists of a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 followed by the percentage sign (`%`). Optionally, it may be preceded by a single `+` or `-` sign, although negative values are not valid for all properties. As with all CSS dimensions, there is no space between the symbol and the number.

[Interpolation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage#interpolation)

------------------------------------------------------------------------------------------------------------

When animated, values of the `<percentage>` data type are [interpolated](https://developer.mozilla.org/en-US/docs/Glossary/Interpolation)
 as real, floating-point numbers. The speed of the interpolation is determined by the [easing function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function)
 associated with the animation.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage#examples)

--------------------------------------------------------------------------------------------------

### [Width and margin-left](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage#width_and_margin-left)

html

    <div class="container">
      <div class="box1">Width: 50%, Left margin: 20%</div>
      <div class="box2">Width: 30%, Left margin: 60%</div>
    </div>
    

css

    .container {
      background-color: navy;
    }
    
    .box1 {
      width: 50%;
      margin-left: 20%;
      background-color: chartreuse;
    }
    
    .box2 {
      width: 30%;
      margin-left: 60%;
      background-color: pink;
    }
    

### [Font-size](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage#font-size)

html

    <div class="container">
      <p>Full-size text (18px)</p>
      <p><span class="half">50% (9px)</span></p>
      <p><span class="double">200% (36px)</span></p>
    </div>
    

css

    .container {
      font-size: 18px;
    }
    
    .half {
      font-size: 50%;
    }
    
    .double {
      font-size: 200%;
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage#specifications)

--------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Values and Units Module Level 4  <br>\# percentages](https://drafts.csswg.org/css-values/#percentages) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage#see_also)

--------------------------------------------------------------------------------------------------

*   [`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
    
*   [CSS values and units](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/percentage/index.md?plain=1 "Folder: en-us/web/css/reference/values/percentage (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fpercentage&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fpercentage%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fpercentage%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fpercentage%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc88e03530319b73272fd4f9a9f6ebe878f026004%0A*+Document+last+modified%3A+2026-04-20T01%3A40%3A53.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")