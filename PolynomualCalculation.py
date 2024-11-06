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

    def __sub__(self, other):
        new_coefficients = self.coefficients.copy()

        for key,value in other.coefficients.items():
            new_coefficients[key] = new_coefficients.get(key,0) - value
        return Polynomial(new_coefficients).simplify()

    def __mul__(self, other):
        #对右边多项式进行按断，看是多项式还是常数项
        if isinstance(other,Polynomial):
            new_coefficients = {}
            for key1,value1 in self.coefficients.items():
                for key2,value2 in other.coefficients.items():
                    new_coefficients[key1+key2] = value1*value2
            return Polynomial(new_coefficients).simplify()
        elif isinstance(other,(int,float)):
            new_coefficients = {key : value * other for key,value in self.coefficients.items()}
            return Polynomial(new_coefficients).simplify()
        else:
            return NotImplemented

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




