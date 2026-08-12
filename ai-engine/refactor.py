import json


class RefactoringEngine:

    def __init__(self, model):
        self.model = model

    def build_prompt(self, source_code, analysis_report):
        return f"""
You are an expert C++ code refactoring assistant.

Refactor the provided C++ code based on the static analysis report.

Rules:
1. Preserve the original behavior.
2. Preserve the intended output.
3. Fix the detected issues.
4. Improve readability and maintainability.
5. Do not make unrelated changes.
6. Return valid C++ code.

Static Analysis Report:
{json.dumps(analysis_report, indent=2)}

Original C++ Code:
{source_code}

Return your response as JSON with exactly these fields:

{{
    "refactored_code": "complete refactored C++ code",
    "changes": [
        "description of change 1",
        "description of change 2"
    ],
    "explanation": "overall explanation of the refactoring"
}}
"""

    def refactor(self, source_code, analysis_report):
        prompt = self.build_prompt(
            source_code,
            analysis_report
        )

        response = self.model.generate(prompt)

        return response
