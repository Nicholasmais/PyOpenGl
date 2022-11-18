#https://www.youtube.com/watch?v=a4NVQC_2S2U&t=64s&ab_channel=NaseemShah
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import random

global x1,y1, x2,y2, x3,y3, xstep, ystep, rsize, windowWidth, windowHeight, corFundo, corLosango, corCirculo, initialHeight, initalWidth

x1, y1 = 0, 0
x2, y2 = 0, 0
x3, y3 = 0, 0

xstep = 0.1
ystep = 0.1

windowWidth = random.randint(100,1000)
windowHeight = random.randint(100,1000)

rsize = 10

cor_Fundo = [0,.5,0]
cor_Losango = [.8,.8,0]
cor_Circulo = [0,0,.5]

initialWidth = 100
initialHeight = 100

def DesenhaBrasil(flagSize, x, y,
                 corFundo = [0,.5,0],
                 corLosango = [.8,.8,.0],
                 corCirculo = [0,0,.5],
                 width = 100,
                 height = 100):

  global x1,y1, x2,y2, x3,y3, xstep, ystep, rsize, windowWidth, windowHeight

  glColor3f(corFundo[0], corFundo[1], corFundo[2])
  glBegin(GL_QUADS)

  glVertex2f(-1*flagSize*width/100 + x,-1*flagSize*height/100 + y)
  glVertex2f(-1*flagSize*width/100 + x,1*flagSize*height/100 + y)
  glVertex2f(1*flagSize*width/100 + x,1*flagSize*height/100 + y)
  glVertex2f(1*flagSize*width/100 + x,-1*flagSize*height/100 + y)

  glEnd()

  glColor3f(corLosango[0], corLosango[1], corLosango[2])
  glBegin(GL_QUADS)

  glVertex2f(-1*flagSize*width/100/1.5 + x,0*flagSize*height/100/1.5 + y)
  glVertex2f(0*flagSize*width/100/1.5 + x,1*flagSize*height/100/1.5 + y)
  glVertex2f(1*flagSize*width/100/1.5 + x,0*flagSize*height/100/1.5 + y)
  glVertex2f(0*flagSize*width/100/1.5 + x,-1*flagSize*height/100/1.5 + y)

  glEnd()
  
  glColor3f(corCirculo[0], corCirculo[1], corCirculo[2])
  glBegin(GL_QUADS)
  
  glVertex2f(-1*flagSize*width/100/6 + x,-1*flagSize*height/100/6 + y)
  glVertex2f(-1*flagSize*width/100/6 + x,1*flagSize*height/100/6 + y)
  glVertex2f(1*flagSize*width/100/6 + x,1*flagSize*height/100/6 + y)
  glVertex2f(1*flagSize*width/100/6 + x,-1*flagSize*height/100/6 + y)

  glEnd()

def Desenha():
  global x1,y1, x2,y2, x3,y3, xstep, ystep, rsize, windowWidth, windowHeight, cor_Fundo, cor_Losango, cor_Circulo, initialWidth, initialHeight

  glClear(GL_COLOR_BUFFER_BIT)

  glViewport(0,int(windowHeight/2),windowWidth,int(windowHeight / 2))
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()
  gluOrtho2D(-rsize,rsize,-rsize,rsize)
  DesenhaBrasil(1, x1, y1)

  glViewport(0,0,int(windowWidth/2),int(windowHeight / 2))
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()
  gluOrtho2D(-rsize,rsize,-rsize,rsize)
  DesenhaBrasil(4,x2, y2, corFundo = cor_Fundo,
                          corLosango = cor_Losango,
                          corCirculo = cor_Circulo,
                          width = initialWidth,
                          height = initialHeight)

  glViewport(int(windowWidth/2),0,int(windowWidth/2),int(windowHeight / 2))
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()
  gluOrtho2D(-rsize,rsize,-rsize,rsize)
  DesenhaBrasil(2, x3, y3)

  glutSwapBuffers()

def Inicializa():
  glClearColor(255,255,255,1)

def Timer(value):
  global x1,y1, x2,y2, x3,y3, xstep, ystep, rsize, windowWidth, windowHeight

  if abs(x1) > rsize-1:
    xstep *= -1

  if abs(y1) > rsize-1:
    ystep *= -1

  x1 += xstep
  y1 += 1.5*ystep
  glutPostRedisplay()
  glutTimerFunc(33, Timer, 1)

def Teclado(key, x, y):
  global x1,y1, x2,y2, x3,y3, xstep, ystep, rsize, windowWidth, windowHeight

  match key:
    case b"w":
      y3 += abs(ystep)
    case b"a":
      x3 -= abs(xstep)
    case b"s":
      y3 -= abs(ystep)
    case b"d":
      x3 += abs(xstep)

    
  glutPostRedisplay()

def Mouse(button, state, x, y):
  global x1,y1, x2,y2, x3,y3, xstep, ystep, rsize, windowWidth, windowHeight
  if button == GLUT_LEFT_BUTTON:
    if state == GLUT_DOWN:
      x3 = 4*rsize/windowWidth * x - 3*rsize
      y3 = -4*rsize/windowHeight*y + 3*rsize

  glutPostRedisplay()

