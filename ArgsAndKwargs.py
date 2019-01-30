def multiply_args(*args):
    print(args)
    for number in args:
        print(number)


multiply_args(2, 3, 4)


def multiply_kwargs(**kwargs):
    print(kwargs)
    print(kwargs["id"])


multiply_kwargs(id=1, name='John', age=22)
