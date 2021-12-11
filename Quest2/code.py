from z3 import *

a = Bool('A')
b = Bool('B')
c = Bool('C')
d = Bool('D')
e = Bool('E')
f = Bool('F')
g = Bool('G')
h = Bool('H')
i = Bool('I')
j = Bool('J')

exp1 = And(Not(Or(a, Not(b))), Not(Or(Or(Not(c), d),Or(e, Not(f)))))
exp2 = And(And(Not(Or(g,h)), Xor(h, i)), And(i, j))

print(solve(And(exp1, exp2)))
