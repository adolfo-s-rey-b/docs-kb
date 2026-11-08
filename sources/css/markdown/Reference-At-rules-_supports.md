*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports#mdn-search)
    

`@supports` CSS at-rule
=======================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`@supports`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/At-rules)
 lets you specify CSS declarations that depend on a browser's support for CSS features. Using this at-rule is commonly called a _feature query_. The rule must be placed at the top level of your code or nested inside any other conditional group at-rule.

In JavaScript, `@supports` can be accessed via the CSS object model interface [`CSSSupportsRule`](https://developer.mozilla.org/en-US/docs/Web/API/CSSSupportsRule)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports#try_it)

-----------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports#syntax)

-----------------------------------------------------------------------------------------------

The `@supports` at-rule consists of a block of statements with a _supports condition._ The conditions can be combined by conjunctions (`and`), disjunctions (`or`), and/or negations (`not`). The precedence of operators can be defined with parentheses.

Supports conditions can use either a `<property>: <value>` declaration syntax or a `<function()>` syntax. The following sections describe the use of each type of supports condition.

### [Declaration syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports#declaration_syntax)

The declaration syntax checks if a browser supports the specified `<property>: <value>` declaration. The declaration must be surrounded by parentheses. The following example returns true if the browser supports the expression `transform-origin: 5% 5%`:

### [Function syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports#function_syntax)

The function syntax checks if a browser supports values or expressions within the function. The functions supported in the function syntax are described in the following sections.

#### `at-rule()`

This function checks if a browser supports the specified [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/At-rules)
. The following example returns true and applies the contained CSS styles if the browser supports the [`@keyframes`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes)
 at-rule:

#### `selector()`

This function evaluates if a browser supports the specified selector syntax. The following example returns true and applies the contained CSS styles if the browser supports the [child combinator](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Child_combinator)
:

#### `font-tech()`

This function checks if a browser supports the specified font technology for layout and rendering. The following example returns true and applies the contained CSS styles if the browser supports the `COLRv1` font technology:

The table below describes the font technologies (`<font-tech>`), including color font technologies (`<color-font-tech>`), font feature technologies (`<font-features-tech>`), and other available font technologies that can be queried using the `font-tech()` function:

| Technology | Supports |
| --- | --- |
| **`<color-font-tech>`** |     |
| `color-colrv0` | Multi-colored glyphs via COLR version 0 table |
| `color-colrv1` | Multi-colored glyphs via COLR version 1 table |
| `color-svg` | SVG multi-colored tables |
| `color-sbix` | Standard bitmap graphics tables |
| `color-cbdt` | Color bitmap data tables |
| **`<font-features-tech>`** |     |
| `features-opentype` | OpenType `GSUB` and `GPOS` tables |
| `features-aat` | TrueType `morx` and `kerx` tables |
| `features-graphite` | Graphite features, namely `Silf`, `Glat`, `Gloc`, `Feat`, and `Sill` tables |
| **Other `<font-tech>` values** |     |
| `incremental-patch` | Incremental font loading using the patch subset method |
| `incremental-range` | Incremental font loading using the range request method |
| `incremental-auto` | Incremental font loading using method negotiation |
| `variations` | Font variations in TrueType and OpenType fonts to control the font axis, weight, glyphs, etc. |
| `palettes` | Font palettes by means of `font-palette` to select one of many color palettes in the font |

#### `font-format()`

This function checks if a browser supports the specified font format for layout and rendering. The following example returns true and applies the contained CSS styles if the browser supports the `opentype` font format:

The following table describes the available formats (`<font-format>` values) that can be queried with this function:

| Format | Description | File extensions |
| --- | --- | --- |
| `collection` | OpenType Collection | `.otc`, `.ttc` |
| `embedded-opentype` | Embedded OpenType | `.eot` |
| `opentype` | OpenType | `.ttf`, `.otf` |
| `svg` | SVG Font (deprecated) | `.svg`, `.svgz` |
| `truetype` | TrueType | `.ttf` |
| `woff` | WOFF 1.0 (Web Open Font Format) | `.woff` |
| `woff2` | WOFF 2.0 (Web Open Font Format) | `.woff2` |

#### `named-feature()`

This function takes one predefined keyword and evaluates if a browser supports the specified named feature. This is to allow for feature support that cannot be tested for using the other `@supports` functions.

**Note:** More features will be added rarely and only when there is real demand for feature testing something specific that would not be covered by more general testing methods.

[`anchor-position-follows-transforms`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports#anchor-position-follows-transforms)

This `named-feature()` checks if the browser supports transform-aware [anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning)
.

[`single-axis-scroll-container`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports#single-axis-scroll-container)

This `named-feature()` checks if the browser supports the ability to have single-axis scroll containers, where one axis is either [`scroll`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow#scroll)
, or [`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow#auto)
, or [`hidden`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow#hidden)
 and the other is [`clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow#clip)
.

### [The not operator](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports#the_not_operator)

The `not` operator precedes an expression resulting in the negation of the expression. The following returns true if the browser's [`transform-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-origin)
 property considers `10em 10em 10em` **to be invalid:**

As with any operator, the `not` operator can be applied to a declaration of any complexity. The following examples are both valid:

**Note:** There is no need to enclose the `not` operator between two parentheses at the top level. To combine it with other operators, like `and` and `or`, the parentheses are required.

### [The and operator](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports#the_and_operator)

The `and` operator creates a new expression from the conjunction of two shorter expressions. It returns true only if **both** of the shorter expressions are also true. The following example returns true if and only if the two shorter expressions are simultaneously true:

Multiple conjunctions can be juxtaposed without the need of more parentheses. The following are both equivalent:

### [The or operator](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports#the_or_operator)

The `or` operator creates a new expression from the disjunction of two shorter expressions. It returns true if **one or both** of the shorter expressions is also true. The following example returns true if at least one of the two shorter expressions is true:

Multiple disjunctions can be juxtaposed without the need of more parentheses. The following are both equivalent:

**Note:** When using both `and` and `or` operators, the parentheses must be used to define the order in which they apply. Otherwise, the condition is invalid and the whole rule is ignored.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports#formal_syntax)

-------------------------------------------------------------------------------------------------------------

@supports =   
  @supports <supports-condition> { [<rule-list>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/rule-list)
 }    
  
<supports-condition> =   
  not <supports-in-parens>                            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <supports-in-parens> [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 and <supports-in-parens> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[\*](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#asterisk "Asterisk: the entity may occur zero, one or several times")
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <supports-in-parens> [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 or <supports-in-parens> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[\*](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#asterisk "Asterisk: the entity may occur zero, one or several times")
     
  
<supports-in-parens> =   
  ( <supports-condition> )  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <supports-feature>        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <general-enclosed>          
  
<supports-feature> =   
  <supports-selector-fn>       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <supports-font-tech-fn>      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <supports-font-format-fn>    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <supports-at-rule-fn>        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <supports-named-feature-fn>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <supports-env-fn>            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <supports-decl>                
  
<general-enclosed> =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <function-token> <any-value>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 ) [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 ( <any-value>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 ) [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
                   
  
<supports-selector-fn> =   
  selector( <complex-selector> )    
  
<supports-font-tech-fn> =   
  font-tech( <font-tech> )    
  
<supports-font-format-fn> =   
  font-format( <font-format> )    
  
<supports-at-rule-fn> =   
  at-rule( <at-keyword-token> )    
  
<supports-named-feature-fn> =   
  named-feature( [<ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ident)
 )    
  
<supports-env-fn> =   
  env( [<ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ident)
 )    
  
<supports-decl> =   
  ( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <declaration> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <supports-condition-name> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 )    
  
<complex-selector> =   
  <complex-selector-unit> [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <combinator>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 <complex-selector-unit> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[\*](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#asterisk "Asterisk: the entity may occur zero, one or several times")
    
  
<font-tech> =   
  <font-features-tech>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <color-font-tech>     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  variations            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  palettes              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  incremental             
  
<font-format> =   
  [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  collection         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  embedded-opentype  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  opentype           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  svg                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  truetype           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  woff               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  woff2                
  
<complex-selector-unit> =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <compound-selector>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 <pseudo-compound-selector>[\*](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#asterisk "Asterisk: the entity may occur zero, one or several times")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
!    
  
<combinator> =   
  '>'                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  '+'                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  '~'                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 '|' '|' [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 / <wq-name> / [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    
  
<font-features-tech> =   
  features-opentype  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  features-aat       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  features-graphite    
  
<color-font-tech> =   
  color-COLRv0  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  color-COLRv1  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  color-SVG     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  color-sbix    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  color-CBDT      
  
<compound-selector> =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <type-selector>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 <subclass-selector>[\*](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#asterisk "Asterisk: the entity may occur zero, one or several times")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
!    
  
<pseudo-compound-selector> =   
  <pseudo-element-selector> <pseudo-class-selector>[\*](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#asterisk "Asterisk: the entity may occur zero, one or several times")
    
  
<wq-name> =   
  <ns-prefix>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 <ident-token>    
  
<type-selector> =   
  <wq-name>         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <ns-prefix>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 '\*'    
  
<subclass-selector> =   
  <id-selector>            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <class-selector>         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <attribute-selector>     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <pseudo-class-selector>    
  
<pseudo-element-selector> =   
  : <pseudo-class-selector>         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <legacy-pseudo-element-selector>    
  
<pseudo-class-selector> =   
  : <ident-token>                   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  : <function-token> <any-value> )    
  
<ns-prefix> =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <ident-token> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 '\*' [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 '|'    
  
<id-selector> =   
  <hash-token>    
  
<class-selector> =   
  '.' <ident-token> '\*'[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    
  
<attribute-selector> =   
  '\[' <wq-name> '\]'                                   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  '\[' <wq-name> <attr-matcher> [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <string-token> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <ident-token> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <attr-modifier>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 '\]'    
  
<legacy-pseudo-element-selector> =   
  : [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 before [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 after [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 first-line [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 first-letter [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    
  
<attr-matcher> =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 '~' [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 '|' [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 '^' [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 '$' [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 '\*' [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 '='    
  
<attr-modifier> =   
  i  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  s    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports#examples)

---------------------------------------------------------------------------------------------------

### [Testing for the support of a CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports#testing_for_the_support_of_a_css_property)

### [Testing for the support of a given CSS property or a prefixed version](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports#testing_for_the_support_of_a_given_css_property_or_a_prefixed_version)

### [Testing for the non-support of a specific CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports#testing_for_the_non-support_of_a_specific_css_property)

### [Testing for the support of a selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports#testing_for_the_support_of_a_selector)

CSS conditional rules provide the ability to test for the support of a selector such as [`:has()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:has)
.

### [Testing for the support of a font technology](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports#testing_for_the_support_of_a_font_technology)

The following example applies the [Bungee Spice](https://fonts.google.com/specimen/Bungee+Spice "External link (opens in new tab)")
 color font if the browser supports the `COLRv1` font technology:

It's also possible to test for the support of a font technology by using the `tech` function inside the [`@font-face`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face)
 at-rule. In the following example, if a browser doesn't support the color font technology in the [`bungee-spice.woff2`](https://fonts.google.com/specimen/Bungee+Spice "External link (opens in new tab)")
 font, a regular [`bungee.woff2`](https://fonts.google.com/specimen/Bungee "External link (opens in new tab)")
 font will be used instead.

### [Testing for the support of a font format](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports#testing_for_the_support_of_a_font_format)

The following example uses the WOFF2 version of the font if the browser supports this font format, otherwise it falls back to the previously specified WOFF version:

However, a more efficient way to specify multiple font formats is to list them in the `src` descriptor of a single [`@font-face`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face)
 at-rule in the order from the most preferred format to the least preferred:

### [Testing for the support of an at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports#testing_for_the_support_of_an_at-rule)

The following example applies a set of scoped color scheme styles if the browser supports the [`@scope`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@scope)
 at-rule:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports#specifications)

---------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Conditional Rules Module Level 5  <br>\# at-supports-ext](https://drafts.csswg.org/css-conditional-5/#at-supports-ext) |
| [CSS Conditional Rules Module Level 4  <br>\# at-supports-ext](https://drafts.csswg.org/css-conditional-4/#at-supports-ext) |
| [CSS Conditional Rules Module Level 3  <br>\# at-supports](https://drafts.csswg.org/css-conditional-3/#at-supports) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports#see_also)

---------------------------------------------------------------------------------------------------

*   [Using feature queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Conditional_rules/Using_feature_queries)
    
*   [CSS at-rule functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/At-rule_functions)
    
*   [`CSSSupportsRule`](https://developer.mozilla.org/en-US/docs/Web/API/CSSSupportsRule)
    
*   [`CSS.supports()`](https://developer.mozilla.org/en-US/docs/Web/API/CSS/supports_static "CSS.supports()")
     method

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@supports/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@supports (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40supports&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40supports%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40supports%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40supports%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fef4050055cbb6ba03fc245947b47d35252bd2376%0A*+Document+last+modified%3A+2026-09-14T13%3A52%3A50.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")