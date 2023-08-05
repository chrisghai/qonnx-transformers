from transformers import Pipeline
from fastapi import APIRouter, Depends

from lib.utils import parse_ner
from lib.models import TextInput
from lib.services import get_classifier

router = APIRouter(
    prefix="/ner", 
    tags=["Named Entity Recognition"],
)

@router.post("/identify")
def identify(
    input: TextInput,
    classifier: Pipeline = Depends(get_classifier),
):
    text = input.text
    results = classifier(text)
    if results:
        results = parse_ner(results)

    return results
