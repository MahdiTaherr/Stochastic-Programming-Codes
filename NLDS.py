# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 19:49:16 2021

@author: mtaher
"""
import pulp
import numpy as np
from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable
# Define parameters
T1=[-1.25,-1.14]
T2=[-1.06,-1.12]
T_41=[1.25,1.14]
T_42=[1.06,1.12]
h1=0
h2=80
#Define variables
x1 = LpVariable.dicts("x",[(i,j) for i in range(1,3) for j in range(1,2)],cat='Continuous',lowBound=0)
x2 = LpVariable.dicts("x",[(i,j,k) for i in range(1,3) for j in range(2,3) for k in range(1,3)],cat='Continuous',lowBound=0)
x3 = LpVariable.dicts("x",[(i,j,k,l) for i in range(1,3) for j in range(3,4) for k in range(1,3) for l in range(1,3) ],cat='Continuous',lowBound=0)
y =  LpVariable.dicts("y",[(i,j,k) for i in range(1,3) for j in range(1,3) for k in range(1,3) ],cat='Continuous',lowBound=0)
w =  LpVariable.dicts("w",[(i,j,k) for i in range(1,3) for j in range(1,3) for k in range(1,3)] ,cat='Continuous',lowBound=0)
tetha1 = LpVariable.dicts("tetha1",[(i,j) for i in range(1,2) for j in range(1,2)],cat='Continuous',)
tetha2 = LpVariable.dicts("tetha2",[(i,j) for i in range(2,3) for j in range(1,3)],cat='Continuous',)
tetha3 = LpVariable.dicts("tetha3",[(i,j) for i in range(3,4) for j in range(1,5)],cat='Continuous',)
tetha4 = LpVariable.dicts("tetha4",[(i,j) for i in range(4,5) for j in range(1,9)],cat='Continuous',)

def NLDS_1(new_constraints=list()):
    model_1 =  LpProblem(name="NLDS(1)" , sense = 1)
    model_1 += tetha1[(1,1)]
    model_1 += x1[(1,1)]+x1[(2,1)]==55                      
    if len(new_constraints)>=1:
        for i in new_constraints:
            model_1 += i
    return model_1
                           
def NLDS_21(new_constraints,x):
    model_21 =  LpProblem(name="NLDS(2,1)" , sense = 1)
    model_21 += tetha2[(2,1)]                      
    model_21 += -1.25*x[0] -1.14*x[1]  + x2[(1,2,1)] + x2[(2,2,1)] ==0
    if len(new_constraints)>=1:
        for i in new_constraints:
            model_21 += i
    return model_21
                           
def NLDS_22(new_constraints, x):
    model_22 =  LpProblem(name="NLDS(2,2)" , sense = 1)
    model_22 += tetha2[(2,2)]                       
    model_22 += -1.06*x[0] -1.12*x[1]  + x2[(1,2,2)] + x2[(2,2,2)] ==0                     
    if len(new_constraints)>=1:
        for i in new_constraints:
            model_22 += i
    return model_22
                           
def NLDS_31(new_constraints, x):
    model_31 =  LpProblem(name="NLDS(3,1)" , sense = 1)
    model_31 += tetha3[(3,1)]                       
    model_31 += -1.25*x[0] -1.14*x[1]  + x3[(1,3,1,1)] + x3[(2,3,1,1)] ==0                       
    if len(new_constraints)>=1:
        for i in new_constraints:
            model_31 += i
    return model_31
                           
def NLDS_32(new_constraints, x):
    model_32 =  LpProblem(name="NLDS(3,2)" , sense = 1)
    model_32 += tetha3[(3,2)]                       
    model_32 += -1.06*x[0] -1.12*x[1]  + x3[(1,3,1,2)] + x3[(2,3,1,2)] ==0                       
    if len(new_constraints)>=1:
        for i in new_constraints:
            model_32 += i
    return model_32
                           
def NLDS_33(new_constraints, x):
    model_33 =  LpProblem(name="NLDS(3,3)" , sense = 1)
    model_33 += tetha3[(3,3)]
    model_33 += -1.25*x[0] -1.14*x[1]  + x3[(1,3,2,1)] + x3[(2,3,2,1)] ==0
    if len(new_constraints)>=1:
        for i in new_constraints:
            model_33 += i
    return model_33
                           
def NLDS_34(new_constraints, x):                      
    model_34 =  LpProblem(name="NLDS(3,4)" , sense = 1)
    model_34 += tetha3[(3,4)]
    model_34 += -1.06*x[0] -1.12*x[1]  + x3[(1,3,2,2)] + x3[(2,3,2,2)] ==0
    if len(new_constraints)>=1:
        for i in new_constraints:
            model_34 += i
    return model_34
                           
def NLDS_41(x):
    model_41 =  LpProblem(name="NLDS(4,1)" , sense = 1)
    model_41 += tetha4[(4,1)]+ (-y[(1,1,1)] + 4*w[(1,1,1)] )                
    model_41 += 1.25*x[0] +1.14*x[1]  - y[(1,1,1)] + w[(1,1,1)] ==80

    return model_41
                           
def NLDS_42(x):
    model_42 =  LpProblem(name="NLDS(4,2)" , sense = 1)
    model_42 += tetha4[(4,2)]+ (- y[(1,1,2)] + 4*w[(1,1,2)] )                
    model_42 += 1.06*x[0] + 1.12*x[1]  - y[(1,1,2)] + w[(1,1,2)] ==80
    return model_42
                           
def NLDS_43(x):
    model_43 =  LpProblem(name="NLDS(4,3)" , sense = 1)
    model_43 += tetha4[(4,3)]+ (-y[(1,2,1)] + 4*w[(1,2,1)] )                
    model_43 += 1.25*x[0] +1.14*x[1]  - y[(1,2,1)] + w[(1,2,1)] ==80                       

    return model_43
                           
def NLDS_44(x):
    model_44 =  LpProblem(name="NLDS(4,4)" , sense = 1)
    model_44 += tetha4[(4,4)]+ (-y[(1,2,2)] + 4*w[(1,2,2)] )               
    model_44 += 1.06*x[0] +1.12*x[1]  - y[(1,2,2)] + w[(1,2,2)] ==80                       
    return model_44
                           
def NLDS_45(x):
    model_45 =  LpProblem(name="NLDS(4,5)" , sense = 1)
    model_45 += tetha4[(4,5)]+ (-y[(2,1,1)] + 4*w[(2,1,1)] )               
    model_45 += 1.25*x[0] + 1.14*x[1]  - y[(2,1,1)] + w[(2,1,1)] ==80
    return model_45
                           
def NLDS_46(x):
    model_46 =  LpProblem(name="NLDS(4,6)" , sense = 1)
    model_46 += tetha4[(4,6)]+ (-y[(2,1,2)] + 4*w[(2,1,2)] )               
    model_46 += 1.06*x[0] +1.12*x[1]  - y[(2,1,2)] + w[(2,1,2)] ==80
    return model_46
                           
def NLDS_47(x):
    model_47 =  LpProblem(name="NLDS(4,7)" , sense = 1)
    model_47 += tetha4[(4,7)]+(- y[(2,2,1)] + 4*w[(2,2,1)] )                
    model_47 += 1.25*x[0] +1.14*x[1]  - y[(2,2,1)] + w[(2,2,1)] ==80
    return model_47                       
def NLDS_48(x):
    model_48 =  LpProblem(name="NLDS(4,8)" , sense = 1)
    model_48 += tetha4[(4,8)]+(-y[(2,2,2)] + 4*w[(2,2,2)] )                
    model_48 += 1.06*x[0] +1.12*x[1]  - y[(2,2,2)] + w[(2,2,2)] ==80
    return model_48
cuts_1=list()
cuts_21=list()
cuts_22=list()
cuts_31=list()
cuts_32=list()
cuts_33=list()
cuts_34=list()
cuts_41=list()
cuts_42=list()
cuts_43=list()
cuts_44=list()
cuts_45=list()
cuts_46=list()
cuts_47=list()
cuts_48=list()
ecuts_21=list()
ecuts_22=list()
ecuts_31=list()
ecuts_32=list()
ecuts_33=list()
ecuts_34=list()
I=0
Continue=True
while Continue:
    I=I+1
    print('Iteration ', I)
    print('DIR = FORWARD')
    nlds_1 = NLDS_1(cuts_1)
    if I==1:
        nlds_1 += tetha1[(1,1)]==0
    status= nlds_1.solve()
    x_1=list()
    for var in nlds_1.variables()[1:]:
        x_1.append(var.value())
    Tetha_1=nlds_1.variables()[0].value()
    print('NLDS1 solution is : ',x_1)                       
    nlds_21= NLDS_21(cuts_21, x_1)
    if I==1:
        nlds_21 += tetha2[(2,1)]==0
    status=nlds_21.solve()
    x_21=list()
    for var in nlds_21.variables()[1:]:
        x_21.append(var.value())
    Tetha_21=nlds_21.variables()[0].value()
    dual_21=list(nlds_21.constraints.items())[0][1].pi
    optimality_dual_21=list()
    if len(cuts_21)>0:                      
        for i in range(1,len(list(nlds_21.constraints.items()))):                    
            optimality_dual_21.append(list(nlds_21.constraints.items())[i][1].pi)
    else:
        optimality_dual_21=0                 
    print('NLDS21 solution is : ',x_21)
    
    nlds_22= NLDS_22(cuts_22, x_1)
    if I==1:
        nlds_22 += tetha2[(2,2)]==0
    status= nlds_22.solve()                     
    x_22=list()
    for var in nlds_22.variables()[1:]:
        x_22.append(var.value())
    Tetha_22=nlds_22.variables()[0].value()
    dual_22=list(nlds_22.constraints.items())[0][1].pi
    optimality_dual_22=list()
    if len(cuts_22)>0:                      
        for i in range(1,len(list(nlds_22.constraints.items()))):                    
            optimality_dual_22.append(list(nlds_22.constraints.items())[i][1].pi)
    else:
        optimality_dual_22=0
    print('NLDS22 solution is : ',x_22)
    
    nlds_31= NLDS_31(cuts_31, x_21)
    if I==1:
        nlds_31 += tetha3[(3,1)]==0
    status=nlds_31.solve()
    x_31=list()
    for var in nlds_31.variables()[1:]:
        x_31.append(var.value())
    Tetha_31=nlds_31.variables()[0].value()
    dual_31=list(nlds_31.constraints.items())[0][1].pi
    optimality_dual_31=list()
    if len(cuts_31)>0:                      
        for i in range(1,len(list(nlds_31.constraints.items()))):                    
            optimality_dual_31.append(list(nlds_31.constraints.items())[i][1].pi)
    else:
        optimality_dual_31=0
    print('NLDS31 solution is : ',x_31)
    
    nlds_32= NLDS_32(cuts_32, x_21)
    if I==1:
        nlds_32 += tetha3[(3,2)]==0
    status=nlds_32.solve()                      
    x_32=list()
    for var in nlds_32.variables()[1:]:
        x_32.append(var.value())
    Tetha_32=nlds_32.variables()[0].value()
    dual_32=list(nlds_32.constraints.items())[0][1].pi
    optimality_dual_32=list()
    if len(cuts_32)>0:                      
        for i in range(1,len(list(nlds_32.constraints.items()))):                    
            optimality_dual_32.append(list(nlds_32.constraints.items())[i][1].pi)
    else:
        optimality_dual_32=0
    print('NLDS32 solution is : ',x_32)
    
    nlds_33= NLDS_33(cuts_33, x_22)
    if I==1:
        nlds_33 += tetha3[(3,3)]==0
    status=nlds_33.solve()                      
    x_33=list()
    for var in nlds_33.variables()[1:]:
        x_33.append(var.value())
    Tetha_33=nlds_33.variables()[0].value()
    dual_33=list(nlds_33.constraints.items())[0][1].pi
    optimality_dual_33=list()
    if len(cuts_33)>0:                      
        for i in range(1,len(list(nlds_33.constraints.items()))):                    
            optimality_dual_33.append(list(nlds_33.constraints.items())[i][1].pi)
    else:
        optimality_dual_33=0
    print('NLDS33 solution is : ',x_33)
    
    nlds_34= NLDS_34(cuts_34, x_22)
    if I==1:
        nlds_34 += tetha3[(3,4)]==0
    status=nlds_34.solve()
    x_34=list()
    for var in nlds_34.variables()[1:]:
        x_34.append(var.value())
    Tetha_34=nlds_34.variables()[0].value()
    dual_34=list(nlds_34.constraints.items())[0][1].pi
    optimality_dual_34=list()
    if len(cuts_34)>0:                      
        for i in range(1,len(list(nlds_34.constraints.items()))):                    
            optimality_dual_34.append(list(nlds_34.constraints.items())[i][1].pi)
    else:
        optimality_dual_34=0 
    print('NLDS34 solution is : ',x_34)
    
    nlds_41= NLDS_41(x_31)
    nlds_41 += tetha4[(4,1)]==0
    status= nlds_41.solve()                 
    x_41=list()
    for var in nlds_41.variables()[1:]:
        x_41.append(var.value())
    Tetha_41=nlds_41.variables()[0].value()                      
    dual_41=list(nlds_41.constraints.items())[0][1].pi
    print('NLDS41 solution is : ',x_41)
    
    nlds_42= NLDS_42(x_31)
    nlds_42 += tetha4[(4,2)]==0
    status=nlds_42.solve()                 
    x_42=list()
    for var in nlds_42.variables()[1:]:
        x_42.append(var.value())
    Tetha_42=nlds_42.variables()[0].value()
    dual_42=list(nlds_42.constraints.items())[0][1].pi
    optimality_dual_42=list()
    if len(cuts_42)>0:                      
        for i in range(1,len(list(nlds_42.constraints.items()))):                    
            optimality_dual_42.append(list(nlds_42.constraints.items())[i][1].pi)
    else:
        optimality_dual_42=0
    print('NLDS42 solution is : ',x_42)
    
    nlds_43= NLDS_43(x_32)
    nlds_43 += tetha4[(4,3)]==0
    status=nlds_43.solve()                  
    x_43=list()
    for var in nlds_43.variables()[1:]:
        x_43.append(var.value())
    Tetha43=nlds_43.variables()[0].value()
    dual_43=list(nlds_43.constraints.items())[0][1].pi
    optimality_dual_43=list()
    if len(cuts_43)>0:                      
        for i in range(1,len(list(nlds_43.constraints.items()))):                    
            optimality_dual_43.append(list(nlds_43.constraints.items())[i][1].pi)
    else:
        optimality_dual_43=0
    print('NLDS43 solution is : ',x_43)
    
    nlds_44= NLDS_44(x_32)
    nlds_44 += tetha4[(4,4)]==0
    status=nlds_44.solve()                 
    x_44=list()
    for var in nlds_44.variables()[1:]:
        x_44.append(var.value())
    Tetha_44=nlds_44.variables()[0].value()                      
    dual_44=list(nlds_44.constraints.items())[0][1].pi
    optimality_dual_44=list()
    if len(cuts_44)>0:                      
        for i in range(1,len(list(nlds_44.constraints.items()))):                    
            optimality_dual_44.append(list(nlds_44.constraints.items())[i][1].pi)
    else:
        optimality_dual_44=0
    print('NLDS44 solution is : ',x_44)
    
    nlds_45= NLDS_45(x_33)
    nlds_45 += tetha4[(4,5)]==0                  
    status=nlds_45.solve()                 
    x_45=list()
    for var in nlds_45.variables()[1:]:
        x_45.append(var.value())
    Tetha45=nlds_45.variables()[0].value()
    dual_45=list(nlds_45.constraints.items())[0][1].pi
    optimality_dual_45=list()
    if len(cuts_45)>0:                      
        for i in range(1,len(list(nlds_45.constraints.items()))):                    
            optimality_dual_45.append(list(nlds_45.constraints.items())[i][1].pi)
    else:
        optimality_dual_45=0
    print('NLDS45 solution is : ',x_45)
    
    nlds_46= NLDS_46(x_33)
    nlds_46 += tetha4[(4,6)]==0                  
    status=nlds_46.solve()                 
    x_46=list()
    for var in nlds_46.variables()[1:]:
        x_46.append(var.value())
    Tetha_46=nlds_46.variables()[0].value()
    dual_46=list(nlds_46.constraints.items())[0][1].pi
    optimality_dual_46=list()
    if len(cuts_46)>0:                      
        for i in range(1,len(list(nlds_46.constraints.items()))):                    
            optimality_dual_46.append(list(nlds_46.constraints.items())[i][1].pi)
    else:
        optimality_dual_46=0
    print('NLDS46 solution is : ',x_46)
    
    nlds_47= NLDS_47(x_34)
    nlds_47 += tetha4[(4,7)]==0
    status=nlds_47.solve()
    x_47=list()
    for var in nlds_47.variables()[1:]:
        x_47.append(var.value())
    Tetha_47=nlds_47.variables()[0].value()
    dual_47=list(nlds_47.constraints.items())[0][1].pi
    optimality_dual_47=list()
    if len(cuts_47)>0:                      
        for i in range(1,len(list(nlds_47.constraints.items()))):                    
            optimality_dual_47.append(list(nlds_47.constraints.items())[i][1].pi)
    else:
        optimality_dual_47=0
    print('NLDS47 solution is : ',x_47)
    
    nlds_48= NLDS_48(x_34)
    nlds_48 += tetha4[(4,8)]==0
    status=nlds_48.solve()              
    x_48=list()
    for var in nlds_48.variables()[1:]:
        x_48.append(var.value())
    Tetha_48=nlds_48.variables()[0].value()
    dual_48=list(nlds_48.constraints.items())[0][1].pi
    optimality_dual_48=list()
    if len(cuts_48)>0:                      
        for i in range(1,len(list(nlds_48.constraints.items()))):                    
            optimality_dual_48.append(list(nlds_48.constraints.items())[i][1].pi)
    else:
        optimality_dual_48=0
    print('NLDS48 solution is : ',x_48)
    print('DIR = BACKWARD')
    print('----------------------------')
    E_31=list(0.5 * (np.matmul([dual_41],[T_41]) + np.matmul([dual_42],[T_42])))  
    e_31= 0.5 * (np.matmul([dual_41],[h2]) + np.matmul([dual_42],[h2]))
    E_32=list(0.5 * (np.matmul([dual_43],[T_41]) + np.matmul([dual_44],[T_42])))                                                                              
    e_32= 0.5 * (np.matmul([dual_43],[h2]) + np.matmul([dual_44],[h2]))
    E_33=list(0.5 * (np.matmul([dual_45],[T_41]) + np.matmul([dual_46],[T_42])))                                                                               
    e_33=0.5 * (np.matmul([dual_45],[h2]) + np.matmul([dual_46],[h2]))
    E_34=list(0.5 * (np.matmul([dual_47],[T_41]) + np.matmul([dual_48],[T_42])))                                                                               
    e_34= 0.5 * (np.matmul([dual_47],[h2]) + np.matmul([dual_48],[h2]))
    if I==1:
        a=nlds_31.constraints.pop('_C2')
        a=nlds_32.constraints.pop('_C2')
        a=nlds_33.constraints.pop('_C2')
        a=nlds_34.constraints.pop('_C2')
        cuts_31.append( E_31[0] * x3[(1,3,1,1)] +E_31[1] * x3[(2,3,1,1)] +tetha3[(3,1)] >= e_31 )
        print('the cut : ', E_31[0] * x3[(1,3,1,1)] +E_31[1] * x3[(2,3,1,1)] +tetha3[(3,1)] >= e_31 , "   is added to nlds31")
        cuts_32.append( E_32[0] * x3[(1,3,1,2)] +E_32[1] * x3[(2,3,1,2)] +tetha3[(3,2)] >= e_32 )
        print('the cut : ', E_32[0] * x3[(1,3,1,2)] +E_32[1] * x3[(2,3,1,2)] +tetha3[(3,2)] >= e_32 , "   is added to nlds32")
        cuts_33.append( E_33[0] * x3[(1,3,2,1)] +E_33[1] * x3[(2,3,2,1)] +tetha3[(3,3)] >= e_33 )
        print('the cut : ', E_33[0] * x3[(1,3,2,1)] +E_33[1] * x3[(2,3,2,1)] +tetha3[(3,3)] >= e_33, "   is added to nlds33")
        cuts_34.append( E_34[0] * x3[(1,3,2,2)] +E_34[1] * x3[(2,3,2,2)] +tetha3[(3,4)] >= e_34 )
        print('the cut : ', E_34[0] * x3[(1,3,2,2)] +E_34[1] * x3[(2,3,2,2)] +tetha3[(3,4)] >= e_34 , "   is added to nlds34")
        ecuts_31.append(e_31)
        ecuts_32.append(e_32)
        ecuts_33.append(e_33)
        ecuts_34.append(e_34)
    else:
        if e_31 - (E_31[0] * x3[(1,3,1,1)].varValue +E_31[1] * x3[(2,3,1,1)].varValue ) > Tetha_31:
            cuts_31.append( E_31[0] * x3[(1,3,1,1)] +E_31[1] * x3[(2,3,1,1)] +tetha3[(3,1)] >= e_31 )
            print('the cut : ', E_31[0] * x3[(1,3,1,1)] +E_31[1] * x3[(2,3,1,1)] +tetha3[(3,1)] >= e_31 , "   is added to nlds31")
            ecuts_31.append(e_31)
        if e_32 - (E_32[0] * x3[(1,3,1,2)].varValue +E_32[1] * x3[(2,3,1,2)].varValue ) > Tetha_32:
            cuts_32.append( E_32[0] * x3[(1,3,1,2)] +E_32[1] * x3[(2,3,1,2)] +tetha3[(3,2)] >= e_32 )
            print('the cut : ', E_32[0] * x3[(1,3,1,2)] +E_32[1] * x3[(2,3,1,2)] +tetha3[(3,2)] >= e_32 , "   is added to nlds32")
            ecuts_32.append(e_32)
        if e_33 - (E_33[0] * x3[(1,3,2,1)].varValue +E_33[1] * x3[(2,3,2,1)].varValue ) > Tetha_33:
            cuts_33.append( E_33[0] * x3[(1,3,2,1)] +E_33[1] * x3[(2,3,2,1)] +tetha3[(3,3)] >= e_33 )
            print('the cut : ', E_33[0] * x3[(1,3,2,1)] +E_33[1] * x3[(2,3,2,1)] +tetha3[(3,3)] >= e_33, "   is added to nlds33")
            ecuts_33.append(e_33)
        if e_34 - (E_34[0] * x3[(1,3,2,2)].varValue +E_34[1] * x3[(2,3,2,2)].varValue ) > Tetha_34:
            cuts_34.append( E_34[0] * x3[(1,3,2,2)] +E_34[1] * x3[(2,3,2,2)] +tetha3[(3,4)] >= e_34 )
            print('the cut : ', E_34[0] * x3[(1,3,2,2)] +E_34[1] * x3[(2,3,2,2)] +tetha3[(3,4)] >= e_34 , "   is added to nlds34")
            ecuts_34.append(e_34)
    
    nlds_31= NLDS_31(cuts_31, x_21)
    print('NLDS31 now is :')
    print(nlds_31.extend)
    status=nlds_31.solve()
    x_31=list()
    for var in nlds_31.variables()[1:]:
        x_31.append(var.value())
    Tetha_31=nlds_31.variables()[0].value()
    dual_31=list(nlds_31.constraints.items())[0][1].pi
    optimality_dual_31=list()
    if len(cuts_31)>0:                      
        for i in range(1,len(list(nlds_31.constraints.items()))):                    
            optimality_dual_31.append(list(nlds_31.constraints.items())[i][1].pi)
    else:
        optimality_dual_31=0
    nlds_32= NLDS_32(cuts_32, x_21)
    print('NLDS32 now is :')
    print(nlds_32.extend)
    status=nlds_32.solve()                      
    x_32=list()
    for var in nlds_32.variables()[1:]:
        x_32.append(var.value())
    Tetha_32=nlds_32.variables()[0].value()
    dual_32=list(nlds_32.constraints.items())[0][1].pi
    optimality_dual_32=list()
    if len(cuts_32)>0:                      
        for i in range(1,len(list(nlds_32.constraints.items()))):                    
            optimality_dual_32.append(list(nlds_32.constraints.items())[i][1].pi)
    else:
        optimality_dual_32=0
                           
    nlds_33= NLDS_33(cuts_33, x_22)
    print('NLDS33 now is :')
    print(nlds_33.extend)
    status=nlds_33.solve()                      
    x_33=list()
    for var in nlds_33.variables()[1:]:
        x_33.append(var.value())
    Tetha_33=nlds_33.variables()[0].value()
    dual_33=list(nlds_33.constraints.items())[0][1].pi
    optimality_dual_33=list()
    if len(cuts_33)>0:                      
        for i in range(1,len(list(nlds_33.constraints.items()))):                    
            optimality_dual_33.append(list(nlds_33.constraints.items())[i][1].pi)
    else:
        optimality_dual_33=0
                           
    nlds_34= NLDS_34(cuts_34, x_22)
    print('NLDS34 now is :')
    print(nlds_34.extend)
    status=nlds_34.solve()
    x_34=list()
    for var in nlds_34.variables()[1:]:
        x_34.append(var.value())
    Tetha_34=nlds_34.variables()[0].value()
    dual_34=list(nlds_34.constraints.items())[0][1].pi
    optimality_dual_34=list()
    if len(cuts_34)>0:                      
        for i in range(1,len(list(nlds_34.constraints.items()))):                    
            optimality_dual_34.append(list(nlds_34.constraints.items())[i][1].pi)
    else:
        optimality_dual_34=0
    E_21=list(0.5 * (np.matmul([dual_31],[T1]) + np.matmul([dual_32],[T2])))
    e_21=0.5 * (np.matmul([dual_31],[h1]) + np.matmul([dual_32],[h1])+ np.matmul(ecuts_31,optimality_dual_31) +np.matmul(ecuts_32,optimality_dual_32))
    E_22=list(0.5 * (np.matmul([dual_33],[T1]) + np.matmul([dual_34],[T2])))
    e_22=0.5 * (np.matmul([dual_33],[h1]) + np.matmul([dual_34],[h1])+np.matmul(ecuts_33,optimality_dual_33) +np.matmul(ecuts_34,optimality_dual_34))
    if I==1:
        a=nlds_21.constraints.pop('_C2')
        a=nlds_22.constraints.pop('_C2')
        cuts_21.append( E_21[0] * x2[(1,2,1)] +E_21[1] * x2[(2,2,1)] +tetha2[(2,1)] >= e_21 )
        print('the cut : ', E_21[0] * x2[(1,2,1)] +E_21[1] * x2[(2,2,1)] +tetha2[(2,1)] >= e_21 , "   is added to nlds21")
        cuts_22.append( E_22[0] * x2[(1,2,2)] +E_22[1] * x2[(2,2,2)] +tetha2[(2,2)] >= e_22 )
        print('the cut : ', E_22[0] * x2[(1,2,2)] +E_22[1] * x2[(2,2,2)] +tetha2[(2,2)] >= e_22 , "   is added to nlds22")
        ecuts_21.append(e_21)
        ecuts_22.append(e_22)
    else:
        if e_21 - (E_21[0] * x2[(1,2,1)].varValue +E_21[1] * x2[(1,2,1)].varValue ) > Tetha_21:
            cuts_21.append( E_21[0] * x2[(1,2,1)] +E_21[1] * x2[(2,2,1)] +tetha2[(2,1)] >= e_21 )
            print('the cut : ', E_21[0] * x2[(1,2,1)] +E_21[1] * x2[(2,2,1)] +tetha2[(2,1)] >= e_21 , "   is added to nlds21")
            ecuts_21.append(e_21)
        if e_22 - (E_22[0] * x2[(1,2,2)].varValue +E_22[1] * x2[(2,2,2)].varValue ) > Tetha_22:
            cuts_22.append( E_22[0] * x2[(1,2,2)] +E_22[1] * x2[(2,2,2)] +tetha2[(2,2)] >= e_22 )
            print('the cut : ', E_22[0] * x2[(1,2,2)] +E_22[1] * x2[(2,2,2)] +tetha2[(2,2)] >= e_22 , "   is added to nlds22")
            ecuts_22.append(e_22)   
    nlds_21= NLDS_21(cuts_21, x_1)
    print('NLDS21 now is :')
    print(nlds_21.extend)
    status=nlds_21.solve()
    x_21=list()
    for var in nlds_21.variables()[1:]:
        x_21.append(var.value())
    Tetha_21=nlds_21.variables()[0].value()
    dual_21=list(nlds_21.constraints.items())[0][1].pi
    optimality_dual_21=list()
    if len(cuts_21)>0:                      
        for i in range(1,len(list(nlds_21.constraints.items()))):                    
            optimality_dual_21.append(list(nlds_21.constraints.items())[i][1].pi)
    else:
        optimality_dual_21=0                 
    
    nlds_22= NLDS_22(cuts_22, x_1)
    print('NLDS22 now is :')
    print(nlds_22.extend)
    status= nlds_22.solve()                     
    x_22=list()
    for var in nlds_22.variables()[1:]:
        x_22.append(var.value())
    Tetha_22=nlds_22.variables()[0].value()
    dual_22=list(nlds_22.constraints.items())[0][1].pi
    optimality_dual_22=list()
    if len(cuts_22)>0:                      
        for i in range(1,len(list(nlds_22.constraints.items()))):                    
            optimality_dual_22.append(list(nlds_22.constraints.items())[i][1].pi)
    else:
        optimality_dual_22=0
               
    E1=list(0.5 * (np.matmul([dual_21],[T1]) + np.matmul([dual_22],[T2])))
    e1=0.5 * (np.matmul([dual_21],[h1]) + np.matmul([dual_22],[h1]) + np.matmul(ecuts_21,optimality_dual_21)+np.matmul(ecuts_22,optimality_dual_22))
    Continue=False
    
    if I==1:
        a=nlds_1.constraints.pop('_C2')
        cuts_1.append( E1[0] * x1[(1,1)] +E1[1] * x1[(2,1)] +tetha1[(1,1)] >= e1 )
        print('the cut : ',E1[0] * x1[(1,1)] +E1[1] * x1[(2,1)] +tetha1[(1,1)] >= e1 , "   is added to nlds1")
        print('NLDS1 now is :')
        print(nlds_1.extend)
        Continue=True
    else:
        if np.round(e1 - (E1[0] * x1[(1,1)].varValue +E1[1] * x1[(2,1)].varValue ),4) > np.round(Tetha_1,4):
            cuts_1.append( E1[0] * x1[(1,1)] +E1[1] * x1[(2,1)] +tetha1[(1,1)] >= e1 )
            print('the cut : ',E1[0] * x1[(1,1)] +E1[1] * x1[(2,1)] +tetha1[(1,1)] >= e1 , "   is added to nlds1")
            print('NLDS1 now is :')
            print(nlds_1.extend)
            print('----------------------------------------------------------------')
            Continue=True
    if not Continue:
        print('no cut is added to nlds1')
        print('Therefore, the optimal solution is as below:')
        print('The Objective Function Value is : ',-(nlds_41.objective.value()+nlds_42.objective.value()+nlds_43.objective.value()+nlds_44.objective.value()+nlds_45.objective.value()+nlds_46.objective.value()+nlds_47.objective.value()+nlds_48.objective.value())/8)
        for var in nlds_1.variables():
             print(f"{var.name}: {var.value()}")
        for var in nlds_21.variables():
             print(f"{var.name}: {var.value()}")
        for var in nlds_22.variables():
             print(f"{var.name}: {var.value()}")
        for var in nlds_31.variables():
             print(f"{var.name}: {var.value()}")
        for var in nlds_32.variables():
             print(f"{var.name}: {var.value()}")
        for var in nlds_33.variables():
             print(f"{var.name}: {var.value()}")
        for var in nlds_34.variables():
             print(f"{var.name}: {var.value()}")
        for var in nlds_41.variables():
             print(f"{var.name}: {var.value()}")
        for var in nlds_42.variables():
             print(f"{var.name}: {var.value()}")
        for var in nlds_43.variables():
             print(f"{var.name}: {var.value()}")
        for var in nlds_44.variables():
             print(f"{var.name}: {var.value()}")
        for var in nlds_45.variables():
             print(f"{var.name}: {var.value()}")
        for var in nlds_46.variables():
             print(f"{var.name}: {var.value()}")
        for var in nlds_47.variables():
             print(f"{var.name}: {var.value()}")
        for var in nlds_48.variables():
             print(f"{var.name}: {var.value()}")
