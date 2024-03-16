with open("C:\\Users\\Admin\\Documents\\Code\\Python\\Bài luyện youtube\\Bai5\\KANGAROO.INP") as f:
    n,a,b = map(int, f.readline().split())
def foot(n):
    dem=0
    max_long = n // b
    for i in range(max_long,-1,-1):
        remain = n - i * b
        if remain % a == 0:
            dem = i + remain / a
            break  
    return int(dem)
with open("C:\\Users\\Admin\\Documents\\Code\\Python\\Bài luyện youtube\\Bai5\\KANGAROO.OUT","w") as f_2:
    f_2.write(str(foot(n)))