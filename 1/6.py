a = list(map(int, input().split())) 
is_prime = list(filter(lambda i: all(i%j!=0 for j in range(2, i//2)), a))
print(is_prime)