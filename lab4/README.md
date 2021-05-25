# LFPC_Lab_PP-191
Lab4: Variant 15 [(32+1)-18=15]

![alt text](https://westeurope1-mediap.svc.ms/transform/thumbnail?provider=spo&inputFormat=png&cs=fFNQTw&docid=https%3A%2F%2Futm-my.sharepoint.com%3A443%2F_api%2Fv2.0%2Fdrives%2Fb!y6MwbFI-kUGmQV0u5PrmxsbeXfZxaptDrmIyBQHgyf6FBIBUyIBlQqUbQk45vTjK%2Fitems%2F01TQG3XYE4RQCFTFX23RA2HIIC5GXB662P%3Fversion%3DPublished&access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTBmZjEtY2UwMC0wMDAwMDAwMDAwMDAvdXRtLW15LnNoYXJlcG9pbnQuY29tQDFiNmQxZjQ4LTg4OTMtNDg4OS1iZGJmLTFmYjg0MWJjYWU0NiIsImlzcyI6IjAwMDAwMDAzLTAwMDAtMGZmMS1jZTAwLTAwMDAwMDAwMDAwMCIsIm5iZiI6IjE2MjE5NjU2MDAiLCJleHAiOiIxNjIxOTg3MjAwIiwiZW5kcG9pbnR1cmwiOiJlVGhCUmY2Z0p3Z2lQd1RCZGUrS3VlM0pJa0hCVzJvMk02dXRzamNHNlA4PSIsImVuZHBvaW50dXJsTGVuZ3RoIjoiMTEzIiwiaXNsb29wYmFjayI6IlRydWUiLCJ2ZXIiOiJoYXNoZWRwcm9vZnRva2VuIiwic2l0ZWlkIjoiTm1Nek1HRXpZMkl0TTJVMU1pMDBNVGt4TFdFMk5ERXROV1F5WldVMFptRmxObU0yIiwic2lnbmluX3N0YXRlIjoiW1wia21zaVwiXSIsIm5hbWVpZCI6IjAjLmZ8bWVtYmVyc2hpcHxwb3Blc2N1LnBhdWxhQGlzYS51dG0ubWQiLCJuaWkiOiJtaWNyb3NvZnQuc2hhcmVwb2ludCIsImlzdXNlciI6InRydWUiLCJjYWNoZWtleSI6IjBoLmZ8bWVtYmVyc2hpcHwxMDAzMjAwMDYxZTY4ODE3QGxpdmUuY29tIiwidHQiOiIwIiwidXNlUGVyc2lzdGVudENvb2tpZSI6IjMifQ.Skc3L0RkZ3BxUU1ndDB6dHdKQXZuK3NXc1lNWWtjKzRQNDZVOUszWTIxMD0&encodeFailures=1&width=1920&height=854&srcWidth=&srcHeight=)

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

<pre>
----- FIRST and FOLLOW table------ <br />
----|   FIRST:   |   FOLLOW:   | <br />
S 	 a    		$ <br />
A 	 a    		g <br />
B 	 e    		g <br />
C 	 e    		d <br />
D 	 e    		$ <br />
X 	 #,f		d <br />
</pre>

<pre>
----------Parsing table:-----------
    a    b    c    d    e    f    g
S   Ag
A   abcB
B                       Cd
C                       eX
D                       e
X                  #         fDX
</pre>

<pre>
---------Analysing the string abcefedg----------
Production			Derivation
				S
S->Ag				Ag
A->abcB				abcBg
B->Cd				abcCdg
C->eX				abceXdg
X->fDX				abcefDXdg
D->e				abcefeXdg
X->#				abcefedg
</pre>

