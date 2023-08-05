from fastapi import Depends
from transformers import Pipeline

from app import CLASSIFIER


async def _get_classifier() -> Pipeline:
    return CLASSIFIER


async def get_classifier(
        service: Pipeline = Depends(_get_classifier)
    ) -> Pipeline:
    return service
