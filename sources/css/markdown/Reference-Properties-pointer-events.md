*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/pointer-events#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/pointer-events#mdn-search)
    

`pointer-events` CSS property
=============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/pointer-events#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`pointer-events`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets under what circumstances (if any) a particular graphic element can become the [target](https://developer.mozilla.org/en-US/docs/Web/API/Event/target)
 of pointer events.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/pointer-events#try_it)

------------------------------------------------------------------------------------------------------

    pointer-events: auto;
    

    pointer-events: none;
    

    pointer-events: stroke; /* SVG-only */
    

    pointer-events: fill; /* SVG-only */
    

    <section class="flex-column" id="default-example">
      <div id="example-element">
        <p>
          <a href="#">example link</a>
        </p>
        <p>
          <svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <a xlink:href="#">
              <circle
                cx="50"
                cy="50"
                fill="#3E6E84"
                r="40"
                stroke="#ffb500"
                stroke-width="5"></circle>
              <text fill="white" text-anchor="middle" x="50" y="55">SVG</text>
            </a>
          </svg>
        </p>
      </div>
    </section>
    

    #example-element {
      font-weight: bold;
    }
    
    #example-element a {
      color: #009e5f;
    }
    
    #example-element svg {
      width: 10em;
      height: 10em;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/pointer-events#syntax)

------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    pointer-events: auto;
    pointer-events: none;
    
    /* Values used in SVGs */
    pointer-events: visiblePainted;
    pointer-events: visibleFill;
    pointer-events: visibleStroke;
    pointer-events: visible;
    pointer-events: painted;
    pointer-events: fill;
    pointer-events: stroke;
    pointer-events: bounding-box;
    pointer-events: all;
    
    /* Global values */
    pointer-events: inherit;
    pointer-events: initial;
    pointer-events: revert;
    pointer-events: revert-layer;
    pointer-events: unset;
    

The `pointer-events` property is specified as a single keyword chosen from the list of values below.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/pointer-events#values)

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/pointer-events#auto)

The element behaves as it would if the `pointer-events` property were not specified. In SVG content, this value and the value `visiblePainted` have the same effect.

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/pointer-events#none)

