def student_scores():
    students = {"Harry":"66",
                "Ron":"52",                 #names are keys for ex {name:"Harry", score: "99"} keys are name and score.
                "Hermione":"99"}
    new_student, score = input("New student name: "), input("Score: ")
    if new_student in students:
        print("We already have this student")
    students[new_student] = score
    name = input("Update score for: ")
    if name in students:
        students[name] = input("New score: ")
    else:
        print("We do not have this student")
    return students


#Main program:
final_scores = student_scores()
for name in final_scores:
    print(f"Student {name}, score {final_scores[name]}")

#ritems() returns a view object that gives you each key–value pair in the dictionary as a tuple.
sorted_dict = dict(sorted(final_scores.items(), key=lambda item: item[1], reverse=True))

# Three ways to print out first item in sorted dictionary
for name in sorted_dict:
    print(f"1) Student {name}, score {sorted_dict[name]}")
    break

for name, score in sorted_dict.items():
    print(f"2) The highest score has {name}: {score}.")
    break

for name, score in sorted_dict.items():
    print(f"3) The highest score has {name}: {score}.")
    break


def top_st(scores):
    highest_name = max(scores, key=scores.get)
    return highest_name

print(f"Top student is {top_st(final_scores)}")