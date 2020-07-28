def calc_pay(hour, rate):
	pay = hour * rate
	print "pay:",pay



h = int(raw_input("enter hour: "))
r = int(raw_input("enter rate: "))

calc_pay(h,r)
