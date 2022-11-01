# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 15:23:32 2022

@author: USER
"""

Paises = ["Brazil","Peru","Alemania","Mexico","Canada"]
print(f"Lista Organizada:\n{Paises}")

Paises.sort() #Metodo
sorted_Paises = sorted(Paises) #Función

print(f"\nLista organizada metodo sort:\n{Paises}") #Imprimir con el metodo
print(f"\nLista organizada metodo sorted:\n{sorted_Paises}")


Paises.sort(reverse = True) #Metodo
sorted_Paises = sorted(Paises, reverse = True) #Funcion

print(f"\nLista organizada metodo sort inverso:\n{Paises}") #Imprimir con el metodo
print(f"\nLista organizada metodo sorted inverso:\n{sorted_Paises}") #Imprimir con la funcion



print("\nMetodo REVERSE()")

Paises1 = ["Brazil","Peru","Alemania","Mexico","Canada"]
print(f"\nLista organizada Orginal:\n{Paises1}")

Paises1.reverse()
print(f"\nLista organizada metodo reverse:\n{Paises1}")

Paises1.reverse()
print(f"\nLista organizada metodo reverse de nuevo a la lista ya transformada:\n{Paises1}")