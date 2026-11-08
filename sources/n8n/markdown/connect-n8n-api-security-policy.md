For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/connect/n8n-api/security-policy.md)
.

Copy

On this page

Operations about the instance security policy settings

### Retrieve the security policy[](https://docs.n8n.io/connect/n8n-api/security-policy#get-settings-security-policy)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/settings/security-policy

Retrieve the instance security policy: personal-space publishing and sharing, the execution-data redaction enforcement floor, and the read-only usage counts shown in the UI. Requires the `securitySettings:manage` scope and the Personal Space Policy feature to be licensed.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Responses

200

Operation successful.

application/json

personalSpacePublishingbooleanRequired

Whether members may publish workflows and agents from their personal space.

Example: `true`

personalSpaceSharingbooleanRequired

Whether members may share workflows and credentials from their personal space.

Example: `true`

publishedPersonalWorkflowsCountintegerRead-onlyRequired

Number of currently published personal workflows, shown for awareness before tightening the policy.

Example: `3`

sharedPersonalWorkflowsCountintegerRead-onlyRequired

Number of personal workflows currently shared with other users.

Example: `5`

sharedPersonalCredentialsCountintegerRead-onlyRequired

Number of personal credentials currently shared with other users.

Example: `2`

redactionEnforcementobjectRequired

Show properties

401

Unauthorized

403

Forbidden

get/settings/security-policy

HTTP

Copy

    GET /api/v1/settings/security-policy HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "personalSpacePublishing": true,
      "personalSpaceSharing": true,
      "publishedPersonalWorkflowsCount": 3,
      "sharedPersonalWorkflowsCount": 5,
      "sharedPersonalCredentialsCount": 2,
      "redactionEnforcement": {
        "floor": "production"
      }
    }

### Set the security policy[](https://docs.n8n.io/connect/n8n-api/security-policy#put-settings-security-policy)

put

/api/v1Current n8n instance (self-hosted built-in playground)

/settings/security-policy

Replace the instance security policy with the provided full object. Every writable field must be sent. Read-only usage counts from GET are ignored if included, so a GET response can be sent back as a PUT body. The update takes effect exactly as it would from the UI, using the same validation. Requires the `securitySettings:manage` scope and the Personal Space Policy feature to be licensed. When the group is managed via environment variables, the write is rejected with 409 and no changes are made; a read still returns the current values.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Body

application/json

Full security policy. All writable fields must be provided; partial updates are not supported.

personalSpacePublishingbooleanRequired

Whether members may publish workflows and agents from their personal space.

Example: `false`

personalSpaceSharingbooleanRequired

Whether members may share workflows and credentials from their personal space.

Example: `false`

redactionEnforcementobjectRequired

Show properties

publishedPersonalWorkflowsCountintegerOptional

Read-only usage count returned by GET. Ignored on write so a GET response can be sent back as a PUT body.

sharedPersonalWorkflowsCountintegerOptional

Read-only usage count returned by GET. Ignored on write so a GET response can be sent back as a PUT body.

sharedPersonalCredentialsCountintegerOptional

Read-only usage count returned by GET. Ignored on write so a GET response can be sent back as a PUT body.

Responses

200

Operation successful.

application/json

personalSpacePublishingbooleanRequired

Whether members may publish workflows and agents from their personal space.

Example: `true`

personalSpaceSharingbooleanRequired

Whether members may share workflows and credentials from their personal space.

Example: `true`

publishedPersonalWorkflowsCountintegerRead-onlyRequired

Number of currently published personal workflows, shown for awareness before tightening the policy.

Example: `3`

sharedPersonalWorkflowsCountintegerRead-onlyRequired

Number of personal workflows currently shared with other users.

Example: `5`

sharedPersonalCredentialsCountintegerRead-onlyRequired

Number of personal credentials currently shared with other users.

Example: `2`

redactionEnforcementobjectRequired

Show properties

400

The request is invalid or provides malformed data.

401

Unauthorized

403

Forbidden

409

Conflict

415

Unsupported media type.

put/settings/security-policy

HTTP

Copy

    PUT /api/v1/settings/security-policy HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 212
    
    {
      "personalSpacePublishing": false,
      "personalSpaceSharing": false,
      "redactionEnforcement": {
        "floor": "production"
      },
      "publishedPersonalWorkflowsCount": 1,
      "sharedPersonalWorkflowsCount": 1,
      "sharedPersonalCredentialsCount": 1
    }

Test it

200

Operation successful.

Copy

    {
      "personalSpacePublishing": true,
      "personalSpaceSharing": true,
      "publishedPersonalWorkflowsCount": 3,
      "sharedPersonalWorkflowsCount": 5,
      "sharedPersonalCredentialsCount": 2,
      "redactionEnforcement": {
        "floor": "production"
      }
    }

[PreviousRole Mapping Rule](https://docs.n8n.io/connect/n8n-api/role-mapping-rule)
[NextSettings Ldap](https://docs.n8n.io/connect/n8n-api/settings-ldap)

Last updated 9 days ago

Was this helpful?