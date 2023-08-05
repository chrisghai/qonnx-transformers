from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html

from lib.config import APP_TASK
from lib.classifiers import load_singleton_classifier

CLASSIFIER = load_singleton_classifier(APP_TASK)
app = FastAPI()

from routers import translation, zero_shot, ner

match APP_TASK:
    case "translation":
        app.include_router(translation.router)
    case "zero-shot-classification":
        app.include_router(zero_shot.router)
    case "ner":
        app.include_router(ner.router)
    case other:
        app.include_router(translation.router)


@app.get("/docs", include_in_schema=False)
def swagger_ui():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title="qONNX Transformers - Swagger UI",
    )

@app.get("/health")
async def health():
    return "OK\n"
