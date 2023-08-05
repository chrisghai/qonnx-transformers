from transformers import Pipeline
from fastapi import APIRouter, Depends

from lib.models import ZeroShotInput
from lib.services import get_classifier

router = APIRouter(
    prefix="/zero-shot", 
    tags=["Zero Shot Classification"],
)

@router.post("/classify")
def classify(
    input: ZeroShotInput,
    classifier: Pipeline = Depends(get_classifier),
):
    text, classes = input.text, input.classes
    return classifier(text, candidate_labels=classes)
