  class Solution:
      def my_roman_numerals_converter(self,num):
          number_dict = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}
          answer,i = "",0
          while num > 0:
              for _ in range(num //list(number_dict.keys())[::-1][i]):
                  answer += list(number_dict.values())[::-1][i]
                  num -= list(number_dict.keys())[::-1][i]
              i += 1
          return answer
 
