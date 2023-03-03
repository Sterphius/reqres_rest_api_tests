from voluptuous import Schema, PREVENT_EXTRA

login_schema = Schema(
    {
        "token": str
    },
    required=True,
    extra=PREVENT_EXTRA
)

error_schema = Schema(
    {
        "error": str
    },
    required=True,
    extra=PREVENT_EXTRA
)