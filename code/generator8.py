AFC = 16
BFC = 16
CFC = 16
DFC = 17

def PrintVars(A, B, C, D):
	return " A " + str(A) + " B " + str(B) + " C " + str(C) + " D " + str(D) + "\n"

def PrintTUpdate(T, V, A, B, C, D, VAL):
	return "<T" + str(T) + "," + V + "," + str(VAL) + ">" + PrintVars(A, B, C, D)

def PrintTUpdateUR(T, V, A, B, C, D, OVAL, NVAL):
	return "<T" + str(T) + "," + V + "," + str(OVAL) + "," + \
			str(NVAL) + ">" + PrintVars(A, B, C, D)

def OneUndo(dA, dB, dC, dD):
	A = dA
	B = dB
	C = dC
	D = dD

	f = open('../log/8.txt_undo', 'w')
	lines = []

	lines.append("<START T1>" + PrintVars(A, B, C, D))
	t = A
	t = t*2
	lines.append(PrintTUpdate(1, "A", t, B, C, D, A))
	A = t
	t = B
	t = t*2
	lines.append(PrintTUpdate(1, "B", A, t, C, D, B))
	B = t
	lines.append("<COMMIT T1>" + PrintVars(A, B, C, D))
	dA = A
	dB = B
	
	lines.append("<START T2>" + PrintVars(A, B, C, D))
	t1 = C
	t2 = D
	t1 = t1 + t2
	lines.append(PrintTUpdate(2, "C", A, B, t1, D, C))
	C = t1
	t1 = t1 - t2
	t1 = t1 + t2
	lines.append(PrintTUpdate(2, "D", A, B, C, t1, D))
	D = t1
#	lines.append("<COMMIT T2>" + PrintVars(A, B, C, D))
	dC = C
#	dD = D

	lines.append("<START T3>" + PrintVars(A, B, C, D))
	t3 = D
#	print t3
	t3 = t3 + 1
#	print t3
	lines.append(PrintTUpdate(3, "C", A, B, t3, D, C))
	C = t3
	t3 = C
	t3 = t3 + 1
#	print t3
	lines.append(PrintTUpdate(3, "D", A, B, C, t3, D))
	D = t3
	lines.append("<COMMIT T3>" + PrintVars(A, B, C, D))
	lines.append("<COMMIT T2>" + PrintVars(A, B, C, D))
	dD = D

	if A == AFC and B == BFC and C == CFC and D == DFC:
		lines.append("8\n")

	f.writelines(lines)

def OneRedo(dA,dB,dC,dD):
	A = dA
	B = dB
	C = dC
	D = dD

	f = open('../log/8.txt_redo', 'w')
	lines = []

	lines.append("<START T1>" + PrintVars(A, B, C, D))
	t = A
	t = t*2
	lines.append(PrintTUpdate(1, "A", t, B, C, D, t))
	A = t
	t = B
	t = t*2
	lines.append(PrintTUpdate(1, "B", A, t, C, D, t))
	B = t
	lines.append("<COMMIT T1>" + PrintVars(A, B, C, D))
	dA = A
	dB = B
	
	lines.append("<START T2>" + PrintVars(A, B, C, D))
	t1 = C
	t2 = D
	t1 = t1 + t2
	lines.append(PrintTUpdate(2, "C", A, B, t1, D, t1))
	C = t1
	t1 = t1 - t2
	t1 = t1 + t2
	lines.append(PrintTUpdate(2, "D", A, B, C, t1, t1))
	D = t1
	lines.append("<COMMIT T2>" + PrintVars(A, B, C, D))
	dC = C
	dD = D

	lines.append("<START T3>" + PrintVars(A, B, C, D))
	t3 = D
#	print t3
	t3 = t3 + 1
#	print t3
	lines.append(PrintTUpdate(3, "C", A, B, t3, D, t3))
	C = t3
	t3 = C
	t3 = t3 + 1
#	print t3
	lines.append(PrintTUpdate(3, "D", A, B, C, t3, t3))
	D = t3
	lines.append("<COMMIT T3>" + PrintVars(A, B, C, D))
#	lines.append("<COMMIT T2>" + PrintVars(A, B, C, D))
#	dD = D

	if A == AFC and B == BFC and C == CFC and D == DFC:
		lines.append("8\n")

	f.writelines(lines)

def OneUndoRedo(dA,dB,dC,dD):
	A = dA
	B = dB
	C = dC
	D = dD

	f = open('../log/8.txt_undoredo', 'w')
	lines = []

	lines.append("<START T1>" + PrintVars(A, B, C, D))
	t = A
	t = t*2
	lines.append(PrintTUpdateUR(1, "A", t, B, C, D, A, t))
	A = t
	t = B
	t = t*2
	lines.append(PrintTUpdateUR(1, "B", A, t, C, D, B, t))
	B = t
	lines.append("<COMMIT T1>" + PrintVars(A, B, C, D))
	dA = A
	dB = B
	
	lines.append("<START T2>" + PrintVars(A, B, C, D))
	t1 = C
	t2 = D
	t1 = t1 + t2
	lines.append(PrintTUpdateUR(2, "C", A, B, t1, D, C, t1))
	C = t1
	t1 = t1 - t2
	t1 = t1 + t2
	lines.append(PrintTUpdateUR(2, "D", A, B, C, t1, D, t1))
	D = t1
#	lines.append("<COMMIT T2>" + PrintVars(A, B, C, D))
	dC = C
#	dD = D

	lines.append("<START T3>" + PrintVars(A, B, C, D))
	t3 = D
#	print t3
	t3 = t3 + 1
#	print t3
	lines.append(PrintTUpdateUR(3, "C", A, B, t3, D, C, t3))
	C = t3
	t3 = C
	t3 = t3 + 1
#	print t3
	lines.append(PrintTUpdateUR(3, "D", A, B, C, t3, D, t3))
	D = t3
	lines.append("<COMMIT T3>" + PrintVars(A, B, C, D))
	lines.append("<COMMIT T2>" + PrintVars(A, B, C, D))
	dD = D

	if A == AFC and B == BFC and C == CFC and D == DFC:
		lines.append("8\n")

	f.writelines(lines)


OneUndo(8, 8, 5, 10)
OneRedo(8,8,5,10)
OneUndoRedo(8,8,5,10)