import cmath;
import math;

a = float(input("define value for 'a'"));
b = float(input("define value for 'b'"));
c = float(input("define value for 'c'"));

def solve_quadratic(a, b, c):

    discriminant = b**2 - 4*a*c

    root_1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    root_2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    print("root 1", root_1, "root 2", root_2)

solve_quadratic(a, b, c)



