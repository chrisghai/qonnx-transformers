import os

from transformers import (
    Pipeline,
    pipeline,
    AutoTokenizer,
)
from optimum.onnxruntime import (
    ORTModelForSeq2SeqLM,
    ORTModelForTokenClassification,
    ORTModelForSequenceClassification,
)

from lib.config import APP_ROOT

TASK2NAME = {
    "translation": os.environ.get("TRANSLATION_MODEL"),
    "zero-shot-classification": os.environ.get("ZERO_SHOT_MODEL"),
    "ner": os.environ.get("NER_MODEL"),
}

TASK2MODEL = {
    "translation": ORTModelForSeq2SeqLM,
    "zero-shot-classification": ORTModelForSequenceClassification,
    "ner": ORTModelForTokenClassification,
}


def load_singleton_classifier(
        task: str = "translation",
        model_dir: str = "models",
    ) -> Pipeline:
    model_postfix = "onnx-quantized"
    model_name = TASK2NAME.get(task)
    model_class = TASK2MODEL.get(task)
    model_id = APP_ROOT / model_dir / f"{model_name}-{model_postfix}"

    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = model_class.from_pretrained(model_id)
    
    pipeline_kwargs = {}
    if task == "ner":
        pipeline_kwargs["aggregation_strategy"] = "simple"

    return pipeline(
        task, 
        model=model, 
        tokenizer=tokenizer, 
        **pipeline_kwargs,
    )
