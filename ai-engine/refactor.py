class RefactoringEngine:

    def __init__(self, model):
        self.model = model

    def build_prompt(self, source_code, analysis_report):
        prompt = f"""
You are an expert C++ code refactoring assistant.

Your task is to refactor the provided C++ code.

IMPORTANT RULES:
1. Preserve the original behavior.
2. Do not change the program's intended output.
3. Fix the issues identified by static analysis.
4. Improve readability and maintainability.
5. Do not make unnecessary changes.
6. Return valid C++ code.

STATIC ANALYSIS REPORT:
{analysis_report}

ORIGINAL C++ CODE:
{source_code}

Return:
1. Refactored C++ code
2. List of changes made
3. Explanation of why each change was made
"""

        return prompt

    def refactor(self, source_code, analysis_report):
        prompt = self.build_prompt(
            source_code,
            analysis_report
        )

        response = self.model.generate(prompt)

        return response
