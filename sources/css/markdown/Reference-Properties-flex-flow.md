*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-flow#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-flow#mdn-search)
    

`flex-flow` CSS property
========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-flow#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`flex-flow`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 property specifies the direction of a flex container, as well as its wrapping behavior.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-flow#try_it)

-------------------------------------------------------------------------------------------------

    flex-flow: row wrap;
    

    flex-flow: row-reverse nowrap;
    

    flex-flow: row wrap balance;
    

    flex-flow: column wrap-reverse;
    

    flex-flow: column wrap;
    

    flex-flow: column balance wrap;
    

    <section class="default-example" id="default-example">
      <div class="transition-all" id="example-element">
        <div>Item One</div>
        <div>Item Two</div>
        <div>Item Three</div>
        <div>Item Four</div>
        <div>Item Five</div>
        <div>Item Six</div>
        <div>Item Seven</div>
      </div>
    </section>
    

    #example-element {
      border: 1px solid #c5c5c5;
      width: 80%;
      max-height: 300px;
      display: flex;
    }
    
    #example-element > div {
      background-color: rgb(0 0 255 / 0.2);
      border: 3px solid blue;
      width: 60px;
      margin: 5px 10px;
    }
    

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-flow#constituent_properties)

---------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [`flex-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction)
    
*   [`flex-wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-wrap)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-flow#syntax)

-------------------------------------------------------------------------------------------------

css

    /* flex-flow: <'flex-direction'> */
    flex-flow: row;
    flex-flow: row-reverse;
    flex-flow: column;
    flex-flow: column-reverse;
    
    /* flex-flow: <'flex-wrap'> */
    flex-flow: nowrap;
    flex-flow: wrap;
    flex-flow: wrap-reverse;
    flex-flow: wrap balance;
    flex-flow: balance wrap-reverse;
    
    /* flex-flow: <'flex-direction'> and <'flex-wrap'> */
    flex-flow: row nowrap;
    flex-flow: column wrap;
    flex-flow: column-reverse wrap-reverse;
    flex-flow: row-reverse balance wrap
    
    /* Global values */
    flex-flow: inherit;
    flex-flow: initial;
    flex-flow: revert;
    flex-flow: revert-layer;
    flex-flow: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-flow#values)

This property is specified as a space-separated list of keywords of the following types:

[`flex-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction)

A keyword specifying the main axis and direction of how flex items are placed in the flex container.

[`flex-wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-wrap)

One or two keywords specifying whether flex items can wrap onto multiple lines, and, if wrapping is allowed, sets the direction that lines are stacked and whether they are balanced.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-flow#description)

-----------------------------------------------------------------------------------------------------------

The `flex-flow` shorthand property specifies the [`flex-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction)
 and [`flex-wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-wrap)
 properties, defining the direction of a flex container and its wrapping behavior. It can also define flex items to be balanced when wrapping is allowed.

For example, `column-reverse wrap` will set the main-axis to the block direction with a reversed main-start and main-end, with flex items being allowed to wrap, creating new lines if needed.

css

    .container {
      flex-flow: column-reverse wrap;
    }
    

To distribute the flex items evenly across each flex line, you can include the `flex-wrap` keyword [`balance`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-wrap#balance)
 in addition to `wrap`:

css

    .container {
      flex-flow: column-reverse wrap balance;
    }
    

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-flow#formal_definition)

-----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | as each of the properties of the shorthand:  <br><br>*   [`flex-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction)<br>    : `row`<br>*   [`flex-wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-wrap)<br>    : `nowrap` |
| Applies to | flex containers |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as each of the properties of the shorthand:  <br><br>*   [`flex-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction)<br>    : as specified<br>*   [`flex-wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-wrap)<br>    : as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | as each of the properties of the shorthand:  <br><br>*   [`flex-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction)<br>    : discrete<br>*   [`flex-wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-wrap)<br>    : discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-flow#formal_syntax)

---------------------------------------------------------------------------------------------------------------

flex-flow =   
  [<'flex-direction'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction)
  [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  [<'flex-wrap'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-wrap)
         
  
[<flex-direction>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction)
 =   
  row             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  row-reverse     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  column          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  column-reverse    
  
[<flex-wrap>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-wrap)
 =   
  nowrap                              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 wrap [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 wrap-reverse [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
 balance    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-flow#examples)

-----------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-flow#basic_usage)

This example demonstrates using the `flex-flow` shorthand on a flex container so the items are laid out backwards across multiple rows.

#### HTML

We include a list of words in alphabetical order:

html

    <ul>
      <li>Alphabet</li>
      <li>Banana</li>
      <li>Crayons</li>
      <li>Dinosaurs</li>
      <li>Eggplant</li>
      <li>Foundation</li>
      <li>Ghosts</li>
      <li>Happy</li>
      <li>Igloo</li>
      <li>Janitors</li>
      <li>Kittens</li>
      <li>Lasso</li>
      <li>Magic 8-ball</li>
      <li>Nincompoop</li>
      <li>Orange</li>
      <li>Petunia</li>
      <li>Quality</li>
      <li>Rancid</li>
      <li>Shoelace</li>
      <li>Terydactyl</li>
      <li>Umbrella</li>
      <li>Valentine</li>
      <li>Westward</li>
      <li>Xylophone</li>
    </ul>
    

#### CSS

We set the [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)
 to be a flex container with the [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 property, define a [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
, add a [`gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/gap)
 so there is some room between flex items and flex lines, and then set the `flex-flow` to wrap the items in reverse order. Additional CSS has been hidden for brevity.

css

    ul {
      display: flex;
      width: 31em;
      gap: 1em;
    
      flex-flow: row-reverse wrap-reverse;
    }
    

    ul {
      list-style: none;
      border: 1px solid;
      font-family: sans-serif;
    }
    li {
      font-size: 1.25rem;
      padding: 5px;
      border: 1px solid;
      background-color: lightpink;
    }
    li:nth-of-type(even) {
      background-color: lightgreen;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-flow#specifications)

-----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Flexible Box Layout Module Level 1  <br>\# flex-flow-property](https://drafts.csswg.org/css-flexbox/#flex-flow-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-flow#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-flow#see_also)

-----------------------------------------------------------------------------------------------------

*   [Basic concepts of flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Basic_concepts)
    
*   [Ordering flex items](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Ordering_items)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-flow/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/flex-flow/index.md?plain=1 "Folder: en-us/web/css/reference/properties/flex-flow (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fflex-flow&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fflex-flow%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fflex-flow%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fflex-flow%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6354422058e438a2599e4eab71eaec8eb40850fa%0A*+Document+last+modified%3A+2026-09-14T09%3A57%3A47.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")