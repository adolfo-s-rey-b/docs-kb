*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle#mdn-search)
    

`<angle>` CSS type
==================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<angle>`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
 represents an angle value expressed in degrees, gradians, radians, or turns. It is used, for example, in [`<gradient>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient)
s and in some [`transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
 functions.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle#try_it)

-----------------------------------------------------------------------------------------

    transform: rotate(45deg);
    

    transform: rotate(3.1416rad);
    

    transform: rotate(-50grad);
    

    transform: rotate(1.75turn);
    

    <section class="default-example" id="default-example">
      <div class="transition-all" id="example-element">
        This box can rotate to different angles.
      </div>
    </section>
    

    #example-element {
      background-color: #0118f3;
      padding: 0.75em;
      width: 180px;
      height: 120px;
      color: white;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle#syntax)

-----------------------------------------------------------------------------------------

The `<angle>` data type consists of a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 followed by one of the units listed below. As with all dimensions, there is no space between the unit literal and the number. While some legacy uses accept a unitless `0`, you should always include a unit for zero values, such as: `0deg`, `0grad`, `0rad`, or `0turn`.

Optionally, it may be preceded by a single `+` or `-` sign. Positive numbers represent clockwise angles, while negative numbers represent counterclockwise angles. For static properties of a given unit, any angle can be represented by various equivalent values. For example, `90deg` equals `-270deg`, and `1turn` equals `4turn`. For dynamic properties, like when applying an [`animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
 or [`transition`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition)
, the effect will nevertheless be different.

### [Units](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle#units)

[`deg`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle#deg)

Represents an angle in [degrees](https://en.wikipedia.org/wiki/Degree_%28angle%29 "External link (opens in new tab)")
. One full circle is `360deg`. Examples: `0deg`, `90deg`, `14.23deg`.

[`grad`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle#grad)

Represents an angle in [gradians](https://en.wikipedia.org/wiki/Gradian "External link (opens in new tab)")
. One full circle is `400grad`. Examples: `0grad`, `100grad`, `38.8grad`.

[`rad`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle#rad)

Represents an angle in [radians](https://en.wikipedia.org/wiki/Radian "External link (opens in new tab)")
. One full circle is 2π radians which approximates to `6.2832rad`. `1rad` is 180/π degrees. Examples: `0rad`, `1.0708rad`, `6.2832rad`.

[`turn`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle#turn)

Represents an angle in a number of turns. One full circle is `1turn`. Examples: `0turn`, `0.25turn`, `1.2turn`.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle#examples)

---------------------------------------------------------------------------------------------

### [Setting a clockwise right angle](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle#setting_a_clockwise_right_angle)

|     |     |
| --- | --- |
| ![A diagram showing a clockwise 90-degree rotation along a circle by moving from the topmost point to the rightmost point.](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle/angle90.png) | `90deg = 100grad = 0.25turn ≈ 1.5708rad` |

### [Setting a flat angle](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle#setting_a_flat_angle)

|     |     |
| --- | --- |
| ![A diagram showing a clockwise 180-degree rotation along a circle by moving from the topmost point to the bottommost point.](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle/angle180.png) | `180deg = 200grad = 0.5turn ≈ 3.1416rad` |

### [Setting a counterclockwise right angle](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle#setting_a_counterclockwise_right_angle)

|     |     |
| --- | --- |
| ![A diagram showing a counterclockwise 90-degree rotation along a circle by moving from the topmost point to the leftmost point.](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle/angleminus90.png) | `-90deg = -100grad = -0.25turn ≈ -1.5708rad` |

### [Setting a null angle](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle#setting_a_null_angle)

|     |     |
| --- | --- |
| ![A diagram showing a 0-degree rotation. There is no movement.](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle/angle0.png) | `0deg = 0grad = 0turn = 0rad` |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle#specifications)

---------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Values and Units Module Level 4  <br>\# angles](https://drafts.csswg.org/css-values/#angles) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle#see_also)

---------------------------------------------------------------------------------------------

*   [CSS data types](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
    
*   The [`<gradient>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient)
     type
*   CSS rotation transforms: [`rotate()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate)
    , [`rotate3d()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate3d)
    , [`rotateX()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotateX)
    , [`rotateY()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotateY)
    , and [`rotateZ()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotateZ)
    
*   [CSS transforms](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transforms)
    
*   [Using CSS transforms](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transforms/Using)
    
*   [Using CSS gradients](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Images/Using_gradients)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on May 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/angle/index.md?plain=1 "Folder: en-us/web/css/reference/values/angle (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fangle&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fangle%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fangle%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fangle%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F06d31d3fa6fbe7ecf0d2c3f3f0b14e1d5fe874c5%0A*+Document+last+modified%3A+2026-05-17T23%3A35%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")