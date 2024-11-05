class Polynomial:
    def __init__(self, coefficients):
        """初始化多项式，coefficients 是一个字典，键为指数，值为系数"""
        self.coefficients = coefficients

    def __add__(self, other):
        """重载加法运算符"""
        new_coefficients = self.coefficients.copy()

        for power, coeff in other.coefficients.items():
            new_coefficients[power] = new_coefficients.get(power, 0) + coeff

        return Polynomial(new_coefficients).simplify()

    # def __sub__(self, other):
    #     """重载减法运算符"""
    #     new_coefficients = self.coefficients.copy()
    #
    #     for power, coeff in other.coefficients.items():
    #         new_coefficients[power] = new_coefficients.get(power, 0) - coeff
    #
    #     return Polynomial(new_coefficients).simplify()
    #
    # def __mul__(self, other):
    #     """重载乘法运算符"""
    #     if isinstance(other, Polynomial):
    #         new_coefficients = defaultdict(int)
    #         for power1, coeff1 in self.coefficients.items():
    #             for power2, coeff2 in other.coefficients.items():
    #                 new_coefficients[power1 + power2] += coeff1 * coeff2
    #         return Polynomial(new_coefficients).simplify()
    #     elif isinstance(other, (int, float)):
    #         new_coefficients = {power: coeff * other for power, coeff in self.coefficients.items()}
    #         return Polynomial(new_coefficients).simplify()
    #     else:
    #         return NotImplemented

    def simplify(self):
        """化简多项式，移除系数为零的项"""
        self.coefficients = {k: v for k, v in self.coefficients.items() if v != 0}
        return self

    def __str__(self):
        """输出多项式的字符串表示"""
        if not self.coefficients:
            return "0"

        terms = []
        for power in sorted(self.coefficients.keys(), reverse=True):
            coeff = self.coefficients[power]
            if power == 0:
                terms.append(f"{coeff}")
            elif power == 1:
                terms.append(f"{coeff}x" if coeff != 1 else "x")
            else:
                terms.append(f"{coeff}x^{power}" if coeff != 1 else f"x^{power}")

        return " + ".join(terms).replace("+ -", "- ")


# 示例使用
# 创建多项式: 2x^2 + 3x + 4
poly1 = Polynomial({2: 2, 1: 3, 0: 4})

# 创建多项式: 5x^2 - x + 1
poly2 = Polynomial({2: 5, 1: -1, 0: 1})

# 相加
result_add = poly1 + poly2

# # 相减
# result_sub = poly1 - poly2
#
# # 乘以常数
# result_mul_const = poly1 * 3

# 乘以另一个多项式
#result_mul_poly = poly1 * poly2

print("多项式 1:", poly1)
print("多项式 2:", poly2)
print("相加结果:", result_add)
# print("相减结果:", result_sub)
# print("乘以常数 3 的结果:", result_mul_const)
#print("乘以多项式的结果:", result_mul_poly)