class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        matrix = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board)):
                num = board[r][c]
                key = (r//3, c//3)
                if num == ".":
                    continue
                if num in row[r]:
                    return False
                else:
                    row[r].add(num)
                if num in col[c]:
                    return False
                else:
                    col[c].add(num)
                if num in matrix[key]:
                    return False
                else:
                    matrix[key].add(num)
        return True
                

