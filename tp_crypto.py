from random import randint
def pgcd_rec(a, b):
    """ Returns pgcd of a and b recursively """
    if b == 0:
        return a
    else:
        return pgcd_rec(b, a % b)

def pgcd_iter(a, b):
    """ Returns pgcd of a and b iteratively """
    while b != 0:
        tmp = b
        b = a % b
        a = tmp
    return a


def euclide_ext(a, b):
    """ Extended euclide """
    if b == 0:
        return (1, 0)
    else:
        (u, v) = euclide_ext(b, a % b)
        return (v, u - (a // b) * v)

def inverse_modulaire(a, N):
    """ Modular inverse """
    (u,v) = euclide_ext(a,N)
    d = a*u + N*v
    return u

def expo_modulaire(e, b, n, showmultmod=False):
    """ Modular exponentation """
    if n == 1:
        return 0
        
    if e == 0:
        return 1

    res = 1
    while e > 0:
        res = (res * b) % n
        e = e - 1
    if showmultmod:
        print(f'{e} x et %')
    return res

def expo_modulaire_rapide(e, a, n, showmultmod=False):
    """ Rapid modular exponentiation """
    if n == 1:
        return 0

    p = 1
    count = 0
    for bit in format(e, 'b'):
        count += 1
        p = (p * p ) % n
        if bit == '1':
            p = (p * a) % n
            count += 1
    if showmultmod:
        print(f'{count} x et %')
    return p

# Question 6
def test_fermat(n, t):
    """ Fermat  primality test"""
    if t > n-1 :
        t = n-1
    for i in range(1,t):
        a = randint(1,n-1)
        if(expo_modulaire_rapide(n-1,a,n) != 1):
            return False
    return True
   
#Question 7
def pair_decomp(n):
    """ Rabin decomposition """
    r = 0
    tmp = n
    while tmp % 2 == 0:
        tmp = tmp // 2
        r = r + 1
    u = n // (2 ** r)
    return (r, u)
    
#Question 8
def temoin_rabin(a, n):
    """ Rabin proof """
    r,u = pair_decomp(n - 1)
    m = expo_modulaire_rapide(u, a, n)
    if m == 1 or m == n - 1:
        return False
    for i in range(1, r):
        if expo_modulaire_rapide(u * 2**i, a, n) == n - 1:
            return False
    return True

def test_rabin(n, t):
    """ Rabin primality test """
    if n == 2:
        return True
    if n % 2 == 0 or n == 1:
        return False
    for i in range(t):
        a = randint(1, n - 1)
        if pgcd_iter(a, n) != 1:
            return False
        if temoin_rabin(a, n):
            return False
    return True


# Question 9
def gen_prime(l):
    """ Generates prime number """
    x = randint(2**(l-1),2**l)
    if test_fermat(x,3000):
        if test_rabin(x,3000):
            #print(x)
            return x
        else:
            return gen_prime(l)
    else:
        return gen_prime(l)

def phi_prime(n):
    """ Generates prime number with phi """
    while True:
        num = randint(2, n)
        if pgcd_iter(num, n) == 1:
            return num

def gen_rsa(l):
    """ Generates key couple pk = n,e and sk = d """
    p, q = 0, 0
    
    while q == p :
        p = gen_prime(l//2)
        q = gen_prime(l - l // 2)

    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = phi_prime(phi)
    
    d = inverse_modulaire(e,phi)
    if d < 0 :
        d = d % phi
    
    return (n,e,d)

# Question 10
def enc_rsa(m,e,n):
    """ Encrypts message m using pk = n, e """
    return expo_modulaire_rapide(e, m, n)

def dec_rsa(c,d,n):
    """ Encrypts message c using sk = d, n """
    return expo_modulaire_rapide(d, c, n)

# Question 11
def str_to_int(m):
    s = 0
    b = 1
    for i in range(len(m)):
        s = s + ord(m[i])*b
        b = b * 256
    return s

def int_to_str(c):
    s = ""
    q,r = divmod(c,256)
    s = s+str(chr(r))
    while q != 0:
        q,r = divmod(q,256)
        s = s+str(chr(r))
    return s

# Question 12
def enc_example():
    """ Encryts example text message s """ 
    n, e, d = gen_rsa(512)
    s = "ceci est le message de la question 12"
    m = str_to_int(s)
    c = enc_rsa(m, e, n)
    msg_c = int_to_str(c)
    return msg_c, d, n

def verify_example(msg_c, d, n):
    """ Decrypts example text message """ 
    return int_to_str(dec_rsa(str_to_int(msg_c), d, n))


# Question 13
def prime_factors(n):
    """ Fucntion that helps to get the prime factors of a number n in an array"""
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def dec_example(c, e, N):
    """ Decrypts message c without knowing d """
    dvs = prime_factors(N)
    phi = (deviders[0] - 1) * (deviders[1] - 1)
    d = inverse_modulaire(e, phi) % phi
    m = expo_modulaire_rapide(d, c, N, False)
    return int_to_str(m)

# Question 14
def found_crypted_message():
    """ Found message crypted in the example """
    pk1 = (e1, N1) = (3910690008818283670868637293583807472406071014855467369376562453386568115118575549998307514095977446821904723128834716386012345019774749462224705453754125884105038313503535027306620172125186316567937615638323556850956880936518300302602805131676135113108484963880039142798231895843109891553380806740147280757, 69062688172064155658911250623824437247555723148603353738302253474984234478451724017342927200711212198561324986531605253193903441692089256620618833106961546429636445891984627695781384630013598341331689939178245781706540076751973610738227963889376714904403031694051296788833443496526885726775528827375948071929)
    pk2 = (e2, N2) = (50397573445568763030099703004373898485585249797981757548804415428108299083942229312259373614894595903577758246150442182256560679304788412233292957789570033238043365999611082606264134175517480208252580509041639010254535825802825318897321850834897940554139541328154602147460933321382694123780993639943682579161, 133996121506180462100555893114601434003049417003992050068931466928433702114247562694298268069726711436045516534210904716141897493553167880291439666527456807577995348332438299166875918790184716514217950877638447810365245678429514775529856742797659000032921952599049570889869462864202149565613900963189237850671)
    c = 24611251859812674169475796819303494911673745448473749394264526728162562685914074480537612941297670059801437381400024027253730653656476905281069179513708218469741624630326718738842101073851660606585444810976721216050363222115416379071737436541444450899126931955382088463221366246065910447241755253937828596484

    div = pgcd_iter(N1, N2)
    p, q = div, N1//div
    phi = (p-1)*(q-1)
    d = inverse_modulaire(e1,phi)
    print(int_to_str(dec_rsa(c,d,N1)))

# Question 15
def found_crypted_message1():
    """ Function that decrypt a message m crypted with 3 different keys"""
    pk1 = e1, N1 = (3,209972710381843986019222724306085916069)
    c1  = 98607549210059445213327744289011210961  # = M^3 mod N1
    pk2 = e2, N2 = (3, 205189342117195706999905843901134883221)
    c2  = 132884908601266001427764987011290838595 # = M^3 mod N2
    pk3 = e3, N3 = (3, 153796631843893344041809725352383124009)
    c3  = 143095419972589988082906041499952513358 # = M^3 mod N3
    
    # Chinese remainder theorem C = M^3 mod (n1*n2*n3)
    m1 = inverse_modulaire(N2*N3, N1)
    m2 = inverse_modulaire(N1*N3, N2)
    m3 = inverse_modulaire(N1*N2, N3)

    M3 = (c1*m1*N2*N3 + c2*m2*N1*N3 + c3*m3*N1*N2)%(N1*N2*N3)

    M = int(pow(M3, 1/3)) # M != C^(1/3) but we can get it easily
    while M *M *M < M3:
        M  += 1
    msg = int_to_str(M )
    print(msg)