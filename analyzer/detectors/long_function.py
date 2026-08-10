def find_long_functions(tree, source_code, threshold=30):
    issues = []

    def walk(node):
        if node.type == "function_definition":
            start_line = node.start_point[0] + 1
            end_line = node.end_point[0] + 1

            lines = end_line - start_line + 1

            if lines > threshold:
                function_name = "unknown"

                declarator = node.child_by_field_name("declarator")

                if declarator:
                    name_node = declarator.child_by_field_name("declarator")

                    if name_node:
                        function_name = source_code[
                            name_node.start_byte:name_node.end_byte
                        ]

                issues.append({
                    "type": "long_function",
                    "function": function_name,
                    "severity": "medium",
                    "line": start_line,
                    "message": f"Function contains {lines} lines."
                })

        for child in node.children:
            walk(child)

    walk(tree.root_node)

    return issues
