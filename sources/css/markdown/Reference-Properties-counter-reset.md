*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-reset#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-reset#mdn-search)
    

`counter-reset` CSS property
============================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-reset#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`counter-reset`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property creates named [CSS counters](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles/Using_counters)
 and initializes their values. It can create both regular and reversed counters.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-reset#try_it)

-----------------------------------------------------------------------------------------------------

    counter-reset: none;
    

    counter-reset: chapter-count 0;
    

    counter-reset: chapter-count;
    

    counter-reset: chapter-count 5;
    

    counter-reset: chapter-count -5;
    

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
      content: "Chapter " counters(chapter-count, ".") ": ";
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-reset#syntax)

-----------------------------------------------------------------------------------------------------

css

    /* Keyword value */
    counter-reset: none;
    
    /* Regular counters with default initial values */
    counter-reset: my-counter;
    counter-reset: another-counter;
    
    /* Regular counters with an initial value */
    counter-reset: my-counter -3;
    counter-reset: another-counter 15;
    
    /* Reversed counters */
    counter-reset: reversed(my-counter);
    counter-reset: reversed(my-counter) 3;
    counter-reset: reversed(another-counter) 15;
    
    /* Multiple counters */
    counter-reset: my-counter -3 another-counter 15;
    counter-reset: reversed(pages) items 1 reversed(sections) 4;
    
    /* Global values */
    counter-reset: inherit;
    counter-reset: initial;
    counter-reset: revert;
    counter-reset: revert-layer;
    counter-reset: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-reset#values)

This property is specified as a space-separated list of counter or reversed counter names, each optionally followed by an `<integer>`, or the keyword `none`:

[`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)

Specifies the counter name to create and initialize. The `reversed()` functional notation can be used to create a reversed counter.

[`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)

Specifies the initial value to set on the newly created counter. If not specified, defaults to `0` for regular counters. The initial value for reversed counters is calculated automatically.

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-reset#none)

Specifies that no counters are created.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-reset#description)

---------------------------------------------------------------------------------------------------------------

The `counter-reset` property can be used to create and initialize named [counters](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles/Using_counters)
 or reversed counters to number elements in ascending or descending order.

The `none` value can be used to override a `counter-reset` declaration in a rule with lower specificity.

