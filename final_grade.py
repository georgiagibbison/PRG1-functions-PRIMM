
def Final_Grade (Homework,Test):
    total=Homework+Test
    HWpercent=(Homework/total)*100
    TPercent=(Test/total)*100
    return TPercent

print(Final_Grade(5,7))