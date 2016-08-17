def checkDistinct(id, next):
    '''重複チェック'''
    tmp = [0,0]
    #print(id)
    while id:
        x = id[0]
        if x == '0':
            tmp[1] -= 1
        elif x == '1':
            tmp[0] += 1
        elif x == '2':
            tmp[1] += 1
        elif x == '3':
            tmp[0] -= 1
        #print("next = "+str(next))
        #print("tmp = "+str(tmp))
        #print("tmp="+str(tmp))
        #print("next="+str(next))
        if tmp == next:
            #print("dame")
            return False
        id = id[1:]
    return True

def checkKabe(next):
    #print("next="+str(next))
    if data[next[0]][next[1]] is "*" or next == [21, 21]:
        return False
    return True
def check(id, next):
    if checkKabe(next):
        if checkDistinct(id, next):
            return True
    return False

def printans(id):
    ans = ""
    tmp = [0,0]
    while id:
        x = id[0]
        if x == '0':
            tmp[1] -= 1
        elif x == '1':
            tmp[0] += 1
        elif x == '2':
            tmp[1] += 1
        elif x == '3':
            tmp[0] -= 1
        if data[tmp[0]][tmp[1]] is not "+":
            ans = ans + str(data[tmp[0]][tmp[1]])
        id = id[1:]
    print(ans)








f = open("input.txt", "r")
i = 0
data = [[]]
for row in f:
    data[i] = row
    data[i].rstrip("\n")
    i = i+1
    data.append([])

##ここまでで配列rに一行ごとに読み込まれている

nm = data[0].split(" ")
height = int(nm[0])
width = int(nm[1])
del data[0]
##ここまでで高さnと横幅mをゲット

tree = [{}]
#treeを初期化する

tree[0]["pre"] = -1 #前のやつ
tree[0]["now"] = [0, 0]
#次に行ける場所を見つける
if data[0][1] is not "*":
    tree[0]["next3"] = [0, 1]
if data[1][0] is not "*":
    tree[0]["next2"] = [1, 0]
#桁数
#tree[0]["dig"] = 0
tree[0]["id"] = ""
n=1
pre=0

while tree[pre]["now"] != [height-1, width-1]:
    for i in range(1, 5):
        if "next" + str(i) in tree[pre]:
            tree.append({})
            tree[n]["pre"] = pre
            tree[n]["now"] = tree[pre]["next" + str(i)]
            #tree[n]["dig"] = 1
            tree[n]["id"] = str(tree[pre]["id"]) + str(i - 1)
            #nextを入れる
            #nextがtree[tree[n]["pre"]]["now"](きたとこ)以外の場合。
            #←↓→↑
            k=1
            id = tree[n]["id"]
            next = [tree[n]["now"][0], tree[n]["now"][1]-1]
            if next != tree[tree[n]["pre"]]["now"] and next[1] >= 0 and check(id, next):
                #nowの左
                #print(next)
                tree[n]["next1"] = next
                k+=1
            next = [tree[n]["now"][0]+1, tree[n]["now"][1]]
            if next != tree[tree[n]["pre"]]["now"] and next[0] < height and check(id, next):
                #nowの下
                #print(next)
                tree[n]["next2"] = next
                k+=1
            next = [tree[n]["now"][0], tree[n]["now"][1]+1]
            if next != tree[tree[n]["pre"]]["now"] and next[1] < width and check(id, next): 
                #nowの右
                #print(next)
                tree[n]["next3"] = next
                k+=1
            next = [tree[n]["now"][0]-1, tree[n]["now"][1]]
            if next != tree[tree[n]["pre"]]["now"] and next[0] >= 0 and check(id, next):
                #nowの上
                #print(next)
                tree[n]["next4"] = next

            print("pre"+str(pre)+str(tree[pre]["now"])+"->"+str(n)+str(tree[n]["now"]))

            n += 1
    pre += 1 
    #print("n = "+str(n))
    #print("pre = "+str(pre))
    #print("pre[now] = "+str(tree[pre]["now"]))
    #print("pre[id] = "+str(tree[pre]["id"]))
    #print("end")

print(tree[pre]["id"])
ans = tree[pre]["id"]
print(ans)
print(n)
printans(ans)
f.close()
