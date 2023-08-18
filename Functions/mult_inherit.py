class Teacher(object):
    def __int__(self,teach,mark,assign):
        self.teach=teach
        self.mark=mark
        self.assign=assign

class Student(Teacher):
    def __int__(self,teach,mark,assign , study,exam):
        self.study=study
        self.exam=exam
        Teacher.__int__(self,teach,mark,assign)

    def display(self):
        print(self.teach, self.mark, self.mark, self.assign, self.assign, self.exam)

class  Youtuber():
    def __int__(self,teach,mark,assign,study,exam,create):
         self.create=create
         Student.__int__(self,teach,mark,assign,study,exam)





