from backend.ingest.schema import AuthEvent

def parse_auth_log(log: dict) -> AuthEvent:
    return AuthEvent(**log)