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

def OneUndo(dA, dB, dC, dD):
	A = dA
	B = dB
	C = dC
	D = dD

	f = open('../log/1.txt_undo', 'w')
	lines = []

	lines.append("<start T1>" + PrintVars(A, B, C, D))
	t = dA
	lines.append("<start T2>" + PrintVars(A, B, C, D))
	t1 = dC
	lines.append("<start T3>" + PrintVars(A, B, C, D))
	t3 = dD

	t = t*2
	t2 = dD
	t3 = t3 + 1

	lines.append(PrintTUpdate(1, "A", t, B, C, D, A))
	A = t
	t1 = t1 + t2
	lines.append(PrintTUpdate(3, "C", A, B, t3, D, C))
	C = t3

	t = dB
	lines.append(PrintTUpdate(2, "C", A, B, t1, D, C))
	C = t1
	t3 = dC

	t = t*2
	t1 = t1 - t2
	t3 = t3 + 1

	lines.append(PrintTUpdate(1, "B", A, t, C, D, B))
	B = t
	t1 = t1 + t2
	lines.append(PrintTUpdate(3, "D", A, B, C, t3, D))
	D = t3

	lines.append(PrintTUpdate(2, "D", A, B, C, t1, D))
	D = t1

	lines.append("<commit T1>" + PrintVars(A, B, C, D))
	lines.append("<commit T2>" + PrintVars(A, B, C, D))
	lines.append("<commit T3>" + PrintVars(A, B, C, D))

	if A == AFC and B == BFC and C == CFC and D == DFC:
		lines.append("1\n")

	f.writelines(lines)

def OneRedo(dA, dB, dC, dD):
	A = dA
	B = dB
	C = dC
	D = dD

	f = open('../log/1.txt_redo', 'w')
	lines = []

	lines.append("<start T1>" + PrintVars(A, B, C, D))
	t = dA
	lines.append("<start T2>" + PrintVars(A, B, C, D))
	t1 = dC
	lines.append("<start T3>" + PrintVars(A, B, C, D))
	t3 = dD

	t = t*2
	t2 = dD
	t3 = t3 + 1

	A = t
	lines.append(PrintTUpdate(1, "A", A, B, C, D, A))
	t1 = t1 + t2
	C = t3
	lines.append(PrintTUpdate(3, "C", A, B, C, D, C))

	t = dB
	C = t1
	lines.append(PrintTUpdate(2, "C", A, B, C, D, C))
	t3 = dC

	t = t*2
	t1 = t1 - t2
	t3 = t3 + 1

	B = t
	lines.append(PrintTUpdate(1, "B", A, B, C, D, B))
	t1 = t1 + t2
	D = t3
	lines.append(PrintTUpdate(3, "D", A, B, C, D, D))

	D = t1
	lines.append(PrintTUpdate(2, "D", A, B, C, D, D))

	lines.append("<commit T1>" + PrintVars(A, B, C, D))
	lines.append("<commit T2>" + PrintVars(A, B, C, D))
	lines.append("<commit T3>" + PrintVars(A, B, C, D))

	if A == AFC and B == BFC and C == CFC and D == DFC:
		lines.append("1\n")

	f.writelines(lines)

def OneUndoRedo(dA, dB, dC, dD):
	A = dA
	B = dB
	C = dC
	D = dD

	f = open('../log/1.txt_undoredo', 'w')
	lines = []

	lines.append("<start T1>" + PrintVars(A, B, C, D))
	t = dA
	lines.append("<start T2>" + PrintVars(A, B, C, D))
	t1 = dC
	lines.append("<start T3>" + PrintVars(A, B, C, D))
	t3 = dD

	t = t*2
	t2 = dD
	t3 = t3 + 1

	lines.append(PrintTUpdateUR(1, "A", t, B, C, D, A, t))
	A = t
	t1 = t1 + t2
	lines.append(PrintTUpdateUR(3, "C", A, B, t3, D, C, t3))
	C = t3

	t = dB
	lines.append(PrintTUpdateUR(2, "C", A, B, t1, D, C, t1))
	C = t1
	t3 = dC

	t = t*2
	t1 = t1 - t2
	t3 = t3 + 1

	lines.append(PrintTUpdateUR(1, "B", A, t, C, D, B, t))
	B = t
	t1 = t1 + t2
	lines.append(PrintTUpdateUR(3, "D", A, B, C, t3, D, t3))
	D = t3

	lines.append(PrintTUpdateUR(2, "D", A, B, C, t1, D, t1))	
	D = t1
	
	lines.append("<commit T1>" + PrintVars(A, B, C, D))
	lines.append("<commit T2>" + PrintVars(A, B, C, D))
	lines.append("<commit T3>" + PrintVars(A, B, C, D))

	if A == AFC and B == BFC and C == CFC and D == DFC:
		lines.append("1\n")

	f.writelines(lines)

OneUndo(8, 8, 5, 10)
OneRedo(8, 8, 5, 10)
OneUndoRedo(8, 8, 5, 10)