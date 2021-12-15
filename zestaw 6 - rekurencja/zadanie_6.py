def main_f(t):
    def rek(tab, new_tab, s=0, s_id=0, p=0, best=999999999, best_s=0, b_tab=[]):

        if p >= len(tab):
            if s == s_id and s_id != 0:
                return len(new_tab), s_id, new_tab
            return 99999999999999999, -1, []

        length1, ans1, t1 = rek(tab, new_tab + [tab[p]], s + tab[p], s_id + p, p + 1)
        if length1 < best:
            best_s = ans1
            best = length1
            b_tab = t1
        length1, ans1, t1 = rek(tab, new_tab, s, s_id, p + 1)
        if length1 < best:
            best_s = ans1
            best = length1
            b_tab = t1
        return best, best_s, b_tab
    _, x, _ = rek(t, [])
    return x

print(main_f([1,7,3,5,11,2]))