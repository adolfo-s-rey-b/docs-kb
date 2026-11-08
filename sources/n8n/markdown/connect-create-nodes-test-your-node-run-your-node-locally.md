For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/connect/create-nodes/test-your-node/run-your-node-locally.md)
.

You can test your node as you build it by running it in a local n8n instance with the [`n8n-node` tool](https://docs.n8n.io/connect/create-nodes/build-your-node/using-the-n8n-node-tool)
. `n8n-node` includes n8n, so you don't need a global n8n installation.

1.  In your project's root directory, run the `dev` command:
    
    Copy
    
        npm run dev
    
    This runs `n8n-node dev`, which builds your node, links it into the n8n custom nodes directory, starts a local n8n instance with your node loaded, and rebuilds your node when you change a file.
    

**Custom nodes directory**

Copy

    `n8n-node dev` uses its own n8n user folder, `.n8n-node-cli`, so it doesn't touch an existing n8n installation. The default location depends on your operating system:
    - For Windows: `C:\Users\<username>\.n8n-node-cli\.n8n\custom`
    - For Linux: `/home/<username>/.n8n-node-cli/.n8n/custom`
    - For macOS: `/Users/<username>/.n8n-node-cli/.n8n/custom`
    
    To test against an n8n instance you run yourself, pass `--external-n8n` and set `--custom-user-folder <path>` to that instance's user folder (the parent of its `.n8n` directory). Set `N8N_DEV_RELOAD=true` on that instance so it picks up your changes.
    
    Note: `.n8n-node-cli` and `.n8n` are hidden folders, so your file browser may not show them.

1.  Open `http://localhost:5678` in your browser and sign in to your n8n instance.
    
2.  Open a workflow and search for your node in the nodes panel.
    

**Node names**

Copy

    Make sure you search using the node name, not the package name. For example, if your npm package name is `n8n-nodes-weather-nodes`, and the package contains nodes named `rain`, `sun`, `snow`, you should search for `rain`, not `weather-nodes`.

Add the node to your workflow and test it as you develop. To stop n8n, press `ctrl` + `c`.

Related resources[](https://docs.n8n.io/connect/create-nodes/test-your-node/run-your-node-locally#related-resources)

---------------------------------------------------------------------------------------------------------------------

*   [Test your node](https://docs.n8n.io/connect/create-nodes/test-your-node)
    
*   [Node linter](https://docs.n8n.io/connect/create-nodes/test-your-node/node-linter)
    
*   [Troubleshooting](https://docs.n8n.io/connect/create-nodes/test-your-node/troubleshooting)
    

[PreviousTest your node](https://docs.n8n.io/connect/create-nodes/test-your-node)
[NextNode linter](https://docs.n8n.io/connect/create-nodes/test-your-node/node-linter)

Last updated 10 days ago

Was this helpful?