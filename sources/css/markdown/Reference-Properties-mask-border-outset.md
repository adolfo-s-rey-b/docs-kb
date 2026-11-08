*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border-outset#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border-outset#mdn-search)
    

`mask-border-outset` CSS property
=================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/225)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border-outset#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`mask-border-outset`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies the distance by which an element's [mask border](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border)
 is set out from its border box.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border-outset#syntax)

----------------------------------------------------------------------------------------------------------

css

    /* <length> value */
    mask-border-outset: 1rem;
    
    /* <number> value */
    mask-border-outset: 1.5;
    
    /* top and bottom | left and right */
    mask-border-outset: 1 1.2;
    
    /* top | left and right | bottom */
    mask-border-outset: 30px 2 45px;
    
    /* top | right | bottom | left */
    mask-border-outset: 7px 12px 14px 5px;
    
    /* Global values */
    mask-border-outset: inherit;
    mask-border-outset: initial;
    mask-border-outset: revert;
    mask-border-outset: revert-layer;
    mask-border-outset: unset;
    

The `mask-border-outset` property may be specified as one, two, three, or four values. Each value is a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 or [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
. Negative values are invalid.

*   When **one** value is specified, it applies the same outset to **all four sides**.
*   When **two** values are specified, the first outset applies to the **top and bottom**, the second to the **left and right**.
*   When **three** values are specified, the first outset applies to the **top**, the second to the **left and right**, the third to the **bottom**.
*   When **four** values are specified, the outsets apply to the **top**, **right**, **bottom**, and **left** in that order (clockwise).

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border-outset#values)

[`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)

The size of the mask border outset as a dimension.

[`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)

The size of the mask border outset as a multiple of the corresponding [`border-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-width)
.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border-outset#formal_definition)

--------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `0` |
| Applies to | all elements; In SVG, it applies to container elements excluding the [`<defs>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/defs)<br> element and all graphics elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified, but with relative lengths converted into absolute lengths |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border-outset#formal_syntax)

------------------------------------------------------------------------------------------------------------------------

mask-border-outset =   
  [<'border-image-outset'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-outset)
    
  
[<border-image-outset>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-outset)
 =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<length \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<number \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[{1,4}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border-outset#examples)

--------------------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border-outset#basic_usage)

This property doesn't appear to be supported anywhere yet. When it eventually starts to be supported, it will serve to move the mask away from the inner edge of the element's border box — you can use it to make the mask start from part way across the border, rather than the inside of it.

css

    mask-border-outset: 1rem;
    

Chromium-based browsers support an outdated version of this property — `mask-box-image-outset` — with a prefix:

css

    -webkit-mask-box-image-outset: 1rem;
    

**Note:** The [`mask-border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border)
 page features a working example (using the out-of-date prefixed border mask properties supported in Chromium), so you can get an idea of the effect.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border-outset#specifications)

--------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Masking Module Level 1  <br>\# the-mask-border-outset](https://drafts.csswg.org/css-masking/#the-mask-border-outset) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border-outset#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border-outset#see_also)

--------------------------------------------------------------------------------------------------------------

*   [`mask-border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border)
    
*   [`mask-border-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border-mode)
    
*   [`mask-border-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border-repeat)
    
*   [`mask-border-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border-source)
    
*   [`mask-border-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border-width)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border-outset/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/mask-border-outset/index.md?plain=1 "Folder: en-us/web/css/reference/properties/mask-border-outset (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fmask-border-outset&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fmask-border-outset%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fmask-border-outset%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fmask-border-outset%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")