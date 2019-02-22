
class permuteString:

    def permute(lst):
        if len(lst) == 0:
            return []
        elif len(lst) == 1:
            return [lst]
        else:
            li = []
            for i in range(len(lst)):
                x = lst[i]
                xs = lst[:i] + lst[i + 1:]
                for k in permuteString.permute(xs):
                    li.append([x] + k)
            return li


data = list('ABC')
# print(permute(data))
for p in permuteString.permute(data):
    print(p)
