# LFPC_Lab_PP-191
Lab1: Variant 15 [(32+1)-18=15]

G=(VN, VT, P, S) VN={S, A, B, C, D} VT={a, b}
P={1. S->AC
2. S->bA
3. S->B
4. S->aA
5. A->ε
6. A->aS
7. A->ABab
8. B->a
9. B->bS
10. C->abC
11. D->AB}

1. Remove ε productions
P={1. S->AC
2. S->bA
3. S->B
4. S->aA
5. A->aS
6. A->ABab
7. B->a
8. B->bS
9. C->abC
10. D->AB
11. S->C
12. S->b
13. S->a
14. A->Bab
15. B->B}

2. Remove Unit Productions
P={1. S->AC
2. S->bA
3. S->aA
4. A->aS
5. A->ABab
6. B->a
7. B->bS
8. C->abC
9. D->AB
10. S->b
11. S->a
12. A->Bab
13. S->bS
14. D->a
15. S->abC
16. D->bS}

3. Useless Removal
P={1. S->bA
2. S->aA
3. S->b
4. S->a
5. S->bS
6. A->Bab
7. A->ABab
8. B->bS
9. B->a
10. A->aS}

4. CNF
P={
S -> Z A | Y A | b | a | Z S
A -> A A1 | Y S | B A2
D -> A B | Z S
Z -> b
Y -> a
A1 -> B A2
A2 -> Y Z
B -> Z S
C -> Y B1
B1 -> Z C
S0 -> Z A | Y A | b | a | Z S
}

