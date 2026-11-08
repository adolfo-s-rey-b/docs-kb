*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@position-try#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@position-try#mdn-search)
    

`@position-try` CSS at-rule
===========================

Baseline 2026

Newly available

Since January 2026, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/245)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@position-try#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`@position-try`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/At-rules)
 is used to define a custom position try fallback option, which can be used to define positioning and alignment for anchor-positioned elements. One or more sets of position try fallback options can be applied to the anchored element via the [`position-try-fallbacks`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try-fallbacks)
 property or [`position-try`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try)
 shorthand. When the positioned element is moved to a position where it starts to overflow its containing block or the viewport, the browser will select the first position try fallback option it finds that places the positioned element fully back on-screen.

Each position option is named with a [`<dashed-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)
 and contains a descriptor list specifying declarations that define information such as inset position, margin, sizing, and self-alignment. The `<dashed-ident>` is used to reference the custom position option in the [`position-try-fallbacks`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try-fallbacks)
 property and [`position-try`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try)
 shorthand.

For detailed information on anchor features and position try fallback usage, see the [CSS anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning)
 module and the [Fallback options and conditional hiding for overflow](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Try_options_hiding)
 guide.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@position-try#syntax)

---------------------------------------------------------------------------------------------------

css

    @position-try --try-option-name {
      descriptor-list
    }
    

**Note:** The `--try-option-name` is a [`<dashed-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)
 specifying an identifying name for the custom position option, which can then be used to add that fallback option to the [`position-try-fallbacks`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try-fallbacks)
 list.

### [Descriptors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@position-try#descriptors)

The descriptors specify property values that define the behavior of the custom position option, i.e., where it will result in the positioned element being placed.

[`position-anchor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@position-try#position-anchor)

Specifies a [`position-anchor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor)
 property value that defines the anchor element that the positioned element is tethered to, by specifying a [`<dashed-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)
 value equal to the anchor element's [`anchor-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-name)
 property value.

