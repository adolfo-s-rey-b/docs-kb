*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes#mdn-search)
    

`@keyframes` CSS at-rule
========================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`@keyframes`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/At-rules)
 controls the intermediate steps in a CSS animation sequence by defining styles for keyframes (or waypoints) along the animation sequence. This gives more control over the intermediate steps of the animation sequence than [transitions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transitions)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes#syntax)

------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes#values)

[`<keyframes-name>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes#keyframes-name)

A case-sensitive [`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
 or string naming the keyframe list.

[`from`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes#from)

Equivalent to the value `0%`.

[`to`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes#to)

Equivalent to the value `100%`.

[`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)

A percentage through the animation sequence at which the specified keyframe should occur.

[`<timeline-range-name>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name)
 [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)

A percentage through the specified [`animation-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range)
 at which the specified keyframe should occur.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes#description)

----------------------------------------------------------------------------------------------------------

To use keyframes, create a `@keyframes` rule with a name that is then used by the [`animation-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-name)
 property to match an animation to its keyframe declaration. Each `@keyframes` rule contains a style list of [keyframe selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Keyframe_selectors)
, which specify percentages along the animation when the keyframe occurs, and a block containing the styles for that keyframe.

You can list the keyframe percentages in any order; they will be handled in the order they should occur.

JavaScript can access the `@keyframes` at-rule with the CSS object model interface [`CSSKeyframesRule`](https://developer.mozilla.org/en-US/docs/Web/API/CSSKeyframesRule)
.

### [Valid keyframe lists](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes#valid_keyframe_lists)

If a keyframe rule doesn't specify the start or end states of the animation (that is, `0%`/`from` and `100%`/`to`), browsers will use the element's existing styles for the start/end states. This can be used to animate an element from its initial state and back.

Properties that can't be animated in keyframe rules are ignored, but supported properties will still be animated.

### [Resolving duplicates](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes#resolving_duplicates)

If multiple keyframe sets exist for a given name, the last one encountered by the parser is used. `@keyframes` rules don't cascade, so animations never derive keyframes from more than one rule set.

If a given animation time offset is duplicated, all keyframes in the `@keyframes` rule for that percentage are used for that frame. There is cascading within a `@keyframes` rule if multiple keyframes specify the same percentage values.

### [When properties are left out of some keyframes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes#when_properties_are_left_out_of_some_keyframes)

Properties that aren't specified in every keyframe are interpolated if possible — properties that can't be interpolated are dropped from the animation. For example:

Here, the [`top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/top)
 property animates using the `0%`, `30%`, and `100%` keyframes, and [`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/left)
 animates using the `0%`, `68%`, `72%` and `100%` keyframes.

### [When a keyframe is defined multiple times](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes#when_a_keyframe_is_defined_multiple_times)

If a keyframe is defined multiple times but not all affected properties are in each keyframe, all values specified in these keyframes are considered. For example:

In this example, at the `50%` keyframe, the values used are `top: 10px` and `left: 20px`.

### [`!important` in a keyframe](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes#!important_in_a_keyframe)

Declarations in a keyframe qualified with the [`important`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/important)
 flag set are ignored.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes#formal_syntax)

--------------------------------------------------------------------------------------------------------------

@keyframes =   
  @keyframes <keyframes-name> { <qualified-rule-list> }    
  
<keyframes-name> =   
  [<custom-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
          

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes#examples)

----------------------------------------------------------------------------------------------------

### [CSS animation examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes#css_animation_examples)

See [Using CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Using)
 and [scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines)
 for examples.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes#specifications)

----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Animations Level 1  <br>\# keyframes](https://drafts.csswg.org/css-animations/#keyframes) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes#see_also)

----------------------------------------------------------------------------------------------------

*   [`animation-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-name)
    
*   [Using CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Using)
    
*   [CSS scroll-driven animation timelines](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines)
    
*   [Understanding timeline range names](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timeline_range_names)
    
*   [CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations)
     module
*   [CSS scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations)
     module
*   [`AnimationEvent`](https://developer.mozilla.org/en-US/docs/Web/API/AnimationEvent)
    
*   [Animate elements on scroll with Scroll-driven animations](https://developer.chrome.com/docs/css-ui/scroll-driven-animations "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 23, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@keyframes/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@keyframes (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40keyframes&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40keyframes%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40keyframes%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40keyframes%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff2a9542e6c266ac7028eae954b5c7913e499d1f1%0A*+Document+last+modified%3A+2026-04-23T23%3A49%3A53.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")