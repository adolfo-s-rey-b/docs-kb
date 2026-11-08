*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-basis#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-basis#mdn-search)
    

`flex-basis` CSS property
=========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-basis#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`flex-basis`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the initial main size of a [flex item](https://developer.mozilla.org/en-US/docs/Glossary/Flex_Item)
. It sets the size of the content box unless otherwise set with [`box-sizing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-sizing)
.

**Note:** It is recommended to use the [`flex`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex)
 shorthand with a keyword value like `auto` or `initial` instead of setting `flex-basis` on its own. The [keyword values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex#values)
 expand to reliable combinations of [`flex-grow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-grow)
, [`flex-shrink`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-shrink)
, and `flex-basis`, which help to achieve the commonly desired flex behaviors.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-basis#try_it)

--------------------------------------------------------------------------------------------------

    flex-basis: auto;
    

    flex-basis: 0;
    

    flex-basis: 200px;
    

    <section class="default-example" id="default-example">
      <div class="transition-all" id="example-element">Item One</div>
      <div>Item Two</div>
      <div>Item Three</div>
    </section>
    

    .default-example {
      border: 1px solid #c5c5c5;
      width: auto;
      max-height: 300px;
      display: flex;
    }
    
    .default-example > div {
      background-color: rgb(0 0 255 / 0.2);
      border: 3px solid blue;
      margin: 10px;
      flex-grow: 1;
      flex-shrink: 1;
      flex-basis: auto;
    }
    

