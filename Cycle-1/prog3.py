import math
def find_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        return None

    elif discriminant == 0:
        root = -b / (2 * a)
        return round(root, 2), round(root, 2)

    else:
        sqrt_discriminant = math.sqrt(discriminant)
        root1 = (-b + sqrt_discriminant) / (2 * a)
        root2 = (-b - sqrt_discriminant) / (2 * a)
        return round(root1, 2), round(root2, 2)


# Get user input for coefficients
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

roots = find_roots(a, b, c)
if roots:
    root1, root2 = roots
    print(f"The roots of the quadratic equation {a}x^2 + {b}x + {c} = 0 are: {root1} and {root2}")
else:
    print("The quadratic equation has no real roots.")
