
from typing import List, TypedDict

class MedicalImage(TypedDict):
    id: str
    data: List[str]
    deviceName: str