**Warning:** There is [a difference between `counter-reset` and `counter-set` properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles/Using_counters#difference_between_counter-set_and_counter-reset)
. After creating a counter using `counter-reset`, you can adjust its value by using the [`counter-set`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-set)
 property. This is counterintuitive because, despite its name, the `counter-reset` property creates and initializes counters, while the `counter-set` property resets the value of existing counters.

Separate multiple counter names or name-value pairs with spaces. For counter names, regular counters use the format `<counter-name>` and reversed counters use the format `reversed(<counter-name>)`, where `<counter-name>` is a [`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
 or `list-item` for the built-in [`<ol>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol)
 counter.

### [Default initial values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-reset#default_initial_values)

Declaring regular and reversed counters without including an integer enables you to implement the two most common numbering patterns: counting up from `1` to the number of elements and counting down from the number of elements to `1`, with increments or decrements of `1`. By specifying an initial value for a named counter, you can change its starting value. The increment or decrement can be adjusted by using the [`counter-increment`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-increment)
 property.

The following example creates three counters. The `chapter` and `page` counters are set to the initial default value of `0`, while `section` is set to `4`:

css

    h1 {
      counter-reset: chapter section 4 page;
    }
    

Reversed counters created without an `<integer>` have an automatically calculated initial value. The browser counts the number of elements in the set, with the calculated initial value ensuring that if the `counter-increment` is set to `-1`, thereby decrementing the named counter by `1` for each element, the counter will be at `1` on the last element in the set.

The following example creates two reversed counters, `chapter` and `section`, and a regular counter, `pages`. The `section` counter starts at `10`, and `pages` uses the default initial value of `0`. The initial value of the `chapter` counter is calculated automatically. The counter is decremented by `1` each time an `<h2>` is encountered, so its value is `1` on the last `<h2>`.

css

    h1 {
      counter-reset: reversed(chapter) reversed(section) 10 pages;
    }
    h2 {
      counter-increment: chapter -1;
    }
    

### [Built-in `list-item` counter](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-reset#built-in_list-item_counter)

Ordered lists ([`<ol>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol)
) come with built-in `list-item` counters that control their numbering. These counters automatically increase or decrease by one with each list item. The `counter-reset` property can be used to reset the `list-item` counters. Like with other counters, you can override the default increment value for `list-item` counters by using the [`counter-increment`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-increment)
 property.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-reset#formal_definition)

---------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-reset#formal_syntax)

-------------------------------------------------------------------------------------------------------------------

counter-reset =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <counter-name> <integer>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <reversed-counter-name> <integer>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[+](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#plus "Plus: the entity may occur one or several times")
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  none                                                  
  
<counter-name> =   
  [<custom-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
    
  
[<integer>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 =   
  <number-token>    
  
<reversed-counter-name> =   
  reversed( <counter-name> )    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-reset#examples)

---------------------------------------------------------------------------------------------------------

### [Overriding the `list-item` counter](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-reset#overriding_the_list-item_counter)

In this example, the `counter-reset` property is used to set a starting value for an implicit `list-item` counter.

#### HTML

We include an ordered list ([`<ol>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol)
) containing five list items ([`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)
).

html

    <ol>
      <li>First</li>
      <li>Second</li>
      <li>Third</li>
      <li>Fourth</li>
      <li>Fifth</li>
    </ol>
    

#### CSS

Using `counter-reset`, we set the implicit `list-item` counter to start at a value other than the default `1`:

css

    ol {
      counter-reset: list-item 3;
    }
    

#### Result

The first item is numbered `4`. This is similar to the effect of writing [`<ol start="4">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol#start)
 in HTML.

### [Using a reverse counter](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-reset#using_a_reverse_counter)

In this example, the `reversed()` function is used to create a reversed counter named `priority` that numbers five tasks.

#### HTML

We include an unordered list ([`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)
) containing five list items ([`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)
).

html

    <ul class="stack">
      <li>Task A</li>
      <li>Task B</li>
      <li>Task C</li>
      <li>Task D</li>
      <li>Task E</li>
    </ul>
    

#### CSS

We create a reversed counter named `priority` on the `<ul>` and remove the default bullets. We decrement the counter by `1` on each `<li>`. We then use generated content to display the counter value before each list item's content.

css

    .stack {
      counter-reset: reversed(priority);
      list-style: none;
    }
    li {
      counter-increment: priority -1;
    }
    li::before {
      content: counter(priority) ". ";
    }
    

    @supports not (counter-reset: reversed(priority)) {
      body::before {
        content: "Your browser doesn't support the reversed() function.";
        background-color: wheat;
        display: block;
        text-align: center;
        padding: 1rem 0;
      }
    }
    

#### Result

The items are numbered in reverse order from `5` to `1`. Notice that we haven't specified the counter's initial value. The browser automatically calculates the initial value at layout time.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-reset#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Lists and Counters Module Level 3  <br>\# counter-reset](https://drafts.csswg.org/css-lists/#counter-reset) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-reset#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-reset#see_also)

---------------------------------------------------------------------------------------------------------

*   [Using CSS Counters](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles/Using_counters)
     guide
*   [`counter-increment`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-increment)
     property
*   [`counter-set`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-set)
     property
*   [`@counter-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style)
     at-rule
*   [`counter()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/counter)
     and [`counters()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/counters)
     functions
*   [`content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content)
     property
*   [`::marker`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::marker)
     pseudo-class
*   [CSS lists and counters](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Lists)
     module
*   [CSS counter styles](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 25, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-reset/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/counter-reset/index.md?plain=1 "Folder: en-us/web/css/reference/properties/counter-reset (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcounter-reset&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcounter-reset%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcounter-reset%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcounter-reset%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa326384789bf2f13f96506d4e2fdb4688d873cd0%0A*+Document+last+modified%3A+2026-09-25T13%3A52%3A40.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")