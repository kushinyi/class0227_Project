#計算圓面積
#a=int(input('輸入圓直徑='))
#pi=3.14
#print(2*a**2*pi)

#計算學生平均成績
#grades=[10,30,40,90,100,60]
#print(sum(grades)/len(grades))
#計算成績開根號再乘以10
#grades[0]=grades[0]**0.5*10
#grades[1]=grades[1]**0.5*10
#grades[2]=grades[2]**0.5*10
#grades[3]=grades[3]**0.5*10
#grades[4]=grades[4]**0.5*10
#grades[5]=grades[5]**0.5*10
#print(grades)

#---------
#x=10
#y=6
#print(x>=y)
#---------
#score=60
#if score>=60:
#    print('及格了')
#else:
#    print('不及格')
#--------
#sex=int(input('輸入性別(女生0,男生1):'))
#hight=int(input('輸入身高:'))
#if sex<=0:
#    if hight>=170:
#        print("打排球")
#    else:
#        print("不打球")
#else:
#    if hight>=190:
#        print("打籃球")
#    else:
#        print("不打球")
#--------------------------
#number=int(input('輸入數字:'))
#if number%2<1:
#    print("是偶數")
#else:
#    print("是奇數")
#-------------------------
#for i in range(0,10):
#    print(i)
#for i in range(0,10,2): #(開始,結束,一次跳多少)
#    print(i)
#------------------------
#mathScores=[60,70,10,20,81,63,4]
#l=len(mathScores)
#for i in range(0,l):
#    print(i,mathScores[i])
#for item in mathScores:  #印出每一個元素
#    print(item)
#------------------------
#mathScore=[60,70,10,20,81,63,4]
#for item in mathScore:
#    item=item*10
#    print(item)
#[item*10 for item in mathScore]
#------------------------
#family={'dad':'Homer','mom':'Lisa'}
#for title,name in family.items():
#    print(title,name)
#for i,j in family.items():
#    print(i)
#for i, j in family.items():
#    print(i,j)
#------------------------
#X=(1,2,3)
#Y=(4,5,6)
#for x,y in zip(X,Y): #解壓縮
#    print(x,y)
#------------------------
#mathScores=[60,70,10,20,81,63,4]
#l=len(mathScores)
#for i in range(0,l):
#    print((i,mathScores[i]))
#for item in mathScores:
#    item=item*10
#    print(item)
#for index,item in enumerate(mathScores):
#    print(index,item)
#-----------------------------------
#count=0
#while count<10: #用while要小心出現無窮迴圈
#    print(count)
#    count+=1
#else:
#    print('coint>=10')
#--------------------------------
#跳出迴圈
mathScores=[60,70,10,20,81,63,4]
#for item in mathScores:
#    if item>80:
#        break
#    print(item)
#mathScores=[60,70,10,20,81,63,4]

#以下的程式碼都跳過，直接進行下一次迴圈
for item in mathScores:
    if item>80:
        continue
    print(item)
