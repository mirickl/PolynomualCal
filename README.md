# 基于Python实现的一元多项式计算
Unary sparse polynomials based on python



### 【问题描述】 


设计一个一元稀疏多项式简单计算器。 




### 【基本要求】 


一元稀疏多项式简单计算器的基本功能是：


(1) 输入并建立多项式 ；


(2) 输出多项式，输出形式为整数序列：n，cl，el，c2，e2，…，cn，en，其中n是多项式的项数，ci 和ei，分别是第 i 项的系数和指数，序列按指数降序排列；


(3) 多项式a和b相加，建立多项式a +b；


(4) 多项式a和b相减，建立多项式a -b 。 





### 【测试数据】 


(2x+5x8－3.1x11) + (7－5x8+11x9)=(－3.lx11+11x9+2x+7) 


(6x-3－x+4.4x2－1.2x9) －(-6x-3+5.4x2－x2+7.8x15)  =(-7.8x15-1.2x9+12x-3-x)  


(1 +x + x2+x3+x4+x5)+(-x3－x4)=(1+x+x2+x5) 
 

(x+x3)+(-x－x3)=0  

(x+x100)+(x100 +x200)=(x+2x100+x200)


(x+x2+x3)+0=x+x2+x3  


计算多项式在x处的值。多项式a和b相乘，建立乘积多项式ab 。 


多项式的输出形式为类数学表达式。例如 ，多项式 -3x8+6x3－18 的输出形式为  -3x^8+6x^3-18，x15+(－8)x7－14的输出形式为x^15-8x^7-14。


注意，数值为1的非零次项的输出形式中略去系数1，如项1x8的输出形式为x8，项 －1x3的输出形式为－x3。




### 【实现提示】  


用带表头结点的单链表存储多项式。 
