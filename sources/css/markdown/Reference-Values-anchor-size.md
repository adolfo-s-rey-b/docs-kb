*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size#mdn-search)
    

`anchor-size()` CSS function
============================

Baseline 2026

Newly available

\*

Since January 2026, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/245)

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`anchor-size()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 enables setting anchor-positioned element's [size](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Using#sizing_elements_based_on_anchor_size)
, [position](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Using#setting_element_position_based_on_anchor_size)
, and [margins](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Using#setting_element_margin_based_on_anchor_size)
 relative to the dimensions of anchor elements. It returns the `<length>` of a specified side of the target anchor element. `anchor-size()` is only valid when used within the value of anchor-positioned elements' [sizing, inset, and margin properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size#properties_that_accept_anchor-size_function_values)
.

For detailed information on anchor features and usage, see the [CSS anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning)
 module and the [Using CSS anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Using)
 guide.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size#syntax)

-----------------------------------------------------------------------------------------------

css

    /* without parameters */
    anchor-size()
    
    /* anchor size parameter */
    anchor-size(width);
    anchor-size(block);
    anchor-size(self-inline);
    
    /* anchor-name and anchor-side */
    width: anchor-size(--my-anchor width);
    block-size: anchor-size(--my-anchor block);
    
    /* sizing relative to named anchor's side with fallback */
    width: anchor-size(--my-anchor width, 50%);
    block-size: anchor-size(--my-anchor block, 200px);
    
    /* positioning relative to anchor side */
    left: anchor-size(width);
    inset-inline-end: anchor-size(--my-anchor height, 100px);
    
    /* setting margin relative to anchor side */
    margin-left: calc(anchor-size(width) / 4);
    margin-block-start: anchor-size(--my-anchor self-block, 20px);
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size#parameters)

The `anchor-size()` function's syntax is as follows:

anchor-size(<anchor-name> <anchor-size>, <length-percentage>)

The parameters are:

[`<anchor-name>` Optional](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size#anchor-name)

The [`anchor-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-name)
 property value of an anchor element you want to set the element's size, position, or margins relative to. This is a `<dashed-ident>` value. If omitted, the element's default anchor is used.

**Note:** Specifying an `<anchor-name>` inside an `anchor-size()` function neither associates nor tethers an element to an anchor; it only defines which anchor the element's property values should be set relative to.

