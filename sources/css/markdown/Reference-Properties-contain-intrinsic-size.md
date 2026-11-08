*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-size#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-size#mdn-search)
    

`contain-intrinsic-size` CSS property
=====================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2023.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-size#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`contain-intrinsic-size`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 property sets the size of an element that a browser will use for layout when the element is subject to [size containment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Using#size_containment)
.

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-size#constituent_properties)

----------------------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [`contain-intrinsic-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-width)
    
*   [`contain-intrinsic-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-height)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-size#syntax)

--------------------------------------------------------------------------------------------------------------

css

    /* Keyword value */
    contain-intrinsic-size: none;
    
    /* <length> values */
    contain-intrinsic-size: 1000px;
    contain-intrinsic-size: 10rem;
    
    /* width | height */
    contain-intrinsic-size: 1000px 1.5em;
    
    /* auto <length> */
    contain-intrinsic-size: auto 300px;
    contain-intrinsic-size: auto none;
    
    /* auto width | auto height */
    contain-intrinsic-size: auto 300px auto 4rem;
    
    /* Global values */
    contain-intrinsic-size: inherit;
    contain-intrinsic-size: initial;
    contain-intrinsic-size: revert;
    contain-intrinsic-size: revert-layer;
    contain-intrinsic-size: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-size#values)

The following values may be specified for the `contain-intrinsic-size` property:

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-size#none)

The element has no intrinsic size in the given dimension(s).

[`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-size#length)

The element has the specified [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 in the given dimension(s).

[`auto [<length> | none]`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-size#auto_length_none)

A remembered value of the "normally rendered" element size if one exists and the element is skipping its contents (for example, when it is offscreen); otherwise the specified `<length>`. The `none` keyword may be used in place of `<length>` where `0px` fixed lengths behave differently than `none` (such as in multi column, or grid layouts).

If one value is provided as a keyword, a length or an `auto [<length> | none]` pair, it applies to both width and height.

Two length values may be specified, which apply to the width and height in that order. If two `auto [<length> | none]` pairs are specified, the first pair applies to the width, and the second to the height.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-size#description)

------------------------------------------------------------------------------------------------------------------------

The property is commonly applied alongside elements that can trigger size containment, such as [`contain: size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain)
 and [`content-visibility`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content-visibility)
.

Size containment allows a user agent to lay out an element as though it had a fixed size, preventing unnecessary reflows by avoiding the re-rendering of child elements to determine the actual size (thereby improving user experience). By default, size containment treats elements as though they had no contents, and may collapse the layout in the same way as if the contents had no width or height. The `contain-intrinsic-size` property allows authors to specify an appropriate value to be used as the size for layout.