The element is generally not the [target](https://developer.mozilla.org/en-US/docs/Web/API/Event/target)
 of pointer events, with the exception of `pointerenter` and `pointerleave` events fired at the element or its descendants. Note that pointer events targeted at descendants (that don't set `pointer-events` to `none`) will still trigger event listeners on this parent element during the event capture and [bubble](https://developer.mozilla.org/en-US/docs/Web/API/Event/bubbles)
 phases.

**Note:** The `pointerenter` and `pointerleave` events are fired when a pointing device is moved into an element or one of its descendants. So, even if `pointer-events: none` is set on the parent and not set on children, the events are triggered on the parent after the pointer is moved in or out of a descendant.

#### SVG only (experimental for HTML)

[`visiblePainted`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/pointer-events#visiblepainted)

SVG only (experimental for HTML). The element can only be the target of a pointer event when the `visibility` property is set to `visible` and e.g., when a mouse cursor is over the interior (i.e., 'fill') of the element and the `fill` property is set to a value other than `none`, or when a mouse cursor is over the perimeter (i.e., 'stroke') of the element and the `stroke` property is set to a value other than `none`.

[`visibleFill`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/pointer-events#visiblefill)

SVG only. The element can only be the target of a pointer event when the `visibility` property is set to `visible` and when e.g., a mouse cursor is over the interior (i.e., fill) of the element. The value of the `fill` property does not affect event processing.

[`visibleStroke`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/pointer-events#visiblestroke)

SVG only. The element can only be the target of a pointer event when the `visibility` property is set to `visible` and e.g., when the mouse cursor is over the perimeter (i.e., stroke) of the element. The value of the `stroke` property does not affect event processing.

[`visible`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/pointer-events#visible)

SVG only (experimental for HTML). The element can be the target of a pointer event when the `visibility` property is set to `visible` and e.g., the mouse cursor is over either the interior (i.e., fill) or the perimeter (i.e., stroke) of the element. The values of the `fill` and `stroke` do not affect event processing.

[`painted`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/pointer-events#painted)

SVG only (experimental for HTML). The element can only be the target of a pointer event when e.g., the mouse cursor is over the interior (i.e., 'fill') of the element and the `fill` property is set to a value other than `none`, or when the mouse cursor is over the perimeter (i.e., 'stroke') of the element and the `stroke` property is set to a value other than `none`. The value of the `visibility` property does not affect event processing.

[`fill`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/pointer-events#fill)

SVG only. The element can only be the target of a pointer event when the pointer is over the interior (i.e., fill) of the element. The values of the `fill` and `visibility` properties do not affect event processing.

[`stroke`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/pointer-events#stroke)

SVG only. The element can only be the target of a pointer event when the pointer is over the perimeter (i.e., stroke) of the element. The values of the `stroke` and `visibility` properties do not affect event processing.

[`bounding-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/pointer-events#bounding-box)

SVG only. The element can only be the target of a pointer event when the pointer is over the [bounding box](https://developer.mozilla.org/en-US/docs/Glossary/Bounding_box)
 of the element.

[`all`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/pointer-events#all)

SVG only (experimental for HTML). The element can only be the target of a pointer event when the pointer is over the interior (i.e., fill) or the perimeter (i.e., stroke) of the element. The values of the `fill`, `stroke`, and `visibility` properties do not affect event processing.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/pointer-events#description)

----------------------------------------------------------------------------------------------------------------

When this property is unspecified, the same characteristics of the `visiblePainted` value apply to SVG content.

In addition to indicating that the element is not the target of pointer events, the value `none` instructs the pointer event to go "through" the element and target whatever is "underneath" that element instead.

Note that preventing an element from being the target of pointer events by using `pointer-events` does _not_ necessarily mean that pointer event listeners on that element _cannot_ or _will not_ be triggered. If one of the element's children has `pointer-events` explicitly set to _allow_ that child to be the target of pointer events, then any events targeting that child will pass through the parent as the event travels along the parent chain, and trigger event listeners on the parent as appropriate. Of course any pointer activity at a point on the screen that is covered by the parent but not by the child will not be caught by either the child or the parent (it will go "through" the parent and target whatever is underneath).

Elements with `pointer-events: none` will still receive focus through sequential keyboard navigation using the Tab key.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/pointer-events#formal_definition)

----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/pointer-events#formal_syntax)

--------------------------------------------------------------------------------------------------------------------

pointer-events =   
  auto            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  bounding-box    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  visiblePainted  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  visibleFill     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  visibleStroke   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  visible         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  painted         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  fill            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  stroke          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  all             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  none              

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/pointer-events#examples)

----------------------------------------------------------------------------------------------------------

### [Disabling pointer events on all images](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/pointer-events#disabling_pointer_events_on_all_images)

This example disables pointer events (clicking, dragging, hovering, etc.) on all images.

css

    img {
      pointer-events: none;
    }
    

### [Disabling pointer events on a single link](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/pointer-events#disabling_pointer_events_on_a_single_link)

This example disables pointer events on the link to `http://example.com`.

#### HTML

html

    <ul>
      <li><a href="https://developer.mozilla.org">MDN</a></li>
      <li><a href="http://example.com">example.com</a></li>
    </ul>
    

#### CSS

css

    a[href="http://example.com"] {
      pointer-events: none;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/pointer-events#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Basic User Interface Module Level 4  <br>\# pointer-events-control](https://drafts.csswg.org/css-ui/#pointer-events-control) |
| [Scalable Vector Graphics (SVG) 2  <br>\# PointerEventsProperty](https://w3c.github.io/svgwg/svg2-draft/interact.html#PointerEventsProperty) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/pointer-events#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/pointer-events#see_also)

----------------------------------------------------------------------------------------------------------

*   [`user-select`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-select)
    
*   SVG [`pointer-events`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/pointer-events)
     attribute
*   SVG [`visibility`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/visibility)
     attribute
*   [`PointerEvent`](https://developer.mozilla.org/en-US/docs/Web/API/PointerEvent)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/pointer-events/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/pointer-events/index.md?plain=1 "Folder: en-us/web/css/reference/properties/pointer-events (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fpointer-events&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fpointer-events%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fpointer-events%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fpointer-events%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb9c07e549a6e66272c589a254ebcd5a8c91f37a5%0A*+Document+last+modified%3A+2026-08-14T00%3A05%3A09.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")