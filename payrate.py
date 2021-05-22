hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate per hour:")
r = float(rate)
if(h <= 40):
    pay = h*r
else:
    pay = 40.0*r+((h-40)*1.5*r)
print(pay)
