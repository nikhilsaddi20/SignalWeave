import uuid

def store_event(event) -> str:
    """
    OpenSearch stub.
    In real SOC systems this writes to SIEM storage.
    """
    event_id = f"auth-{uuid.uuid4()}"

    # Convert Pydantic model safely
    data = event.model_dump()

    print("[SignalWeave] Stored event:")
    print(data)

    return event_id