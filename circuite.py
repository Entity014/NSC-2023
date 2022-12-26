import schemdraw
import schemdraw.elements as elm
import matplotlib.pyplot as plt
import numpy as np
import time

def cir1():
    with schemdraw.Drawing() as d:
        d += (c1 := elm.Capacitor(polar=True).label('25$\mu$F'))
        d += elm.Capacitor(polar=True).right().label('10$\mu$F')
        d += elm.Resistor().up().label('$1k\Omega$').at(c1.start)
        d += elm.Resistor().right().label('$1k\Omega$')
        d += elm.Resistor().right().label('$2k\Omega$')
        d += elm.Diode().down()

def cir2():
    with schemdraw.Drawing() as d:
        d.config(inches_per_unit=.5, unit=3)
        d += (D := elm.Rectifier())
        d += elm.Line().down(d.unit*2).at(D.W)
        d += (G := elm.Line().right(d.unit*1.9).idot())
        d += (T := elm.Line().right(d.unit*0.5).at(D.E).dot(open=True).idot())
        d += elm.Capacitor(polar=True).toy(G.start).flip().label('25$\mu$F').dot().idot()
        d += elm.Ground().right().at(G.start)
        d += (R1 := elm.Line().right().at(T.start).dot(open=True))
        d += elm.Resistor().down().label('$1k\Omega$').at(R1.end).idot()
        d += elm.LED().down().dot(open=True)
        d += (G2 := elm.Line().left(d.unit/2).dot().idot())
        d += (R2 := elm.Resistor().right().label('$2k\Omega$').at(R1.end).dot(open=True))
        d += (G3 := elm.Line().right().at(G2.start).dot(open=True))
        d += elm.LED().at(R2.end).to(G3.end).dot().idot()

def lineB(d, arr, direct:str, color:str, end:int):
    for i, var in enumerate(range(1, end)):
        if direct == 'right':
            d += (var := elm.Line().right().dot(open=True).idot(open=True).color(color))
            arr = np.append(arr, var)
        elif direct == 'left':
            d += (var := elm.Line().left().dot(open=True).idot(open=True).color(color))
            arr = np.append(arr, var)
        elif direct == 'up':
            d += (var := elm.Line().up().dot(open=True).idot(open=True).color(color))
            arr = np.append(arr, var)
        elif direct == 'down':
            d += (var := elm.Line().down().dot(open=True).idot(open=True).color(color))
            arr = np.append(arr, var)
    return arr

def textB(d, dictO:dict, dictS:dict, arrS:str, text:str):
    d += elm.Annotate().at(dictO['N_arr'][0].start).delta(dx=-1, dy=0.5).label('-').color('black')
    d += elm.Annotate().at(dictO['P_arr'][0].start).delta(dx=-1, dy=0.5).label('+').color('red')
    d += elm.Annotate().at(dictO['N_arr'][-1].end).delta(dx=1, dy=0.5).label('-').color('black')
    d += elm.Annotate().at(dictO['P_arr'][-1].end).delta(dx=1, dy=0.5).label('+').color('red')
    d += elm.Annotate().at(dictS[f'{arrS}{1}'][0].start).delta(dx=-1, dy=0.5).label(chr(ord(text))).color('black')
    d += elm.Annotate().at(dictS[f'{arrS}{30}'][0].start).delta(dx=1, dy=0.5).label(chr(ord(text))).color('black')
    for i in range(0, 4):
            d += elm.Annotate().at(dictS[f'{arrS}{1}'][i].end).delta(dx=-1, dy=0.5).label(chr(ord(text) - i - 1)).color('black')
            d += elm.Annotate().at(dictS[f'{arrS}{30}'][i].end).delta(dx=1, dy=0.5).label(chr(ord(text) - i - 1)).color('black')

def cir3():
    comp = [['C', ['ae1', 0, 'ae2', 0]], ['R', ['ae1', 2,'ae2', 2]]]
    start_time = time.time()
    arrRow = [i for i in range(5)]
    arrOut = np.array(['N_arr', 'P_arr'])
    arrSide = np.array(['fj', 'ae'])
    dictOut1, dictOut2 = {'N_arr': np.array([], dtype='object'),'P_arr': np.array([], dtype='object')}, {'N_arr': np.array([], dtype='object'),'P_arr': np.array([], dtype='object')}
    dictSide1, dictSide2 = {}, {}
    arr1, arr2 = [], []
    for i in range(1, 31):
        dictSide1[f'{arrSide[0]}{i}'] = np.array([], dtype='object')
        dictSide2[f'{arrSide[1]}{i}'] = np.array([], dtype='object')
        arr1.append([f'{arrSide[0]}{i}', arrRow])
        arr2.append([f'{arrSide[1]}{i}', arrRow])
    with schemdraw.Drawing() as d:
        for i in range(0, 2):
            if arrOut[i] == 'N_arr':
                dictOut1[arrOut[i]] = lineB(d, dictOut1[arrOut[i]], 'right', 'black', 30)
                d.here = (0, (-i) - 1)
            elif arrOut[i] == 'P_arr':
                dictOut1[arrOut[i]] = lineB(d, dictOut1[arrOut[i]], 'right', 'red', 30)
                d.here = (0, (-i) - 1)
        for i in range(0, 30):
            dictSide1[f'{arrSide[0]}{i + 1}'] = lineB(d, dictSide1[f'{arrSide[0]}{i + 1}'], 'down', 'blue', 5)
            d.here = (((i + 1)*3), -2)
        d.here = (0, -16)
        for i in range(0, 30):
            dictSide2[f'{arrSide[1]}{i + 1}'] = lineB(d, dictSide2[f'{arrSide[1]}{i + 1}'], 'down', 'blue', 5)
            d.here = (((i + 1)*3), -16)
        d.here = (0, -29)
        for i in range(0, 2):
            if arrOut[i] == 'N_arr':
                dictOut2[arrOut[i]] = lineB(d, dictOut2[arrOut[i]], 'right', 'black', 30)
                d.here = (0, (-i) - 30)
            elif arrOut[i] == 'P_arr':
                dictOut2[arrOut[i]] = lineB(d, dictOut2[arrOut[i]], 'right', 'red', 30)
                d.here = (0, (-i) - 30)
        textB(d, dictOut1, dictSide1, arrSide[0], 'j')
        textB(d, dictOut2, dictSide2, arrSide[1], 'e')
        
        for i in range(len(comp)):
            if comp[i][0] == 'R':
                d += elm.Resistor().at(dictSide2[comp[i][1][0]][comp[i][1][1]].start).to(dictSide2[comp[i][1][2]][comp[i][1][3]].start)
            elif comp[i][0] == 'C':
                d += elm.Capacitor().at(dictSide2[comp[i][1][0]][comp[i][1][1]].start).to(dictSide2[comp[i][1][2]][comp[i][1][3]].start)
        
        d.save('image.png', False)
        plt.close()
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")

def main():
    cir3()

if __name__ == '__main__':
    main()
