cc=0
def playermove():   #TO READ PLAYERS MOVE
    run=True
    while(run):
        move=input("ENTER A POSITION TO PLACE  'X' IN POSITION (1-9) ")
        try:
            move=int(move)     #STRING ENTER HONE PR ERROR NAHI AAYE ISILIYE
            if move>0 and move<10:
                if(issapcefree(move)):  #TO CHECK SPACE IS FREE OR NOT AT THAT POSITION
                    insert('X',move)    #TO INSERT THE CHARACTER(X)
                    run=False
                else:
                    print("THIS POSITION IS ALREADY OCCUPIED")
            else:
                print("ENTER THE POSITION IN RANGE (1-9)")
        except:
            print("PLEASE TYPE A NUMBER")
def osmove():
    PossibleMove=[x for x,letter in enumerate(brd) if letter ==' ' and x!=0]
    """for x,letter in enumerate(brd):
            if letter== " " and x!=0:
                possiblemoves=x"""
    move=0
    global cc
   # print("global cc  ",cc)
    for Letter in ['O','X']:
        for i in PossibleMove:
            brdcopy=brd[:]
            brdcopy[i]=Letter
            if iswinner(brdcopy,Letter) and cc<2:
                cc+=1
               # print("cc  ",cc)
                move=i
                return move
    cornersmove=[]
    for i in PossibleMove:
        if i in [1,3,7,9]:
            cornersmove.append(i)
    if len(cornersmove)>0:
        move=rand(cornersmove)
        return move
    if 5 in PossibleMove:
        move=5
        return move
    edgesmove = []
    for i in PossibleMove:
        if i in [2, 4, 6, 8]:
            edgesmove.append(i)
    if len(edgesmove) > 0:
        move = rand(edgesmove)
        return move
    return move

def rand(li):
    import random
    ln=len(li)
    r=random.randrange(0,ln)
    return li[r]
def insert(chr,pos):
    brd[pos]=chr

def isboardfull():
    for i in range(1,10):
        if(brd[i]==" "):
            return  True
    else:
        return False
def iswinner(brd,element):
    if ((brd[1]==element and brd[2]==element and brd[3]==element) or
    (brd[4]==element and brd[5]==element and brd[6]==element) or
    (brd[7]==element and brd[8]==element and brd[9]==element) or
    (brd[1]==element and brd[4]==element and brd[7]==element) or
    (brd[2]==element and brd[5]==element and brd[8]==element) or
    (brd[3]==element and brd[6]==element and brd[9]==element) or
    (brd[1]==element and brd[5]==element and brd[9]==element) or
    (brd[3]==element and brd[5]==element and brd[7]==element)):
        return True
    else:
        return False

def issapcefree(pos):
    return brd[pos]==" "

def printboard():

    print("     |       |      ")
    print(("   {} |   {}   |   {} ").format(brd[1],brd[2],brd[3]))
    print("     |       |      ")
    print("--------------------")
    print("     |       |      ")
    print(("   {} |   {}   |   {} ").format(brd[4], brd[5], brd[6]))
    print("     |       |      ")
    print("--------------------")
    print("     |       |      ")
    print(("   {} |   {}   |   {} ").format(brd[7], brd[8], brd[9]))
    print("     |       |      ")
while(1):
    if __name__=="__main__":

        cc=0
        brd = [' ' for x in range(10)]
        print("WELCOME TO TIC TAC TOE")
        printboard()
        c=1
        while (isboardfull() and c):
            if not(iswinner(brd,"O")):
                playermove()
                printboard()
            else:
                print("BETTER LUCK!NEXT TIME ......YOU LOSS ")
                c=0
                break
            if not(iswinner(brd,"X")):
                move=osmove()
                if move==0:
                    print("TIE GAME")
                    break
                else:
                    insert('O',move)
                    print("COMPUTER IS PLACED AN 'O' AT POSITION  ",move)
                    printboard()
            else:
                print("CONGRATS!! YOU WON")
                c=0
                break
        if not(isboardfull()) and c==1:
            print("GAME IS TIED")
            CH=input("Press 'y' to continue")
            if(CH !='y' and CH!='Y'):

                break
        if c==0:
            CH = input("Press 'y' to continue")
            if (CH != 'y' and CH != 'Y'):
                break



