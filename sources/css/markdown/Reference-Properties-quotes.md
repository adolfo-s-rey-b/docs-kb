*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/quotes#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/quotes#mdn-search)
    

`quotes` CSS property
=====================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/quotes#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 **`quotes`** property sets how the browser should render quotation marks that are automatically added to the HTML [`<q>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/q)
 element or added using the `open-quotes` or `close-quotes` (or omitted using the `no-open-quote` and `no-close-quote`) values of the of the CSS [`content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content)
 property.

Browsers insert quotation marks at the opening and closing of `<q>` elements and for the `open-quote` and `close-quote` values of the `content` property. Each opening or closing quote is replaced by one of the strings from the value of `quotes`, based on the depth of nesting, or, if `quotes` is explicitly set to or otherwise resolves to `auto`, the quotation marks used are language dependent.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/quotes#try_it)

----------------------------------------------------------------------------------------------

    quotes: none;
    

    quotes: initial;
    

    quotes: "'" "'";
    

    quotes: "„" "“" "‚" "‘";
    

    quotes: "«" "»" "‹" "›";
    

    <section id="default-example">
      <q id="example-element"
        >Show us the wonder-working <q>Brothers,</q> let them come out publicly—and
        we will believe in them!</q
      >
    </section>
    

    q {
      font-size: 1.2rem;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/quotes#syntax)

----------------------------------------------------------------------------------------------

css

    /* Keyword values */
    quotes: none;
    quotes: auto;
    
    /* <string> values */
    quotes: "«" "»"; /* Set open-quote and close-quote to use French quotation marks */
    quotes: "«" "»" "‹" "›"; /* Set two levels of quotation marks */
    
    /* Global values */
    quotes: inherit;
    quotes: initial;
    quotes: revert;
    quotes: revert-layer;
    quotes: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/quotes#values)

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/quotes#none)

The `open-quote` and `close-quote` values of the [`content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content)
 property produce no quotation marks, as if `no-open-quote` and `no-close-quote` were set, respectively.

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/quotes#auto)

Quotation marks that are typographically appropriate for the inherited language (i.e., via the [`lang`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/lang)
 attribute set on the parent or other ancestor).

