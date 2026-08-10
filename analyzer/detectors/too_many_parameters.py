def find_too_many_parameters(tree, source_code, threshold=5):
    issues = []

    def walk(node):
        if node.type == "function_definition":
            declarator = node.child_by_field_name("declarator")

            if declarator:
                parameters = declarator.child_by_field_name("parameters")

                if parameters:
                    parameter_count = sum(
                        1
                        for child in parameters.named_children
                        if child.type == "parameter_declaration"
                    )

                    if parameter_count > threshold:
                        issues.append({
                            "type": "too_many_parameters",
                            "severity": "medium",
                            "line": node.start_point[0] + 1,
                            "parameters": parameter_count,
                            "message": (
                                f"Function has {parameter_count} parameters, "
                                f"which exceeds the threshold of {threshold}."
                            )
                        })

        for child in node.children:
            walk(child)

    walk(tree.root_node)

    return issues
