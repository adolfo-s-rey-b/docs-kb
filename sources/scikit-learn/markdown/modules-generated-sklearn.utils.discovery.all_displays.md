[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.discovery.all_displays.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.discovery.all_displays.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.discovery.all_displays.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.discovery.all_displays.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.discovery.all_displays.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.discovery.all_displays.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.discovery.all_displays.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.discovery.all_displays.html)

Collapse Sidebar Expand Sidebar

all\_displays[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.discovery.all_displays.html#all-displays "Link to this heading")

==================================================================================================================================================

sklearn.utils.discovery.all\_displays()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/discovery.py#L153)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.discovery.all_displays.html#sklearn.utils.discovery.all_displays "Link to this definition")

Get a list of all displays from `sklearn`.

Returns:

**displays**list of tuples

List of (name, class), where `name` is the display class name as string and `class` is the actual type of the class.

Examples

\>>> from sklearn.utils.discovery import all\_displays
\>>> displays \= all\_displays()
\>>> displays\[0\]
('CalibrationDisplay', <class 'sklearn.calibration.CalibrationDisplay'>)

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)