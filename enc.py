def n(t, e):
    def r(t, e):
        r = ""
        if type(t) == dict or type(t) == list:
            for n in range(0,len(t)):
                r += chr(t[n])
        t = r or t
        a = [0 for i in range(len(t))]
        s = len(e)
        for n in range(0,len(t)):
            o = n % s
            i = t[n]
            i = ord(str(i)[0])
            a[n] = i ^ ord(e[o])
        return a
    
    def n(t):
        # print(t)
        e = ""
        if type(t) == dict or type(t) == list:
            for r in range(0,len(t)):
                e += chr(t[r])
        t = e or t;
        n = [0 for i in range(len(t))]
        for r in range(0,len(t)):
            n[r] = ord(str(t[r])[0])
        i, o, r = 0,0,0
        while r < len(n):
            i = n[r] % 3
            if 0 != i:
                if  r + i < len(n):
                    o = n[r + 1]
                    n[r + 1] = n[r + i]
                    n[r + i] = o
                    r = r + i + 1
            r += 1
        return n


    def i(t):
        e = ""
        if type(t) == dict or type(t) == list:
            for r in range(0,len(t)):
                e += chr(t[r])
        t = e or t;
        n = [0 for i in range(len(t))]
        for r in range(0,len(t)):
            n[r] = ord(str(t[r])[0])
        r = 0
        i = 0
        o = 0
        a = 0
        while r <len(n):
            o = n[r] % 2
            if o:
                r += 1
            a += 1
            r += 1

        s = [0 for i in range(a)]
        r = 0
        while r < len(n):
            o = n[r] % 2
            if o:
                s[i] = n[r]
                i+=1
                r+=1
            else:    
                s[i] = n[r]
                i+=1
            r += 1

        return s
    
    def o(t, e):
        # print(t,e)
        r = 0
        n = 0
        i = 0
        o = 0
        a = ""
        if type(t) == dict or type(t) == list:
            for r in range(0,len(t)):
                a += chr(t[r])        
        t = a or t
        s = [0 for i in range(len(t))]
        for r in range(0,len(t)):
            s[r] = ord(str(t[r])[0])

        r = 0
        while r< len(t):
            o = s[r] % 5
            if 0 != o:
                if 1 != o and r + o < len(s):
                    i = s[r + 1]
                    n = r + 2
                    s[r + 1] = s[r + o]
                    s[o + r] = i
                    r = r + o + 1
                    if r - 2 > n:
                        while n< r - 2:
                            s[n] = s[n] ^ ord(e[(n % len(e))])
                            n += 1    
            r += 1

        for r in range(0,len(t)):
            s[r] = s[r] ^ ord(e[r % len(e)])
        return s
    

    a = {'data':{'info':t}}
    s = {
            'q': r,
            'h': n,
            'm': i,
            'k': o
        }
    l = a['data']['info']
    u = list(l[len(l)-4:])
    for c in range(0,len(u)):
        u[c] = ord(str(u[c])[0]) % 4
    u = u[::-1]
    d = []
    for c in range(0,len(u)):
        d.append(l[u[c]+1:u[c]+2])

        l = l[0:u[c] + 1] + l[u[c] + 2:]
    a['data']['encrypt_table'] = d
    a['data']['key_table'] = []
    for index,c in enumerate(a['data']['encrypt_table']):
        # print(c)
        if "q" != a['data']['encrypt_table'][index] and "k" != a['data']['encrypt_table'][index]:
            pass
        else:
            a['data']['key_table'].append(l[len(l) - 12:])
            l = l[0:len(l) - 12]

    a['data']['key_table'] = a['data']['key_table'][::-1]
    a['data']['info'] = l
    f = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 62, -1, -1, -1, 63, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, -1, -1, -1, -1, -1, -1, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, -1, -1, -1, -1, -1, -1, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, -1, -1, -1, -1, -1]
    def niming(t):
        # var e, r, n, i, o, a, s;
        a = len(t)
        o = 0
        s = ""
        n= 0
        while o < a:
            while True:
                e = f[255 & ord(t[o])]
                o+=1
                if not (o < a and -1 == e):
                    break
            if (-1 == e):
                break   
            while True:
                r = f[255 & ord(t[o])]
                o+=1
                if not (o < a and -1 == r):
                    break
            if (-1 == r):
                break
            s += chr(e << 2 | (48 & r) >> 4);
            while True:
                n = 255 & ord(t[o])
                o += 1
                if (61 == n):
                    return s;
                n = f[n]
                if not (o < a and -1 == n):
                    break
            if (-1 == n):
                break   
            s += chr((15 & r) << 4 | (60 & n) >> 2)
            while True:
                i = 255 & ord(t[o])
                o+=1
                if (61 == i):
                    return s;
                i = f[i]
                if not (o < a and -1 == i):
                    break
            if (-1 == i):
                break
            s += chr((3 & n) << 6 | i)
        return s

    a['data']['info'] = niming(a['data']['info'])
    for index,c in enumerate(a['data']['encrypt_table']):
        # print(index)
        h = a['data']['encrypt_table'][index]
        if ("q" == h or "k" == h):
            p = a['data']['key_table'].pop()
            a['data']['info'] = s[a['data']['encrypt_table'][index]](a['data']['info'],p)
        else:
            a['data']['info'] = s[a['data']['encrypt_table'][index]](a['data']['info'])
    
    if e:
        return bytes(bytearray(a['data']['info']))
    g = ""
    for c in range(0,len(a['data']['info'])):
        g += chr(a['data']['info'][c])
    return g

if __name__ == '__main__':

    str_ = "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3XBBkdwjSzP4"
    print(n(str_,''))