# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 14:08:53 2021

@author: Sławomir Jedziniak
"""

import numpy as np


#% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#% % % % % PRE - PROCESSING % % % % %

#%% 1(a) inicjalizacja parametrow sterujacych programem CZESC 1
[ parametry_sterujace ] = inicjalizacja_parametrow_sterujacych ( ... ) ;

c=0
f=0

x_0 = 0; x_p = 1
n=4

x_i=np.array([0,1,0.5,0.75])
iwp=np.array




# 1(b) definicja parametrow fizycznych i geometrycznych obszaru , warunkow brzegowych CZESC 1
# - definicja przedzialu ,
# - liczba wezlow / elementow modelu w przypadku dyskretyzacji jednorodnej
# - zadanie funkcji wymuszajacej , parametrow rownania rozniczkowego
# - ...

[ parametry_geom_i_fiz ] = definicja_parametrow_geom_i_fiz ( ... ) ;
#%% 1(b/c) CZESC 1
[ WEZLY , ELEMENTY , WAR_BRZEGOWE ] = definicja_zmiennych_przechowujacych_informacje_o_geometrii (
parametry_geom_i_fiz , ... )
#% - / ew. odczytanie geometrii z pliku





