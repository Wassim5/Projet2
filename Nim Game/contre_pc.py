#!/usr/bin/env python
#coding=utf-8

import string
import random
import time
import sys

def print_rules():
    print '\n'
    time.sleep(0.1)
    print '\n'
    time.sleep(0.1)
    print '                 ___           ___    '
    time.sleep(0.1)
    print '    ___         /\__\         /\  \      '
    time.sleep(0.1)
    print '   /\__\       /:/ _/_        \:\  \    '
    time.sleep(0.1)
    print '  /:/__/      /:/ /\__\        \:\  \       '
    time.sleep(0.1)
    print ' /::\  \     /:/ /:/ _/_   ___  \:\  \    '
    time.sleep(0.1)
    print ' \/\:\  \   /:/_/:/ /\__\ /\  \  \:\__\  '
    time.sleep(0.1)
    print '    \:\  \  \:\/:/ /:/  / \:\  \ /:/  /  '
    time.sleep(0.1)
    print '     \:\__\  \::/_/:/  /   \:\  /:/  /  '
    time.sleep(0.1)
    print '     /:/  /   \:\/:/  /     \:\/:/  / '
    time.sleep(0.1)
    print '    /:/  /     \::/  /       \::/  /  '
    time.sleep(0.1)
    print '    \/__/       \/__/         \/__/   '
    time.sleep(0.1)
    print '                         ___      '
    time.sleep(0.1)
    print '          _____         /\__\       '
    time.sleep(0.1)
    print '         /::\  \       /:/ _/_    '
    time.sleep(0.1)
    print '        /:/\:\  \     /:/ /\__\   '
    time.sleep(0.1)
    print '       /:/  \:\__\   /:/ /:/ _/_  '
    time.sleep(0.1)
    print '      /:/__/ \:|__| /:/_/:/ /\__\ '
    time.sleep(0.1)
    print '      \:\  \ /:/  / \:\/:/ /:/  /'
    time.sleep(0.1)
    print '       \:\  /:/  /   \::/_/:/  / '
    time.sleep(0.1)
    print '        \:\/:/  /     \:\/:/  /  '
    time.sleep(0.1)
    print '         \::/  /       \::/  /    '
    time.sleep(0.1)
    print '          \/__/         \/__/     '
    time.sleep(0.1)
    print '                             '
    time.sleep(0.1)
    print '                              '
    time.sleep(0.1)
    print '      ___                       ___                   '
    time.sleep(0.5)
    print '     /\  \                     /\  \                                  '
    time.sleep(0.1)
    print '     \:\  \       ___         |::\  \                                '
    time.sleep(0.1)
    print '      \:\  \     /\__\        |:|:\  \                                '
    time.sleep(0.1)
    print '  _____\:\  \   /:/__/      __|:|\:\  \                               '
    time.sleep(0.1)
    print ' /::::::::\__\ /::\  \     /::::|_\:\__\                              '
    time.sleep(0.1)
    print ' \:\  \  \/__/ \/\:\  \__  \:\  \  \/__/          '
    time.sleep(0.5)
    print '  \:\  \          \:\/\__\  \:\  \                                    '
    time.sleep(0.1)
    print '   \:\  \          \::/  /   \:\  \                '
    time.sleep(0.5)
    print '    \:\__\         /:/  /     \:\__\                                 '
    time.sleep(0.1)
    print '     \/__/         \/__/       \/__/              '
    time.sleep(0.5)
    print("\nBienvenue dans le Jeu de NIM\n")
    time.sleep(0.5)
    print("L'objectif est de ne pas enlever la derniére pierre de la table\n")
    time.sleep(0.5)
    print("Chacun son tour, Vous pouvez enlevez le nombre que vous voulez d'un seul tas\n")
    time.sleep(0.5)
    print("Le jeu s'arete quand toutes les pierres sont enlevées!\n")
    time.sleep(0.5)
    print '\n'
    time.sleep(0.1)

def o_n_reponse(str):
    reponse_oui_valide = ['o','oui','bien sur!']
    if str.lower() in reponse_oui_valide:
        return True
    return False

def r_quit(str):
    reponse_q_valide = ['q','quitter','exit','stop']
    if str.lower() in reponse_q_valide:
        return True
    else:
        return False

def r_quit_routine():
    print "Quitter au milieu du jeu? OK."
    for x in range(0,10):
        time.sleep(0.5)
        sys.stdout.write('.')
        sys.stdout.flush()
    print '\nOn commence de nouveau\n'
    time.sleep(2)
    return True

def print_table(t,b_x):
    print "\nTable des Valeurs:",bin(b_x),b_x
    print "\n#--------------------------#\n"
    for x in range(0,len(t)):
        print 'Tas '+str(x)+':','0' * t[x],'('+str(t[x])+')'
    print "\n#--------------------------#"

