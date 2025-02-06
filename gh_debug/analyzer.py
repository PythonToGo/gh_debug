import re

ERROR_PATTERNS = {
    "Permission Denied": r"permission denied",
    "Timeout Error": r"timeout.*/d+S",
    "Authentication Error": r"401 Unauthorized",
    "Syntax Error": r"SyntaxError|unexpected token",
}

def analyze_logs(log_text):
    for error_name, pattern in ERROR_PATTERNS.items():
        if re.search(pattern, log_text, re.IGNORECASE):
            return error_name
    return "No errors found"
