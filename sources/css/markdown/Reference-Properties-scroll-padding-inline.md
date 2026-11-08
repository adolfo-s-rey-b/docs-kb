*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-inline#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-inline#mdn-search)
    

`scroll-padding-inline` CSS property
====================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2021.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-inline#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`scroll-padding-inline`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 property sets the scroll padding of an element in the inline dimension.

The scroll-padding properties define offsets for the _optimal viewing region_ of the scrollport: the region used as the target region for placing things in view of the user. This allows the author to exclude regions of the scrollport that are obscured by other content (such as fixed-positioned toolbars or sidebars) or to put more breathing room between a targeted element and the edges of the scrollport.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-inline#try_it)

-------------------------------------------------------------------------------------------------------------

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-inline#constituent_properties)

---------------------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [`scroll-padding-inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-inline-end)
    
*   [`scroll-padding-inline-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-inline-start)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-inline#syntax)

-------------------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-inline#values)

[`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-inline#length-percentage)

An inwards offset from the corresponding edge of the scrollport, as a valid length or a percentage.

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-inline#auto)

The offset is determined by the user agent. This will generally be 0px, but a user agent is able to detect and do something else if a non-zero value is more appropriate.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-inline#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | as each of the properties of the shorthand:  <br><br>*   [`scroll-padding-inline-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-inline-start)<br>    : `auto`<br>*   [`scroll-padding-inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-inline-end)<br>    : `auto` |
| Applies to | scroll containers |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| Percentages | relative to the scroll container's scrollport |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as each of the properties of the shorthand:  <br><br>*   [`scroll-padding-inline-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-inline-start)<br>    : as specified<br>*   [`scroll-padding-inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-inline-end)<br>    : as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-inline#formal_syntax)

---------------------------------------------------------------------------------------------------------------------------

scroll-padding-inline =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 auto [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <length-percentage \[0,∞\]> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[{1,2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
    
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-inline#specifications)

-----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Scroll Snap Module Level 1  <br>\# propdef-scroll-padding-inline](https://drafts.csswg.org/css-scroll-snap/#propdef-scroll-padding-inline) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-inline#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-inline#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [CSS scroll snap](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap)
     module
*   [Well-controlled scrolling with CSS scroll snap](https://web.dev/articles/css-scroll-snap "External link (opens in new tab)")
     on web.dev (2018)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 16, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-inline/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/scroll-padding-inline/index.md?plain=1 "Folder: en-us/web/css/reference/properties/scroll-padding-inline (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fscroll-padding-inline&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fscroll-padding-inline%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fscroll-padding-inline%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fscroll-padding-inline%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F880c2c4b113c6fe127ca3ae3603a56ef7a2eb9a6%0A*+Document+last+modified%3A+2026-09-16T20%3A20%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")