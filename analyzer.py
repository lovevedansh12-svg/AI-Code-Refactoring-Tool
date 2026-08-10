from parser import parse_cpp_code
from detectors.long_function import find_long_functions
from detectors.deep_nesting import find_deep_nesting


def analyze_cpp(source_code):
    tree = parse_cpp_code(source_code)

    issues = []

    issues.extend(
        find_long_functions(tree, source_code)
    )

    issues.extend(
        find_deep_nesting(tree, source_code)
    )

    return {
        "language": "cpp",
        "issues": issues
    }

if __name__ == "__main__":
    code = """
    void test() {
        int a = 1;
        int b = 2;
        int c = 3;
        int d = 4;
        int e = 5;
        int f = 6;
        int g = 7;
        int h = 8;
        int i = 9;
        int j = 10;
        int k = 11;
        int l = 12;
        int m = 13;
        int n = 14;
        int o = 15;
        int p = 16;
        int q = 17;
        int r = 18;
        int s = 19;
        int t = 20;
        int u = 21;
        int v = 22;
        int w = 23;
        int x = 24;
        int y = 25;
        int z = 26;
        int aa = 27;
        int ab = 28;
        int ac = 29;
        int ad = 30;
        int ae = 31;
    }
    """

    result = analyze_cpp(code)

    print(result)
