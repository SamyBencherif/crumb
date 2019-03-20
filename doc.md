```
Ops

v		variable     VARNAME   VALUE

a		addition     DEST    OP
s		subtraction    DEST   OP
m		multiplication     DEST   OP
d		integer division   DEST   OP

c		circle   COLORRED COLORGREEN COLORBLUE POSX POSY RADIUS

C		clear   COLORRED COLORGREEN COLORBLUE

U		U loop address marker should only be 1; everything after this is executed once per frame

f		conditional jump  LOW HIGH  MEGASEGMENT SUPERSEGMENT SEGMENT MICROSEGMENT


example:
`vx0`
creates a variable called x initialized at 0

`c12300f`
renders a circle with rgb color (1,2,3) at position (0,0) with radius f (hexadecimal 15)

notes:
a conditional jump (f) comes with 6 arguments x y a_0 a_1 a_2 a_3.
the jump occurs if and only if x < y. The program will jump to the address formed by 0x1000*a_0 + 0x100*a_1 + 0x10*a_2 + 0x1*a_3
The program's memory is indexed from 0 <= M <= len(PROG)
Any jumps outside of memory will cause wrap around.

Variables/Video Buffer are stored elsewhere.
```