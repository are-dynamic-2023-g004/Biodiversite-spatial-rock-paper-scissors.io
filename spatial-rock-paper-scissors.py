"""Les paramètres modifiables se trouvent au début du code juste après les import"""

import numpy as np
import random as rand
import tkinter as tk
import time
import matplotlib.pyplot as plt


"""Choix de la valeur des paramètres (probabilité entre 0 et 1)"""
sigma=0.8     #probabilité de prédation
mu=0.6        #probabilité de reproduction
epsilon=0.2   #probabilité de mobilité/permutation

tm=80 #taille de la matrice

def gagne(a,b):
    if ((a-b==1) or (a-b==-nb_types+1))and(a!=-1 and b!=-1):
        return True
    else:
        return False
    
def predation(matr,i,j):
    res=[]
    if (i-1>=0) and (gagne(matr[i][j],matr[i-1][j])):
        res.append('g')
    if (j-1>=0) and (gagne(matr[i][j],matr[i][j-1])):
        res.append('b')
    if (i+1<len(matr)) and (gagne(matr[i][j],matr[i+1][j])):
        res.append('d')
    if (j+1<len(matr[0])) and (gagne(matr[i][j],matr[i][j+1])):
        res.append('h')
    return res

def reproduction(matr,i,j):
    res=[]
    if (i-1>=0) and matr[i-1][j]==-1:
        res.append('g')
    if (j-1>=0) and matr[i][j-1]==-1:
        res.append('b')
    if (i+1<len(matr)) and matr[i+1][j]==-1:
        res.append('d')
    if (j+1<len(matr[0])) and matr[i][j+1]==-1:
        res.append('h')
    return res

def permutation(matr,i,j):
    res=[]
    if (i-1>=0):
        res.append('g')
    if (j-1>=0):
        res.append('b')
    if (i+1<len(matr)):
        res.append('d')
    if (j+1<len(matr[0])):
        res.append('h')
    return res

def chgmt_mat(matr,sigma,mu,epsilon):
    m=np.zeros((len(matr),len(matr[0])))
    m=np.copy(matr)
    for i in range(len(matr)):
        for j in range(len(matr[0])):
            if rand.random()<=sigma:
                pred=predation(matr,i,j)
                if len(pred)!=0:
                    ch=rand.choice(pred)
                    if ch=='g':
                        m[i-1][j]=-1
                    if ch=='b':
                        m[i][j-1]=-1
                    if ch=='d':
                        m[i+1][j]=-1
                    if ch=='h':
                        m[i][j+1]=-1 
            if rand.random()<=mu:
                rep=reproduction(matr,i,j)
                if len(rep)!=0:
                    ch=rand.choice(rep)
                    if ch=='g':
                        m[i-1][j]=matr[i][j]
                    if ch=='b':
                        m[i][j-1]=matr[i][j]
                    if ch=='d':
                        m[i+1][j]=matr[i][j]
                    if ch=='h':
                        m[i][j+1]=matr[i][j]
            if rand.random()<=epsilon:
                perm=permutation(matr,i,j)
                if len(perm)!=0:
                    ch=rand.choice(perm)
                    if ch=='g':
                        aux=m[i][j]
                        m[i][j]=m[i-1][j]
                        m[i-1][j]=aux
                    if ch=='b':
                        aux=m[i][j]
                        m[i][j]=m[i][j-1]
                        m[i][j-1]=aux
                    if ch=='d':
                        aux=m[i][j]
                        m[i][j]=m[i+1][j]
                        m[i+1][j]=aux
                    if ch=='h':
                        aux=m[i][j]
                        m[i][j]=m[i][j+1]
                        m[i][j+1]=aux
    return m


"""Initialisation de la fenêtre"""
fenetre=tk.Tk()
fenetre.title("Pierre feuille ciseaux spatial")
tfx=800
tfy=800
fenetre.geometry(str(tfx)+"x"+str(tfy))
dessin=tk.Canvas(fenetre,width=tfx,height=tfy)
dessin.grid(row=0,column=0,columnspan=1,padx=0,pady=0)
echx=tfx/tm #calcul de l'échelle
echy=tfy/tm


"""Initialisation de la matrice"""
nb_types=3 #nombre d'espèces différentes (toujours à 3 dans notre étude mais on a tout de même 
           #généralisé notre algorithme pour pouvoir augmenter le nombre d'espèces)
           #le maximum prévu dans ce programme est 6
l=[i for i in range(nb_types)]
matr=[[rand.choice(l)for j in range(tm)]for k in range(tm)]


