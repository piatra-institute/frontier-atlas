# Explicit length-11 algorithm over \(\mathbb F_2\)

Let

\[
A=\begin{pmatrix}a&b\\c&d\end{pmatrix},\qquad
B=\begin{pmatrix}e&f&g\\h&i&j\end{pmatrix}.
\]

All additions below are in \(\mathbb F_2\), so subtraction and addition coincide.

\[
\begin{aligned}
p_1&=(a+d)(e+i), &p_2&=(c+d)e,\\
p_3&=a(f+i), &p_4&=d(h+e),\\
p_5&=(a+b)i, &p_6&=(c+a)(e+f),\\
p_7&=(b+d)(h+i),\\
p_8&=ag, &p_9&=bj,\\
p_{10}&=cg, &p_{11}&=dj.
\end{aligned}
\]

Recover

\[
AB=\begin{pmatrix}
p_1+p_4+p_5+p_7 & p_3+p_5 & p_8+p_9\\
p_2+p_4 & p_1+p_2+p_3+p_6 & p_{10}+p_{11}
\end{pmatrix}.
\]

The first seven products are Strassen's \(2\times2\) scheme applied to columns 0 and 1; the last four are the two length-2 dot products for column 2. `verify_upper.py` checks the full 144-entry tensor identity and all 1,024 input pairs.
