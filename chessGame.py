#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 13:48:57 2022

@author: alexandrew
"""

import chess

def get_move():
    coup = input("Donnez le coup à jouer (ex: d6a4): ")
    try:
        move = chess.Move.from_uci(coup)
    except:
        move = get_move()
    return move

def launch_game():
    
    board = chess.Board()
    itsWhiteTurn = True

    while not board.is_game_over():
        print("Tour des " + ("blancs" if itsWhiteTurn else "noires"))
        
        move = get_move()
        while(move not in board.legal_moves):
            print("Coup illégal")
            move = get_move()
        board.push(move)
        print(board)
        itsWhiteRuen = not itsWhiteTurn
        
    print("Victoire des " + ("blancs" if itsWhiteTurn else "noires"))
    
launch_game()
    
    
    
    