import sys, pygame

# circle R G B X Y

prog = open(sys.argv[1], 'rt').read()
prog = ''.join(prog.split())
prog = list(prog)

i = 0
s = {}

pygame.init()
size = width, height = 256,256
screen = pygame.display.set_mode(size)
pygame.display.set_caption("crumb window")

def resolve(v):
    # intentionally, user can overide numeric constants
    if v in s.keys():
        return s[v]
    else:
        if not v in '0123456789abcdefABCDEF':
            print("Undefined var %s." % v)
            exit(1)
        return int(v,16)

def evalNextExpr(prog, i, s):
    if prog[i] == 'v':
        s.update({prog[i+1]: resolve(prog[i+2])})
        i += 3
    elif prog[i] == 'a':
        s[prog[i+1]] += resolve(prog[i+2])
        s[prog[i+1]] = s[prog[i+1]] % 256
        i += 3
    elif prog[i] == 's':
        s[prog[i+1]] -= resolve(prog[i+2])
        s[prog[i+1]] = s[prog[i+1]] % 256
        i += 3
    elif prog[i] == 'm':
        s[prog[i+1]] *= resolve(prog[i+2])
        s[prog[i+1]] = s[prog[i+1]] % 256
        i += 3
    elif prog[i] == 'd':
        s[prog[i+1]] //= resolve(prog[i+2])
        s[prog[i+1]] = s[prog[i+1]] % 256
        i += 3
    elif prog[i] == 'C':
        screen.fill(
            (resolve(prog[i+1]),
             resolve(prog[i+2]),
             resolve(prog[i+3]))
        )
        i += 4
    elif prog[i] == 'c':
        pygame.draw.circle(screen,
        (resolve(prog[i+1]),resolve(prog[i+2]),resolve(prog[i+3])),
        (resolve(prog[i+4]),resolve(prog[i+5])),
        resolve(prog[i+6]))
        i += 7
    else:
        print("Unexpected token %s." % prog[i])
        exit(1)

    return i

while prog[i] != 'U':
    i = evalNextExpr(prog, i, s)
# store update loop head
U = i
i += 1

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    while i < len(prog):
        i = evalNextExpr(prog, i, s)

    # return to Update loop
    i = U+1

    #screen.fill((255,255,255))
    #pygame.draw.circle(screen, (0,20,112), (20,20), 10)

    pygame.display.flip()