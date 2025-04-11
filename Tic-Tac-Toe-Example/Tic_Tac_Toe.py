import Player1
import Player2

def reset_board():
    return [ [ " " for i in range(3) ] for j in range(3) ]

def is_move_legal( board, move ):
    return board[ (move - 1) // 3 ][ (move - 1) % 3 ] == " "

def is_board_full( board ):
    return all( [ all( [ cell != " " for cell in row ] ) for row in board ] )

def is_game_won( board ):
    for row in board:
        if ( row[0] == row[1] == row[2] and row[0] != " " ):
            return True

    for col in range(3):
        if ( board[0][col] == board[1][col] == board[2][col] and board[0][col] != " " ):
            return True

    if ( board[0][0] == board[1][1] == board[2][2] and board[0][0] != " " ):
        return True

    if ( board[0][2] == board[1][1] == board[2][0] and board[0][2] != " " ):
        return True

    return False

def switch_player( player ):
    if ( player == "X" ):
        return "O"
    else:
        return "X"

def show_board( board ):
    board_string = ""
    board_string += f"{board[0][0]} | {board[0][1]} | {board[0][2]}\n"
    board_string += "---------\n"
    board_string += f"{board[1][0]} | {board[1][1]} | {board[1][2]}\n"
    board_string += "---------\n"
    board_string += f"{board[2][0]} | {board[2][1]} | {board[2][2]}\n"

    return board_string

def main():
    play_again = True
    x_wins = 0
    o_wins = 0

    while ( play_again ):
        game_board = reset_board()
        player = "X"
        game_over = False

        while ( not( game_over ) ):
            print( show_board( game_board ) )

            legal_move = False
            while ( not( legal_move ) ):
                if ( player == "X" ):
                    move = Player1.getMove( game_board )
                else:
                    move = Player2.getMove( game_board )

                legal_move = is_move_legal( game_board, move )
                if ( not( legal_move ) ):
                    print( "Illegal move, try again." )

            game_board[ (move - 1) // 3 ][ (move - 1) % 3 ] = player

            if ( is_board_full( game_board) ):
                game_over = True
                print( show_board( game_board ) )
                print( "Game over, tied!")
            elif ( is_game_won( game_board ) ):
                game_over = True
                print( show_board( game_board ) )
                print( f"Game won by {player}" )

                if ( player == "X" ):
                    x_wins += 1
                else:
                    o_wins += 1
            else:
                player = switch_player( player )

        print( f"X has won {x_wins} times, and O has won {o_wins} times.")
        play_more = input( "Would you like to play again [Y/N]? " ).upper()
        play_again = play_more == "Y"
    return

if __name__ == "__main__":
    main()