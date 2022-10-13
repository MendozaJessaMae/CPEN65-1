def main():
    class Circle:
        def __init__(self, radius=1):
            self._radius = radius


    class AreaUsingRadius(Circle):
        def area_radius(self):
            pi = 3.14
            return (pi * (self._radius**2))

    radius = float(input("Enter the radius of the circle: "))
    solve = AreaUsingRadius(radius)
    print(str(solve.area_radius()) + " unit squared ")

main()