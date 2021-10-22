class Sol:
    def matrix_score(self,str1,str2):
        dif1,dif2=[],[]
        if len(str1)!=len(str2):
            return False
        for i in range(len(str1)):
            if str1[i]!=str2[i] and len(dif1)==2:
                return False
            elif str1[i]!=str2[i]:
                dif1.append(str1[i])
                dif2.append(str2[i])
        if len(dif1)==2:
            return dif1[::-1]==dif2
        elif len(dif1)==1:
            return False
        return len(set(str1))!=len(str1)

if __name__ == '__main__':
    p = Sol()
    print(p.matrix_score(str1='aaaaaaabc', str2='aaaaaaacb'))
    print(p.matrix_score(str1='ab', str2='ab'))
