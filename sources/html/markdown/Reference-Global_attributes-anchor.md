*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/anchor#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/anchor#mdn-search)
    

`anchor` HTML global attribute
==============================

**Non-standard:** This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/anchor#browser_compatibility)
 carefully before using this in production.

The **`anchor`** [global attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
 is used to associate a positioned element with an anchor element. The attribute's value is the [`id`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/id)
 value of the element you want to anchor the positioned element to. The element can then be positioned using [CSS anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Using)
.

**Note:** Alternatively, you can associate a positioned element with an anchor element via CSS, using the [`anchor-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-name)
 and [`position-anchor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor)
 properties. If both anchoring techniques are used on the same element, the CSS technique takes precedence over the HTML technique.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/anchor#examples)

----------------------------------------------------------------------------------------------------------

### [Basic `anchor` attribute usage](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/anchor#basic_anchor_attribute_usage)

The following example uses HTML to associate a positioned element with an anchor. CSS is then used to tether the positioned element to the right of the anchor.

#### HTML

We create a [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 element with an `id` of `example-anchor`. This is our anchor element. We then include another `<div>` with the `anchor` attribute set to `example-anchor`. This designates the first `<div>` as the anchor for the second `<div>`, associating the two together.

We also include some filler text around the two `<div>`s to make the [`<body>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body)
 taller so that it will scroll.

#### CSS

We use CSS to convert the `infobox` element into an _anchor-positioned element_ and position it relative to its anchor. We set its:

*   [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position)
     property to `fixed`, converting it to a positioned element so it can be positioned relative to the anchor's position.
*   [`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/left)
     property to an [`anchor()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor)
     function with a value of `right`. This tethers the positioned element to its anchor, positioning its left edge flush to the anchor's right edge.
*   [`align-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self)
     property to [`anchor-center`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Using#centering_on_the_anchor_using_anchor-center)
    . This causes the infobox to be aligned centrally to the center of the anchor in the inline direction.
*   [`margin-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-left)
     to `10px`, creating space between the anchor-positioned element and its anchor.

#### Result

Scroll the example to see how the infobox is tethered to the anchor. When the `anchor` attribute is supported, the infobox will be fixed to the right of the anchor. If not supported, the infobox will be fixed to the viewport.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/anchor#specifications)

----------------------------------------------------------------------------------------------------------------------

This attribute is not currently part of the HTML specification. Read the discussion about adding the `anchor` attribute at [https://github.com/whatwg/html/pull/9144](https://github.com/whatwg/html/pull/9144 "External link (opens in new tab)")
.

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/anchor#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/anchor#see_also)

----------------------------------------------------------------------------------------------------------

*   [`HTMLElement.anchorElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/anchorElement)
    
*   CSS [`anchor-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-name)
     property
*   CSS [`position-anchor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor)
     property
*   [CSS anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/anchor/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/global_attributes/anchor/index.md?plain=1 "Folder: en-us/web/html/reference/global_attributes/anchor (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fanchor&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fanchor%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fanchor%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fanchor%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9c70c6ff09189cad43d40e241fbd2fe67349c3c2%0A*+Document+last+modified%3A+2026-04-17T01%3A02%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")