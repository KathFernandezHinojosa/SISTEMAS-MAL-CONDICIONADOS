import numpy as np

A = np.array([[1.0001, 2, 3],[1, 2, 3],[1, 2, 3.0001]])
B = np.array([[1],[1],[1]])
print("Matriz A: \n"+str(A))
print("Vector B: \n"+str(B))

inv_A = np.linalg.inv(A)
print("\nMatriz_inversa de A: \n"+str(inv_A))

ident_A=A.dot(inv_A)
print("\nIdentidad: \n"+str(ident_A))

cond_A = np.linalg.cond(A)
print("\nCondicional ===> cond="+str(cond_A))

det_A = np.linalg.det (A)
print("\nDeterminante ===> det="+str(det_A)+"\n")
