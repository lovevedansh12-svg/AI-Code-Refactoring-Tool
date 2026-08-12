# C++ Code Analyzer

The Code Analyzer is responsible for detecting code smells and structural problems in C++ source code.

## Current Detectors

1. Long functions
2. Deep nesting
3. Too many parameters

## Input

C++ source code.

## Output

A structured analysis report containing:

- Programming language
- Total number of detected issues
- Issue type
- Severity
- Source line
- Additional information

## Technology

- Python
- Tree-sitter
- Tree-sitter C++
