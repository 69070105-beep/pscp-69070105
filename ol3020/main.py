"""coke"""

old_price = int(input())
cap = int(input())
new_price = int(input())
many = int(input())

if not many:
    print(0)
elif not cap:
    print(old_price * many)
else:
    on_sale_cap = (many - 1) // cap
    many_old = many - on_sale_cap
    total_newprice = on_sale_cap * new_price
    total_oldprice = many_old * old_price
    all_total = total_oldprice + total_newprice
    print(all_total)
