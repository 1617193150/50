#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
class Student:
   '所有学生的基类'
   stuCount = 1
 
   def __init__(self, name, stu_no, class_no, gender):
      self.name = name
      self.stu_no = stu_no
      self.class_no = class_no
      self.gender = gender
      Student.stuCount += 1
   

   def speakEnglish(self):
      print self.name, "can speak english!!"

   def canPrograme(self):
      print self.name, "canPrograme!!"

   def canSwin(self):
      print self.name, "canSwin!!"
