
from typing import List, Dict, TypedDict

class MedicalImage(TypedDict):
    id: str
    data: List[str]
    deviceName: str

DevicesDict = Dict[str, MedicalImage]