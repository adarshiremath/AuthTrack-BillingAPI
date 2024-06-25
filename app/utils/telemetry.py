from prometheus_fastapi_instrumentator import Instrumentator

def setup_telemetry(app):
    Instrumentator().instrument(app).expose(app)
