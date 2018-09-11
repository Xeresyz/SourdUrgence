#Breakthrough (deux joueurs)

def newBoard():
    n=0
    while n<4:
        n = eval(input("Entrez le nombre de lignes souhaitées, celui-ci ne pouvant être inférieur à 4: "))
    p=0
    while p<1:
        p = eval(input("Entrez le nombre de colonnes souhaitées, celui-ci ne pouvant être inférieur à 1: "))
    board=[[0]*p for _ in range(n)]
    i=0
    while i<2:
        for j in range(0,p):
            board[i][j]=1
        i+=1
    i=n-2
    while i<n:
        for j in range(0,p):
            board[i][j]=2
        i+=1
    return board,n,p

def display(board,n,p):
    y=0
    x=0
    print("\n")
    for i in range(0,n):
        for j in range(0,p):
            if board[i][j]==1:
                print("x",end="")
                y+=1
            if y==p:
                print("")
                y=0
            if board[i][j]==0:
                print(".",end="")
                y+=1
            if y==p:
                print("")
                y=0
            if board[i][j]==2:
                print("o",end="")
                y+=1
                x+=1
            if y==p:
                print("")
                y=0
    print("\n")
    return x

def selectPawn(board,n,p,player):
    if player==1:
        print("~Tour Joueur 1~\n")
        x=n-1
        y=p-1
        while x<0 or y<0 or x==n or y==p or board[x][y]!=1:
            x=eval(input("Entrez la ligne du pion que vous voulez déplacer: "))
            y=eval(input("Entrez la colonne du pion que vous voulez déplacer: "))
            x-=1
            y-=1
        return x,y

    if player==2:
        print("~Tour Joueur 2~\n")
        x=0
        y=0
        while x<0 or y<0 or x==n or y==p or board[x][y]!=2:
            x=eval(input("Entrez la ligne du pion que vous voulez déplacer: "))
            y=eval(input("Entrez la colonne du pion que vous voulez déplacer: "))
            x-=1
            y-=1
        return x,y

def where(board,n,p,player,i,j):
    if player==1:
        a=0
        while board[i][j]==1:
            y=eval(input("Entrez la colonne où vous souhaitez déplacer le pion: "))
            y-=1
            if board[i+1][y]!=1 and y>j-2 and y<j+2:
                board[i+1][y]=1
                board[i][j]=0
            elif y>j+2 or y<j-2:
                print("Le pion ne peut être déplacé à cet emplacement")
            else:
                print("Déplacement impossible")
                a+=1
            if a==3:
                return 5
        return board
    
    if player==2:
        a=0
        while board[i][j]==2:
            y=eval(input("Entrez la colonne où vous souhaitez déplacer le pion: "))
            y-=1
            if board[i-1][y]!=2 and y>j-2 and y<j+2:
                board[i-1][y]=2
                board[i][j]=0
            elif y>j+2 or y<j-2:
                print("Le pion ne peut être déplacé à cet emplacement")
            else:
                print("Déplacement impossible")
                a+=1
            if a==3:
                return 5
        return board

    if player==3:
        a=0
        while board[i][j]==2:
            if j==0:
                y=random.randrange(0,1)
            elif j==5:
                y=random.randrange(-1,0)
            else:
                y=random.randrange(-1,1)
            if board[i-1][j+y]!=2:
                board[i-1][j+y]=2
                board[i][j]=0
            else:
                a+=1
            if a==3:
                return 5
        return board
        

def breakthrough():
    print("Initialisation programme Breakthrough (deux joueurs)...")
    board,n,p = newBoard()
    player=1
    z=0
    test=[[0]*p for _ in range(n)]
    print("Voici le plateau de jeu créé.")
    while z!=1 and z!=2:
        display(board,n,p)
        i,j=selectPawn(board,n,p,player)
        test=where(board,n,p,player,i,j)
        if test==5:
            print("Vous avez choisi un pion indéplaçable. Veuillez en choisir un nouveau.\n")
        elif player==1:
            player+=1
            board=test
        else:
            player-=1
            board=test
        for r in range(0,p):
            if board[0][r]==2:
                z=2
                break
            if board[n-1][r]==1:
                z=1
                break
    if z==1:
        print("Le Joueur 1 a gagné!")
    else:
        print("Le Joueur 2 a gagné!")

#Breakthrough(un joueur)

import random

def WhoStart():
    player = 0
    while player!=1 and player!=3:
        player = eval(input("Voulez vous commencer(1)ou laisser l'ordinateur commencer(3)? "))
    return player

def selectOrdi(x,board,n,p):
        selected=random.randrange(1,x)
        y=0
        for i in range(0,n):
            for j in range(0,p):
                if board[i][j]==2:
                    y+=1
                    if y==selected:
                        return i,j

def breakthrough2():
    print("Initialisation programme Breakthrough(un joueur)...")
    board,n,p = newBoard()
    player=WhoStart()
    z=0
    b=0
    test=[[0]*p for _ in range(n)]
    print("Voici le plateau de jeu créé.")
    while z!=1 and z!=3:
        x=display(board,n,p)
        if player==1:
            i,j=selectPawn(board,n,p,player)
            test=where(board,n,p,player,i,j)
            if test==5:
                print("Vous avez choisi un pion indéplaçable. Veuillez en choisir un nouveau.\n")
            else:
                player+=2
                board=test
                display(board,n,p)
                
        if player==3:
            test=5
            while test==5:
                i,j=selectOrdi(x,board,n,p)
                test=where(board,n,p,player,i,j)
                if test==5:
                    print("Veuillez patienter, l'ordi cherche un pion à déplaçer...\n")
                    b=x
            player-=2
            board=test    
        for r in range(0,p):
            if board[0][r]==2:
                z=3
                break
            if board[n-1][r]==1:
                z=1
                break
    if z==1:
        print("Le Joueur Humain a gagné!")
    else:
        print("L'ordi a gagné!")

NbP=eval(input("Allez-vous jouer à 2 (1) ou seul contre un ordi (2) ? "))
if NbP==1:
    breakthrough()
if NbP==2:
    breakthrough2()
