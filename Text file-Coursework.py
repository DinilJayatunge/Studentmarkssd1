List=["[120,0,0]","[100,0,20]","[80,20,20]","[60,0,60]","[40,0,80]"]
List1=["[progress]","[trailer]","[retriever]","[retriever]","[exclude]"]
F=open("Coursework SD 1 PRO-Lists.txt","a")
for i in range(len(List)):
    F.write(List1[i]+":"+List[i])
    F.write("\n")
F.close()    

