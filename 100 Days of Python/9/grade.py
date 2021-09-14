marks ={"Anshuman":81,"Jay":83,"Himanshu":86,"Draco":90,"Harry":92,"malfboy":66}

grade={}
for i in marks:
    if marks[i]>90:
        grade[i]="Outstanding"
    elif marks[i]>80 and marks[i]<91:
        grade[i]="Exceeds Exception"
    elif marks[i]>70 and marks[i]<81:
        grade[i]="Acceptable"
    elif marks[i]<71:
        grade[i]="Fail"

print(grade)