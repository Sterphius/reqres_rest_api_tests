from voluptuous import Schema, PREVENT_EXTRA, Optional

user_schema = Schema(
    {
        "job": str,
        "name": str,
        Optional("id"):str,
        Optional("createdAt"): str,
        Optional("updatedAt"): str,
    },
    extra=PREVENT_EXTRA,
    required=True
)

support_schema = Schema(
    {
        "url": str,
        "text": str,
    },
    extra=PREVENT_EXTRA,
    required=True
)
