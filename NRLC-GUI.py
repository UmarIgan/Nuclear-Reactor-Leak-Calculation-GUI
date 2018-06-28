import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *

pencere=Tk()
pencere.geometry('600x600+100+100')
pencere.title('RADİATİON DİFİSSİON')

lbl1=Label(text='difission(gr/sec):')
lbl1.grid(row=1, column=0)
lbl3=Label(text='Wind speed(km/h):')
lbl3.grid(row=3, column=0)
lbl4=Label(text='how far(meter):')
lbl4.grid(row=4, column=0)
e1=Entry()
e1.grid(row=1, column=1)
e2=Entry()
e2.grid(row=3, column=1)
e3=Entry()
e3.grid(row=4, column=1)
def SUNNY_DAY():   #formulation of leak calculation for sunny days. All formula and data taken from Introduction to Nuclear Engineering Third Edition
#by John R. Lamarsh and Anthony J. Baratta. Chapter 11 Reactor licensing, safety and enviroment.

    df = pd.read_csv('l_y.txt')# data of Horizantal dispersion coefficient sigma-y as a function of distance for the various pasquill conditions
                               #you can find it on the book page-642
    l=float(e2.get())#Wind speed
    
    w=int(e3.get())#Distance
    l_mapping = [1, 5, 12, 20, 35, 50]
    l_index = np.searchsorted(l_mapping, l)
    col = df.columns[1:][l_index]
    row = np.searchsorted(df.mesafe.values, w)
    k=df[col].iloc[row]#sigma-y, finding the sigma-y value in a spesific cell

    df2 = pd.read_csv('l_z.txt')
    l_mapping2 = [1, 5, 12, 20, 35, 50]
    l_index2 = np.searchsorted(l_mapping2, l)
    col2 = df2.columns[1:][l_index2]
    row2 = np.searchsorted(df2.mesafe.values, w)
    k2=df[col2].iloc[row2]#sigma-z,finding the sigma-z value in a spesific cell
    
    Vd=0.02 #storage speed
    h=30 #chimney height
    landa=8.1384311168273*(10**-9) #St-90^s half life per In2
    m=float(e1.get())#yayılma oranı
    u=np.exp(-((landa/l)*w)*(-(h**2)/(2*(k2**2))))
    r=float(m/(np.pi*l*k*k2))
    X=float(u*r)
    blank.insert(0, X)
    liste.insert(0, X) #i am also add the result to the list so you cant take them and draw a graph
btn=Button(text='Sunny day(g/m3)', command=SUNNY_DAY)
btn.grid(row=5, column=0)
blank=Entry()
blank.grid(row=5, column=1)
liste=Listbox()
liste.grid(row=8, column=0)
def delet():
    liste.delete(0,END)
    liste2.delete(0, END)
    
btn3=Button(text='del list', command=delet)
btn3.grid(row=9, column=1)
def new_window():  #graph for sunny day based on 12 g/s leak of St-90
    fig = plt.subplot()
    t=np.array([1.0000, 2.0000, 5.0000,
            10.0000,20.0000, 50.0000, 100.0000]) #x-axis distances(km)

    l=np.array([9.54, 2.38, 0.568, 0.149, 0.0487, 0.0109, 0.00381])#1 km/h wind speed
    l2=np.array([2.98, 0.848, 0.293, 0.0530, 0.0173, 0.00361, 0.00116])#5 km/h 
    l3=np.array([2.63, 0.795, 0.220, 0.0440, 0.0124, 0.00275, 0.000855])#12 km/h
    l4=np.array([3.684, 0.974, 0.211, 0.063, 0.019, 0.0018, 0.0012])#20 km/h
    l5=np.array([3.607, 1.391, 0.206, 0.068, 0.016, 0.0042, 0.0013])#35 km/h
    l6=np.array([4.774, 1.559, 0.298, 0.090, 0.030, 0.0063, 0.0019])#50 km/h
    fig.set(xlabel='km', ylabel='difission(g/m3)',title='spread to meter graph')
    plt.plot(t, l)
    plt.plot(t, l2)
    plt.plot(t, l3)
    plt.plot(t, l4)
    plt.plot(t, l5)
    plt.plot(t,l6)
    plt.show()

btn2=Button(text='sunny_graph', command=new_window)
btn2.grid(row=1, column=2)


