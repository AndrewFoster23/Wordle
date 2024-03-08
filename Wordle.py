import pygame

pygame.init()
pygame.mixer.init()

size = width, height = 565, 650

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Wordle")

font = pygame.font.SysFont("Arial", 60, bold = True)

def drawText(text, x, y):
    img = font.render(text, True, white)
    screen.blit(img, (x, y))
    
def drawBlocks():
    for i in range(len(boxes)):
        pygame.draw.rect(screen, colors[i], boxes[i])
        
def drawText2():
    count = 0
    row = 0
    col = 0
    textPosX2 = 92
    textPosY2 = 75
    textDiff2 = 85.5
    for i in range(len(letters)):
        drawText(letters[i], textPosX2 + textDiff2 * col, textPosY2 + textDiff2 * row)
        textPosX2 += textDiff2
        count += 1
        if count%5 == 0:
            row += 1
            textPosX2 = 92
            col = 0
        

def flipColors(endIndex):
    startIndex = endIndex - 4
    for startIndex in range(5):
        color = checkSame(startIndex)
        colors[startIndex] = color
    
def checkSame(startIndex):
    print(word[startIndex])
    print(letters[startIndex])
    print(startIndex)
    if  letters[startIndex] == word[startIndex]:
        return green
    for i in range(5):
        if letters[startIndex] == word[i]:
            return yellow
    return gray
  
def checkWin(endIndex):
    startIndex = endIndex - 4
    guessWord = ""
    for i in range(5):
        guessWord += word[i]
    if letters[startIndex] == word[startIndex]:
        return True
     
        
word = "CRANE"
currGuess = ""
currRow = 0
currCol = 0
textPosX = 92
textPosY = 75
textDiff = 85.5

