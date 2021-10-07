"""
2018-腾讯—在线编程题
给定一个正整数，编写程序计算有多少对质数的和等于输入的这个正整数，并输出结果，输入值小于1000

Tips:输入的值 3<= n < 1000
"""
num = int(input("Please enter a num between 3 and 100 >>> "))

def isPrime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
        else:
            return True

prime_list = [i for i in range(2,num) if isPrime(i)]
print(prime_list)
prime_count = 0
for item in prime_list:
    if (num - item) in prime_list and item <= num - item:
        prime_count += 1
print(prime_count)