import tensor

class Matrix(tensor.Tensor) :
    def __init__(self, data , dimension = None) -> None:
        super().__init__(data, dimension)
        if len(self.dimension) != 2 :
            raise ValueError("Matrix may have only 2 dimensions")

    def cony_rc2i(self, row : int, column : int) -> int:
        if not (0 <= row < self.dimension[0] and 0 <= column < self.dimension[1]):
            raise ValueError('Invalid arguments')
        
        return row * self.dimension[0] + column

    def cony_i2rc(self, ind : int) -> tuple[int, int]:
        if not(0 <= ind < self.dimension[0] * self.dimension[1]):
            raise ValueError('Invalid argument')
        
        return (ind // self.dimension[1], self % self.dimension[1])
    
    def __str__(self):
        rows, cols = self.dimension
        maxx = max(len(str(value)) for value in self.data)
        lines = []
        
        for r in range(rows):
            line = []
            for c in range(cols):
                line.append(f"{self.data[r * cols + c]:>{maxx}}")
            lines.append("  " + "  ".join(line))
        
        return "[\n" + "\n\n".join(lines) + "\n]"
    
    def __getitem__(self, key):
        rows, cols = self.dimension

        if isinstance(key, int):
            key = key % rows
            start = key * cols
            return Matrix(self.data[start:start + cols], (1, cols))

        if isinstance(key, list):
            selected_rows = [r % rows for r in key]
            result_data = [self.data[r * cols:(r + 1) * cols] for r in selected_rows]
            return Matrix([num for row in result_data for num in row], (len(selected_rows), cols))

        if isinstance(key, slice):
            selected_rows = range(*key.indices(rows))
            result_data = [self.data[i * cols:(i + 1) * cols] for i in selected_rows]
            return Matrix([num for row in result_data for num in row], (len(selected_rows), cols))

        if isinstance(key, tuple):
            row_key, col_key = key

            if isinstance(row_key, int):
                row_key = [row_key % rows]
            elif isinstance(row_key, slice):
                row_key = range(*row_key.indices(rows))
            elif isinstance(row_key, list):
                row_key = [r % rows for r in row_key]

            if isinstance(col_key, int):
                col_key = [col_key % cols]
            elif isinstance(col_key, slice):
                col_key = range(*col_key.indices(cols))
            elif isinstance(col_key, list):
                col_key = [c % cols for c in col_key]

            result_data = [self.data[r * cols + c] for r in row_key for c in col_key]
            return Matrix(result_data, (len(row_key), len(col_key)))

        raise TypeError("Invalid index type")
    