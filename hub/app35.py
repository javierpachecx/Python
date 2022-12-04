# Solving a higher order differential equation

def runge_kutta_4th_order(f, x0, y0, x1, n):
    vx = [0] * (n + 1)
    vy = [0] * (n + 1)
    h = (x1 - x0) / float(n)
    vx[0] = x = x0
    vy[0] = y = y0
    for i in range(1, n + 1):
        k1 = h * f(x, y)
        k2 = h * f(x + 0.5 * h, y + 0.5 * k1)
        k3 = h * f(x + 0.5 * h, y + 0.5 * k2)
        k4 = h * f(x + h, y + k3)
        vx[i] = x = x0 + i * h
        vy[i] = y = y + (k1 + k2 + k2 + k3 + k3 + k4) / 6
    return vx, vy

def f(x, y):
    # Here you must write the differential equation you want to solve.
    # For example, if you want to solve the differential equation y' = x + y, you can write:
    return x + y
    pass

x0 = float(input("Enter the value of x0: "))
y0 = float(input("Enter the value of y0: "))
x1 = float(input("Enter the value of x1: "))
n = int(input("Enter the number of steps: "))

vx, vy = runge_kutta_4th_order(f, x0, y0, x1, n)

for x, y in zip(vx, vy):
    print(f"x = {x:.5f}, y = {y:.5f}")