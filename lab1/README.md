# LFPC_Lab_PP-191
Lab1: Variant 15 [(32+1)-18=15]

VN={S, A, B}, VT={a, b, c},
P={
1. S -> aS
2. S -> bS
3. S -> cA
4. A -> aB
5. B -> aB
6. B -> bB
7. B -> c }

FA= (Q, Σ, δ,q0, F)
Q={q0, q1, q2, q3}; Σ={a, b, c}; q0={q2}; F={q3};

q0={A}; q1={B}; q2={S};
1. δ(q2,a)={q2}; 
2. δ(q2,b)={q2}; 
3. δ(q2,c)={q0}; 
4. δ(q0,a)={q1};
5. δ(q1,a)={q1};
6. δ(q1,b)={q1};
7. δ(q1,c)={q3}.

![alt_image](https://westeurope1-mediap.svc.ms/transform/thumbnail?provider=spo&inputFormat=png&cs=fFNQTw&docid=https%3A%2F%2Futm-my.sharepoint.com%3A443%2F_api%2Fv2.0%2Fdrives%2Fb!y6MwbFI-kUGmQV0u5PrmxsbeXfZxaptDrmIyBQHgyf6FBIBUyIBlQqUbQk45vTjK%2Fitems%2F01TQG3XYBGMP7SEBEK3VD2DPCGWZFA7DCH%3Fversion%3DPublished&access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTBmZjEtY2UwMC0wMDAwMDAwMDAwMDAvdXRtLW15LnNoYXJlcG9pbnQuY29tQDFiNmQxZjQ4LTg4OTMtNDg4OS1iZGJmLTFmYjg0MWJjYWU0NiIsImlzcyI6IjAwMDAwMDAzLTAwMDAtMGZmMS1jZTAwLTAwMDAwMDAwMDAwMCIsIm5iZiI6IjE2MjE5NTQ4MDAiLCJleHAiOiIxNjIxOTc2NDAwIiwiZW5kcG9pbnR1cmwiOiJlVGhCUmY2Z0p3Z2lQd1RCZGUrS3VlM0pJa0hCVzJvMk02dXRzamNHNlA4PSIsImVuZHBvaW50dXJsTGVuZ3RoIjoiMTEzIiwiaXNsb29wYmFjayI6IlRydWUiLCJ2ZXIiOiJoYXNoZWRwcm9vZnRva2VuIiwic2l0ZWlkIjoiTm1Nek1HRXpZMkl0TTJVMU1pMDBNVGt4TFdFMk5ERXROV1F5WldVMFptRmxObU0yIiwic2lnbmluX3N0YXRlIjoiW1wia21zaVwiXSIsIm5hbWVpZCI6IjAjLmZ8bWVtYmVyc2hpcHxwb3Blc2N1LnBhdWxhQGlzYS51dG0ubWQiLCJuaWkiOiJtaWNyb3NvZnQuc2hhcmVwb2ludCIsImlzdXNlciI6InRydWUiLCJjYWNoZWtleSI6IjBoLmZ8bWVtYmVyc2hpcHwxMDAzMjAwMDYxZTY4ODE3QGxpdmUuY29tIiwidHQiOiIwIiwidXNlUGVyc2lzdGVudENvb2tpZSI6IjMifQ.K0ExTU5mbFpSYW9FVDFiK3U0Tm1uSkpPbFlvaW0rYkQ1K2wyd0VaaXJTWT0&encodeFailures=1&width=1920&height=854&srcWidth=&srcHeight=)
