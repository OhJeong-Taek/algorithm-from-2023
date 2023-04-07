# my answer
def solution(s):
    ans = 0
    for ch in s:
        if ch == '(':
            ans += 1
        else:
            ans -= 1
        if ans < 0:
            return False

    if ans == 0:
        return True
    else:
        return False
    
    # try - except version
    def is_pair(s):
    st = list()
    for c in s:
        if c == '(':
            st.append(c)

        if c == ')':
            try:
                st.pop()
            except IndexError:
                return False

    return len(st) == 0
