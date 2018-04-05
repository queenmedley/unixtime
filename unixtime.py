import time

t=time.time()
days=int(t/(60*60*24))
hours=int(t/(60*60))
minute=int(t/60)
secs=int(t)
print('unix time is',days,hours,minute,secs)
base_year=1970
d=int(days)

print('All day is',d)

while d>365 :
    if base_year%4==0:
        d=d-366
        base_year=base_year+1
    else:
        d=d-365
        base_year=base_year+1

print('this is year is', base_year)

if base_year%4==0:
    feb=29
else:
    feb=28
print('this',base_year, 'Febrary is',feb)

if d>31+feb+31+30+31+30+31+31+30+31+30:
    month=12
    print('this month is',month)
    d=d-(31+feb+31+30+31+30+31+31+30+31+30)
elif d>31+feb+31+30+31+30+31+31+30+31:
    month=11
    print('this month is',month)
    d=d-(31+feb+31+30+31+30+31+31+30+31)
elif d>31+feb+31+30+31+30+31+31+30:
    month=10
    print('this month is',month)
    d=d-(31+feb+31+30+31+30+31+31+30)
elif d>31+feb+31+30+31+30+31+31:
    month=9
    print('this month is',month)
    d=d-(31+feb+31+30+31+30+31+31)
elif d>31+feb+31+30+31+30+31:
    month=8
    print('this month is',month)
    d=d-(31+feb+31+30+31+30+31)
elif d>31+feb+31+30+31+30:
    month=7
    print('this month is',month)
    d=d-(31+feb+31+30+31+30)
elif d>31+feb+31+30+31:
    month=6
    print('this month is',month)
    d=d-(31+feb+31+30+31)
elif d>31+feb+31+30:
    month=5
    print('this month is',month)
    d=d-(31+feb+31+30)
elif d>31+feb+31:
    month=4
    print('this month is',month)
    d=d-(31+feb+31)
elif d>31+feb:
    month=3
    print('this month is',month)
    d=d-(31+feb)
elif d>31:
    month=2
    print('this month is',month)
    d=d-(31)
else :
    print('this month is 1')

print('today is', d+1)

t_hour=hours-days*24
print('hour is',t_hour+9)

t_mint=minute-days*24*60-t_hour*60
print('min is',t_mint)

t_sec=secs-days*24*60*60-t_hour*60*60-t_mint*60
print('sec is',t_sec)
