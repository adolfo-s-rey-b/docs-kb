*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Introduction#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Introduction#mdn-search)
    

Introduction to CSS syntax: declarations, rulesets, and statements
==================================================================

The basic goal of the Cascading Stylesheet ([CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
) language is to allow a browser engine to paint elements of the page with specific features, like colors, positioning, or decorations. The _CSS syntax_ reflects this goal and its basic building blocks are:

*   The **property** which is an identifier, that is a human-readable _name_, that defines which feature is considered.
*   The **value** which describe how the feature must be handled by the engine. Each property has a set of valid values, defined by a formal grammar, as well as a semantic meaning, implemented by the browser engine.

[CSS declarations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Introduction#css_declarations)

-----------------------------------------------------------------------------------------------------------------

Setting CSS properties to specific values is the core function of the CSS language. A property and value pair is called a **declaration**, and any CSS engine calculates which declarations apply to every single element of a page in order to appropriately lay it out, and to style it.

Both properties and values are case-insensitive by default in CSS. The pair is separated by a colon, `:` (U+003A COLON), and white spaces before, between, and after properties and values, but not necessarily inside, are ignored.

![A css declaration is a property value pair, with a colon separating the two entities and a semi-colon closing the declaration.](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Introduction/css_syntax_-_declaration.png)

There are [hundreds of different properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference)
 in CSS and a practically endless number of different values. Not all pairs of properties and values are allowed and each property defines what are the valid values. When a value is not valid for a given property, the declaration is deemed _invalid_ and is wholly ignored by the CSS engine.

[CSS declaration blocks](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Introduction#css_declaration_blocks)

-----------------------------------------------------------------------------------------------------------------------------

Declarations are grouped in **blocks**, that is in a structure delimited by an opening brace, `{` (U+007B LEFT CURLY BRACKET), and a closing one, `}` (U+007D RIGHT CURLY BRACKET). Blocks sometimes can be nested, so opening and closing braces must be matched.

![Two braces delimit the start and end of a CSS block, with css content or no content between the braces.](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Introduction/css_syntax_-_block.png)

Such blocks are naturally called **declaration blocks** and declarations inside them are separated by a semicolon, `;` (U+003B SEMICOLON). A declaration block may be empty, that is containing null declaration. White spaces around declarations are ignored. The last declaration of a block doesn't need to be terminated by a semicolon, though it is often considered _good style_ to do it as it prevents forgetting to add it when extending the block with another declaration.

A CSS declaration block is visualized in the diagram below.

![Within a CSS block, encompassed in braces, semicolons separate declarations, with the final semicolon being optional but recommended as good practice.](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Introduction/declaration-block.png)

**Note:** The content of a CSS declaration block, that is a list of semicolon-separated declarations, without the initial and closing braces, can be put inside an HTML [`style`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/style)
 attribute.

[CSS rulesets](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Introduction#css_rulesets)

---------------------------------------------------------------------------------------------------------

If style sheets could only apply a declaration to each element of a Web page, they would be pretty useless. The real goal is to apply different declarations to different parts of the document.

CSS allows this by associating conditions with declarations blocks. Each (valid) declaration block is preceded by one or more comma-separated [**selectors**](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors)
, which are conditions selecting some elements of the page. A [selector list](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Selector_list)
 and an associated declarations block, together, are called a **ruleset**, or often a **rule**.

A CSS ruleset (or rule) is visualized in the diagram below.

![A group of comma-separated selectors precedes the brace-delimited declaration block, which contains multiple declarations ending in semicolons.](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Introduction/ruleset.png)

As an element of the page may be matched by several selectors, and therefore by several rules potentially containing a given property several times, with different values, the CSS standard defines which one has precedence over the other and must be applied: this is called the cascade algorithm (see [Handling conflicts](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Handling_conflicts)
).

**Note:** It is important to note that even if a ruleset characterized by a group of selectors is a kind of shorthand replacing rulesets with a single selector each, this doesn't apply to the validity of the ruleset itself.

This leads to an important consequence: if one single basic selector is invalid, like when using an unknown pseudo-element or pseudo-class, the whole _selector_ is invalid and therefore the entire rule is ignored (as invalid too).

[CSS statements](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Introduction#css_statements)

-------------------------------------------------------------------------------------------------------------

Rulesets are the main building blocks of a style sheet, which often consists of only a big list of them. But there is other information that a Web author wants to convey in the style sheet, like the character set, other external style sheets to import, font face or list counter descriptions and many more. It will use other and specific kinds of statements to do that.

A **statement** is a building block that begins with any non-space characters and ends at the first closing brace or semicolon (outside a string, non-escaped and not included into another {}, () or \[\] pair).

![A Venn diagram of statements noting all rulesets are nested statements, while some at-rules are nested statements but most aren't. Anything that is not an at-rule or nested is invalid.](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Introduction/css_syntax_-_statements_venn_diag.png)

There are two kinds of statements:

*   **Rulesets** (or _rules_) that, as seen, associate a collection of CSS declarations to a condition described by a [selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors)
    .
*   **At-rules** that start with an at sign, `@` (U+0040 COMMERCIAL AT), followed by an identifier and then continuing up to the end of the statement, that is up to the next semicolon (;) outside of a block, or the end of the next block. Each type of [at-rules](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/At-rules)
    , defined by the identifier, may have its own internal syntax, and semantics of course. They are used to convey meta-data information (like [`@layer`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@layer)
     or [`@import`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@import)
    ), conditional information (like [`@media`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
     or [`@document`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@document)
    ), or descriptive information (like [`@font-face`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face)
    ).

Any statement which isn't a ruleset or an at-rule is invalid and ignored.

### [Nested statements](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Introduction#nested_statements)

There is another group of statements – the **nested statements**. These are statements that can be used in a specific subset of at-rules – the _conditional group rules_. These statements only apply if a specific condition is matched: the `@media` at-rule content is applied only if the device on which the browser runs matches the expressed condition; the `@document` at-rule content is applied only if the current page matches some conditions, and so on. In CSS1 and CSS2.1, only _rulesets_ could be used inside conditional group rules. That was very restrictive and this restriction was lifted in [_CSS Conditionals Level 3_](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Conditional_rules)
. Now, though still experimental and not supported by every browser, conditional group rules can contain a wider range of content: rulesets but also some, but not all, at-rules.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Introduction#see_also)

-------------------------------------------------------------------------------------------------

*   [CSS syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax)
     module
*   [Selectors and combinators](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors/Selectors_and_combinators)
    
*   [Selector structure](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors/Selector_structure)
    
*   [Error handling](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Error_handling)
    
*   [Specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Specificity)
    
*   [Inheritance](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance)
    
*   [Cascade](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Introduction)
    
*   [Value definition syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax)
    
*   Values
    *   [Initial values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value)
        
    *   [Computed values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value)
        
    *   [Used values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#used_value)
        
    *   [Actual values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#actual_value)
        
*   [Shorthand properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Introduction/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/syntax/introduction/index.md?plain=1 "Folder: en-us/web/css/guides/syntax/introduction (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FSyntax%2FIntroduction&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fsyntax%2Fintroduction%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FSyntax%2FIntroduction%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fsyntax%2Fintroduction%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")