In this example, the [`flex-grow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-grow)
 and [`flex-shrink`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-shrink)
 properties are both set to `1` on all three items, indicating that the flex item can grow and shrink from the initial `flex-basis`.

The demo changes the `flex-basis` value set on the first flex item, causing it to grow or shrink to fill the available space. The other flex items will also change size; they will be at least `min-content`\-sized. For example, when the `flex-basis` of the first item is set to `200px`, it will start at `200px` but then shrink to fit the space available.

If `flex-basis` is set to a value other than `auto` and there is a `width` (or `height` in case of `flex-direction: column`) set for that same flex item, the `flex-basis` value takes precedence.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-basis#syntax)

--------------------------------------------------------------------------------------------------

css

    /* Specify <'width'> */
    flex-basis: 10em;
    flex-basis: 3px;
    flex-basis: 50%;
    flex-basis: auto;
    
    /* Intrinsic sizing keywords */
    flex-basis: max-content;
    flex-basis: min-content;
    flex-basis: fit-content;
    
    /* Automatically size based on the flex item's content */
    flex-basis: content;
    
    /* Global values */
    flex-basis: inherit;
    flex-basis: initial;
    flex-basis: revert;
    flex-basis: revert-layer;
    flex-basis: unset;
    

The `flex-basis` property is specified as either the keyword `content` or a `<'width'>`.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-basis#values)

[`content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-basis#content)

Indicates automatic sizing, based on the flex item's content.

[`<'width'>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-basis#width)

Any of the following units:

*   [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
     sets an absolute value.
*   [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
     sets a percentage of the width or height of the containing block's content area. Percentage values of `flex-basis` are resolved against the flex container. If the flex container's size is indefinite, the used value for `flex-basis` is `content`.
*   `auto` uses the value of the [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
     in horizontal writing mode, and the value of the [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
     in vertical writing mode; when the corresponding value is also `auto`, the `content` value is used instead.
*   [`max-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/max-content)
     sets the intrinsic preferred width.
*   [`min-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/min-content)
     sets the intrinsic minimum width.
*   [`fit-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content)
     sets the maximum possible size of a containing block's content area, bounded by the `min-content` and `max-content` values, and calculated based on the content of the current element.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-basis#formal_definition)

------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | flex items, including in-flow pseudo-elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| Percentages | refer to the flex container's inner main size |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified, but with relative lengths converted into absolute lengths |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a [length](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#interpolation "Values of the <length> CSS data type are interpolated as real, floating-point numbers.")<br>, [percentage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage#interpolation "Values of the <percentage> CSS data type are interpolated as real, floating-point numbers.")<br> or calc(); |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-basis#formal_syntax)

----------------------------------------------------------------------------------------------------------------

flex-basis =   
  content    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<'width'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
    
  
[<width>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
 =   
  auto             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <box-size>       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <anchor-size()>    
  
<box-size> =   
  <length-percentage \[0,∞\]>                 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  stretch                                   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  contain                                   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  min-content                               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  max-content                               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  fit-content                               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  stretch( <length-percentage \[0,∞\]> )      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  fit-content( <length-percentage \[0,∞\]> )  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <calc-size()>                               
  
[<anchor-size()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size)
 =   
  anchor-size( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <anchor-name> [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 <anchor-size> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 , <length-percentage>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    
  
[<calc-size()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-size)
 =   
  calc-size( <calc-size-basis> , <calc-sum> )    
  
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
  
<calc-size-basis> =   
  <size-keyword>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <calc-sum>      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <calc-size()>   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  any               
  
[<calc-sum>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-sum)
 =   
  <calc-product> [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 '+' [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 '-' [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <calc-product> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[\*](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#asterisk "Asterisk: the entity may occur zero, one or several times")
    
  
<calc-product> =   
  <calc-value> [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 '\*' [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 / [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <calc-value> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[\*](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#asterisk "Asterisk: the entity may occur zero, one or several times")
    
  
<calc-value> =   
  [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<dimension>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dimension)
     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <calc-keyword>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ( <calc-sum> )    
  
[<calc-keyword>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-keyword)
 =   
  e          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  pi         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  infinity   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  \-infinity  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  NaN          

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-basis#examples)

------------------------------------------------------------------------------------------------------

### [Setting flex item initial sizes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-basis#setting_flex_item_initial_sizes)

#### HTML

html

    <ul class="container">
      <li class="flex flex1">1: flex-basis test</li>
      <li class="flex flex2">2: flex-basis test</li>
      <li class="flex flex3">3: flex-basis test</li>
      <li class="flex flex4">4: flex-basis test</li>
      <li class="flex flex5">5: flex-basis test</li>
    </ul>
    
    <ul class="container">
      <li class="flex flex6">6: flex-basis test</li>
    </ul>
    

#### CSS

css

    .container {
      font-family: "Arial", sans-serif;
      margin: 0;
      padding: 0;
      list-style-type: none;
      display: flex;
      flex-wrap: wrap;
    }
    
    .flex {
      background: #6ab6d8;
      padding: 10px;
      margin-bottom: 50px;
      border: 3px solid #2e86bb;
      color: white;
      font-size: 14px;
      text-align: center;
      position: relative;
    }
    
    .flex::after {
      position: absolute;
      z-index: 1;
      left: 0;
      top: 100%;
      margin-top: 10px;
      width: 100%;
      color: #333333;
      font-size: 12px;
    }
    
    .flex1 {
      flex-basis: auto;
    }
    
    .flex1::after {
      content: "auto";
    }
    
    .flex2 {
      flex-basis: max-content;
    }
    
    .flex2::after {
      content: "max-content";
    }
    
    .flex3 {
      flex-basis: min-content;
    }
    
    .flex3::after {
      content: "min-content";
    }
    
    .flex4 {
      flex-basis: fit-content;
    }
    
    .flex4::after {
      content: "fit-content";
    }
    
    .flex5 {
      flex-basis: content;
    }
    
    .flex5::after {
      content: "content";
    }
    

#### Results

### [Flex basis `0` vs `0%`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-basis#flex_basis_0_vs_0)

This example demonstrates the difference between a `flex-basis` of `0` versus a `flex-basis` of `0%` when `flex-direction` is set to `column` and the flex containers and flex items don't have a set height; while `0` is an absolute length, percentage flex-basis values resolve to [`content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-basis#content)
 values.

#### HTML

We include two same-structure flex containers, which will be styled similarly except for their `flex-basis` values. The containers each have two children: a heading `<div>` and a `<section>`. The `<section>` element has a content `<div>` child, which will not be set as a flex item but will be given a height.

html

    <div class="container basis-0">
      <div>heading</div>
      <section>
        <div class="content">flex-basis: 0;</div>
      </section>
    </div>
    <div class="container basis-0-percent">
      <div>heading</div>
      <section>
        <div class="content">flex-basis: 0%;</div>
      </section>
    </div>
    

#### CSS

We style the containers as inline flex containers that will appear side by side to better enable comparing them. We set the `flex-direction` to `column`. The first container's flex items have a `flex-basis` value of `0`, while the second container's flex items have a `flex-basis` value of `0%`. Neither the flex containers nor their flex items have a height explicitly set; however, the heights of `section` elements must be at least `200px`, and their children have a height of `300px`.

css

    .container {
      width: 40vw;
      padding: 1rem;
      border: 1px dashed blue;
    
      display: inline-flex;
      flex-direction: column;
    }
    
    section {
      outline: 1px solid red;
    
      overflow: auto;
      min-height: 200px;
    }
    
    .content {
      background: wheat;
      height: 300px;
    }
    
    .container.basis-0 > * {
      flex-basis: 0;
    }
    .container.basis-0-percent > * {
      flex-basis: 0%;
    }
    

#### Results

In the first container, with `flex-basis: 0`, the `<section>` element has an initial main size of zero, and it grows to the `200px` minimum height. In the second container, with `flex-basis: 0%`, the `<section>` element has an initial main size of `300px` because, as the flex container doesn't have a set height, the percentage flex-basis values resolve to the [`content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-basis#content)
 value.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-basis#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Flexible Box Layout Module Level 1  <br>\# flex-basis-property](https://drafts.csswg.org/css-flexbox/#flex-basis-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-basis#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-basis#see_also)

------------------------------------------------------------------------------------------------------

*   [`flex`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex)
     shorthand
*   [`inline-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inline-size)
    
*   [Basic concepts of flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Basic_concepts)
    
*   [Controlling ratios of flex items along the main axis](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Controlling_flex_item_ratios)
    
*   [CSS flexible box layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-basis/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/flex-basis/index.md?plain=1 "Folder: en-us/web/css/reference/properties/flex-basis (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fflex-basis&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fflex-basis%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fflex-basis%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fflex-basis%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")