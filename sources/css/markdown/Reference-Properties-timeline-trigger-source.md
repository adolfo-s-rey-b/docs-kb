*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source#mdn-search)
    

timeline-trigger-source CSS property
====================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/961)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source#browser_compatibility)
 carefully before using this in production.

The **`timeline-trigger-source`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies the timeline that will trigger a [scroll-triggered animation](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers/Using_scroll-triggered_animations)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source#syntax)

---------------------------------------------------------------------------------------------------------------

css

    /* Keywords */
    timeline-trigger-source: none;
    timeline-trigger-source: auto;
    
    /* Named timeline */
    timeline-trigger-source: --my-timeline;
    
    /* Anonymous scroll progress timeline */
    timeline-trigger-source: scroll();
    timeline-trigger-source: scroll(x root);
    
    /* Anonymous view progress timeline */
    timeline-trigger-source: view();
    timeline-trigger-source: view(inline);
    timeline-trigger-source: view(x 200px auto);
    
    /* Multiple source values */
    timeline-trigger-source: view(), none, --my-timeline;
    timeline-trigger-source: scroll(x), auto, scroll(y root);
    
    /* Global values */
    timeline-trigger-source: inherit;
    timeline-trigger-source: initial;
    timeline-trigger-source: revert;
    timeline-trigger-source: revert-layer;
    timeline-trigger-source: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source#values)

This property is specified as a comma-separated list of the following values:

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source#none)

The element's trigger does not have a source: it is not associated with any timeline and the animation does not happen.

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source#auto)

