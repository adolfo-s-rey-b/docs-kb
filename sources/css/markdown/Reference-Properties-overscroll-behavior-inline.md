*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior-inline#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior-inline#mdn-search)
    

`overscroll-behavior-inline` CSS property
=========================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/567)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior-inline#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`overscroll-behavior-inline`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the browser's behavior when the inline direction boundary of a scrolling area is reached.

See [`overscroll-behavior`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior)
 for a full explanation.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior-inline#syntax)

------------------------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior-inline#values)

This property is specified as one of the following keyword values:

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior-inline#auto)

Allows the default behavior at a scroll boundary. Scrolling may continue in another scroll container.

[`chain`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior-inline#chain)

Allows scrolling to continue outside the scroll container, but prevents overscroll "bounce" effects.

[`contain`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior-inline#contain)

Prevents scrolling from continuing outside the scroll container. "Bounce" effects may still occur.

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior-inline#none)

Prevents scrolling from continuing outside the scroll container and also prevents overscroll "bounce" effects.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior-inline#formal_definition)

----------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | non-replaced block-level elements and non-replaced inline-block elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior-inline#formal_syntax)

--------------------------------------------------------------------------------------------------------------------------------

overscroll-behavior-inline =   
  contain  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  none     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  auto     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  chain      

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior-inline#examples)

----------------------------------------------------------------------------------------------------------------------

### [Preventing inline overscrolling](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior-inline#preventing_inline_overscrolling)

In this demo we have two block-level boxes, one inside the other. The outer box has a large [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
 set on it so the page will scroll horizontally. The inner box has a small width (and [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
) set on it so it sits comfortably inside the viewport, but its content is given a large width so it will also scroll horizontally.

By default, when the inner box is scrolled and a scroll boundary is reached, the whole page will begin to scroll, which is probably not what we want. To avoid this happening in the inline direction, we've set `overscroll-behavior-inline: contain` on the inner box.

#### HTML

#### CSS

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior-inline#specifications)

----------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Overscroll Behavior Module Level 1  <br>\# overscroll-behavior-longhands-logical](https://drafts.csswg.org/css-overscroll/#overscroll-behavior-longhands-logical) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior-inline#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior-inline#see_also)

----------------------------------------------------------------------------------------------------------------------

*   [`overscroll-behavior`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior)
    
*   [`overscroll-behavior-x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior-x)
    
*   [`overscroll-behavior-y`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior-y)
    
*   [`overscroll-behavior-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior-block)
    
*   [CSS overscroll behavior](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overscroll_behavior)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 13, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior-inline/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/overscroll-behavior-inline/index.md?plain=1 "Folder: en-us/web/css/reference/properties/overscroll-behavior-inline (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Foverscroll-behavior-inline&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Foverscroll-behavior-inline%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Foverscroll-behavior-inline%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Foverscroll-behavior-inline%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F151d527b2d48812d732cb4f3fdffa0737682e684%0A*+Document+last+modified%3A+2026-10-13T13%3A35%3A54.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")