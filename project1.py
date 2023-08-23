from numpy.linalg import matrix_rank
andis_paye=[]
def soton_mostaghel(dim,M):
    LI=[M[0]]
    for i in range(dim):
        tmp=[]
        for r in LI:
            tmp.append(r)
        tmp.append(M[i])
        if matrix_rank(tmp)>len(LI):
            LI.append(M[i])
            andis_paye.append(i)
    return LI
def maakoos(mat):
    return numpy.linalg.inv(mat)
def X(matB,matb):
    a=0
    x=[]
    for i in range(dim):
        x.append(0)
    matBmaakoos=[]
    matBmaakoos=maakoos(matB)
    for i in range(dim):
        for j in range(dim):
            a=a+matB[i][j]+matb[j]
        x[andis_paye[i]].append(a)
    return x

def cB():
    cB=[]
    for item in andis_paye:
        cB.append(c[andis_paye])
    return cB
def taranahade(mat):
    result=[]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            result[j][i] = mat[i][j]
    return result

def zarb_mat(A,B):
    result=[]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

matA=[]
matB=[]
dim=int(input("lotfan dim matris ra vared konid"))
for i in range(dim):
    matA.append([])
    matB.append([])
for i in range(dim):
    for j in range(dim):
        matA[i].append(int(input("onsore",j," ome satre",i," om matris A vared konid")))
matb=[]
for i in range(dim):
    matb.append(int(input("lotfan onsore",i," om matris b ra vared konid")))
matB=soton_mostaghel(dim,matA)
print("matris paye avalie:",matB)
print("andis haye javab haye paye:",andis_paye)
c=[]
for i in range(dim):
    c.append(int(input("lotfan onsore",i," om matris hazine ra vared konid")))
p_taranahade=zarb_mat(taranahade(cB(),maakoos(matB)))
c_bar=[]
for i in range(dim):
    c_bar[i].append(c[i]-(p_taranahade*matA[i]))
n=0
m=0
j_valid=[]
for i in range (len(c_bar)):
    if c_bar[i]<0:
        n=n+1
        j_valid.append(i)
u=[]
u_valid=[]
teta=[]
teta_star=0
andis_valid=[]
k=0
x_behine=X(matB,matb)
while 1>0:
    if n==0:
        print("javabe behine ma",X(matB,matb),"ast")
    else:
        u=zarb_mat(maakoos(matB),matA[j_valid[0]])
        for i in range (len(u)):
            if u[i]>0:
                m=m+1
                u_valid.append(u[i])
                andis_valid.append(i)
        if m==0:
            print("javabe behine menhaye binaayat ast")
        else:
            for i in range (len(u_valid)):
                teta.append(x_behine[andis_paye[i]]/u_valid[i])
            for item in teta:
                for iitem in teta:
                    teta_star=min(item,iitem)
                    k=teta.index(teta_star)
            for i in range(dim):
                matB[i][k]=matA[i][j_valid]
            y=x_behine
            y[j_valid]=teta_star
            for i in len(u):
                y[andis_paye[i]]=x[andis_paye[i]]-(teta_star*u[i])
