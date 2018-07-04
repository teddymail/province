# s = set([])
# print 's:', s
# s.add(1)
# s.add(2)
# s.add(3)
# s.add(2)
# print s
# for num in s:
#     print(num)

# '''
# http://www.lawtime.cn/fayuan/city/hefei
# http://www.lawtime.cn/fayuan/city/p1/hefei
# '''
#
# hf = 'http://www.lawtime.cn/fayuan/city/hefei'
# li = hf.split('/')
# print li
# new_hf = 'http://www.lawtime.cn/fayuan/city/p1/' + li[-1]
# print new_hf

wrong_list = ['http://www.lawtime.cn/fayuan/province/ganshu', 'http://www.lawtime.cn/fayuan/province/beijing',
                      'http://www.lawtime.cn/fayuan/province/chongqing', 'http://www.lawtime.cn/fayuan/province/shanghai',
                      'http://www.lawtime.cn/fayuan/province/tianjin']
wrong = 'http://www.lawtime.cn/fayuan/province/ganshu'
if wrong in wrong_list:
    print 'ok'