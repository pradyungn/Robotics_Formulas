"""
Variable Names
--------------
gg: Ground Green
go: Ground Orange
gp: Ground Purple
tg: Tower Green
to: Tower Orange
tp: Tower Purple
p: points
hp: highest points
"""
"""
Constraints
-----------
22 >= tg + gg
22 >= to + go
22 >= tp + gp
"""
"""
Equation
--------
p =  (1+tp)*gp + (1+to)*go + (1+tg)*gg
"""
hp = 0
permutations = []
curset = []
for tg in range(22):
    for gg in range(22):
        if tg+gg <= 22:
            for to in range(22):
                for go in range(22):
                    if to+go <= 22:
                        for tp in range(22):
                            for gp in range(22):
                                if tp+gp <= 22:
                                    if (tg+to+tp)/7 <= 1:
                                        if tg+to+tp+gp+go+gg <= 66:
                                            p = (1 + tp) * gp + (1 + to) * go + (1 + tg) * gg
                                            if p == hp:
                                                curset = [gg, tg, go, to, gp, tp]
                                                permutations.append(curset)
                                                print('Points was '+str(p))
                                                print('Values were '+str(curset))
                                            elif p > hp:
                                                hp = p
                                                permutations = []
                                                curset = [gg, tg, go, to, gp, tp]
                                                permutations.append(curset)
                                                print('Points was ' + str(p))
                                                print('Values were ' + str(curset))
                                            else:
                                                print("Failed run")
lmao = open('cool.txt', 'w')
for i in permutations:
    lmao.write(str(i))
print(hp)
