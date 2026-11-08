*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-set#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-set#mdn-search)
    

`counter-set` CSS property
==========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since December 2023.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-set#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`counter-set`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets [CSS counters](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles/Using_counters)
 on the element to the given values.

If the counters don't exist the `counter-set` property creates a new counter for each named counter in the list of space-separated counter and value pairs. However, to create a new counter it is recommended to use the [`counter-reset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-reset)
 CSS property.

If a named counter in the list is missing a value, the value of the counter will be set to `0`.

**Note:** The counter's value can be incremented or decremented using the [`counter-increment`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-increment)
 CSS property.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-set#try_it)

---------------------------------------------------------------------------------------------------

    counter-set: none;
    

    counter-set: chapter-count 0;
    

    counter-set: chapter-count;
    

    counter-set: chapter-count 5;
    

    counter-set: chapter-count -5;
    

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
      counter-set: chapter-count;
    }
    
    #example-element {
      background-color: #37077c;
      color: white;
    }
    
    h2 {
      counter-increment: chapter-count;
      font-size: 1em;
    }
    
    h2::before {
      content: "Chapter " counter(chapter-count) ": ";
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-set#syntax)

---------------------------------------------------------------------------------------------------

css

    /* Set "my-counter" to 0 */
    counter-set: my-counter;
    
    /* Set "my-counter" to -1 */
    counter-set: my-counter -1;
    
    /* Set "counter1" to 1, and "counter2" to 4 */
    counter-set: counter1 1 counter2 4;
    
    /* Cancel any counter that could have been set in less specific rules */
    counter-set: none;
    
    /* Global values */
    counter-set: inherit;
    counter-set: initial;
    counter-set: revert;
    counter-set: revert-layer;
    counter-set: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-set#values)

This property is specified as either a space-separated list of `<custom-ident>` values, each optionally followed by an `<integer>`, or the keyword `none`:

[`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)

The name of the counter to set.

[`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)

The value to set the counter to on each occurrence of the element. Defaults to `0` if not specified. If there isn't currently a counter of the given name on the element, the element will create a new counter of the given name with a starting value of `0` (though it may then immediately set or increment that value to something different).

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-set#none)

No counter set is to be performed. This can be used to override a `counter-set` defined in a less specific rule.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-set#formal_definition)

-------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-set#formal_syntax)

-----------------------------------------------------------------------------------------------------------------

counter-set =   
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

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-set#examples)

-------------------------------------------------------------------------------------------------------

### [Setting named counters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-set#setting_named_counters)

css

    h1 {
      counter-set: chapter section 1 page;
      /* Sets the chapter and page counters to 0,
         and the section counter to 1 */
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-set#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Lists and Counters Module Level 3  <br>\# propdef-counter-set](https://drafts.csswg.org/css-lists/#propdef-counter-set) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-set#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-set#see_also)

-------------------------------------------------------------------------------------------------------

*   [Using CSS Counters](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles/Using_counters)
    
*   [`counter-increment`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-increment)
    
*   [`counter-reset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-reset)
    
*   [`@counter-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style)
    
*   [`counter()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/counter)
     and [`counters()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/counters)
     functions
*   [`content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content)
     property
*   [CSS lists and counters](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Lists)
     module
*   [CSS counter styles](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-set/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/counter-set/index.md?plain=1 "Folder: en-us/web/css/reference/properties/counter-set (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcounter-set&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcounter-set%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcounter-set%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcounter-set%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F737b931225e92e0cba47e57a150878b1a78ee45a%0A*+Document+last+modified%3A+2026-08-24T15%3A52%3A28.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")