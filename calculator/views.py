from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'home.html')

def calcu(request):
    day = int(request.POST["day"])
    month = int(request.POST["month"])
    year = int(request.POST["year"])

    
    a = str(int(year/4))
    b,c= (year - 1),(month-1)
    y = ((b%400)%100)
    r = int((b%400)/100)
    x = int(y/4)
    z = y - x
    m = z + x*2
    if c>= 1:
        if year%4 == 0:
            if a.endswith("5"):
                t = 0
            else:
                t = 1
        else:
            t = 0
    if c == 0:
        k = 0
    elif c == 1:
        k = 3
    elif c == 2:
        k = 3 + t
    elif c == 3:
        k = 6 + t
    elif c == 4:
        k = 8 + t
    elif c == 5:
        k = 11 + t
    elif c == 6:
        k = 13 + t
    elif c == 7:
        k = 16 + t
    elif c == 8:
        k = 19 + t
    elif c == 9:
        k = 21 + t
    elif c == 10:
        k = 24 + t
    elif c == 11:
        k = 26 + t
    else:
        res = 'INVALID MONTH'
    if r == 1:
        q = 5
    elif r == 2:
        q = 3
    elif r == 3:
        q = 1
    else:
        q = 0
    Day = ((day+k+m)%7+q%7)%7
    if Day == 0:
        res = 'SUNDAY'
    if Day == 1:
        res = 'MONDAY'
    if Day == 2:
        res = 'TUESDAY'
    if Day == 3:
        res = 'WEDNESDAY'
    if Day == 4:
        res = 'THURSDAY'
    if Day == 5:
        res = 'FRIDAY'
    if Day == 6:
        res = 'SATURDAY'
    else:
        pass

    return render(request, 'result.html', {'result':res})