AFC = 16
BFC = 16
CFC = 16
DFC = 17

def PrintVars(A, B, C, D):
	return " A " + str(A) + " B " + str(B) + " C " + str(C) + " D " + str(D) + "\n"

def PrintTUpdate(T, V, A, B, C, D, VAL):
	return "<T" + str(T) + ", " + V + ", " + str(VAL) + ">" + PrintVars(A, B, C, D)

def PrintTUpdateUR(T, V, A, B, C, D, OVAL, NVAL):
	return "<T" + str(T) + ", " + V + ", " + str(OVAL) + ", " + \
			str(NVAL) + ">" + PrintVars(A, B, C, D)

def Undo(dA, dB, dC, dD):
	A = dA
	B = dB
	C = dC
	D = dD

	f = open('../log/5.txt_undo', 'w')
	lines = []

	lines.append("<start T1>" + PrintVars(A, B, C, D))
	t = dA
	t = t*2
	lines.append(PrintTUpdate(1, "A", t, B, C, D, A))
	A = t
	t = dB
	t = t*2
	lines.append("<start T2>" + PrintVars(A, B, C, D))
	t1 = dC
	t2 = dD
	t1 = t1 + t2
	lines.append(PrintTUpdate(2, "C", A, B, t1, D, C))
	C = t1
	t1 = t1 - t2
	lines.append("<start T3>" + PrintVars(A, B, C, D))
	t3 = dD
	t3 = t3 + 1	
	lines.append(PrintTUpdate(3, "C", A, B, t3, D, C))
	C = t3
	t3 = dC
	t3 = t3 + 1
	
	lines.append(PrintTUpdate(1, "B", A, t, C, D, B))
	B = t
	lines.append("<commit T1>" + PrintVars(A, B, C, D))
	t1 = t1 + t2
	lines.append(PrintTUpdate(2, "D", A, B, C, t1, D))
	D = t1
	lines.append("<commit T2>" + PrintVars(A, B, C, D))
	lines.append(PrintTUpdate(3, "D", A, B, C, t3, D))
	D = t3
	lines.append("<commit T3>" + PrintVars(A, B, C, D))
	
	if A == AFC and B == BFC and C == CFC and D == DFC:
		lines.append("1\n")

	f.writelines(lines)

def Redo(dA, dB, dC, dD):
	A = dA
	B = dB
	C = dC
	D = dD

	f = open('../log/5.txt_redo', 'w')
	lines = []

	lines.append("<start T1>" + PrintVars(A, B, C, D))
	t = dA
	t = t*2
	A = t
	lines.append(PrintTUpdate(1, "A", A, B, C, D, A))
	t = dB
	t = t*2
	lines.append("<start T2>" + PrintVars(A, B, C, D))
	t1 = dC
	t2 = dD
	t1 = t1 + t2
	C = t1
	lines.append(PrintTUpdate(2, "C", A, B, C, D, C))
	t1 = t1 - t2
	lines.append("<start T3>" + PrintVars(A, B, C, D))
	t3 = dD
	t3 = t3 + 1
	C = t3
	lines.append(PrintTUpdate(3, "C", A, B, C, D, C))
	t3 = dC
	t3 = t3 + 1
	
	B = t
	lines.append(PrintTUpdate(1, "B", A, B, C, D, B))
	lines.append("<commit T1>" + PrintVars(A, B, C, D))
	t1 = t1 + t2
	D = t1
	lines.append(PrintTUpdate(2, "D", A, B, C, D, D))
	lines.append("<commit T2>" + PrintVars(A, B, C, D))
	D = t3
	lines.append(PrintTUpdate(3, "D", A, B, C, D, D))
	lines.append("<commit T3>" + PrintVars(A, B, C, D))	
	
	if A == AFC and B == BFC and C == CFC and D == DFC:
		lines.append("1\n")

	f.writelines(lines)

def UndoRedo(dA, dB, dC, dD):
	A = dA
	B = dB
	C = dC
	D = dD

	f = open('../log/5.txt_undoredo', 'w')
	lines = []

	lines.append("<start T1>" + PrintVars(A, B, C, D))
	t = dA
	t = t*2
	lines.append(PrintTUpdateUR(1, "A", t, B, C, D, A, t))
	A = t
	t = dB
	t = t*2
	lines.append("<start T2>" + PrintVars(A, B, C, D))
	t1 = dC
	t2 = dD
	t1 = t1 + t2
	lines.append(PrintTUpdateUR(2, "C", A, B, t1, D, C, t1))
	C = t1
	t1 = t1 - t2
	lines.append("<start T3>" + PrintVars(A, B, C, D))
	t3 = dD
	t3 = t3 + 1
	lines.append(PrintTUpdateUR(3, "C", A, B, t3, D, C, t3))
	C = t3
	t3 = dC
	t3 = t3 + 1
	
	lines.append(PrintTUpdateUR(1, "B", A, t, C, D, B, t))
	B = t
	lines.append("<commit T1>" + PrintVars(A, B, C, D))
	t1 = t1 + t2
	lines.append(PrintTUpdateUR(2, "D", A, B, C, t1, D, t1))	
	D = t1
	lines.append("<commit T2>" + PrintVars(A, B, C, D))
	lines.append(PrintTUpdateUR(3, "D", A, B, C, t3, D, t3))
	D = t3
	lines.append("<commit T3>" + PrintVars(A, B, C, D))

	if A == AFC and B == BFC and C == CFC and D == DFC:
		lines.append("1\n")

	f.writelines(lines)

Undo(8, 8, 5, 10)
Redo(8, 8, 5, 10)
UndoRedo(8, 8, 5, 10)