*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles/Using_counters#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles/Using_counters#mdn-search)
    

Using CSS counters
==================

**CSS counters** let you adjust the appearance of content based on its location in a document. For example, you can use counters to automatically number the headings on a webpage or to change the numbering on ordered lists.

Counters are, in essence, variables maintained by CSS whose values may be incremented or decremented by CSS rules that track how many times they're used. The following things affect the counter values on an element:

1.  Counters are [inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles/Using_counters#counter_inheritance_and_propagation)
     from the parent element or received from a previous sibling.
2.  New counters are instantiated using [`counter-reset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-reset)
     property.
3.  Counters are incremented using [`counter-increment`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-increment)
     property.
4.  Counters are directly set to a value using the [`counter-set`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-set)
     property.

You can define your own named counters, and you can also manipulate the `list-item` counter that is created by default for all ordered lists.

[Using counters](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles/Using_counters#using_counters)

-----------------------------------------------------------------------------------------------------------------------

To use a counter, it must first be initialized to a value with the [`counter-reset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-reset)
 property. The counter's value can be increased or decreased using the [`counter-increment`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-increment)
 property and can be directly set to a specific value using the [`counter-set`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-set)
 property. The current value of a counter is displayed using the [`counter()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/counter)
 or [`counters()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/counters)
 function, typically within a [pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements)
 [`content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content)
 property.

Counters can only be set, reset, or incremented in elements that generate boxes. For example, if an element is set to `display: none`, then any counter operation on that element is ignored.

The properties of counters can be scoped to specific elements using style containment, which is described in more detail in the [`contain`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain)
 property.

### [Manipulating a counter's value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles/Using_counters#manipulating_a_counters_value)

To use a CSS counter, it must first be initialized to a value with the [`counter-reset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-reset)
 property. The property can also be used to change the counter value to any specific number.

The following declaration initializes a counter named `section` to the default value (`0`):

You can also initialize multiple counters, optionally specifying an initial value for each. The following declaration initializes the `section` and `topic` counters to the default value, and the `page` counter to `3`:

Once initialized, a counter's value can be increased or decreased using [`counter-increment`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-increment)
. For example, the following declaration increments the value of the `section` counter by `1` on every `<h3>` element:

You can specify the increment or decrement amount after the counter name. It can be a positive or negative number, but defaults to `1` if no integer is provided.

Apart from being incremented or decremented, counters can also be explicitly set to a value using the [`counter-set`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-set)
 property.

The counter's name must not be `none`, `inherit`, or `initial`; otherwise the declaration is ignored.

### [Displaying a counter](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles/Using_counters#displaying_a_counter)

The value of a counter can be displayed using either the [`counter()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/counter)
 or [`counters()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/counters)
 function in a [`content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content)
 property.

For example, the following declaration uses `counter()` to prefix each `h3` heading with the text `Section <number>:`, where `<number>` is the value of the count in decimal (the default display style):

This creates a counter named `section` on the [`<body>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body)
 element and sets its initial value to `0`. The counter increments by `1` on every `<h3>` element. Before the content of each `<h3>` heading, `Section <n>:` is displayed, where `<n>` is the default decimal value of the `section` counter.

### [Comparing `counter()` and `counters()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles/Using_counters#comparing_counter_and_counters)

The [`counter()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/counter)
 function is used when the numbering of nesting levels does not include the context of parent levels. For example, here each nested level restarts from one:

1 One
  1 Nested one
  2 Nested two
2 Two
  1 Nested one
  2 Nested two
  3 Nested three
3 Three

The [`counters()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/counters)
 function is used when the count for nested levels must include the count from parent levels. For example, you might use this to lay out sections as shown:

1 One
  1.1 Nested one
  1.2 Nested two
2 Two
  2.1 Nested one
  2.2 Nested two
  2.3 Nested three
3 Three

The [`counter()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/counter)
 function has two forms: `counter(<counter-name>)` and `counter(<counter-name>, <counter-style>)`. The generated text is the value of the innermost counter of the given name in scope at the pseudo-element.

The [`counters()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/counters)
 function also has two forms: `counters(<counter-name>, <separator>)` and `counters(<counter-name>, <separator>, <counter-style>)`. The generated text is the value of all counters with the given name in scope at the given pseudo-element, from outermost to innermost, separated by the specified string (`<separator>`).

The counter is rendered in the specified `<counter-style>` for both methods (`decimal` by default). You can use any of the [`list-style-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type)
 values or your own [custom styles](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles)
.

The use of the `counter()` and `counters()` functions is demonstrated later in the [Basic example](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles/Using_counters#basic_example)
 and [Nested counters](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles/Using_counters#nested_counters)
 sections, respectively.

### [Reversed counters](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles/Using_counters#reversed_counters)

A reversed counter is one that is intended to count down (decrement) rather than up (increment). Reversed counters are created using the `reversed()` function notation when naming the counter in [`counter-reset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-reset)
.

Reversed counters have a default initial value equal to the number of elements (unlike normal counters, which have a default value of 0). This enables implementing a counter that counts from the number of elements down to one.

For example, to create a reversed counter named `section` with a default initial value, you would use the following syntax:

You can, of course, specify any initial value that you like.

The counter value is decreased by specifying a negative value for [`counter-increment`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-increment)
.

**Note:** You can also use [`counter-increment`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-increment)
 to decrement a non-reversed counter. The main benefit of using a reversed counter is the default initial value, and that the `list-item` counter automatically decrements reversed counters.

### [Counter inheritance and propagation](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles/Using_counters#counter_inheritance_and_propagation)

Each element or pseudo-element has a set of counters in the scope of that element. Initial counters in the set are received from the element's parent and the preceding sibling. The counter values are received from the last descendant of the previous sibling, the last sibling, or the parent.

When an element declares a counter, the counter is nested inside the counter with the same name received from the parent. If the parent doesn't have a counter with the same name, then the counter is added to the element's counters set as it is. A counter with the same name received from the previous sibling is removed from the element's set of counters.

The [`counter()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/counter)
 function retrieves the innermost counter with the provided name. The [`counters()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/counters)
 function retrieves the entire counter tree with the given name.

The following example demonstrates an inherited counter named `primary` and a sibling counter named `secondary`. All the `<div>` elements display their counters using the `counters()` function. Note that all the counters have been created using the `counter-reset` property, and none of the counters have been incremented.

We create the `primary` counter on divs' parent, then create a new `primary` counter on `D`. We create the `secondary` counter on `F`, then override the sibling `secondary` counter on `I`.

The section element initializes a counter named `primary` with value `3`, and all the child `<div>`s receive the inherited `primary` counter. The element 'D' creates a new `primary` (value `6`) counter which gets nested in the counter received from the parent, so the element has two counters named `primary` with values `3` and `6`.

The element 'F' creates the `secondary` (value `5`) counter for the first time, and it passes the counter to the next sibling 'G'. The element 'G' passes the counter to the next element 'H' and so on. Next, the element 'I' creates a new counter with the same name `secondary` (value `10`), but it drops the `secondary` (value `5`) counter received from the previous sibling 'H' and passes its own counter to 'J'.

### [Difference between counter-set and counter-reset](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles/Using_counters#difference_between_counter-set_and_counter-reset)

The [`counter-set`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-set)
 property updates an existing counter. If no counter with that name exists, then a new counter is instantiated. The [`counter-reset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-reset)
 property _always_ creates a new counter.

In the following example, we have two sub-lists inside a parent list. Each list item has been numbered using a counter named 'item'. The first sub-list uses [`counter-set`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-set)
 property and the second sub-list uses [`counter-reset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-reset)
 property to change the 'item' counter.

html

    <ul class="parent">
      <li>A</li>
      <li>B</li>
      <li>
        C (the counter updated using `counter-set`)
        <ul class="sub-list-one">
          <li>sub-A</li>
          <li>sub-B</li>
        </ul>
      </li>
      <li>D</li>
      <li>
        E (a new counter created using `counter-reset`)
        <ul class="sub-list-two">
          <li>sub-A</li>
          <li>sub-B</li>
          <li>sub-C</li>
        </ul>
      </li>
      <li>F</li>
      <li>G</li>
    </ul>
    

    ul {
      list-style: none;
    }
    

We create a new counter on `parent` and increment it on each list item, then show the numbers on the list items using generated content. We update the existing counter value with `counter-set`, then reset it with `counter-reset` on `.sub-list-one` and `.sub-list-two`, respectively.

css

    .parent {
      counter-reset: item 0;
    }
    
    li {
      counter-increment: item;
    }
    
    li::before {
      content: counter(item) " ";
    }
    
    .sub-list-one {
      counter-set: item 10;
    }
    
    .sub-list-two {
      counter-reset: item 0;
    }
    

Notice how the first sub-list starts at `11`, and its numbering continues in the parent list. This is because the `counter-set` property updates the same `item` counter declared on `.parent`. The second sub-list starts at `1` and the parent list items after it don't carry forward the numbering. This is because the `counter-reset` property creates a new counter with the same name, so the parent list items use the original counter.

### [List item counters](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles/Using_counters#list_item_counters)

Ordered lists, as created using [`<ol>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol)
 elements, implicitly have a counter named `list-item`.

Like other counters, this has a default initial value of 0 for upward counters and "number of items" for reversed counters. Unlike author-created counters, `list-item` _automatically_ increments or decrements by one for each list element, depending on whether or not the counter is reversed.

You can use the `list-item` counter to manipulate the default behavior of ordered lists with CSS. For example, you can change the default initial value, or use [`counter-increment`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-increment)
 to change the way in which the list items increment or decrement.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles/Using_counters#examples)

-----------------------------------------------------------------------------------------------------------

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles/Using_counters#basic_example)

This example adds "Section \[the value of the counter\]:" to the beginning of each heading.

#### HTML

We include three `<h3>` elements.

html

    <h3>Introduction</h3>
    <h3>Body</h3>
    <h3>Conclusion</h3>
    

#### CSS

We create a counter named 'section', letting its initial value default to `0`. We increment the value of `section` counter by `1` at each `<h3>` and display the word "Section", the value of `section` counter, and a colon before the content of each `<h3>`.

css

    body {
      counter-reset: section;
    }
    
    h3::before {
      counter-increment: section;
    }
    h3::before {
      content: "Section " counter(section) ": ";
    }
    

#### Result

### [Reversed counter](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles/Using_counters#reversed_counter)

This example uses the same HTML as the previous example but uses a reversed counter, numbering the elements from 3 to 1.

    <h3>Introduction</h3>
    <h3>Body</h3>
    <h3>Conclusion</h3>
    

#### CSS

We use the `reversed()` function to create a counter named 'section', letting the initial value default so that when we decrement the value of `section` counter by `1` on each `<h3>`, the last element in the set will have the counter set to `1`. We use [generated content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Generated_content)
 to display the word 'Section ' and the value of the counter before the content of each `<h3>`.

css

    body {
      counter-reset: reversed(section);
    }
    
    h3 {
      counter-increment: section -1;
    }
    h3::before {
      content: "Section " counter(section) ": ";
    }
    

    @supports not (counter-reset: reversed(section)) {
      body::before {
        content: "Your browser doesn't support the reversed() function.";
        background-color: wheat;
        display: block;
        text-align: center;
        padding: 1rem 0;
      }
    }
    

#### Result

### [A more elaborate example](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles/Using_counters#a_more_elaborate_example)

A counter need not necessarily be shown every time it is incremented. This example counts all links but shows the counter as generated content only when a link has no text.

#### HTML

We include three paragraphs, each with a link, but the first and last links contain no text.

html

    <p>See <a href="https://www.mozilla.org/" aria-label="Mozilla"></a></p>
    <p>Do not forget to <a href="contact-me.html">leave a message</a>!</p>
    <p>See also <a href="https://developer.mozilla.org/" aria-label="MDN"></a></p>
    

#### CSS

We create and initialize the counter on `:root`, increment it on every link, and generate content only when the link is [`:empty`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:empty)
.

css

    :root {
      counter-reset: link;
    }
    
    a[href] {
      counter-increment: link;
    }
    
    a[href]:empty::after {
      content: "[" counter(link) "]";
    }
    

#### Result

### [Nested counters](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles/Using_counters#nested_counters)

A CSS counter can be especially useful for making outlined lists, because a new instance of the counter is automatically created in child elements. Using the [`counters()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/counters)
 function, separating text can be inserted between different levels of nested counters.

#### CSS

We create a new instance of the section counter with each `<ol>` element, incrementing only the current instance of the section counter on each `<li>`. Using the [`counters()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/counters)
 function, we combine the values of all instances of the section counter, separated by a period.

css

    ol {
      counter-reset: section;
      list-style-type: none;
    }
    
    li {
      counter-increment: section;
    }
    
    li::before {
      content: counters(section, ".") " ";
    }
    

#### HTML

html

    <ol>
      <li>item</li>          <!-- 1     -->
      <li>item               <!-- 2     -->
        <ol>
          <li>item</li>      <!-- 2.1   -->
          <li>item</li>      <!-- 2.2   -->
          <li>item           <!-- 2.3   -->
            <ol>
              <li>item</li>  <!-- 2.3.1 -->
              <li>item</li>  <!-- 2.3.2 -->
            </ol>
            <ol>
              <li>item</li>  <!-- 2.3.1 -->
              <li>item</li>  <!-- 2.3.2 -->
              <li>item</li>  <!-- 2.3.3 -->
            </ol>
          </li>
          <li>item</li>      <!-- 2.4   -->
        </ol>
      </li>
      <li>item</li>          <!-- 3     -->
      <li>item</li>          <!-- 4     -->
    </ol>
    <ol>
      <li>item</li>          <!-- 1     -->
      <li>item</li>          <!-- 2     -->
    </ol>
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles/Using_counters#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Lists and Counters Module Level 3  <br>\# auto-numbering](https://drafts.csswg.org/css-lists/#auto-numbering) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles/Using_counters#see_also)

-----------------------------------------------------------------------------------------------------------

*   [`contain`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain)
    
*   [`counter-reset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-reset)
    
*   [`counter-set`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-set)
    
*   [`counter-increment`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-increment)
    
*   [`@counter-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style)
    
*   [CSS counter styles](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles)
     module
*   [CSS lists and counters](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Lists)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 15, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles/Using_counters/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/counter_styles/using_counters/index.md?plain=1 "Folder: en-us/web/css/guides/counter_styles/using_counters (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FCounter_styles%2FUsing_counters&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fcounter_styles%2Fusing_counters%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FCounter_styles%2FUsing_counters%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fcounter_styles%2Fusing_counters%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff60b6627900af0ba2132de74c77829fa6c189b57%0A*+Document+last+modified%3A+2026-10-15T08%3A50%3A12.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")