*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-anchor#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-anchor#mdn-search)
    

`overflow-anchor` CSS property
==============================

Baseline 2026

Newly available

Since September 2026, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-anchor#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`overflow-anchor`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property provides a way to opt out of the browser's scroll anchoring behavior, which adjusts scroll position to minimize content shifts.

Scroll anchoring behavior is enabled by default in any browser that supports it. Therefore, changing the value of this property is typically only required if you are experiencing problems with scroll anchoring in a document or part of a document and need to turn the behavior off.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-anchor#try_it)

-------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-anchor#syntax)

-------------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-anchor#values)

This property is specified as one of the following keyword values:

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-anchor#auto)

The element becomes a potential anchor when adjusting scroll position.

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-anchor#none)

The element won't be selected as a potential anchor.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-anchor#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-anchor#formal_syntax)

---------------------------------------------------------------------------------------------------------------------

overflow-anchor =   
  auto  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  none    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-anchor#examples)

-----------------------------------------------------------------------------------------------------------

### [Prevent scroll anchoring](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-anchor#prevent_scroll_anchoring)

To prevent scroll anchoring in a document, use the `overflow-anchor` property.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-anchor#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Scroll Anchoring Module Level 1  <br>\# exclusion-api](https://drafts.csswg.org/css-scroll-anchoring/#exclusion-api) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-anchor#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-anchor#see_also)

-----------------------------------------------------------------------------------------------------------

*   [Overview of scroll anchoring](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_anchoring/Overview)
    
*   [CSS scroll anchoring](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_anchoring)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-anchor/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/overflow-anchor/index.md?plain=1 "Folder: en-us/web/css/reference/properties/overflow-anchor (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Foverflow-anchor&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Foverflow-anchor%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Foverflow-anchor%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Foverflow-anchor%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F071fd0613b1b5728d2d83845ea11512cb615067a%0A*+Document+last+modified%3A+2026-07-26T23%3A33%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")