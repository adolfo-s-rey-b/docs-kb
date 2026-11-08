For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/run-security-audits.md)
.

You can run a security audit on your n8n instance, to detect common security issues.

How do I run a security audit in n8n?[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/run-security-audits#run-an-audit)

-------------------------------------------------------------------------------------------------------------------------------------

You can run an audit using the CLI, the public API, or the n8n node.

### CLI[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/run-security-audits#cli)

Run `n8n audit`.

### API[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/run-security-audits#api)

Make a `POST` call to the `/audit` endpoint. You must authenticate as the instance owner.

### n8n node[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/run-security-audits#n8n-node)

Add the [n8n node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.n8n)
 to your workflow. Select **Resource** > **Audit** and **Operation** > **Generate**.

What's in the security audit report?[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/run-security-audits#report-contents)

---------------------------------------------------------------------------------------------------------------------------------------

The audit generates five risk reports:

### Credentials[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/run-security-audits#credentials)

This report shows:

*   Credentials not used in a workflow.
    
*   Credentials not used in an active workflow.
    
*   Credentials not use in a recently active workflow.
    

### Database[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/run-security-audits#database)

This report shows:

*   Expressions used in **Execute Query** fields in SQL nodes.
    
*   Expressions used in **Query Parameters** fields in SQL nodes.
    
*   Unused **Query Parameters** fields in SQL nodes.
    

### File system[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/run-security-audits#file-system)

This report lists nodes that interact with the file system.

### Nodes[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/run-security-audits#nodes)

This report shows:

*   Official risky nodes. These are n8n built in nodes. You can use them to fetch and run any code on the host system, which exposes the instance to exploits. You can view the list in [n8n code | Audit constants](https://github.com/n8n-io/n8n/blob/master/packages/cli/src/security-audit/constants.ts#L51)
    , under `OFFICIAL_RISKY_NODE_TYPES`.
    
*   Community nodes.
    
*   Custom nodes.
    

### Instance[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/run-security-audits#instance)

This report shows:

*   Unprotected webhooks in the instance.
    
*   Missing security settings
    
*   If your instance is outdated.
    

Related resources[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/run-security-audits#related-resources)

----------------------------------------------------------------------------------------------------------------------

*   [Security](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security)
    

[PreviousConfigure SSO](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/configure-sso)
[NextDisable the public API](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/disable-the-public-api)

Last updated 10 days ago

Was this helpful?