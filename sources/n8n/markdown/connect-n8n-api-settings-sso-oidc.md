For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/connect/n8n-api/settings-sso-oidc.md)
.

Copy

On this page

Operations about OIDC SSO settings

### Retrieve the OIDC SSO configuration[](https://docs.n8n.io/connect/n8n-api/settings-sso-oidc#get-settings-sso-oidc)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/settings/sso/oidc

Retrieve the current OIDC SSO configuration, including every field exposed in the UI. The client secret is redacted on read and is never echoed back in plaintext. Requires the `oidc:manage` scope and the OIDC feature to be licensed.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Responses

200

Operation successful.

application/json

clientIdstringRequired

The client ID issued when registering n8n with the OIDC provider.

Example: `n8n-client`

clientSecretstringRequired

The client secret issued when registering n8n with the OIDC provider. Redacted on read when set; never echoed back in plaintext.

Example: `**hidden**`

discoveryEndpointstring · uriRequired

The OIDC provider's well-known discovery endpoint.

Example: `https://accounts.google.com/.well-known/openid-configuration`

loginEnabledbooleanRequired

Whether OIDC single sign-on is enabled.

Example: `false`

promptstring · enumRequired

The prompt parameter to use when authenticating with the OIDC provider.

Example: `select_account`Possible values: `none``login``consent``select_account``create`

authenticationContextClassReferencestring\[\]Required

ACR values to include in the authorization request (acr\_values parameter), in order of preference.

Example: `["mfa","pwd"]`

additionalScopesstringRequired

Additional scopes to request, space separated. n8n always requests `openid`, `profile` and `email`.

Example: `groups roles`

emailVerifiedRequiredbooleanRequired

Whether the identity provider must assert that the user's email address is verified before the login is accepted. When disabled, only an explicit negative assertion is rejected.

Example: `false`

rpInitiatedLogoutEnabledbooleanRequired

Whether signing out of n8n also ends the session at the OIDC provider via RP-Initiated Logout. When disabled, sign-out is local to n8n only.

Example: `false`

401

Unauthorized

403

Forbidden

get/settings/sso/oidc

HTTP

Copy

    GET /api/v1/settings/sso/oidc HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "clientId": "n8n-client",
      "clientSecret": "**hidden**",
      "discoveryEndpoint": "https://accounts.google.com/.well-known/openid-configuration",
      "loginEnabled": false,
      "prompt": "select_account",
      "authenticationContextClassReference": [\
        "mfa",\
        "pwd"\
      ],
      "additionalScopes": "groups roles",
      "emailVerifiedRequired": false,
      "rpInitiatedLogoutEnabled": false
    }

### Set the OIDC SSO configuration[](https://docs.n8n.io/connect/n8n-api/settings-sso-oidc#put-settings-sso-oidc)

put

/api/v1Current n8n instance (self-hosted built-in playground)

/settings/sso/oidc

Set the OIDC SSO configuration. The update takes effect exactly as it would from the UI, using the same validation. `clientId`, `clientSecret` and `discoveryEndpoint` are required; submit the redacted client secret sentinel to keep the stored secret unchanged. Requires the `oidc:manage` scope and the OIDC feature to be licensed. The client secret is redacted in the response. When the configuration is managed declaratively (via environment variables), the write is rejected with 409 and no changes are made.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Body

application/json

Full OIDC SSO configuration to set. This is a full replacement: every writable field must be provided. Partial updates are rejected. Submit the redacted secret sentinel for `clientSecret` to keep the stored secret unchanged.

clientIdstring · min: 1Required

The client ID issued when registering n8n with the OIDC provider.

Example: `n8n-client`

clientSecretstring · min: 1Required

The client secret issued when registering n8n with the OIDC provider. Submit the redacted sentinel value returned on read to keep the stored secret unchanged.

Example: `my-client-secret`

discoveryEndpointstring · uriRequired

