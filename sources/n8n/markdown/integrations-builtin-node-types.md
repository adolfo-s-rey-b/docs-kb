For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/node-types.md)
.

This section contains the node library: reference documentation for every built-in node in n8n, and their credentials.

### Node operations: Triggers and Actions[](https://docs.n8n.io/integrations/builtin/node-types#node-operations-triggers-and-actions)

When you add a node to a workflow, n8n displays a list of available operations. An operation is something a node does, such as getting or sending data.

There are two types of operation:

*   Triggers start a workflow in response to specific events or conditions in your services. When you select a Trigger, n8n adds a trigger node to your workflow, with the Trigger operation you chose pre-selected. When you search for a node in n8n, Trigger operations have a bolt icon ![Trigger icon](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2738857267-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FGixZThfitWP21x2gQFpD%252Fuploads%252Fgit-blob-4829d6f9de935beb784ab8cce7a682aaaf30432c%252Ftrigger.png%3Falt%3Dmedia&width=26&dpr=3&quality=100&sign=654467905ab06631af4e1f5367be046d&sv=3).
    
*   Actions are operations that represent specific tasks within a workflow, which you can use to manipulate data, perform operations on external systems, and trigger events in other systems as part of your workflows. When you select an Action, n8n adds a node to your workflow, with the Action operation you chose pre-selected.
    

Core nodes[](https://docs.n8n.io/integrations/builtin/node-types#core-nodes)

-----------------------------------------------------------------------------

Core nodes can be actions or triggers. Whereas most nodes connect to a specific external service, core nodes provide functionality such as logic, scheduling, or generic API calls.

Cluster nodes[](https://docs.n8n.io/integrations/builtin/node-types#cluster-nodes)

-----------------------------------------------------------------------------------

[Cluster nodes](https://docs.n8n.io/key-concept-glossary#cluster-node-n8n)
 are node groups that work together to provide functionality in an n8n workflow. Instead of using a single node, you use a [root node](https://docs.n8n.io/key-concept-glossary#root-node-n8n)
 and one or more [sub-nodes](https://docs.n8n.io/key-concept-glossary#sub-node-n8n)
 that extend the functionality of the node.

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2738857267-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FGixZThfitWP21x2gQFpD%252Fuploads%252Fgit-blob-eeb624d06de1a0d1328156fc353875aa0b8cdebe%252Froot-sub-nodes.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=02bf310fdc0561f34d191fe9858f9fa6&sv=3)

A workflow diagram with one root node connected to two sub-nodes

Credentials[](https://docs.n8n.io/integrations/builtin/node-types#credentials)

-------------------------------------------------------------------------------

External services need a way to identify and authenticate users. This data can range from an API key over an email/password combination to a long multi-line private key. You can save these in n8n as credentials.

Nodes in n8n can then request that credential information. As another layer of security, only node types with specific access rights can access the credentials.

To make sure that the data is secure, it gets saved to the database encrypted. n8n uses a random personal encryption key, which it automatically generates on the first run of n8n and then saves under `~/.n8n/config`.

To learn more about creating, managing, and sharing credentials, refer to [Manage credentials](https://docs.n8n.io/build/understand-workflows/create-and-edit-credentials)
.

Community nodes[](https://docs.n8n.io/integrations/builtin/node-types#community-nodes)

---------------------------------------------------------------------------------------

n8n supports community nodes. Refer to [Community nodes](https://docs.n8n.io/integrations/community-nodes/installation-and-management)
 for guidance on installing and using these nodes.

For help building and publishing your own community nodes to [npm](https://www.npmjs.com/)
, refer to [Create nodes](https://docs.n8n.io/connect/create-nodes/overview)
 for more information.

See [Built-in nodes](https://docs.n8n.io/integrations/builtin)
 for other integration topics.

[PreviousBuilt-in nodes](https://docs.n8n.io/integrations/builtin)
[NextCore nodes](https://docs.n8n.io/integrations/builtin/core-nodes)

Last updated 10 days ago

Was this helpful?