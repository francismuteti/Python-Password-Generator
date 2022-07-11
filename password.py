import random
letters_upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters_lower_case="abcdefghijklmnopqrst"
special_cases="!£$%^&*_-?/\|#"
numbers="0123456789"
use_for=letters_upper_case+letters_lower_case+special_cases+numbers
pass_limit=8
password="".join(random.sample(use_for,pass_limit))
print(password) 