The element's trigger source is the document's default time-based [`DocumentTimeline`](https://developer.mozilla.org/en-US/docs/Web/API/DocumentTimeline)
. This is the default value.

[`<dashed-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)

The element creates a scroll-triggered animation trigger as a [named view progress timeline](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines#named_view_progress_timeline)
.

[`scroll()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/scroll)

The element creates a scroll-triggered animation trigger as an [anonymous scroll progress timeline](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines#anonymous_scroll_progress_timelines)
.

[`view()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/view)

The element creates a scroll-triggered animation trigger as an [anonymous view progress timeline](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines#anonymous_view_progress_timeline_the_view_function)
.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source#description)

-------------------------------------------------------------------------------------------------------------------------

The `timeline-trigger-source` property specifies the timeline trigger that will control a scroll-triggered animation.

For example:

css

    .trigger {
      timeline-trigger-name: --my-trigger;
      timeline-trigger-source: view();
    }
    

The resulting [`ViewTimeline`](https://developer.mozilla.org/en-US/docs/Web/API/ViewTimeline)
 tracks the position of the `.trigger` element across the block-axis of the nearest ancestor scroller. The trigger activates and deactivates when the tracked element is scrolled to certain positions inside the scrollport. By default, when `timeline-trigger-source` is set to `view()`, activation occurs when the tracked element starts to enter the scrollport, and deactivation occurs when the tracked element completely exits the scrollport.

An animated element can be triggered by the previously described trigger by referencing its `timeline-trigger-name` in its [`animation-trigger`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-trigger)
 property. The `animation-trigger` value consists of a comma-separated list, each containing the name of a trigger and one or two [`<animation-action>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action)
 keywords that specify what the animation should do when its trigger activates and deactivates.

For example:

css

    .animated {
      animation: rotate 3s infinite linear both;
      animation-trigger: --my-trigger play-once;
    }
    

The animated element and the element that creates the trigger can be the same element. In this case, the animated element creates its own trigger:

css

    .animatedAndTrigger {
      animation: rotate 3s infinite linear both;
      animation-trigger: --my-trigger play-once;
    
      timeline-trigger-name: --my-trigger;
      timeline-trigger-source: view();
    }
    

The `timeline-trigger-source` property, along with the [`timeline-trigger-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-name)
, [`timeline-trigger-activation-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range)
, and [`timeline-trigger-active-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range)
 properties, can also be set using the [`timeline-trigger`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger)
 shorthand property.

### [Trigger source types](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source#trigger_source_types)

To create a triggered animation, set the `timeline-trigger-source` property to one of three main value types:

*   A [`view()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/view)
     function referencing an [anonymous view progress timeline](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines#anonymous_view_progress_timeline_the_view_function)
     trigger. This is created on the nearest scrolling ancestor of the element that creates the trigger. As shown earlier, this allows you to create functionality whereby an element will start animating when it (or another element) reaches a certain scroll offset in the scrollport, and stop animating (or some other action) when it (or another element) reaches a different scroll offset. For example:
    
    css
    
        timeline-trigger-name: --t;
        timeline-trigger-source: view();
        
    
*   A [`scroll()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/scroll)
     function referencing an [anonymous scroll progress timeline](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines#anonymous_scroll_progress_timelines)
     trigger. You can create this on the root element or the nearest scroller of the element that creates the trigger. This allows you to create functionality whereby an element will start animating when it (or another element) reaches an absolute scroll offset (for example, it scrolls upwards by `600px`), and stop animating (or some other action) when it (or another element) reaches a different offset. For example:
    
    css
    
        timeline-trigger-name: --t;
        timeline-trigger-source: scroll();
        timeline-trigger-activation-range: 600px;
        
    
    **Note:** See the [`scroll()` example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source#basic_scroll_progress_timeline_source_usage)
    .
    
*   A [`<dashed-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)
     referencing a [named view progress timeline](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines#named_view_progress_timeline)
     or [named scroll progress timeline](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines#named_scroll_progress_timelines)
    . This involves setting a [`view-timeline-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-name)
     or [`scroll-timeline-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline-name)
     on the element that creates the trigger, and then referring to that name in the value of the `timeline-trigger-source` property, for example:
    
    css
    
        view-timeline-name: --my-timeline;
        timeline-trigger-source: --my-timeline;
        
    

Scroll progress timelines are arguably less useful for scroll-triggered animations than view progress timelines. You are more likely to want an animation to start at a scroll offset relative to the scrollport, not after an arbitrary amount of scrolling, where the animation may well be triggered offscreen on smaller screens.

### [Other values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source#other_values)

It is also possible to set `timeline-trigger-source` to a keyword of `auto` or `none`. Both result in a non-scroll-triggered animation, but their effects differ.

*   The default value, `auto`, sets the element's trigger source to the document's default time-based [`DocumentTimeline`](https://developer.mozilla.org/en-US/docs/Web/API/DocumentTimeline)
    . This results in any animations applied to the element playing on page load.
*   The `none` value results in the element's trigger having no source, which means that any animations applied to the element will not play at all.

### [Multiple sources](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source#multiple_sources)

When you specify multiple comma-separated values on a single `timeline-trigger-source` property, they are applied to the timeline triggers in the order in which the [`timeline-trigger-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-name)
s appear. When the number of triggers and `timeline-trigger-source` property values do not match, they are applied in the same way as [multiple animation property values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Using#setting_multiple_animation_property_values)
.

For example, if multiple `timeline-trigger-name` values are set, but only a single `timeline-trigger-source` value is set, the `timeline-trigger-source` will apply to all the `timeline-trigger-name`s. If two `timeline-trigger-source` values are set, they will cycle between the `timeline-trigger-name`s until all of them have a `timeline-trigger-source` value set. And so on.

Consider these declarations:

css

    timeline-trigger-name: --my-trigger, --my-other-trigger, --another-trigger;
    timeline-trigger-source: view(), --my-source;
    

In this case, the first name will use the `view()` source, and the second name will use the `--my-source` source. The third name will cycle back to using the `view()` source again.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source#formal_definition)

-------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | A list, with each item being either the keyword `none`, the keyword `auto`, a case-sensitive [`<ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ident)<br>, a computed [`scroll()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/scroll)<br> function, or a computed [`view()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/view)<br> function. |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | Not animatable |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source#formal_syntax)

-----------------------------------------------------------------------------------------------------------------------------

timeline-trigger-source =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 none [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 auto [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<dashed-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <scroll()> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <view()> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
[+](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#plus "Plus: the entity may occur one or several times")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
[<scroll()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/scroll)
 =   
  scroll( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <scroller> [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 <axis> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
[<view()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/view)
 =   
  view( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <axis> [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 [<'view-timeline-inset'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-inset)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
<scroller> =   
  root     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  nearest  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  self       
  
[<axis>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/axis)
 =   
  block   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  inline  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  x       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  y         
  
[<view-timeline-inset>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-inset)
 =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 auto [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <length-percentage> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
[{1,2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source#examples)

-------------------------------------------------------------------------------------------------------------------

### [Basic view progress timeline source usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source#basic_view_progress_timeline_source_usage)

In this example, we create a basic scroll-triggered animation that uses an anonymous view progress timeline trigger source.

#### HTML

The markup contains two [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 elements: one to animate and one to create a trigger, plus basic text content to make the page scroll. The text is hidden for brevity.

html

    <div class="animated">I am animated</div>
    
    ...
    
    <div class="trigger">I create the trigger</div>
    
    ...
    

    <div class="animated">I am animated</div>
    
    <p>
      Fusce dictum ex quis ipsum consectetur placerat. Cras sed lectus ex. Quisque
      purus dolor, vulputate ac mi eget, commodo varius odio. Suspendisse faucibus
      ipsum vel libero finibus, in placerat nibh congue. Sed iaculis, metus et
      euismod posuere, mi diam vestibulum felis, ac vulputate eros ipsum id justo.
      Etiam a tincidunt purus. Maecenas semper sed enim at blandit. Aenean ut
      sagittis lorem, eget gravida purus. Phasellus eleifend, lectus nec pulvinar
      facilisis, dui dolor feugiat odio, iaculis tempor felis est non tortor. In
      suscipit lorem efficitur molestie tempus. Integer sit amet neque et risus
      iaculis sodales sed eget diam. Quisque sodales nunc sapien, vitae lacinia ex
      luctus quis. Maecenas scelerisque scelerisque elit eu consequat. Etiam ac
      tristique tellus, sed tincidunt velit.
    </p>
    
    <p>
      Fusce dictum ex quis ipsum consectetur placerat. Cras sed lectus ex. Quisque
      purus dolor, vulputate ac mi eget, commodo varius odio. Suspendisse faucibus
      ipsum vel libero finibus, in placerat nibh congue. Sed iaculis, metus et
      euismod posuere, mi diam vestibulum felis, ac vulputate eros ipsum id justo.
      Etiam a tincidunt purus. Maecenas semper sed enim at blandit. Aenean ut
      sagittis lorem, eget gravida purus. Phasellus eleifend, lectus nec pulvinar
      facilisis, dui dolor feugiat odio, iaculis tempor felis est non tortor. In
      suscipit lorem efficitur molestie tempus. Integer sit amet neque et risus
      iaculis sodales sed eget diam. Quisque sodales nunc sapien, vitae lacinia ex
      luctus quis. Maecenas scelerisque scelerisque elit eu consequat. Etiam ac
      tristique tellus, sed tincidunt velit.
    </p>
    
    <div class="trigger">I create the trigger</div>
    
    <p>
      Fusce dictum ex quis ipsum consectetur placerat. Cras sed lectus ex. Quisque
      purus dolor, vulputate ac mi eget, commodo varius odio. Suspendisse faucibus
      ipsum vel libero finibus, in placerat nibh congue. Sed iaculis, metus et
      euismod posuere, mi diam vestibulum felis, ac vulputate eros ipsum id justo.
      Etiam a tincidunt purus. Maecenas semper sed enim at blandit. Aenean ut
      sagittis lorem, eget gravida purus. Phasellus eleifend, lectus nec pulvinar
      facilisis, dui dolor feugiat odio, iaculis tempor felis est non tortor. In
      suscipit lorem efficitur molestie tempus. Integer sit amet neque et risus
      iaculis sodales sed eget diam. Quisque sodales nunc sapien, vitae lacinia ex
      luctus quis. Maecenas scelerisque scelerisque elit eu consequat. Etiam ac
      tristique tellus, sed tincidunt velit.
    </p>
    
    <p>
      Fusce dictum ex quis ipsum consectetur placerat. Cras sed lectus ex. Quisque
      purus dolor, vulputate ac mi eget, commodo varius odio. Suspendisse faucibus
      ipsum vel libero finibus, in placerat nibh congue. Sed iaculis, metus et
      euismod posuere, mi diam vestibulum felis, ac vulputate eros ipsum id justo.
      Etiam a tincidunt purus. Maecenas semper sed enim at blandit. Aenean ut
      sagittis lorem, eget gravida purus. Phasellus eleifend, lectus nec pulvinar
      facilisis, dui dolor feugiat odio, iaculis tempor felis est non tortor. In
      suscipit lorem efficitur molestie tempus. Integer sit amet neque et risus
      iaculis sodales sed eget diam. Quisque sodales nunc sapien, vitae lacinia ex
      luctus quis. Maecenas scelerisque scelerisque elit eu consequat. Etiam ac
      tristique tellus, sed tincidunt velit.
    </p>
    

#### CSS

The animated `<div>` element's [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position)
 is set to `fixed`, positioning it near the top-left of the scrollport to enable us to see when its animation starts and stops.

    body {
      width: 80%;
      margin: 0 auto;
      font-family: "Helvetica", "Arial";
      font-size: 1.3rem;
    }
    
    div {
      height: 100px;
      border: 5px solid black;
    }
    
    .animated {
      width: 100px;
      background: orange;
    }
    
    .trigger {
      background: wheat;
    }
    

css

    .animated {
      position: fixed;
      top: 25px;
      left: 25px;
    }
    

Next, we define the [`@keyframes`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes)
 for the `rotate` animation we will use later:

css

    @keyframes rotate {
      from {
        rotate: 0deg;
      }
    
      to {
        rotate: 360deg;
      }
    }
    

Using the `animation` shorthand, the `.animated` element has the `rotate` animation applied. Without an associated trigger, the element would start animating when the page loads. The `animation-trigger` property makes it a triggered animation. The value references a `timeline-trigger-name` of `--t` and specifies two `<animation-action>` values — `play` and `pause` — which specify that the animation will play on activation and pause on deactivation.

css

    .animated {
      animation: rotate 3s infinite linear;
      animation-trigger: --t play pause;
    }
    

The `.trigger` element creates the animated `<div>`'s trigger via the following properties:

*   A [`timeline-trigger-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-name)
     with value `--t`, which is equal to the identifier referenced in the `.animated` element's `animation-trigger` property value, associating the two together.
*   A `timeline-trigger-source` with value [`view()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/view)
    , which sets the timeline trigger as a view progress timeline, and the element providing the timeline trigger as the nearest scrolling ancestor element.

css

    .trigger {
      timeline-trigger-name: --t;
      timeline-trigger-source: view();
    }
    

#### Result

Try scrolling the content up. When any part of the `.trigger` appears in the scrollport, the animation will play; when it has completely left the scrollport at either edge, the animation will pause.

### [Basic scroll progress timeline source usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source#basic_scroll_progress_timeline_source_usage)

This example is nearly identical to the previous one, except that this time we set `timeline-trigger-source` to an anonymous scroll progress timeline instead of an anonymous view progress timeline.

The HTML and CSS are nearly identical, except that this time we have set our `.trigger` element's `timeline-trigger-source` to [`scroll()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/scroll)
 instead of `view()`. This creates the trigger as an anonymous scroll progress timeline on the element's nearest scrolling ancestor.

We have also set a [`timeline-trigger-activation-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range)
 of `600px`, which means that the trigger will activate (meaning the animation will start playing) when the tracked element scrolls upwards by `600px`. If we didn't set this, the trigger would activate immediately on page load.

    .animated {
      animation: rotate 3s infinite linear;
      animation-trigger: --t play pause;
    }
    

css

    .trigger {
      timeline-trigger-name: --t;
      timeline-trigger-source: scroll();
      timeline-trigger-activation-range: 600px;
    }
    

    @supports not (timeline-trigger-source: scroll()) {
      body::before {
        content: "Your browser does not support the timeline-trigger-source property.";
        background-color: wheat;
        text-align: center;
        padding: 1rem 0;
    
        z-index: 1;
        position: fixed;
        inset: 40% 0 auto;
      }
    }
    

#### Result

The animation will start when the tracked element scrolls `600px` upwards.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source#specifications)

-------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Animation Triggers  <br>\# propdef-timeline-trigger-source](https://drafts.csswg.org/animation-triggers-1/#propdef-timeline-trigger-source) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source#see_also)

-------------------------------------------------------------------------------------------------------------------

*   [`timeline-trigger-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-name)
    , [`timeline-trigger-activation-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range)
    , and [`timeline-trigger-active-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range)
    
*   [`timeline-trigger`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger)
     shorthand property
*   [`animation-trigger`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-trigger)
    
*   [`<animation-action>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action)
     type
*   [`trigger-scope`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/trigger-scope)
    
*   [Using CSS scroll-triggered animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers/Using_scroll-triggered_animations)
    
*   [CSS animation triggers](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers)
     module
*   [CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 12, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/timeline-trigger-source/index.md?plain=1 "Folder: en-us/web/css/reference/properties/timeline-trigger-source (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftimeline-trigger-source&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftimeline-trigger-source%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftimeline-trigger-source%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftimeline-trigger-source%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F1a2a5b56a689b441ebf3be91b90f15746c5a5a01%0A*+Document+last+modified%3A+2026-10-12T05%3A04%3A35.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")