[`<anchor-size>` Optional](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size#anchor-size)

Specifies the dimension of the anchor element that the positioned element's property values will be set relative to. Valid values include:

[`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size#width)

The width of the anchor element.

[`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size#height)

The height of the anchor element.

[`block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size#block)

The length of the anchor element's [containing block](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block)
 in the block direction.

[`inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size#inline)

The length of the anchor element's containing block in the inline direction.

[`self-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size#self-block)

The length of the anchor element in the block direction.

[`self-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size#self-inline)

The length of the anchor element in the inline direction.

**Note:** If this parameter is omitted, the dimension defaults to the `<anchor-size>` keyterm that matches the axis of the property in which the function is included. For example, `width: anchor-size();` is equivalent to `width: anchor-size(width);`.

[`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 Optional

Specifies the size to use as a fallback value if the element is not absolutely or fixed positioned, or the anchor element doesn't exist. If this parameter is omitted in a case when the fallback would otherwise be used, the declaration is invalid.

**Note:** The anchor dimension you set the positioned element's property values relative to does not have to be along the same axis as the sizing value being set. For example, `width: anchor-size(height)` is valid.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size#return_value)

Returns a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 value.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size#description)

---------------------------------------------------------------------------------------------------------

The `anchor-size()` function enables a positioned element's sizing, position, and margin values to be expressed in terms of an anchor element's dimensions; it returns a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 value representing the dimension of a specific anchor element the positioned element's property values are set relative to. It is a valid value for [sizing, inset, and margin properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size#properties_that_accept_anchor-size_function_values)
 set on anchor-positioned elements.

The length returned is the vertical or horizontal size of an anchor element or its containing block. The dimension used is defined by the `<anchor-size>` parameter. If that parameter is omitted, the dimension used will match the axis of the sizing, position, or margin property is it set on. So for example:

*   `width: anchor-size()` is equivalent to `width: anchor-size(width)`.
*   `top: anchor-size()` is equivalent to `top: anchor-size(height)`.
*   `margin-inline-end: anchor-size()` is equivalent to `margin-inline-end: anchor-size(self-inline)`. `margin-inline-end: anchor-size()` is also equivalent to `margin-inline-end: anchor-size(width)` in horizontal writing modes, or `margin-inline-end: anchor-size(height)` in vertical writing modes.

The anchor element used as the basis for the dimension length is the element with the `anchor-name` specified in the `<anchor-name>` parameter. If more than one element has the same anchor name, the last element with that anchor name in the DOM order is used.

If no `<anchor-name>` parameter is included in the function call, the element's **default anchor**, referenced in its [`position-anchor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor)
 property, or associated with the element via the [`anchor`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/anchor)
 HTML attribute, is used.

If an `<anchor-name>` parameter is included and there are no elements matching that anchor name, the fallback value is used. If no fallback was included, the declaration is ignored. For example, if `width: anchor-size(--foo width, 50px); height: anchor-size(--foo width);` were specified on the positioned element but no anchor named `--foo` exists in the DOM, the `width` would be `50px` and the `height` declaration would have no effect.

If an element has sizing, position, or margin properties with `anchor-size()` values set on them, but it is not an anchor-positioned element (it does not have its [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position)
 property set to `absolute` or `fixed` or does not have an anchor associated with it via its `position-anchor` property), the fallback value will be used if one is available. If no fallback is available, the declaration is ignored.

For example, if `width: anchor-size(width, 50px);` were specified on the positioned element but no anchor was associated with it, the fallback value would be used, so `width` would get a computed value of `50px`.

For detailed information on anchor features and usage, see the [CSS anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning)
 module and the [Using CSS anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Using)
 guide.

### [Properties that accept `anchor-size()` function values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size#properties_that_accept_anchor-size_function_values)

The properties that accept an `anchor-size()` function as a value include:

*   Sizing properties:
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
        
*   Inset properties:
    *   [`bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/bottom)
        
    *   [`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/left)
        
    *   [`right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/right)
        
    *   [`top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/top)
        
    *   [`inset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset)
         shorthand
    *   [`inset-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-block)
         shorthand
    *   [`inset-block-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-block-end)
        
    *   [`inset-block-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-block-start)
        
    *   [`inset-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-inline)
         shorthand
    *   [`inset-inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-inline-end)
        
    *   [`inset-inline-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-inline-start)
        
*   Margin properties:
    *   [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
         shorthand
    *   [`margin-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-bottom)
        
    *   [`margin-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-left)
        
    *   [`margin-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-right)
        
    *   [`margin-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-top)
        
    *   [`margin-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-block)
         shorthand
    *   [`margin-block-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-block-end)
        
    *   [`margin-block-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-block-start)
        
    *   [`margin-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline)
         shorthand
    *   [`margin-inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline-end)
        
    *   [`margin-inline-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline-start)
        

### [Using `anchor-size()` inside `calc()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size#using_anchor-size_inside_calc)

The most common `anchor-size()` functions you'll use will just refer to a dimension of the default anchor. Alternative, include the `anchor-size()` function inside a [`calc()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc)
 function to modify the size applied to the positioned element.

For example, this rule sizes the positioned element's width equal to the default anchor element's width:

css

    .positionedElem {
      width: anchor-size(width);
    }
    

This rule sizes the positioned element's inline size to 4 times the anchor element's inline size, with the multiplication being done inside a [`calc()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc)
 function:

css

    .positionedElem {
      inline-size: calc(anchor-size(self-inline) * 4);
    }
    

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size#formal_syntax)

-------------------------------------------------------------------------------------------------------------

<anchor-size()> =   
  anchor-size( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <anchor-name> [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 <anchor-size> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 , <length-percentage>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
<anchor-name> =   
  [<dashed-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)
    
  
<anchor-size> =   
  width        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  height       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  block        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  inline       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  self-block   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  self-inline    
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size#examples)

---------------------------------------------------------------------------------------------------

### [Basic `anchor-size()` usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size#basic_anchor-size_usage)

This example shows two elements positioned relative to an anchor and sized using `anchor-size()` functions.

#### HTML

We specify three [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 elements, one `anchor` element and the two `infobox` elements we'll position relative to the anchor. We also include filler text to make the [`<body>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body)
 tall enough to require scrolling, but this has been hidden for the sake of brevity.

    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
    
    <p>
      Nisi quis eleifend quam adipiscing vitae proin sagittis nisl rhoncus. In arcu
      cursus euismod quis viverra nibh cras pulvinar. Vulputate ut pharetra sit amet
      aliquam.
    </p>
    

html

    <div class="anchor">⚓︎</div>
    
    <div class="infobox" id="infobox1">
      <p>This is the first infobox.</p>
    </div>
    
    <div class="infobox" id="infobox2">
      <p>This is the second infobox.</p>
    </div>
    

    <p>
      Malesuada nunc vel risus commodo viverra maecenas accumsan lacus. Vel elit
      scelerisque mauris pellentesque pulvinar pellentesque habitant morbi
      tristique. Porta lorem mollis aliquam ut porttitor. Turpis cursus in hac
      habitasse platea dictumst quisque. Dolor sit amet consectetur adipiscing elit.
      Ornare lectus sit amet est placerat. Nulla aliquet porttitor lacus luctus
      accumsan.
    </p>
    

#### CSS

We declare the `anchor` `<div>` as an anchor element by giving it an [`anchor-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-name)
. The positioned elements, with their [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position)
 properties set to `fixed`, are associated with the anchor element via their [`position-anchor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor)
 properties. We also set absolute [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
 and [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
 dimensions on the anchor to provide a reference point when checking the positioned element dimensions, for example, with browser developer tools:

    .anchor {
      font-size: 2rem;
      color: white;
      text-shadow: 1px 1px 1px black;
      background-color: hsl(240 100% 75%);
      text-align: center;
      align-content: center;
      outline: 1px solid black;
    }
    
    body {
      width: 80%;
      margin: 0 auto;
    }
    
    .infobox {
      align-content: center;
      color: darkblue;
      background-color: azure;
      outline: 1px solid #dddddd;
      font-size: 1rem;
      text-align: center;
    }
    

css

    .anchor {
      anchor-name: --my-anchor;
      width: 100px;
      height: 50px;
    }
    
    .infobox {
      position-anchor: --my-anchor;
      position: fixed;
    }
    

We set some distinct property values on the positioned elements:

*   The positioned elements are tethered to the anchor with different [`position-area`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-area)
     values that position the elements in different places around the anchor element.
*   The [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
     of the first infobox is set to the same height as the anchor element: `anchor-size(height)` returns the anchor element's height. The element's [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
     is set to double the anchor element's width using the `anchor-size()` function within a [`calc()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc)
     function: `anchor-size(width)` retrieves the anchor element's width, which is then multiplied by two.
*   The [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
     of the second infobox is set to 80% of the anchor element's height, using a similar technique.
*   Margin values are included to provide some separation from the anchor element.

css

    #infobox1 {
      position-area: right;
      height: anchor-size(height);
      width: calc(anchor-size(width) * 2);
      margin-left: 5px;
    }
    
    #infobox2 {
      position-area: top span-right;
      height: calc(anchor-size(height) / 1.25);
      margin-bottom: 5px;
    }
    

#### Result

Use your browser tools to inspect the anchor-positioned elements. The first infobox will be `50px` tall and `200px` wide, while the second infobox will be `40px` tall, with the `width` defaulting to [`max-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/max-content)
.

### [Position and margin example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size#position_and_margin_example)

See [`anchor-size()` position and margin example](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Using#anchor-size_position_and_margin_example)
.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size#specifications)

---------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Anchor Positioning Module Level 1  <br>\# anchor-size-fn](https://drafts.csswg.org/css-anchor-position-1/#anchor-size-fn) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size#see_also)

---------------------------------------------------------------------------------------------------

*   [`anchor-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-name)
    
*   [`position-anchor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor)
    
*   [`anchor()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor)
     function
*   [Using CSS anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Using)
     guide
*   [CSS anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 18, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/anchor-size/index.md?plain=1 "Folder: en-us/web/css/reference/values/anchor-size (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fanchor-size&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fanchor-size%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fanchor-size%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fanchor-size%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb760560abe30bd69ca968dac38528102f423b5ea%0A*+Document+last+modified%3A+2026-04-18T06%3A09%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")