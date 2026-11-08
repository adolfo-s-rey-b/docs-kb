*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/reading-order#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/reading-order#mdn-search)
    

`reading-order` CSS property
============================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/290)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/reading-order#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/reading-order#browser_compatibility)
 carefully before using this in production.

The **`reading-order`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property enables changing the order in which a child of a [reading flow container](https://developer.mozilla.org/en-US/docs/Glossary/Reading_order#reading_flow_container)
 is read relative to its element siblings.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/reading-order#syntax)

-----------------------------------------------------------------------------------------------------

### [Value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/reading-order#value)

[`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)

Represents the ordinal group the element belongs to.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/reading-order#description)

---------------------------------------------------------------------------------------------------------------

When an element's [block](https://developer.mozilla.org/en-US/docs/Glossary/Block/CSS)
, [flex](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
, or [grid](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout)
 parent container has a [`reading-flow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/reading-flow)
 property set to a value other than `normal`, the `reading-order` property can be used to set the element's [reading flow](https://developer.mozilla.org/en-US/docs/Glossary/Reading_order#reading_flow)
 position relative to that of its siblings.

For reading and navigation, elements inside a block, flex, or grid container are sorted by ascending `reading-order` value. If multiple siblings have the same `reading-order` value, those items are sorted according to the container's `reading-flow`. Siblings not given an explicit `reading-order` value are assigned the default value of `0`, which puts all the children of a reading flow container in the same ordinal group by default.

Sibling elements are ordered starting from the lowest numbered ordinal group to the highest. Therefore, to cause an element to be read out after its siblings, you could set a `reading-order` value or `1` or more on it. To cause an element to be read out before its siblings, you could set a `reading-order` value or `-1` or less on it.

The `reading-order` defines the reading and tabbing order, but has no effect on visual order.

### [Interaction with `tabindex`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/reading-order#interaction_with_tabindex)

If a set of reading flow container child elements that are not normally focusable are made focusable with [`tabindex="0"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/tabindex)
 attributes, their reading order will be modified as expected by the `reading-flow` and `reading-order` properties, in just the same way as interactive elements such as [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
 or [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
.

However, any attempt to modify the tabbing order of a reading flow container's content using positive `tabindex` values will be ignored — overridden by the effects of `reading-flow` and `reading-order`. You generally shouldn't be using these anyway; see [Don't Use Tabindex Greater than 0](https://adrianroselli.com/2014/11/dont-use-tabindex-greater-than-0.html "External link (opens in new tab)")
. The `reading-flow` and `reading-order` properties provide a much better way to modify tabbing order if required.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/reading-order#formal_definition)

---------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `0` |
| Applies to | Block-containers, flex containers, and grid containers |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | The specified integer |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value type |

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/reading-order#examples)

---------------------------------------------------------------------------------------------------------

### [Grid row order](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/reading-order#grid_row_order)

This example demonstrates using `reading-order` to control the positions of individual grid items within a grid container's reading order. One grid item has a `reading-order` value that is lower than the default `0`, so will be read out before its sibling elements. Another has a higher `reading-order` value set, so will be read out after the others, regardless of source or display order.

#### HTML

In our markup we have six [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
 elements contained inside a wrapper [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
.

#### CSS

On the `<div>`, we set the [grid-auto-flow](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-flow)
 property to `dense`, therefore items may display out of source order. The `reading-order` property on the `<a>` element with a class of `top` is set to `-1`, therefore "Item 4" will be the first item in reading flow. The `reading-order` property on the `<a>` element with a class of `bottom` is set to `21`, therefore "Item 4" will be the last item in the reading order. The remaining items will be visited in between, in grid row order, as the `<div>` element's [`reading-flow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/reading-flow)
 property is set to [grid-rows](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row)
.

#### Result

The above demo renders as follows:

Try tabbing through the links. Note how "Item 4" is tabbed to first and "Item 2" is tabbed to last because of their modified `reading-order` values. In between, the items are tabbed to in grid row order.

### [Source order override](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/reading-order#source_order_override)

In this example, the odd-numbered items have a lower `reading-order` value set, so will be read out before the others in a group, regardless of source or display order.

#### HTML

In our markup, we have five `<a>` elements contained inside a wrapper [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
.

html

    <div class="wrapper">
      <a href="#">Item 1</a>
      <a href="#">Item 2</a>
      <a href="#">Item 3</a>
      <a href="#">Item 4</a>
      <a href="#">Item 5</a>
    </div>
    

#### CSS

The `<div>` element's `reading-flow` property is set to `source-order`, which allows `reading-order` to be used to override the default source reading order. The odd-numbered `<a>` elements have a `reading-order` value of `-1`, therefore they are read out before the even-numbered items.

css

    .wrapper {
      reading-flow: source-order;
    }
    
    .wrapper > a {
      display: block;
    }
    
    .wrapper a:nth-child(odd) {
      reading-order: -1;
    }
    

#### Result

The above demo renders as follows:

Try tabbing through the links, and note how "Item 1", "Item 3", and "Item 5" are tabbed to first because of their modified `reading-order`. After that, the items are tabbed to in source order.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/reading-order#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Display Module Level 4  <br>\# propdef-reading-order](https://drafts.csswg.org/css-display-4/#propdef-reading-order) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/reading-order#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/reading-order#see_also)

---------------------------------------------------------------------------------------------------------

*   [`reading-flow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/reading-flow)
    
*   [CSS `reading-flow` examples](https://chrome.dev/reading-flow-examples/ "External link (opens in new tab)")
     via chrome.dev

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/reading-order/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/reading-order/index.md?plain=1 "Folder: en-us/web/css/reference/properties/reading-order (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Freading-order&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Freading-order%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Freading-order%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Freading-order%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")