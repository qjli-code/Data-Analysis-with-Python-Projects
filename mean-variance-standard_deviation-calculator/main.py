# This entrypoint file to be used in development. Start by reading README.md
import mean_var_std
from unittest import main

print(f'input list:', [0,1,2,3,4,5,6,7,8])
result = mean_var_std.calculate([0,1,2,3,4,5,6,7,8])
print(f'====================================================')
print(f'results are for axis=0, axis=1, and flattened array.')
print(f'====================================================')
for rk, rv in result.items():
    print(f'{rk}:')
    for i in rv:
        print(f'    {i}')

# Run unit tests automatically
main(module='test_module', exit=False)
