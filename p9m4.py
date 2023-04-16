
import networkx as nx
from graphviz import Graph
from IPython.display import display_html
def hasse_diagram(op,rel,dual,unary=[]):
    A = range(len(op))
    G = nx.DiGraph()
    if rel:
        G.add_edges_from([(x,y) for x in A for y in A if (op[y][x] if dual else op[x][y]) and x!=y])
    else: 
        G.add_edges_from([(x,y) for x in A for y in A if op[x][y]==(y if dual else x) and x!=y])
    try:
        G = nx.algorithms.dag.transitive_reduction(G)
    except:
        pass
    P = Graph()
    P.attr('node', shape='circle', width='.15', height='.15', fixedsize='true', fontsize='10')
    for x in A: P.node(str(x), color='red' if unary[x] else 'black')
    P.edges([(str(x[0]),str(x[1])) for x in G.edges])
    return P

def m4diag(li,symbols="<= v", unaryRel=""):
  # use graphviz to display a mace4 structure as a diagram
  # symbols is a list of binary symbols that define a poset or graph
  # unaryRel is a unary relation symbol that is displayed by red nodes
  i = -1
  sy = symbols.split(" ")
  #print(symbols,"***",sy)
  st = ""
  for x in li:
    i+=1
    st+=str(i)
    uR = x.relations[unaryRel] if unaryRel!="" else [0]*x.cardinality
    for s in sy:
            t = s[:-1] if s[-1]=='d' else s
            if t in x.operations.keys():
                st+=hasse_diagram(x.operations[t],False,s[-1]=='d',uR)._repr_image_svg_xml()+"&nbsp; &nbsp; &nbsp; "
            elif t in x.relations.keys():
                st+=hasse_diagram(x.relations[t], True, s[-1]=='d',uR)._repr_image_svg_xml()+"&nbsp; &nbsp; &nbsp; "
    st+=" &nbsp; "
  display_html(st,raw=True)

def compatiblepreorders(A, precon=True, sym=False):
  signum={
  "-":"C(x,y)->C(-y,-x)",
  "~":"C(x,y)->C(~y,~x)",
  "'":"C(x,y)->C(y',x')",
  "f":"C(x,y)->C(f(x),f(y))",
  "*":"C(x,y)->C(x*z,y*z)&C(z*x,z*y)",
  "+":"C(x,y)->C(x+z,y+z)&C(z+x,z+y)",
  "\\":"C(x,y)->C(y\ z,x\ z)&C(z\ x,z\ y)",
  "/":"C(x,y)->C(x/z,y/z)&C(z/y,z/x)",
  "^":"C(x,y)->C(x^z,y^z)&C(z^x,z^y)",
  "v":"C(x,y)->C(x v z,y v z)&C(z v x,z v y)",
  }
  if type(A)==str: A=eval(A)
  m=A.cardinality
  compat = ["C(x,y)&C(y,z)->C(x,z)"]+(["x<=y->C(x,y)"] if precon else ["C(x,x)"])+(["C(x,y)->C(y,x)"] if sym else [])
  for o in A.operations.keys():
    if o in signum.keys(): compat += [signum[o]]
    elif type(A.operations[o])!=int: raise SyntaxError("Operation not handled")
  c=prover9(A.diagram("")+compat,[],100000,0,m,noniso=False)#, options=p9options)
  return frozenset([rel2pairs(x.relations["C"]) for x in c])

def precongruences(A):
  if type(A)==Model: return compatiblepreorders(A)
  return [compatiblepreorders(x) for x in A]

def congruences(A):
  if type(A)==Model: return frozenset(eqrel2partition(x) for x in compatiblepreorders(A,False,True))
  return [frozenset(eqrel2partition(x) for x in compatiblepreorders(y,False,True)) for y in A]

def poset2model(A):
    if len(A)==0: raise Error("Can't show Hasse diagram of an empty set")
    k = list(A)
    S = range(len(A))
    if all(type(x)==frozenset for x in k[0]): 
      U = union(k[0])
      if all(all(type(y)==frozenset for y in x) and union(x)==U for x in k[1:]): #assume K is a set of partitions
        li = [[all(any(x<=y for y in k[j]) for x in k[i]) for i in S] for j in S]
      else: li = [[k[i]<=k[j] for i in S] for j in S]
    else: li = [[k[i]<=k[j] for i in S] for j in S]
    return Model(cardinality=len(k),relations={"<=":li})

def show(K,ops=[]): # show a list of Mace4 models using graphviz or show a set of subsets or partitions
  if type(K)==Model: K=[K]
  if type(K)==list and len(K)>0 and type(K[0])==Model:
    print(ops)
    if ops==[]:
      if "<=" in K[0].relations.keys(): ops.append("<=d")
      if "^" in K[0].operations.keys(): ops.append("^d")
      if "v" in K[0].operations.keys(): ops.append("v")
      if "+" in K[0].operations.keys(): ops.append("+")
      if "*" in K[0].operations.keys(): ops.append("*d")
    else: ops=[la2p9[x.strip()] for x in ops]
    print(ops)
    st=" ".join(ops)
    m4diag(K,st)
  elif type(K)==frozenset: m4diag([poset2model(K)])
  elif type(K)==list: m4diag([poset2model(x) for x in K])

def check(structure,FOformula_list,info=False):
  FOformula_l=[FOformula_list] if type(FOformula_list)==str else FOformula_list
  for st in FOformula_l:
    lt = []
    if "<=" in st:
      if "+" in st: lt = ["x<=y <-> x+y=y"]
      if "*" in st: lt = ["x<=y <-> x*y=x"]
      if "v" in st: lt = ["x<=y <-> x v y=y"]
      if "^" in st: lt = ["x<=y <-> x^y=x"]
    li = prover9(structure.diagram("")+lt,[st],1000,0,structure.cardinality,one=True, options=p9options)
    if li!=[]:
      if info: return li+[st+" fails"]
      return False
  return True
