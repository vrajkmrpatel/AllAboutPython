s = 'aaaabbbcccdeeefffffffgggggghjjjjukimnopqrstuvwxiytrlozrq'

dic = {}
for c in s:
      if c in dic.keys():
            dic[c] = dic[c] + 1
      else :
            dic[c] = 1
for k,v in sorted(dic.items()):
      print("{} = {} times".format(k,v))