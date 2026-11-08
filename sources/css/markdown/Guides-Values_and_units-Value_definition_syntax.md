*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#mdn-search)
    

Value definition syntax
=======================

**CSS value definition syntax**, a formal grammar, is used to define the set of valid values for a CSS property or function. In addition to this syntax, the set of valid values can be further restricted by semantic constraints (for example, for a number to be strictly positive).

The definition syntax describes which values are allowed and the interactions between them. A component can be a _keyword_, some characters considered as a _literal_, or a value of a given CSS data type or another CSS property.

[Component value types](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#component_value_types)

------------------------------------------------------------------------------------------------------------------------------------------------

### [Keywords](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#keywords)

#### Generic keywords

A keyword with a predefined meaning appears literally, without quotation marks. For example: `auto`, `smaller`, or `ease-in`.

#### CSS-wide keywords

All CSS properties accept the keywords `inherit`, `initial`, `revert`, `revert-layer`, and `unset`. They are not shown in the value definition and are implicitly defined.

### [Literals](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#literals)

In CSS, a few characters can appear on their own, like the slash (`/`) or the comma (`,`), and are used in a property definition to separate its parts. The comma is often used to separate values in enumerations, or parameters in mathematical-like functions; the slash often separates parts of the value that are semantically different, but have a common syntax. Typically, the slash is used in shorthand properties; to separate components of the same type, but belong to different properties.

Both symbols appear literally in a value definition.

### [Data types](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#data_types)

#### Basic data types

Some data types are used throughout CSS and are defined once for all values in the specification. Called _basic data types_, they are represented with their name surrounded by the symbols `<` and `>`: [`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)
, [`<string>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
, …

#### Non-terminal data types

Less common data types, called _non-terminal data types_, are also surrounded by `<` and `>`.

Non-terminal data types are of two kinds:

*   data types _sharing the same name of a property_, put between quotes. In this case, the data type shares the same set of values as the property. They are often used in the definition of shorthand properties.
*   data types _not sharing the same name of a property_. These data types are very close to the basic data types. They only differ from the basic data types in the physical location of their definition. In this case, the definition is usually physically very close to the definition of the property using them.

[Component value combinators](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#component_value_combinators)

------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Brackets](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets)

_Brackets_ enclose several entities, combinators, and multipliers, then transform them as a single component. They are used to **group components to bypass the precedence rules**.

example =   
  bold [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 thin [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")\
 [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    

This example matches the following values:

*   `bold thin 2vh`
*   `bold 0 thin`
*   `bold thin 3.5em`

But not:

*   `thin bold 3em`, as `bold` is juxtaposed with the component defined by the brackets, it must appear before it.

### [Juxtaposition](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#juxtaposition)

Placing several keywords, literals, or data types, next to one another, only separated by one or several spaces, is called _juxtaposition_. All juxtaposed components are **mandatory and should appear in the exact order**.

example =   
  bold [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 , thin    

This example matches the following values:

*   `bold 1em, thin`
*   `bold 0, thin`
*   `bold 2.5cm, thin`
*   `bold 3vh, thin`

But not:

*   `thin 1em, bold`, as the entities must be in the expressed order
*   `bold 1em thin`, as the entities are mandatory; the comma, a literal, must be present
*   `bold 0.5ms, thin`, as the `ms` values are not [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
    

### [Double ampersand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand)

Separating two or more components, by a _double ampersand_, `&&`, means that all these entities are **mandatory but may appear in any order**.

example =   
  bold      [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")
  
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
    

This example matches the following values:

*   `bold 1em`
*   `bold 0`
*   `2.5cm bold`
*   `3vh bold`

But not:

*   `bold`, as both components must appear in the value.
*   `bold 1em bold`, as both components must appear only once.

**Note:** Juxtaposition has precedence over the double ampersand, meaning that `bold thin && <length>` is equivalent to `[ bold thin ] && <length>`. It describes `bold thin <length>` or `<length> bold thin` but not `bold <length> thin`.

### [Double bar](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar)

Separating two or more components by a _double bar_, `||`, means that all entities are options: **at least one must be present, and they may appear in any order**. Typically this is used to define the different values of a [shorthand property](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
.

example =   
  [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
  [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
  [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
     

This example matches the following values:

*   `1em 1 blue`
*   `blue 1em`
*   `1 1px yellow`

But not:

*   `blue yellow`, as a component must appear once at most.
*   `bold`, as it isn't a keyword allowed as a value of any of the entities.

**Note:** The double ampersand has precedence over the double bar, meaning that `bold || thin && <length>` is equivalent to `bold || [ thin && <length> ]`. It describes `bold`, `thin <length>`, `bold thin <length>`, or `thin <length> bold` but not `<length> bold thin` as bold, if not omitted, must be placed before or after the whole `thin && <length>` component.

### [Single bar](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar)

Separating two or more entities by a _single bar_, `|`, means that all entities are exclusive options: **exactly one of these options must be present**. This is typically used to separate a list of possible keywords.

example =   
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  left          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  center        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  right         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  top           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  bottom          

This example matches the following values:

*   `3%`
*   `0`
*   `3.5em`
*   `left`
*   `center`
*   `right`
*   `top`
*   `bottom`

But not:

*   `center 3%`, as only one of the components must be present.
*   `3em 4.5em`, as a component must be present at most one time.

**Note:** The double bar has precedence over the single bar, meaning that `bold | thin || <length>` is equivalent to `bold | [ thin || <length> ]`. It describes `bold`, `thin`, `<length>`, `<length> thin`, or `thin <length>` but not `bold <length>` as only one entity from each side of the `|` combinator can be present.

[Component value multipliers](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#component_value_multipliers)

------------------------------------------------------------------------------------------------------------------------------------------------------------

A multiplier is a sign that indicates how many times a preceding entity can be repeated. Without a multiplier, an entity must appear exactly one time.

Multipliers cannot be added and have precedence over all combinators.

### [Asterisk (`*`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#asterisk)

The _asterisk multiplier_ indicates that the entity may appear **zero, one or several times**.

example =   
  bold smaller[\*](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#asterisk "Asterisk: the entity may occur zero, one or several times")
    

This example matches the following values:

*   `bold`
*   `bold smaller`
*   `bold smaller smaller`
*   `bold smaller smaller smaller`, and so on.

But not:

*   `smaller`, as `bold` is juxtaposed, and must appear before any `smaller` keyword.

### [Plus (`+`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#plus)

The _plus multiplier_ indicates that the entity may appear **one or several times**.

example =   
  bold smaller[+](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#plus "Plus: the entity may occur one or several times")
    

This example matches the following values:

*   `bold smaller`
*   `bold smaller smaller`
*   `bold smaller smaller smaller`, and so on.

But not:

*   `bold`, as `smaller` must appear at least once.
*   `smaller`, as `bold` is juxtaposed and must appear before any `smaller` keyword.

### [Question mark (`?`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark)

The _question mark multiplier_ indicates that the entity is optional, and **must appear zero or one time**.

example =   
  bold smaller[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    

This example matches the following values:

*   `bold`
*   `bold smaller`

But not:

*   `bold smaller smaller`, as `smaller` must appear at most once.
*   `smaller`, as `bold` is juxtaposed and must appear before any `smaller` keyword.

### [Curly braces (`{ }`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces)

The _curly braces multiplier_, enclosing two integers separated by a comma, A and B, indicates that the entity **must appear at least A times and at most B times**.

example =   
  bold smaller[{1,3}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
    

This example matches the following values:

*   `bold smaller`
*   `bold smaller smaller`
*   `bold smaller smaller smaller`

But not:

*   `bold`, as `smaller` must appear at least once.
*   `bold smaller smaller smaller smaller`, as `smaller` must appear at most three times.
*   `smaller`, as `bold` is juxtaposed and must appear before any `smaller` keyword

### [Hash mark (`#`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark)

The _hash mark multiplier_ indicates that the entity may be repeated one or more times (for example, the plus multiplier), but each occurrence is separated by a comma (',').

example =   
  bold smaller[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    

This example matches the following values:

*   `bold smaller`
*   `bold smaller, smaller`
*   `bold smaller, smaller, smaller`, and so on.

But not:

*   `bold`, as `smaller` must appear at least once.
*   `bold smaller smaller smaller`, as the different occurrences of `smaller` must be separated by commas.
*   `smaller`, as `bold` is juxtaposed and must appear before any `smaller` keyword.

The hash mark may optionally be followed by curly braces to indicate how many times the entity repeats.

example =   
  bold smaller[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
[{1,3}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
    

This example matches the following values:

*   `bold smaller`
*   `bold smaller, smaller`
*   `bold smaller, smaller, smaller`

But not:

*   `bold smaller, smaller, smaller, smaller`, as `smaller` must appear at most three times.

example =   
  bold smaller[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
[{2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
    

This example matches the following value:

*   `bold smaller, smaller`

But not:

*   `bold smaller`, as `smaller` must appear exactly two times.

### [Exclamation point (`!`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#exclamation_point_!)

The _exclamation point multiplier_ after a group indicates that the group is required, and must produce at least one value; even if the grammar of the items within the group would otherwise allow the entire contents to be omitted, at least one component value must not be omitted.

example =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 bold[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 smaller[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
!    

This example matches the following values:

*   `bold`
*   `smaller`
*   `bold smaller`

But not:

*   neither `bold` nor `smaller`, as one of them must appear.
*   `smaller bold`, as `bold` is juxtaposed and must appear before the `smaller` keyword.
*   `bold smaller bold`, as `bold` and `smaller` may only appear once.

[Bracketed range notation (`[min,max]`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#bracketed_range_notation_minmax)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Some types can accept numeric values within a certain range. For example, the [`column-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-count)
 property can accept an integer value between positive 1 and infinity, inclusive. The corresponding syntax looks like this:

example =   
  <integer \[1,∞\]>    
  
[<integer>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 =   
  <number-token>    

Any value outside this specified range causes the whole declaration to be invalid, therefore the browser will ignore it.

The _bracketed range notation_ `[min, max]` indicates an inclusive range between a `min` and `max` value. This notation is used in numeric type notations and can include units, e.g., `<angle [0,180deg]>`. Positive and negative Infinity (-∞ and ∞) must not have units specified. Types specified in units can have zero values specified with or without units, for example `<time [0s,10s]>` or `<time [0,10s]>`.

Here are some more examples:

*   `<integer [-∞,∞]>`: Any integer from negative infinity to positive infinity.
*   `<integer [0,∞]>`: Any integer from 0 to positive infinity is valid. Negative integers are invalid.
*   `<time [0s,10s]>` or `<time [0,10s]>`: Any duration from 0 to 10 seconds is valid.
*   `<integer [-∞,-1]> | <integer [1,∞]>`: Any integer except zero is valid.

[Summary](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#summary)

--------------------------------------------------------------------------------------------------------------------

| Sign | Name | Description | Example |
| --- | --- | --- | --- |
| Combinators |     |     |     |
|     | Juxtaposition | Components are mandatory and should appear in that order | `solid <length>` |
| `&&` | Double ampersand | Components are mandatory but may appear in any order | `<length> && <string>` |
| `\|` | Double bar | At least one of the components must be present, and they may appear in any order. | `<'border-image-outset'> \| <'border-image-slice'>` |
| `\|` | Single bar | Exactly one of the components must be present | `smaller \| small \| normal \| big \| bigger` |
| `[ ]` | Brackets | Group components to bypass precedence rules | `bold [ thin && <length> ]` |
| Multipliers |     |     |     |
|     | No multiplier | Exactly 1 time | `solid` |
| `*` | Asterisk | 0 or more times | `bold smaller*` |
| `+` | Plus sign | 1 or more times | `bold smaller+` |
| `?` | Question mark | 0 or 1 time (that is _optional)_ | `bold smaller?` |
| `{min,max}` | Curly braces | At least `min` times, at most `max` times | `bold smaller{1,3}` |
| `#` | Hash mark | 1 or more times, with each occurrence separated by a comma (`,`) | `bold smaller#` |
| `!` | Exclamation point | Group must produce at least 1 value | `[ bold? smaller? ]!` |
| Ranges |     |     |     |
| `[min,max]` | Numeric bracketed range | Specifies a numeric range | `<integer [0,∞]>` |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#specifications)

----------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Values and Units Module Level 4  <br>\# value-defs](https://drafts.csswg.org/css-values/#value-defs) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#see_also)

----------------------------------------------------------------------------------------------------------------------

*   CSS key concepts:
    *   [CSS syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Introduction)
        
    *   [Comments](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Comments)
        
    *   [Specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Specificity)
        
    *   [Inheritance](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance)
        
    *   [Box model](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Introduction)
        
    *   [Layout modes](https://developer.mozilla.org/en-US/docs/Glossary/Layout_mode)
        
    *   [Visual formatting model](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Visual_formatting_model)
        
    *   [Margin collapsing](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Margin_collapsing)
        
    *   Values
        *   [Initial values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value)
            
        *   [Computed values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value)
            
        *   [Used values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#used_value)
            
        *   [Actual values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#actual_value)
            
    *   **Value definition syntax**
    *   [Shorthand properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
        
    *   [Replaced elements](https://developer.mozilla.org/en-US/docs/Glossary/Replaced_elements)
        

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Dec 16, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/values_and_units/value_definition_syntax/index.md?plain=1 "Folder: en-us/web/css/guides/values_and_units/value_definition_syntax (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FValues_and_units%2FValue_definition_syntax&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fvalues_and_units%2Fvalue_definition_syntax%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FValues_and_units%2FValue_definition_syntax%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fvalues_and_units%2Fvalue_definition_syntax%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F33094d735e90b4dcae5733331b79c51fee997410%0A*+Document+last+modified%3A+2025-12-16T15%3A14%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")