def Responsivo(width, height):
  global x1,y1, x2,y2, x3,y3, xstep, ystep, rsize, windowWidth, windowHeight
  windowWidth = width
  windowHeight = height

def alterarCorFundo(op):
  global x1,y1, x2,y2, x3,y3, xstep, ystep, rsize, windowWidth, windowHeight, corFundo, corLosango, corCirculo

  match op:
    case 0:
      corFundo = [1,0,0]
    case 1:
      corFundo = [0,1,0]
    case 2:
      corFundo = [0,0,1]

  glutPostRedisplay()
  return 0

def alterarCorFundo(op):
  global x1,y1, x2,y2, x3,y3, xstep, ystep, rsize, windowWidth, windowHeight, cor_Fundo, cor_Losango, cor_Circulo

  match op:
    case 0:
      cor_Fundo = [1,0,0]
    case 1:
      cor_Fundo = [0,1,0]
    case 2:
      cor_Fundo = [0,0,1]

  glutPostRedisplay()
  return 0

def alterarCorLosango(op):
  global x1,y1, x2,y2, x3,y3, xstep, ystep, rsize, windowWidth, windowHeight, cor_Fundo, cor_Losango, cor_Circulo

  match op:
    case 0:
      cor_Losango = [1,0,0]
    case 1:
      cor_Losango = [0,1,0]
    case 2:
      cor_Losango = [0,0,1]

  glutPostRedisplay()
  return 0

def alterarCorCirculo(op):
  global x1,y1, x2,y2, x3,y3, xstep, ystep, rsize, windowWidth, windowHeight, cor_Fundo, cor_Losango, cor_Circulo

  match op:
    case 0:
      cor_Circulo = [1,0,0]
    case 1:
      cor_Circulo = [0,1,0]
    case 2:
      cor_Circulo = [0,0,1]

  glutPostRedisplay()
  return 0

def changeFlagWidth(val):
  global x1,y1, x2,y2, x3,y3, xstep, ystep, rsize, windowWidth, windowHeight, corFundo, corLosango, corCirculo, initialWidth, initialHeight
  print(windowHeight)
  if val == 0:
    initialWidth += 20
  
  else:
    initialWidth -= 20
  
  glutPostRedisplay()
  return 0

def changeFlagHeight(val):
  global x1,y1, x2,y2, x3,y3, xstep, ystep, rsize, windowWidth, windowHeight, corFundo, corLosango, corCirculo, initialWidth, initialHeight

  if val == 0:
    initialHeight += 20
  
  else:
    initialHeight -= 20

  glutPostRedisplay()
  return 0

def CriaMenu():

  subMenuWidth = glutCreateMenu(changeFlagWidth)
  glutAddMenuEntry("Aumentar", 0)
  glutAddMenuEntry("Diminuir", 1)

  subMenuHeight = glutCreateMenu(changeFlagHeight)
  glutAddMenuEntry("Aumentar", 0)
  glutAddMenuEntry("Diminuir", 1)

  subMenuTamanho = glutCreateMenu(lambda: None)
  glutAddSubMenu("Comprimento", subMenuWidth)
  glutAddSubMenu("Altura", subMenuHeight)
  
  subMenuFundo = glutCreateMenu(alterarCorFundo)
  glutAddMenuEntry("Vermelho", 0)
  glutAddMenuEntry("Verde", 1)
  glutAddMenuEntry("Azul", 2)

  subMenuLosango = glutCreateMenu(alterarCorLosango)
  glutAddMenuEntry("Vermelho", 0)
  glutAddMenuEntry("Verde", 1)
  glutAddMenuEntry("Azul", 2)

  subMenuCirculo = glutCreateMenu(alterarCorCirculo)
  glutAddMenuEntry("Vermelho", 0)
  glutAddMenuEntry("Verde", 1)
  glutAddMenuEntry("Azul", 2)

  subMenuCor = glutCreateMenu(lambda: None)
  glutAddSubMenu("Fundo", subMenuFundo)
  glutAddSubMenu("Losango", subMenuLosango)
  glutAddSubMenu("Circulo", subMenuCirculo)
  


  menu = glutCreateMenu(lambda: None)
  glutAddSubMenu("Alterar tamanho de bandeira.", subMenuTamanho)
  glutAddSubMenu("Mudar cor de bandeira", subMenuCor)
  glutAttachMenu(GLUT_RIGHT_BUTTON)

def main():
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
  glutInitWindowPosition(0,0)
  glutInitWindowSize(windowWidth,windowHeight)
  glutCreateWindow(b"Brasil")
  glutDisplayFunc(Desenha)
  glutReshapeFunc(Responsivo)
  glutKeyboardFunc(Teclado)
  glutMouseFunc(Mouse)
  glutTimerFunc(33, Timer, 1)
  CriaMenu()
  Inicializa()
  glutMainLoop()

main()
