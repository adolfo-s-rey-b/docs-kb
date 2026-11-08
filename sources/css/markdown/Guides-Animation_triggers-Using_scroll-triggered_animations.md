*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers/Using_scroll-triggered_animations#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers/Using_scroll-triggered_animations#mdn-search)
    

Using CSS scroll-triggered animations
=====================================

CSS **scroll-triggered animations** provide a declarative mechanism to start, pause, stop, or reverse an element's [`DocumentTimeline`](https://developer.mozilla.org/en-US/docs/Web/API/DocumentTimeline)
\-based [CSS animation](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations)
 when the user scrolls it (or a different element) to a specified offset within a scrollport.

This article covers how to create CSS scroll-triggered animations.

[Scroll-triggered animation concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers/Using_scroll-triggered_animations#scroll-triggered_animation_concepts)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

A common UI pattern involves triggering animations on a web page when the user scrolls to a certain place in the content, for example, to pull in additional UI elements or draw the user's attention to certain details.

CSS scroll-triggered animations enable defining scroll-based triggers that start and stop regular time-based [CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations)
. You can define trigger positions inside a [scroll container](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_container)
 so that, when a tracked element reaches those positions within the scrollport, they toggle the play state of an animation applied to that element, or to a completely different element.

**Note:** Scroll-triggered animations provide an alternative to using JavaScript features — such as frameworks or the [Intersection Observer API](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API)
 — to trigger animations on scroll. CSS scroll-triggered animations are more performant and, arguably, simpler to implement.

### [Scroll-triggered versus scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers/Using_scroll-triggered_animations#scroll-triggered_versus_scroll-driven_animations)

Scroll-triggered animations are similar to [CSS scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations)
, but they are different:

*   Scroll-triggered animations are regular time-based animations that play when a trigger becomes active; they observe the [`animation-delay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-delay)
     each time the animation starts, and always complete each iteration in the amount of time defined by the [`animation-duration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-duration)
    , regardless of how fast the user scrolls.
*   With scroll-driven animations, the normal, time-based animation timeline is replaced by a scroll-based timeline, meaning that the animation progresses forwards and backwards as you scroll towards the start and end of the content, respectively, with faster scrolling resulting in a faster animation. Scroll-driven animations ignore the `animation-duration` and `animation-delay` properties.

[Scroll-triggered animation basics](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers/Using_scroll-triggered_animations#scroll-triggered_animation_basics)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Let's walk through a basic example to show you how a scroll-triggered animation works. An image caption will fade in and out when the image it is captioning is scrolled into and out of view. In this case:

*   The [`<figcaption>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/figcaption)
     element has a [`@keyframes`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes)
     animation set on it: a fade-in effect. This animation is the _triggered animation_.
*   For the _animation actions_, we specify that the animation should play forwards when the trigger is _activated_, fading the caption in, and play backwards when the trigger is _deactivated_, fading the caption out.
*   The _animation triggers_ are defined on the `<img>` element. The activation is triggered when the `<img>` starts entering the scrollport and the deactivation occurs when the `<img>` fully exits the scrollport, meaning the full scrollport is the _timeline range_, the `<img>` is the _tracked element_, and the `<figcaption>` is the animated element.
*   We'll set an [anonymous view progress timeline](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines#anonymous_view_progress_timeline_the_view_function)
     as the _trigger source_ on the [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
     element, created using the [`view()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines#anonymous_view_progress_timeline_the_view_function)
     function.

As the content is scrolled up and down, the caption's animation will start as soon as the `<img>` begins to appear inside the scrollport, with the animation reversing when the `<img>` exits the scrollport. This basic example doesn't create the effect we want, but it's a good start that we can improve on as we learn about more features.

The HTML features several paragraphs of content with a [`<figure>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/figure)
 element included in the middle of them, which contains the `<img>` and `<figcaption>`. For the sake of brevity, we are not showing the full source.

We'll start by defining [`@keyframes`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes)
 for the `fade-in` animation we'll apply to our `<figcaption>`.

The first declaration block applies the animation and an animation trigger, along with the animation actions, to the [`<figcaption>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/figcaption)
 element:

1.  We use the [`animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
     shorthand to apply the `fade-in` animation to `<figcaption>`. By itself, without triggers, this would cause the `<figcaption>` to fade into view as soon as the page loads.
2.  We use the [`animation-trigger`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-trigger)
     property to delay the start of the animation until the [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
     element is scrolled into view by identifying which element will provide the triggers, and what those trigger's actions will be. The `animation-trigger` property value components include:
    *   A [`<dashed-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)
        , `--t`, which is the identifier set as the value of the [`timeline-trigger-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-name)
         property on the triggering element.
    *   Two [`<animation-action>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action)
         values, which specify how the animation should behave when the trigger is activated and deactivated (the [animation actions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers/Using_scroll-triggered_animations#adjusting_the_animations_action)
        ). When the trigger is activated, we set the `<figcaption>` element's animation to play forwards. When the trigger is deactivated, we set the `<figcaption>` element's animation to play backwards.

The second declaration block creates the animation trigger:

1.  We use the `timeline-trigger-name` property to give the `<img>` element an identifying name for triggers created on it. This is the same dashed identifier as the trigger name referenced in the `<figcaption>` element's `animation-trigger` property value.
2.  We use the [`timeline-trigger-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source)
     property to create the animation trigger type. Specifying the [`view()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines#anonymous_view_progress_timeline_the_view_function)
     function means our trigger type is an [anonymous view progress timeline](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines#anonymous_view_progress_timeline_the_view_function)
    , which has a default [activation range](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers/Using_scroll-triggered_animations#adjusting_the_trigger_activation_range)
     equal to the `cover` [timeline range](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timeline_insets)
    .

By default, the [`ViewTimeline`](https://developer.mozilla.org/en-US/docs/Web/API/ViewTimeline)
 created by the `view()` function tracks the position of the `<img>` element across the block-axis of the nearest parent scroller. The element that is tracked, in this case the `<img>`, is the **subject** or the **tracked element**.

By default, the triggers are activated and deactivated when the tracked element is scrolled to the start and end of the timeline range respectively, in the block direction, causing the `<figcaption>` animation to play forwards and play backwards. Activation occurs when the tracked element enters the [**activation range**](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range#description)
, and deactivation occurs when the tracked element leaves the [**active range**](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range#description)
. When the `timeline-trigger-source` is set to `view()`, the default activation and active ranges resolve to `cover`, which is from the point when the tracked element's start border edge starts to enter the scrollport to the point when the tracked element's end border edge completely exits the scrollport.

The example renders like so:

Note how the caption starts to fade in as soon as any part of the image becomes visible in the scrollport, whether you are moving it in from the bottom or the top. It doesn't fade out again until the entire image has moved out of the scrollport, so you won't be able to see the fading out effect; if you scroll the image back into view, the caption will fade in again.

[Creating the trigger on the same element](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers/Using_scroll-triggered_animations#creating_the_trigger_on_the_same_element)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In the previous example, the trigger was defined on the `<img>` element, and the `<figcaption>` was animated. It is possible to define the trigger on the animated element itself. Let's modify the previous example to create the trigger on the animated [`<figcaption>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/figcaption)
 element.

The HTML is identical to the previous example. The CSS differs only in where the `timeline-trigger-*` properties are set.

This time, the [`animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
, [`animation-trigger`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-trigger)
, [`timeline-trigger-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-name)
, and [`timeline-trigger-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source)
 properties are all set on the `<figcaption>` element — it will animate when it appears in the scrollport. In the previous example, the `<figcaption>` was the animated element and the `<img>` was the tracked element. Now the caption plays both roles.

css

    figcaption {
      animation: fade-in 1s ease-in both;
      animation-trigger: --t play-forwards play-backwards;
      timeline-trigger-name: --t;
      timeline-trigger-source: view();
    }
    

The updated rendering looks like this:

In this case, the `<figcaption>` fades into view when it, rather than the image, first enters into the scrollport.

[Adjusting the trigger activation range](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers/Using_scroll-triggered_animations#adjusting_the_trigger_activation_range)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In the previous examples, the trigger activates (`fade-in` starts) as soon as a block edge of the tracked element enters the scrollport at one edge, and deactivates (fade-out starts: `fade-in` is played backwards) when the tracked element has finished exiting the scrollport at the opposite edge. As a result, the fade out is never visible. This is because the default activation and active ranges (see [`<timeline-range-name>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name)
) when using `view()` as the `timeline-trigger-source` are both `cover`.

To make the fade out animation visible, we can offset the start and end of the activation range using the [`timeline-trigger-activation-range-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-start)
 and [`timeline-trigger-activation-range-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-end)
 properties, respectively, or the [`timeline-trigger-activation-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range)
 shorthand to set both values in a single declaration. Each of these properties can take the following values:

*   The `normal` default value.
*   A [`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
     value to specify a point along the default range.
*   A [`<timeline-range-name>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name)
     keyword specifying a named range.
*   A `timeline-range-name` and a `<length-percentage>` to specify a point along the named range.

Percentages are relative to the length of the `<timeline-range-name>`, which resolves to `cover` for our [view progress timeline](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines#view_progress_timelines)
. Had we set [`scroll()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines#scroll_progress_timelines)
 as our [`timeline-trigger-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source)
, the default `<timeline-range-name>` would have resolved to `scroll`. See [Timeline range names](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timeline_range_names)
 to learn about the `<timeline-range-name>` values.

The following example will cause the trigger to activate `50%` of the way through the `entry` range (when `50%` of the tracked element has entered the scrollport via one of the scrollport's block edges) and deactivate `0%` of the way through the `exit` range (when `50%` of the tracked element has exited the scrollport's opposite block edge).

Let's apply this to our first example so you can see what the effect is. Our `img` declaration block is updated to the following:

css

    img {
      timeline-trigger-name: --t;
      timeline-trigger-source: view();
      timeline-trigger-activation-range: entry 50% exit 0%;
    }
    

The updated rendering looks like this:

The animation of the `<figcaption>` is now a bit more useful — it only starts to fade into view when a significant portion of the `<img>` has entered the scrollport at its end edge, and it starts to fade out when the `<img>` has started to exit the scrollport at its start edge. When you scroll the content back down again, the trigger reactivates and the fade-in occurs again at the scrollport's start edge, and deactivation occurs again at the scrollport's end edge.

[Setting a custom active range](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers/Using_scroll-triggered_animations#setting_a_custom_active_range)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The **active range** is the range within which a trigger will remain activated once activation has occurred. By default, the active range is the same as the activation range; therefore, in the examples we've seen so far, the range for activation and deactivation has been the same.

It is possible to set a different active range from the activation range using the [`timeline-trigger-active-range-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range-start)
 and [`timeline-trigger-active-range-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range-end)
 properties, or the [`timeline-trigger-active-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range)
 shorthand to set both values in a single declaration.

You might want to do this to extend the time an animation has to complete — for example, if you want the animation trigger to activate only within a small range but stay active over a larger range. Only when the tracked element moves out of the active range does the trigger become inactive; after that, you can activate it again by moving the subject back into the activation range.

Let's build on our previous examples to demonstrate the effect of the active range. The HTML is the same, except we've included two identical `<figure>` elements with classes of `.one` and `.two`, placed next to one another using [flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Basic_concepts)
, meaning they'll come in and go out of view at the same time as each other. In each case, the `<img>` will be the tracked element for its sibling animated `<figcaption>`.

    <h1>Information about Cairns</h1>
    
    <p>
      The countryside surrounding Cairns, located in eastern Australia, is a
      breathtakingly beautiful region characterized by diverse landscapes, lush
      greenery, and unique natural wonders.
    </p>
    
    <p>
      Nestled between the Great Dividing Range and the sparkling Coral Sea, this
      area offers a stunning blend of tropical rainforests, pristine beaches, and
      majestic mountain ranges.
    </p>
    
    <p>
      As you venture away from the city, you'll be greeted by the verdant
      rainforests of the Wet Tropics World Heritage Area. Towering ancient trees,
      vibrant ferns, and cascading waterfalls create a serene and magical
      atmosphere.
    </p>
    <p>
      Exploring the lush undergrowth, you may encounter unique wildlife such as
      colorful birds, tree-dwelling mammals, and rare reptiles. The sounds of
      chirping birds and rushing water add to the symphony of nature, providing an
      immersive experience in this captivating wilderness.
    </p>
    
    <p>
      Traveling further, you'll discover the Atherton Tablelands, a plateau renowned
      for its fertile farmlands, rolling hills, and picturesque lakes. This
      agricultural heartland is dotted with quaint rural towns and farms producing
      an array of fresh produce.
    </p>
    <p>
      Fields of sugar cane, banana plantations, and dairy farms stretch as far as
      the eye can see, creating a patchwork of vibrant green hues against the
      backdrop of distant mountains. The region is also famous for its waterfalls,
      such as Millaa Millaa Falls, where crystal-clear water tumbles down verdant
      cliffs, offering a refreshing retreat.
    </p>
    
    <div class="figure-wrapper">
      <figure class="one">
        <img
          src="https://mdn.github.io/shared-assets/images/examples/learn/gallery/pic5.jpg"
          alt="A butterfly with red, white, and gold wing sections, sitting in a leaf" />
        <figcaption>
          A beautiful butterfly seen in the Jungle near Cairns
        </figcaption>
      </figure>
    
      <figure class="two">
        <img
          src="https://mdn.github.io/shared-assets/images/examples/learn/gallery/pic5.jpg"
          alt="A butterfly with red, white, and gold wing sections, sitting in a leaf" />
        <figcaption>
          A beautiful butterfly seen in the Jungle near Cairns
        </figcaption>
      </figure>
    </div>
    
    <p>
      No visit to the countryside surrounding Cairns is complete without exploring
      the stunning beaches that line the Coral Sea. From Palm Cove to Mission Beach,
      the coastline is adorned with golden sands, swaying palm trees, and azure
      waters. These idyllic beaches provide the perfect setting for relaxation,
      swimming, and water sports.
    </p>
    <p>
      Snorkeling enthusiasts can also discover the wonders of the Great Barrier
      Reef, a UNESCO World Heritage Site, which lies just off the coast. This
      vibrant underwater ecosystem teems with an incredible diversity of marine
      life, including colorful coral formations, tropical fish, and sea turtles.
    </p>
    
    <p>
      Lastly, the surrounding countryside is home to an impressive array of national
      parks and mountains. Barron Gorge National Park, for instance, showcases
      rugged terrain, deep gorges, and thundering waterfalls.
    </p>
    <p>
      You can embark on hiking trails that lead to breathtaking viewpoints, offering
      panoramic vistas of the surrounding rainforest-clad mountains and valleys.
      Further west, the towering peaks of the Great Dividing Range present
      opportunities for adventurous hiking and exploring scenic vistas, including
      the iconic Walshs Pyramid near Gordonvale.
    </p>
    

We apply the same `animation` to both `<figcaption>` elements as in previous examples, but their `animation-trigger` property values reference two different `timeline-trigger-name` values.

css

    figcaption {
      animation: fade-in 0.4s ease-in both;
    }
    
    .one figcaption {
      animation-trigger: --t1 play-forwards play-backwards;
    }
    
    .two figcaption {
      animation-trigger: --t2 play-forwards play-backwards;
    }
    

We set the same `timeline-trigger-source` and the same `timeline-trigger-activation-range` on both `<img>` elements. The `timeline-trigger-name` for each `<img>` element reference the two different dashed identifiers in the previous code block, which means the trigger created on each `<img>` acts as the trigger for the animation on its own sibling `<figcaption>`.

The `timeline-trigger-activation-range: contain 40% contain 60%` declaration means that the trigger activates — and thus the animation starts playing — when the tracked element reaches a narrow range, the middle `20%` of the scrollport, and deactivates when the subject exits that narrow range.

By default, the activation range is the same as the active range. However, we also set a `timeline-trigger-active-range` range of `entry 50% exit 100%` on the second `<img>`. This means that, once faded in, the second `<figcaption>` will only fade out again when the second `<img>` scrolls to `exit 100%`, which is when it has completely left the scrollport.

css

    img {
      timeline-trigger-source: view();
      timeline-trigger-activation-range: contain 40% contain 60%;
    }
    
    .one img {
      timeline-trigger-name: --t1;
    }
    
    .two img {
      timeline-trigger-name: --t2;
      timeline-trigger-active-range: entry 50% exit 100%;
    }
    

**Note:** To have an effect, the `timeline-trigger-active-range` must be set to a larger range than the `timeline-trigger-activation-range`.

    .figure-wrapper {
      display: flex;
      gap: 20px;
    }
    
    figcaption {
      left: 5px;
      right: -1px;
    }
    

This example renders like so:

Scroll the images into view, and then scroll them carefully up and down. Note how both captions fade into view at the same time, at a point roughly one third up the embedded page. The first caption fades out slightly further up, whereas the second caption doesn't fade out until it has been moved completely out of the scrollport. This is because both `<img>` triggers have the same _activation_ range, while the second one has a much larger _active_ range applied to it than the activation range.

[The timeline-trigger shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers/Using_scroll-triggered_animations#the_timeline-trigger_shorthand)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

So far, we've written all the CSS for our scroll-triggered animation as a mixture of shorthand and longhand properties, to effectively explain each of the properties and their values. However, this is cumbersome and wordy. Now that you've understood the concepts, we can use the [`timeline-trigger`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger)
 shorthand to create the shortest possible equivalent. You'll likely opt for this shorthand in your future projects.

Taking these declarations as an example:

We can rewrite these in a single line of CSS using the `timeline-trigger` shorthand:

[Adjusting the animation's action](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers/Using_scroll-triggered_animations#adjusting_the_animations_action)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

All the examples so far in this guide have triggered the `fade-in` animation, causing the caption to fade in and fade out. The forwards and backwards play is controlled by the `animation-trigger` declaration set on the animated element:

The [`<animation-action>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action)
 values `play-forwards` and `play-backwards` specify that the animation plays forwards when the trigger activates, and backwards when the trigger deactivates. The first value is the animation activation action, and the second value is the animation deactivation action.

If we set the following `animation` declaration on the same element:

The animation only happens once when the trigger is activated, and once in reverse when it is deactivated: we didn't specify an [`animation-iteration-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-iteration-count)
 in our `animation` shorthand, therefore the default value, `1`, is used.

There are other `animation-action` values that can be set to produce different effects. For example:

*   `play-once` causes the animation to play only once. Once finished, it won't play again on subsequent activations or deactivations.
*   `play` causes the animation to play, in whatever direction it was previously playing in. In contrast, `play-forwards` and `play-backwards` interact with the animation's [`playbackRate`](https://developer.mozilla.org/en-US/docs/Web/API/Animation/playbackRate "playbackRate")
    , setting it to its absolute positive value or its absolute positive value multiplied by `-1`, respectively. This results in the animation playing forwards or backwards. Note that the [`animation-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-direction)
     value is not affected.
*   `pause` causes the animation to pause. For example, you could set an animation's iteration count to `infinite`, and set the corresponding `animation-trigger` to `--t play pause`: This would cause the animation to play when the trigger is activated, and pause when it deactivates.
*   `reset` has the same effect as `pause`, except that additionally it sets the animation progress back to `0`.

Some of these values are designed to be used together. For example, `play-forwards play-backwards` is intended for use in cases where you want to alternate the direction of play in the animation's end visual effect, causing a UI element to "animate in" when it appears on-screen and then "animate out" again when it goes off-screen. On the other hand, `play pause` is common for animating an element as it appears, then pausing the animation as it starts to go off-screen.

Let's look at a brief example — we'll take our first example and change it so that our `<figure>` fades in only once, when has completely entered the scrollport, and doesn't fade out or animate again until the page is reloaded.

We set the `animation-trigger` property's `animation-action` to `play-once` so that the animation only plays once when the `<figure>` first enters the activation range. We've also set the `timeline-trigger-activation-range` to `contain` so that the animation only plays when the `<figure>` is completely on-screen — it only plays once, so we don't want you to miss it.

css

    figure {
      animation: fade-in 1s ease-in both;
      animation-trigger: --t play-once;
    
      timeline-trigger: --t view() contain;
    }
    

This example renders like so:

When you first scroll the `<figure>` on-screen, it will fade in. After that, it will stay at `100%` opacity regardless of how many times you scroll it up and down the scrollport. You can only get it to fade in again by refreshing the page (or reloading the embedded example's `<iframe>`).

[Trigger scope](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers/Using_scroll-triggered_animations#trigger_scope)

--------------------------------------------------------------------------------------------------------------------------------------------

If multiple triggers use the same `timeline-trigger-name`, because of how [triggers are determined by the browser](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/trigger-scope#description)
 by default, the triggers will be associated with the last element in the HTML source order that has that `timeline-trigger-name` value. This is likely not the desired behavior.

For example, if a document contains multiple repeated components, each containing a scroll-triggered animation where the animated element and tracked element are different elements, all of the animated elements will have their animations controlled by the last component's trigger, unless you use a different `timeline-trigger-name` in each component, or scope the name by subtree.

The [`trigger-scope`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/trigger-scope)
 property limits the visibility, or "scope", of a `timeline-trigger-name` value to a specific subtree. The result is that each animated element can only have its animation triggered by a trigger created within the same scoped subtree. See the `trigger-scope` reference page for details of how this works and a [`trigger-scope` example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/trigger-scope#examples)
.

[Multiple scroll-triggered animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers/Using_scroll-triggered_animations#multiple_scroll-triggered_animations)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In previous examples, we set only a single scroll-triggered animation on an element; however, all of the `animation-*` and `timeline-trigger-*` properties discussed in this guide accept a comma separated list of values to enable triggering multiple animations from multiple triggers. In this section we'll build a slightly more complex example with multiple scroll-triggered animations on the same element.

The [`animation-trigger`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-trigger)
 property works in exactly the same way as the [`animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
 shorthand property and the other animation longhand properties with regards to setting [multiple values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Using#setting_multiple_animation_property_values)
. If multiple `animation-name` values are set, but only a single `animation-trigger` value is set, the `animation-trigger` will apply to all the animations. If two `animation-trigger` values are set, they will cycle between the animations until all of them have an `animation-trigger` value set. And so on.

This example progressively animates an element — applying further animations when new triggers are activated as the page scrolls. As the user scrolls, the element first slides in from the right of the screen, then reveals its contents, then slides down the screen and changes its background color.

The HTML is similar to previous examples except that we have included a [`<section>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section)
 element at the top containing some highlighted content, and some empty [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 elements interspersed throughout our main content that will have triggers defined on them to trigger our animations.

    <section>
      <h2>This content is animated!</h2>
    
      <p>
        The countryside surrounding Cairns, located in eastern Australia, is a
        breathtakingly beautiful region characterized by diverse landscapes, lush
        greenery, and unique natural wonders.
      </p>
    </section>
    
    <h1>Information about Cairns</h1>
    
    <p>
      Nestled between the Great Dividing Range and the sparkling Coral Sea, this
      area offers a stunning blend of tropical rainforests, pristine beaches, and
      majestic mountain ranges.
    </p>
    
    <p>
      As you venture away from the city, you'll be greeted by the verdant
      rainforests of the Wet Tropics World Heritage Area. Towering ancient trees,
      vibrant ferns, and cascading waterfalls create a serene and magical
      atmosphere.
    </p>
    <p>
      Exploring the lush undergrowth, you may encounter unique wildlife such as
      colorful birds, tree-dwelling mammals, and rare reptiles. The sounds of
      chirping birds and rushing water add to the symphony of nature, providing an
      immersive experience in this captivating wilderness.
    </p>
    
    <p>
      Traveling further, you'll discover the Atherton Tablelands, a plateau renowned
      for its fertile farmlands, rolling hills, and picturesque lakes. This
      agricultural heartland is dotted with quaint rural towns and farms producing
      an array of fresh produce.
    </p>
    
    <div id="one"></div>
    
    <p>
      Fields of sugar cane, banana plantations, and dairy farms stretch as far as
      the eye can see, creating a patchwork of vibrant green hues against the
      backdrop of distant mountains. The region is also famous for its waterfalls,
      such as Millaa Millaa Falls, where crystal-clear water tumbles down verdant
      cliffs, offering a refreshing retreat.
    </p>
    
    <p>
      No visit to the countryside surrounding Cairns is complete without exploring
      the stunning beaches that line the Coral Sea. From Palm Cove to Mission Beach,
      the coastline is adorned with golden sands, swaying palm trees, and azure
      waters. These idyllic beaches provide the perfect setting for relaxation,
      swimming, and water sports.
    </p>
    
    <p>
      Snorkeling enthusiasts can also discover the wonders of the Great Barrier
      Reef, a UNESCO World Heritage Site, which lies just off the coast. This
      vibrant underwater ecosystem teems with an incredible diversity of marine
      life, including colorful coral formations, tropical fish, and sea turtles.
    </p>
    
    <div id="two"></div>
    
    <p>
      Lastly, the surrounding countryside is home to an impressive array of national
      parks and mountains. Barron Gorge National Park, for instance, showcases
      rugged terrain, deep gorges, and thundering waterfalls.
    </p>
    
    <p>
      You can embark on hiking trails that lead to breathtaking viewpoints, offering
      panoramic vistas of the surrounding rainforest-clad mountains and valleys.
      Further west, the towering peaks of the Great Dividing Range present
      opportunities for adventurous hiking and exploring scenic vistas, including
      the iconic Walshs Pyramid near Gordonvale.
    </p>
    
    <p>
      Lastly, the surrounding countryside is home to an impressive array of national
      parks and mountains. Barron Gorge National Park, for instance, showcases
      rugged terrain, deep gorges, and thundering waterfalls.
    </p>
    
    <p>
      You can embark on hiking trails that lead to breathtaking viewpoints, offering
      panoramic vistas of the surrounding rainforest-clad mountains and valleys.
      Further west, the towering peaks of the Great Dividing Range present
      opportunities for adventurous hiking and exploring scenic vistas, including
      the iconic Walshs Pyramid near Gordonvale.
    </p>
    
    <div id="three"></div>
    
    <p>
      Walshs Pyramid is located within Wooroonooran National Park south of Cairns,
      Queensland, Australia. An annual footrace to its summit is held on the third
      Saturday in August. For experienced hikers, the ascent and descent can take 4
      to 6 hours. The vegetation on the mountain is fairly dense with exposed rocks
      which can make the surface very slippery after rain.
    </p>
    

Initially, the highlighted content `<section>` is hidden off-screen. Our CSS starts by styling the `<section>` element, giving it a [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position)
 of `fixed` and positioning it near the top-left of the scrollport. We also define the initial styles that we will be animating from and returning to. We then set three [`animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
 values, which will make the `<section>` element `slide-from-right`, then `reveal` its contents, then `slide-down` the screen and change its background color. We also set an `animation-trigger` for each one of the animations so that they will be triggered by different triggers being activated.

We want the finished state of each animation to apply throughout, after it is reached, therefore it is important to set appropriate [`animation-fill-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode)
 values on the animations and `<animation-action>` values on the `animation-trigger` values to achieve this. We had to set an `animation-fill-mode` of `forwards` rather than `both` on the last animation because there is no `from` keyframe.

    body {
      overflow-x: hidden;
      font-family: "Helvetica", "Arial";
      font-size: 1.3rem;
      width: 80%;
      margin: 0 auto;
    }
    
    h1 {
      font-size: 3rem;
    }
    
    h2 {
      font-size: 2rem;
    }
    
    p {
      font-size: 1.5rem;
      line-height: 1.5;
    }
    
    section {
      background: red;
      color: #ffffff00;
      padding: 10px;
      width: 400px;
      height: 50px;
    }
    
    section p {
      font-size: 1.2rem;
    }
    

css

    section {
      position: fixed;
      left: 1em;
      top: 1em;
      height: 240px;
      background: red;
      width: 400px;
      transform-origin: top;
    
      animation:
        slide-from-right 1s both,
        reveal 1s both,
        slide-down 1s forwards;
    
      animation-trigger:
        --t1 play-forwards pause,
        --t2 play-forwards pause,
        --t3 play-forwards pause;
    }
    

Next, we create triggers on the `<div>` elements, setting their [`timeline-trigger-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-name)
 equal to the identifiers specified in the `<section>` elements' `animation-trigger` property values. This means that as the user scrolls, when each tracked `<div>` enters the scrollport, a different animation is activated. In this case, our tracked elements are invisible — they don't contain any useful content and are only here to create the triggers.

css

    #one {
      timeline-trigger: --t1 view();
    }
    
    #two {
      timeline-trigger: --t2 view();
    }
    
    #three {
      timeline-trigger: --t3 view();
    }
    

Finally, we define the animation [`@keyframes`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes)
 referenced in the `<section>` element's `animation` property earlier on.

css

    @keyframes slide-from-right {
      from {
        translate: 400%;
      }
      to {
        translate: 0;
      }
    }
    
    @keyframes reveal {
      from {
        color: #ffffff00;
        transform: scaleY(0.2);
      }
      to {
        color: white;
        transform: scaleY(1);
      }
    }
    
    @keyframes slide-down {
      to {
        translate: 0 100%;
        background: blue;
      }
    }
    

This example renders as follows:

Try carefully scrolling the example, and note how each animation is applied to the `<section>` when each `<div>` is scrolled to.

### [Multiple triggers for the same animation](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers/Using_scroll-triggered_animations#multiple_triggers_for_the_same_animation)

If you have an animated element, and you want to define triggers on multiple different elements that all trigger the same animation, you need to specify the same named animation multiple times on the animated element, and then give each instance of that animation a different trigger. See [Multiple triggers for the same animation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-trigger#multiple_triggers_for_the_same_animation)
 for more information.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers/Using_scroll-triggered_animations#see_also)

----------------------------------------------------------------------------------------------------------------------------------

*   [CSS animation triggers](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers)
     module
*   [CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations)
     module
*   [CSS scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations)
     module
*   [Using the Web Animations API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Animations_API/Using_the_Web_Animations_API)
    
*   [CSS scroll-triggered animations are coming!](https://developer.chrome.com/blog/scroll-triggered-animations "External link (opens in new tab)")
     on developer.chrome.com (2025)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 12, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers/Using_scroll-triggered_animations/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/animation_triggers/using_scroll-triggered_animations/index.md?plain=1 "Folder: en-us/web/css/guides/animation_triggers/using_scroll-triggered_animations (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FAnimation_triggers%2FUsing_scroll-triggered_animations&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fanimation_triggers%2Fusing_scroll-triggered_animations%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FAnimation_triggers%2FUsing_scroll-triggered_animations%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fanimation_triggers%2Fusing_scroll-triggered_animations%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F1a2a5b56a689b441ebf3be91b90f15746c5a5a01%0A*+Document+last+modified%3A+2026-10-12T05%3A04%3A35.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")