"""
Lab: Code Refactoring Exercise
Course: Software Engineering (24PCA402)

Task: The function below "works" but has several code smells
(long parameter list, deep nesting, duplicated logic, unclear
naming). Refactor it while preserving its observable behavior.
Both versions are included so you can diff them.
"""


# ---- BEFORE: smelly version -------------------------------------------
def calc(o, t, d, c, x):
    if o == 1:
        if t == "vip":
            if d > 0:
                p = c - (c * d / 100)
            else:
                p = c
            if x:
                p = p - 5
        else:
            if d > 0:
                p = c - (c * d / 100)
            else:
                p = c
    else:
        p = c
    return p


# ---- AFTER: refactored version -----------------------------------------
VIP_FLAT_DISCOUNT = 5


def calculate_price(is_order_active, customer_type, discount_percent,
                     base_cost, has_extra_coupon):
    """Compute the final price for an order.

    Preserves the behavior of the original `calc` function:
    - Inactive orders are charged the base cost with no discount.
    - Active orders get a percentage discount if one applies.
    - VIP customers additionally get a flat coupon discount.
    """
    if not is_order_active:
        return base_cost

    price = apply_percentage_discount(base_cost, discount_percent)

    if customer_type == "vip" and has_extra_coupon:
        price -= VIP_FLAT_DISCOUNT

    return price


def apply_percentage_discount(cost, discount_percent):
    if discount_percent <= 0:
        return cost
    return cost - (cost * discount_percent / 100)


if __name__ == "__main__":
    args = (1, "vip", 10, 200, True)
    assert calc(*args) == calculate_price(*args), "Behavior mismatch!"
    print("Refactor verified. Result:", calculate_price(*args))
