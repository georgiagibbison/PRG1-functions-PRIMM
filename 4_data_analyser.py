def analyse_scores(scores):
    if not scores:
        return {"error": "No scores provided"}
    
    total = sum(scores)
    average = total / len(scores)
    highest = max(scores)
    lowest = min(scores)
    
   
    # Count grades
    grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    grade_percentages = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for score in scores:
        if score >= 90:
            grade_counts["A"] += 1
            
        elif score >= 80:
            grade_counts["B"] += 1
            
        elif score >= 70:
            grade_counts["C"] += 1

        elif score >= 60:
            grade_counts["D"] += 1
          
        else:
            grade_counts["F"] += 1

    for grade in grade_counts:
        grade_percentages[grade]=f"{(grade_counts[grade]/len(scores)*100)}%"
    
    return {
            "average": round(average, 2),
            "highest": highest,
            "lowest": lowest,
            "total_students": len(scores),
            "grade_distribution": grade_counts,
            "grade_percentage":grade_percentages,
            
            }


# Test data
test_scores = [85, 92, 78, 90, 87, 95, 82, 88, 91, 79]
total_tests = len(test_scores)

import statistics
median=(statistics.median(test_scores))




empty_list = []
length=len(test_scores)
#pass mark
i=0
while length>0:
    if test_scores[i]>=60:
        print("you have passed")
        length=length-1
    else:
        print("you have failed")
        length=length-1

#grade percentage

print("Test Results:")
print(analyse_scores(test_scores))
print(median)
print("\nEmpty List Test:")
print(analyse_scores(empty_list))

