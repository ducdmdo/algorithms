def get_fib(position):
    if position == 0:
        return position
        print ("position = 0")
    if position == 1:
        return position
        print ("position = 1")

    print ("position is at %s" % position)
    result = get_fib(position-1) + get_fib(position-2)
    return result

print (get_fib(8))


