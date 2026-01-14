# Implement a Matrix class with the following attributes:
# - entries: this will be a list containing the entries of the matrix

# implement the following methods:
# __str__: to print the matrix
# __getitem__(row_idx, col_idx): returns the entry at the given row index and column index
# __add__(other: Matrix) -> Matrix: adds the matrices (THIS SHOULD CHECK THEY're compatible for addition, and raise an error if they're not)
# __mul__(other: Matrix) -> Matrix: multiplies the matrices (THIS SHOULD CHECK THEY're compatible for multiplication, and if they're not it should raise an ERROR)
# __mul__(scalar: float) -> Matrix: multiplies with a scalar

# anything else you'd like to add

# TEST IT WITH THE MATRICES FROM THE EXERCISES IN THE CLASS!


class Matrix:
    def __init__(self, data: tuple[tuple[float, ...], ...]):
        self.data = data
        self.rows = len(data)
        self.columns = len(data[0])
        # assumes there is at least one row and every row is same width :/

    def __str__(self) -> str:
        """print the matrix"""
        # found these silly lil unicode symbols for big square brackets
        # and yes, of course LEFT SQUARE BRACKET EXTENSION and RIGHT SQUARE BRACKET EXTENSION are different symbols, duh

        # ⎡   ⎤
        # ⎢   ⎥
        # ⎣   ⎦

        # ⎡a b 1⎤
        # ⎢h i j⎥
        # ⎢c d 2⎥
        # ⎣e f 3⎦
        beautified_matrix = """"""
        extension = self.rows - 2
        beautified_matrix += f"⎡{self.data[0]}⎤\n"
        if extension > 0:
            for row in range(extension):
                beautified_matrix += f"⎢{self.data[row]}⎥\n"
        beautified_matrix += f"⎣{self.data[extension + 1]}⎦"

        return beautified_matrix

    def __getitem__(self, idxs: tuple[int, int]):
        """return entry at given row index and column index"""
        row_idx, col_idx = idxs
        return self.data[row_idx][col_idx]

    def __add__(self, other: "Matrix") -> "Matrix":
        """add matrix to another matrix"""
        nm = []
        for row in range(self.rows):
            nmrow = []
            for entry in range(self.columns):
                nmrow.append(self[row, entry] + other[row, entry])
            nm.append(nmrow)

        return Matrix(tuple(tuple(thing) for thing in nm))

    def __mul__(self, other: "Matrix | float | int") -> "Matrix":
        """multiply matrix by another matrix OR a scalar"""
        # other_columns = (
        #     (row[column] for row in other.data) for column in range(other.columns)
        # )
        # ^ seems to match "transposing" a matrix?
        # nvm?

        if type(other) is Matrix and self.columns == other.rows:
            # 2x2
            # a b   e f   ae+bg af+bh
            #     x     =
            # c d   g h   ce+dg cf+dh
            # ((a, b), (c, d)) * ((e, f), (g, h)) = ((a * e + b * g, a * f + b * h), (c * e + d * g, c * f + d * h))
            # self * other = out

            # self = Matrix(((0, -2), (-2, -5)))
            # other = Matrix(((6, -6), (3, 0)))
            # out = (
            #     (
            #         self[0, 0] * other[0, 0] + self[0, 1] * other[1, 0],
            #         self[0, 0] * other[0, 1] + self[0, 1] * other[1, 1],
            #     ),
            #     (
            #         self[1, 0] * other[0, 0] + self[1, 1] * other[1, 0],
            #         self[1, 0] * other[0, 1] + self[1, 1] * other[1, 1],
            #     ),
            # )

            # abds = [[0.0] * 2 for _ in range(2)]
            # # out2 = ((a, b), (c, d))
            # for i in range(2):
            #     for j in range(2):
            #         abds[i][j] = self[i, 0] * other[0, j] + self[i, 1] * other[1, j]

            k = self.columns

            abds2 = [[0.0] * other.columns for _ in range(self.rows)]

            for i in range(k):
                for j in range(k):
                    abds2[i][j] = sum(
                        self[i, index] * other[index, j] for index in range(k)
                    )

            return Matrix(tuple(tuple(thing) for thing in abds2))

        elif type(other) is float or type(other) is int:
            return Matrix(tuple(tuple(other * h for h in row) for row in self.data))
        else:
            pass

        def __iter__(self):  # for unpacking with * and iterating rows
            pass


# matrices from homework: numbered by problem number and left/right, accordingly
# or uhh tuple pairs of (left, right) i guess that works

matrices1 = ((0, 2), (-2, -5)), ((6, -6), (3, 0))
matrices2 = ((6), (-3)), ((-5), (4))
matrices8 = ((3, 2, 5), (2, 3, 1)), ((4, 5, -5), (5, -1, 6))  # undefined product


# uwu = Matrix(matrices1[0])
# owo = Matrix(((0, -2), (-2, -5)))[0, 0]


class TestMatrix:
    # def test_str(self):
    #     assert (
    #         str(matrices1[0])
    #         == """⎡a b 1⎤
    #     ⎢h i j⎥
    #     ⎢c d 2⎥
    #     ⎣e f 3⎦"""
    #     )

    #     pass

    def test_getitem(self):
        m1 = Matrix(matrices1[0])
        assert m1.data == ((0, 2), (-2, -5))

    def test_add(self):
        added1 = Matrix(matrices1[0]) + Matrix(matrices1[1])
        assert added1.data == ((6, -4), (1, -5))

    def test_mul_matrix(self):
        m3 = Matrix(matrices1[0]) * Matrix(matrices1[1])
        assert m3.data == ((6, 0), (-27, 12))

    def test_mul_scalar(self):
        m3 = Matrix(((4, 0), (1, -9))) * 2
        assert m3.data == ((8, 0), (2, -18))


def main():
    print("Hello from matrix-class!")


if __name__ == "__main__":
    main()