The OIDC provider's well-known discovery endpoint.

Example: `https://accounts.google.com/.well-known/openid-configuration`

loginEnabledbooleanRequired

Whether OIDC single sign-on is enabled.

Example: `false`

promptstring · enumRequired

The prompt parameter to use when authenticating.

Example: `select_account`Possible values: `none``login``consent``select_account``create`

authenticationContextClassReferencestring\[\]Required

ACR values to include in the authorization request (acr\_values parameter), in order of preference. Use an empty array when unused.

Example: `["mfa","pwd"]`

additionalScopesstringRequired

Additional scopes to request, space separated. n8n always requests `openid`, `profile` and `email`. Use an empty string when unused.

Example: `groups roles`

emailVerifiedRequiredbooleanRequired

Whether the identity provider must assert that the user's email address is verified before the login is accepted. When disabled, only an explicit negative assertion is rejected.

Example: `false`

rpInitiatedLogoutEnabledbooleanRequired

Whether signing out of n8n also ends the session at the OIDC provider via RP-Initiated Logout. When disabled, sign-out is local to n8n only.

Example: `false`

Responses

200

Operation successful.

application/json

clientIdstringRequired

The client ID issued when registering n8n with the OIDC provider.

Example: `n8n-client`

clientSecretstringRequired

The client secret issued when registering n8n with the OIDC provider. Redacted on read when set; never echoed back in plaintext.

Example: `**hidden**`

discoveryEndpointstring · uriRequired

The OIDC provider's well-known discovery endpoint.

Example: `https://accounts.google.com/.well-known/openid-configuration`

loginEnabledbooleanRequired

Whether OIDC single sign-on is enabled.

Example: `false`

promptstring · enumRequired

The prompt parameter to use when authenticating with the OIDC provider.

Example: `select_account`Possible values: `none``login``consent``select_account``create`

authenticationContextClassReferencestring\[\]Required

ACR values to include in the authorization request (acr\_values parameter), in order of preference.

Example: `["mfa","pwd"]`

additionalScopesstringRequired

Additional scopes to request, space separated. n8n always requests `openid`, `profile` and `email`.

Example: `groups roles`

emailVerifiedRequiredbooleanRequired

Whether the identity provider must assert that the user's email address is verified before the login is accepted. When disabled, only an explicit negative assertion is rejected.

Example: `false`

rpInitiatedLogoutEnabledbooleanRequired

Whether signing out of n8n also ends the session at the OIDC provider via RP-Initiated Logout. When disabled, sign-out is local to n8n only.

Example: `false`

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

put/settings/sso/oidc

HTTP

Copy

    PUT /api/v1/settings/sso/oidc HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 338
    
    {
      "clientId": "n8n-client",
      "clientSecret": "my-client-secret",
      "discoveryEndpoint": "https://accounts.google.com/.well-known/openid-configuration",
      "loginEnabled": false,
      "prompt": "select_account",
      "authenticationContextClassReference": [\
        "mfa",\
        "pwd"\
      ],
      "additionalScopes": "groups roles",
      "emailVerifiedRequired": false,
      "rpInitiatedLogoutEnabled": false
    }

Test it

200

Operation successful.

Copy

    {
      "clientId": "n8n-client",
      "clientSecret": "**hidden**",
      "discoveryEndpoint": "https://accounts.google.com/.well-known/openid-configuration",
      "loginEnabled": false,
      "prompt": "select_account",
      "authenticationContextClassReference": [\
        "mfa",\
        "pwd"\
      ],
      "additionalScopes": "groups roles",
      "emailVerifiedRequired": false,
      "rpInitiatedLogoutEnabled": false
    }

[PreviousSettings Otel](https://docs.n8n.io/connect/n8n-api/settings-otel)
[NextSettings Sso Saml](https://docs.n8n.io/connect/n8n-api/settings-sso-saml)

Last updated 9 days ago

Was this helpful?