[`<string>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)

Defines one or more pairs of quotation mark values for opening and closing quotes. In each pair, the first of each pair of quotes are used as the values for the `open-quote` and the second of each pair is the `close-quote`.

The first pair represents the quotation's outer level. The second pair, if present, represents the first nested level. The next pair is used for doubly nested levels, and so on. If the depth of quote nesting is greater than the number of pairs, the last pair in the `quotes` value is repeated.

Which pair of quotes is used depends on the depth, or nesting level, of quotes: the number of occurrences of `<q>` quotes or `open-quote` (or `no-open-quote`) in all generated text before the current occurrence, minus the number of occurrences of closing quotes, either as `</q>`, `close-quote`, or `no-close-quote`. If the depth is 0, the first pair is used, if the depth is 1, the second pair is used, etc.

**Note:** The CSS `content` property value `no-open-quote` increments and `no-close-quote` decrements the quoting level, but they do not insert quotation marks.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/quotes#formal_definition)

--------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | depends on user agent |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/quotes#formal_syntax)

------------------------------------------------------------------------------------------------------------

quotes =   
  auto                    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  none                    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  bikeshed-this           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)\
 [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[+](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#plus "Plus: the entity may occur one or several times")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/quotes#examples)

--------------------------------------------------------------------------------------------------

### [Default quotes and overrides](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/quotes#default_quotes_and_overrides)

This example compares the default quotes provided by the semantic HTML `<q>` element to those we define using the CSS `quotes` property.

The default value of `quotes` is [`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/quotes#auto)
. In this example, the first list item has `quotes: auto` set, so gets the default quotes for the language specified; the same as if no `quotes` property was set. The second list item defines which quotation marks to use for quotes and nested quotes; these quotation marks will be used for descendants of an element with `specialQuotes` class regardless of the language (like any [`lang`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/lang)
 attribute values set).

#### HTML

html

    <ul>
      <li>
        Default quotes:
        <p lang="ru">
          <q
            >Митч Макконнелл - это человек, который знает о России и ее влиянии
            меньше, чем даже Дональд Трамп, и <q>я ничего не знаю</q>, сказал
            Трамп</q
          >, - писал Раджу.
        </p>
      </li>
      <li class="specialQuotes">
        Defined by <code>quotes</code> property :
        <p lang="ru">
          <q
            >Митч Макконнелл - это человек, который знает о России и ее влиянии
            меньше, чем даже Дональд Трамп, и <q>я ничего не знаю</q>, сказал
            Трамп</q
          >, - писал Раджу.
        </p>
      </li>
    </ul>
    

#### CSS

css

    li {
      quotes: auto;
    }
    
    .specialQuotes {
      quotes: "“" "”" "‘" "’";
    }
    

#### Result

By default, browser provide language specific quotation marks when the `<q>` element is used. If the `quotes` property is defined, the values provided override the browser defaults. Note the `quotes` property is inherited. The `quotes` property is set on the `<li>` with the `specialQuotes` class, but the quotes are applied the `<q>` elements.

Note that each open-quote and close-quote is replaced by one of the strings from the value of quotes, based on the depth of nesting.

### [Auto quotes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/quotes#auto_quotes)

The default value of `quotes` is `auto`. This example works without it being explicitly being set.

#### HTML

html

    <ul>
      <li lang="fr">
        <q>Ceci est une citation française.</q>
      </li>
      <li lang="ru">
        <q>Это русская цитата</q>
      </li>
      <li lang="de">
        <q>Dies ist ein deutsches Zitat</q>
      </li>
      <li lang="en">
        <q>This is an English quote.</q>
      </li>
    </ul>
    

#### CSS

css

    q {
      quotes: auto;
    }
    li:not(:last-of-type) {
      border-bottom: 1px solid;
    }
    

    li {
      padding: 0.5em 0;
    }
    

#### Result

Note that the [`lang`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/lang)
 attribute was placed on an ancestor of the `<q>`, not the `<q>` itself. If a quotation is in a different language than the surrounding text, it is customary to quote the text with the quote marks of the language of the surrounding text, not the language of the quotation itself.

### [With generated content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/quotes#with_generated_content)

In this example, instead of using the `<q>` element, we are adding quotation marks to the [`::before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::before)
 and [`::after`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::after)
 pseudo-elements before and after the content of each element with a specific class name.

#### HTML

html

    <p>
      <span class="quote">I should be using quotes</span>, I thought,
      <span class="quote"
        >But why use semantic HTML elements when I can add classes to
        <span class="quote">ALL THE THINGS!</span>?
      </span>
    </p>
    

#### CSS

css

    .quote {
      quotes: '"' '"' "'" "'";
    }
    .quote::before {
      content: open-quote;
    }
    .quote::after {
      content: close-quote;
    }
    

#### Result

### [Text as quotes and empty quotes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/quotes#text_as_quotes_and_empty_quotes)

This example demonstrates using something other than quotation marks as the `<string>` values. The open-quote indicates the speaker and, as there is no opening quotation mark, the close-quote is empty. (Mixing a `<string>` with an enumerated keyword to create a pair is not supported). We set `auto` for the nested quotes. These nested quotes will be book-ended by whatever the language dictates is normal for nested quotes.

#### HTML

html

    <ul>
      <li><q data-speaker="karen">Hello</q></li>
      <li><q data-speaker="chad">Hi</q></li>
      <li><q data-speaker="karen">this conversation is not interesting</q></li>
      <li>
        <q data-speaker="pat"
          >OMG! <q>Hi</q>? Seriously? at least <q>hello</q> is five letters long.</q
        >
      </li>
    </ul>
    

#### CSS

css

    [data-speaker="karen" i] {
      quotes: "She said: " "";
    }
    [data-speaker="chad" i] {
      quotes: "He said: " "";
    }
    [data-speaker="pat" i] {
      quotes: "They said: " "";
    }
    [data-speaker] q {
      quotes: auto;
    }
    

    li {
      padding: 0.5em 0;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/quotes#specifications)

--------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Generated Content Module Level 3  <br>\# quotes](https://drafts.csswg.org/css-content/#quotes) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/quotes#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/quotes#see_also)

--------------------------------------------------------------------------------------------------

*   [CSS generated content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Generated_content)
     module
*   [`contain`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain)
    
*   [`content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 16, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/quotes/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/quotes/index.md?plain=1 "Folder: en-us/web/css/reference/properties/quotes (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fquotes&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fquotes%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fquotes%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fquotes%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F880c2c4b113c6fe127ca3ae3603a56ef7a2eb9a6%0A*+Document+last+modified%3A+2026-09-16T20%3A20%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")