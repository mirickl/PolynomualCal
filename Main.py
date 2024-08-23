class Node:

    def __init__(self, coef=0, exp=0, next=None):

        self.coef = coef

        self.exp = exp

        self.next = next

class SparsePolynomial:

    def __init__(self):

        self.head = Node()

    def add_term(self, coef, exp):

        if coef == 0:

            return

        cur = self.head

        while cur.next and cur.next.exp > exp:

            cur = cur.next

        if cur.next and cur.next.exp == exp:

            cur.next.coef += coef

        else:

            new_node = Node(coef, exp)

            new_node.next = cur.next

            cur.next = new_node

    def display(self):

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