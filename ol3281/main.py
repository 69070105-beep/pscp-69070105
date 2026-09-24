"""ijudge-itkmitl"""

link = input()
NEED = "https://ijudge.it.kmitl.ac.th/problems/"

if link.startswith(NEED):
    remainder = link[len(NEED):]
    if remainder.endswith("/"):
        remainder = remainder[:-1]

    if len(remainder) == 4 and remainder.isdigit() and remainder[0] in "0123":
        print(f"{remainder[0]} STAR")
    else:
        print("INVALID")
else:
    print("INVALID")
