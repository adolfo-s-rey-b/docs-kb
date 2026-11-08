*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-left#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-left#mdn-search)
    

`margin-left` CSS property
==========================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-left#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`margin-left`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the [margin area](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Introduction#margin_area)
 on the left side of an element. A positive value places it farther from its neighbors, while a negative value places it closer.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-left#try_it)

---------------------------------------------------------------------------------------------------

    margin-left: 1em;
    

    margin-left: 10%;
    

    margin-left: 10px;
    

    margin-left: 0;
    

    <section id="default-example">
      <div id="container">
        <div class="col"></div>
        <div class="col transition-all" id="example-element"></div>
        <div class="col"></div>
      </div>
    </section>
    

    #container {
      width: 300px;
      height: 200px;
      display: flex;
      align-content: flex-start;
      justify-content: flex-start;
    }
    
    .col {
      width: 33.33%;
      border: solid #5b6dcd 10px;
      background-color: rgb(229 232 252 / 0.6);
      flex-shrink: 0;
    }
    
    #example-element {
      border: solid 10px #ffc129;
      background-color: rgb(255 244 219 / 0.6);
    }
    

The vertical margins of two adjacent boxes may fuse. This is called [_margin collapsing_](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Margin_collapsing)
.

In the rare cases where width is overconstrained (i.e., when all of `width`, `margin-left`, `border`, `padding`, the content area, and `margin-right` are defined), `margin-left` is ignored, and will have the same calculated value as if the `auto` value was specified.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-left#syntax)

---------------------------------------------------------------------------------------------------

css

    /* <length> values */
    margin-left: 10px; /* An absolute length */
    margin-left: 1em; /* relative to the text size */
    margin-left: 5%; /* relative to the nearest block container's width */
    margin-left: anchor-size(self-inline);
    margin-left: calc(anchor-size(--my-anchor width, 20px) / 4);
    
    /* Keyword value */
    margin-left: auto;
    
    /* Global values */
    margin-left: inherit;
    margin-left: initial;
    margin-left: revert;
    margin-left: revert-layer;
    margin-left: unset;
    

The `margin-left` property is specified as the keyword `auto`, or a `<length>`, or a `<percentage>`. Its value can be positive, zero, or negative.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-left#values)

[`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)

The size of the margin as a fixed value.

*   For _anchor-positioned elements_, the [`anchor-size()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size)
     function resolves to a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
     value relative to the associated _anchor element_'s width or height (see [Setting element margin based on anchor size](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Using#setting_element_margin_based_on_anchor_size)
    ).

[`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)

The size of the margin as a percentage, relative to the inline size (_width_ in a horizontal language, defined by [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
) of the [containing block](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block)
.

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-left#auto)

The left margin receives a share of the unused horizontal space, as determined mainly by the layout mode that is used. If the values of `margin-left` and `margin-right` are both `auto`, the calculated space is evenly distributed. This table summarizes the different cases:

| Value of [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display) | Value of [`float`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/float) | Value of [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position) | Computed value of `auto` | Comment |
| --- | --- | --- | --- | --- |
| `inline`, `inline-block`, `inline-table` | _any_ | `static` or `relative` | `0` | Inline layout mode |
| `block`, `inline`, `inline-block`, `block`, `table`, `inline-table`, `list-item`, `table-caption` | _any_ | `static` or `relative` | `0`, except if both `margin-left` and `margin-right` are set to `auto`. In this case, it is set to the value centering the element inside its parent. | Block layout mode |
| `block`, `inline`, `inline-block`, `block`, `table`, `inline-table`, `list-item`, `table-caption` | `left` or `right` | `static` or `relative` | `0` | Block layout mode (floating element) |
| _any_ `table-*`_, except_ `table-caption` | _any_ | _any_ | `0` | Internal `table-*` elements don't have margins, use [`border-spacing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-spacing)<br> instead |
| _any, except `flex`,_ `inline-flex`_, or_ `table-*` | _any_ | _`fixed`_ or `absolute` | `0`, except if both `margin-left` and `margin-right` are set to `auto`. In this case, it is set to the value centering the border area inside the available `width`, if fixed. | Absolutely positioned layout mode |
| `flex`, `inline-flex` | _any_ | _any_ | `0`, except if there is any positive horizontal free space. In this case, it is evenly distributed to all horizontal `auto` margins. | Flexbox layout mode |

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-left#formal_definition)

-------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `0` |
| Applies to | all elements, except elements with table [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)<br> types other than `table-caption`, `table` and `inline-table`. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| Percentages | refer to the width of the containing block |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | the percentage as specified or the absolute length |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a [length](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#interpolation "Values of the <length> CSS data type are interpolated as real, floating-point numbers.") |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-left#formal_syntax)

-----------------------------------------------------------------------------------------------------------------

margin-left =   
  <length-percentage>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  auto                 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <anchor-size()>        
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    
  
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
    
  
[<anchor-size>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size)
 =   
  width        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  height       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  block        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  inline       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  self-block   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  self-inline    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-left#examples)

-------------------------------------------------------------------------------------------------------

### [Setting margin-left as a percentage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-left#setting_margin-left_as_a_percentage)

Percentage values for `margin-left` are relative to the container's inline size.

#### HTML

html

    <p>
      A large rose-tree stood near the entrance of the garden: the roses growing on
      it were white, but there were three gardeners at it, busily painting them red.
    </p>
    <p class="example">
      Alice thought this a very curious thing, and she went nearer to watch them,
      and just as she came up to them she heard one of them say, "Look out now,
      Five! Don't go splashing paint over me like that!"
    </p>
    <p>
      "I couldn't help it," said Five, in a sulky tone; "Seven jogged my elbow."
    </p>
    

#### CSS

css

    .example {
      margin-left: 50%;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-left#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Box Model Module Level 3  <br>\# margin-physical](https://drafts.csswg.org/css-box/#margin-physical) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-left#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-left#see_also)

-------------------------------------------------------------------------------------------------------

*   [`margin-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-top)
    , [`margin-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-right)
    , and [`margin-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-bottom)
    
*   [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
     shorthand
*   [`margin-block-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-block-start)
    , [`margin-block-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-block-end)
    , [`margin-inline-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline-start)
    , and [`margin-inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline-end)
    
*   [`margin-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-block)
     and [`margin-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline)
     shorthands
*   [CSS box model](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 16, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-left/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/margin-left/index.md?plain=1 "Folder: en-us/web/css/reference/properties/margin-left (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fmargin-left&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fmargin-left%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fmargin-left%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fmargin-left%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F880c2c4b113c6fe127ca3ae3603a56ef7a2eb9a6%0A*+Document+last+modified%3A+2026-09-16T20%3A20%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")