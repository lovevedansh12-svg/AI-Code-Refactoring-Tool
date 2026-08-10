from tree_sitter import Language, Parser
import tree_sitter_cpp as tscpp

CPP_LANGUAGE = Language(tscpp.language())

parser = Parser(CPP_LANGUAGE)


def parse_cpp_code(source_code):
    """
    Parse C++ source code and return its syntax tree.
    """
    source_bytes = source_code.encode("utf-8")
    tree = parser.parse(source_bytes)
    return tree
