from refactor import RefactoringEngine
from model import OpenAIModel


code = """
void calculate(int a, int b, int c, int d, int e, int f)
{
    if (a > 0)
    {
        if (b > 0)
        {
            if (c > 0)
            {
                cout << a + b + c;
            }
        }
    }
}
"""


analysis_report = {
    "language": "cpp",
    "total_issues": 2,
    "issues": [
        {
            "type": "deep_nesting",
            "severity": "high"
        },
        {
            "type": "too_many_parameters",
            "severity": "medium"
        }
    ]
}


model = OpenAIModel()

engine = RefactoringEngine(model)

result = engine.refactor(
    code,
    analysis_report
)

print(result)
