class Polynomial:
    def __init__(self,coefficients):
        #初始化多项式，其中coefficients是一个字典
        self.coefficients = coefficients

    def simplify(self):
        # 化简多项式，移除系数项为0的项
        self.coefficients = {k:v for k,v in self.coefficients.items() if v != 0}
        return self

    def __add__(self, other):
        # 创建多项式加法的方法
        new_coefficients = self.coefficients.copy()

        for key,value in other.coefficients.items():
            #通过键值进行相加
            new_coefficients[key] = new_coefficients.get(key,0) + value

        return Polynomial(new_coefficients).simplify()

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

if __name__ == "__main__":
    poly1 = Polynomial({3:1,2:3,0 : 8})
    poly2 = Polynomial({5:1,3:1,4:5, 0: 8})

    result_add = poly1 + poly2

    print(result_add)



