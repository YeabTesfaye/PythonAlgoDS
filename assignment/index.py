

def multiply_polynomials(poly1, poly2):
    # Initialize the result list with the appropriate size
    result = [0] * (len(poly1) + len(poly2) - 1)
    print(len(result))
    # Multiply the coefficients
    for i in range(len(poly1)):
        for j in range(len(poly2)):
            result[i + j] += poly1[i] * poly2[j]

    return result


# import numpy as np 


def add(poly1, poly2):
    """Add two polynomials"""
    result = [0] * max(len(poly1), len(poly2))
    for i in range(len(result)):
        if i < len(poly1):
            result[i] += poly1[i]
        if i < len(poly2):
            result[i] += poly2[i]
    return result

def split(poly1, poly2):
    """Split each polynomial into two smaller polynomials"""
    mid = max(len(poly1), len(poly2)) // 2
    return  (poly1[:mid], poly1[mid:]), (poly2[:mid], poly2[mid:])

def increase_exponent(poly, n):
    """Multiply poly1 by x^n"""
    return [0] * n + poly

#numpy 
def multiply_optimized(poly1, poly2):
    # Base cases (Edge)
    if (not poly1 or poly1 == [0]) or (not poly2 or poly2 == [0]):
      return [0]

    # Base cases (Normal)
    poly3 = []
    if len(poly1) == 1:
      for i in poly2:
        poly3.append(i * poly1[0])
      return poly3

    if len(poly2) == 1:
      for i in poly1:
        poly3.append(i * poly2[0])
      return poly3

    # 'Step' cases (Where the recursion actually happens)
    splitPoly = split(poly1, poly2)
    poly10, poly11 = splitPoly[0][0], splitPoly[0][1]
    poly20, poly21 = splitPoly[1][0], splitPoly[1][1]

    y = multiply_optimized(add(poly10, poly11), add(poly20, poly21))
    u = multiply_optimized(poly10, poly20)
    z = multiply_optimized(poly11, poly21)

    u2 = []  # This equals -u
    for i in u:
      u2.append(-i)

    z2 = []  # This equals -z
    for i in z:
      z2.append(-i)

    sum = add(add(y, u2), z2)  # This equals y - u - z
    w = increase_exponent(sum, len(poly1) // 2)  # This equals [y - u - z] * x^(n//2)
    v = increase_exponent(z, 2 * (len(poly1) // 2))  # This equals z * x ^ (2*(n//2))

    result = add(add(u, w), v)
    return result


poly2 = [2, 0, 5, 7] 
poly1  = [3, 4, 2]
poly2 = [2, 1, 4]
poly1 = [3, 0, 2]
print(multiply_polynomials(poly1, poly2))
print(multiply_optimized(poly1, poly2))