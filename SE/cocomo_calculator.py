"""
Lab: Software Size Estimation - Basic COCOMO
Course: Software Engineering (24PCA402)

Task: Estimate effort (person-months), development time (months),
and team size for a sample project using the Basic COCOMO model.

Effort  = a * (KLOC ^ b)
Time    = c * (Effort ^ d)
Staff   = Effort / Time
"""

PROJECT_MODES = {
    # mode: (a, b, c, d)
    "organic": (2.4, 1.05, 2.5, 0.38),
    "semi-detached": (3.0, 1.12, 2.5, 0.35),
    "embedded": (3.6, 1.20, 2.5, 0.32),
}


def estimate(kloc, mode="organic"):
    a, b, c, d = PROJECT_MODES[mode]
    effort = a * (kloc ** b)          # person-months
    time = c * (effort ** d)          # months
    staff = effort / time             # average headcount
    return {
        "mode": mode,
        "kloc": kloc,
        "effort_pm": round(effort, 2),
        "time_months": round(time, 2),
        "avg_staff": round(staff, 2),
    }


if __name__ == "__main__":
    for mode in PROJECT_MODES:
        result = estimate(kloc=25, mode=mode)
        print(
            f"{result['mode']:<14} | "
            f"Effort: {result['effort_pm']:>7} PM | "
            f"Time: {result['time_months']:>6} mo | "
            f"Staff: {result['avg_staff']:>5}"
        )
