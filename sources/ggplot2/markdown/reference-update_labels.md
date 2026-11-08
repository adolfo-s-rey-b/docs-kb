[Skip to content](https://ggplot2.tidyverse.org/reference/update_labels.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Update axis/legend labels
=========================

Source: [`R/labels.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/labels.R)

`update_labels.Rd`

Update axis/legend labels

Usage[](https://ggplot2.tidyverse.org/reference/update_labels.html#ref-usage)

------------------------------------------------------------------------------

    update_labels(p, labels)

Arguments[](https://ggplot2.tidyverse.org/reference/update_labels.html#arguments)

----------------------------------------------------------------------------------

p[](https://ggplot2.tidyverse.org/reference/update_labels.html#arg-p)

plot to modify

labels[](https://ggplot2.tidyverse.org/reference/update_labels.html#arg-labels)

named list of new labels

Examples[](https://ggplot2.tidyverse.org/reference/update_labels.html#ref-examples)

------------------------------------------------------------------------------------

    p <- ggplot(mtcars, aes(mpg, wt)) + geom_point()
    update_labels(p, list(x = "New x"))
    
    update_labels(p, list(x = expression(x / y ^ 2)))
    
    update_labels(p, list(x = "New x", y = "New Y"))
    
    update_labels(p, list(colour = "Fail silently"))
    #> Ignoring unknown labels:
    #> • colour : "Fail silently"