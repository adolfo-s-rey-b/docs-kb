For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/code-in-n8n/cookbook/built-in-methods-and-variables-examples/vars.md)
.

**Feature availability**

`vars` is available on:

*   **n8n Cloud:** Pro, Enterprise
    
*   **Self-hosted:** Business, Enterprise
    

You need access to the n8n instance owner account to create variables.

`vars` contains all [Variables](https://docs.n8n.io/build/code-in-n8n/define-custom-variables)
 for the active environment. It's read-only: you can access variables using `vars`, but must set them using the UI.

JavaScript

Python

Copy

    // Access a variable
    $vars.<variable-name>

Copy

    # Access a variable
    _vars.<variable-name>

`**vars**` **and** `**env**`

`vars` gives access to user-created variables. It's part of the [Environments](https://docs.n8n.io/administer/use-source-control-and-environments)
 feature. `env` gives access to the [configuration environment variables](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables)
 for your n8n instance.

Related resources[](https://docs.n8n.io/build/code-in-n8n/cookbook/built-in-methods-and-variables-examples/vars#related-resources)

-----------------------------------------------------------------------------------------------------------------------------------

*   [Built-in methods and variables examples](https://docs.n8n.io/build/code-in-n8n/cookbook/built-in-methods-and-variables-examples)
    

[Previous(node-name).all](https://docs.n8n.io/build/code-in-n8n/cookbook/built-in-methods-and-variables-examples/node-name-.all)
[NextCode node](https://docs.n8n.io/build/code-in-n8n/cookbook/code-node)

Last updated 10 days ago

Was this helpful?