import schemdraw
import schemdraw.elements as elm
import numpy as np

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

def lineB(d, arr, direct:str, end:int):
    for i, var in enumerate(range(1, end)):
        if direct == 'right':
            d += (var := elm.Line().right().dot(open=True).idot(open=True))
            arr = np.append(arr, var)
        elif direct == 'left':
            d += (var := elm.Line().left().dot(open=True).idot(open=True))
            arr = np.append(arr, var)
        elif direct == 'up':
            d += (var := elm.Line().up().dot(open=True).idot(open=True))
            arr = np.append(arr, var)
        elif direct == 'down':
            d += (var := elm.Line().down().dot(open=True).idot(open=True))
            arr = np.append(arr, var)
    return arr

def cir3():
    arrOut = np.array(['N_arr', 'P_arr'])
    arrSide1, arrSide2 = np.array([]), np.array([])
    dictOut1, dictOut2 = {'N_arr': np.array([], dtype='object'),'P_arr': np.array([], dtype='object')}, {'N_arr': np.array([], dtype='object'),'P_arr': np.array([], dtype='object')}
    dictSide1, dictSide2 = {}, {}
    for i in range(1, 31):
        dictSide1[f'fj{i}'] = np.array([], dtype='object')
        arrSide1 = np.append(arrSide1, f'fj{i}')
        dictSide2[f'ae{i}'] = np.array([], dtype='object')
        arrSide2 = np.append(arrSide2, f'ae{i}')
    with schemdraw.Drawing() as d:
        for i in range(0, 2):
            dictOut1[arrOut[i]] = lineB(d, dictOut1[arrOut[i]], 'right', 30)
            d.here = (0, (-i) - 1)
        for i in range(0, 30):
            dictSide1[arrSide1[i]] = lineB(d, dictSide1[arrSide1[i]], 'down', 5)
            d.here = (((i + 1)*3), -2)
        d.here = (0, -16)
        for i in range(0, 30):
            dictSide2[arrSide2[i]] = lineB(d, dictSide2[arrSide2[i]], 'down', 5)
            d.here = (((i + 1)*3), -16)
        d.here = (0, -29)
        for i in range(0, 2):
            dictOut2[arrOut[i]] = lineB(d, dictOut2[arrOut[i]], 'right', 30)
            d.here = (0, (-i) - 30)
        # for i in range(0, 2):
        #     dictSide2[arrSide2[i]] = lineB(d, dictSide2[arrSide2[i]], 'right', 5)
        #     d.here = (((i + 1)*3), -16)
        #d += elm.LED().down().at(P_arr[2].end).to(N_arr[2].end)
        d += elm.Annotate().at(dictOut1['N_arr'][0].start).delta(dx=-1, dy=0.5).label('-').color('black')
        d += elm.Annotate().at(dictOut1['P_arr'][0].start).delta(dx=-1, dy=0.5).label('+').color('red')
        d += elm.Annotate().at(dictOut1['N_arr'][-1].end).delta(dx=1, dy=0.5).label('-').color('black')
        d += elm.Annotate().at(dictOut1['P_arr'][-1].end).delta(dx=1, dy=0.5).label('+').color('red')
        d += elm.Annotate().at(dictOut2['N_arr'][0].start).delta(dx=-1, dy=0.5).label('-').color('black')
        d += elm.Annotate().at(dictOut2['P_arr'][0].start).delta(dx=-1, dy=0.5).label('+').color('red')
        d += elm.Annotate().at(dictOut2['N_arr'][-1].end).delta(dx=1, dy=0.5).label('-').color('black')
        d += elm.Annotate().at(dictOut2['P_arr'][-1].end).delta(dx=1, dy=0.5).label('+').color('red')
        d += elm.Annotate().at(dictSide1[arrSide1[0]][0].start).delta(dx=-1, dy=0.5).label(chr(ord('j'))).color('black')
        d += elm.Annotate().at(dictSide1[arrSide1[-1]][0].start).delta(dx=1, dy=0.5).label(chr(ord('j'))).color('black')
        d += elm.Annotate().at(dictSide2[arrSide2[0]][0].start).delta(dx=-1, dy=0.5).label(chr(ord('e'))).color('black')
        d += elm.Annotate().at(dictSide2[arrSide2[-1]][0].start).delta(dx=1, dy=0.5).label(chr(ord('e'))).color('black')
        
        for i in range(0, 4):
            d += elm.Annotate().at(dictSide1[arrSide1[0]][i].end).delta(dx=-1, dy=0.5).label(chr(ord('j') - i - 1)).color('black')
            d += elm.Annotate().at(dictSide1[arrSide1[-1]][i].end).delta(dx=1, dy=0.5).label(chr(ord('j') - i - 1)).color('black')
            d += elm.Annotate().at(dictSide2[arrSide2[0]][i].end).delta(dx=-1, dy=0.5).label(chr(ord('e') - i - 1)).color('black')
            d += elm.Annotate().at(dictSide2[arrSide2[-1]][i].end).delta(dx=1, dy=0.5).label(chr(ord('e') - i - 1)).color('black')

def main():
    cir3()

if __name__ == '__main__':
    main()
