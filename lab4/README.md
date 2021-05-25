# LFPC_Lab_PP-191
Lab4: Variant 15 [(32+1)-18=15]

The grammar is left-recursive and I make the changes and in this way the grammar is accepted for parsing.

Initial productions:
1. S->Ag  
2. A->abcB
3. B->Cd  
4. C->e   
5. C->eX  
6. D->e   
7. X->#   
8. X->fDX

1. FIRST and FOLLOW table
	FISRT:    	FOLLOW
S 	 a    		$
A 	 a    		g
B 	 e    		g
C 	 e    		d
D 	 e    		$
X 	 #,f		d


2.Parsing table:
    a    b    c    d    e    f    g
S   Ag
A   abcB
B                       Cd
C                       eX
D                       e
X                  #         fDX

3. Analysing the string abcefedg
Production			Derivation
				S
S->Ag				Ag
A->abcB				abcBg
B->Cd				abcCdg
C->eX				abceXdg
X->fDX				abcefDXdg
D->e				abcefeXdg
X->#				abcefedg


