class Polynomial:
    def __init__(self,coefficients):
        #初始化多项式，其中coefficients是一个字典
        self.coefficients = coefficients

    def simplify(self):
        # 化简多项式，移除系数项为0的项
        self.coefficients = {k:v for k,v in self.coefficients.items() if v != 0}
        return self

    def __add__(self, other):
        """重载加法运算符"""
        new_coefficients = self.coefficients.copy()

        if isinstance(other, Polynomial):
            for power, coeff in other.coefficients.items():
                new_coefficients[power] = new_coefficients.get(power, 0) + coeff
        elif isinstance(other, (int, float)):
            new_coefficients[0] = new_coefficients.get(0, 0) + other
            # print(new_coefficients)
        return Polynomial(new_coefficients).simplify()

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        #对多项式进行判断
        new_coefficients = self.coefficients.copy()

        if isinstance(other,Polynomial):
            for key,value in other.coefficients.items():
                new_coefficients[key] = new_coefficients.get(key, 0) - value
            print(new_coefficients)
        elif isinstance(other,(int,float)):
            new_coefficients[0] = new_coefficients.get(0,0) - other

        return Polynomial(new_coefficients).simplify()

    def __rsub__(self, other):
        #重载常数项与多项式的减法
        if isinstance(other,(int,float)):
            new_coefficients = {0:other}
            for key,value in self.coefficients.items():
                new_coefficients[key] = -value
            return Polynomial(new_coefficients).simplify()
        return NotImplemented

    def __mul__(self, other):
        #对多项式进行按断，看是多项式还是常数项
        if isinstance(other,Polynomial):
            new_coefficients = {}
            for key1,value1 in self.coefficients.items():
                for key2,value2 in other.coefficients.items():
                    new_coefficients[key1+key2] = value1*value2
                    # print(new_coefficients)
            return Polynomial(new_coefficients).simplify()
        elif isinstance(other,(int,float)):
            new_coefficients = {key : value * other for key,value in self.coefficients.items()}
            return Polynomial(new_coefficients).simplify()
        else:
            return NotImplemented

    def __pow__(self, power, modulo=None):
        if power < 0 :
            print("请输入一个正数")
        elif power == 0:
            return Polynomial({0:1})
        elif power == 1:
            return self
        else:
            new_coefficients = Polynomial({0:1})
            for _ in range(power):
                # print(new_coefficients)
                new_coefficients *= self

            return new_coefficients
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
        # print(terms)
        return " + ".join(terms).replace("+ -", "- ")