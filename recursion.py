# -*- coding: utf-8 -*-
"""
Created on Wed May 28 16:20:18 2025

@author: hp
"""
# Program of a factorial of a number using recursion
def factorial(n):
    if n == 0:
       return 1
    else:
       return n * factorial(n - 1)
#print(factorial(4))

# Program of fibonacci sequence using recursion
def fibonacci(n):
    if n == 0:
     return 0
    elif n == 1:
     return 1
    else:
     return fibonacci(n - 1) + fibonacci(n - 2)
#print(fibonacci(4))


def reverse_string(s):
    if len(s) <= 1:
       return s[0]
    else:
      return reverse_string(s[1:]) + s[0]


def sum_of_digits(n):
   if n < 10:
      return n # Base case
   else:
      return n % 10 + sum_of_digits(n // 10) 

def tower_of_hanoi(n,from_source ,to_destination,via):
    if n == 1:
       print(f"Move disk 1 from {from_source} to {to_destination}")
       
    else:
        tower_of_hanoi(n-1,from_source,via,to_destination)
        print(f"Move disk {n} from {from_source} to {to_destination}")
        tower_of_hanoi(n-1,via,to_destination,from_source)
        
#print(tower_of_hanoi(1,'A','B','C'))

def decimal_to_binary(n):
    if n == 0:
       return ""
    else:
       return decimal_to_binary(n//2)+ str(n%2)
      
#print(decimal_to_binary(5))

def hcf(a,b):
    if  b==0:
       return a
    else:
       return hcf(b,a%b)

#print(hcf(6,7))

def lcm(a,b):
    if a==0 or b==0:
       return 0
    else:
       return  (a*b)//hcf(a,b)
 
#print(lcm(6,7))


def subsets(num,index=0,result=[],current=[]):
    if index == len(num):
       result.append(current[:])
       
    else:
       subsets(num,index+1,result,current)
       
       current.append(num[index])
       subsets(num,index+1,result,current)
       current.pop()
      
    return result

print(subsets([1,2,3]))
       
def length_of_list(arr):
    if arr==[]:
       return 0
    else: 
        return 1+length_of_list(arr[1:])
 
digits=1234
def sum_digit(digits):
    if digits == 0:
       return 0
    else:
       return digits%10 + sum_digit(digits//10)
        
print(sum_digit(digits))       








