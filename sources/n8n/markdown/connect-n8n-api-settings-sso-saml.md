For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/connect/n8n-api/settings-sso-saml.md)
.

Copy

On this page

Operations about SAML SSO settings

### Retrieve the SAML SSO configuration[](https://docs.n8n.io/connect/n8n-api/settings-sso-saml#get-settings-sso-saml)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/settings/sso/saml

Retrieve the current SAML SSO configuration, including every field exposed in the UI plus the service provider entity ID and ACS return URL. Signing private keys, signing certificates, and identity provider metadata are redacted on read. Requires the `saml:manage` scope and the SAML feature to be licensed.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Responses

200

Operation successful.

application/json

entityIDstringRead-onlyRequired

Service provider entity ID (metadata URL).

Example: `https://n8n.example.com/rest/sso/saml/metadata`

returnUrlstringRead-onlyRequired

Assertion Consumer Service (ACS) return URL.

Example: `https://n8n.example.com/rest/sso/saml/acs`

mappingobjectRequired

Mapping of SAML attributes to n8n user fields.

Show properties

metadatastringRequired

Identity provider metadata in XML format. Redacted on read when set because it contains IdP certificates; never echoed back in plaintext. Use an empty string when unset.

Example: `**hidden**`

metadataUrlstringRequired

URL to fetch identity provider metadata from. Use an empty string when unset.

ignoreSSLbooleanRequired

Whether to ignore SSL certificate errors when fetching metadata from a URL.

Example: `false`

loginBindingstring · enumRequired

SAML login request binding.

Example: `redirect`Possible values: `redirect``post`

loginEnabledbooleanRequired

Whether SAML login is enabled.

Example: `false`

loginLabelstringRequired

Label shown on the SAML login button.

Example: `SAML`

authnRequestsSignedbooleanRequired

Whether authentication requests are signed.

Example: `false`

wantAssertionsSignedbooleanRequired

Whether signed assertions are required.

Example: `true`

wantMessageSignedbooleanRequired

Whether signed SAML messages are required.

Example: `true`

emailVerifiedRequiredbooleanRequired

Whether the identity provider must assert that the user's email address is verified before a login is linked to an existing user by email. When disabled, only an explicit negative assertion is rejected.

Example: `false`

signingPrivateKeystringRequired

PEM-encoded private key for signing SAML AuthnRequests. Redacted on read when set; never echoed back in plaintext. Use an empty string when unset.

Example: `**hidden**`

signingCertificatestringRequired

PEM-encoded certificate containing the public key matching the signing private key. Redacted on read when set; never echoed back in plaintext. Use an empty string when unset.

Example: `**hidden**`

acsBindingstring · enumRequired

Assertion Consumer Service binding.

Example: `post`Possible values: `redirect``post`

signatureConfigobjectRequired

Configuration for the signature in SAML requests and responses.

Show properties

relayStatestringRequired

Default relay state value for SAML requests. Use an empty string when unset.

Example: `https://n8n.example.com`

401

Unauthorized

403

Forbidden

get/settings/sso/saml

HTTP

Copy

    GET /api/v1/settings/sso/saml HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "entityID": "https://n8n.example.com/rest/sso/saml/metadata",
      "returnUrl": "https://n8n.example.com/rest/sso/saml/acs",
      "mapping": {
        "email": "text",
        "firstName": "text",
        "lastName": "text",
        "userPrincipalName": "text",
        "emailVerified": "text",
        "n8nInstanceRole": "text",
        "n8nProjectRoles": [\
          "text"\
        ]
      },
      "metadata": "**hidden**",
      "metadataUrl": "text",
      "ignoreSSL": false,
      "loginBinding": "redirect",
      "loginEnabled": false,
      "loginLabel": "SAML",
      "authnRequestsSigned": false,
      "wantAssertionsSigned": true,
      "wantMessageSigned": true,
      "emailVerifiedRequired": false,
      "signingPrivateKey": "**hidden**",
      "signingCertificate": "**hidden**",
      "acsBinding": "post",
      "signatureConfig": {
        "prefix": "ds",
        "location": {
          "reference": "/samlp:Response/saml:Issuer",
          "action": "after"
        }
      },
      "relayState": "https://n8n.example.com"
    }

