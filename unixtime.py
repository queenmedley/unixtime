import time

t=time.time()
days=t/(60*60*24)
year_sec=60*60*24*365
year_4_sec=60*60*24*366
year_4_sec_sum=3*year_sec+year_4_sec

year=t/year_4_sec_sum
day_sum=0
base_year=1970
d=int(days)
print('All day is',d)
while d>0 :
    if base_year%4==0:
        d=d-366
        base_year=base_year+1
        day_sum=day_sum+366
        print('366',d,base_year,day_sum)
    else:
        d=d-365
        base_year=base_year+1
        day_sum=day_sum+365
        print('365',d,base_year,day_sum)





