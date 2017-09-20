
def cached(cache=None):
    cache = cache or dict()
    def wrap(func):
        def args(*args, **kwargs):
            if args not in cache:
                cache[args] = func(*args, **kwargs)
            return cache.get(args)
        return args
    return wrap
