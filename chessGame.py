#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 13:48:57 2022

@author: alexandrew
"""

import chess
import time

score = {"r":-5, "R":5, "n":-3, "N":3, "b":-3, "B":3, "q":-10, "Q":10, "p":-1, "P":1, "k":-900, "K":900}
#board = chess.Board()
board = chess.Board("4r1k1/1b2rppp/p2p2n1/1ppP4/1P1R1P2/N1PB4/P5PP/5RK1 w - c6")

def get_move():
    """
    Retourne l'objet Move du module chess correspondant au coup légal associé l'input donné

    Returns
    -------
    move : Move du module chess
        le coup légal.

    """
    coup = input("Donnez le coup à jouer (ex: d6a4): ")
    try:
        move = chess.Move.from_uci(coup)
    except:
        move = get_move()
    return move

def launch_gameHumans():
    """
    Lance la partie d'echec en humain contre humain'

    Returns
    -------
    None.

    """

    while not board.is_game_over():
        itsWhiteTurn = True
        print("Tour des " + ("blancs" if itsWhiteTurn else "noires"))
        
        move = get_move()
        while(move not in board.legal_moves):
            print("Coup illégal")
            move = get_move()
        board.push(move)
        chess.svg.board(board, size=350)
        itsWhiteTurn = not itsWhiteTurn
        
    print("Victoire des " + ("blancs" if not itsWhiteTurn else "noires"))
    
def evaluateScore(board):
    return sum(score.get(c,0) for c in board.fen().split(" ")[0])

def minimax(board,depth,maximizingPlayer):
    if depth == 0:
        return evaluateScore(board)
    if maximizingPlayer:
        value = -float("inf")
        for move in board.legal_moves:
            board.push(move)
            value = max(value, minimax(board,depth-1, False))
            board.pop()
    else:
        value = float("inf")
        for move in board.legal_moves:
            board.push(move)
            value = min(value, minimax(board,depth-1, True))
            board.pop()
    return value
    
def minimaxPruned(board,depth,maximizingPlayer,alpha,beta):
    if depth == 0:
        return evaluateScore(board)
    if maximizingPlayer:
        value = -float("inf")
        for move in board.legal_moves:
            board.push(move)
            value = max(value, minimaxPruned(board,depth-1, False,alpha,beta))
            board.pop()
            if value >= beta:
                return value
            alpha = max(alpha,value)

    else:
        value = float("inf")
        for move in board.legal_moves:
            board.push(move)
            value = min(value, minimaxPruned(board,depth-1, True,alpha,beta))
            board.pop()
            if alpha >= value:
                return value
            beta = min(beta,value)
    
    return value

timeS = time.time()
minimax(board,3,True)
timeE = time.time()-timeS
print(timeE)

timeS = time.time()
minimaxPruned(board,3,True,-float("inf"),float("inf"))
timeE = time.time()-timeS
print(timeE)
    
#launch_gameHumans()
    
    
    
    