def RAİNY_DAY():# data of Vertical dispersion coefficient sigma-z as a function of distance for the various pasquill conditions
                #you can find it on the book page-643
                
    df = pd.read_csv('l_y.txt')
    l=float(e2.get())#rüzgar hızı
    w=int(e3.get())#mesefa
    l_mapping = [1, 12, 20, 30, 40, 50]
    l_index = np.searchsorted(l_mapping, l)
    col = df.columns[1:][l_index]
    row = np.searchsorted(df.mesafe.values, w)
    k=df[col].iloc[row]# sigma-y

    df2 = pd.read_csv('l_z.txt')
    l_mapping2 = [1, 12, 20, 30,40, 50]
    l_index2 = np.searchsorted(l_mapping2, l)
    col2 = df2.columns[1:][l_index2]
    row2 = np.searchsorted(df2.mesafe.values, w)
    k2=df[col2].iloc[row2]#sigma-z
    
    Vd=0.02#depolama hızı
    h=30#baca yüksekliği
    landa=8.1384311168273*(10**-9)
    m=float(e1.get())#spread rate of St-90
    d=Vd/l
    u=np.exp(d+((landa/l)*w)+((h**2)/(2*(k2**2))))
    e=m/(np.pi*k*k2*l)
    X=float(u*e)
    blank2.insert(0, X)
    liste2.insert(0, X)
liste2=Listbox()
liste2.grid(row=8, column=1)    


btn2=Button(text="rainy day(g/m3)",command=RAİNY_DAY)
btn2.grid(row=7, column=0)
blank2=Entry()
blank2.grid(row=7, column=1)

def new_window2():#graph for sunny day with 12 g/s leak of St-90, this part is calculated 
    fig = plt.subplot()
    t=np.array([1.0000, 2.0000, 5.0000,
            10.0000,20.0000, 50.0000, 100.0000])

    l=np.array([3.852, 2.442, 0.575, 0.152, 0.0497, 0.0111, 0.0039])#1 m/s için difission
    l2=np.array([3.049, 0.856, 0.295, 0.0532, 0.0179, 0.0036, 0.0011])#5 m/s için 
    l3=np.array([1.267, 0.356, 0.122, 0.0221, 0.00723, 0.0015, 0.0048])#12 m/s için
    l4=np.array([1.639, 0.483, 0.132, 0.0269, 0.0074, 0.0016, 0.0005])#20 m/s
    l5=np.array([4.188, 1.142, 0.208, 0.0684, 0.0162, 0.00426, 0.0013])#35 m/s
    l6=np.array([6.327, 1.709, 0.303, 0.0913, 0.0306, 0.0063, 0.0019])#50 m/s
    fig.set(xlabel='km', ylabel='difission(g/m3)',title='difission to meter rate')
    plt.plot(t, l)
    plt.plot(t, l2)
    plt.plot(t, l3)
    plt.plot(t, l4)
    plt.plot(t, l5)
    plt.plot(t,l6)
    plt.show()
btn2=Button(text='rainy_graph', command=new_window2)
btn2.grid(row=1, column=4)

def new_window2(): #graph for rainy day with 12 g/s leak of St-90, this part is calculated 
    fig = plt.subplot()
    t=np.array([1.0000, 2.0000, 5.0000,
            10.0000,20.0000, 50.0000, 100.0000])

    l=np.array([3.852, 2.442, 0.575, 0.152, 0.0497, 0.0111, 0.0039])#1 m/s 
    l2=np.array([3.049, 0.856, 0.295, 0.0532, 0.0179, 0.0036, 0.0011])#5 m/s 
    l3=np.array([1.267, 0.356, 0.122, 0.0221, 0.00723, 0.0015, 0.0048])#12 m/s 
    l4=np.array([1.639, 0.483, 0.132, 0.0269, 0.0074, 0.0016, 0.0005])#20 m/s
    l5=np.array([4.188, 1.142, 0.208, 0.0684, 0.0162, 0.00426, 0.0013])#35 m/s
    l6=np.array([6.327, 1.709, 0.303, 0.0913, 0.0306, 0.0063, 0.0019])#50 m/s
    fig.set(xlabel='km', ylabel='difission(g/m3)',title='difission to meter rate')
    plt.plot(t, l)
    plt.plot(t, l2)
    plt.plot(t, l3)
    plt.plot(t, l4)
    plt.plot(t, l5)
    plt.plot(t,l6)
    plt.show()
btn2=Button(text='rainy_graph', command=new_window2)
btn2.grid(row=1, column=4)
mainloop()