[`position-area`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@position-try#position-area)

Specifies a [`position-area`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-area)
 property value that defines the position of the anchor-positioned element relative to the anchor.

[Inset property](https://developer.mozilla.org/en-US/docs/Glossary/Inset_properties)
 descriptors

Specify [`anchor()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor)
 function values that define the position of the anchor-positioned element's edges relative to the anchor element's edge. Inset property descriptors can be set that represent the following properties:

*   [`top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/top)
    
*   [`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/left)
    
*   [`bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/bottom)
    
*   [`right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/right)
    .
*   [`inset-block-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-block-start)
    
*   [`inset-block-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-block-end)
    
*   [`inset-inline-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-inline-start)
    
*   [`inset-inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-inline-end)
    
*   [`inset-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-block)
    
*   [`inset-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-inline)
    
*   [`inset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset)
    

[Margin property descriptors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@position-try#margin_property_descriptors)

Specify the margin set on the anchor-positioned element. Margin property descriptors can be set that represent the following properties:

*   [`margin-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-top)
    
*   [`margin-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-left)
    
*   [`margin-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-bottom)
    
*   [`margin-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-right)
    
*   [`margin-block-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-block-start)
    
*   [`margin-block-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-block-end)
    
*   [`margin-inline-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline-start)
    
*   [`margin-inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline-end)
    
*   [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
    
*   [`margin-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-block)
    
*   [`margin-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline)
    

[Sizing property descriptors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@position-try#sizing_property_descriptors)

Specify [`anchor-size()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size)
 function values that define the size of the anchor-positioned element relative to the anchor element size. Sizing property descriptors can be set that represent the following properties:

*   [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
    
*   [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
    
*   [`min-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-width)
    
*   [`min-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-height)
    
*   [`max-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-width)
    
*   [`max-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-height)
    
*   [`block-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/block-size)
    
*   [`inline-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inline-size)
    
*   [`min-block-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-block-size)
    
*   [`min-inline-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-inline-size)
    
*   [`max-block-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-block-size)
    
*   [`max-inline-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-inline-size)
    

[Self-alignment property descriptors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@position-try#self-alignment_property_descriptors)

Specify the [`anchor-center`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Using#centering_on_the_anchor_using_anchor-center)
 value to align the anchor-positioned element relative to the anchor element's center, in the block or inline direction. [`align-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self)
 and [`justify-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self)
 property descriptors can take the `anchor-center` value.

**Note:** When a custom position option is applied to an element, the property values defined in the `@position-try` at-rule descriptor takes precedence over the values set on the element via standard CSS properties.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@position-try#formal_syntax)

-----------------------------------------------------------------------------------------------------------------

@position-try =   
  @position-try [<dashed-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)
 { <declaration-list> }    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@position-try#examples)

-------------------------------------------------------------------------------------------------------

### [Custom position option usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@position-try#custom_position_option_usage)

In this example, we define an anchor element and an anchor-positioned element, then create four named custom position try fallback options. These options are applied to the positioned element to ensure its contents are always visible no matter where the anchor element is within the viewport.

#### HTML

We include two [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 elements that will become an anchor and an anchor-positioned element:

html

    <div class="anchor">⚓︎</div>
    
    <div class="infobox">
      <p>This is an information box.</p>
    </div>
    

#### CSS

We first style the `<body>` element to be very large, so that we can scroll the anchor and the positioned element around in the viewport, both horizontally and vertically:

css

    body {
      width: 1500px;
      height: 500px;
    }
    

    .anchor {
      font-size: 1.8rem;
      color: white;
      text-shadow: 1px 1px 1px black;
      background-color: hsl(240 100% 75%);
      width: fit-content;
      border-radius: 10px;
      border: 1px solid black;
      padding: 3px;
    }
    

The anchor is given an [`anchor-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-name)
 and has a [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position)
 value of `absolute` set on it. We then position it somewhere near the center of the initial `<body>` rendering using [`top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/top)
 and [`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/left)
 values:

css

    .anchor {
      anchor-name: --my-anchor;
      position: absolute;
      top: 100px;
      left: 350px;
    }
    

    .infobox {
      color: darkblue;
      background-color: azure;
      border: 1px solid #dddddd;
      padding: 10px;
      border-radius: 10px;
      font-size: 1rem;
    }
    

Next, we use the `@position-try` at-rule to define four custom position options, with descriptive [`<dashed-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)
 names to identify them and describe their purpose. Each one places the positioned element in a specific position around the anchor element and gives it an appropriate `10px` margin between the positioned element and its anchor. The positioning is handled in a variety of ways, to demonstrate the different techniques available:

*   The first and last position options use a [`position-area`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-area)
    .
*   The second position option uses [`top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/top)
     with an [`anchor()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor)
     value and [`justify-self: anchor-center`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self)
     to center the positioned element on the anchor in the inline direction.
*   The third position option uses [`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/left)
     with an [`anchor()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor)
     value, wrapped inside a [`calc()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc)
     function that adds `10px` of spacing (rather than creating the spacing with [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
     like the other options do). It then uses [`align-self: anchor-center`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self)
     to center the positioned element on the anchor in the block direction.

Finally, the left and right position options are given a narrower [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)

css

    @position-try --custom-left {
      position-area: left;
      width: 100px;
      margin-right: 10px;
    }
    
    @position-try --custom-bottom {
      top: anchor(bottom);
      justify-self: anchor-center;
      margin-top: 10px;
      position-area: none;
    }
    
    @position-try --custom-right {
      left: calc(anchor(right) + 10px);
      align-self: anchor-center;
      width: 100px;
      position-area: none;
    }
    
    @position-try --custom-bottom-right {
      position-area: bottom right;
      margin: 10px 0 0 10px;
    }
    

The infobox is given fixed positioning, a [`position-anchor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor)
 property that references the anchor's `anchor-name` to associate the two together, and it is tethered to the anchor's top edge using a [`position-area`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-area)
. We also give it a fixed [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
 and some bottom [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
. The custom position options are then referenced in the [`position-try-fallbacks`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try-fallbacks)
 property to prevent the positioned element from overflowing, or being scrolled out of view, when the anchor gets near the edge of the viewport.

css

    .infobox {
      position: fixed;
      position-anchor: --my-anchor;
      position-area: top;
      width: 200px;
      margin-bottom: 10px;
      position-try-fallbacks:
        --custom-left, --custom-bottom, --custom-right, --custom-bottom-right;
    }
    

#### Result

Scroll the page and notice the change in the positioned element's placement as the anchor nears the different edges of the viewport. This is due to different fallback position options being applied.

Let's talk through how these position options work:

*   First of all, note that our default position is defined by `position-area: top`. When the infobox isn't overflowing the page in any direction, the infobox sits above the anchor, and the position try fallback options set in the `position-try-fallbacks` property are ignored. Also note that the infobox has a fixed width and bottom margin set. These values will change as different position try fallback options are applied.
*   If the infobox starts to overflow, the browser first tries the `--custom-left` position. This moves the infobox to the left of the anchor using `position-area: left`, adjusts the margin to suit, and also gives the infobox a different width.
*   Next, the browser tries the `--custom-bottom` position. This moves the infobox to the bottom of the anchor using `top` and `justify-self` instead of a `position-area`, and sets an appropriate margin. It doesn't include a `width` descriptor, so the infobox returns to its default width of `200px` set by the `width` property.
*   The browser next tries the `--custom-right` position. This works much the same as the `--custom-left` position, with the same `width` descriptor value applied. However, we are using `left` and `align-self` to place the positioned element instead of a `position-area`. And we are wrapping the `left` value in a `calc()` function inside which we are adding `10px` to create spacing, instead of using `margin`.
*   If none of the other try fallback options succeed in stopping the positioned element from overflowing, the browser tries the `--custom-bottom-right` position as a last resort. This places the positioned element to the bottom-right of the anchor using `position-area: bottom right`.

When a position option is applied, its values override the initial values set on the positioned element. For example, the `width` initially set on the positioned element is `200px`, but when the `--custom-right` position option is applied, its width is set to `100px`.

In some cases, we need to set values inside the custom position options to turn off the initial values. The `--custom-bottom` and `--custom-right` options use inset property and `*-self: anchor-center` values to place the positioned element, therefore we remove the previously-set `position-area` value in each case by setting `position-area: none`. If we didn't do this, the initially set `position-area: top` value would still take effect and interfere with the other positioning information.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@position-try#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Anchor Positioning Module Level 1  <br>\# at-ruledef-position-try](https://drafts.csswg.org/css-anchor-position-1/#at-ruledef-position-try) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@position-try#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@position-try#see_also)

-------------------------------------------------------------------------------------------------------

*   [`position-area`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-area)
    
*   [`position-anchor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor)
    
*   [`position-try-fallbacks`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try-fallbacks)
    
*   [`position-try`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try)
    
*   The [`anchor()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor)
     function
*   The [`anchor-size()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size)
     function
*   [CSS anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning)
     module
*   [Using CSS anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Using)
     guide
*   [Fallback options and conditional hiding for overflow](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Try_options_hiding)
     guide
*   [`CSSPositionTryRule`](https://developer.mozilla.org/en-US/docs/Web/API/CSSPositionTryRule)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@position-try/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@position-try/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@position-try (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40position-try&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40position-try%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40position-try%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40position-try%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe328268bb418551ab451881845881b5837c9da83%0A*+Document+last+modified%3A+2026-04-20T16%3A14%3A00.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")