The `auto <length>` value allows the size of the element to be stored if the element is ever "normally rendered" (with its child elements), and then used instead of the specified length when the element is skipping its contents. This allows offscreen elements with [`content-visibility: auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content-visibility)
 to benefit from size containment without developers having to be as precise in their estimates of element size. The remembered value is not used if the child elements are being rendered (if size containment is enabled, the `<length>` will be used).

In grid and multi column layouts, an explicit size is treated differently than implicit content-based height. Elements might lay out substantially differently than it would have were it simply filled with content up to that height. The `auto none` value allows the element to fall back to `contain-intrinsic-size: none` if no remembered value exists, which will allow the element to be laid out as though it had no contents. This is almost always preferred to setting 0px as the intrinsic size in grid and multi column layouts, where contained elements may overflow their parents and can result in unexpected page layout.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-size#formal_definition)

------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | as each of the properties of the shorthand:  <br><br>*   [`contain-intrinsic-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-width)<br>    : `none`<br>*   [`contain-intrinsic-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-height)<br>    : `none` |
| Applies to | elements for which size containment can apply |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| Percentages | as each of the properties of the shorthand:  <br><br>*   [`contain-intrinsic-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-width)<br>    : no<br>*   [`contain-intrinsic-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-height)<br>    : no |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as each of the properties of the shorthand:  <br><br>*   [`contain-intrinsic-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-width)<br>    : as specified, with <length>s values computed<br>*   [`contain-intrinsic-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-height)<br>    : as specified, with <length>s values computed |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | as each of the properties of the shorthand:  <br><br>*   [`contain-intrinsic-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-width)<br>    : by computed value type<br>*   [`contain-intrinsic-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-height)<br>    : by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-size#formal_syntax)

----------------------------------------------------------------------------------------------------------------------------

contain-intrinsic-size =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 auto[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 none [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<length \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[{1,2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-size#examples)

------------------------------------------------------------------------------------------------------------------

### [Using auto value pairs for intrinsic size](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-size#using_auto_value_pairs_for_intrinsic_size)

This example demonstrates `contain-intrinsic-size: auto <length>` and `contain-intrinsic-size: auto none`, using a layout where there are many elements displayed vertically that have both accurate and incorrect intrinsic size estimations. Using `content-visibility: auto` skips rendering elements when they are offscreen, so this property is a good candidate to combine with `contain-intrinsic-size` to improve rendering performance and minimize [reflows](https://developer.mozilla.org/en-US/docs/Glossary/Reflow)
.

The `contain-intrinsic-size: auto 500px` value pair tells the browser to use 500px as a kind of 'placeholder' size (width and height) for the element when it is offscreen and the page is being laid out. When the user scrolls to the element and it needs to be displayed, the browser will calculate the actual size of the element and its contents. If there is a difference between the placeholder and calculated size this might force a new layout, with accompanying changes to the sidebar position.

Once the browser has actual size information for the element, it will remember this size when the element scrolls offscreen again, and use the remembered size for layout calculations instead of the placeholder value. The benefit is that the browser does not need to repeatedly render the element contents to calculate its size and is especially useful when the contents are complex or depend on network resources or JavaScript.

#### HTML

html

    <div id="container">
      <div id="auto-length-note">
        <p>
          Your browser does not support
          <code>contain-intrinsic-size: auto &lt;length&gt;</code>.
        </p>
      </div>
      <div class="auto-length">
        <p>Item one</p>
      </div>
      <div class="auto-length">
        <p>Item two</p>
      </div>
      <div class="auto-length large-intrinsic-size">
        <p class="small">Item three</p>
      </div>
      <div class="auto-length large-intrinsic-size">
        <p class="small">Item four</p>
      </div>
      <div id="auto-none-note">
        <p>
          Your browser does not support
          <code>contain-intrinsic-size: auto none</code>.
        </p>
      </div>
      <div class="auto-length none">
        <p>Item five</p>
      </div>
      <div class="auto-length none">
        <p>Item six</p>
      </div>
    </div>
    

#### CSS

    div,
    p {
      padding: 1rem;
      margin-bottom: 1rem;
      font-size: 2rem;
      font-family: sans-serif;
    }
    
    code {
      background-color: lightgray;
      padding: 0.25rem;
      border-radius: 0.25rem;
    }
    
    #container {
      width: 90%;
      height: 80%;
    }
    
    .auto-length,
    .auto-length.none {
      display: none;
    }
    
    #auto-length-note,
    #auto-none-note {
      display: block;
      padding: 0;
    }
    
    #auto-length-note p,
    #auto-none-note p {
      padding: 0.5rem;
      width: 100%;
      height: max-content;
      font-size: 1rem;
      line-height: 1.5rem;
      background-color: tomato;
    }
    
    @supports (contain-intrinsic-size: auto none) {
      .auto-length.none {
        display: block;
      }
      #auto-none-note {
        display: none;
      }
    }
    @supports (contain-intrinsic-size: auto 500px) {
      .auto-length {
        display: block;
      }
      #auto-length-note {
        display: none;
      }
    }
    

css

    p {
      height: 500px;
      width: 500px;
      border: 4px dotted;
      background: lightblue;
    }
    
    .auto-length {
      content-visibility: auto;
      contain-intrinsic-size: auto 500px;
      background-color: linen;
      outline: 4px dotted blue;
    }
    
    .large-intrinsic-size {
      /* Setting an inaccurate intrinsic size for the element */
      contain-intrinsic-size: auto 5000px;
      background-color: lightgray;
      outline: 4px dotted red;
    }
    
    .small {
      /* This element is a lot smaller than expected */
      height: 100px;
      width: 100px;
    }
    
    .none {
      background-color: papayawhip;
      contain-intrinsic-size: auto none;
      outline: 4px dotted red;
    }
    

#### Result

*   The first two boxes have an intrinsic size that matches their actual size, so as they flow into view, the layout is recalculated but we see no change in the scrollbar or the scroll position.
    
*   The third and fourth boxes have a huge intrinsic size, so the initial layout that the browser calculated is far too big, and we've made these boxes smaller so that it's obvious when you've reached a point that forces a drastic layout change.
    
    When the third and fourth boxes scroll into view, the size is recalculated, making the box and its parent less tall. The effect is that the scroller jumps down the page (we've effectively scrolled further through the box than we'd estimated) and the scroller is longer, because the entire page is less tall than we'd estimated.
    
*   The last boxes have `auto none`, so they have zero estimated size. When they scroll into view the size of the element and its parent are recalculated to be much larger, so the scroller decreases in size and moves up the bar.
    

After scrolling all the way to the bottom you can subsequently scroll up and down smoothly, because using `content-visibility: auto` saves the actual rendered size of the element for next time it is displayed.

### [Setting the intrinsic size](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-size#setting_the_intrinsic_size)

This example provides selection lists that can be used to modify `contain-intrinsic-size`, `content-visibility` and `contain` on an element in order to observe the effect of the different settings.

#### CSS

css

    #contained_element {
      border: 2px solid green;
      width: 120px;
    }
    .child_element {
      border: 1px solid red;
      background: blue;
      height: 50px;
      width: 150px;
    }
    

#### JavaScript

The code below adds styles to, and removes styles from, the containing element based on the selected options.

js

    const containedElement = document.querySelector("#contained_element");
    const intrinsicSizeSelector = document.querySelector(
      "#contain_intrinsic_size_selector",
    );
    const containSelector = document.querySelector("#contain_selector");
    const contentVisibilitySelector = document.querySelector(
      "#content_visibility_selector",
    );
    
    containedElement.style["contain-intrinsic-size"] =
      intrinsicSizeSelector.options[intrinsicSizeSelector.selectedIndex].text;
    containedElement.style["contain"] =
      containSelector.options[containSelector.selectedIndex].text;
    containedElement.style["content-visibility"] =
      contentVisibilitySelector.options[\
        contentVisibilitySelector.selectedIndex\
      ].text;
    
    intrinsicSizeSelector.addEventListener("change", () => {
      containedElement.style["contain-intrinsic-size"] =
        intrinsicSizeSelector.options[intrinsicSizeSelector.selectedIndex].text;
    });
    
    containSelector.addEventListener("change", () => {
      containedElement.style["contain"] =
        containSelector.options[containSelector.selectedIndex].text;
    });
    
    contentVisibilitySelector.addEventListener("change", () => {
      containedElement.style["content-visibility"] =
        contentVisibilitySelector.options[\
          contentVisibilitySelector.selectedIndex\
        ].text;
    });
    

#### HTML

The HTML defines two buttons, a container element that is subject to containment via the `content-visibility` property.

html

    <p>
      <label for="contain_intrinsic_size_selector">contain-intrinsic-size:</label>
      <select id="contain_intrinsic_size_selector">
        <option>none</option>
        <option>40px 130px</option>
        <option>auto 40px auto 130px</option></select
      >;<br />
    
      <label for="contain_selector">contain:</label>
      <select id="contain_selector">
        <option>none</option>
        <option>size</option>
        <option>strict</option></select
      >;<br />
    
      <label for="content_visibility_selector">content-visibility:</label>
      <select id="content_visibility_selector">
        <option>visible</option>
        <option>auto</option>
        <option>hidden</option></select
      >;
    </p>
    
    <div id="contained_element">
      <div class="child_element"></div>
    </div>
    

#### Result

Use the selectors to apply the given styles to the containing `div` element. Note that when `content-visibility` is `visible` or `auto`, changing `contain-intrinsic-size` makes no difference. However if the content is hidden, having a `contain-intrinsic-size` of `none` collapses the parent element as though its child element had no size.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-size#specifications)

------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Box Sizing Module Level 4  <br>\# propdef-contain-intrinsic-size](https://drafts.csswg.org/css-sizing-4/#propdef-contain-intrinsic-size) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-size#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-size#see_also)

------------------------------------------------------------------------------------------------------------------

*   [`contain-intrinsic-block-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-block-size)
    
*   [`contain-intrinsic-inline-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-inline-size)
    
*   [Using CSS containment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Using)
    
*   [CSS containment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment)
     module
*   [`content-visibility`: the new CSS property that boosts your rendering performance](https://web.dev/articles/content-visibility "External link (opens in new tab)")
     via web.dev (2020)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 16, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-size/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/contain-intrinsic-size/index.md?plain=1 "Folder: en-us/web/css/reference/properties/contain-intrinsic-size (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcontain-intrinsic-size&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcontain-intrinsic-size%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcontain-intrinsic-size%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcontain-intrinsic-size%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F880c2c4b113c6fe127ca3ae3603a56ef7a2eb9a6%0A*+Document+last+modified%3A+2026-09-16T20%3A20%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")