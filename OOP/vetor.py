class Vector:
    def __init__(self, **coords):
        private_coords = {'_' + k: v for k, v in coords.items()}
        self.__dict__.update(private_coords)

    def __getattr__(self, name):
        private_name = '_' + name 
        try:
            return self.__dict__[private_name]
        except KeyError:
            raise AttributeError('{!r} object has no attribute {!r}'.format(self.__class__, name))

    def __setattr__(self, name, value):
        raise AttributeError("Can't set attribute {!r}".format(name))

    def __delattr__(self, name):
        raise AttributeError("Can't delete attribute {!r}".format(name))

    def __repr__(self):
        return '{} ({})'.format(
                self.__class__.__name__,
                ', '.join('{k}={v}'.format(
                        k=k,
                        v=self.__dict__[k]
                    )
                        for k in sorted(self.__dict__.keys())
                )
            )
# >>> from vetor import Vector
# >>> v = Vector(x=1,y=2)
# >>> print(v)