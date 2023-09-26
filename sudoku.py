from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from datetime import *
import random
guess = 0

# easydataset=pd.read_csv("EasyProbSet.csv")
# print((list(easydataset)))
butlist=None
relist = None
pause1 = True
root = None
counter = 66600
converted = "00:00:00"
M=9
SIZE=9
result = False

def coloring():
    last1=[[0 for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            if butlist[i][j]["text"] != "":
                last1[i][j] = int(butlist[i][j]["text"])
                is_safe1(last1[i][j],i,j,last1)

def chk():
    global last
    last=[[0 for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            if butlist[i][j]["text"] != "":
                last[i][j] = int(butlist[i][j]["text"])
            else:
                last[i][j] = 0
            butlist[i][j].destroy()

def is_safe1(n,r,c,matrix):
    colur =True
    colur1=True
        #checking in row
    for i in range(9):
        #there is a cell with same value
        if matrix[r][i] == n:
#            if i!=c:
                butlist[r][c]["fg"] = 'red'
                butlist[r][i]["fg"] = 'red'
                colur = False
        else:
            butlist[r][c]["fg"] = fg
            butlist[r][i]["fg"] = fg
    #checking in column
    if colur:
        for i in range(9):
            #there is a cell with same value
            if matrix[i][c] == n:
#                if i!=r:
                    butlist[r][c]["fg"] = 'red'
                    butlist[i][c]["fg"] = 'red'
                    colur1=False
            else:
                butlist[r][c]["fg"] = fg
                butlist[r][i]["fg"] = fg
        if colur1:
            row_start = (r//3)*3
            col_start = (c//3)*3;
            #checking submatrix
            for i in range(row_start,row_start+3):
                for j in range(col_start,col_start+3):
                    if matrix[i][j]==n:
 #                       if i!=r or j!=c:
                            butlist[i][j]["fg"] = 'red'
                            butlist[r][c]["fg"] = 'red'
                    else:
                        butlist[r][c]["fg"] = fg
                        butlist[r][i]["fg"] = fg
                

def readScore():
    
    file = open("Control.txt", "r")
    c = int(file.read())
    file.close()
    if (c == 1):
        if last==Suduko(pro,0,0):
            if counter <= 66600+600:
                if guess <= 100:
                    return 600+(66600+600-counter)+(100-guess)*2
                else:
                    return 600+(66600+600-counter)+(100-guess)*2
            else:
                if guess <= 100:
                    return 600+(66600+600-counter)+(100-guess)*2
                else:
                    return 600+(66600+600-counter)+(100-guess)*2
        else:
            return "A"

    elif (c == 2):
        if last==Suduko(pro,0,0):
            if counter <= 66600+1200:
                if guess <= 200:
                    return 600+(66600+1200-counter)+(200-guess)*2
                else:
                    return 600+(66600+1200-counter)+(200-guess)*2
            else:
                if guess <= 200:
                    return 600+(66600+1200-counter)+(200-guess)*2
                else:
                    return 600+(66600+1200-counter)+(200-guess)*2
        else:
            return "A"
    elif(c==3):
        if last==Suduko(pro,0,0):
            if counter <= 66600+2400:
                if guess <= 300:
                    return 600+(66600+2400-counter)+(300-guess)*2
                else:
                    return 600+(66600+2400-counter)+(300-guess)*2
            else:
                if guess <= 300:
                    return 600+(66600+2400-counter)+(300-guess)*2
                else:
                    return 600+(66600+2400-counter)+(300-guess)*2
        else:
            return "A"
    elif (c == 4):
        if last==Suduko(pro,0,0):
            if counter <= 71400+600:
                if guess <= 400:
                    return 600+(66600+3600-counter)+(400-guess)*2
                else:
                    return 600+(66600+3600-counter)+(400-guess)*2
            else:
                if guess <= 400:
                    return 600+(66600+3600-counter)+(400-guess)*2
                else:
                    return 600+(66600+3600-counter)+(400-guess)*2
        else:
            return "A"

def check():
    global converted,result
    info.destroy()
    btn.destroy()
    sub.destroy()
    canvas.destroy()
    timelbl.destroy()
    chk()
    import time
    score = open("score.txt","r")
    re = score.read()
    score.close()
    if re=="":
        score=open("score.txt","w")
        score.write("0")
        score.close()
    score = open("score.txt","r")
    lblh = Label(root,bg=mt,fg=fg,text="Your High Score is:\n"+score.read(),font = ("helvetica",20,"bold"))
    score.close()
    time.sleep(0.5)
    for i in range(50,175):
        lblh.place(x=i,y=200)
        root.update()
    # last=[[0 for _ in range(9)] for _ in range(9)]
    # for i in range(9):
    #     for j in range(9):
    #         if butlist[i][j]["text"] != "":
    #             last[i][j] = int(butlist[i][j]["text"])
    #         else:
    #             last[i][j] = 0
    #         butlist[i][j].destroy()
    # if result:
    #     ll.config(text="You have viewed the solution of this puzzle.\nHence no score will be given.\nKindly solve the puzzle without viewing solution.",font=("helvetica",18,"bold"))
    #     result=False
    # else:
    #     if last == Suduko(pro,0,0):
    #         ll.config(text="Congratulations, you have solved the puzzle successfully.",font=("helvetica",18,"bold"))
    #     else:
    #         ll.config(text="Your solution is incorrect, better luck next time.",font=("helvetica",18,"bold"))
    ctt = 0
    score = open("score.txt","r")
    v= Suduko(pro,0,0)
    for i in range(9):
        for j in range(9):
            if pro[i][j]!=last[i][j]:
                if v[i][j]==last[i][j]:
                    ctt+=2
    num  = int(score.read())
    score.close()
    ll = Label(root,bg=mt,fg=fg,font=("helvetica",20,"bold"))
    lg = Label(root,bg=mt,fg=fg,font=("helvetica",18,"bold"))
    if readScore()=="A":
        ll.config(text = "Your Current Score is:\n"+str(ctt))
        lg.config(text="Your solution is incorrect,\nbetter luck next time.")
        lg.place(x=150,y=400)
        if num<ctt:
            score=open("score.txt","w")
            score.write(str(ctt))
            score.close()
            lblh.config(text="Your High Score is:\n"+str(ctt))
    elif result:
        lg.config(text = "You have viewed the solution of this puzzle.\nHence no score will be given.\nKindly solve the puzzle without viewing solution.",font=("helvetica",18,"bold"))
        ll.config(text="Your Current Score is:\n0")
        lg.place(x=20,y=400)
    else:
        ctt = readScore()
        lg.config(text="Congratulations, you have\nsolved the puzzle successfully.")
        ll.config(text = "Your Current Score is:\n"+str(ctt))
        lg.place(x=150,y=400)
        if num<ctt:
            score=open("score.txt","w")
            score.write(str(ctt))
            score.close()
            lblh.config(text="Your High Score is:\n"+str(ctt))
    for i in range(50,160):
        ll.place(x=i,y=300)
        root.update()
    
    # converted ="00:00:00"
    
        

def prnt(v):
    global result
    for i in range(9):
        for j in range(9):
            if butlist[i][j]["text"]=="":
                butlist[i][j].config(text = str(v[i][j]))
                
    info.config(state = DISABLED)
    btn.config(state = DISABLED)
    result = True
    pause1=False

def solve(grid1, row, col, num):
    for x in range(9):
        if grid1[row][x] == num:
            return False
             
    for x in range(9):
        if grid1[x][col] == num:
            return False
 
 
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid1[i + startRow][j + startCol] == num:
                return False
    return True
 
def Suduko(grid1,row,col):
    if (row == M - 1 and col == M):
        return grid1
    if col == M:
        row += 1
        col = 0
    if grid1[row][col] > 0:
        return Suduko(grid1, row, col + 1)
    for num in range(1, M + 1, 1): 
     
        if solve(grid1, row, col, num):
         
            grid1[row][col] = num
            if Suduko(grid1, row, col + 1):
                return grid1
        grid1[row][col] = 0
    return

def res():
    grid1 = pro
    v=Suduko(grid1,0,0)
    prnt(v)


def load():
    global c
    c=0
    for i in range(9):
        for j in range(9):
            if pro[i][j]!=0:
                butlist[i][j].config(text = str(pro[i][j]),state = DISABLED)
                c+=1
            if pro[i][j]==0:
                if relist[i][j] != 0:
                    butlist[i][j].config(text = str(relist[i][j]))
                else:
                    butlist[i][j].config(text = "")
            
    info.config(command=res)

def loadVal():
    global pro
    global choices

    file = open("Control.txt", "r")
    choices = int(file.read())
    file.close()
    if (choices != 0):
        if (choices == 1):
            file = open("Sets/EasyProbSet.csv", "r")
            data = file.read().split("\n")
            random.shuffle(data)
            x = data.index("")
            del data[x]
            # print(data)
            s = random.choice(data)
            file.close()
        elif (choices == 2):
            file = open("Sets/MediumProbSet.csv", "r")
            data = file.read().split("\n")
            random.shuffle(data)
            x = data.index("")
            del data[x]
            s = random.choice(data)
            file.close()
        elif (choices == 3):
            file = open("Sets/HardProbSet.csv", "r")
            data = file.read().split("\n")
            random.shuffle(data)
            x = data.index("")
            del data[x]
            s = random.choice(data)
            file.close()
        elif (choices == 4):
            file = open("Sets/InsaneProbSet.csv", "r")
            data = file.read().split("\n")
            random.shuffle(data)
            x = data.index("")
            del data[x]
            s = random.choice(data)
            file.close()
        prob = []
        row = []
        i = 0
        while (True):
            count = 0
            for j in s:
                if (count < 9):
                    if (j != "["):
                        if (j != "]"):
                            if (j != "," and j != " "):
                                row.append(int(j))
                                count += 1
                else:
                    prob.append(row)
                    row = []
                    i += 1
                    count = 0
            if (i == 9):
                break
        pro = prob

    else:
        pass
    load()


def pause():
    global pause1
    pause1 = False
    for i in range(9):
        for j in range(9):
            butlist[i][j].config(text = "",state = DISABLED)
    btn.config(image = fotu1,command=start)
    

def start():
    global counter,pause1,converted,tt
    if pause1:
        btn.config(command=pause,image=fotu9)
        for i in range(9):
            for j in range(9):
                butlist[i][j].config(state = NORMAL)
        load()
        if counter==66600:
            pass
        else:
            tt = datetime.fromtimestamp(counter)
            converted = tt.strftime("%H:%M:%S")
        if c<81:
            timelbl.after(1000, start)
        timelbl.config(text = converted)
        counter+=1
    if not pause1:
        pause1=True

def warn(e):
    for i in range(9):
        for j in range(9):
            butlist[i][j]["text"]!=""
    root.update()

def keybut(event):
    global relist,guess
    if event.char in "123456789":
        butlist[r][co]["text"]=event.char
        relist[r][co] = event.char
        coloring()
        guess+=1

def button(but,col):
    global r,co
    r=but
    co=col
    
    root.bind("<Key>",keybut)
    
def but():
    global butlist,relist,guess
    y=128
    butlist=[[None for _ in range(9)] for _ in range(9)]
    relist=[[0 for _ in range(9)] for _ in range(9)]
    for i in range(9):
        x=62
        for j in range(9):
            crt=Button(root,bg="white",fg=fg,width = 2,height=1,font=("helvetica",17),borderwidth=0,command=lambda i=i,j=j:button(i,j),activebackground=fg)
            crt.place(x=x,y=y)
            x+=56
            butlist[i][j] = crt
        y+=56
    loadVal()
    

def createCan():
        global canvas
        canvas = Canvas(root, height=500, width=500,bg="white",highlightcolor="black",highlightbackground="black")
        x = 5
        y = 56
        p = 500
        q = 56
        for i in range(10):
            if i == 0:
                line = canvas.create_line(2, 2, 500, 2, width=5)
            elif (i == 1 or i == 2):
                line = canvas.create_line(x, y, p, q, width=1)

                y += 56
                q += 56
            elif (i == 3):
                line = canvas.create_line(x, y, p, q, width=5)

                y += 56

                q += 56
            elif (i == 4 or i == 5):
                line = canvas.create_line(x, y, p, q, width=1)
                y += 56

                q += 56
            elif (i == 6):
                line = canvas.create_line(x, y, p, q, width=5)
                y += 56

                q += 56
            elif (i == 7 or i == 8):
                line = canvas.create_line(x, y, p, q, width=1)
                y += 56
                q += 56
            elif (i == 9):
                line = canvas.create_line(x-3, y-3, p, q-3, width=5)
                y += 56
                q += 56
        x1 = 56
        y1 = 0
        p1 = 56
        q1 = 506
        for i in range(10):
            if i == 0:
                line = canvas.create_line(2, 2, 2, 506, width=5)
            elif (i == 1 or i == 2):
                line = canvas.create_line(x1, y1, p1, q1, width=1)
                x1 += 56
                
                p1 += 56
            elif (i == 3):
                line = canvas.create_line(x1, y1, p1, q1, width=5)
                x1 += 56
                
                p1 += 56
            elif (i == 4 or i == 5):
                line = canvas.create_line(x1, y1, p1, q1, width=1)
                x1 += 56
                
                p1 += 56
            elif (i == 6):
                line = canvas.create_line(x1, y1, p1, q1, width=5)
                x1 += 56
                
                p1 += 56
            elif (i == 7 or i == 8):
                line = canvas.create_line(x1, y1, p1, q1, width=1)
                x1 += 56
                
                p1 += 56
            elif (i == 9):
                line = canvas.create_line(x1 - 3, y1-3, p1-3, q1, width=5)
                x1 += 56
                
                p1 += 56
        canvas.place(x=50, y=120)
        but()


def third():
    global timelbl,sub,info
    lblim.destroy()
    lbl2.destroy()
    choice_button1.destroy()
    choice_button2.destroy()
    choice_button3.destroy()
    choice_button4.destroy()
    lbl11.place(x=134,y=10)
    timelbl = Label(root,text="--:--:--",font=("helvetica",15),bg=mt,fg=fg)
    timelbl.place(x=256,y=630)
    btn.config(command = start,image=fotu9,bg=mt)
    info = Button(root,image=fotu10,bg=mt,borderwidth=0,activebackground=mt)
    info.place(x=65,y=660)
    sub = Button(root,image=fotu11,bg=mt,borderwidth=0,activebackground=mt,command=check)
    sub.place(x=465,y=660)
    createCan()
    start()
    

def second():
    global lblim,choice,selected_choice,choice_button1,choice_button2,choice_button3,choice_button4
    # btn3 = Button(root,text="Back",bg=mt,borderwidth=0,command = first,activebackground=mt)
    # btn3.place(x=10,y=20)
    lbl2.config(text="Please Select the Level of Difficulty:",font=("helvetica",20,"bold"),bg=mt)
    for i in range(-13,35):
        lbl2.place(x=i,y=370)
        root.update()
    l1o8.destroy()
    l2u9.destroy()
    try:
        limg.destroy()
        lb.destroy()
        btnn.destroy()
        btnp.destroy()
        big.destroy()
    except Exception as e:
        pass
    btn2.destroy()
    btn.place(x=265,y=660)
    btn3.place(x=265,y=740)
    try:
        lblim.config(image=fotu,bg=mt)
    except:
        lblim= Label(image=fotu,bg=mt)
        lblim.image=fotu
        lblim.place(x=225,y=150)
    btn32 = Button(root,image=fotu3,bg=mt,borderwidth=0,command = first,activebackground=mt)
    btn32.place(x=10,y=20)        
    choice = IntVar()
    selected_choice = 0
    rad_y=420
    import time
    difficulty = [("  Easy",1),("  Medium",2),("  Hard",3),("  Insane",4)]
    choice_button1 = Radiobutton(root,bg=mt,fg=fg,activebackground=mt,text=difficulty[0][0],variable=choice,command=lambda :ShowChoice(),value=difficulty[0][1],font=("helvetica",17),selectcolor="green")
    # time.sleep(0.2)
    choice_button2 = Radiobutton(root,bg=mt,fg=fg,activebackground=mt, text=difficulty[1][0], variable=choice,command=lambda: ShowChoice(), value=difficulty[1][1],font=("helvetica",17),selectcolor="yellow")
    root.update()
    time.sleep(0.2)
    choice_button3 = Radiobutton(root,bg=mt,fg=fg,activebackground=mt, text=difficulty[2][0], variable=choice,command=lambda: ShowChoice(), value=difficulty[2][1],font=("helvetica",17),selectcolor="orange")    
    root.update()
    time.sleep(0.2)
    choice_button4 = Radiobutton(root,bg=mt,fg=fg,activebackground=mt, text=difficulty[3][0], variable=choice,command=lambda: ShowChoice(), value=difficulty[3][1],font=("helvetica",17),selectcolor="red")
    
    for i in range(15,45):
        choice_button1.place(x=i,y=rad_y)
        choice_button2.place(x=i, y=rad_y+50)
        choice_button3.place(x=i, y=rad_y + 100)
        choice_button4.place(x=i, y=rad_y + 150)
        root.update()
    btn.config(command=lambda:third(),activebackground=mt)
    
def ShowChoice():
    global choices
    control = 1
    selected_choice = choice.get()
    choices = selected_choice
    file = open("Control.txt","w")
    file.write(str(selected_choice))
    file.close()

def helper5():
    btnp.config(command=helper4,bg=mt)
    lbl2.config(text="",bg=mt)
    limg.config(image="",bg=mt)
    s="This game contains 4 types of problem sets. Easy, Medium, Hard and Insane problem set. Each problem set increases the level of difficulty.\nYou have to choose the level and solve the puzzle. Your score will be calculated as you solve the puzzle early. So solve the puzzle as soon as possible.\nYou can pause the game when you want.You can also see the solved answer when you want by clicking \"hint\" button."
    lb.config(text=s,bg=mt)
    btnn.config(state=DISABLED,bg=mt)
    
def helper4():
    btnp.config(command=helper3)
    lbl2.config(text="RuleNo. 4: Use Process of Elimiation",bg=mt,fg=fg)
    limg.config(image=fotu8,bg=mt,fg=fg)
    s="What do we mean by using “process of elimination” to play Sudoku? Here is an example. In this Sudoku grid (shown below), the far left-hand vertical column (circled in Blue) is missing only a few numbers: 1, 5 and 6.\nOne way to figure out which numbers can go in each space is to use “process of elimination” by checking to see which other numbers are already included within each square – since there can be no duplication of numbers 1-9 within each square (or row or column)."
    lb.config(text=s,bg=mt,fg=fg)
    btnn.config(command=helper5,state=NORMAL,bg=mt,fg=fg)

def helper3():
    btnp.config(command=helper2)
    lbl2.config(text="RuleNo. 3: Don't Guess",bg=mt,fg=fg)
    s="Sudoku is a game of logic and reasoning, so you shouldn’t have to guess. If you don’t know what number to put in a certain space, keep scanning the other areas of the grid until you seen an opportunity to place a number. But don’t try to “force” anything – Sudoku rewards patience, insights, and recognition of patterns, not blind luck or guessing."
    lb.config(text=s)
    btnn.config(command=helper4,bg=mt,fg=fg)
    
    
def helper2():
    btnp.config(state=NORMAL,command=helper1)
    lbl2.config(text="RuleNo. 2: Don't Repeat Any Numbers",bg=mt,fg=fg)
    limg.config(image=fotu7,bg=mt,fg=fg)
    s="As you can see, in the upper left square (circled in blue), this square already has 7 out of the 9 spaces filled in. The only numbers missing from the square are 5 and 6. By seeing which numbers are missing from each square, row, or column, we can use process of elimination and deductive reasoning to decide which numbers need to go in each blank space."
    lb.config(text=s,bg=mt,fg=fg)
    btnn.config(command=helper3,bg=mt,fg=fg)
def helper1():
    btnp.config(state=DISABLED)
    lbl2.config(text="RuleNo. 1: Use Numbers 1-9",font=("helvetica",16,"bold"),bg=mt,fg=fg)
    lbl2.place(x=50,y=150)
    s = "Sudoku is played on a grid of 9 x 9 spaces. Within the rows and columns are 9 “squares” (made up of 3 x 3 spaces). Each row, column and square (9 spaces each) needs to be filled out with the numbers 1-9, without repeating any numbers within the row, column or square. Does it sound complicated? As you can see from the image below of an actual Sudoku grid, each Sudoku grid comes with a few spaces already filled in; the more spaces filled in, the easier the game – the more difficult Sudoku puzzles have very few spaces that are already filled in."
    lb.config(text=s,wraplength=500,bg=mt,fg=fg)
    limg.config(image=fotu4,bg=mt,fg=fg)
    btnn.config(command=helper2,bg=mt,fg=fg)

def refresh():
    global btnn,btnp,limg,lb,big
    lblim.destroy()
    l1o8.destroy()
    l2u9.destroy()
    big=Label(root,bg=mt,fg=fg,text="How to play Sudoku?",font = ("helvetica",20,"bold"))
    big.place(x=160,y=110)
    btn.place(x=265,y=660)
    btn3.place(x=265,y=740)
    btn2.destroy()
    btnn = Button(root,image=fotu6,borderwidth=0,bg=mt,activebackground=mt)
    btnn.place(x=430,y=660)
    btnp = Button(root,image=fotu5,borderwidth=0,bg=mt,activebackground=mt)
    btnp.place(x=100,y=660)
    limg =Label(root)
    limg.place(x=215,y=470)
    lb = Label(root,font=("helvetica",15))
    lb.place(x=50,y=190)
    helper1()

def first():
    global btn,btn2,btn3,lbl2,lblim,tip,converted,counter,result
    result = False
    converted="00:00:00"
    counter=66600
    for i in root.winfo_children():
        if i!=lbl11:
            i.destroy()
    lblim = Label(image=fotu,bg=mt)
    lblim.image=fotu
    lblim.place(x=220,y=160)
    lbl2 = Label(root,bg=mt,fg="grey10",text="Sudoku is considered highly addictive\nbut since there are no harmful side effects\ngo right ahead and get addicted!",font=("Broadway",18))
    lbl2.place(x=70,y=400)
    # lbl2 = Label(root,bg="grey20",fg="white",text=" "*0,font=("helvetica",18,"bold"))
    # lbl2.place(x=160,y=580)
    btn = Button(root,image=fotu1,bg=mt,borderwidth=0,command=second,activebackground=mt)
    btn.place(x=170,y=520)
    btn2 = Button(root,image=fotu2,bg=mt,borderwidth=0,command =refresh,activebackground=mt)
    btn2.place(x=270,y=515)
    btn3 = Button(root,image=fotu3,bg=mt,borderwidth=0,command = root.destroy,activebackground=mt)
    btn3.place(x=370,y=520)
    global  l1o8
    global l2u9
    l1o8 = Label(root,image=tr1,font=("Broadway",60,"bold","underline"),bg=mt,fg=fg,bd=0,relief=FLAT,highlightthickness=0,justify="right")
    l1o8.place(x=18,y=640)
    l2u9=Label(root,text="Powered  by  H.R.J.",font=("helvetica",11,'bold'),bg=root.cget("bg"),fg="grey12")
    l2u9.place(x=110,y=680)   
    

def main():
    global root,l1,l2,fotu,fotu1,fotu2,fotu3,fotu4,fotu5,fotu6,fotu7,fotu8,fotu9,mt,fg,tr1,fotu10,fotu11
    root = Tk()
    mt="#9b586c"
    fg="#241518"
    root.config(bg=mt)
    root.title("Sudoku")
    root.geometry("600x800+450+10")
    #root.iconbitmap("sudoku_logo1.ico")
    tr=ImageTk.PhotoImage(file="Images/sudoku_logo.png")
    tr1=ImageTk.PhotoImage(file="Images/sudoku_logo1.png")
    img = Image.open("Images/sudoku.png")
    rimg = img.resize((176,176))
    fotu = ImageTk.PhotoImage(rimg)
    #fotu = PhotoImage(file="C:\\Users\\HARSH JAISWAL\\Downloads\\25623-4-play-button-transparent-background-thumb.png")
    img1 = Image.open("Buttons/round_play_circle_black_36dp.png")
    rimg1 = img1.resize((60,60))
    fotu1 = ImageTk.PhotoImage(rimg1)
    img2 = Image.open("Buttons/round_not_listed_location_black_36dp.png")
    rimg2 = img2.resize((70,70))
    fotu2 = ImageTk.PhotoImage(rimg2)
    img3 = Image.open("Buttons/round_cancel_black_36dp.png")
    rimg3 = img3.resize((60,60))
    fotu3 = ImageTk.PhotoImage(rimg3)
    img4 = Image.open("Images/640px-Sudoku_Puzzle_by_L2G-20050714_standardized_layout.svg.png")
    rimg4 = img4.resize((150,150))
    fotu4 = ImageTk.PhotoImage(rimg4)
    img5 = Image.open("Buttons/next - Copy.png")
    rimg5 = img5.resize((60,60))
    fotu5 = ImageTk.PhotoImage(rimg5)
    img6 = Image.open("Buttons/next.png")
    rimg6 = img6.resize((60,60))
    fotu6 = ImageTk.PhotoImage(rimg6)
    img7 = Image.open("Images/Sudoku-Rules-for-Complete-Beginners-1.png")
    rimg7 = img7.resize((150,150))
    fotu7 = ImageTk.PhotoImage(rimg7)
    img8 = Image.open("Images/Sudoku-Rules-for-Complete-Beginners-2.png")
    rimg8 = img8.resize((150,150))
    fotu8 = ImageTk.PhotoImage(rimg8)
    img9 = Image.open("Buttons/outline_pause_circle_filled_black_24dp.png")
    rimg9 = img9.resize((60,60))
    fotu9 = ImageTk.PhotoImage(rimg9)
    img10 = Image.open("Buttons/baseline_info_black_24dp.png")
    rimg10 = img10.resize((60,60))
    fotu10 = ImageTk.PhotoImage(rimg10)
    img11 = Image.open("Buttons/baseline_arrow_circle_right_black_24dp.png")
    rimg11 = img11.resize((60,60))
    fotu11 = ImageTk.PhotoImage(rimg11)
    l15 = Label(root,image=tr,font=("Broadway",60,"bold","underline"),bg=mt,fg=fg,bd=0,relief=FLAT,highlightthickness=0)
    l15.place(x=160,y=220)
    root.update()
    import time
    time.sleep(2)
    l15.destroy()
    root.bind('<KeyPress>',warn)
    root.title("Sudoku")
    root.iconbitmap("Images/sudoku_logo1.ico")
    global lbl11,l29,l18
    import time
    lbl11 = Label(root,text="Sudoku",font=("Broadway",60,"bold","underline"),bg=mt,fg=fg)
    time.sleep(0.2)
    for i in range(350,15,-1):
        #lbl11.config(font=("broadway",i,"bold","underline"),justify=CENTER)
        lbl11.place(x=150,y=i)
        root.update()
    l18 = Label(root,image=tr1,font=("Broadway",60,"bold","underline"),bg=mt,fg=fg,bd=0,relief=FLAT,highlightthickness=0,justify="right")
    l18.place(x=18,y=640)
    l29=Label(root,text="Powered  by  H.R.J.",font=("helvetica",11,'bold'),bg=root.cget("bg"),fg="grey12")
    l29.place(x=110,y=680)   
    root.update()
    first()
    root.mainloop()
    
main()