### Set the SAML SSO configuration[](https://docs.n8n.io/connect/n8n-api/settings-sso-saml#put-settings-sso-saml)

put

/api/v1Current n8n instance (self-hosted built-in playground)

/settings/sso/saml

Replace the SAML SSO configuration with the provided full object. Every writable field must be sent; use empty strings or empty arrays when a value is unset. Read-only `entityID` / `returnUrl` from GET are ignored if included, so a GET response can be sent back as a PUT body. Redacted secret placeholders keep the stored values unchanged. The update takes effect exactly as it would from the UI, using the same validation. Requires the `saml:manage` scope and the SAML feature to be licensed. When the configuration is managed via environment variables, the write is rejected with 409 and no changes are made.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Body

application/json

Full SAML SSO configuration. Every field must be provided; use empty strings or empty arrays when a value is unset. Partial updates are not supported.

mappingobjectRequired

Mapping of SAML attributes to n8n user fields. Use empty strings / empty arrays for unused attributes.

Show properties

metadatastringRequired

Identity provider metadata in XML format. Use an empty string to clear stored metadata (also clears metadataUrl when no URL is provided). Use the redaction placeholder from a prior GET to leave an existing value unchanged.

metadataUrlstringRequired

URL to fetch identity provider metadata from. Use an empty string to clear a stored URL.

ignoreSSLbooleanRequired

Whether to ignore SSL certificate errors when fetching metadata from a URL.

Example: `false`

loginBindingstring · enumRequired

SAML login request binding.

Example: `redirect`Possible values: `redirect``post`

loginEnabledbooleanRequired

Whether SAML login is enabled.

Example: `false`

loginLabelstringRequired

Label shown on the SAML login button.

Example: `SAML`

authnRequestsSignedbooleanRequired

Whether authentication requests are signed.

Example: `false`

wantAssertionsSignedbooleanRequired

Whether signed assertions are required.

Example: `true`

wantMessageSignedbooleanRequired

Whether signed SAML messages are required.

Example: `true`

emailVerifiedRequiredbooleanRequired

Whether the identity provider must assert that the user's email address is verified before a login is linked to an existing user by email. When disabled, only an explicit negative assertion is rejected.

Example: `false`

signingPrivateKeystringRequired

PEM-encoded private key for signing SAML AuthnRequests. Use an empty string to clear an existing key, or the redaction placeholder from a prior GET to leave it unchanged.

signingCertificatestringRequired

PEM-encoded certificate containing the public key matching the signing private key. Use an empty string when unused or to clear an existing certificate.

acsBindingstring · enumRequired

Assertion Consumer Service binding.

Example: `post`Possible values: `redirect``post`

signatureConfigobjectRequired

Configuration for the signature in SAML requests and responses.

Show properties

relayStatestringRequired

Default relay state value for SAML requests. Use an empty string when unused.

Example: `https://n8n.example.com`

entityIDstringOptional

Service provider entity ID. Returned by GET for convenience; ignored on write so a GET response can be sent back as a PUT body.

Example: `https://n8n.example.com/rest/sso/saml/metadata`

returnUrlstringOptional

Assertion Consumer Service return URL. Returned by GET for convenience; ignored on write so a GET response can be sent back as a PUT body.

Example: `https://n8n.example.com/rest/sso/saml/acs`

Responses

200

Operation successful.

application/json

entityIDstringRead-onlyRequired

Service provider entity ID (metadata URL).

Example: `https://n8n.example.com/rest/sso/saml/metadata`

returnUrlstringRead-onlyRequired

Assertion Consumer Service (ACS) return URL.

Example: `https://n8n.example.com/rest/sso/saml/acs`

mappingobjectRequired

Mapping of SAML attributes to n8n user fields.

Show properties

metadatastringRequired

Identity provider metadata in XML format. Redacted on read when set because it contains IdP certificates; never echoed back in plaintext. Use an empty string when unset.

Example: `**hidden**`

metadataUrlstringRequired

URL to fetch identity provider metadata from. Use an empty string when unset.

ignoreSSLbooleanRequired

Whether to ignore SSL certificate errors when fetching metadata from a URL.

