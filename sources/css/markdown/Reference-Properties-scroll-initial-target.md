*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-initial-target#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-initial-target#mdn-search)
    

`scroll-initial-target` CSS property
====================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/275)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-initial-target#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-initial-target#browser_compatibility)
 carefully before using this in production.

The **`scroll-initial-target`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property enables the definition of elements that are potential snap targets when their ancestor [scroll container](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_container)
 is first rendered.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-initial-target#syntax)

-------------------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-initial-target#values)

This property is specified as one of the following keyword values:

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-initial-target#none)

The element is not an initial scroll target.

[`nearest`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-initial-target#nearest)

The element is potentially an initial scroll target for its nearest scroll container ancestor.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-initial-target#description)

-----------------------------------------------------------------------------------------------------------------------

The `scroll-initial-target` property enables defining elements that should be snapped when their parent [scroll snap](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_snap)
 containers are first rendered. Setting the value to `nearest` defines the element as a potential target that should be snapped to when the nearest ancestor [scroll container](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_container)
 first shows up on the page.

If multiple elements or pseudo-elements in the scroll container are set to `nearest`, the first element in the tree order is the initial scroll-snapping target.

The initial value is `none`, meaning a scroll-snappable element is not by default an initial scroll target. The `none` value can also be set on an element to explicitly make it not be an initial scroll target.

If a scroll container's initial scroll position is potentially set by both the [`place-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-content)
 content-distribution property and by `scroll-initial-target` on any descendants — the first descendant with `scroll-initial-target: nearest` wins.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-initial-target#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | the specified keyword |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | Not animatable |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-initial-target#formal_syntax)

---------------------------------------------------------------------------------------------------------------------------

scroll-initial-target =   
  none     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  nearest    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-initial-target#examples)

-----------------------------------------------------------------------------------------------------------------

### [Using `scroll-initial-target`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-initial-target#using_scroll-initial-target)

The example below demonstrates the two values of `scroll-initial-target`, and how the first element with `scroll-initial-target` gets snapped.

#### HTML

We include 5 containers, preceded by a paragraph explaining the expected effect.

#### CSS

We set up the nearest and none elements as scroll-snap containers, centering the snapped elements.

We then set `scroll-initial-target` of either `none` or `nearest` on all the elements with the `.set` class.

#### Result

The property's effect is demonstrated when the scroll-snap container is drawn to the page.

Each row snaps to the first element with `nearest` set, if any, in tree order. In the last example, we've overridden the `nearest` value with `none` on the first element, so the first element with `nearest` applied is #3.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-initial-target#specifications)

-----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Scroll Snap Module Level 2  <br>\# propdef-scroll-initial-target](https://drafts.csswg.org/css-scroll-snap-2/#propdef-scroll-initial-target) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-initial-target#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-initial-target#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [CSS scroll snap](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 28, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-initial-target/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/scroll-initial-target/index.md?plain=1 "Folder: en-us/web/css/reference/properties/scroll-initial-target (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fscroll-initial-target&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fscroll-initial-target%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fscroll-initial-target%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fscroll-initial-target%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb7e9f482c51817d3a885e26092f8219fd0d9d278%0A*+Document+last+modified%3A+2026-09-28T21%3A00%3A55.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")