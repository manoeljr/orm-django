from django.db.models import Q
from django.shortcuts import render

from students.models import Student

from django.db import connection

from students.models import Teacher


def student_list(request):
    # posts = Student.objects.all()
    # posts = Student.objects.filter(surname__startswith='austin') | Student.objects.filter(surname__startswith='baldwin')
    # posts = Student.objects.filter(
    #     Q(surname__startswith='austin') |
    #     ~Q(surname__startswith='baldwin') |
    #     Q(surname__startswith='avery-parker')
    # )
    # posts = Student.objects.filter(
    #     classroom=3 & Student.objects.filter(firstname__startswith='shaina')
    # )

    # posts = Student.objects.all().values_list('firstname').union(Teacher.objects.all().values_list('firstname'))
    # posts = Student.objects.exclude(age__gt=20) & Student.objects.exclude(firstname__startswith='raquel')
    posts = Student.objects.filter(
        ~Q(age__gt=19) &
        ~Q(surname__startswith='baldwin')
    )
    """
        =  Equl
        != Not equal
        >  Greater than, gt
        <  Less than, lt
        >= Greater than or equal to, gte
        <= Less than or equal to, lte
    """

    print(posts)
    print(connection.queries)

    return render(request, 'output.html', {'posts': posts})
