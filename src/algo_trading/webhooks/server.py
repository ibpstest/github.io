from fastapi import FastAPI

app = FastAPI(title="Algo Trading Webhook")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/signal")
def signal(payload: dict) -> dict:
    # TODO: validate signature and convert payload into internal signal.
    return {"received": True, "payload": payload}
