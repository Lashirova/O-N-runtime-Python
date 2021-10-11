duplicate_list = ["homework", "assignment", "quiz", "discussion", "quiz", "program"];

for i in range(len(duplicate_list)):
    for j in range(i+1,len(duplicate_list)):
        if(duplicate_list[i] == duplicate_list[j]):
            print("Yes, there is a duplicate. [e.g. '{}']".format(duplicate_list[i]))
            