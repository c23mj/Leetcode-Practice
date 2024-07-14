class Solution {
public:
    vector<vector<char>> updateBoard(vector<vector<char>>& board, vector<int>& click) {
        // for(auto row: board){
        //     for(auto c: row){
        //         cout << c << ' ';
        //     }
        //     cout << '\n';
        // }
        // redundancy check:
        if(board[click[0]][click[1]] != 'E' && board[click[0]][click[1]] != 'M'){
            return board;
        }
        // click a mine!
        if(board[click[0]][click[1]] == 'M'){
            board[click[0]][click[1]] = 'X';
            return board;
        }
        vector<vector<int>> adjs = getAdjacents(board, click);
        int mineCount = 0;
        for(auto adj: adjs){
            if(board[adj[0]][adj[1]] == 'M') mineCount++;
        }

        if(mineCount > 0){
            board[click[0]][click[1]] = '0' + mineCount;
            return board;
        }
        else{
            board[click[0]][click[1]] = 'B';
            for(auto adj: adjs){
                updateBoard(board, adj);
            }
            return board;
        }
        
    }
private:
    vector<vector<int>> getAdjacents(vector<vector<char>>& board, vector<int>& click){
        static vector<vector<int>> diffs = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};
        vector<vector<int>> adjs;
        for(auto diff: diffs){
            vector<int> potential_adj = {click[0] + diff[0], click[1] + diff[1]};
            if(potential_adj[0] >= 0 && potential_adj[0] < board.size() && \
               potential_adj[1] >= 0 && potential_adj[1] < board[0].size()){
                   adjs.push_back(potential_adj);
            }
        }
        return adjs;
    }
};
