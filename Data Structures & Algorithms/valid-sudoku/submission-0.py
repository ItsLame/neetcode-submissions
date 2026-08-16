class Solution:
    def safeAddToSet(self, s: set[str], e: str) -> bool:
        init_set = len(s)
        if e != ".":
            s.add(e)
            if init_set == len(s):
                return False

        return True

    def isValidRow(self, row: List[str]) -> bool:
        row_nums = set()

        for r in row:
            is_safe = self.safeAddToSet(row_nums, r)
            if not is_safe:
                return False

        return True
    
    def isValidCol(self, board: List[List[str]], cell: int) -> bool:
        col_nums = set()

        for n in range(9):
            c = board[n][cell]
            is_safe = self.safeAddToSet(col_nums, c)
            if not is_safe:
                return False

        return True

    def isValidBox(self, board:List[List[str]], box_row: int, box_col: int) -> bool:
        box_nums = set()
        start_row = box_row * 3
        start_col = box_col * 3
        
        for r in range(3):
            for c in range(3):
                cell = board[start_row + r][start_col + c]
                is_safe = self.safeAddToSet(box_nums, cell)
                if not is_safe:
                    return False

        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        is_row_valid = True
        is_col_valid = True
        is_box_valid = True

        # check row validity
        for row in board:
            is_row_valid = self.isValidRow(row)
            if not is_row_valid:
                return False
            
        # check col validity
        for cell in range(len(board[0])):
            is_col_valid = self.isValidCol(board, cell)
            if not is_col_valid:
                return False

        # check box validity
        for r in range(3):
            for c in range(3):
                is_box_valid = self.isValidBox(board, r, c)
                if not is_box_valid:
                    return False

        return True