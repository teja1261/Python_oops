import math

class ComplexNumber:
    
    def __init__(self, real_part=0, imaginary_part=0):
        self._real_part = 0
        self._imaginary_part = 0
        
        if type(imaginary_part) == str and type(real_part) == str:
            raise ValueError("Invalid value for real and imaginary part")
        
        if type(real_part) == str:
            raise ValueError("Invalid value for real part")
        else:
            self._real_part = real_part
        
        if type(imaginary_part) == str:
            raise ValueError("Invalid value for imaginary part")
        else:
            self._imaginary_part = imaginary_part
            
        
    def conjugate(self):
            return ComplexNumber(self._real_part,-self._imaginary_part)
            
    def __str__(self):
        return '{}+{}i'.format(self._real_part,self._imaginary_part)
        
    def __add__(self,other):
        add_real = self._real_part + other._real_part
        add_imag = self._imaginary_part + other._imaginary_part
        return ComplexNumber(add_real,add_imag)
        
    def __sub__(self,other):
        sub_real = self._real_part - other._real_part
        sub_imag = self._imaginary_part - other._imaginary_part
        return __class__(sub_real,sub_imag)
                    #OR
        #return ComplexNumber(sub_real,sub_imag)
        
    def __mul__(self,other):
        mul_real = (self._real_part * other._real_part) - (self._imaginary_part * other._imaginary_part)
        mul_imag = (self._real_part * other._imaginary_part) + (other._real_part * self._imaginary_part)
        return __class__(mul_real, mul_imag)
        
    def __truediv__(self,other):
        if other._real_part == 0 and other._imaginary_part == 0:
            raise ZeroDivisionError("division by zero")
        
        div_real = complex(self._real_part,self._imaginary_part)
        div_imag = complex(other._real_part, other._imaginary_part)
        division = div_real / div_imag
        return __class__(division.real, division.imag)
        
    def __abs__(self):
        absolute_value = math.sqrt(self._real_part ** 2 + self._imaginary_part ** 2)
        return (round(absolute_value, 3))
        
    def __eq__(self,other):
        return (self._real_part == other._real_part) and (self._imaginary_part == other._imaginary_part)

    @property
    def real_part(self):
        return self._real_part
        
    @property
    def imaginary_part(self):
        return self._imaginary_part