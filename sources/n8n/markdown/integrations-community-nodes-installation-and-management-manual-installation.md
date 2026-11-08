For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/community-nodes/installation-and-management/manual-installation.md)
.

You can manually install community nodes from the npm registry on self-hosted n8n.

You need to manually install community nodes in the following circumstances:

*   Your n8n instance runs in queue mode.
    
*   You want to install [private packages](https://docs.npmjs.com/creating-and-publishing-private-packages)
    .
    

Install a community node[](https://docs.n8n.io/integrations/community-nodes/installation-and-management/manual-installation#install-a-community-node)

------------------------------------------------------------------------------------------------------------------------------------------------------

Access your Docker shell:

Copy

    docker exec -it n8n sh

Create `~/.n8n/nodes` if it doesn't already exist, and navigate into it:

Copy

    mkdir ~/.n8n/nodes
    cd ~/.n8n/nodes

Install the node:

Copy

    npm i n8n-nodes-nodeName

Then restart n8n.

Uninstall a community node[](https://docs.n8n.io/integrations/community-nodes/installation-and-management/manual-installation#uninstall-a-community-node)

----------------------------------------------------------------------------------------------------------------------------------------------------------

Access your Docker shell:

Copy

    docker exec -it n8n sh

Run npm uninstall:

Copy

    npm uninstall n8n-nodes-nodeName

Upgrade a community node[](https://docs.n8n.io/integrations/community-nodes/installation-and-management/manual-installation#upgrade-a-community-node)

------------------------------------------------------------------------------------------------------------------------------------------------------

**Breaking changes in versions**

Node developers may introduce breaking changes in new versions of their nodes. A breaking change is an update that breaks previous functionality. Depending on the node versioning approach that a node developer chooses, upgrading to a version with a breaking change could cause all workflows using the node to break. Be careful when upgrading your nodes. If you find that an upgrade causes issues, you can [downgrade](https://docs.n8n.io/integrations/community-nodes/installation-and-management/manual-installation#upgrade-or-downgrade-to-a-specific-version)
.

### Upgrade to the latest version[](https://docs.n8n.io/integrations/community-nodes/installation-and-management/manual-installation#upgrade-to-the-latest-version)

Access your Docker shell:

Copy

    docker exec -it n8n sh

Run npm update:

Copy

    npm update n8n-nodes-nodeName

### Upgrade or downgrade to a specific version[](https://docs.n8n.io/integrations/community-nodes/installation-and-management/manual-installation#upgrade-or-downgrade-to-a-specific-version)

Access your Docker shell:

Copy

    docker exec -it n8n sh

Run npm uninstall to remove the current version:

Copy

    npm uninstall n8n-nodes-nodeName

Run npm install with the version specified:

Copy

    # Replace 2.1.0 with your version number <a href="#replace-210-with-your-version-number" id="replace-210-with-your-version-number"></a>
    npm install n8n-nodes-nodeName@2.1.0

[PreviousGUI installation](https://docs.n8n.io/integrations/community-nodes/installation-and-management/gui-installation)
[NextEnvironment variable installation](https://docs.n8n.io/integrations/community-nodes/installation-and-management/environment-variable-installation)

Last updated 10 days ago

Was this helpful?