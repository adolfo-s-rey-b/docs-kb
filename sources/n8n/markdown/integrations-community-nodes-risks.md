For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/community-nodes/risks.md)
.

Installing community nodes from npm means you are installing unverified code from a public source into your n8n instance. This has some risks.

Risks include:

*   System security: community nodes have full access to the machine that n8n runs on, and can do anything, including malicious actions.
    
*   Data security: any community node that you use has access to data in your workflows.
    
*   Breaking changes: node developers may introduce breaking changes in new versions of their nodes. A breaking change is an update that breaks previous functionality. Depending on the node versioning approach that a node developer chooses, upgrading to a version with a breaking change could cause all workflows using the node to break. Be careful when upgrading your nodes.
    

**n8n vets verified community nodes**

In addition to publicly available community nodes from npm, n8n inspects some nodes and makes them available as [verified community node inside the nodes panel](https://docs.n8n.io/integrations/community-nodes/installation-and-management/install-verified-community-nodes)
. These nodes have to meet a set of data and system security requirements for approval.

Report bad community nodes[](https://docs.n8n.io/integrations/community-nodes/risks#report-bad-community-nodes)

----------------------------------------------------------------------------------------------------------------

You can report bad community nodes to \[security@n8n.io\](mailto: security@n8n.io)

Disable community nodes[](https://docs.n8n.io/integrations/community-nodes/risks#disable-community-nodes)

----------------------------------------------------------------------------------------------------------

If you are self-hosting n8n, you can disable community nodes by setting `N8N_COMMUNITY_PACKAGES_ENABLED` to `false`. On n8n Cloud, the instance owner can turn off **Verified community nodes** in **Instance settings** in the [n8n Cloud console](https://docs.n8n.io/deploy/use-n8n-cloud/use-the-cloud-console)
. See [troubleshooting](https://docs.n8n.io/integrations/community-nodes/troubleshooting)
 for more information.

[PreviousEnvironment variable installation](https://docs.n8n.io/integrations/community-nodes/installation-and-management/environment-variable-installation)
[NextBlocklist](https://docs.n8n.io/integrations/community-nodes/blocklist)

Last updated 10 days ago

Was this helpful?