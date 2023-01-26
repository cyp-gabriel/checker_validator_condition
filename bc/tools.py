def curry1(fn):
    def first(arg):
        return fn(arg)
    return first

def curry2(fn):
    def second(secondArg):
        def first(firstArg):
            return fn(firstArg, secondArg)
        return first
    return second

def retarg(arg):
    return arg

_identity = curry1(retarg)


def validator(msg, fn):
    """Encapsulates a condition and a predicate function.

    Args:
        msg (str): error message applying to case when argument fn returns false.
        fn (function): predicate function that represents the condition
    """
    def inner(*args):
        return fn(*args)
    
    f = inner
    f.msg = msg
    return f

def checker(*args):
    validators = args
    def inner(obj):
        # errs = []
        # for v in validators:
        #     if v(obj):
        #         errs.append(v.msg)
        errs = [v.msg for v in validators if not v(obj)]
        return errs
    return inner

def condition(*args):
    validators = args
    
    def inner(fn, arg):
        errs = [v.msg for v in validators if not v(arg)]
        if len(errs) > 0:
            raise Exception('; '.join(errs))
        return fn(arg)
    
    return inner
