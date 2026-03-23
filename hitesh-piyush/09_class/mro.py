class A:
    label = "Base Chai"
class B(A):
    label = "Masala Chai"
class C(A):
    label = "Elaichi Chai"

# The attribute will resolve from first class only
class D(B, C):
    pass

cup = D()
print(cup.label)
print(D.__mro__)
