For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/connect/create-nodes/build-your-node/set-up-your-development-environment.md)
.

This document lists the essential dependencies for developing a node, as well as guidance on setting up your editor.

Requirements[](https://docs.n8n.io/connect/create-nodes/build-your-node/set-up-your-development-environment#requirements)

--------------------------------------------------------------------------------------------------------------------------

To build and test a node, you need:

*   Node.js and npm. Minimum Node.js version: 24. Refer to [nvm's installation instructions](https://github.com/nvm-sh/nvm)
     to install both using nvm (Node Version Manager) for Linux, Mac, and WSL (Windows Subsystem for Linux). For Windows users, refer to Microsoft's guide to [Install NodeJS on Windows](https://docs.microsoft.com/en-us/windows/dev-environment/javascript/nodejs-on-windows)
    .
    
*   The [`n8n-node` tool](https://docs.n8n.io/connect/create-nodes/build-your-node/using-the-n8n-node-tool)
    . Use it to create, build, and test your node. It includes n8n for local development, so you don't need a global n8n installation. Refer to [Run your node locally](https://docs.n8n.io/connect/create-nodes/test-your-node/run-your-node-locally)
     for the testing workflow. When [building verified community nodes](https://docs.n8n.io/integrations/community-nodes/building-community-nodes)
    , you must use `n8n-node`.
    

You should also have [git](https://git-scm.com/)
 installed. This allows you to clone and use the [n8n-nodes-starter](https://github.com/n8n-io/n8n-nodes-starter)
.

Editor setup[](https://docs.n8n.io/connect/create-nodes/build-your-node/set-up-your-development-environment#editor-setup)

--------------------------------------------------------------------------------------------------------------------------

n8n recommends using [VS Code](https://code.visualstudio.com/)
 as your editor.

Install these extensions:

*   [ESLint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint)
    
*   [EditorConfig](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig)
    
*   [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)
    

By using VS Code and these extensions, you get access to the n8n node linter's warnings as you code.

Related resources[](https://docs.n8n.io/connect/create-nodes/build-your-node/set-up-your-development-environment#related-resources)

------------------------------------------------------------------------------------------------------------------------------------

*   [Build your node](https://docs.n8n.io/connect/create-nodes/build-your-node)
    
*   [Using the n8n-node tool](https://docs.n8n.io/connect/create-nodes/build-your-node/using-the-n8n-node-tool)
    
*   [Tutorial: Build a declarative-style node](https://docs.n8n.io/connect/create-nodes/build-your-node/tutorial-build-a-declarative-style-node)
    
*   [Tutorial: Build a programmatic-style node](https://docs.n8n.io/connect/create-nodes/build-your-node/tutorial-build-a-programmatic-style-node)
    
*   [Reference](https://docs.n8n.io/connect/create-nodes/build-your-node/reference)
    

[PreviousBuild your node](https://docs.n8n.io/connect/create-nodes/build-your-node)
[NextUsing the n8n-node tool](https://docs.n8n.io/connect/create-nodes/build-your-node/using-the-n8n-node-tool)

Last updated 5 days ago

Was this helpful?