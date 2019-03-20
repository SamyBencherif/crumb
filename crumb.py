import sys
# import pygame

def execute(prog, PROFILERMODE=True):

    global INTERESTING
    INTERESTING = False

    if not PROFILERMODE:
        import pygame

    ULIMIT=1000

    # when this flag is enabled, instead of running the program
    # crumb attempts to determine if it is interesting ;^D
    BRTHRES = 30
    MAXLOOPS = 1

    prog = ''.join(prog.split())
    prog = list(prog)

    if len(prog) == 0:
        # for lack of a better soln, an empty program terminates without creating an SDL window
        exit()

    # wrap around accessor
    progg = lambda i: prog[i%len(prog)]

    i = 0
    s = {}

    size = width, height = 256, 256
    if not PROFILERMODE:
        pygame.init()
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("crumb window")

    def resolve(v):
        # intentionally, user can overide numeric constants
        if v in s.keys():
            return s[v]
        else:
            if not v in '0123456789abcdefABCDEF':
                # print("Undefined var %s." % v)
                # exit(1)
                s[v] = 0
                return 0
            return int(v,16)

    def evalNextExpr(prog, i, s):
        global INTERESTING
        if prog[i] == 'v':
            s.update({progg(i+1): resolve(progg(i+2))})
            return i + 3
        elif prog[i] == 'a':
            if not progg(i+1) in s.keys():
                s[progg(i+1)] = 0
            s[progg(i+1)] += resolve(progg(i+2))
            s[progg(i+1)] = s[progg(i+1)] % 256
            return i + 3
        elif prog[i] == 's':
            if not progg(i+1) in s.keys():
                s[progg(i+1)] = 0
            s[progg(i+1)] -= resolve(progg(i+2))
            s[progg(i+1)] = s[progg(i+1)] % 256
            return i + 3
        elif prog[i] == 'm':
            if not progg(i+1) in s.keys():
                s[progg(i+1)] = 0
            s[progg(i+1)] *= resolve(progg(i+2))
            s[progg(i+1)] = s[progg(i+1)] % 256
            return i + 3
        elif prog[i] == 'd':
            if not progg(i+1) in s.keys():
                s[progg(i+1)] = 0
            if resolve(progg(i+2)) == 0:
                s[progg(i+1)] = 255
            else:
                s[progg(i+1)] //= resolve(progg(i+2))
            s[progg(i+1)] = s[progg(i+1)] % 256
            return i + 3
        elif prog[i] == 'C':
            if PROFILERMODE:
                if resolve(progg(i+1)) > BRTHRES or resolve(progg(i+2)) > BRTHRES or resolve(progg(i+3)) > BRTHRES:
                    # print("This program is (possibly) interesting! 8~D")
                    INTERESTING = True
                    # exit()
            else:
                screen.fill(
                    (resolve(progg(i+1)),
                    resolve(progg(i+2)),
                    resolve(progg(i+3)))
                )
            return i + 4
        elif prog[i] == 'c':
            if PROFILERMODE:
                if resolve(progg(i+1)) > BRTHRES or resolve(progg(i+2)) > BRTHRES or resolve(progg(i+3)) > BRTHRES:
                    # print("This program is (maybe maybe) interesting! 3^O")
                    INTERESTING = True
                    # exit()
            else:
                pygame.draw.circle(screen,
                (resolve(progg(i+1)),resolve(progg(i+2)),resolve(progg(i+3))),
                (resolve(progg(i+4)),resolve(progg(i+5))),
                resolve(progg(i+6)))
            return i + 7
        elif prog[i] == 'f':
            if resolve(progg(i+1)) < resolve(progg(i+2)):
                loc = 0x1000 * resolve(progg(i+3)) + 0x100 * resolve(progg(i+4)) + 0x10 * resolve(progg(i+5)) + 0x1 * resolve(progg(i+6))
                return loc
            else:
                return i+7
        else:
            if not progg(i) in s.keys():
                s[progg(i)] = 1
            else:
                s[progg(i)] += 1
                s[progg(i)] = s[progg(i)]%256
            return i + 1
            #print("Unexpected token %s at position %i." % (prog[i], i))
            #exit(1)

    while progg(i) != 'U' and i < len(prog):
        i = evalNextExpr(prog, i, s)
    # store update loop head
    U = i
    i += 1

    while MAXLOOPS:

        if PROFILERMODE:
            MAXLOOPS -= 1

        if not PROFILERMODE:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

        guard=0
        while i < len(prog) and guard<ULIMIT:
            i = evalNextExpr(prog, i, s)
            guard += 1

        # return to Update loop
        i = U+1

        if not PROFILERMODE:
            pygame.display.flip()

    if PROFILERMODE:
        return INTERESTING

if __name__ == "__main__":
    execute(open(sys.argv[1], 'rt').read(), PROFILERMODE=False)