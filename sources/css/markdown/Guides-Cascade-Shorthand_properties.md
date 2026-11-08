*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties#mdn-search)
    

Shorthand properties
====================

**_Shorthand properties_** are CSS properties that let you set the values of multiple other CSS properties in one declaration. Using a shorthand property, you can write more concise (and often more readable) style sheets, saving time and energy.

The CSS specification defines shorthand properties to group the definition of common properties acting on the same theme. For example, the CSS [`background`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background)
 property is a shorthand property that's able to define the values of [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
, [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
, [`background-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat)
, and [`background-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position)
.

[Tricky edge cases](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties#tricky_edge_cases)

----------------------------------------------------------------------------------------------------------------------------

There are a few edge cases to keep in mind when using shorthand properties.

### [Omitting properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties#omitting_properties)

A value which is not specified is set to a default value defined by the shorthand, which may differ from the property's initial value.

That means that it **overrides** previously set values. For example:

This will not set the color of the background to `red` but to the default value for [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
, which is `transparent`.

Only the individual properties values can inherit. As missing values are replaced by their initial value, it is impossible to allow inheritance of individual properties by omitting them. The keyword `inherit` can be applied to a property, but only as a whole, not as a keyword for one value or another. That means that the only way to make some specific value to be inherited is to use the longhand property with the keyword `inherit`.

### [Ordering properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties#ordering_properties)

Shorthand properties try not to force a specific order for the values of the properties they replace. This works well when these properties use values of different types, as the order has no importance, but this does not work as easily when several properties can have identical values.

Two important cases here are:

*   Properties related to the sides of the box, like [`border-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style)
    , [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
     or [`padding`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding)
    
*   Properties related to the corners of the box, like [`border-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
    

#### Sides of the box

Shorthands handling properties related to the sides of the box, like [`border-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style)
, [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
 or [`padding`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding)
, always use a consistent 1-to-4-value syntax representing those sides:

*   **1-value syntax:** `border-width: 1em` — A single value represents all sides: ![Box edges with one-value syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties/border1.png)
    
*   **2-value syntax:** `border-width: 1em 2em` — The first value represents the top and bottom sides, and the second value represents the left and right sides: ![Box edges with two-value syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties/border2.png)
    
*   **3-value syntax:** `border-width: 1em 2em 3em` — The first value represents the top side, the second value represents the left and right sides, and the third value represents the bottom side: ![Box edges with three-value syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties/border3.png)
    
*   **4-value syntax:** `border-width: 1em 2em 3em 4em` — The four values represent the top, the right, the bottom, and the left sides, respectively, always in that order; that is, clock-wise starting at the top: ![Box edges with four-value syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties/border4.png) The initial letter of Top-Right-Bottom-Left matches the order of the consonant of the word _trouble_: TRBL. You can also remember it as the order that the hands would rotate on a clock: `1em` starts in the 12 o'clock position, then `2em` in the 3 o'clock position, then `3em` in the 6 o'clock position, and `4em` in the 9 o'clock position.
    

#### Corners of the box

Similarly, shorthands handling properties related to the corners of the box, like [`border-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
, always use a consistent 1-to-4-value syntax representing those corners:

*   **1-value syntax:** `border-radius: 1em` — A single value represents all corners: ![Box corners with one-value syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties/corner1.png)
    
*   **2-value syntax:** `border-radius: 1em 2em` — The first value represents the top-left and bottom-right corners, and the second value represents the top-right and bottom-left corners: ![Box corners with two-value syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties/corner2.png)
    
*   **3-value syntax:** `border-radius: 1em 2em 3em` — The first value represents the top-left corner, the second value represents the top-right and bottom-left corners, and the third value represents the bottom-right corner: ![Box corners with three-value syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties/corner3.png)
    
*   **4-value syntax:** `border-radius: 1em 2em 3em 4em` — The four values represent the top-left, top-right, bottom-right, and bottom-left corners respectively, always in that order; that is, clock-wise starting at the top-left: ![Box corners with four-value syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties/corner4.png)
    

[Background properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties#background_properties)

------------------------------------------------------------------------------------------------------------------------------------

Consider a background with the following properties

These four declarations can be shortened to just one:

(The shorthand form is actually the equivalent of the longhand properties above plus `background-attachment: scroll` and, in CSS3, some additional properties.)

See [`background`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background)
 for more detailed information, including CSS3 properties.

[Font properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties#font_properties)

------------------------------------------------------------------------------------------------------------------------

Consider the following declarations:

These 5 statements can be shortened to the following:

This shorthand declaration is actually equivalent to the longhand declarations above plus `font-variant: normal`, `font-size-adjust: none`, and `font-stretch: normal`.

[Border properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties#border_properties)

----------------------------------------------------------------------------------------------------------------------------

With borders, the width, color, and style can be simplified into one declaration. For example, consider the following CSS:

It can be simplified as:

[Margin and padding properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties#margin_and_padding_properties)

----------------------------------------------------------------------------------------------------------------------------------------------------

Shorthand versions of margin and padding values work similarly; the margin property allows for shorthand values to be specified using one, two, three, or four values. Consider the following CSS declarations:

They are the same as the following declaration using the four value shorthand. Note that the values are in clockwise order, beginning at the top: top, right, bottom, then left (TRBL, the consonants in "trouble").

Margin shorthand rules for one, two, three and four value declarations are:

*   When **one** value is specified, it applies the same margin to **all four sides**.
*   When **two** values are specified, the first margin applies to the **top and bottom**, the second to the **left and right**.
*   When **three** values are specified, the first margin applies to the **top**, the second to the **left and right**, the third to the **bottom**.
*   When **four** values are specified, the margins apply to the **top**, **right**, **bottom**, and **left** in that order (clockwise).

[Position properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties#position_properties)

--------------------------------------------------------------------------------------------------------------------------------

With position, the shorthand versions of top, right, bottom and left can be simplified into one declaration. For example, consider the following CSS:

It can be simplified as:

Just like margins and paddings, the inset values are ordered clockwise - top, right, bottom, then left (TRBL).

[The universal shorthand property](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties#the_universal_shorthand_property)

----------------------------------------------------------------------------------------------------------------------------------------------------------

CSS provides a universal shorthand property, [`all`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/all)
, which applies its value to every property in the document. Its purpose is to change the properties' inheritance model.

See [Handling conflicts](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Handling_conflicts)
 or [Introducing the CSS Cascade](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Introduction)
 for more information about how inheritance works in CSS.

[Shorthand properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties#shorthand_properties)

----------------------------------------------------------------------------------------------------------------------------------

*   [`all`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/all)
    
*   [`animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
    
*   [`animation-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range)
    
*   [`background`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background)
    
*   [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
    
*   [`border-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block)
    
*   [`border-block-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-end)
    
*   [`border-block-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-start)
    
*   [`border-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom)
    
*   [`border-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-color)
    
*   [`border-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image)
    
*   [`border-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline)
    
*   [`border-inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-end)
    
*   [`border-inline-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-start)
    
*   [`border-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-left)
    
*   [`border-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
    
*   [`border-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-right)
    
*   [`border-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style)
    
*   [`border-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top)
    
*   [`border-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-width)
    
*   [`column-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule)
    
*   [`columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/columns)
    
*   [`contain-intrinsic-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-size)
    
*   [`container`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container)
    
*   [`flex`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex)
    
*   [`flex-flow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-flow)
    
*   [`font`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font)
    
*   [`font-synthesis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis)
    
*   [`font-variant`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant)
    
*   [`gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/gap)
    
*   [`grid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid)
    
*   [`grid-area`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-area)
    
*   [`grid-column`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-column)
    
*   [`grid-row`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row)
    
*   [`grid-template`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template)
    
*   [`inset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset)
    
*   [`inset-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-block)
    
*   [`inset-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-inline)
    
*   [`list-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style)
    
*   [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
    
*   [`margin-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-block)
    
*   [`margin-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline)
    
*   [`mask`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask)
    
*   [`mask-border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border)
    
*   [`offset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset)
    
*   [`outline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline)
    
*   [`overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow)
    
*   [`overscroll-behavior`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior)
    
*   [`padding`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding)
    
*   [`padding-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-block)
    
*   [`padding-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-inline)
    
*   [`place-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-content)
    
*   [`place-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-items)
    
*   [`place-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-self)
    
*   [`position-try`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try)
    
*   [`scroll-margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin)
    
*   [`scroll-margin-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-block)
    
*   [`scroll-margin-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-inline)
    
*   [`scroll-padding`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding)
    
*   [`scroll-padding-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-block)
    
*   [`scroll-padding-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-inline)
    
*   [`scroll-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline)
    
*   [`text-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box)
    
*   [`text-decoration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration)
    
*   [`text-emphasis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis)
    
*   [`text-wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap)
    
*   [`transition`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition)
    
*   [`view-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline)
    
*   [`-webkit-text-stroke`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-text-stroke)
    
*   [`-webkit-border-before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-border-before)
    
*   [`-webkit-mask-box-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-box-image)
    

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties#see_also)

----------------------------------------------------------------------------------------------------------

*   [CSS cascading and inheritance](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade)
     module
*   [Introduction to CSS syntax: declarations, rulesets, and statements](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Introduction)
    
*   [At-rules](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/At-rules)
    
*   [Specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Specificity)
    
*   [Inheritance](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance)
    
*   [Introduction to the CSS cascade](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Introduction)
    
*   [Learn: Handling conflicts](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Handling_conflicts)
    
*   [Learn: Cascade layers](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Cascade_layers)
    
*   [Visual formatting models](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Visual_formatting_model)
    
*   Values: [initial](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value)
    , [computed](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value)
    , [used](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#used_value)
    , and [actual](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#actual_value)
    
*   [Value definition syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on May 25, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/cascade/shorthand_properties/index.md?plain=1 "Folder: en-us/web/css/guides/cascade/shorthand_properties (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FCascade%2FShorthand_properties&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fcascade%2Fshorthand_properties%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FCascade%2FShorthand_properties%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fcascade%2Fshorthand_properties%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9dad06197b9a4c09d7c1e03b5aac47458a30cb2e%0A*+Document+last+modified%3A+2026-05-25T01%3A16%3A17.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")