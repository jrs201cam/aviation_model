d_per_y = 365.0
p_y = 4.46E9
f_d = 2.0
s = 150.0

p_d =  p_y/d_per_y
a_d = p_d/(s*f_d)

print(f"{p_d=:.2e}")
print(f"{a_d=:.2e}")