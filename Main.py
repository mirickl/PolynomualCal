import re


class Node:
    # 定义一个节点类，用于表示稀疏多项式中的每一项
    def __init__(self, coef=0, exp=0, next=None):
        self.coef = coef  # 系数
        self.exp = exp  # 指数
        self.next = next  # 指向下一个节点的指针


class SparsePolynomial:
    # 定义一个稀疏多项式类，用于表示和操作稀疏多项式
    def __init__(self):
        self.head = Node()  # 创建一个头节点，方便添加新的项

    def add_term(self, coef, exp):
        # 向多项式中添加一项
        if coef == 0:
            return  # 如果系数为0，则不添加该项
        cur = self.head
        # 找到合适的位置插入新项，保持指数降序排列
        while cur.next and cur.next.exp > exp:
            cur = cur.next
        # 如果已存在相同指数的项，则合并系数
        if cur.next and cur.next.exp == exp:
            cur.next.coef += coef
        else:
            # 否则，创建新节点并插入到链表中
            new_node = Node(coef, exp)
            new_node.next = cur.next
            cur.next = new_node

    def display(self):
        # 显示多项式的字符串形式
        cur = self.head.next
        terms = []
        while cur:
            term = ""
            if cur.coef != 1 or (cur.coef == 1 and cur.exp == 0):
                term += str(cur.coef)
            if cur.exp != 0:
                term += "x"
                if cur.exp != 1:
                    term += "^" + str(cur.exp)
            terms.append(term)
            cur = cur.next
        result = "+".join(terms).replace("+-", "-")
        if result=='':
            result = "0"
        return result

    def add(self, other):
        # 实现两个稀疏多项式的加法
        result = SparsePolynomial()
        p1, p2 = self.head.next, other.head.next
        while p1 and p2:
            if p1.exp > p2.exp:
                result.add_term(p1.coef, p1.exp)
                p1 = p1.next
            elif p1.exp < p2.exp:
                result.add_term(p2.coef, p2.exp)
                p2 = p2.next
            else:
                result.add_term(p1.coef + p2.coef, p1.exp)
                p1 = p1.next
                p2 = p2.next
        while p1:
            result.add_term(p1.coef, p1.exp)
            p1 = p1.next
        while p2:
            result.add_term(p2.coef, p2.exp)
            p2 = p2.next
        return result

    def subtract(self, other):
        # 实现两个稀疏多项式的减法
        result = SparsePolynomial()
        p1, p2 = self.head.next, other.head.next
        while p1 and p2:
            if p1.exp > p2.exp:
                result.add_term(p1.coef, p1.exp)
                p1 = p1.next
            elif p1.exp < p2.exp:
                result.add_term(-p2.coef, p2.exp)
                p2 = p2.next
            else:
                result.add_term(p1.coef - p2.coef, p1.exp)
                p1 = p1.next
                p2 = p2.next
        while p1:
            result.add_term(p1.coef, p1.exp)
            p1 = p1.next
        while p2:
            result.add_term(-p2.coef, p2.exp)
            p2 = p2.next
        return result


def transform(input):
    # 该函数通过输入的字符串转化为对应的一元多项式
    poly = SparsePolynomial()
    input = input.replace("-", "+-")
    inputList = re.split(r'[+]', input)
    for i in inputList:
        if i=='':
            continue
        if i.split('x')[0] == '':
            coef = 1
        else:
            temp = i.split('x')[0]
            if temp == '-':
                coef = -1
            else:
                try:
                    coef = int(temp)
                except ValueError:
                    coef = float(temp)

        if len(i.split('^')) == 1:
            if i.find('x') != -1:
                exp = 1
            else:
                exp = 0
        else:
            exp = int(i.split('^')[1])
        poly.add_term(coef, exp)
    return poly


# 主程序
print("欢迎使用一元稀疏多项式计算系统")
choice = "1"
while choice != '0':
    in1 = input("请输入第一个运算数：")
    ploy1 = transform(in1)
    in2 = input("请输入运算符(+/-)：")
    in3 = input("请输入第二个运算数：")
    ploy2 = transform(in3)
    if in2 == "+":
        result = ploy1.add(ploy2)
    elif in2 == "-":
        result = ploy1.subtract(ploy2)
    else:
        print("运算符输入异常,自动设置结果为0")
        result = 0
    print("计算结果：", result.display())
    choice = input("输入0结束程序，输入其他值继续运行\n请输入：")

# 测试数据
'''
(2x+5x^8-3.1x^11)+(7-5x^8+11x^9)=(-3.lx^11+11x^9+2x+7)

(6x-3-x+4.4x^2-1.2x^9)-(-6x-3+5.4x^2-x^2+7.8x^15) =(-7.8x^15-1.2x^9+11x) 

(1+x+x^2+x^3+x^4+x^5)+(-x^3-x^4)=(1+x+x^2+x^5) 

(x+x^3)+(-x-x^3)=0 

(x+x^100)+(x^100+x^200)=(x+2x^100+x^200)

(x+x^2+x^3)+0=x+x^2+x^3

'''
