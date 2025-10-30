x=int(input())
bill=0
if x<=100:
    bill=x*4
elif x<=200:
  bill=400+(x-100)*5
elif x<=300:
    bill=900+(x-200)*6
elif x<=400:
    bill=1500+(x-300)*7
elif x>400:
    bill=2200+(x-400)*8
bill+=bill*0.1
print(round(bill,1))
