from image2net import toNetlist
from lcapy import Circuit

def checkParallel(netlist):
  new_netlist = netlist.copy()
  finished = set()
  max_level = 0
  for idx1,comp1,nl1,nr1 in netlist:
    count = 0
    for idx2,comp2,nl2,nr2 in netlist:
      if idx2 > idx1 and not(idx2 in finished) and nl1 == nl2 and nr1 == nr2:         
          new_netlist[idx2-1] = [idx2,comp2,str(nl1)+"_"+str(count),str(nr1)+"_"+str(count)]
          if count == 0:
            new_netlist.append([-1, 'W', nl1, str(nl1)+"_"+str(count)])
            new_netlist.append([-1, 'W', nr1, str(nr1)+"_"+str(count)])
          else:
            new_netlist.append([-1, 'W',  str(nl1)+"_"+str(count-1), str(nl1)+"_"+str(count)])
            new_netlist.append([-1, 'W', str(nr1)+"_"+str(count-1), str(nr1)+"_"+str(count)])
          count += 1
          finished.add(idx2)
    max_level = max([max_level,count])
  return new_netlist,max_level


def netlist2Circuit(netlist):
  netlist,max_level = checkParallel(netlist)
  #print(netlist)
  text = ""
  nodes = []
  for idx,comp,nl,nr in netlist:
    if comp == "W":
      text += comp+" "+str(nl)+" "+str(nr)+"; up\n"
    else:
      text += comp+" "+str(nl)+" "+str(nr)+"; right, l=\n"
    nodes += [nl,nr]
  
  gnds = []
  vccs = []
  finished = set()
  for n in nodes:
    if not(n in finished) and (nodes.count(n) == 1 or str(n).find("_") == -1):
      text += "O"+str(n)+" "+str(n)+" 0_"+str(n)+"; down\n"      
      gnds.append("0_"+str(n))
      if len(vccs) == 0:
        text += "O99"+str(n)+" "+str(n)+" 99"+"; up = "+str(max_level+1)+"\n"
        vccs.append("99")
      else:
        text += "O99"+str(n)+" "+str(n)+" 99_"+str(n)+"; up = "+str(max_level+1)+"\n"
        vccs.append("99_"+str(n)) 
      finished.add(n) 
      

  for i in range(len(gnds)-1):
    if i < len(gnds)-2:
      text += "W "+gnds[i]+" "+gnds[i+1]+"; right\n"
    else:
      text += "W "+gnds[i]+" "+gnds[i+1]+"; right,implicit, l=GND\n"

  for i in range(len(vccs)-1):
    if i < len(vccs)-2:
      text += "W "+vccs[i]+" "+vccs[i+1]+"; right\n"
    else:
      text += "W "+vccs[i]+" "+vccs[i+1]+"; right,implicit, l=V_S\n"


  text += ";label_nodes=false, draw_nodes=connections"
  cct = Circuit(text)

  return text, cct


#netlist = [[1, 'R0', 4, 1], [2, 'C1', 1, 2], [3, 'D2', 3, 5]]
#netlist = [[1, 'R0', 1, 2], [2, 'R1', 1, 2]]
#netlist = [[1, 'R0', 1, 2], [2, 'R1', 1, 2], [3, 'R3', 2, 3],[4, 'R4', 3, 4],[5, 'R5', 3, 4],[6, 'R6', 3, 4]]
#netlist = [[1, 'R0', 1, 2], [2, 'R1', 1, 2], [3, 'R3', 2, 3],[4, 'R4', 3, 4],[5, 'R5', 3, 4],[6, 'R6', 3, 4],[7, 'R7', 4, 5],[8, 'R8', 6, 7]]
#netlist = [[1, 'R0', 1, 2], [2, 'R1', 2, 3],[3, 'R3', 1, 3]]
path = "runs/detect/exp6/labels/IMG_2467.txt"
netlist = toNetlist(path ,"Low")
text,cct = netlist2Circuit(netlist)

print(text)
cct.draw("Result/result.png")
