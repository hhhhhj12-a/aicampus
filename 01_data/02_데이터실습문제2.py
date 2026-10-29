#거스름돈 계산
bread_price=3500
bread_count=2
cake_price=4200
cake_count=1
paid=20000

bread_total=bread_price*bread_count
cake_total=cake_price*cake_count
total=bread_total+cake_total
change=paid-total


print(total)
print('거스름돈 : ', change, '원')





