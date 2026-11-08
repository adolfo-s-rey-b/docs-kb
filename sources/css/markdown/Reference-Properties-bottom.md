*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/bottom#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/bottom#mdn-search)
    

`bottom` CSS property
=====================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/bottom#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`bottom`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property participates in setting the vertical position of a [positioned element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position)
. This [inset property](https://developer.mozilla.org/en-US/docs/Glossary/Inset_properties)
 has no effect on non-positioned elements.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/bottom#try_it)

----------------------------------------------------------------------------------------------

    bottom: 0;
    

    bottom: 4em;
    

    bottom: 10%;
    

    bottom: 20px;
    

    <section id="default-example">
      <div class="example-container">
        <div id="example-element">I am absolutely positioned.</div>
        <p>
          As much mud in the streets as if the waters had but newly retired from the
          face of the earth, and it would not be wonderful to meet a Megalosaurus,
          forty feet long or so, waddling like an elephantine lizard up Holborn
          Hill.
        </p>
      </div>
    </section>
    

    .example-container {
      border: 0.75em solid;
      padding: 0.75em;
      text-align: left;
      position: relative;
      width: 100%;
      min-height: 200px;
    }
    
    #example-element {
      background-color: #264653;
      border: 4px solid #ffb500;
      color: white;
      position: absolute;
      width: 140px;
      height: 60px;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/bottom#syntax)

----------------------------------------------------------------------------------------------

css

    /* <length> values */
    bottom: 3px;
    bottom: 2.4em;
    bottom: calc(anchor(--my-anchor 50%) + 5px);
    bottom: anchor-size(width);
    
    /* <percentage>s of the height of the containing block */
    bottom: 10%;
    
    /* Keyword value */
    bottom: auto;
    
    /* Global values */
    bottom: inherit;
    bottom: initial;
    bottom: revert;
    bottom: revert-layer;
    bottom: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/bottom#values)

[`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)

A negative, null, or positive [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
:

*   for _absolutely positioned elements_, it represents the distance to the bottom edge of the containing block.
*   for _relatively positioned elements_, it represents the distance that the element is moved above its normal position.
*   for _anchor-positioned elements_, the [`anchor()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor)
     function resolves to a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
     value relative to the position of the associated _anchor element_'s top or bottom edge (see [Using inset properties with `anchor()` function values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Using#using_inset_properties_with_anchor_function_values)
    ), and the [`anchor-size()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size)
     function resolves to a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
     value relative to the associated anchor element's width or height (see [Setting element position based on anchor size](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Using#setting_element_position_based_on_anchor_size)
    ).

[`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)

A [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 of the containing block's height.

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/bottom#auto)

Specifies that:

*   for _absolutely positioned elements_, the position of the element is based on the [`top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/top)
     property, while `height: auto` is treated as a height based on the content; or if `top` is also `auto`, the element is positioned where it should vertically be positioned if it were a static element.
*   for _relatively positioned elements_, the distance of the element from its normal position is based on the [`top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/top)
     property; or if `top` is also `auto`, the element is not moved vertically at all.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/bottom#description)

--------------------------------------------------------------------------------------------------------

The effect of `bottom` depends on how the element is positioned (i.e., the value of the [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position)
 property):

*   When `position` is set to `absolute` or `fixed`, the `bottom` property specifies the distance between the outer edge of the element's [bottom margin](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Introduction)
     and the outer edge of the containing block's bottom padding, or, in the case of [anchor positioned elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Using)
     when the [`anchor()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor)
     function is used within the value, relative to the position of the specified [`<anchor-side>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor#anchor-side)
     edge. The `bottom` property is [compatible](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor#compatibility_of_inset_properties_and_anchor-side_values)
     with the `top`, `bottom`, `start`, `end`, `self-start`, `self-end`, `center`, and `<percentage>` values.
*   When `position` is set to `relative`, the `bottom` property specifies the distance the element's bottom edge is moved above its normal position.
*   When `position` is set to `sticky`, the `bottom` property is used to compute the sticky-constraint rectangle.
*   When `position` is set to `static`, the `bottom` property has _no effect_.

When both [`top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/top)
 and `bottom` are specified, `position` is set to `absolute` or `fixed`, _and_ [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
 is unspecified (either `auto` or `100%`) both the `top` and `bottom` distances are respected. In all other situations, if [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
 is constrained in any way or `position` is set to `relative`, the `top` property takes precedence and the `bottom` property is ignored.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/bottom#formal_definition)

--------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | positioned elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| Percentages | refer to the height of the containing block |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | if specified as a length, the corresponding absolute length; if specified as a percentage, the specified value; otherwise, `auto` |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a [length](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#interpolation "Values of the <length> CSS data type are interpolated as real, floating-point numbers.")<br>, [percentage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage#interpolation "Values of the <percentage> CSS data type are interpolated as real, floating-point numbers.")<br> or calc(); |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/bottom#formal_syntax)

------------------------------------------------------------------------------------------------------------

bottom =   
  auto                 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <length-percentage>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <anchor()>           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <anchor-size()>        
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    
  
[<anchor()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor)
 =   
  anchor( <anchor-name>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
                  [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")
  
  <anchor-side> , <length-percentage>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
[<anchor-size()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size)
 =   
  anchor-size( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <anchor-name> [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 <anchor-size> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 , <length-percentage>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
<anchor-name> =   
  [<dashed-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)
    
  
<anchor-side> =   
  inside        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  outside       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  top           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  left          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  right         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  bottom        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  start         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  end           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  self-start    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  self-end      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  center          
  
[<anchor-size>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size)
 =   
  width        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  height       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  block        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  inline       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  self-block   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  self-inline    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/bottom#examples)

--------------------------------------------------------------------------------------------------

### [Absolute and fixed positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/bottom#absolute_and_fixed_positioning)

This example demonstrates the difference in behavior of the `bottom` property, when [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position)
 is `absolute` versus `fixed`.

#### HTML

html

    <p>
      This<br />is<br />some<br />tall,<br />tall,<br />tall,<br />tall,<br />tall<br />content.
    </p>
    <div class="fixed"><p>Fixed</p></div>
    <div class="absolute"><p>Absolute</p></div>
    

#### CSS

css

    p {
      font-size: 30px;
      line-height: 2em;
    }
    
    div {
      width: 48%;
      text-align: center;
      background: rgb(55 55 55 / 20%);
      border: 1px solid blue;
    }
    
    .absolute {
      position: absolute;
      bottom: 0;
      left: 0;
    }
    
    .fixed {
      position: fixed;
      bottom: 0;
      right: 0;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/bottom#specifications)

--------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Positioned Layout Module Level 3  <br>\# insets](https://drafts.csswg.org/css-position/#insets) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/bottom#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/bottom#see_also)

--------------------------------------------------------------------------------------------------

*   [`top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/top)
    , [`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/left)
    , and [`right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/right)
    
*   [`inset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset)
     shorthand
*   [`inset-block-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-block-start)
    , [`inset-block-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-block-end)
    , [`inset-inline-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-inline-start)
    , and [`inset-inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-inline-end)
    
*   [`inset-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-block)
     and [`inset-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-inline)
     shorthands
*   [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position)
    
*   [CSS positioned layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/bottom/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/bottom/index.md?plain=1 "Folder: en-us/web/css/reference/properties/bottom (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbottom&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbottom%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbottom%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbottom%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")