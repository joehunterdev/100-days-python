WIDTH: int = 800
HEIGHT: int = 600
BG_COLOR: str = "Black"
IN_GAME: bool = True
BORDER_WIDTH: int = 1
MAX_Y: int = ((HEIGHT / 2) - BORDER_WIDTH )
MIN_Y: int = -abs((HEIGHT / 2)  + BORDER_WIDTH ) 
MAX_X: int = ((WIDTH / 2) - BORDER_WIDTH )
MIN_X: int = -abs((WIDTH / 2)  + BORDER_WIDTH ) 
BAT_HEIGHT: int = 6
BAT_WIDTH: int = 1
# BAT_SHAPE:str ="strech_wid" 
BALL_SIZE = 2
BALL_SPEED=1

# from tkinter import Tk

# main=Tk()
# main.geometry('+100+200')
# main.mainloop()