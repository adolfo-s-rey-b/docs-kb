[Skip to content](https://ggplot2.tidyverse.org/reference/combine_vars.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Take input data and define a mapping between faceting variables and ROW, COL and PANEL keys
===========================================================================================

Source: [`R/facet-.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/facet-.R)

`combine_vars.Rd`

Take input data and define a mapping between faceting variables and ROW, COL and PANEL keys

Usage[](https://ggplot2.tidyverse.org/reference/combine_vars.html#ref-usage)

-----------------------------------------------------------------------------

    combine_vars(data, env = emptyenv(), vars = NULL, drop = TRUE)

Arguments[](https://ggplot2.tidyverse.org/reference/combine_vars.html#arguments)

---------------------------------------------------------------------------------

data[](https://ggplot2.tidyverse.org/reference/combine_vars.html#arg-data)

A list of data.frames, the first being the plot data and the subsequent individual layer data

env[](https://ggplot2.tidyverse.org/reference/combine_vars.html#arg-env)

The environment the vars should be evaluated in

vars[](https://ggplot2.tidyverse.org/reference/combine_vars.html#arg-vars)

A list of quoted symbols matching columns in data

drop[](https://ggplot2.tidyverse.org/reference/combine_vars.html#arg-drop)

should missing combinations/levels be dropped

Value[](https://ggplot2.tidyverse.org/reference/combine_vars.html#value)

-------------------------------------------------------------------------

A data.frame with columns for PANEL, ROW, COL, and faceting vars