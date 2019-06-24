#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import django
os.environ["DJANGO_SETTINGS_MODULE"] = 'project.settings'
django.setup()

from courses.models import Student, Course, Team, Student_Team

from rubrics.models import Rubric

from evaluation.models import Evaluation, Evaluation_Course, Evaluation_Student 

from accounts.models import Account
from django.contrib.auth.models import User

import csv
import os

from datetime import datetime

# def load_students():
#     c = Course.objects.get(code='CC4401', year=2019, semester="Otoño")
#     with open('data/alumnos.tsv') as tsvfile:
#         reader = csv.reader(tsvfile, delimiter='\t')
#         for row in reader:
#             # print(row)
#             names = row[1].split(" ")
#             first_name = names[0]
#             last_name = names[-2] if len(names[-1]) == 2 else names[-1]
#             a = Student(first_name=first_name, family_name=last_name, course=c)
#             a.save()


def load_teams():
    c = Course.objects.get(code='CC4401', year=2019, semester="Otoño")
    with open(os.path.dirname(os.path.realpath(__file__))+ '/data/grupos.tsv') as file:
        for line in file:
            team_name = line.replace("\t", "").replace("\n", "")
            a = Team(name=team_name, course=c)
            a.save()


def load_student_at_team():
    c = Course.objects.get(code='CC4401', year=2019, semester="Otoño")
    group = ""
    t = None
    with open(os.path.dirname(os.path.realpath(__file__))+'/data/grupo-alumno.tsv') as tsvfile:
        reader = csv.reader(tsvfile, delimiter='\t')
        for row in reader:
            if row[0] == "Grupo":
                group = row[1]
                print(group)
                t = Team.objects.get(name=group, course=c)
            
            else:
                names = row[1].split(" ")
                first_name = names[0]
                last_name = names[-2] if len(names[-1]) == 2 else names[-1]
                s = Student.objects.create(first_name=first_name, family_name=last_name, team=t)
                # sat = StudentAtTeam(student=s, team=t, active=True)
                s.save()


def create_evaluators():
    
    names = ["Jocelyn", "Daniela", "María", "Pablo"]
    last_names = ["Simmonds", "Chacón", "Berguer", "Miranda"]
    is_admin = [False]*3 + [True]
    
    for i in range(len(names)):
        account = Account.objects.create(nombre = names[i], appellido = last_names[i],
                                        correo = f"foo{i}@gmail.com", clave = "$foo$bar$", is_superuser = is_admin[i])
        account.save()
        nickname = names[i] + last_names[i]
        user = User.objects.create_user(username=nickname, email=f"foo{i}@gmail.com", password="$foo$bar$")
        user.save()


def create_course():
    course = Course.objects.create(code="CC4401", section=1, year=2019, semester="Otoño", title="Ingeniería de Software I")
    course.save()


def create_rubric():
    name = "test"
    duration_min = 5
    duration_max = 7
    state = True

    rubric =""" 
        [["", "0.", "0.3", "0.5", "0.7", "1.0"],
        ["A", "B", "C", "D", "E", "F", "G"],
        ["A", "B", "C", "D", "E", "F", "G"],
        ["A", "B", "C", "D", "E", "F", "G"],
        ["A", "B", "C", "D", "E", "F", "G"],
        ["A", "B", "C", "D", "E", "F", "G"],
        ["A", "B", "C", "D", "E", "F", "G"]]"""

    # rubric = str(rubric)
    r = Rubric.objects.create(name=name, duration_min=duration_min, duration_max=duration_max, state=state, rubric=rubric)



def create_evaluations(n=1):
    c = Course.objects.get(code='CC4401', year=2019, semester="Otoño")
    r = Rubric.objects.get(name='test')

    for i in range(n):
        ev = Evaluation.objects.create(name=f"Evaluation {i}", init_date=datetime.today(), fin_date=datetime.today(), state=False , rubric=r)
        ev.save()
        evc = Evaluation_Course(evaluation_name=ev, course=c)
        evc.save()

            teams = Team.objects.filter(course=c)
        for team in teams:
            people = Student.objects.filter(team=team)
            for student in people:
                eval = Evaluation_Student.objects.create(evaluation_id=ev, student=student, grade=0.0)
                eval.save()


if __name__ == '__main__':
    # create_evaluators()
    load_students()
    load_teams()
    load_student_at_team()
    # load_teams()
