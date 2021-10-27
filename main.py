import math
from matrixcal import MatrixCalculator as mc

answer_list = []
for i in range(0,4):
    answer_list.append([])

a = [[2,-1],[3,5]]
b = [[-2,0],[4,2]]
c = [[-1,2,0],[2,0,3]]
e = [[2,-1],[math.pi,math.log10(2)],[-2,6]]
f = [[1,2,3],[2,3,4],[3,5,7]]
i = [[1,0,0],[0,1,0],[0,0,1]]

Ans1_a = mc.plus(a,mc.multiply(3,b))

answer_list[0].append(Ans1_a)
Ans1_a_2 = mc.minus(c,mc.matrixmultiply(b,mc.matrixtran(e)))
answer_list[0].append(Ans1_a_2)

Ans1_a_3 = mc.matrixtran(a)
answer_list[0].append(Ans1_a_3)

m = mc.matrixmultiply(a,b)
n = mc.matrixmultiply(b,a)

Ans1_b = m == n

answer_list[1].append(Ans1_b)

p = mc.matrixmultiply(mc.matrixtran(c),mc.matrixtran(b))
q = mc.matrixtran(mc.matrixmultiply(b,c))

Ans1_c = p == q
answer_list[2].append(Ans1_c)

ans1_d = mc.inv(a)

answer_list[3].append(ans1_d)

print(answer_list)





