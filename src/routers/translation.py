from transformers import Pipeline
from fastapi import APIRouter, Depends

from lib.models import TranslationInput
from lib.services import get_classifier

router = APIRouter(
    prefix="/translation", 
    tags=["translation"],
)

@router.post("/translate")
def translate(
    input: TranslationInput,
    classifier: Pipeline = Depends(get_classifier),
):
    text, src, tgt = input.text, input.src, input.tgt
    return classifier(text, src_lang=src, tgt_lang=tgt)[0]
