import java.util.Scanner;

public class TicTacToe {
    static final char HUMAN = 'X';
    static final char AI = 'O';
    static final char EMPTY = ' ';
    
    // Utility function to check for a winner
    public static boolean checkWinner(char[][] board, char player) {
        // Check rows, columns, and diagonals
        return (board[0][0] == player && board[0][1] == player && board[0][2] == player) || // Row 1
               (board[1][0] == player && board[1][1] == player && board[1][2] == player) || // Row 2
               (board[2][0] == player && board[2][1] == player && board[2][2] == player) || // Row 3
               (board[0][0] == player && board[1][0] == player && board[2][0] == player) || // Column 1
               (board[0][1] == player && board[1][1] == player && board[2][1] == player) || // Column 2
               (board[0][2] == player && board[1][2] == player && board[2][2] == player) || // Column 3
               (board[0][0] == player && board[1][1] == player && board[2][2] == player) || // Diagonal 1
               (board[0][2] == player && board[1][1] == player && board[2][0] == player);   // Diagonal 2
    }
    
    // Function to check if the game is a tie
    public static boolean isTie(char[][] board) {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[i][j] == EMPTY) {
                    return false;
                }
            }
        }
        return true;
    }
    
    // Minimax with alpha-beta pruning
    public static int minimax(char[][] board, int depth, int alpha, int beta, boolean isMaximizing) {
        if (checkWinner(board, AI)) {
            return 1;
        }
        if (checkWinner(board, HUMAN)) {
            return -1;
        }
        if (isTie(board)) {
            return 0;
        }

        if (isMaximizing) {
            int maxEval = Integer.MIN_VALUE;
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    if (board[i][j] == EMPTY) {
                        board[i][j] = AI;
                        int eval = minimax(board, depth + 1, alpha, beta, false);
                        board[i][j] = EMPTY;
                        maxEval = Math.max(maxEval, eval);
                        alpha = Math.max(alpha, eval);
                        if (beta <= alpha) {
                            break;
                        }
                    }
                }
            }
            return maxEval;
        } else {
            int minEval = Integer.MAX_VALUE;
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    if (board[i][j] == EMPTY) {
                        board[i][j] = HUMAN;
                        int eval = minimax(board, depth + 1, alpha, beta, true);
                        board[i][j] = EMPTY;
                        minEval = Math.min(minEval, eval);
                        beta = Math.min(beta, eval);
                        if (beta <= alpha) {
                            break;
                        }
                    }
                }
            }
            return minEval;
        }
    }
    
    // Function for the AI to make its move
    public static void aiMove(char[][] board) {
        int bestScore = Integer.MIN_VALUE;
        int[] bestMove = new int[2];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[i][j] == EMPTY) {
                    board[i][j] = AI;
                    int score = minimax(board, 0, Integer.MIN_VALUE, Integer.MAX_VALUE, false);
                    board[i][j] = EMPTY;
                    if (score > bestScore) {
                        bestScore = score;
                        bestMove[0] = i;
                        bestMove[1] = j;
                    }
                }
            }
        }
        board[bestMove[0]][bestMove[1]] = AI;
    }
    
    // Function for the human player to make a move
    public static boolean humanMove(char[][] board, int row, int col) {
        if (board[row][col] == EMPTY) {
            board[row][col] = HUMAN;
            return true;
        }
        return false;
    }
    
    // Function to print the current board
    public static void printBoard(char[][] board) {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.print(board[i][j]);
                if (j < 2) {
                    System.out.print("|");
                }
            }
            System.out.println();
            if (i < 2) {
                System.out.println("-----");
            }
        }
    }
    
    // Main game loop
    public static void playGame() {
        Scanner scanner = new Scanner(System.in);
        char[][] board = {
            {EMPTY, EMPTY, EMPTY},
            {EMPTY, EMPTY, EMPTY},
            {EMPTY, EMPTY, EMPTY}
        };
        
        System.out.println("Tic-Tac-Toe Game!");
        printBoard(board);
        
        while (true) {
            // Human's turn
            System.out.println("Enter the row (0, 1, or 2): ");
            int row = scanner.nextInt();
            System.out.println("Enter the column (0, 1, or 2): ");
            int col = scanner.nextInt();
            
            if (humanMove(board, row, col)) {
                printBoard(board);
                if (checkWinner(board, HUMAN)) {
                    System.out.println("You win!");
                    break;
                }
                if (isTie(board)) {
                    System.out.println("It's a tie!");
                    break;
                }
            } else {
                System.out.println("Invalid move! Try again.");
                continue;
            }
            
            // AI's turn
            aiMove(board);
            System.out.println("AI's move:");
            printBoard(board);
            if (checkWinner(board, AI)) {
                System.out.println("AI wins!");
                break;
            }
            if (isTie(board)) {
                System.out.println("It's a tie!");
                break;
            }
        }
        
        scanner.close();
    }

    public static void main(String[] args) {
        playGame();
    }
}
