with open("C:\\Users\\Admin\\Documents\\Lập trình cơ bản\\Python\\Bài luyện youtube\\Bai3\\XEPHANG.INP") as f:
    n=int(f.readline())
    lst=f.readline().split()
height=max(lst,key=lst.count)
count=lst.count(height)
out=str(count)+' '+str(height)
with open("C:\\Users\\Admin\\Documents\\Lập trình cơ bản\\Python\\Bài luyện youtube\\Bai3\\XEPHANG.OUT","w") as f_2:
    f_2.write(out)