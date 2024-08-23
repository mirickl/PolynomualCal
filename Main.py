class Node:
    # 定义一个节点类，用于表示稀疏多项式中的每一项
    def __init__(self, coef=0, exp=0, next=None):
        self.coef = coef  # 系数
        self.exp = exp    # 指数
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
        return "+".join(terms)

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

# 示例代码：
poly1 = SparsePolynomial()
poly1.add_term(2, 8)
poly1.add_term(5, 0)
poly2 = SparsePolynomial()
poly2.add_term(7, 0)
poly2.add_term(-5, 8)
poly2.add_term(11, 9)
result = poly1.add(poly2)
print(result.display())  # 输出：2x^8+16x^9+7