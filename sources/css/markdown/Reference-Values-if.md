*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/if#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/if#mdn-search)
    

`if()` CSS function
===================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/303)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/if#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/if#browser_compatibility)
 carefully before using this in production.

The **`if()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 allows different values to be set for a property depending on the result of a conditional test. The test can be based on a [style query](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_size_and_style_queries#container_style_queries)
, a [media query](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using)
, or a [feature query](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Conditional_rules/Using_feature_queries)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/if#syntax)

--------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/if#parameters)

The parameter is a semi-colon–separated list of `<if-branch>`es. Each `<if-branch>` is an `<if-condition>` followed by a colon and a `<value>`:

<if-branch> = <if-condition> : <value>;

[`<if-condition>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/if#if-condition)

An `<if-test>` or the `else` keyword.

[`<if-test>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/if#if-test)

A [style query](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_size_and_style_queries#container_style_queries)
, [media query](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using)
, or [feature query](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Conditional_rules/Using_feature_queries)
.

[`else`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/if#else)

A keyword representing an `<if-condition>` that always evaluates to true.

[`<value>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/if#value)

A property value.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/if#return_value)

A value or [guaranteed-invalid](https://developer.mozilla.org/en-US/docs/Glossary/guaranteed_invalid_value)
.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/if#description)

------------------------------------------------------------------------------------------------

The CSS `if()` function provides conditional logic to CSS property values, and works in a similar fashion to JavaScript [`if...else`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else)
 statements.

The `if()` function can be used inside the value of any property, and can contain zero or more semi-colon-separated `<if-condition>`s. Each `<if-condition>` is either an `<if-test> : <value>` pair or an `else : <value>` pair. The semi-colon after the last `<if-condition>` is optional.

The return value is calculated as follows:

1.  The `<if-condition>` expressions are evaluated, in the order they appear in the function.
2.  The first `<if-condition>` that evaluates to `true` has its associated `<value>` returned.
3.  If no `<if-condition>` evaluates to `true`, the function returns a [<guaranteed-invalid>:](https://developer.mozilla.org/en-US/docs/Glossary/guaranteed_invalid_value)
    . This behaves as invalid or `false` if the `if()` function is used in a value statement that has a fallback, such as a [custom property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/--*)
     or an [`anchor()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor)
     function.

For example:

In this case, we are setting a different [`linear-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient)
 as the [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
 on [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 elements, depending on whether a `--scheme` [custom property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/--*)
 is set to `ice` or `fire`. If `--scheme` doesn't exist, or it exists and is set to any other value, the `else` value comes into play, and the `background-image` property is set to `none`.

**Note:** Each condition must be separated from its associated value with a colon, and each `<if-condition> : <value>` pair must be separated with a semi-colon. The semi-colon is optional for the last `<if-condition> : <value>` pair.

**Warning:** There must be no space between the `if` and the opening parenthesis (`(`). If there is, the whole declaration is invalid.

If a single `<if-condition>` or `<value>` is invalid, it does not invalidate the entire `if()` function; instead, the parser moves on to the next `<if-condition> : <value>` pair. If no `<if-condition>` nor `<value>` is valid, the function returns [guaranteed-invalid](https://developer.mozilla.org/en-US/docs/Glossary/guaranteed_invalid_value)
.

### [Frequency and position of `else : <value>` pairs](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/if#frequency_and_position_of_else_value_pairs)

You can include multiple `else : <value>` pairs inside an `if()` function, in any position. However, in most cases, a single `else : <value>` pair at the end of the semi-colon-separated list is used to provide the default value that is always returned if none of the `<if-test>`s evaluate to true.

If you include an `else : <value>` pair before any `<if-test> : <value>` pairs, the conditions that follow it are not evaluated because `else` always evaluates to `true`. The following `if()` therefore always returns `none`, and the two `<if-test> : <value>` pairs are never evaluated:

Debugging a value that is not behaving as expected is one case where you might want to put an `else : <value>` in a position other than the end of the value list. In the following example, we are trying to work out whether the first `<if-test> : <value>` pair is working properly. If it isn't, the `else : <value>` pair returns a value of `url("debug.png")` to display an image indicating that the first `<if-test> : <value>` pair needs fixing. The last two `<if-test> : <value>` pairs are again never evaluated.

Note that an `if()` function is still valid if it contains only an `else : <value>` pair, or nothing at all. The following property values are both valid:

These functions are not useful. They were included to demonstrate their validity. In this case, the [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
 value will always be set to `yellow` and the `background-image` will be set to its initial value. You would be better off setting the `background-color` directly to `yellow`, and the `background-image` to `initial` or `none`.

### [Types of if-tests](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/if#types_of_if-tests)

An `<if-test>` accepts one of three query types. This section looks at each one in detail.

#### Style queries

A [style query](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_size_and_style_queries#container_style_queries)
 `<if-test>` allows you to test whether a particular property value is set on an element, and apply a value to a different property as a result. We walked through several style query examples earlier on; let's look at another example:

If the `--scheme` custom property is set to a value of `ice` on the same element, the provided `linear-gradient()` value is returned. If not, then `none` is returned.

Using style queries inside `if()` statements has an advantage over [`@container`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container)
 queries — you can target an element with styles directly, based on whether a custom property is set on it, rather than having to check set styles on a container parent element.

You can also use `and`, `or`, or `not` logic inside style queries. For example:

A `@container` query does have some advantages — you can only set single property values at a time with `if()` style queries, whereas `@container` queries can be used to conditionally apply whole sets of rules. The two approaches are complementary, and have different uses.

Note that container style queries currently don't support regular CSS properties, just CSS custom properties. For example, the following won't work:

#### Media queries

A [media query](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using)
 `<if-test>` can be used to set a value for a property depending on whether a media query test returns true.

You can use media types. For example, the following `<if-test> : <value>` pair returns a value of `white` on print media, while the `else` clause causes `#eeeeee` to be returned on non-print media.

You can also use media features — the following returns a value of `0 auto` if the current viewport width is less than `700px`, or `20px auto` if this is not the case:

This is really useful when you need to vary a single property value based on a media query result.

You can also use `and`, `or`, or `not` logic inside media queries. For example:

When you want to set multiple declarations or rules based on one media query, a regular [`@media`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
 construct is needed. The two approaches are complementary, and have different uses.

#### Feature queries

A [feature query](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Conditional_rules/Using_feature_queries)
 `<if-test>` can be used to set a value for a property depending on whether the browser supports a particular property value.

For example, the following returns an [`lch()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/lch)
 color if `lch()` colors are supported, or an [`rgb()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/rgb)
 color if not:

Selector support queries also work. The following will return a value of `1em` if the browser supports the [`:buffering`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:buffering)
 pseudo-class, or `initial` if not:

You can also use `and`, `or`, or `not` logic inside feature queries. For example:

Feature queries are really useful inside `if()` statements when you need to vary a single property value based on support for a particular value or a separate property. When you want to set multiple declarations or rules based on one feature query, a regular [`@supports`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports)
 construct is better. The two approaches are complementary, and have different uses.

### [Providing fallback values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/if#providing_fallback_values)

The `if()` statement does not gracefully degrade; an explicit fallback needs to be provided for non-supporting browsers.

For example, in this case we provide a static [`padding`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding)
 value for browsers that don't support `if()`. Browsers that support `if()` will override the first declaration with the second one, which sets different padding values depending on whether or not the `--size: "2xl"` custom property is set.

**Note:** Remember to include the `else` condition. In `if()`\-supporting browsers, if no `else` value were included and `--size` was not equal to `"2xl"`, the padding would be set to `initial`.

### [Whole and partial values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/if#whole_and_partial_values)

An `if()` function can be set as the value of any CSS property, but it can also be used to determine parts of property values. For example, the following sets a different [`border-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-color)
 inside a [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
 shorthand property, depending on whether [`lch()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/lch)
 colors are supported:

However, we could use the `if()` function to determine the [`border-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-color)
 component only:

### [Nesting if() functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/if#nesting_if_functions)

Because an `if()` function can take the place of whole property values or individual components, it is possible to nest `if()` functions within other `if()` functions, and inside other functions such as [`calc()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc)
.

For example, in this declaration we are using `if()` to set a `color` property value depending on various conditions. We have an outer `if()` function that returns a particular value depending on whether the `--scheme` custom property is set to `ice` or `fire` (with an `else` value of `black` that is returned if neither of the conditions return true).

However, the two `<value>`s are also `if()` functions. These inner `if()` functions return a light color value if the user prefers a dark color scheme (determined using the [`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-color-scheme)
 media query), and a dark color value otherwise.

In the next example, we set the `width` property equal to a `calc()` function that subtracts `50px` from a percentage of the parent element's width. The percentage is represented by an `if()` function, which test whether the `--scheme: wide` custom property is set. If so, the percentage is `70%`, so the outer function resolves to `calc(70% - 50px)`. If not, the percentage is `50%`, so the outer function resolves to `calc(50% - 50px)`.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/if#formal_syntax)

----------------------------------------------------------------------------------------------------

<if()> =   
  if( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <if-branch> ; [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[\*](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#asterisk "Asterisk: the entity may occur zero, one or several times")
 <if-branch> ;[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
<if-branch> =   
  <if-condition> : <declaration-value>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    
  
<if-condition> =   
  <if-test>\]>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  else                         
  
<if-test> =   
  supports( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ident)\
 : <declaration-value> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <supports-condition> )                       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  media( <media-feature>                       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <media-condition> )                          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  style( <style-query> )                         
  
<supports-condition> =   
  not <supports-in-parens>                            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <supports-in-parens> [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 and <supports-in-parens> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[\*](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#asterisk "Asterisk: the entity may occur zero, one or several times")
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <supports-in-parens> [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 or <supports-in-parens> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[\*](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#asterisk "Asterisk: the entity may occur zero, one or several times")
     
  
<media-feature> =   
  <mf-plain>    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <mf-boolean>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <mf-range>      
  
<media-condition> =   
  <media-not>                                       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <media-in-parens> [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <media-and>[\*](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#asterisk "Asterisk: the entity may occur zero, one or several times")\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <media-or>[\*](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#asterisk "Asterisk: the entity may occur zero, one or several times")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    
  
<style-query> =   
  not <style-in-parens>                               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <style-in-parens> [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 and <style-in-parens> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
[\*](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#asterisk "Asterisk: the entity may occur zero, one or several times")\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 or <style-in-parens> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
[\*](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#asterisk "Asterisk: the entity may occur zero, one or several times")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <style-feature>                                       
  
<supports-in-parens> =   
  ( <supports-condition> )  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <supports-feature>        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <general-enclosed>          
  
<mf-plain> =   
  <mf-name> : <mf-value>    
  
<mf-boolean> =   
  <mf-name>    
  
<mf-range> =   
  <mf-name> <mf-comparison> <mf-value>             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <mf-value> <mf-comparison> <mf-name>             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <mf-value> <mf-lt> <mf-name> <mf-lt> <mf-value>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <mf-value> <mf-gt> <mf-name> <mf-gt> <mf-value>    
  
<media-not> =   
  not <media-in-parens>    
  
<media-in-parens> =   
  ( <media-condition> )  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ( <media-feature> )    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <general-enclosed>       
  
<media-and> =   
  and <media-in-parens>    
  
<media-or> =   
  or <media-in-parens>    
  
<style-in-parens> =   
  ( <style-query> )    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ( <style-feature> )  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <general-enclosed>     
  
<style-feature> =   
  <style-feature-plain>    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <style-feature-boolean>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <style-range>              
  
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
                   
  
<mf-name> =   
  [<ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ident)
    
  
<mf-value> =   
  [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<dimension>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dimension)
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ident)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <ratio>        
  
<mf-comparison> =   
  <mf-lt>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <mf-gt>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <mf-eq>    
  
<mf-lt> =   
  '<' '='[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    
  
<mf-gt> =   
  '>' '='[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    
  
<style-feature-plain> =   
  <style-feature-name> : <style-feature-value>    
  
<style-feature-boolean> =   
  <style-feature-name>    
  
<style-range> =   
  <style-range-value> <mf-comparison> <style-range-value>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <style-range-value> <mf-lt> <style-range-value> <mf-lt> <style-range-value>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <style-range-value> <mf-gt> <style-range-value> <mf-gt> <style-range-value>    
  
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
  
[<ratio>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ratio)
 =   
  [<number \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 / [<number \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    
  
<mf-eq> =   
  '='    
  
<style-range-value> =   
  <custom-property-name>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <style-feature-value>     
  
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

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/if#examples)

------------------------------------------------------------------------------------------

### [Basic `if()` usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/if#basic_if_usage)

In this example, we'll show basic usage of each of the three types of `<if-test>`.

#### HTML

Our HTML features a [`<section>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section)
 element with two [`<article>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/article)
 elements inside it, containing `<h2>` [headings](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
. The `<section>` has a custom property set on it inside its [`style`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/style)
 attribute — `--show-apple:true` — which we use later on to conditionally set a property value.

#### CSS

In our CSS, we first target the `<section>` element, laying it out with [flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
 and setting a [`gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/gap)
 between the two child `<article>` elements. We then use an `if()` function with an [`orientation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/orientation)
 media query `<if-test>` to set the value of the [`flex-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction)
 property to `row` if the document is in landscape orientation, or `column` if it is in portrait orientation. This lays out the `article` elements side-by-side in wide screens, and top-to-bottom in narrow screens.

Next, we target the `<h2>` element's [`::before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::before)
 pseudo-element, setting its [`content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content)
 property to an apple emoji, but only if `--show-apple: true` is set (we did this earlier with an inline [`<style>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/style)
 in our HTML). We achieve this using an `if()` function with a [style query](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_size_and_style_queries#style_queries_for_custom_properties)
 `<if-test>`:

Finally, we target the `<h2>` element itself. We use a feature query `<if-test>` to test whether the browser supports `lch()` colors, and set the [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
 property to an `lch()` color if so, or a hex equivalent if not.

#### Result

Note how the styling is applied. Test out the conditional styling for the first two `if()` queries by modifying the rendered demo using your browser's devtools:

*   Remove the `<section>` element's `style` attribute and note how the apple emojis are no longer rendered.
*   Change the `height` attribute of the embedding `<iframe>` to `1200px`. This will change the orientation from landscape to portrait. Note how the layout changes as a result.

### [Controlling a color scheme with `if()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/if#controlling_a_color_scheme_with_if)

This demo shows how you can start to have some real fun with CSS `if()` functions. Among other things, we use `if()` functions to conditionally set the values of some custom properties, enabling us to control the entire color scheme!

#### HTML

Our HTML contains an [`<article>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/article)
 element with some content inside it — a top-level heading, a couple of [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
 elements, and an [`<aside>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/aside)
. We also include a [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
 containing a [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
 drop-down that enables selecting a color scheme.

html

    <article>
      <h1>Main heading</h1>
      <p>
        Lorem ipsum dolor sit amet consectetur adipiscing elit.
        Quisque faucibus ex sapien vitae pellentesque sem placerat.
        In id cursus mi pretium tellus duis convallis.
      </p>
      <aside>
        <h2>An aside</h2>
        <p>
          Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus
          fringilla lacus nec metus bibendum egestas.
        </p>
      </aside>
      <p>
        Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut
        hendrerit semper vel class aptent taciti sociosqu. Ad litora
        torquent per conubia nostra inceptos himenaeos.
      </p>
    </article>
    <form>
      <label for="scheme">Choose color scheme:</label>
      <select id="scheme">
        <option value="">Default</option>
        <option value="ice">Ice</option>
        <option value="fire">Fire</option>
      </select>
    </form>
    

### [JavaScript](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/if#javascript)

Our JavaScript adds a [`change`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event)
 event listener to the `<select>` element. When a new value is selected, our script sets the `<article>` element's [`class`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/class)
 attribute to equal that value.

js

    const articleElem = document.querySelector("article");
    const selectElem = document.querySelector("select");
    
    selectElem.addEventListener("change", () => {
      articleElem.className = selectElem.value;
    });
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/if#css_2)

In our CSS, we give the `<body>` element a [`max-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-width)
 of `700px` and center it using `auto` [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
 values. However, we use an `if()` function with a media query `<if-test>` to set the [`margin-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-top)
 component inside the `margin` shorthand to `0` if the viewport's width is less than `700px`, and `20px` if it is wider. This means that on wide screens we get a bit of margin at the top of the content, but this is removed on narrow screens, where it looks a bit weird.

    * {
      box-sizing: border-box;
    }
    
    html {
      font-family: "Helvetica", "Arial", sans-serif;
    }
    
    p {
      line-height: 1.5;
    }
    
    form {
      padding-left: 20px;
      margin-top: 20px;
    }
    
    article h2 {
      margin: 0;
      font-size: 1.8rem;
    }
    

css

    body {
      max-width: 700px;
      margin: if(
        media(width < 700px): 0;
        else: 20px;
      ) auto 0;
    }
    

We then set the `--scheme` custom property to match the `<article>` element's `class` name. The class will be set by our JavaScript when a new value is selected in our `<select>` element. You'll see the significance of the custom element value in the next CSS block.

css

    .ice {
      --scheme: ice;
    }
    
    .fire {
      --scheme: fire;
    }
    

We can see the real power of CSS `if()` functions when we combine them with custom properties. Here we use `if()` functions to set our `--color1` and `--color2` custom properties to different color values depending on the value of the `--scheme` custom property. We then use the `--color1` and `--color2` values in our `<article>` element's [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
, [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
, and [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
 properties, and our `<aside>` element's `color` and `background-color` properties.

We are controlling our entire color scheme via custom properties, with different values set via `if()` functions.

css

    article {
      padding: 20px;
      --color1: if(
        style(--scheme: ice): #03045e;
        style(--scheme: fire): #621708;
        else: black;
      );
      --color2: if(
        style(--scheme: ice): #caf0f8;
        style(--scheme: fire): #ffc971;
        else: white;
      );
    
      color: var(--color1);
      border: 3px solid var(--color1);
      background-image: linear-gradient(
        to left,
        var(--color2),
        white,
        var(--color2)
      );
    }
    
    aside {
      color: var(--color2);
      background-color: var(--color1);
      padding: 20px;
    }
    

Finally, we use `if()` functions in a couple more places:

*   We set our `<h1>` element's [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
     to be `calc(3rem + 2vw)` if the viewport is wider than `700px`, and `3rem` otherwise. This means the font size updates dynamically with viewport width changes on wider screens, but stays the same on narrow screens.
*   We set a suitable emoji as the [`content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content)
     of our `<h1>` element's [`::before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::before)
     pseudo-class, depending on the value of the `--scheme` custom property.

css

    h1 {
      margin: 0;
      font-size: if(
        media(width > 700px): calc(3rem + 2vw);
        else: 3rem;
      );
    }
    
    h1::before {
      content: if(
        style(--scheme: ice): "❄️ ";
        style(--scheme: fire): "🔥 ";
        else: "";
      );
    }
    

#### Result

This demo renders as follows:

Try selecting different color scheme values to see the effect on the look and feel.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/if#specifications)

------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Values and Units Module Level 5  <br>\# if-notation](https://drafts.csswg.org/css-values-5/#if-notation) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/if#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/if#see_also)

------------------------------------------------------------------------------------------

*   [Container style queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_size_and_style_queries#container_style_queries)
    
*   [Media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using)
    
*   [Feature queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Conditional_rules/Using_feature_queries)
    
*   [CSS values and units module](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 4, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/if/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/if/index.md?plain=1 "Folder: en-us/web/css/reference/values/if (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fif&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fif%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fif%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fif%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff0179562ad8e2a4dd1f0916c529792198d7e06b2%0A*+Document+last+modified%3A+2026-09-04T18%3A21%3A18.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")