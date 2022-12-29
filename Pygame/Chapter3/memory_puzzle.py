# Memory Puzzle
import random, pygame, sys
from pygame.locals import *


# 定义多种常量，方便更改
FPS = 30  # frames per second, the general speed of the program
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
REVEALSPEED = 8
BOXSIZE = 40
GAPSIZE = 10
BOARDWIDTH = 10
BOARDHEIGHT = 7

# assert语句全面检查，必须全都是true，否则程序崩溃
assert (BOARDWIDTH * BOARDHEIGHT) % 2 == 0, 'BOARD needs to have an even number of boxes for pairs of matches.'
XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)


GRAY = (100, 100, 100)
NAVYBLUE = (60, 60, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 255, 0)
PUPPLE = (255, 0, 255)
CYAN = (0, 255, 255)
BGCOLOR = NAVYBLUE
LIGHTBGCOLOR = GRAY
BOXCOLOR = WHITE
HIGHLIGHTCOLOR = BLUE


# 使用常量变量
DONUT = 'donut'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'


# 确保足够多的图标
# 使用元组，不可修改
# 直接好处：使用元组比使用列表速度快
ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PUPPLE, CYAN)
ALLSHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)
assert len(ALLCOLORS) * len(
    ALLSHAPES) * 2 >= BOARDWIDTH * BOARDHEIGHT, "Board is too big for the numer of shapes/colors defined."


def main():
    # 标记为全局变量
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    mousex = 0
    mousey = 0
    pygame.display.set_caption("Memory Game")

    # 数据结构与2D列表
    # 返回一个数据结构，表示游戏板的状态
    mainBoard = getRandomizedBoard()
    # 表示哪个方块被盖住
    revealedBoxes = generateRevealedBoxesData(False)
    # 开始游戏的动画
    # 使用None 设置一个名为 firstSelection的变量，它是数据类型NoneType唯一一值。
    firstSelection = None #stores the (x,y) of the first box clicked

    DISPLAYSURF.fill(BGCOLOR)
    startGameAnimation(mainBoard)

    # 负责无限循环，只要游戏还在运行，该循环就会持续迭代
    while True:
        mouseClicked = False
        # 填充窗口颜色
        DISPLAYSURF.fill(BGCOLOR)
        # drawBoard(mainBoard,revealedBoxes)
    # 事件处理循环

        for event in pygame.event.get():
    # 如果对象是一个QUIT事件或者针对ESC键的一个KEYUP事件，那么，程序将终止
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            elif event.type == MOUSEMOTION:
                mousex, mousey =event.pos
            elif event.type==MOUSEBUTTONUP:
                mousex,mousey = event.pos
                mouseClicked = True
        # 返回两个整数的一个元组
        boxx,boxy = getBoxAtPixel(mousex,mousey)
        if boxx !=  None and boxy != None:
            # 检查boxx和boxy中都不是None的情况Ω
            if not revealedBoxes[boxx][boxy]:
                # 高亮边框绘制
                drawHighlightBox(boxx,boxy)
            # 检查鼠标光标是否不仅在一个盖住的方框上，而且已经点击了鼠标
            if not revealedBoxes[boxx][boxy] and mouseClicked:
                # 这种情况下调用revealedBoxesAnimation()函数，以播放该方块"揭开"动画
                revealedBoxesAnimation(mainBoard,[(boxx,boxy)])
                # 负责记录游戏状态已经更新的数据结构
                revealedBoxes[boxx][boxy] = True

    # 处理第一次点击的方块
    # 执行进入游戏循环之前，firstSelection变量设置为None
    # 程序解释为没有方块被点击
    # 如果是True,这意味着这是点击的两个可能匹配的方块中的第一个
        if firstSelection == None:
            # 将变量设置为点击的方块的方块坐标
            firstSelection = (boxx,boxy)
        else:
            # 获取该图标的形状和颜色值
            icon1shape,icon1color = getShapeAndColor(mainBoard,firstSelection[0],firstSelection[1])
            icon2shape,icon2color = getShapeAndColor(mainBoard,boxx,boxy)
            # 检查两个图标的形状颜色是否一致
            # 调用pygame.time.wait(1000)

            if icon1shape != icon2shape or icon1color != icon2color:
                pygame.time.wait(1000)
                coverBoxesAnimation(mainBoard,[(firstSelection[0],firstSelection[1]),(boxx,boxy)])
                revealedBoxes[firstSelection[0]][firstSelection[1]] = False
                revealedBoxes[boxx][boxy] =False

            elif hasWon(revealedBoxes):
                # 播放游戏获胜动画
                # 重新设置mainBoard和revealedBoxes中的数据结构以启动一次新的游戏
                gameWonAnimation(mainBoard)
                pygame.time.wait(2000)

                mainBoard = getRandomizedBoard()
                revealedBoxes = generateRevealedBoxesData(False)

                drawBoard(mainBoard,revealedBoxes)
                pygame.display.update()
                pygame.time.wait(1000)
                # 再次播放"开始游戏"的动画
                startGameAnimation(mainBoard)
            # 不管方块是否一致，在第118行点击第二个方块之后，都会将firstSelection设置回到None
            # 以便玩家点击下一个方块的时候，会被当作可能匹配的图标对中第一次点击的方块
            firstSelection = None






def getRandomizedBoard():
    # Get a list of every possible shape in every possible color
    icons = []
    for color in ALLCOLORS:
        for shape in ALLSHAPES:
            icons.append((shape, color))
    random.shuffle(icons) # randomize the order of the icons list
    numIconsUsed = int(BOARDWIDTH*BOARDHEIGHT/2) # calculate how many icons are needed
    icons = icons[:numIconsUsed] * 2 # make two of each
    random.shuffle(icons)

    # Create the board data structure, with randomly placed icons
    board = []
    for x in range(BOARDWIDTH):
        column = []
        for y in range(BOARDHEIGHT):
            column.append(icons[0])
            del icons[0] # remove the icons  as we assign them
        board.append(column)
    return board


def generateRevealedBoxesData(val):
    revealedBoxes = []
    for i in range(BOARDWIDTH):
        revealedBoxes.append([val]*BOARDHEIGHT)
    return revealedBoxes


def startGameAnimation(board)