Example: `false`

loginBindingstring · enumRequired

SAML login request binding.

Example: `redirect`Possible values: `redirect``post`

loginEnabledbooleanRequired

Whether SAML login is enabled.

Example: `false`

loginLabelstringRequired

Label shown on the SAML login button.

Example: `SAML`

authnRequestsSignedbooleanRequired

Whether authentication requests are signed.

Example: `false`

wantAssertionsSignedbooleanRequired

Whether signed assertions are required.

Example: `true`

wantMessageSignedbooleanRequired

Whether signed SAML messages are required.

Example: `true`

emailVerifiedRequiredbooleanRequired

Whether the identity provider must assert that the user's email address is verified before a login is linked to an existing user by email. When disabled, only an explicit negative assertion is rejected.

Example: `false`

signingPrivateKeystringRequired

PEM-encoded private key for signing SAML AuthnRequests. Redacted on read when set; never echoed back in plaintext. Use an empty string when unset.

Example: `**hidden**`

signingCertificatestringRequired

PEM-encoded certificate containing the public key matching the signing private key. Redacted on read when set; never echoed back in plaintext. Use an empty string when unset.

Example: `**hidden**`

acsBindingstring · enumRequired

Assertion Consumer Service binding.

Example: `post`Possible values: `redirect``post`

signatureConfigobjectRequired

Configuration for the signature in SAML requests and responses.

Show properties

relayStatestringRequired

Default relay state value for SAML requests. Use an empty string when unset.

Example: `https://n8n.example.com`

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

put/settings/sso/saml

HTTP

Copy

    PUT /api/v1/settings/sso/saml HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 738
    
    {
      "mapping": {
        "email": "text",
        "firstName": "text",
        "lastName": "text",
        "userPrincipalName": "text",
        "emailVerified": "text",
        "n8nInstanceRole": "text",
        "n8nProjectRoles": [\
          "text"\
        ]
      },
      "metadata": "text",
      "metadataUrl": "text",
      "ignoreSSL": false,
      "loginBinding": "redirect",
      "loginEnabled": false,
      "loginLabel": "SAML",
      "authnRequestsSigned": false,
      "wantAssertionsSigned": true,
      "wantMessageSigned": true,
      "emailVerifiedRequired": false,
      "signingPrivateKey": "text",
      "signingCertificate": "text",
      "acsBinding": "post",
      "signatureConfig": {
        "prefix": "ds",
        "location": {
          "reference": "/samlp:Response/saml:Issuer",
          "action": "after"
        }
      },
      "relayState": "https://n8n.example.com",
      "entityID": "https://n8n.example.com/rest/sso/saml/metadata",
      "returnUrl": "https://n8n.example.com/rest/sso/saml/acs"
    }

Test it

200

Operation successful.

Copy

    {
      "entityID": "https://n8n.example.com/rest/sso/saml/metadata",
      "returnUrl": "https://n8n.example.com/rest/sso/saml/acs",
      "mapping": {
        "email": "text",
        "firstName": "text",
        "lastName": "text",
        "userPrincipalName": "text",
        "emailVerified": "text",
        "n8nInstanceRole": "text",
        "n8nProjectRoles": [\
          "text"\
        ]
      },
      "metadata": "**hidden**",
      "metadataUrl": "text",
      "ignoreSSL": false,
      "loginBinding": "redirect",
      "loginEnabled": false,
      "loginLabel": "SAML",
      "authnRequestsSigned": false,
      "wantAssertionsSigned": true,
      "wantMessageSigned": true,
      "emailVerifiedRequired": false,
      "signingPrivateKey": "**hidden**",
      "signingCertificate": "**hidden**",
      "acsBinding": "post",
      "signatureConfig": {
        "prefix": "ds",
        "location": {
          "reference": "/samlp:Response/saml:Issuer",
          "action": "after"
        }
      },
      "relayState": "https://n8n.example.com"
    }

[PreviousSettings Sso Oidc](https://docs.n8n.io/connect/n8n-api/settings-sso-oidc)
[NextSource Control](https://docs.n8n.io/connect/n8n-api/source-control)

Last updated 9 days ago

Was this helpful?