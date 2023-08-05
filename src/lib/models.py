from pydantic import BaseModel


class TextInput(BaseModel):
    text: str


class TranslationInput(BaseModel):
    text: str
    src: str = "no"
    tgt: str = "en"


class ZeroShotInput(BaseModel):
    text: str
    classes: list[str]
