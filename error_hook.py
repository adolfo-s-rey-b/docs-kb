#!/usr/bin/env python3
"""
docs-kb error hook: Detects technology-specific errors in Bash tool output
and suggests documentation consultation.

This is a PostToolUse hook for the Bash matcher. It reads the tool result
from stdin (JSON), identifies error patterns, and prints a short suggestion
to stdout if a known technology error is detected.

Always exits 0 (informational, never blocks execution).
"""

import json
import re
import sys


# Technology error patterns: {tech_key: [regex_patterns]}
TECH_PATTERNS = {
    "python": [
        r"Traceback \(most recent call last\)",
        r"ModuleNotFoundError:",
        r"ImportError:",
        r"AttributeError:",
        r"NameError:",
        r"ValueError:",
        r"TypeError:",
    ],
    "pandas": [
        r"pandas[\.\w]*Error",
        r"KeyError:.*(?:DataFrame|Series|column)",
        r"(?:merge|concat|groupby).*(?:Error|Warning)",
        r"SettingWithCopyWarning",
    ],
    "numpy": [
        r"numpy[\.\w]*Error",
        r"AxisError:",
        r"LinAlgError:",
        r"UFuncTypeError:",
    ],
    "r": [
        r"Error in\s+\w+",
        r"could not find function",
        r"object .+ not found",
        r"there is no package called",
    ],
    "dplyr": [
        r"dplyr.*error",
        r"Column .+ doesn't exist",
        r"must not be duplicated",
    ],
    "ggplot2": [
        r"ggplot.*error",
        r"geom_\w+.*requires.*aesthetic",
        r"Aesthetics must be",
    ],
    "react": [
        r"React[\.\w]*Error",
        r"Invalid hook call",
        r"Cannot read propert(?:y|ies)",
        r"Uncaught.*React",
    ],
    "javascript": [
        r"ReferenceError:",
        r"SyntaxError:",
        r"Uncaught TypeError:",
        r"npm ERR!",
        r"node:internal",
    ],
    "tensorflow": [
        r"tensorflow\.\w+",
        r"tf\..*Error",
        r"ResourceExhaustedError",
        r"InvalidArgumentError.*shape",
    ],
    "pytorch": [
        r"torch\.\w+.*Error",
        r"RuntimeError:.*CUDA",
        r"RuntimeError:.*expected.*tensor",
        r"Expected.*but got",
    ],
    "scikit-learn": [
        r"sklearn\.\w+",
        r"NotFittedError:",
        r"ConvergenceWarning",
    ],
    "keras": [
        r"keras\.\w+.*Error",
        r"ValueError:.*(?:input|layer|shape)",
    ],
    "matplotlib": [
        r"matplotlib\.\w+.*Error",
        r"AttributeError.*(?:Axes|Figure)",
    ],
    "seaborn": [
        r"seaborn\.\w+.*Error",
        r"ValueError:.*(?:hue|palette|data)",
    ],
    "n8n": [
        r"n8n.*error",
        r"workflow.*fail",
        r"NodeApiError",
        r"NodeOperationError",
    ],
    "css": [
        r"CSSStyleDeclaration",
        r"Unknown property",
        r"Expected.*selector",
    ],
    "html": [
        r"HTMLElement.*Error",
        r"Uncaught.*DOM",
        r"querySelector.*null",
    ],
}

# Error keyword extraction patterns
ERROR_KEYWORD_PATTERNS = [
    r"(\w+Error):",
    r"(\w+Warning):",
    r"Error in (\w+)",
    r"could not find function '(\w+)'",
    r"No module named '(\w+)'",
    r"Cannot find module '(\w+)'",
    r"there is no package called '(\w+)'",
]


def extract_error_keyword(text: str) -> str:
    """Extract the most specific error keyword from error text."""
    for pattern in ERROR_KEYWORD_PATTERNS:
        match = re.search(pattern, text)
        if match:
            return match.group(1)
    return "error"


def detect_tech_error(output: str) -> tuple[str, str] | None:
    """Detect technology and error keyword from output text.

    Returns (tech_key, error_keyword) or None.
    """
    if not output:
        return None

    # Check each technology's patterns
    # More specific patterns first (pandas before python, etc.)
    priority_order = [
        "pandas", "numpy", "scikit-learn", "keras", "tensorflow", "pytorch",
        "matplotlib", "seaborn",
        "dplyr", "ggplot2",
        "react", "n8n",
        "r", "python", "javascript", "css", "html",
    ]

    for tech in priority_order:
        patterns = TECH_PATTERNS.get(tech, [])
        for pattern in patterns:
            if re.search(pattern, output, re.IGNORECASE):
                keyword = extract_error_keyword(output)
                return (tech, keyword)

    return None


def main():
    try:
        raw_input = sys.stdin.read()
        if not raw_input.strip():
            sys.exit(0)

        data = json.loads(raw_input)
    except (json.JSONDecodeError, Exception):
        sys.exit(0)

    # Extract tool result text
    tool_result = data.get("tool_result", {})

    # Handle both string and dict tool_result formats
    if isinstance(tool_result, str):
        output_text = tool_result
    else:
        stdout = tool_result.get("stdout", "")
        stderr = tool_result.get("stderr", "")
        output_text = f"{stdout}\n{stderr}"

    # Also check the raw content if available
    if not output_text.strip():
        content = tool_result.get("content", "")
        if isinstance(content, str):
            output_text = content

    # Detect error
    result = detect_tech_error(output_text)
    if result:
        tech, keyword = result
        print(
            f"NOTA: Error detectado en {tech}. "
            f"Busqueda rapida: /docs-search {tech} {keyword} | "
            f"Analisis detallado: /docs-debug-agent"
        )

    sys.exit(0)


if __name__ == "__main__":
    main()
