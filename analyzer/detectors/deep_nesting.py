NESTING_NODES = {
    "if_statement",
    "for_statement",
    "while_statement",
    "do_statement",
    "switch_statement"
}


def find_deep_nesting(tree, source_code, threshold=4):
    issues = []

    def walk(node, depth=0):
        current_depth = depth

        if node.type in NESTING_NODES:
            current_depth += 1

            if current_depth > threshold:
                line = node.start_point[0] + 1

                issues.append({
                    "type": "deep_nesting",
                    "severity": "high",
                    "line": line,
                    "depth": current_depth,
                    "message": (
                        f"Nesting depth reaches {current_depth}, "
                        f"which exceeds the threshold of {threshold}."
                    )
                })

        for child in node.children:
            walk(child, current_depth)

    walk(tree.root_node)

    return issues
