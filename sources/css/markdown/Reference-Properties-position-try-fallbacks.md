*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try-fallbacks#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try-fallbacks#mdn-search)
    

`position-try-fallbacks` CSS property
=====================================

Baseline 2026

Newly available

Since January 2026, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/245)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try-fallbacks#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`position-try-fallbacks`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property enables you to specify a list of one or more alternative **position try fallback options** for anchor-positioned elements to be placed relative to their associated anchor elements. When the element would otherwise overflow its inset-modified containing block, the browser will try placing the positioned element in these different fallback positions, in the order provided, until it finds a value that stops it from overflowing its container or the viewport.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try-fallbacks#syntax)

--------------------------------------------------------------------------------------------------------------

css

    /* Default value: no try fallback options */
    position-try-fallbacks: none;
    
    /* Single try option */
    position-try-fallbacks: flip-block;
    position-try-fallbacks: top;
    position-try-fallbacks: --custom-try-option;
    
    /* Multiple value combination option */
    position-try-fallbacks: flip-block flip-inline;
    
    /* Multiple values */
    position-try-fallbacks: flip-block, flip-inline;
    position-try-fallbacks: top, right, bottom;
    position-try-fallbacks: --custom-try-option1, --custom-try-option2;
    position-try-fallbacks:
      flip-block,
      flip-inline,
      flip-block flip-inline;
    position-try-fallbacks:
      flip-block,
      --custom-try-option,
      --custom-try-option flip-inline,
      right;
    
    /* Global values */
    position-try-fallbacks: inherit;
    position-try-fallbacks: initial;
    position-try-fallbacks: revert;
    position-try-fallbacks: revert-layer;
    position-try-fallbacks: unset;
    

The `position-try-fallbacks` property may be specified as either the keyword value `none` or as a comma-separated list of one or more space-separated custom position option names or `<try-tactic>`s or a `position-area` value.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try-fallbacks#values)

This property is specified as the keyword `none` or a comma-separated list of the following values:

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try-fallbacks#none)

The default value. There are no position try fallback options set.

