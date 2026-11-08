*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-sizing#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-sizing#mdn-search)
    

`box-sizing` CSS property
=========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-sizing#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`box-sizing`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets how the total width and height of an element is calculated.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-sizing#try_it)

--------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-sizing#syntax)

--------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-sizing#values)

This property is specified as one of the following keyword values:

[`content-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-sizing#content-box)

This is the initial and default value as specified by the CSS standard. The [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
 and [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
 properties include the content, but does not include the padding, border, or margin. For example, `.box {width: 350px; border: 10px solid black;}` renders a box that is 370px wide.

Here, the dimensions of the element are calculated as: _width = width of the content_, and _height = height of the content_. (Borders and padding are not included in the calculation.)

[`border-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-sizing#border-box)

The [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
 and [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
 properties include the content, padding, and border, but do not include the margin. Note that padding and border will be inside of the box. For example, `.box {width: 350px; border: 10px solid black;}` renders a box that is 350px wide, with the area for content being 330px wide. The content box can't be negative and is floored to 0, making it impossible to use `border-box` to make the element disappear.

Here the dimensions of the element are calculated as: _width = border + padding + width of the content_, and _height = border + padding + height of the content_.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-sizing#description)

------------------------------------------------------------------------------------------------------------

By default in the [CSS box model](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Introduction)
, the `width` and `height` you assign to an element is applied only to the element's content box. If the element has any border or padding, this is then added to the `width` and `height` to arrive at the size of the box that's rendered on the screen. This means that when you set `width` and `height`, you have to adjust the value you give to allow for any border or padding that may be added. For example, if you have four boxes with `width: 25%;`, if any has left or right padding or a left or right border, they will not by default fit on one line within the constraints of the parent container.

The `box-sizing` property can be used to adjust this behavior:

*   `content-box` gives you the default CSS box-sizing behavior. If you set an element's width to 100 pixels, then the element's content box will be 100 pixels wide, and the width of any border or padding will be added to the final rendered width, making the element wider than 100px.
    
*   `border-box` tells the browser to account for any border and padding in the values you specify for an element's width and height. If you set an element's width to 100 pixels, that 100 pixels will include any border or padding you added, and the content box will shrink to absorb that extra width. This typically makes it much easier to size elements.
    
    `box-sizing: border-box` is the default styling that browsers use for the [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)
    , [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
    , and [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
     elements, and for [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
     elements whose type is `[radio](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/radio) `, `[checkbox](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox) `, `[reset](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/reset) `, `[button](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/button) `, `[submit](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit) `, `[color](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/color) `, or `[search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search) `.
    

**Note:** It is often useful to set `box-sizing` to `border-box` to lay out elements. This makes dealing with the sizes of elements much easier, and generally eliminates a number of pitfalls you can stumble on while laying out your content. On the other hand, when using `position: relative` or `position: absolute`, use of `box-sizing: content-box` allows the positioning values to be relative to the content, and independent of changes to border and padding sizes, which is sometimes desirable.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-sizing#formal_definition)

------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `content-box` |
| Applies to | all elements that accept width or height |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-sizing#formal_syntax)

----------------------------------------------------------------------------------------------------------------

box-sizing =   
  content-box  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  border-box     

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-sizing#examples)

------------------------------------------------------------------------------------------------------

### [Box sizes with content-box and border-box](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-sizing#box_sizes_with_content-box_and_border-box)

This example shows how different `box-sizing` values alter the rendered size of two otherwise identical elements.

#### HTML

#### CSS

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-sizing#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Box Sizing Module Level 3  <br>\# box-sizing](https://drafts.csswg.org/css-sizing/#box-sizing) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-sizing#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-sizing#see_also)

------------------------------------------------------------------------------------------------------

*   [CSS box model](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Introduction)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-sizing/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/box-sizing/index.md?plain=1 "Folder: en-us/web/css/reference/properties/box-sizing (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbox-sizing&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbox-sizing%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbox-sizing%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbox-sizing%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F737b931225e92e0cba47e57a150878b1a78ee45a%0A*+Document+last+modified%3A+2026-08-24T15%3A52%3A28.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")