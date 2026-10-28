
from graphics import Canvas


# ---------------------------------------------------------------------------
# Layout constants  – tweak these to resize or restyle the game
# ---------------------------------------------------------------------------
CANVAS_WIDTH      = 600           # Total canvas width  (pixels)
CANVAS_HEIGHT     = 660           # Total canvas height (grid + status bar)
GRID_SIZE         = 600           # The square grid fills the top 600 px
CELL_SIZE         = GRID_SIZE // 3        # Each cell is 200 × 200 px
SYMBOL_PADDING    = 40            # Gap between cell edge and drawn symbol

# Colours (standard CSS colour strings accepted by the Canvas API)
BACKGROUND_COLOR  = "#1e1e2e"     # Dark navy background
GRID_LINE_COLOR   = "#89b4fa"     # Soft blue grid lines
X_COLOR           = "#f38ba8"     # Pink/red for X
O_COLOR           = "#a6e3a1"     # Green for O
HIGHLIGHT_COLOR   = "#45475a"     # Grey highlight for winning cells
STATUS_COLOR      = "white"       # Status bar text colour


# ---------------------------------------------------------------------------
# Board helpers
# ---------------------------------------------------------------------------
def create_empty_board():
    """Return a 3×3 board as a flat list of 9 None values.

    Cell index layout:
        0 | 1 | 2
        ---------
        3 | 4 | 5
        ---------
        6 | 7 | 8
    """
    return [None] * 9


