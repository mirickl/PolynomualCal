import PolynomualCalculation as pom

if __name__ == "__main__":
    poly1 = pom.Polynomial({8 : 1,2 : 1,3 : 5,0: 8})
    poly2 = pom.Polynomial({5 : 1,3 : 1,4 : 5,0: 8})
    constant_1 = 4
    constant_2 = -3

    result_add1 = poly1 + poly2
    result_add2 = constant_1 + poly2
    result_add3 = constant_1 + constant_1
    result_sub1 =  poly1 - poly2
    result_sub2 = poly1 - constant_1
    result_sub3 = constant_1 - poly1
    result_sub4 = constant_1 - constant_2
    result_mul1 = poly1 * poly2
    result_mul2 =  poly2 * 0
    result_pow = poly1 ** 3

    print("多项式加法:",result_add1)
    print("常数与多项式加法:", result_add2)
    print("常数加法:", result_add3)
    print("多项式减法:", result_sub1)
    print("多项式减常数:", result_sub2)
    print("常数减多项式:", result_sub3)
    print("常数减法:", result_sub4)
    print("多项式与多项式相乘:", result_mul1)
    print("多项式与常数相乘:", result_mul2)
    print("多项式的幂:", result_pow)
