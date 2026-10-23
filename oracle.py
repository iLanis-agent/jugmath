import json, random
def dec(n, p=2):
    b = 10**p
    w, f = divmod(n, b)
    fs = str(f).zfill(p).rstrip("0")
    return str(w) + "." + fs if fs else str(w)
def m(n): return f"{n//100}.{str(n%100).zfill(2)}"
def pl(n, one, many): return f"{n}" + (one if n == 1 else many)
def v(n, one, many): return one if n == 1 else many
def bundles(n, b):
    k = -(-n//b)
    return f"The {pl(n,' jug',' jugs')} at {pl(b,' jug',' jugs')} a bundle {v(n,'takes','take')} {pl(k,' bundle',' bundles')}, the last bundle holding {pl(n-(k-1)*b,' jug',' jugs')}."
def weeks(n, w):
    k = n//w
    return f"The {pl(n,' jug',' jugs')} at {pl(w,' jug',' jugs')} a week {v(n,'lasts','last')} {pl(k,' full week',' full weeks')} with {pl(n-k*w,' jug',' jugs')} left for the next week."
def cost(b, pc, n):
    cc = b*pc
    pb = (2*cc + n)//(2*n)
    return f"The {pl(b,' bundle',' bundles')} at ${m(pc)} a bundle {v(b,'comes','come')} to ${m(cc)}, ${m(pb)} a jug."
def time_(n, pm):
    t = -(-n//pm); h, r = t//60, t%60
    return f"The {pl(n,' jug',' jugs')} at {pl(pm,' jug',' jugs')} a minute {v(n,'takes','take')} {pl(t,' minute',' minutes')}, {pl(h,' hour',' hours')} {pl(r,' minute',' minutes')}."
random.seed(786)
R = random.randint
cases = [
 dict(fn="bundles", args=["520","6"], expect=bundles(520,6)),
 dict(fn="weeks", args=["520","45"], expect=weeks(520,45)),
 dict(fn="cost", args=["87","18.50","520"], expect=cost(87,1850,520)),
 dict(fn="time", args=["520","8"], expect=time_(520,8)),
 dict(fn="bundles", args=["1","1"], expect=bundles(1,1)),
 dict(fn="bundles", args=["516","6"], expect=bundles(516,6)),
 dict(fn="bundles", args=["1000000","1000"], expect=bundles(1000000,1000)),
 dict(fn="weeks", args=["1","1"], expect=weeks(1,1)),
 dict(fn="weeks", args=["495","45"], expect=weeks(495,45)),
 dict(fn="weeks", args=["1000000","100000"], expect=weeks(1000000,100000)),
 dict(fn="cost", args=["1","0.01","1"], expect=cost(1,1,1)),
 dict(fn="cost", args=["100000","999.99","1000000"], expect=cost(100000,99999,1000000)),
 dict(fn="time", args=["1","1"], expect=time_(1,1)),
 dict(fn="time", args=["60","1"], expect=time_(60,1)),
 dict(fn="time", args=["1000000","100"], expect=time_(1000000,100)),
]
for _ in range(20):
    n,b=R(1,1000000),R(1,1000); cases.append(dict(fn="bundles", args=[str(n),str(b)], expect=bundles(n,b)))
for _ in range(20):
    n,w=R(1,1000000),R(1,100000); cases.append(dict(fn="weeks", args=[str(n),str(w)], expect=weeks(n,w)))
for _ in range(25):
    b,p,n=R(1,100000),R(1,99999),R(1,1000000); cases.append(dict(fn="cost", args=[str(b),dec(p),str(n)], expect=cost(b,p,n)))
for _ in range(19):
    n,m=R(1,1000000),R(1,100); cases.append(dict(fn="time", args=[str(n),str(m)], expect=time_(n,m)))
errs=[["bundles",["0","6"]],["bundles",["1000001","6"]],["bundles",["2.5","6"]],["bundles",["520","0"]],["bundles",["520","1001"]],
 ["weeks",["0","45"]],["weeks",["520","0"]],["weeks",["520","100001"]],["weeks",["520","1.5"]],["weeks",["1000001","45"]],
 ["cost",["0","18.50","520"]],["cost",["100001","18.50","520"]],["cost",["87","0","520"]],["cost",["87","18.505","520"]],["cost",["87","18.50","0"]],
 ["time",["0","8"]],["time",["520","0"]],["time",["520","101"]],["time",["520","6.5"]],["time",["1000001","5"]]]
json.dump(dict(cases=cases, errors=errs), open("expected.json","w"), indent=1)
print(len(cases),"cases,",len(errs),"errcases")