def calc_table_xor(t):
    b_x = t[0]
    for x in range(0,len(t)):
        b_x = b_x ^ t[x]
    return b_x


def tour_ordi(t):
    mod_temp = -1
    temp = list(set(t))
    for x in temp:
        if t.count(x)%2 == 0:
            temp.remove(x)
    for x in range(0,len(temp)):
        temp_xor = 0
        for y in range(0,len(temp)):
            if temp[x] != temp[y]:
                temp_xor = temp_xor ^ temp[y]
        if temp_xor < temp[x]:
            mod_temp = temp[x]
            temp[x] = temp_xor
            break
        elif temp_xor == temp[x] and temp_xor != 0:
            mod_temp = temp[x]
            temp[x] = 0
            break
    if mod_temp != -1:
        sub = t[t.index(mod_temp)] - temp[x]
        x_temp = t.index(mod_temp)
        t[t.index(mod_temp)] = temp[x]
        x = x_temp
    else:
        for x in range(0,len(t)):
            if t[x] != 0:
                t[x] += -1
                sub = 1
                break
    return t, x, sub

def tour_joueur(table,quit):
    col = -1
    while int(col) < 0 or len(table) - 1 < int(col):
        col = raw_input("\nChoisissez un tas ")
        if not col.isdigit():
            if r_quit(str(col)):
                quit, loss = True, r_quit_routine()
                break
            else:
                print '\nSVP Choisissez un tas existant'
                col = -1
    if quit:
        return 0,0,quit
    count = 0
    while int(count) == 0 or table[int(col)] < int(count):
        count = raw_input("\nCombien de pierres voulez_vous enlevé de ce tas? ")
        if not count.isdigit():
            if r_quit(str(count)):
                quit, loss = True, r_quit_routine()
                break
            else:
                print '\nSVP Choisir un nombre'
                count = 0
    return col, count, quit

def jouer_nim(C_V_C,numero_joueur):
    quit, loss = False, False
    cols = random.randint(3,7)
    table = []
    for x in range(0,cols):
        table.append(random.randint(5,23))
    print_table(table,calc_table_xor(table))
    while sum(table) > 0:
        if C_V_C:
            table, col, count = tour_ordi(table)
            print "\nOrdinateur 1 a enlevé",count,"depuis le tas",col
            print_table(table,calc_table_xor(table))
            time.sleep(1)
            if sum(table) == 0:
                break
        else:
            if numero_joueur == 1:
                col, count, quit = tour_joueur(table,quit)
                table[int(col)] += -1 * int(count)
                if quit:
                    break
                if sum(table) == 0:
                    break
            else:
                table, rm_column, rm_count = tour_ordi(table)
                print "\nOrdinateur a enlevé",rm_count,"depuis le tas",rm_column
                print_table(table,calc_table_xor(table))
                if sum(table) == 0:
                    loss = True
                    break

        bit_xor = calc_table_xor(table)
        if C_V_C:
            table, rm_column, rm_count = tour_ordi(table)
            print "\nOrdinateur 2 a enlevé",rm_count,"depuis le tas",rm_column
            print_table(table,calc_table_xor(table))
            time.sleep(1)
            if sum(table) == 0:
                loss = True
                break
        else:
            if numero_joueur == 2:
                col, count, quit = tour_joueur(table,quit)
                table[int(col)] += -1 * int(count)
                if quit:
                    break
                if sum(table) == 0:
                    break
            else:
                table, rm_column, rm_count = tour_ordi(table)
                print "\nOrdinateur a enlevé",rm_count,"depuis le tas",rm_column
                print_table(table,calc_table_xor(table))
                if sum(table) == 0:
                    loss = True
                    break

    if (loss or quit) and not C_V_C:
        print '\nOh non! Vous avez perdu. Bonne chance pour la prochaine fois.'
        time.sleep(0.1)
        print '(Vous jouerez mieux)'
    elif not C_V_C:
        print "\nCool, vous avez gagné!"
    elif loss:
        print "\nOrdinateur 2 a gagné."
    else:
        print "\nOrdinateur 1 a gagné."

print_rules()
envie_de_jouer = o_n_reponse(raw_input("\nVoulez-vous jouer? (o = oui) "))
while envie_de_jouer:
    c_v_c = o_n_reponse(raw_input("\nOrdinateur v. Ordinateur? "))
    if c_v_c:
        jouer_nim(c_v_c,1)
    else:
        id =  0
        while id != 1 and id != 2:
            id = int(raw_input("\nJoueur(1) ou Joueur(2)? "))
        jouer_nim(c_v_c,id)
enviee_de_jouer = o_n_reponse(raw_input("\nVoulez-vous jouer encore une fois? "))
