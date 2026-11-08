*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-increment#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-increment#mdn-search)
    

`counter-increment` CSS property
================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-increment#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`counter-increment`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property can be used to increase or decrease the value of the named [CSS counters](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles/Using_counters)
 by the specified values, or to prevent all counters or an individual counter's value from being changed.

If a named counter in the list of space-separated counters and values doesn't exist, it will be created. If no value is provided for a counter in the list of counters, the counter will be increased by `1`.

The counter's value can be reset to any integer value with the [`counter-reset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-reset)
 CSS property.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-increment#try_it)

---------------------------------------------------------------------------------------------------------

    counter-increment: chapter-count;
    

    counter-increment: chapter-count 0;
    

    counter-increment: chapter-count 5;
    

    counter-increment: chapter-count -5;
    

    <section class="default-example" id="default-example">
      <div class="transition-all" id="chapters">
        <h1>Alice's Adventures in Wonderland</h1>
        <h2>Down the Rabbit-Hole</h2>
        <h2 id="example-element">The Pool of Tears</h2>
        <h2>A Caucus-Race and a Long Tale</h2>
        <h2>The Rabbit Sends in a Little Bill</h2>
      </div>
    </section>
    

    #default-example {
      text-align: left;
      counter-reset: chapter-count;
    }
    
    #example-element {
      background-color: lightblue;
      color: black;
    }
    
    h2 {
      counter-increment: chapter-count;
      font-size: 1em;
    }
    
    h2::before {
      content: "Chapter " counter(chapter-count) ": ";
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-increment#syntax)

---------------------------------------------------------------------------------------------------------

css

    /* Increases "my-counter" by 1 */
    counter-increment: my-counter;
    
    /* Decreases "my-counter" by 1 */
    counter-increment: my-counter -1;
    
    /* Increases "counter1" by 1 and decreases "counter2" by 4 */
    counter-increment: counter1 counter2 -4;
    
    /* Increases "page" by 1, "section" by 2, while "chapter" doesn't change */
    counter-increment: chapter 0 section 2 page;
    
    /* Do not increment/decrement anything: used to override less specific rules */
    counter-increment: none;
    
    /* Global values */
    counter-increment: inherit;
    counter-increment: initial;
    counter-increment: revert;
    counter-increment: revert-layer;
    counter-increment: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-increment#values)

This property is specified as a space-separated list of `<custom-ident>` values, each optionally followed by an `<integer>`, or the keyword `none`:

[`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)

Specifies the name of the counter to increase or decrease.

[`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)

Specifies the value to add to the counter. If the integer is preceded by a `-` sign, the value will be subtracted from the counter. Defaults to `1` if no value is specified.

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-increment#none)

Indicates that no counter must be increased or decreased. This value can also be used to cancel all counters from being increased or decreased in more specific rules. This is the default value of the property.

**Note:** Using the `none` value prevents all counters from being increased or decreased for the selected elements where this rule applies. To prevent only specific counters from being increased or decreased, set the `integer` value as `0` on the relevant counter(s).

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-increment#formal_definition)

-------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-increment#formal_syntax)

-----------------------------------------------------------------------------------------------------------------------

counter-increment =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <counter-name> <integer>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[+](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#plus "Plus: the entity may occur one or several times")
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  none                              
  
<counter-name> =   
  [<custom-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
    
  
[<integer>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 =   
  <number-token>    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-increment#examples)

-------------------------------------------------------------------------------------------------------------

### [Decreasing the counter value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-increment#decreasing_the_counter_value)

In this example, we display a sequence of numbers counting backward. To do this, we use a counter to display numbers starting from 100 and decreasing by 7 each time.

#### HTML

html

    <div>
      <i></i><i></i><i></i><i></i><i></i><i></i><i></i> <i></i><i></i><i></i><i></i
      ><i></i><i></i><i></i> <i></i><i></i><i></i><i></i><i></i><i></i><i></i>
      <i></i><i></i><i></i><i></i><i></i><i></i><i></i>
    </div>
    

#### CSS

We set the initial value of the counter named `sevens` to `100` by using [`counter-reset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-reset)
. Then, for each [`<i>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/i)
, we decrease the counter by `7`.

To set the first count at `100`, we target the first `<i>` element by using the [`:first-of-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first-of-type)
 pseudo-class and setting `counter-increment: none;`. Additionally, the [`content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content)
 property is used in the [`::before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::before)
 pseudo-element to display the value of the counter using the [`counter()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/counter)
 function.

css

    div {
      counter-reset: sevens 100;
    }
    i {
      counter-increment: sevens -7;
    }
    i:first-of-type {
      counter-increment: none;
    }
    i::before {
      content: counter(sevens);
    }
    

    div {
      display: flex;
      flex-direction: column;
      flex-wrap: wrap;
      height: 300px;
      width: 200px;
    }
    i {
      flex: 0 0 2em;
    }
    

#### Result

Had we not used `counter-reset` (or [`counter-set`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-set)
) to create the counter and set the value to `100`, the `sevens` counter would still have been created, but with an initial value `0`.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-increment#specifications)

-------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Lists and Counters Module Level 3  <br>\# increment-set](https://drafts.csswg.org/css-lists/#increment-set) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-increment#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-increment#see_also)

-------------------------------------------------------------------------------------------------------------

*   Counter properties: [`counter-set`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-set)
    , [`counter-reset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-reset)
    
*   Counter at-rule: [`@counter-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style)
    
*   Counter functions: [`counter()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/counter)
    , [`counters()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/counters)
    
*   [Using CSS counters](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles/Using_counters)
     guide
*   [CSS lists and counters](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Lists)
     module
*   [CSS counter styles](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-increment/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/counter-increment/index.md?plain=1 "Folder: en-us/web/css/reference/properties/counter-increment (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcounter-increment&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcounter-increment%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcounter-increment%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcounter-increment%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffd30a91f7c0f5bc65445dd931ec9754806bbd5fb%0A*+Document+last+modified%3A+2026-08-27T17%3A13%3A11.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")