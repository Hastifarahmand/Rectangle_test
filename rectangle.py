class Rectangle:
    _width=10
    _length=0
    def get_width(self):
        return self._width
    def set_width(self,width):
        if width<=0 :
            raise ValueError("with should be positive")
        else:
            self._width=width 
    def get_length(self):
        return self._length
    def set_length(self,length):
        if length<=0:
            raise ValueError("With should be positive")
        else:
            self._length=length
    width=property(get_width,set_width)
    length=property(get_length,set_length)
r1=Rectangle()
r1.width=4
print(r1.width)
r1=Rectangle()
r1.length=7
print(r1.width)
# r1.length=-3