"""A chaque tour de boucle, la matrice est actualisée grace à notre fonction chgmt_mat et l'affichage est réalisé"""
for k in range(4000):
    for i in range(len(matr)):
        for j in range(len(matr[0])):
            if matr[i][j]==0:
                dessin.create_rectangle(i*echx,j*echy,i*echx+echx,j*echy+echy,fill='gold')
            elif matr[i][j]==1:
                dessin.create_rectangle(i*echx,j*echy,i*echx+echx,j*echy+echy,fill='red')
            elif matr[i][j]==2:
                dessin.create_rectangle(i*echx,j*echy,i*echx+echx,j*echy+echy,fill='blue')
            elif matr[i][j]==-1:
                dessin.create_rectangle(i*echx,j*echy,i*echx+echx,j*echy+echy,fill='white') 
            
            #lignes utiles uniquement si on augmente le nombre d'espèces
            elif matr[i][j]==3:
                dessin.create_rectangle(i*echx,j*echy,i*echx+echx,j*echy+echy,fill='green')
            elif matr[i][j]==4:
                dessin.create_rectangle(i*echx,j*echy,i*echx+echx,j*echy+echy,fill='orange')
            elif matr[i][j]==5:
                dessin.create_rectangle(i*echx,j*echy,i*echx+echx,j*echy+echy,fill='purple')
            
            
    fenetre.update()
    time.sleep(0.001)
    dessin.delete("all")
    matr=chgmt_mat(matr,sigma,mu,epsilon)
fenetre.mainloop()





"""FONCTIONS DE TESTS POUR OBTENIR NOS COURBES"""

def cpt_extinction_courbe1(deb,fin,pas,nb_iter,taille_echantillon,sigma,mu,tm):
    eps=deb
    axex=[]
    axey=[]
    while eps<=fin:
        lnb=[]
        matr=np.zeros((tm,tm))
        for j in range(taille_echantillon):
            test=False
            i=0
            matr=[[rand.choice(l)for x in range(len(matr))]for y in range(len(matr[0]))]
            while i<nb_iter and test==False :
                matr=chgmt_mat(matr,sigma,mu,eps)
                print('tour ',i,' it ',j,' pro ',eps)
                cpty=0
                cptr=0
                cptb=0
                for k in range(len(matr)):
                    for p in range(len(matr[0])):
                        if matr[k][p]==0:
                            cpty=cpty+1
                        elif matr[k][p]==1:
                            cptr=cptr+1
                        elif matr[k][p]==2:
                            cptb=cptb+1
                if cptr==0 or cpty==0 or cptb==0:
                    test=True
                i=i+1
            lnb.append(i)
        axex.append(eps)
        axey.append(np.mean(lnb))  
        eps+=pas
    plt.plot(axex,axey,'red')
    plt.xlabel('probabilite de mobilite (permutation)')
    plt.ylabel('nombre moyen de tours avant extinction')
    plt.show()
    return (axex,axey)

"""
cpt1=cpt_extinction_courbe1(0,1,0.1,5000,100,0.3,0.3,40)  
#instruction utilisée pour afficher notre première courbe, la fonction met plusieurs heures à s'exécuter
"""

def cpt_extinction_courbe2(deb,fin,pas,nb_iter,taille_echantillon,sigma,mu,tm):
    eps=deb
    axex=[]
    axey=[]
    while eps<=fin:
        cptE=0
        matr=np.zeros((tm,tm))
        for j in range(taille_echantillon):
            test=False
            i=0
            matr=[[rand.choice(l)for x in range(len(matr))]for y in range(len(matr[0]))]
            while i<nb_iter and test==False :
                matr=chgmt_mat(matr,sigma,mu,eps)
                print('tour ',i,' it ',j,' pro ',eps)
                cpty=0
                cptr=0
                cptb=0
                for k in range(len(matr)):
                    for p in range(len(matr[0])):
                        if matr[k][p]==0:
                            cpty=cpty+1
                        elif matr[k][p]==1:
                            cptr=cptr+1
                        elif matr[k][p]==2:
                            cptb=cptb+1
                if cptr==0 or cpty==0 or cptb==0:
                    test=True
                    cptE+=1;
                i=i+1
        axex.append(eps)
        axey.append(float(cptE)/taille_echantillon)
        eps+=pas
    plt.plot(axex,axey,'red')
    plt.xlabel('probabilite de mobilite (permutation)')
    plt.ylabel("proportion de cas d'extinction sur 100 tirages")
    plt.show()
    return (axex,axey)

"""
cpt2=cpt_extinction_courbe1(0,0.3,0.03,5000,100,0.3,0.3,40)  
#instruction utilisée pour afficher notre deuxième courbe, la fonction met plusieurs heures à s'exécuter
"""