def get_cell_index(click_x, click_y):
    """Convert a mouse-click coordinate into a board cell index (0–8).

    Returns None when the click lands outside the 3×3 grid area.
    """
    if click_x < 0 or click_x >= GRID_SIZE:
        return None
    if click_y < 0 or click_y >= GRID_SIZE:
        return None

    column = int(click_x // CELL_SIZE)   # 0, 1, or 2  (left → right)
    row    = int(click_y // CELL_SIZE)   # 0, 1, or 2  (top  → bottom)
    return row * 3 + column


def get_cell_center(cell_index):
    """Return the (cx, cy) pixel coordinates for the centre of a cell."""
    row    = cell_index // 3
    column = cell_index  % 3
    center_x = column * CELL_SIZE + CELL_SIZE // 2
    center_y = row    * CELL_SIZE + CELL_SIZE // 2
    return center_x, center_y


# ---------------------------------------------------------------------------
# Win / draw detection
# ---------------------------------------------------------------------------

# All eight winning lines expressed as triples of cell indices
WINNING_COMBINATIONS = [
    (0, 1, 2),   # top row
    (3, 4, 5),   # middle row
    (6, 7, 8),   # bottom row
    (0, 3, 6),   # left column
    (1, 4, 7),   # centre column
    (2, 5, 8),   # right column
    (0, 4, 8),   # diagonal: top-left → bottom-right
    (2, 4, 6),   # diagonal: top-right → bottom-left
]


def check_winner(board):
    """Scan every winning combination and return 'X', 'O', or None."""
    for a, b, c in WINNING_COMBINATIONS:
        if board[a] is not None and board[a] == board[b] == board[c]:
            return board[a]   # Return the symbol that has won
    return None


def is_board_full(board):
    """Return True when no empty cell (None) remains on the board."""
    return all(cell is not None for cell in board)


# ---------------------------------------------------------------------------
# Drawing helpers  (all use the Canvas API from the docs)
# ---------------------------------------------------------------------------

def draw_background(canvas):
    """Fill the entire canvas with the background colour."""
    canvas.create_rectangle(
        0, 0,
        CANVAS_WIDTH, CANVAS_HEIGHT,
        BACKGROUND_COLOR
    )


def draw_grid(canvas):
    """Draw the two vertical and two horizontal lines that form the 3×3 grid."""
    for divider in range(1, 3):
        x_position = divider * CELL_SIZE
        y_position = divider * CELL_SIZE

        # Vertical line
        canvas.create_line(
            x_position, 0,
            x_position, GRID_SIZE,
            GRID_LINE_COLOR
        )

        # Horizontal line
        canvas.create_line(
            0, y_position,
            GRID_SIZE, y_position,
            GRID_LINE_COLOR
        )


def draw_x_in_cell(canvas, cell_index):
    """Draw an X symbol (two crossing diagonal lines) inside the given cell.

    The lines are inset by SYMBOL_PADDING pixels from the cell edges so
    the symbol does not touch the grid lines.
    """
    cx, cy = get_cell_center(cell_index)
    half_symbol = CELL_SIZE // 2 - SYMBOL_PADDING   # Distance from centre to corner of symbol

    # Top-left → bottom-right diagonal
    canvas.create_line(
        cx - half_symbol, cy - half_symbol,
        cx + half_symbol, cy + half_symbol,
        X_COLOR
    )

    # Top-right → bottom-left diagonal
    canvas.create_line(
        cx + half_symbol, cy - half_symbol,
        cx - half_symbol, cy + half_symbol,
        X_COLOR
    )


def draw_o_in_cell(canvas, cell_index):
    """Draw an O symbol (a ring / hollow oval) inside the given cell.

    canvas.create_oval() takes the bounding box of the oval so we
    compute left/top/right/bottom from the cell centre and the radius.
    """
    cx, cy       = get_cell_center(cell_index)
    oval_radius  = CELL_SIZE // 2 - SYMBOL_PADDING

    left   = cx - oval_radius
    top    = cy - oval_radius
    right  = cx + oval_radius
    bottom = cy + oval_radius

    # Fill with background colour so it looks like a ring, not a disc
    canvas.create_oval(
        left, top, right, bottom,
        BACKGROUND_COLOR,   # fill
        O_COLOR             # outline / ring colour
    )


def highlight_winning_cells(canvas, board):
    """Draw a coloured rectangle behind each of the three winning cells."""
    for a, b, c in WINNING_COMBINATIONS:
        if board[a] is not None and board[a] == board[b] == board[c]:
            for cell_index in (a, b, c):
                cx, cy      = get_cell_center(cell_index)
                inset       = 6    # Small gap so the highlight does not overlap grid lines
                half_cell   = CELL_SIZE // 2 - inset

                canvas.create_rectangle(
                    cx - half_cell, cy - half_cell,
                    cx + half_cell, cy + half_cell,
                    HIGHLIGHT_COLOR
                )
            break   # Only one winning line can exist at a time


def create_status_text(canvas, message):
    """Draw the status message in the bar below the grid and return its object id.

    The id is needed later so we can update the text with canvas.change_text().
    """
    status_x = CANVAS_WIDTH  // 2
    status_y = GRID_SIZE + (CANVAS_HEIGHT - GRID_SIZE) // 2   # Vertically centred in bar

    status_id = canvas.create_text(
        status_x, status_y,
        message,
        font      = "Arial",
        font_size = 20,
        color     = STATUS_COLOR
    )
    return status_id


# ---------------------------------------------------------------------------
# Main game loop
# ---------------------------------------------------------------------------

def play_game():
    """Initialise the canvas, run the turn loop, and display the final result.

    Game flow per turn:
        1. Wait for the player to click  (canvas.wait_for_click)
        2. Work out which cell was clicked
        3. Validate the click (inside grid? cell empty?)
        4. Record the move and draw the symbol
        5. Check for a winner or a draw
        6. Switch players or end the game
    """

    # --- Set up the canvas ---------------------------------------------------
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.set_canvas_title("XO Game – Tic-Tac-Toe")

    draw_background(canvas)
    draw_grid(canvas)

    # Create the status text object and keep its id for later updates
    status_text_id = create_status_text(canvas, "Player X's turn  –  click a cell")

    # --- Initialise game state -----------------------------------------------
    board          = create_empty_board()
    current_player = "X"    # X always goes first
    game_over      = False

    # --- Turn loop -----------------------------------------------------------
    while True:
        # Block until the user clicks anywhere on the canvas
        click = canvas.wait_for_click()   # Returns an object with .x and .y
        click_x = click.x
        click_y = click.y

        # Any click after the game ends exits the loop and closes the window
        if game_over:
            break

        # Determine which cell index (0-8) was clicked
        cell_index = get_cell_index(click_x, click_y)

        # Reject clicks that land outside the grid
        if cell_index is None:
            continue

        # Reject clicks on cells that are already occupied
        if board[cell_index] is not None:
            canvas.change_text(status_text_id, "That cell is taken!  Pick another.")
            continue

        # --- Register the move and draw the symbol ---------------------------
        board[cell_index] = current_player

        if current_player == "X":
            draw_x_in_cell(canvas, cell_index)
        else:
            draw_o_in_cell(canvas, cell_index)

        # --- Check game-ending conditions ------------------------------------
        winner = check_winner(board)

        if winner:
            # Redraw winning cells with a highlight, then update the status
            highlight_winning_cells(canvas, board)

            # Re-draw the symbols on top of the highlight rectangles
            for index, mark in enumerate(board):
                if mark == "X":
                    draw_x_in_cell(canvas, index)
                elif mark == "O":
                    draw_o_in_cell(canvas, index)

            canvas.change_text(status_text_id, f"Player {winner} wins!  Click anywhere to exit.")
            game_over = True

        elif is_board_full(board):
            canvas.change_text(status_text_id, "It's a draw!  Click anywhere to exit.")
            game_over = True

        else:
            # Switch to the next player and update the prompt
            current_player = "O" if current_player == "X" else "X"
            canvas.change_text(status_text_id, f"Player {current_player}'s turn  –  click a cell")

    # One final click to close
    canvas.wait_for_click()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    play_game()