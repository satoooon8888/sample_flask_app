from dataclasses import dataclass
from typing import Optional

# データクラスの定義 (プロパティだけ持つクラス)
@dataclass
class Todo:
	content: str
	id: Optional[int] = None