black = (0, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
white = (255, 255, 255)
gray = (100, 100, 100)

boxes = [pygame.Rect(75, 75, 75, 75), pygame.Rect(160, 75, 75, 75), pygame.Rect(245, 75, 75, 75), pygame.Rect(330, 75, 75, 75), pygame.Rect(415, 75, 75, 75),
         pygame.Rect(75, 160, 75, 75), pygame.Rect(160, 160, 75, 75), pygame.Rect(245, 160, 75, 75), pygame.Rect(330, 160, 75, 75), pygame.Rect(415, 160, 75, 75),
         pygame.Rect(75, 245, 75, 75), pygame.Rect(160, 245, 75, 75), pygame.Rect(245, 245, 75, 75), pygame.Rect(330, 245, 75, 75), pygame.Rect(415, 245, 75, 75),
         pygame.Rect(75, 330, 75, 75), pygame.Rect(160, 330, 75, 75), pygame.Rect(245, 330, 75, 75), pygame.Rect(330, 330, 75, 75), pygame.Rect(415, 330, 75, 75),
         pygame.Rect(75, 415, 75, 75), pygame.Rect(160, 415, 75, 75), pygame.Rect(245, 415, 75, 75), pygame.Rect(330, 415, 75, 75), pygame.Rect(415, 415, 75, 75),
         pygame.Rect(75, 500, 75, 75), pygame.Rect(160, 500, 75, 75), pygame.Rect(245, 500, 75, 75), pygame.Rect(330, 500, 75, 75), pygame.Rect(415, 500, 75, 75),]


colors = [black, black, black, black, black,
          black, black, black, black, black,
          black, black, yellow, black, black,
          black, black, black, black, black,
          black, black, black, green, black,
          black, black, black, black, black]

letters = ["", "", "", "", "",
           "", "", "", "", "",
           "", "", "", "", "",
           "", "", "", "", "",
           "", "", "", "", "",
           "", "", "", "", ""]
rect1 = pygame.Rect(0, 400 - 100, 150, 100)

clock = pygame.time.Clock()



index = 0
endIndex = 4
lockedIndex = 0



run = True
# Loop
while run:
    clock.tick(60)
    screen.fill((0,0,255))
    
    key = pygame.key.get_pressed()
    
    if letters[endIndex] != "":
        
        if key[pygame.K_RETURN] == True:
            pygame.time.delay(150)
            flipColors(endIndex)
           # checkWin(endIndex)
            endIndex += 5
            lockedIndex += 5
        
        if key[pygame.K_BACKSPACE] == True:
            if index != lockedIndex: 
                index -= 1
            letters[index] = ""
            pygame.time.delay(150)
            
    else:
        if key[pygame.K_BACKSPACE] == True:
            if index != lockedIndex: 
                index -= 1
            letters[index] = ""
            pygame.time.delay(150)
            
        if key[pygame.K_a] == True:
            letters[index] = "A"
            index += 1
            pygame.time.delay(150)
        if key[pygame.K_b] == True:
            letters[index] = "B"
            index += 1
            pygame.time.delay(150)
        if key[pygame.K_c] == True:
            letters[index] = "C"
            index += 1
            pygame.time.delay(150)
        if key[pygame.K_d] == True:
            letters[index] = "D"
            index += 1
            pygame.time.delay(150)
        if key[pygame.K_e] == True:
            letters[index] = "E"
            index += 1
            pygame.time.delay(150)
        if key[pygame.K_f] == True:
            letters[index] = "F"
            index += 1
            pygame.time.delay(150)
        if key[pygame.K_g] == True:
            letters[index] = "G"
            index += 1
            pygame.time.delay(150)
        if key[pygame.K_h] == True:
            letters[index] = "H"
            index += 1
            pygame.time.delay(150)
        if key[pygame.K_i] == True:
            letters[index] = "I"
            index += 1
            pygame.time.delay(150)
        if key[pygame.K_j] == True:
            letters[index] = "J"
            index += 1
            pygame.time.delay(150)
        if key[pygame.K_k] == True:
            letters[index] = "K"
            index += 1
            pygame.time.delay(150)
        if key[pygame.K_l] == True:
            letters[index] = "L"
            index += 1
            pygame.time.delay(150)
        if key[pygame.K_m] == True:
            letters[index] = "M"
            index += 1
            pygame.time.delay(150)
        if key[pygame.K_n] == True:
            letters[index] = "N"
            index += 1
            pygame.time.delay(150)
        if key[pygame.K_o] == True:
            letters[index] = "O"
            index += 1
            pygame.time.delay(150)
        if key[pygame.K_p] == True:
            letters[index] = "P"
            index += 1
            pygame.time.delay(150)
        if key[pygame.K_q] == True:
            letters[index] = "Q"
            index += 1
            pygame.time.delay(150)
        if key[pygame.K_r] == True:
            letters[index] = "R"
            index += 1
            pygame.time.delay(150)
        if key[pygame.K_s] == True:
            letters[index] = "S"
            index += 1
            pygame.time.delay(150)
        if key[pygame.K_t] == True:
            letters[index] = "T"
            index += 1
            pygame.time.delay(150)
        if key[pygame.K_u] == True:
            letters[index] = "U"
            index += 1
            pygame.time.delay(150)
        if key[pygame.K_v] == True:
            letters[index] = "V"
            index += 1
            pygame.time.delay(150)
        if key[pygame.K_w] == True:
            letters[index] = "W"
            index += 1
            pygame.time.delay(150)
        if key[pygame.K_x] == True:
            letters[index] = "X"
            index += 1
            pygame.time.delay(150)
        if key[pygame.K_y] == True:
            letters[index] = "Y"
            index += 1
            pygame.time.delay(150)
        if key[pygame.K_z] == True:
            letters[index] = "Z"
            index += 1
            pygame.time.delay(150)
    
    drawBlocks()
    drawText2()
        
        
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False
           
        
    pygame.display.flip()
    
    
pygame.time.delay(2000)
pygame.quit()
