""" Hint """

ops = {
    "==": lambda a, b: a == b,
    ">": lambda a, b: a > b,
    "<": lambda a, b: a < b,
    ">=": lambda a, b: a >= b,
    "<=": lambda a, b: a <= b,
    "!=": lambda a, b: a != b,
}

u_op, u_val = input().split()
t_op, t_val = input().split()
h_op, h_val = input().split()

u_val, t_val, h_val = int(u_val), int(t_val), int(h_val)

for h in range(10):
    if ops[h_op](h, h_val):
        for t in range(10):
            if ops[t_op](t, t_val):
                for u in range(10):
                    if ops[u_op](u, u_val):
                        print(f"{h}{t}{u}")
