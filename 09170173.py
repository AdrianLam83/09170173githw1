import pprint

james = ["leborn james",23,19,22,31,18]
games = len(james)
score_max = max(james[1:games])
x = james.index(score_max)
print(f"{james[0]} 在第{x}場得最高分{score_max}")


a = [["leborn james","SF","12/30/84"],23,19,22,31,18]
games = len(a)
score_max = max(a[1:games])
y = a.index(score_max)
name,tion,bd = a[0][0],a[0][1],a[0][2]
print("姓名:     ",name)
print("位置:     ",tion)
print("出生日期: ",bd)


sc = [["洪錦魁", 80, 95, 88, 0],
        ["洪冰儒", 98, 97, 96, 0],
        ["洪雨星", 90, 91, 92, 0],
        ["洪冰雨", 91, 93, 95, 0],
        ["洪星宇", 92, 97, 90, 0]]
sc [0][4] = sum(sc[0][1:4])
sc [1][4] = sum(sc[1][1:4])
sc [2][4] = sum(sc[2][1:4])
sc [3][4] = sum(sc[3][1:4])
sc [4][4] = sum(sc[4][1:4])
pprint.pprint(sc)

sc.sort(key = lambda x:x[4],reverse = True)
for z in sc:
    print(z)


