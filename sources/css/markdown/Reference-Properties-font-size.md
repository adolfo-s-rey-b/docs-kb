*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size#mdn-search)
    

`font-size` CSS property
========================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`font-size`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the size of the font. Changing the font size also updates the sizes of the font size-relative [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 units, such as `em`, `ex`, and so forth.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size#try_it)

-------------------------------------------------------------------------------------------------

    font-size: 1.2rem;
    

    font-size: x-small;
    

    font-size: smaller;
    

    font-size: 12px;
    

    font-size: 80%;
    

    <section id="default-example">
      <p id="example-element">
        London. Michaelmas term lately over, and the Lord Chancellor sitting in
        Lincoln's Inn Hall. Implacable November weather. As much mud in the streets
        as if the waters had but newly retired from the face of the earth, and it
        would not be wonderful to meet a Megalosaurus, forty feet long or so,
        waddling like an elephantine lizard up Holborn Hill.
      </p>
    </section>
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size#syntax)

-------------------------------------------------------------------------------------------------

css

    /* <absolute-size> values */
    font-size: xx-small;
    font-size: x-small;
    font-size: small;
    font-size: medium;
    font-size: large;
    font-size: x-large;
    font-size: xx-large;
    font-size: xxx-large;
    
    /* <relative-size> values */
    font-size: smaller;
    font-size: larger;
    
    /* <length> values */
    font-size: 12px;
    font-size: 0.8em;
    
    /* <percentage> values */
    font-size: 80%;
    
    /* math value */
    font-size: math;
    
    /* Global values */
    font-size: inherit;
    font-size: initial;
    font-size: revert;
    font-size: revert-layer;
    font-size: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size#values)

This property is specified as a single value from the following list:

[`xx-small`, `x-small`, `small`, `medium`, `large`, `x-large`, `xx-large`, `xxx-large`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size#xx-small)

[Absolute-size](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/absolute-size)
 keywords, based on the user's default font size (which is `medium`).

[`larger`, `smaller`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size#larger)

[Relative-size](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/relative-size)
 keywords. The font will be larger or smaller relative to the parent element's font size, roughly by the ratio used to separate the absolute-size keywords above.

[`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)

A positive [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 value. For most font-relative units (such as `em` and `ex`), the font size is relative to the parent element's font size.

For font-relative units that are root-based (such as `rem`), the font size is relative to the size of the font used by the [`<html>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/html)
 (root) element.

[`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)

A positive [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 value, relative to the parent element's font size.

**Note:** To maximize accessibility, it is generally best to use values that are relative to the user's default font size.

[`math`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size#math)

[Scaling rules](https://w3c.github.io/mathml-core/#the-math-script-level-property "External link (opens in new tab)")
 are applied when determining the computed value of the `font-size` property for math elements relative to the `font-size` of the containing parent. See the [math-depth](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-depth)
 property for more information.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size#description)

-----------------------------------------------------------------------------------------------------------

There are several ways to specify the font size, including keywords or numerical values for pixels or ems. Choose the appropriate method based on the needs of the particular web page.

### [Keywords](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size#keywords)

Keywords are a good way to set the size of fonts on the web. By setting a keyword font size on the [`<body>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body)
 element, you can set relative font-sizing everywhere else on the page, giving you the ability to easily scale the font up or down on the entire page accordingly.

### [Pixels](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size#pixels)

Setting the font size in pixel values (`px`) is a good choice when you need pixel accuracy. A px value is static. This is an OS-independent and cross-browser way of literally telling the browsers to render the letters at exactly the number of pixels in height that you specified. The results may vary slightly across browsers, as they may use different algorithms to achieve a similar effect.

Font sizing settings can also be used in combination. For example, if a parent element is set to `16px` and its child element is set to `larger`, the child element displays larger than the parent element on the page.

**Note:** Defining font sizes in `px` is _[not accessible](https://en.wikipedia.org/wiki/Web_accessibility "External link (opens in new tab)")
_, because the user cannot change the font size in some browsers. For example, users with limited vision may wish to set the font size much larger than the size chosen by a web designer. Avoid using them for font sizes if you wish to create an inclusive design.

### [Ems](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size#ems)

Using an `em` value creates a dynamic or computed font size (historically the `em` unit was derived from the width of a capital "M" in a given typeface.). The numeric value acts as a multiplier of the `font-size` property of the element on which it is used. Consider this example:

css

    p {
      font-size: 2em;
    }
    

In this case, the font size of `<p>` elements will be double the computed `font-size` inherited by `<p>` elements. By extension, a `font-size` of `1em` equals the computed `font-size` of the element on which it is used.

If a `font-size` has not been set on any of the `<p>`'s ancestors, then `1em` will equal the default browser `font-size`, which is usually `16px`. So, by default `1em` is equivalent to `16px`, and `2em` is equivalent to `32px`. If you were to set a `font-size` of 20px on the `<body>` element say, then `1em` on the `<p>` elements would instead be equivalent to `20px`, and `2em` would be equivalent to `40px`.

In order to calculate the `em` equivalent for any pixel value required, you can use this formula:

em = desired element pixel value / parent element font-size in pixels

For example, suppose the `font-size` of the `<body>` of the page is set to `16px`. If the font-size you want is `12px`, then you should specify `0.75em` (because 12/16 = 0.75). Similarly, if you want a font size of `10px`, then specify `0.625em` (10/16 = 0.625); for `22px`, specify `1.375em` (22/16).

The `em` is a very useful unit in CSS since it automatically adapts its length relative to the font that the reader chooses to use.

One important fact to keep in mind: em values compound. Take the following HTML and CSS:

css

    html {
      font-size: 100%;
    }
    span {
      font-size: 1.6em;
    }
    

html

    <div>
      <span>Outer <span>inner</span> outer</span>
    </div>
    

The result is:

Assuming that the browser's default `font-size` is 16px, the words "outer" would be rendered at 25.6px, but the word "inner" would be rendered at 40.96px. This is because the inner [`<span>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/span)
's `font-size` is 1.6em which is relative to its parent's `font-size`, which is in turn relative to its parent's `font-size`. This is often called **compounding**.

### [Rems](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size#rems)

`rem` values were invented in order to sidestep the compounding problem. `rem` values are relative to the root `html` element, not the parent element. In other words, it lets you specify a font size in a relative fashion without being affected by the size of the parent, thereby eliminating compounding.

The CSS below is nearly identical to the previous example. The only exception is that the unit has been changed to `rem`.

css

    html {
      font-size: 100%;
    }
    span {
      font-size: 1.6rem;
    }
    

Then we apply this CSS to the same HTML, which looks like this:

html

    <span>Outer <span>inner</span> outer</span>
    

In this example, the words "outer inner outer" are all displayed at 25.6px (assuming that the browser's `font-size` has been left at the default value of 16px).

### [Ex](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size#ex)

Like the `em` unit, an element's `font-size` set using the `ex` unit is computed or dynamic. It behaves in exactly the same way, except that when setting the `font-size` property using `ex` units, the `font-size` equals the x-height of the [first available font](https://drafts.csswg.org/css-fonts/#first-available-font "External link (opens in new tab)")
 used on the page. The number value multiplies the element's inherited `font-size` and the `font-size` compounds relatively.

See the W3C Editor's Draft for a more detailed description of [font-relative length units](https://drafts.csswg.org/css-values-4/#font-relative-length "External link (opens in new tab)")
 such as `ex`.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size#formal_definition)

-----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `medium` |
| Applies to | all elements and text. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br> and [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| Percentages | refer to the parent element's font size |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | absolute [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length) |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size#formal_syntax)

---------------------------------------------------------------------------------------------------------------

font-size =   
  <absolute-size>            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <relative-size>            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <length-percentage \[0,∞\]>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  math                         
  
[<absolute-size>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/absolute-size)
 =   
  xx-small   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  x-small    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  small      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  medium     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  large      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  x-large    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  xx-large   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  xxx-large    
  
[<relative-size>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/relative-size)
 =   
  larger   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  smaller    
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size#examples)

-----------------------------------------------------------------------------------------------------

### [Setting font sizes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size#setting_font_sizes)

#### CSS

css

    .small {
      font-size: xx-small;
    }
    .larger {
      font-size: larger;
    }
    .point {
      font-size: 24pt;
    }
    .percent {
      font-size: 200%;
    }
    

#### HTML

html

    <h1 class="small">Small H1</h1>
    <h1 class="larger">Larger H1</h1>
    <h1 class="point">24 point H1</h1>
    <h1 class="percent">200% H1</h1>
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size#specifications)

-----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fonts Module Level 4  <br>\# font-size-prop](https://drafts.csswg.org/css-fonts/#font-size-prop) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size#see_also)

-----------------------------------------------------------------------------------------------------

*   [`font-size-adjust`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size-adjust)
    
*   [`font-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style)
    
*   [`font-weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight)
    
*   [`math-depth`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-depth)
    
*   [`math-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-style)
    
*   SVG [`font-size`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/font-size)
     attribute
*   [Learn: Fundamental text and font styling](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Text_styling/Fundamentals)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 11, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/font-size/index.md?plain=1 "Folder: en-us/web/css/reference/properties/font-size (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-size&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-size%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-size%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-size%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa5531a7b1fa30ab1de952ffff619a9830eb1c1a9%0A*+Document+last+modified%3A+2026-08-11T19%3A18%3A35.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")