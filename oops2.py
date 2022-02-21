class student:
    school_name="bbs"# class variable
    pass
marks =student()
subjects= student()
marks.kunal={"english":92,
             "maths":96,
             "hindi":31,
             "science":100}
marks.amit={"english":49,
             "maths":34,
             "hindi":31,
             "science":100}
subjects.amit=["python","java"]
subjects.kunal=["c#","ds and algo"]
print(marks.kunal,
      subjects.kunal,
      marks.amit,
      subjects.amit)
print(marks.school_name)
student.school_name ="kanyakumari school"
print(marks.school_name)
print(marks.__dict__)
