from dataclasses import dataclass
from typing import Optional

@dataclass
class Todo:
	content: str
	id: Optional[int] = None

