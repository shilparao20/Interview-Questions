"""
You are a developer for a university. Your current project is to develop a system for students to find courses they share with friends. The university has a system for querying courses students are enrolled in, returned as a list of (ID, course) pairs.

Write a function that takes in a collection of (student ID number, course name) pairs and returns, for every pair of students, a collection of all courses they share.
"""

def find_pairs(student_course_pairs):

    course_pair = {}

    for i in range(len(student_course_pairs)):
         temp = []

         studId = student_course_pairs[i][0]
         courseName = student_course_pairs[i][1]

         while i < (len(student_course_pairs)-1):
            next_studId = student_course_pairs[i+1][0]
            next_courseName = student_course_pairs[i+1][1]

            new_studId = str(studId).strip() + "," + str(next_studId).strip()
            temp_key = str(next_studId).strip() + "," + str(studId).strip()

            if courseName == next_courseName:
                temp.append(courseName)
                if temp_key in course_pair:
                    # get the value and append the new value to the key
                    # check if the course is already added to the key
                    if courseName not in course_pair[temp_key]:
                        temp = course_pair[temp_key] + temp
                        course_pair[temp_key] = temp
                else:
                    if new_studId in course_pair:
                        temp = course_pair[new_studId] + temp
                    course_pair[new_studId] = temp
                    temp = []
            else:
               # if the course is not repeated
               if str(studId).strip() != str(next_studId).strip():
                   if temp_key not in course_pair and new_studId not in course_pair:
                        new_studId = str(studId).strip() + "," + str(next_studId).strip()
                        course_pair[new_studId] = []

            i += 1

    print('\n',course_pair,'\n')


student_course_pairs_1 = [
  ["58", "Linear Algebra"],
  ["94", "Art History"],
  ["94", "Operating Systems"],
  ["17", "Software Design"],
  ["58", "Mechanics"],
  ["58", "Economics"],
  ["17", "Linear Algebra"],
  ["17", "Political Science"],
  ["94", "Economics"],
  ["25", "Economics"],
  ["58", "Software Design"],
]

find_pairs(student_course_pairs_1)

'''
Sample Output (pseudocode, in any order):

find_pairs(student_course_pairs_1) =>
{
  "58,17": ["Software Design", "Linear Algebra"]
  "58,94": ["Economics"]
  "58,25": ["Economics"]
  "94,25": ["Economics"]
  "17,94": []
  "17,25": []
}
'''

student_course_pairs_2 = [
  ["0", "Advanced Mechanics"],
  ["0", "Art History"],
  ["1", "Course 1"],
  ["1", "Course 2"],
  ["2", "Computer Architecture"],
  ["3", "Course 1"],
  ["3", "Course 2"],
  ["4", "Algorithms"]
]

find_pairs(student_course_pairs_2)

'''
Sample output:

find_pairs(student_course_pairs_2) =>
{
  "1,0":[]
  "2,0":[]
  "2,1":[]
  "3,0":[]
  "3,1":["Course 1", "Course 2"]
  "3,2":[]
  "4,0":[]
  "4,1":[]
  "4,2":[]
  "4,3":[]
} 
'''

student_course_pairs_3 = [
  ["23", "Software Design"], 
  ["3", "Advanced Mechanics"], 
  ["2", "Art History"], 
  ["33", "Another"],
]

find_pairs(student_course_pairs_3)

'''
Sample output:

find_pairs(student_course_pairs_3) =>
{
  "23,3": []
  "23,2": []
  "23,33":[]
  "3,2":  []
  "3,33": []
  "2,33": []
}
'''
