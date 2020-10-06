from z3 import *

qword_602148 = Int('0')
qword_602150 = Int('1')
qword_602158 = Int('2')
qword_602160 = Int('3')

SOLVER = Solver()
SOLVER.add(-24 * qword_602148 -18 * qword_602150 -15 * qword_602158 - 12 * qword_602160 == -18393)
SOLVER.add(9 * qword_602158 + 18 * (qword_602150 + qword_602148) - 9 * qword_602160 == 4419)
SOLVER.add(4 * qword_602158 + 16 * qword_602148 + 12 * qword_602150 + 2 * qword_602160 == 7300)
SOLVER.add(-6 * (qword_602150 + qword_602148) - 3 * qword_602158 - 11 * qword_602160 == -8613)

print(SOLVER.check())
print(SOLVER.model())

