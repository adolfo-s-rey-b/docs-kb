*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/system#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/system#mdn-search)
    

`system` CSS at-rule descriptor
===============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2023.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/system#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`system`** descriptor specifies the algorithm to be used for converting the integer value of a counter to a string representation. It is used in a [`@counter-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style)
 to define the behavior of the defined style.

If the algorithm specified in the `system` descriptor is unable to construct the representation for a particular counter value, then that value's representation will be constructed using the fallback system provided.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/system#syntax)

-----------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    system: cyclic;
    system: numeric;
    system: alphabetic;
    system: symbolic;
    system: additive;
    system: fixed;
    
    /* Other values */
    system: fixed 3;
    system: extends decimal;
    system: extends circled-letters;
    

[Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/system#values)

-----------------------------------------------------------------------------------------------------------

This may take one of three forms:

*   One of the keyword values `cyclic`, `numeric`, `alphabetic`, `symbolic`, `additive`, or `fixed`.
*   The keyword value `fixed` along with an integer.
*   The keyword value `extends` along with a [`<counter-style-name>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style#counter-style-name)
     value.

The values include:

[`cyclic`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/system#cyclic)

Cycles through the list of symbols provided in the [`symbols`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/symbols)
 descriptor. Once the end of the list is reached, the cycle will loop back to the beginning and start over. This value is useful both for basic bullet styles with just one symbol and for styles with multiple symbols. At least one symbol must be specified in the `symbols` descriptor, otherwise the counter style is not valid.

[`numeric`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/system#numeric)

Interprets the counter symbols as digits in a [place-value numbering system](https://en.wikipedia.org/wiki/Positional_notation "External link (opens in new tab)")
. The numeric system is similar to the `alphabetic` system, described above. The main difference is that in the `alphabetic` system, the first counter symbol given in the `symbols` descriptor is interpreted as `1`, the next as `2`, and so on. However, in the numeric system, the first counter symbol is interpreted as 0, the next as `1`, then `2`, and so on.

At least two counter symbols must be specified in the `symbols` descriptor or the counter style is not valid.

[`alphabetic`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/system#alphabetic)

Interprets the specified symbols as digits, to an alphabetic numbering system. If the characters `"a"` to `"z"` are specified as symbols in a counter style, with the `alphabetic` system, then the first 26 counter representations will be `"a"`, `"b"` up to `"z"`. Until this point, the behavior is the same as that of the `symbolic` system, described above. However, after `"z"`, it will continue as `"aa"`, `"ab"`, `"ac"`…

The `symbols` descriptor must contain at least two symbols or the counter style is not valid. The first counter symbol provided in the `symbols` descriptor is interpreted as `1`, the next as `2`, and so on. This system is also defined strictly over positive counter values.

[`symbolic`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/system#symbolic)

Cycles through the symbols provided in the `symbols` descriptor list repeatedly, doubling, tripling, and so on, the symbols on each successive pass through the list. For example, if two symbols "◽" and "◾" are specified in the `symbols` descriptor, on each successive pass, they will become "◽◽" and "◾◾", then "◽◽◽" and "◾◾◾", and so on in subsequent passes. At least one symbol must be specified in the `symbols` descriptor, otherwise the counter style is not valid. This counter system works for positive counter values only.

[`additive`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/system#additive)

Used to represent "sign-value" numbering systems, such as Roman numerals, which rather than reuse digits in different positions to obtain different values, define additional digits for larger values. The value of a number in such a system can be found out by adding the digits in the number.

An additional descriptor called `additive-symbols` must be specified with at least one _additive tuple_, or else the counter style rule will not be valid. An additive tuple is similar to a composite counter symbol, which is made up of two parts: a normal counter symbol and a non-negative integer weight. The additive tuples must be specified in the descending order of their weights or the system is invalid.

[`fixed` or `fixed <integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/system#fixed)

Defines a finite set of symbols, iterating once through the list of symbols provided in the `symbols` descriptor. Once the specified symbols have been iterated through, the fallback counter style is used. This keyword value is useful in cases where the counter style values are finite. At least one symbol must be specified in the `symbols` descriptor, otherwise the counter style is not valid. The `fixed` keyword can be followed by an optional [`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 value. If specified, the `<integer>` value indicates the item in the list that will get the first symbol from the list of symbols. If omitted, the default value of `integer` is `1`, which gives the first item in the list the first symbol.

[`extends`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/system#extends)

Extends the algorithm of another browser- or author-defined counter style by allowing the alteration of some aspects of the extended counter style. Any unspecified descriptors and their values are inherited from the extended counter style specified. If the counter style name specified with `extends` is not yet defined, the `decimal` counter style will be extended by default.

It must not contain a `symbols` or `additive-symbols` descriptor, otherwise the counter style rule will be invalid. If one or more counter styles definitions form a cycle with their `extends` values, the browser will treat all the participating counter styles as extending from the `decimal` style.

**Note:** The [`symbols`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/symbols)
 descriptor is required when the value is `cyclic`, `numeric`, `alphabetic`, `symbolic`, or `fixed`. The [`additive-symbols`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/additive-symbols)
 descriptor is required if the `additive` value is set.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/system#formal_definition)

---------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| Related [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules) | [`@counter-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style) |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `symbolic` |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/system#formal_syntax)

-------------------------------------------------------------------------------------------------------------------------

system =   
  cyclic                            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  numeric                           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  alphabetic                        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  symbolic                          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  additive                          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 fixed <integer>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 extends <counter-style-name> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    
  
[<integer>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 =   
  <number-token>    
  
<counter-style-name> =   
  [<custom-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/system#examples)

---------------------------------------------------------------------------------------------------------------

### [Cyclic counter](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/system#cyclic_counter)

The `cyclic` value iterates through the list of symbols, repeating the list as necessary:

#### CSS

    <ul>
      <li>One</li>
      <li>Two</li>
      <li>Three</li>
      <li>Four</li>
      <li>Five</li>
      <li>Six</li>
    </ul>
    

css

    @counter-style fisheye {
      system: cyclic;
      symbols: ◉ ➀;
      suffix: ": ";
    }
    
    ul {
      list-style: fisheye;
    }
    

#### Result

### [Fixed counter](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/system#fixed_counter)

The `fixed` value iterates through the list of symbols only once, starting the single cycle at the list item number indicated by the `integer` value:

#### CSS

    <ul>
      <li>One</li>
      <li>Two</li>
      <li>Three</li>
      <li>Four</li>
      <li>Five</li>
      <li>Six</li>
    </ul>
    

css

    @counter-style circled-digits {
      system: fixed 3;
      symbols: ➀ ➁ ➂;
      suffix: ": ";
    }
    
    ul {
      list-style: circled-digits;
    }
    

#### Result

### [Symbolic counter](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/system#symbolic_counter)

The `symbolic` value loops through the list defined in the `symbols` descriptor, doubling and tripling the number of symbols for the second and third cycles through the list, respectively:

#### CSS

    <ul>
      <li>One</li>
      <li>Two</li>
      <li>Three</li>
      <li>Four</li>
      <li>Five</li>
      <li>Six</li>
      <li>Seven</li>
      <li>Eight</li>
    </ul>
    

css

    @counter-style abc {
      system: symbolic;
      symbols: a b c;
      suffix: ". ";
    }
    
    ul {
      list-style: abc;
    }
    

#### Result

### [Alphabetic counter](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/system#alphabetic_counter)

#### CSS

    <ul>
      <li>One</li>
      <li>Two</li>
      <li>Three</li>
      <li>Four</li>
      <li>Five</li>
      <li>Six</li>
      <li>Seven</li>
      <li>Eight</li>
    </ul>
    

css

    @counter-style abc {
      system: alphabetic;
      symbols: a b c;
      suffix: ". ";
    }
    
    ul {
      list-style: abc;
    }
    

#### Result

### [Numeric counter](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/system#numeric_counter)

The first symbol provided in the `symbols` descriptor is interpreted as `0` here.

#### CSS

    <ul>
      <li>One</li>
      <li>Two</li>
      <li>Three</li>
      <li>Four</li>
      <li>Five</li>
      <li>Six</li>
      <li>Seven</li>
      <li>Eight</li>
    </ul>
    

css

    @counter-style abc {
      system: numeric;
      symbols: a b c;
      suffix: ". ";
    }
    
    ul {
      list-style: abc;
    }
    

#### Result

### [Numeric counter with numeric symbols](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/system#numeric_counter_with_numeric_symbols)

As shown in the following example, if digits from `0` to `9` are specified as symbols, this counter style will render symbols same as the decimal counter style.

#### CSS

    <ul class="list">
      <li>One</li>
      <li>Two</li>
      <li>Three</li>
      <li>Four</li>
      <li>Five</li>
      <li>Six</li>
      <li>Seven</li>
      <li>Eight</li>
      <li>Nine</li>
      <li>Ten</li>
    </ul>
    

css

    @counter-style numbers {
      system: numeric;
      symbols: "0" "1" "2" "3" "4" "5" "6" "7" "8" "9";
      suffix: ".";
    }
    
    ul {
      list-style: numbers;
    }
    

#### Result

### [Additive counter](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/system#additive_counter)

This example renders a list using Roman numerals. Notice that a `range` is specified. This is because the representation will produce correct Roman numerals only until the counter value of `3999`. Once outside of the range, the rest of the counter representations will be based on the `decimal` style, which is the fallback. If you need to represent counter values as Roman numerals, you could use either one of the predefined counter styles, `upper-roman` or `lower-roman`, rather than recreating the rule yourself.

#### HTML

We use the [`start`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol#start)
 attribute on the [`<ol>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol)
 element to demonstrate that counting doesn't need to start at `1`. Additionally, we use the [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li#value)
 attribute on the fifth [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)
 element to demonstrate that the counters you define using `@counter-style` behave just like native counters.

html

    <ol start="48">
      <li>48</li>
      <li>49</li>
      <li>50</li>
      <li>51</li>
      <li value="109">109</li>
      <li>110</li>
    </ol>
    

#### CSS

css

    @counter-style uppercase-roman {
      system: additive;
      range: 1 3999;
      additive-symbols:
        1000 M,
        900 CM,
        500 D,
        400 CD,
        100 C,
        90 XC,
        50 L,
        40 XL,
        10 X,
        9 IX,
        5 V,
        4 IV,
        1 I;
    }
    
    ol {
      list-style: uppercase-roman;
      padding-left: 5em;
    }
    

#### Result

### [Extending a counter](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/system#extending_a_counter)

This example uses the algorithm, symbols, and other properties of [`lower-alpha`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#lower-alpha)
, one of the several native [`list-style-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type)
 counter values, but extends it by removing the period (`'.'`) after the counter representation and enclosing the characters in parentheses, as in `(a)` and `(b)`.

#### HTML

html

    <ul class="list">
      <li>One</li>
      <li>Two</li>
      <li>Three</li>
      <li>Four</li>
      <li>Five</li>
    </ul>
    

#### CSS

css

    @counter-style alpha-modified {
      system: extends lower-alpha;
      prefix: "(";
      suffix: ") ";
    }
    
    ul {
      list-style: alpha-modified;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/system#specifications)

---------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Counter Styles Level 3  <br>\# counter-style-system](https://drafts.csswg.org/css-counter-styles/#counter-style-system) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/system#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/system#see_also)

---------------------------------------------------------------------------------------------------------------

*   Other [`@counter-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style)
     descriptors, including [`symbols`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/symbols)
    , [`additive-symbols`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/additive-symbols)
    , [`negative`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/negative)
    , [`prefix`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/prefix)
    , [`suffix`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/suffix)
    , [`range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/range)
    , [`pad`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/pad)
    , [`speak-as`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/speak-as)
    , and [`fallback`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/fallback)
    
*   [`list-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style)
    , [`list-style-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-image)
    , [`list-style-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-position)
    
*   [`symbols()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/symbols)
    , the functional notation for creating anonymous counter styles.

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 2, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/system/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@counter-style/system/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@counter-style/system (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40counter-style%2Fsystem&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40counter-style%2Fsystem%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40counter-style%2Fsystem%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40counter-style%2Fsystem%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F07758d01509695fe45ccc3f7687f6597dc3d9e2a%0A*+Document+last+modified%3A+2026-09-02T04%3A34%3A34.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")