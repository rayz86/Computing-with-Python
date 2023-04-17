# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 23:06:16 2022

@author: rayyan
"""
import random

movies=['insidious','initial d','avengers','dangal','shang chi','the box','tarzan']
def create_question(movie):
    n=len(movie)
    letters=list(movie)
    temp=[]
    for i in range(n):
        if letters[i]==' ':
            temp.append(' ')
        else:
            temp.append('*')
    qn=' '.join(str(x) for x in temp)
    return qn

def is_present(letters,movie):
    c=movie.count(letters)
    if c==0:
        return False
    else:
        return True

def unlock(qn,movie,letters):
    ref=list(movie)
    qn_list=list(qn)
    temp=[]
    n=len(movie)
    for i in range(n):
        if ref[i]==' ' or ref[i]==letters:
            temp.append(ref[i])
        else:
           if qn_list[i]=='*':
               temp.append('*')
           else:
               temp.append(ref[i])
    qn_new=' '.join(str(x) for x in temp)
    return qn_new

    
def play():
    p1name=input('player 1 pls input name')
    p2name=input('player 2 pls input name')
    pp1=0
    pp2=0
    turn=0
    willing=True
    while willing:
        if turn%2==0:
            #player 1
            print(p1name,'your turn')
            picked_movie=random.choice(movies)
            qn=create_question(picked_movie)
            print (qn)
            modified_qn=qn
            not_said=True
            while not_said:
                letters=input('your letter:')
                if (is_present,picked_movie):
                    #unlock
                    modified_qn=unlock(modified_qn,picked_movie,letters)
                    print (modified_qn)
                    d=input('press 1 to guess the movie or 2 to unlock another letter')
                    if d==1:
                        ans=input('your answer:')
                        if ans==picked_movie:
                            pp1=pp1+1
                            print('correct')
                            not_said=False
                            print(p1name,'your score:',pp1)
                        else:
                            print('WRONG ANSWER, try unlocking more characters')
                            
                    else:
                        print(letters,'not found')
                c=input('press 1 to continue or 0 to quit')
                if c==0:
                    print(p1name,'your score',pp1)
                    print(p2name,'your score',pp2)
                    willing=False
        else:
            #player 2
            print(p2name,'your turn')
            picked_movie=random.choice(movies)
            qn=create_question(picked_movie)
            print (qn)
            modified_qn=qn
            not_said=True
            while not_said:
                letters=input('your letter:')
                if (is_present,picked_movie):
                    #unlock
                    modified_qn=unlock(modified_qn,picked_movie,letters)
                    print (modified_qn)
                    d=input('press 1 to guess the movie or 2 to unlock another letter')
                    if d==1:
                        ans=input('your answer:')
                        if ans==picked_movie:
                            pp2=pp2+1
                            print('correct')
                            not_said=False
                            print(p2name,'your score:',pp2)
                        else:
                            print('WRONG ANSWER, try unlocking more characters')
                            
                    else:
                        print(letters,'not found')
                c=input('press 1 to continue or 0 to quit')
                if c==0:
                    print(p1name,'your score',pp1)
                    print(p2name,'your score',pp2)
                    willing=False
        turn=turn+1

        
play()

            
            