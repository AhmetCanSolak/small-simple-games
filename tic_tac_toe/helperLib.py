import pygame

class Board:
    def __init__(self,displayInfo,text,boardWindow):
        self.player = True
        self.displayInfo = displayInfo
        self.boardWindow = boardWindow
        self.boardHeight = displayInfo.current_h-text.get_height()
        self.initializeSlots( (displayInfo.current_w-self.boardHeight)/2, text.get_height() - 5 , self.boardHeight/3)
        self.xCounts = [[0,0,0],
                        [0,0,0],
                        [0,0,0]]

        self.oCounts = [[0,0,0],
                        [0,0,0],
                        [0,0,0]]

    def initializeSlots(self,topLeftX,topLeftY,slotSideLength):
        self.slots = []
        self.slots.append(Slot(0,0,topLeftX,topLeftY,slotSideLength,self.boardWindow))
        self.slots.append(Slot(1,0,topLeftX+slotSideLength,topLeftY,slotSideLength,self.boardWindow))
        self.slots.append(Slot(2,0,topLeftX+slotSideLength*2,topLeftY,slotSideLength,self.boardWindow))
        self.slots.append(Slot(0,1,topLeftX,topLeftY+slotSideLength,slotSideLength,self.boardWindow))
        self.slots.append(Slot(1,1,topLeftX+slotSideLength,topLeftY+slotSideLength,slotSideLength,self.boardWindow))
        self.slots.append(Slot(2,1,topLeftX+slotSideLength*2,topLeftY+slotSideLength,slotSideLength,self.boardWindow))
        self.slots.append(Slot(0,2,topLeftX,topLeftY+slotSideLength*2,slotSideLength,self.boardWindow))
        self.slots.append(Slot(1,2,topLeftX+slotSideLength,topLeftY+slotSideLength*2,slotSideLength,self.boardWindow))
        self.slots.append(Slot(2,2,topLeftX+slotSideLength*2,topLeftY+slotSideLength*2,slotSideLength,self.boardWindow))
        # Draw slots
        for slot in self.slots:
            pygame.draw.rect(self.boardWindow,(0,0,0),slot.rect,5)

    def getCurrentSlot(self,x,y):
        for slot in self.slots:
            if slot.rect.collidepoint(x,y):
                return slot
        return None

    def isThereWinner(self):
        # For X
        sumRows = [sum(elem) for elem in self.xCounts]
        for elem in sumRows:
            if elem == 3:
                return 'X'


        sumCols = [sum(elem) for elem in zip(*self.xCounts)]
        for elem in sumCols:
            if elem == 3:
                return 'X'

        Diag1 = [r[i] for i, r in enumerate(self.xCounts)]
        sumDiag1 = sum(Diag1)
        if sumDiag1 == 3:
            return 'X'

        Diag2 = [r[-i-1] for i, r in enumerate(self.xCounts)]
        sumDiag2 = sum(Diag2)
        if sumDiag2 == 3:
            return 'X'

        # For O
        sumRows = [sum(elem) for elem in self.oCounts]
        for elem in sumRows:
            if elem == 3:
                return 'O'

        sumCols = [sum(elem) for elem in zip(*self.oCounts)]
        for elem in sumCols:
            if elem == 3:
                return 'O'

        Diag1 = [r[i] for i, r in enumerate(self.oCounts)]
        sumDiag1 = sum(Diag1)
        if sumDiag1 == 3:
            return 'O'

        Diag2 = [r[-i-1] for i, r in enumerate(self.oCounts)]
        sumDiag2 = sum(Diag2)
        if sumDiag2 == 3:
            return 'O'

        return ''

    def finishGame(self,result):
        self.boardWindow.fill((235, 235, 235))
        font = pygame.font.SysFont("papyrus", 192)
        wText = font.render("Winner: ", True, (255, 1, 0))
        self.boardWindow.blit(wText, ( (self.displayInfo.current_w - wText.get_width())//2, wText.get_height() ))

        font = pygame.font.SysFont("papyrus", 492)
        winner = font.render(str(result), True, (255, 1, 0))
        self.boardWindow.blit(winner, ( (self.displayInfo.current_w - winner.get_width())//2, wText.get_height()*2 ))

        font = pygame.font.SysFont("papyrus", 112)
        note = font.render("Press Q to exit the game...", True, (255, 1, 0))
        self.boardWindow.blit(note, ( (self.displayInfo.current_w - note.get_width())//2, (self.displayInfo.current_h/2)+note.get_height() ))



    def handleClick(self,x,y):
        currentSlot = self.getCurrentSlot(x,y)
        if currentSlot != None:
            if currentSlot.hasMark == '':
                print("This is an valid move")
                currentSlot.drawMarker(self.player)
                currentSlot.hasMark = 'X' if self.player==True else 'O'
                if self.player == True:
                    self.xCounts[currentSlot.xIndex][currentSlot.yIndex] = 1
                else:
                    self.oCounts[currentSlot.xIndex][currentSlot.yIndex] = 1
                winner = self.isThereWinner()
                if winner!='':
                    print("Winner: " + str(winner))
                    self.finishGame(winner)
                self.player = not self.player
            else:
                print("This slot is already used")
        else:
            print("You need to click to board and make valid slot selection")

class Slot:
    def __init__(self,xInd,yInd,x,y,oneSideLength,slotWindow):
        self.xIndex = xInd
        self.yIndex = yInd
        self.x = x
        self.y = y
        self.sideLength = oneSideLength
        self.hasMark = ''
        self.rect = pygame.Rect(x,y,oneSideLength,oneSideLength)
        self.slotWindow = slotWindow

    def drawMarker(self,player):
        if player:
            margin = self.sideLength/5
            pygame.draw.line(self.slotWindow,(250,3,0), (self.x+margin,self.y+margin), (self.x+self.sideLength-margin,self.y+self.sideLength-margin), 15)
            pygame.draw.line(self.slotWindow,(250,3,0), (self.x+margin,self.y+self.sideLength-margin), (self.x+self.sideLength-margin,self.y+margin), 15)
        else:
            pygame.draw.circle(self.slotWindow,(250,3,0), (self.rect.centerx,self.rect.centery), int(self.sideLength/3), 15)
