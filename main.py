def qoshish(a, b):
    return a + b

def ayirish(a, b):
    return a - b

def kopaytirish(a, b):
    return a * b

def bolish(a, b):
    if b != 0:
        return a / b
    return "0 ga bo‘lib bo‘lmaydi"

# iwlatiw

import matematik

print(matematik.qoshish(10, 5))
print(matematik.ayirish(10, 5))
print(matematik.kopaytirish(10, 5))
print(matematik.bolish(10, 5))
