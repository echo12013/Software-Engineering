import math

def is_prime(n):
    """判断一个数是否为素数"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    primes = []
    count = 0
    
    # 找出1~20000内的所有素数
    for num in range(1, 20001):
        if is_prime(num):
            primes.append(num)
            count += 1
    
    # 按每行5个打印
    for i in range(0, len(primes), 5):
        line = primes[i:i + 5]
        print(" ".join(f"{p:6d}" for p in line))
    
    print(f"\n总共找到 {count} 个素数")

if __name__ == "__main__":
    main()

#最费时的函数是 is_prime()，改进可以考虑使用筛法：可以将时间复杂度从 O(n√n) 降到 O(n log log n)