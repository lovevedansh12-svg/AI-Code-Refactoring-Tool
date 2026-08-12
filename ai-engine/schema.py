from dataclasses import dataclass
from typing import List


@dataclass
class RefactoringResult:
    refactored_code: str
    changes: List[str]
    explanation: str
