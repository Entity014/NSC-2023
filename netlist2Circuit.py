from lcapy import Circuit, Vstep, R, C
from image2net import toNetlist
def netlist2Circuit(netlist):
  text = ""
  nodes = []
  for idx,comp,nl,nr in netlist:
    text += comp+" "+str(nl)+" "+str(nr)+"; right\n"
    nodes += [nl,nr]
  
  gnds = []
  for n in nodes:
    if nodes.count(n) == 1:
      text += "O"+str(n)+" "+str(n)+" 0_"+str(n)+"; down\n"
      gnds.append("0_"+str(n))

  for i in range(len(gnds)-1):
    if i < len(gnds)-2:
      text += "W "+gnds[i]+" "+gnds[i+1]+"; right\n"
    else:
      text += "W "+gnds[i]+" "+gnds[i+1]+"; right,implicit, l=GND\n"

  cct = Circuit(text)

  return text, cct


# netlist = [[1, 'R0', 4, 1], [2, 'R1', 1, 2], [3, 'R2', 3, 5]]
netlist = toNetlist("High")
text,cct = netlist2Circuit(netlist)

print(text)
cct.draw("result.png")