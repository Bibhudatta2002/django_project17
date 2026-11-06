from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from django.db.models import *
#from django.db.models import Avg,Max,Min,Sum,Count,F,OuterRef,Subquery
from django.db.models.functions import Length

# Create your views here.

def insert_emp(request):
    print('available deptnos are:--------')
    for i in Dept.objects.all():
        print(i.deptno)
    dn=input('Enter a deptno')
    LDO=Dept.objects.filter(deptno=dn)
    if LDO:
        DO=LDO[0]
        empno=int(input('enter employee num'))
        ename=input('enter employee name')
        job=input('enter job')
        mgr=input('enter mgr number')
        MEO = Emp.objects.filter(mgr=mgr)
        if MEO:
            MEO[0]=int(mgr)
        else:
            mgr=None
        hiredate=input('YYYY-MM-DD')
        sal=int(input('enter salary'))
        comm=input('enter commission')
        if comm:
            comm=int(comm)
        else:
            comm=None
        TUEO=Emp.objects.get_or_create(empno=empno,ename=ename,job=job,mgr=mgr,hiredate=hiredate,sal=sal,comm=comm,deptno=DO)
        if TUEO[1]:
            return HttpResponse('New employee created')
        else:
            return HttpResponse('employee already exits')
    else:
        return HttpResponse('given deptno is not available')
def display_dept(request):
        QSLD=Dept.objects.all()
        QSLD=Dept.objects.raw('select * from app_dept')
        d={'QSLD':QSLD}
        return render(request,'display_dept.html',d)
def display_emp(request):
        QSLE=Emp.objects.all()
        maxsal = Emp.objects.all().aggregate(maxs=Max('sal'))['maxs']
        print(maxsal)
        QSLE=Emp.objects.filter(deptno=10).aggregate(maxc=Max('sal'))
        print(QSLE['maxc'])
        QSLE=Emp.objects.filter(sal__gt=2000)
        QSLE=Emp.objects.filter(deptno__dname='ACCOUNTING')
        AVGSAL=Emp.objects.all().aggregate(avgsal=Avg('sal'))['avgsal']
        print(AVGSAL)
        QSLE=Emp.objects.filter(sal__gt=AVGSAL)
        # d10ms=Emp.objects.filter(deptno=10).aggregate(ms=Max('sal'))['ms']
        # QSLE=Emp.objects.filter(d10ms)
        QSLE=Emp.objects.all()
        QSLE=Emp.objects.filter(comm__gt=F('sal'))
        QSLE=Emp.objects.annotate(lenename=Length('ename')).filter(lenename=5)
        DWAVGSAL=Emp.objects.filter(deptno=OuterRef('deptno')).values('deptno').annotate(avgs=Avg('sal')).values('avgs')
        QSLE=Emp.objects.filter(sal__gt=Subquery(DWAVGSAL))
        print(Emp.objects.values('deptno').annotate(avgs=Avg('sal')))
        QSLE=Emp.objects.raw('select * from app_Emp')
    
def emptodeptjoin (request):
        QSLEDO=Emp.objects.all().select_related('deptno')
        QSLEDO=Emp.objects.select_related('deptno').all()
        QSLEDO=Emp.objects.filter(sal__gt=2000).select_related('deptno')
        QSLEDO=Emp.objects.select_related('deptno').filter(deptno__dname='ACCOUNTING',sal__gt=2000)
        
        d={'QSLEDO':QSLEDO}
        return render(request,'emptodeptjoin.html',d)
def emptomgrjoin (request):
        QSLEMO=Emp.objects.all().select_related('mgr')
        QSLEMO=Emp.objects.select_related('mgr').filter(mgr__ename='KING')

        d={'QSLEMO':QSLEMO}
        return render(request,'emptomgrjoin.html',d)
# def emptomgranddept
#          d={'QSLE':QSLE}
#         return render(request,'display_emp.html',d)
def display_salgrade(request):
        QSLSG=Salgrade.objects.all()
        QSLSG=Salgrade.objects.raw('select * from app_Salgrade')
        d={'QSLSG':QSLSG}
        return render(request,'display_salgrade.html',d)


                

