class LCSMatrix:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
        self.row_count = len(str1)
        self.column_count = len(str2)

        # Pass 1: zero grid
        self.matrix = []
        for r in range(self.row_count):
            row = []
            for c in range(self.column_count):
                row.append(0)
            self.matrix.append(row)
                
        # Pass 2: fill
        for r in range(self.row_count):
            for c in range(self.column_count):
                if self.str1[r] == self.str2[c]:
                    self.matrix[r][c] = 1 + self.get_entry(r - 1, c - 1)
                else:
                    self.matrix[r][c] = max(self.get_entry(r - 1, c), self.get_entry(r, c - 1))
    
    # Returns the number of columns in the matrix, which also equals the length
    # of the second string passed to the constructor.
    def get_column_count(self):
        return self.column_count
    
    # Returns the matrix entry at the specified row and column indices, or 0 if
    # either index is out of bounds.
    def get_entry(self, row_index, column_index):
        if row_index < 0 or column_index < 0 or row_index >= self.row_count or column_index >= self.column_count:
            return 0
        return self.matrix[row_index][column_index]
    
    # Returns the number of rows in the matrix, which also equals the length
    # of the first string passed to the constructor.
    def get_row_count(self):
        return self.row_count
    
    # Returns the set of distinct, longest common subsequences between the two
    # strings that were passed to the constructor.
    def get_longest_common_subsequences(self):
        # Create an empty set that will be returned
        result_set = set()

        # The walk through the matrix begins
        def walk(r, c, current):
            if r < 0 or c < 0 or r >= self.row_count or c >= self.column_count or self.get_entry(r, c) == 0:
                if current != "":
                    result_set.add(current)
                return

            # Check to see if corresponding letters match
            if self.str1[r] == self.str2[c]:           
                # if they do then we add that letter to the subsequences and the move diagonally
                walk(r - 1, c - 1, self.str1[r] + current)
            
            # if they do not match then we look at the left and top and pick whichever is largest
            # if both left and top are the same then we take both paths
            else:
                if self.get_entry(r - 1, c) > self.get_entry(r, c - 1):
                    walk(r - 1, c, current)
                elif self.get_entry(r, c - 1) > self.get_entry(r - 1, c):
                    walk(r, c - 1, current)
                else:
                    walk(r - 1, c, current)
                    walk(r, c - 1, current)

        walk(self.row_count - 1, self.column_count -1, "")

        return result_set