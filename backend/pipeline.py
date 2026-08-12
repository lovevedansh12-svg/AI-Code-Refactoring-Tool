import sys

sys.path.append("../analyzer")
sys.path.append("../ai-engine")

from analyzer import analyze_cpp
from refactor import RefactoringEngine
from model import OpenAIModel


class RefactoringPipeline:

    def __init__(self):
        self.model = OpenAIModel()
        self.engine = RefactoringEngine(self.model)

    def run(self, source_code):

        # Step 1: Analyze the original code
        analysis_report = analyze_cpp(source_code)

        # Step 2: Ask the AI to refactor it
        ai_result = self.engine.refactor(
            source_code,
            analysis_report
        )

        return {
            "analysis": analysis_report,
            "refactoring": ai_result
        }
