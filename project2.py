#import np from numpy
def paye_avalie(A,d,C,penalties=None):
    Af=sum(A)
    df=sum(d)
    if Af<df:
        if penalties is None:
            raise Exception('A<d ast.penalties ra vared konid')
        new_A=A+[df - Af]
        new_C=C+[penalties]
        return new_A, d, new_C
    if Af>df:
        new_d=d+[Af-df]
        new_C=C+[[0 for _ in d]]
        return A,new_d,new_C
    return A,d,C
def makan(A,d):
    A_copy=A.copy()
    d_copy=d.copy()
    i=0
    j=0
    x_behine=[]
    while len(x_behine)<len(A)+len(d)-1:
        s=A_copy[i]
        dd= d_copy[j]
        vp=min(s,dd)
        A_copy[i]=A_copy[i]-vp
        d_copy[j]=d_copy[j]-vp
        x_behine.append(((i, j),vp))
        if A_copy[i]==0 and i<len(A)-1:
            i=i+1
        elif d_copy[j]==0 and j<len(d)-1:
            j=j+1
    return x_behine

def find_u_and_v(x_behine,C):
    u=[None]*len(C)
    v=[None]*len(C[0])
    u[0]=0
    x_behine_copy=x_behine.copy()
    while len(x_behine_copy)>0:
        for index,b in enumerate(x_behine_copy):
            i,j=b[0]
            if u[i] is None and v[j] is None: continue
            C=C[i][j]
            if u[i] is None:
                u[i]=C-v[j]
            else:
                v[j]=C-u[i]
            x_behine_copy.pop(index)
            break
    return u,v
def find_w(x_behine,C,u,v):
    w=[]
    for i, row in enumerate(C):
        for j,C in enumerate(row):
            napaye=all([p[0]!=i or p[1]!=j for p,vp in x_behine])
            if napaye:
                w.append(((i,j),u[i]+v[j]-C))
    return w
def sharte_edame_algorithm(w):
    for p,vp in w:
        if vp>0:
            return True
    return False
def vared_shavande(w):
    w_copy=w.copy()
    w_copy.sort(key=lambda k:k[1])
    return w_copy[-1][0]
def find_x_prime(loop,s):
    gereh_akhar=loop[-1]
    radif=[n for n in s if n[0]==gereh_akhar[0]]
    soton=[n for n in s if n[1]==gereh_akhar[1]]
    if len(loop)<2:
        return radif+soton
    else:
        gereh=loop[-2]
        rradif=gereh[0]==gereh_akhar[0]
        if rradif:
            return soton
        return radif
def halghe(a,g):
    def halghe_prime(loop):
        if len(loop)>3:
            Eend=len(find_x_prime(loop,[g]))==1
            if Eend:
                return loop
        z=list(set(a)-set(loop))
        x_prime=find_x_prime(loop,z)
        for item in x_prime:
            looop=halghe_prime(loop+[item])
            if looop:
                return looop
    return halghe_prime([g])
def mehvar(x_behine,loop):
    zojha=loop[0::2]
    fardha=loop[1::2]
    get_b=lambda pos:next(vp for p,vp in x_behine if p==pos)
    m=sorted(fardha,key=get_b)[0]
    khoroji=get_b(m)
    new_x_behine=[]
    for p,vp in [b for b in x_behine if b[0]!=m]+[(loop[0],0)]:
        if p in zojha:
            vp=vp+khoroji
        elif p in fardha:
            vp=vp-khoroji
        new_x_behine.append((p,vp))
    return new_x_behine
def simplex(A,d,C,penalties=None):
    A_behine,d_behine,C_behine=paye_avalie(A,d,C)
    def sim2(x_behine):
        u,v=find_u_and_v(x_behine,C_behine)
        w=find_w(x_behine,C_behine,u,v)
        if sharte_edame_algorithm(w):
            g=vared_shavande(w)
            loop=halghe([p for p,vp in x_behine],g)
            return sim2(mehvar(x_behine,loop))
        return x_behine
    paye=sim2(makan(A_behine,d_behine))
    Final=np.zeros((len(C),len(C[0])))
    for (i,j), vp in paye:
        Final[i][j]=vp
    return Final
def min_tabe_avalie(C,Final):
    solution=0
    for i,row in enumerate(C):
        for j,C in enumerate(row):
            solution=solution+C*Final[i][j]
    return solution
