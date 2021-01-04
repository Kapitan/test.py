import random
import string

result_str = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(100, 1000)))
print(result_str)
