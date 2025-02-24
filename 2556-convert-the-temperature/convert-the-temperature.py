class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        temp=[]
        kelvin = celsius+273.15
        temp.append(kelvin)
        faren = celsius *1.80+32.00
        temp.append(faren)
        return temp
         