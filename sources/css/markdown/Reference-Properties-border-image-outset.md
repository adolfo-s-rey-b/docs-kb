*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-outset#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-outset#mdn-search)
    

`border-image-outset` CSS property
==================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-outset#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`border-image-outset`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the distance by which an element's [border image](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image)
 is set out from its border box.

The parts of the border image that are rendered outside the element's border box with `border-image-outset` do not trigger overflow scrollbars and don't capture mouse events.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-outset#try_it)

-----------------------------------------------------------------------------------------------------------

    border-image-outset: 0;
    

    border-image-outset: 15px;
    

    border-image-outset: 30px;
    

    border-image-outset: 40px;
    

    <section id="default-example">
      <div id="example-element">This is a box with a border around it.</div>
    </section>
    

    #example-element {
      width: 80%;
      height: 80%;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 50px;
      background: #fff3d4;
      color: black;
      border: 30px solid;
      border-image: url("/shared-assets/images/examples/border-diamonds.png") 30
        round;
      font-size: 1.2em;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-outset#syntax)

-----------------------------------------------------------------------------------------------------------

css

    /* <length> value */
    border-image-outset: 1rem;
    
    /* <number> value */
    border-image-outset: 1.5;
    
    /* top and bottom | left and right */
    border-image-outset: 1 1.2;
    
    /* top | left and right | bottom */
    border-image-outset: 30px 2 45px;
    
    /* top | right | bottom | left */
    border-image-outset: 7px 12px 14px 5px;
    
    /* Global values */
    border-image-outset: inherit;
    border-image-outset: initial;
    border-image-outset: revert;
    border-image-outset: revert-layer;
    border-image-outset: unset;
    

The `border-image-outset` property may be specified as one, two, three, or four values. Each value is a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 or [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
. Negative values are invalid and will cause the `border-image-outset` declaration to be ignored.

1.  If **one** value is specified, it applies to **all four sides**.
2.  If **two** values are specified, the first applies to the **top and bottom** and the second to the **left and right**.
3.  If **three** values are specified, the first applies to the **top**, the second to the **left and right**, and the third to the **bottom**.
4.  If **four** values are specified, they apply to the **top**, **right**, **bottom**, and **left** in that order (clockwise).

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-outset#values)

[`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)

The size of the `border-image` outset as a dimension — a number with a unit.

[`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)

The size of the `border-image` outset as a multiple of the element's corresponding [`border-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-width)
s. For example, if an element has `border-width: 1em 2px 0 1.5rem`, and `border-image-outset: 2`, the final `border-image-outset` would be calculated as `2em 4px 0 3rem`.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-outset#formal_definition)

---------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `0` |
| Applies to | all elements, except internal table elements when [`border-collapse`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-collapse)<br> is `collapse`. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified, but with relative lengths converted into absolute lengths |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-outset#formal_syntax)

-------------------------------------------------------------------------------------------------------------------------

border-image-outset =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<length \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<number \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[{1,4}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-outset#examples)

---------------------------------------------------------------------------------------------------------------

### [Outsetting a border image](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-outset#outsetting_a_border_image)

#### HTML

html

    <div id="outset">This element has an outset border image!</div>
    

#### CSS

css

    #outset {
      width: 10rem;
      background: #cceeff;
      border: 1.4rem solid;
      border-image: radial-gradient(#ffff22, #5555ff) 40;
      border-image-outset: 1.5; /* 1.5 × 1.4rem = 2.1rem */
      margin: 2.1rem;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-outset#specifications)

---------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Backgrounds and Borders Module Level 3  <br>\# border-image-outset](https://drafts.csswg.org/css-backgrounds/#border-image-outset) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-outset#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-outset#see_also)

---------------------------------------------------------------------------------------------------------------

*   [Backgrounds and borders](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders)
    
*   [Learn CSS: Backgrounds and borders](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Backgrounds_and_borders)
    
*   [Border images in CSS: A key focus area for Interop 2023](https://developer.mozilla.org/en-US/blog/border-images-interop-2023/)
     on MDN blog (2023)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-outset/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/border-image-outset/index.md?plain=1 "Folder: en-us/web/css/reference/properties/border-image-outset (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fborder-image-outset&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fborder-image-outset%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fborder-image-outset%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fborder-image-outset%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")