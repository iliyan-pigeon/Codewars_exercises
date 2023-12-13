def balanced_parens(n):
    def generate_parentheses(s='', left=0, right=0):
        if len(s) == 2 * n:
            result.append(s)
            return
        if left < n:
            generate_parentheses(s + '(', left + 1, right)
        if right < left:
            generate_parentheses(s + ')', left, right + 1)

    result = []
    generate_parentheses()
    return result

# Test cases
print(balanced_parens(0))  # Output: [""]
print(balanced_parens(1))  # Output: ["()"]
print(balanced_parens(2))  # Output: ["()()", "(())"]
print(balanced_parens(3))  # Output: ["()()()", "(())()", "()(())", "(()())", "((()))"]