function n(t, e) {
    function r(t, e) {
        var r = "";
        if ("object" == typeof t)
            for (var n = 0; n < t.length; n++)
                r += String.fromCharCode(t[n]);
        t = r || t;
        for (var i, o, a = new Uint8Array(t.length), s = e.length, n = 0; n < t.length; n++)
            o = n % s,
            i = t[n],
            i = i.toString().charCodeAt(0),
            a[n] = i ^ e.charCodeAt(o);
        return a
    }

    function n(t) {
        var e = "";
        if ("object" == typeof t)
            for (var r = 0; r < t.length; r++)
                e += String.fromCharCode(t[r]);
        t = e || t;
        var n = new Uint8Array(t.length);
        for (r = 0; r < t.length; r++)
            n[r] = t[r].toString().charCodeAt(0);
        var i, o, r = 0;
        for (r = 0; r < n.length; r++)
            0 != (i = n[r] % 3) && r + i < n.length && (o = n[r + 1],
                n[r + 1] = n[r + i],
                n[r + i] = o,
                r = r + i + 1);
        return n
    }

    function i(t) {
        var e = "";
        if ("object" == typeof t)
            for (var r = 0; r < t.length; r++)
                e += String.fromCharCode(t[r]);
        t = e || t;
        var n = new Uint8Array(t.length);
        for (r = 0; r < t.length; r++)
            n[r] = t[r].toString().charCodeAt(0);
        var r = 0,
            i = 0,
            o = 0,
            a = 0;
        for (r = 0; r < n.length; r++)
            o = n[r] % 2,
            o && r++,
            a++;
        var s = new Uint8Array(a);
        for (r = 0; r < n.length; r++)
            o = n[r] % 2,
            s[i++] = o ? n[r++] : n[r];
        return s
    }

    function o(t, e) {
        var r = 0,
            n = 0,
            i = 0,
            o = 0,
            a = "";
        if ("object" == typeof t)
            for (var r = 0; r < t.length; r++)
                a += String.fromCharCode(t[r]);
        t = a || t;
        var s = new Uint8Array(t.length);
        for (r = 0; r < t.length; r++)
            s[r] = t[r].toString().charCodeAt(0);

        for (r = 0; r < t.length; r++) {
            if (0 != (o = s[r] % 5) && 1 != o && r + o < s.length && (i = s[r + 1],
                    n = r + 2,
                    s[r + 1] = s[r + o],
                    s[o + r] = i,
                    (r = r + o + 1) - 2 > n)) {
                for (; n < r - 2; n++) {
                    s[n] = s[n] ^ e.charCodeAt(n % e.length)
                }
            }
        }
        for (r = 0; r < t.length; r++)
            s[r] = s[r] ^ e.charCodeAt(r % e.length);

        return s
    }
    for (var a = {
            data: {
                info: t
            }
        }, s = {
            q: r,
            h: n,
            m: i,
            k: o
        }, l = a.data.info, u = l.substring(l.length - 4).split(""), c = 0; c < u.length; c++)
        u[c] = u[c].toString().charCodeAt(0) % 4;
    u.reverse();
    for (var d = [], c = 0; c < u.length; c++)
        d.push(l.substring(u[c] + 1, u[c] + 2)),
        l = l.substring(0, u[c] + 1) + l.substring(u[c] + 2);
    a.data.encrypt_table = d,
        a.data.key_table = [];
    for (var c in a.data.encrypt_table)
        "q" != a.data.encrypt_table[c] && "k" != a.data.encrypt_table[c] || (a.data.key_table.push(l.substring(l.length - 12)),
            l = l.substring(0, l.length - 12));
    a.data.key_table.reverse(),
        a.data.info = l;
    var f = new Array(-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 62, -1, -1, -1, 63, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, -1, -1, -1, -1, -1, -1, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, -1, -1, -1, -1, -1, -1, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, -1, -1, -1, -1, -1);
    a.data.info = function(t) {
        var e, r, n, i, o, a, s;
        for (a = t.length,
            o = 0,
            s = ""; o < a;) {
            do {
                e = f[255 & t.charCodeAt(o++)]
            } while (o < a && -1 == e);
            if (-1 == e)
                break;
            do {
                r = f[255 & t.charCodeAt(o++)]
            } while (o < a && -1 == r);
            if (-1 == r)
                break;
            s += String.fromCharCode(e << 2 | (48 & r) >> 4);
            do {
                if (61 == (n = 255 & t.charCodeAt(o++)))
                    return s;
                n = f[n]
            } while (o < a && -1 == n);
            if (-1 == n)
                break;
            s += String.fromCharCode((15 & r) << 4 | (60 & n) >> 2);
            do {
                if (61 == (i = 255 & t.charCodeAt(o++)))
                    return s;
                i = f[i]
            } while (o < a && -1 == i);
            if (-1 == i)
                break;
            s += String.fromCharCode((3 & n) << 6 | i)
        }
        return s
    }(a.data.info);
    for (var c in a.data.encrypt_table) {
        var h = a.data.encrypt_table[c];
        if ("q" == h || "k" == h) {
            var p = a.data.key_table.pop();
            a.data.info = s[a.data.encrypt_table[c]](a.data.info, p)
        } else{
            a.data.info = s[a.data.encrypt_table[c]](a.data.info)
            }
    }
    if (e)
        return a.data.info;
    var g = "";
    for (c = 0; c < a.data.info.length; c++)
        g += String.fromCharCode(a.data.info[c]);
    return g
}


a = n("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xdiB2fsi87d0")
console.log(a)