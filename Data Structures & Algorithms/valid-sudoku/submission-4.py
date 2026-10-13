class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0,len(board)):
            temp_ls_horizontal=[]
            temp_ls_vertical=[]
            for j in range(len(board)):
                if board[i][j]!='.':
                    temp_ls_horizontal.append(eval(board[i][j]))
                    
                if board[j][i]!='.':
                    temp_ls_vertical.append(eval(board[j][i]))
            if len(set(temp_ls_horizontal))!=len(temp_ls_horizontal):
                # print('breaking the loop horizontally')
                return False
            if len(set(temp_ls_vertical))!=len(temp_ls_vertical):
                # print("breaking the loop vertically")
                return False
        for ii in range(0,len(board),3):
            for jj in range(0,9,3):
                ls=[]
                for rows in range(3):
                    for columns in range(3):
                        if board[ii+rows][jj+columns]!='.':
                            ls.append(eval(board[ii+rows][jj+columns]))
                if len(ls)!=len(set(ls)):
                    return False
        return True                                                                                                                          
        