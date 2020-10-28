from atexit import register


@register
def f():
    print("F is called")
    
# register(f)

nb=12 * 3

print(nb)
print("The end")
