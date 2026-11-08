For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/block-specific-nodes.md)
.

For security reasons, you may want to block your users from accessing or working with specific n8n nodes. This is helpful if your users might be untrustworthy.

Use the `NODES_EXCLUDE` environment variable to prevent your users from accessing specific nodes.

To block nodes per project, or without restarting n8n, use [node type policies](https://docs.n8n.io/administer/manage-users-and-access/control-node-availability)
 instead. `NODES_EXCLUDE` stops n8n from loading a node at all, so it's the stronger option for nodes that must never run.

Exclude nodes[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/block-specific-nodes#exclude-nodes)

---------------------------------------------------------------------------------------------------------------

Update your `NODES_EXCLUDE` environment variable to include an array of strings containing any nodes you want to block your users from using.

For example, setting the variable this way:

Copy

    NODES_EXCLUDE: "[\"n8n-nodes-base.executeCommand\", \"n8n-nodes-base.readWriteFile\"]"

Blocks the [Execute Command](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executecommand)
 and [Read/Write Files from Disk](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.readwritefile)
 nodes.

Your n8n users won't be able to search for or use these nodes.

Suggested nodes to block[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/block-specific-nodes#suggested-nodes-to-block)

-------------------------------------------------------------------------------------------------------------------------------------

The nodes that can pose security risks vary based on your use case and user profile. Here are some nodes you might want to start with:

*   [Execute Command](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executecommand)
    
*   [Read/Write Files from Disk](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.readwritefile)
    

Enable nodes that are blocked by default[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/block-specific-nodes#enable-nodes-that-are-blocked-by-default)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Some nodes, like Execute Command, are blocked by default. Remove them from the exclude list to enable them:

Copy

    NODES_EXCLUDE: "[]"

Related resources[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/block-specific-nodes#related-resources)

-----------------------------------------------------------------------------------------------------------------------

*   [Security](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security)
    : audit, harden, and restrict a self-hosted instance.
    
*   [Nodes environment variables](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/nodes)
    : more information on this environment variable.
    
*   [Configuration](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration)
    : how to set environment variables.
    

[PreviousControl telemetry](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/control-telemetry)
[NextHarden task runners](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/harden-task-runners)

Last updated 10 days ago

Was this helpful?