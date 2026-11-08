*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dynamic-range-limit-mix#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dynamic-range-limit-mix#mdn-search)
    

`dynamic-range-limit-mix()` CSS function
========================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/553)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dynamic-range-limit-mix#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dynamic-range-limit-mix#browser_compatibility)
 carefully before using this in production.

The **`dynamic-range-limit-mix()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 creates a custom maximum luminance limit by mixing different [`dynamic-range-limit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dynamic-range-limit)
 keywords in specified amounts.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dynamic-range-limit-mix#syntax)

-----------------------------------------------------------------------------------------------------------

css

    dynamic-range-limit-mix(standard 70%, no-limit 30%);
    dynamic-range-limit-mix(no-limit 10%, constrained 20%);
    dynamic-range-limit-mix(no-limit 30%, constrained 30%, standard 30%);
    dynamic-range-limit-mix(
        no-limit 20%,
        dynamic-range-limit-mix(standard 25%, constrained 75%) 20%
    )
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dynamic-range-limit-mix#parameters)

[`dynamic-range-limit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dynamic-range-limit)
 [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)

A pair consisting of a `dynamic-range-limit` value (which can be another `dynamic-range-limit-mix()` function) and a `<percentage>` between `0%` and `100%` (inclusive). The `<percentage>` specifies the proportion of a `dynamic-range-limit` keyword value in the custom limit. The `dynamic-range-limit-mix()` function can take two or more of these pairs as parameters.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dynamic-range-limit-mix#return_value)

A custom maximum luminance limit, expressed as a number of photographic stops higher than the HDR reference white. For privacy reasons, the actual calculated result is not exposed.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dynamic-range-limit-mix#description)

---------------------------------------------------------------------------------------------------------------------

The [`dynamic-range-limit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dynamic-range-limit)
 property allows you to control the brightness of High Dynamic Range (HDR) content. The `dynamic-range-limit-mix()` function can be provided as a value of `dynamic-range-limit`, and enables you to create custom brightness limits by mixing together percentages of the `dynamic-range-limit` keyword values.

### [Calculating the percentages](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dynamic-range-limit-mix#calculating_the_percentages)

When the given percentages add up to `100%`, the result is obvious:

css

    /* standard 70%, no-limit 30% */
    dynamic-range-limit-mix(standard 70%, no-limit 30%);
    

When the given percentages do not add up to `100%`, the resulting percentages are equal to the given percentages expressed proportionately to one another so the total equals `100%`:

css

    /* no-limit 40%, constrained 60% */
    dynamic-range-limit-mix(no-limit 20%, constrained 30%);
    
    /* no-limit 20%, constrained 40%, standard 40% */
    dynamic-range-limit-mix(no-limit 40%, constrained 80%, standard 80%);
    

If a `dynamic-range-limit` keyword value is used more than once, the percentages for that keyword value are added together to get the total percentage:

css

    /* constrained 70%, standard 30% */
    dynamic-range-limit-mix(constrained 40%, standard 30%, constrained 30%);
    
    /* no-limit 40%, constrained 60% */
    dynamic-range-limit-mix(no-limit 10%, constrained 30%, no-limit 10%);
    

If a specified percentage is less than `0%` or greater than `100%`, the `dynamic-range-limit-mix()` function — and therefore the associated `dynamic-range-limit` property value — is invalid. If a keyword is used more than once and the cumulative percentage is more than `100%`, the value is valid, and the proportion rules described above come into play.

### [Nesting `dynamic-range-limit-mix()` functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dynamic-range-limit-mix#nesting_dynamic-range-limit-mix_functions)

You can nest `dynamic-range-limit-mix()` functions inside one another. When doing so, the same rules explained earlier apply, and each set of percentages is calculated separately and then added. In the following example:

css

    dynamic-range-limit-mix(
        no-limit 10%,
        dynamic-range-limit-mix(standard 25%, constrained 75%) 20%,
        dynamic-range-limit-mix(constrained 10%, no-limit 30%) 20%
    )
    

*   The first line gives us `no-limit 10%`.
*   Since `25%` and `75%` add up to `100%`, the second line gives us `standard 5%` (`25%` of `20%`) and `constrained 15%` (`75%` of `20%`).
*   In the third line, because `10%` and `30%` add up to only `40%`, not `100%`, we normalize both as proportions of `40%`: 10/40 = `25%` and 30/40 = `75%`. This gives us `constrained 5%` (`25%` of `20%`) and `no-limit 15%` (`75%` of `20%`).

Adding these up to get the raw percentages gives us:

css

    dynamic-range-limit-mix(standard 5%, constrained 20%, no-limit 25%)
    

The above percentages add up to `50%`, so they need to be doubled to get the final percentages. The computed value is therefore:

css

    dynamic-range-limit-mix(standard 10%, constrained 40%, no-limit 50%)
    

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dynamic-range-limit-mix#formal_syntax)

-------------------------------------------------------------------------------------------------------------------------

<dynamic-range-limit-mix()> =   
  dynamic-range-limit-mix( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<'dynamic-range-limit'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dynamic-range-limit)\
 [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")\
 [<percentage \[0,100\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
 )    
  
[<dynamic-range-limit>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dynamic-range-limit)
 =   
  standard                     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  no-limit                     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  constrained                  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<dynamic-range-limit-mix()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dynamic-range-limit-mix)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dynamic-range-limit-mix#examples)

---------------------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dynamic-range-limit-mix#basic_usage)

Consider an [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
 element being used to embed an HDR image on a web page:

html

    <img src="my-hdr-image.jpg" alt="my image" />
    

On HDR displays, the brightest areas of the image could prove to be jarring and uncomfortable to look at. To solve this problem, we could set the image's `dynamic-range-limit` property to `dynamic-range-limit-mix(standard 70%, no-limit 30%)`, which gives it a maximum luminance limit of only slightly brighter than HDR reference white:

css

    img {
      dynamic-range-limit: dynamic-range-limit-mix(standard 70%, no-limit 30%);
    }
    

You can see the `dynamic-range-limit` property in action in our [dynamic-range-limit property demo](https://github.com/mdn/dom-examples/tree/main/dynamic-range-limit "External link (opens in new tab)")
, which includes an HDR image that can be hovered and focused to transition the `dynamic-range-limit` value. [View the example live](https://mdn.github.io/dom-examples/dynamic-range-limit/ "External link (opens in new tab)")
 in a display capable of displaying HDR colors, and try it out.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dynamic-range-limit-mix#specifications)

---------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Color HDR Module Level 1  <br>\# funcdef-dynamic-range-limit-mix](https://drafts.csswg.org/css-color-hdr/#funcdef-dynamic-range-limit-mix) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dynamic-range-limit-mix#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dynamic-range-limit-mix#see_also)

---------------------------------------------------------------------------------------------------------------

*   [`dynamic-range-limit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dynamic-range-limit)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 18, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dynamic-range-limit-mix/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/dynamic-range-limit-mix/index.md?plain=1 "Folder: en-us/web/css/reference/values/dynamic-range-limit-mix (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fdynamic-range-limit-mix&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fdynamic-range-limit-mix%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fdynamic-range-limit-mix%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fdynamic-range-limit-mix%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb760560abe30bd69ca968dac38528102f423b5ea%0A*+Document+last+modified%3A+2026-04-18T06%3A09%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")