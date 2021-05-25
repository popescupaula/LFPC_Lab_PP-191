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

![alt_image](https://utm-my.sharepoint.com/:i:/g/personal/popescu_paula_isa_utm_md/ESZj_yIEit1HobxGtkoPjEcBA73IBRA14dFxi6sIWMVE2Q?e=LQv8nV)
