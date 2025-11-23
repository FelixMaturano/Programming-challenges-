# Vamos a convertir de string a numeros 

nums = [1, 2, 3, 4]
result = int("".join(str(x)for x in nums))
print(result)


# Example
grades_string = "88-77-59-63"
total_grade = 0
grades_list = grades_string.split("-")



# grade_list = [int(x) for x in grades_string.split("-")]

for grade in grades_list:
    grade = int(grade)
    total_grade += grade


print(total_grade)