[`<try-tactic>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try-fallbacks#try-tactic)

Predefined fallback options move the positioned element by taking its computed position and transforming it across a particular axis of the anchor, mirroring any margin offsets. Possible values are:

[`flip-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try-fallbacks#flip-block)

Flips the element's position along the block axis.

[`flip-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try-fallbacks#flip-inline)

Flips the element's position along the inline axis.

[`flip-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try-fallbacks#flip-start)

Flips both the inline and block axis values, swapping the `start` properties with each other, and the `end` properties with each other.

[`position-area`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-area)
 value

Positions the element relative to the edges of its associated anchor element by placing the positioned element on one or more tiles of an implicit 3x3 [position area grid](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-area#description)
 based on the specified [`<position-area>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value)
 value; the effect is the same as a custom [`@position-try`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@position-try)
 fallback option containing only a [`position-area`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-area)
 descriptor.

[`<dashed-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)

Adds a custom [`@position-try`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@position-try)
 option to the fallback options list, the identifying name of which matches the specified `dashed-ident`. If no custom position option exists with that name, the option is ignored.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try-fallbacks#description)

------------------------------------------------------------------------------------------------------------------------

Anchor-positioned elements should always appear in a convenient place for the user to interact with, if at all possible, regardless of where their anchor is positioned. To stop the positioned element from overflowing the viewport, it is often necessary to change its location when its anchor gets close to the edge of its containing element or the viewport.

This is achieved by providing one or more position-try fallback options in the `position-try-fallbacks` property. If the positioned element's initial position would overflow, the browser will try each fallback position option; the first fallback option that doesn't cause the element to overflow its containing block is applied. By default, the browser will try them in the order they appear in the list, applying the first one it finds that will stop the positioned element from overflowing.

If no option can be found that will place the positioned element completely on-screen, the browser will revert to displaying the positioned element at its default position before any try fallback options were applied.

**Note:** In some situations you might want to just hide overflowing positioned elements, which can be achieved using the [`position-visibility`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-visibility)
 property. In most cases however it is better to keep them on-screen and usable.

The `position-try-fallbacks` property, along with the [`position-try-order`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try-order)
 property, can also be set by using the [`position-try`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try)
 shorthand.

For detailed information on anchor features and position try fallback usage, see the [CSS anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning)
 module and the [Fallback options and conditional hiding for overflow](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Try_options_hiding)
 guide.

### [Predefined <try-tactic> values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try-fallbacks#predefined_try-tactic_values)

Referred to as a `<try-tactic>` in the specification, the predefined values move the positioned element by taking its computed position and transforming it across a particular axis of the anchor. The predefined values are:

[`flip-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try-fallbacks#flip-block_2)

Flips the element's position along the block axis so that it appears the same distance away from the anchor but on the opposite side of it. To put it another way, it mirrors the element's position across an inline axis drawn through the center of the anchor. As an example, if the positioned element started to overflow at the top of the anchor, this value would flip the position to the bottom.

[`flip-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try-fallbacks#flip-inline_2)

Flips the element's position along the inline axis so that it appears the same distance away from the anchor but on the opposite side of it. To put it another way, it mirrors the element's position across a block axis drawn through the center of the anchor. As an example, if the positioned element started to overflow at the left of the anchor, this value would flip the position to the right.

[`flip-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try-fallbacks#flip-start_2)

Mirrors the element's position across an axis drawn diagonally through the center of the anchor, passing through the point at the intersection of the block axis start and the inline axis start, and the point at the intersection of the block axis end and the inline axis end. As an example, if the positioned element started to overflow at the left of the anchor, this value would flip the positioned element to the top.

### [Combination options](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try-fallbacks#combination_options)

A single position-try fallback option can include more than one `<try-tactic>` or `dashed-ident` options, or a combination of both by declaring them as a single space-separated option:

*   In the case of multiple predefined `<try-tactic>` options, their transformations are composed together.
*   In the case of declaring a predefined `<try-tactic>` and a `<dashed-ident>` named `@position-try` option, the custom position option is applied first, then the `<try-tactic>` transformation is applied.

`position-area` values cannot be combined like this.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try-fallbacks#formal_definition)

------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | absolutely positioned elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try-fallbacks#formal_syntax)

----------------------------------------------------------------------------------------------------------------------------

position-try-fallbacks =   
  none                                                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<dashed-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)\
 [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 <try-tactic> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <position-area> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
<try-tactic> =   
  flip-block   [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  flip-inline  [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  flip-start   [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  flip-x       [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  flip-y         
  
[<position-area>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value)
 =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 left [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 center [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 right [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 span-left [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 span-right [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 x-start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 x-end [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 span-x-start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 span-x-end [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 self-x-start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 self-x-end [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 span-self-x-start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 span-self-x-end [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 span-all [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 top [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 center [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 bottom [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 span-top [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 span-bottom [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 y-start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 y-end [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 span-y-start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 span-y-end [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 self-y-start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 self-y-end [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 span-self-y-start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 span-self-y-end [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 span-all [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 block-start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 center [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 block-end [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 span-block-start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 span-block-end [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 span-all [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 inline-start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 center [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 inline-end [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 span-inline-start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 span-inline-end [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 span-all [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 self-block-start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 center [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 self-block-end [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 span-self-block-start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 span-self-block-end [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 span-all [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 self-inline-start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 center [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 self-inline-end [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 span-self-inline-start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 span-self-inline-end [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 span-all [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 center [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 end [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 span-start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 span-end [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 span-all [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[{1,2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 self-start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 center [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 self-end [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 span-self-start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 span-self-end [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 span-all [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[{1,2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try-fallbacks#examples)

------------------------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try-fallbacks#basic_usage)

This example shows the basic usage of a couple of predefined `<try-tactic>` fallback options.

#### HTML

The HTML includes two [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 elements that will become an anchor and an anchor-positioned element:

html

    <div class="anchor">⚓︎</div>
    
    <div class="infobox">
      <p>This is an information box.</p>
    </div>
    

#### CSS

We style the `<body>` element to be very large, to enable both horizontal and vertical scrolling.

The anchor is given an [`anchor-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-name)
 and large margins to place it somewhere near the center of the visible section of the `<body>`:

    .anchor {
      font-size: 1.8rem;
      color: white;
      text-shadow: 1px 1px 1px black;
      background-color: hsl(240 100% 75%);
      width: fit-content;
      border-radius: 10px;
      border: 1px solid black;
      padding: 3px;
    }
    

css

    body {
      width: 1500px;
      height: 500px;
    }
    
    .anchor {
      anchor-name: --my-anchor;
      margin: 100px 350px;
    }
    

The infobox is given fixed positioning, a [`position-anchor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor)
 property that references the anchor's `anchor-name`, to associate the two together, and it is tethered to the anchor's top-left corner using a `position-area`.

We include a `position-try-fallbacks` list (and re-declare it with the `position-try` shorthand in case the longhand property name is not yet supported), providing two predefined position-try fallback options to prevent it from overflowing when the anchor gets near the edge of the viewport, by flipping it along the inline or block axis of the anchor.

    .infobox {
      color: darkblue;
      background-color: azure;
      border: 1px solid #dddddd;
      padding: 10px;
      border-radius: 10px;
      font-size: 1rem;
    }
    

css

    .infobox {
      position: fixed;
      position-anchor: --my-anchor;
      position-area: top left;
    
      position-try-fallbacks: flip-block, flip-inline;
      position-try: flip-block, flip-inline;
    }
    

#### Result

This gives us the following result:

Try scrolling so the anchor nears the edges:

*   If you move the anchor near the top of the viewport, you will see the positioned element flip to the bottom-left of the anchor to avoid overflowing.
*   If you move the anchor near the left of the viewport, you will see the positioned element flip to the top-right of the anchor to avoid overflowing.

Depending on the browser, once the positioned element moves to the fallback position, it may remain in the fallback position even if the fallback positioning is no longer necessary, such as when the space allows it to return to the position defined by the [`position-area`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-area)
.

However, if you move the anchor towards the top-left corner of the viewport, you'll notice a problem — as the positioned element starts to overflow in the block and inline direction, it flips back to its default top-left position and overflows in both directions, which is not what we want.

This is because we only gave the browser position options of `flip-block` _or_ `flip-inline`. We didn't give it the option of trying both at the same time. The next example will show you how to fix this issue.

### [Combining multiple values into one option](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try-fallbacks#combining_multiple_values_into_one_option)

Let's use a combined try fallback option to fix the problem we found with the previous demo.

#### HTML and CSS

All of the HTML and CSS in this demo is the same, except for the positioned element code. In this case, it is given a third position try fallback option: `flip-block flip-inline`:

    <div class="anchor">⚓︎</div>
    
    <div class="infobox">
      <p>This is an information box.</p>
    </div>
    

    body {
      width: 1500px;
      height: 500px;
    }
    
    .anchor {
      font-size: 1.8rem;
      color: white;
      text-shadow: 1px 1px 1px black;
      background-color: hsl(240 100% 75%);
      width: fit-content;
      border-radius: 10px;
      border: 1px solid black;
      padding: 3px;
    }
    
    .anchor {
      anchor-name: --my-anchor;
      margin: 100px 350px;
    }
    
    .infobox {
      color: darkblue;
      background-color: azure;
      border: 1px solid #dddddd;
      padding: 10px;
      border-radius: 10px;
      font-size: 1rem;
    }
    

css

    .infobox {
      position: fixed;
      position-anchor: --my-anchor;
      position-area: top left;
    
      position-try:
        flip-block,
        flip-inline,
        flip-block flip-inline;
      position-try-fallbacks:
        flip-block,
        flip-inline,
        flip-block flip-inline;
    }
    

#### Result

The third position-try fallback option means that the browser will try `flip-block` then `flip-inline` to avoid overflow, and if those fallbacks fail, it will combine the two, flipping the element's position in the block and inline directions at the same time. Now when you scroll the anchor towards the top _and_ left edges of the viewport, the positioned element will flip over to the bottom-right.

### [`position-area` try fallback options](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try-fallbacks#position-area_try_fallback_options)

This example shows some `position-area` position-try fallback options in action.

#### HTML and CSS

All of the HTML and CSS in this demo is the same, except for the positioned element code. In this case, our position try fallback options are all `position-area` values — `top`, `top right`, `right`, `bottom right`, `bottom`, `bottom left`, and `left`.

This means that the positioned element will find a reasonable position to display in, whatever viewport edges the anchor is near. This approach is a bit more longwinded than the predefined values approach, but it is also more granular and flexible.

    <div class="anchor">⚓︎</div>
    
    <div class="infobox">
      <p>This is an information box.</p>
    </div>
    

    body {
      width: 1500px;
      height: 500px;
    }
    
    .anchor {
      font-size: 1.8rem;
      color: white;
      text-shadow: 1px 1px 1px black;
      background-color: hsl(240 100% 75%);
      width: fit-content;
      border-radius: 10px;
      border: 1px solid black;
      padding: 3px;
    }
    
    .anchor {
      anchor-name: --my-anchor;
      margin: 100px 350px;
    }
    
    .infobox {
      color: darkblue;
      background-color: azure;
      border: 1px solid #dddddd;
      padding: 10px;
      border-radius: 10px;
      font-size: 1rem;
    }
    

css

    .infobox {
      position: fixed;
      position-anchor: --my-anchor;
      position-area: top left;
    
      position-try:
        top, top right, right,
        bottom right, bottom,
        bottom left, left;
    
      position-try-fallbacks:
        top, top right, right,
        bottom right, bottom,
        bottom left, left;
    }
    

#### Result

Scroll the page and check out the effect of these position-try fallback options as the anchor nears the edge of the viewport.

### [Custom try option examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try-fallbacks#custom_try_option_examples)

See the [`@position-try`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@position-try)
 reference page.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try-fallbacks#specifications)

------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Anchor Positioning Module Level 1  <br>\# position-try-fallbacks](https://drafts.csswg.org/css-anchor-position-1/#position-try-fallbacks) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try-fallbacks#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try-fallbacks#see_also)

------------------------------------------------------------------------------------------------------------------

*   [`position-try`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try)
    
*   [`position-try-order`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try-order)
    
*   [`@position-try`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@position-try)
     at-rule
*   [`position-area`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-area)
    
*   [`<position-area>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value)
     value
*   [Fallback options and conditional hiding for overflow](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Try_options_hiding)
     guide
*   [Using CSS anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Using)
     guide
*   [CSS anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try-fallbacks/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/position-try-fallbacks/index.md?plain=1 "Folder: en-us/web/css/reference/properties/position-try-fallbacks (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fposition-try-fallbacks&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fposition-try-fallbacks%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fposition-try-fallbacks%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fposition-try-fallbacks%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd1cf7346516383565b51a125c064ae3d5d893526%0A*+Document+last+modified%3A+2026-09-14T09%3A37%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")