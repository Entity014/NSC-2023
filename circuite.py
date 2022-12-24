import schemdraw
import schemdraw.elements as elm

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

def main():
    cir1()

if __name__ == '__main__':
    main()
