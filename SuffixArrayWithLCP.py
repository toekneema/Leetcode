class SuffixArray:
    def __init__(self, s):
        self.s = s
        self.sa = self.build_sa(s)
        self.lcp = self.build_lcp(s, self.sa)

    @staticmethod
    def count_sort(k, sa, ra):
        n = len(sa)
        N = n + 256
        nsa = [i for i in sa]
        cnt = [0] * N
        for i in range(n):
            cnt[ra[i]] += 1
            nsa[i] = (nsa[i] + n - k) % n
        for i in range(1, N):
            cnt[i] += cnt[i - 1]
        for i in reversed(range(n)):
            cnt[ra[nsa[i]]] -= 1
            sa[cnt[ra[nsa[i]]]] = nsa[i]

    def build_sa(self, s):
        s = s + '$'
        deque = collections.deque(self.__build_sa(s))
        deque.popleft()
        return list(deque)

    def __build_sa(self, s):
        n = len(s)
        sa, ra = [0] * n, [0] * n
        for (index, value) in enumerate(s):
            sa[index] = index
            ra[index] = ord(value)
        k = 0
        while k < n:
            nra = [0] * n
            self.count_sort(k, sa, ra)
            r = 0
            for i in range(1, n):
                if ra[sa[i]] != ra[sa[i - 1]] or ra[(sa[i] + k) % n] != ra[(sa[i - 1] + k) % n]:
                    r += 1
                nra[sa[i]] = r
            if k != 0:
                k <<= 1
            else:
                k += 1
            ra = nra
        return sa

    @staticmethod
    def build_lcp(s, sa):
        n = len(s)
        lcp, ra = [0] * (n-1), [0] * n
        for i in range(n):
            ra[sa[i]] = i
        k = 0
        for i in range(n):
            if ra[i] == n - 1:
                k = 0
                continue
            j = sa[ra[i] + 1]
            while i + k < n and j + k < n and s[i + k] == s[j + k]:
                k += 1
            lcp[ra[i]] = k
            if k > 0:
                k -= 1
        l = [0]
        l.extend(lcp)
        return l