"""
Lab: White-Box Testing - Cyclomatic Complexity
Course: Software Engineering (24PCA402)

Task: Apply McCabe's Cyclomatic Complexity, V(G) = E - N + 2,
to derive an independent path set and design test cases that
exercise every path.
"""


def classify_grade(score):
    """Sample function under test. Manually trace its control-flow
    graph: nodes (N) = decision points + 1, edges (E) connect them.
    """
    if score < 0 or score > 100:
        return "invalid"
    elif score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "F"


def cyclomatic_complexity(decision_points):
    """V(G) = number of decision points + 1 (for a single-entry,
    single-exit structured function)."""
    return decision_points + 1


if __name__ == "__main__":
    # classify_grade has 4 decision points (if/elif chain) -> V(G) = 5
    decisions = 4
    print("Cyclomatic complexity V(G):", cyclomatic_complexity(decisions))

    # Independent paths to cover (basis path set):
    test_cases = [-5, 150, 95, 80, 65, 40]
    for score in test_cases:
        print(f"score={score:>4} -> {classify_grade(score)}")
