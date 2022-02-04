class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            col_list = [elem[i] for elem in board if elem[i] != '.']
            if len(col_list) != len(set(col_list)):
                return False
        for elem in board:
            row_list = [num for num in elem if num != '.']
            if len(row_list) != len(set(row_list)):
                return False
        row_start = 0
        row_end = 3
        col_start = 0
        col_end = 3
        for i in range(9):
            check_box = []
            for j in range(row_start,row_end):
                for k in range(col_start,col_end):
                    if board[j][k] == ".":
                        continue
                    else:
                        check_box.append(board[j][k])
            if len(check_box) != len(set(check_box)):
                return False

            col_start+=3
            col_end+=3
            if col_end > 9:
                col_start = 0
                col_end = 3
                row_start+= 3
                row_end += 3
        return True