import statistics as st

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2],
          [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Hendrik', 'Aaron'}
ABC_students = sorted(list(students))

average_score = [st.mean(grades[0]), st.mean(grades[1]),
                 st.mean(grades[2]), st.mean(grades[3]), st.mean(grades[4])]

a = dict(zip(ABC_students, average_score))
print(a)

