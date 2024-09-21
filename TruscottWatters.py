#pylint:disable=W0613
from queue import deque

""" Charles Truscott Watters, developing my own algorithm to solve the Rubik's cube 2 x 2 Byron Bay NSW 2481. Thank you John Flynn Hospital and Byron Bay Hospital. Thank you MITx, MIT OCW and Harvard CCE """

""" Thank you Byron Central Hospital Tuckeroo. Thank you Eric Grimson, John Guttag and Ana Bell and all at MITx """


# Need to review and refactor all class attributes and methods, to make sure they are sensible for solving the array of cubits

# 21st September 2024

""" Top Left Front, Top Right Front, Bottom Left Front, Bottom Right Front, Top Left Back, Top Right Back, Bottom Right Back, Bottom Left Back """
class RubiksState(object):
	def __init__(self, tlf, trf, blf, brf, tlb, blb, trb, brb, moves):
#	def __init__(self, left_face, front_face, right_face, back_face, top_face, down_face, moves):
#		self.tlf = [0] * 3
#		self.trf= [0] * 3
#		self.blf = [0] * 3
#		self.brf= [0] * 3
#		self.tlb = [0] * 3
#		self.trb= [0] * 3
#		self.brb = [0] * 3
#		self.blb= [0] * 3
#		
		self.tlf = tlf
		self.trf = trf
		self.blf = blf
		self.brf = brf
		self.tlb = tlb
		self.blb = blb
		self.trb = trb
		self.brb = brb

		self.left_face = [self.tlf[1], self.tlb[1], self.blb[1], self.blf[1]]
		self.front_face = [self.tlf[2], self.blf[2], self.trf[2], self.brf[2]]
		self.right_face = [self.trf[1], self.trb[1], self.brf[1], self.brb[1]]
		self.back_face = [self.tlb[2], self.trb[2], self.blb[2], self.brb[2]]
		self.top_face = [self.tlb[0], self.trb[0], self.tlf[0], self.trf[0]]
		self.down_face = [self.blb[0], self.brb[0], self.blf[0], self.brf[0]]
		self.moves = moves

	def L(self):
		""" Top Left Front to Bottom Left Front.
Bottom Left Front to Bottom Left Back
Bottom Left Back to Top Left Back
Top Left Back to Top Left Front """
# Aaaah, Erroneous decision 
	# Indices 0, 1, 2 to 2, 1, 0 (mapping)
		ttlf = self.tlf.copy()
		tblf = self.blf.copy()
		ttrf = self.trf.copy()
		tbrf = self.brf.copy()
		ttlb = self.tlb.copy()
		tblb = self.blb.copy()
		ttrb = self.trb.copy()
		tbrb = self.brb.copy()
		nblf = [0] * 3
		nblb = [0] * 3
		ntlb = [0] * 3
		ntlf = [0] * 3
		nblf[2], nblf[1], nblf[0] = ttlf[0], ttlf[1], ttlf[2] # Bottom Left Front becomes Top Left Front
		nblb[2], nblb[1], nblb[0] = tblf[0], tblf[1], tblf[2] # Bottom Left Back becomes Bottom Left Front
		ntlb[2], ntlb[1], ntlb[0] = tblb[0], tblb[1], tblb[2] #  Top Left Back becomes Bottom Left Back
		ntlf[2], ntlf[1], ntlf[0] = ttlb[0], ttlb[1], ttlb[2]
		# Top Left Front becomes Top Left Back
		elcopy = self.moves.copy()
		elcopy.append("L")
		# tlf, trf, blf, brf, tlb, blb, trb, brb, moves):
		return RubiksState(ntlf.copy(), ttrf.copy(), nblf.copy(), tbrf.copy(), ntlb.copy(), nblb.copy(), ttrb.copy(), tbrb.copy(), elcopy)
	def L2(self):
		""" Bottom Left Back to Top Left Front. Top Left Front to Bottom Left Back. Bottom Left Front to Top Left Back. Top Left Back to Bottom Left Front """
		ttlf = self.tlf.copy()
		tblf = self.blf.copy()
		ttrf = self.trf.copy()
		tbrf = self.brf.copy()
		ttlb = self.tlb.copy()
		tblb = self.blb.copy()
		ttrb = self.trb.copy()
		tbrb = self.brb.copy()
		nblf = [0] * 3
		nblb = [0] * 3
		ntlb = [0] * 3
		ntlf = [0] * 3
		nblb[0], nblb[1], nblb[2] = ttlf[0], ttlf[1], ttlf[2]
		ntlf[0], ntlf[1], ntlf[2] = tblb[0], tblb[1], tblb[2]
		nblf[0], nblf[1], nblf[2] = ttlb[0], ttlb[1], ttlb[2]
		ntlb[0], ntlb[1], ntlb[2] = tblf[0], tblf[1], tblf[2]
		elcopy = self.moves.copy()
		elcopy.append("L2")
		# tlf, trf, blf, brf, tlb, blb, trb, brb, moves):
		return RubiksState(ntlf.copy(), ttrf.copy(), nblf.copy(), tbrf.copy(), ntlb.copy(), nblb.copy(), ttrb.copy(), tbrb.copy(), elcopy)
	def Linverse(self):
		""" Top Left Front takes on the value of Bottom Left Front. Top Left Back takes on Top Left Front. Bottom Left Back Takes on Top Left Back. Bottom Left Front takes on Bottom Left Back """
		ttlf = self.tlf.copy()
		tblf = self.blf.copy()
		ttrf = self.trf.copy()
		tbrf = self.brf.copy()
		ttlb = self.tlb.copy()
		tblb = self.blb.copy()
		ttrb = self.trb.copy()
		tbrb = self.brb.copy()
		nblf = [0] * 3
		nblb = [0] * 3
		ntlb = [0] * 3
		ntlf = [0] * 3
		ntlf[0], ntlf[1], ntlf[2] = tblf[2], tblf[1], tblf[0]
		# Top Left Front from Bottom Left Front
		ntlb[0], ntlb[1], ntlb[2] = ttlf[2], ttlf[1], ttlf[0]
		#Top Left Back takes on Top Left Front
		nblb[2], nblb[1], nblb[0] = ttlb[0], ttlb[1], ttlb[2] # Bottom Left Back takes top Left back
		nblf[0], nblf[1], nblf[2] = tblb[0], tblb[1], tblb[2]
		
# Repaired hopefully?
		elcopy = self.moves.copy()
		elcopy.append("L inverse")
		# tlf, trf, blf, brf, tlb, blb, trb, brb, moves):
		return RubiksState(ntlf.copy(), ttrf.copy(), nblf.copy(), tbrf.copy(), ntlb.copy(), nblb.copy(), ttrb.copy(), tbrb.copy(), elcopy)
	def R(self):
		# Indices 0, 1, 2 to 2, 1, 0 (mapping)
		""" Top Right Front to Bottom Right Front.
	Bottom Right Front to Bottom Right Back
	Bottom Right Back to Top Right Back
	Top Right Back to Top Right Front """
		ttlf = self.tlf.copy()
		tblf = self.blf.copy()
		ttrf = self.trf.copy()
		tbrf = self.brf.copy()
		ttlb = self.tlb.copy()
		tblb = self.blb.copy()
		ttrb = self.trb.copy()
		tbrb = self.brb.copy()
		nbrf, nbrb, ntrb, ntrf = [0] * 3, [0] * 3, [0] * 3,[0] * 3
		nbrf[2], nbrf[1], nbrf[0] = ttrf[0], ttrf[1], ttrf[2]
		nbrb[2], nbrb[1], nbrb[0] = tbrf[0], tbrf[1], tbrf[2]
		ntrb[2], ntrb[1], ntrb[0] = tbrb[0], tbrb[1], tbrb[2]
		ntrf[2], ntrf[1], ntrf[0] = ttrb[0], ttrb[1], ttrb[2]
		elcopy = self.moves.copy()
		elcopy.append("R")
		return RubiksState(ttlf.copy(), ntrf.copy(), tblf.copy(), nbrf.copy(), ttlb.copy(), tblb.copy(), ntrb.copy(), nbrb.copy(), elcopy)
	def R2(self):
		""" Bottom Right Back to Top Right Front. Top Right Front to Bottom Right Back. Top Right Back to Bottom Right Front. Bottom Right Front to Top Right Back """
		ttlf = self.tlf.copy()
		tblf = self.blf.copy()
		ttrf = self.trf.copy()
		tbrf = self.brf.copy()
		ttlb = self.tlb.copy()
		tblb = self.blb.copy()
		ttrb = self.trb.copy()
		tbrb = self.brb.copy()
		nbrf, nbrb, ntrb, ntrf = [0] * 3, [0] * 3, [0] * 3,[0] * 3
		ntrf[0], ntrf[1], ntrf[2] = tbrb[0], tbrb[1], tbrb[2]
		nbrb[0], nbrb[1], nbrb[2] = ttrf[0], ttrf[1], ttrf[2]
		nbrf[0], nbrf[1], nbrf[2] = ttrb[0], ttrb[1], ttrb[2]
		ntrb[0], ntrb[1], ntrb[2] = tbrf[0], tbrf[1], tbrf[2]

		elcopy = self.moves.copy()
		elcopy.append("R2")
		return RubiksState(ttlf.copy(), ntrf.copy(), tblf.copy(), nbrf.copy(), ttlb.copy(), tblb.copy(), ntrb.copy(), nbrb.copy(), elcopy)
		pass
	def Rinverse(self):
		""" Top Right Front set as Bottom Right Front. Bottom Right Front set as Bottom Right Back. Bottom Right Back set as Top Right Back. Top Right Back set as Top Right Front """
		ttlf = self.tlf.copy()
		tblf = self.blf.copy()
		ttrf = self.trf.copy()
		tbrf = self.brf.copy()
		ttlb = self.tlb.copy()
		tblb = self.blb.copy()
		ttrb = self.trb.copy()
		tbrb = self.brb.copy()
		nbrf, nbrb, ntrb, ntrf = [0] * 3, [0] * 3, [0] * 3,[0] * 3
		ntrf[0], ntrf[1], ntrf[2] = tbrf[0], tbrf[1], tbrf[2]
		nbrf[0], nbrf[1], nbrf[2] = tbrb[0], tbrb[1], tbrb[2]
		nbrb[0], nbrb[1], nbrb[2] = ttrb[0], ttrb[1], ttrb[2]
		ntrb[0], ntrb[1], ntrb[2] = ttrf[0], ttrf[1], ttrf[2]
		elcopy = self.moves.copy()
		elcopy.append("R inverse")
		return RubiksState(ttlf.copy(), ntrf.copy(), tblf.copy(), nbrf.copy(), ttlb.copy(), tblb.copy(), ntrb.copy(), nbrb.copy(), elcopy)
	def U(self):
		# Indices 0, 1, 2 to 0, 2, 1 (mapping)
		""" Top Left Front to Top Left Back
	Top Left Back to Top Right Back. Top Right Back to Top Right Front. Top Right Front to Top Left Front """
		ttlf = self.tlf.copy()
		tblf = self.blf.copy()
		ttrf = self.trf.copy()
		tbrf = self.brf.copy()
		ttlb = self.tlb.copy()
		tblb = self.blb.copy()
		ttrb = self.trb.copy()
		tbrb = self.brb.copy()
		ntlb = [0] * 3
		ntrb = [0] * 3
		ntrf = [0] * 3
		ntlf = [0] * 3
		ntlb[0], ntlb[2], ntlb[1] = ttlf[0], ttlf[1], ttlf[2]
		ntrb[0], ntrb[2], ntrb[1] = ttlb[0], ttlb[1], ttlb[2]
		ntrf[0], ntrf[2], ntrf[1] = ttrb[0], ttrb[1], ttrb[2]
		ntlf[0], ntlf[2], ntlf[1] = ttrf[0], ttrf[1], ttrf[2]
		
		elcopy = self.moves.copy()
		elcopy.append("U")
		return RubiksState(ntlf.copy(), ntrf.copy(), tblf.copy(), tbrf.copy(), ntlb.copy(), tblb.copy(), ntrb.copy(), tbrb.copy(), elcopy)
	def U2(self):
		""" Top Right Back set as Top Left Front. Top Left Front set as Top Right Back. Top Right Front set as Top Left Back. Top Left Back set as Top Right Front """
		ttlf = self.tlf.copy()
		tblf = self.blf.copy()
		ttrf = self.trf.copy()
		tbrf = self.brf.copy()
		ttlb = self.tlb.copy()
		tblb = self.blb.copy()
		ttrb = self.trb.copy()
		tbrb = self.brb.copy()
		ntlb = [0] * 3
		ntrb = [0] * 3
		ntrf = [0] * 3
		ntlf = [0] * 3
		ntrb[0], ntrb[1], ntrb[2] = ttlf[0], ttlf[1], ttlf[1]
		ntlf[0], ntlf[1], ntlf[2] = ttrb[0], ttrb[1], ttrb[2]
		ntrf[0], ntrf[1], ntrf[2] = ttlb[0], ttlb[1], ttlb[2]
		ntlb[0], ntlb[1], ntlb[2] = ttrf[0], ttrf[1], ttrf[2]
		
		elcopy = self.moves.copy()
		elcopy.append("U2")
		return RubiksState(ntlf.copy(), ntrf.copy(), tblf.copy(), tbrf.copy(), ntlb.copy(), tblb.copy(), ntrb.copy(), tbrb.copy(), elcopy)
		pass
	def Uinverse(self):
		""" Top Right Front set as Top Left Front. Top Left Front set as Top Left Back. Top Left Back set as Top Right Back. Top Right Back set as Top Right Front """
		pass
	def D(self):
		# Indices 0, 1, 2 to 0, 2, 1 (mapping)
		""" Bottom Left Front to Bottom Left Back
		Bottom Left Back to Bottom Right Back. Bottom Right Back to Bottom Right Front
		Bottom Right Front to Bottom Left Front """
		ttlf = self.tlf.copy()
		tblf = self.blf.copy()
		ttrf = self.trf.copy()
		tbrf = self.brf.copy()
		ttlb = self.tlb.copy()
		tblb = self.blb.copy()
		ttrb = self.trb.copy()
		tbrb = self.brb.copy()
		nblb, nbrb, nbrf, nblf= [0] * 3, [0] * 3, [0] * 3, [0] * 3
		nblb[0], nblb[2], nblb[1] = tblf[0], tblf[1], tblf[2]
		nbrb[0], nbrb[2], nbrb[1] = tblb[0], tblb[1], tblb[2]
		nbrf[0], nbrf[2], nbrf[1] = tbrb[0], tbrb[1], tbrb[2]
		nblf[0], nblf[2], nblf[1] = tbrf[0], tbrf[1], tbrf[2]
		elcopy = self.moves.copy()
		elcopy.append("D")
		return RubiksState(ttlf.copy(), ttrf.copy(), nblf.copy(), nbrf.copy(), ttlb.copy(), nblb.copy(), ttrb.copy(), nbrb.copy(), elcopy)
		pass
	def D2(self):
		""" Bottom Left Front set as Bottom Right Back. Bottom Right Back set as Bottom Left Front. Bottom Left Back set as Bottom Right Front. Bottom Right Front set as Bottom Left Back """
		ttlf = self.tlf.copy()
		tblf = self.blf.copy()
		ttrf = self.trf.copy()
		tbrf = self.brf.copy()
		ttlb = self.tlb.copy()
		tblb = self.blb.copy()
		ttrb = self.trb.copy()
		tbrb = self.brb.copy()
		nblb, nbrb, nbrf, nblf= [0] * 3, [0] * 3, [0] * 3, [0] * 3
		nblf[0], nblf[1], nblf[2] = tbrb[0], tbrb[1], tbrb[2]
		nbrb[0], nbrb[1], nbrb[2] = tblf[0], tblf[1], tblf[2]
		nblb[0], nblb[1], nblb[2] = tbrf[0], tbrf[1], tbrf[2]
		nbrf[0], nbrf[1], nbrf[2] = tblb[0], tblb[1], tblb[2]
		elcopy = self.moves.copy()
		elcopy.append("D2")
		return RubiksState(ttlf.copy(), ttrf.copy(), nblf.copy(), nbrf.copy(), ttlb.copy(), nblb.copy(), ttrb.copy(), nbrb.copy(), elcopy)
	def Dinverse(self):
		""" Bottom Right Front set as Bottom Left Front. Bottom Left Front set as Bottom Left Back. Bottom Left Back set as Bottom Right Back. Bottom Right Back set as Bottom Right Front """
		pass
	def F(self):
		# Indices 0, 1, 2 to 1, 0, 2 (mapping)
		""" Bottom Left Front to Top Left Front. Top Left Front to Top Right Front. Top Right Front to Bottom Right Front. Bottom Right Front to Bottom Left Front """
		ttlf = self.tlf.copy()
		tblf = self.blf.copy()
		ttrf = self.trf.copy()
		tbrf = self.brf.copy()
		ttlb = self.tlb.copy()
		tblb = self.blb.copy()
		ttrb = self.trb.copy()
		tbrb = self.brb.copy()
		ntlf, ntrf, nbrf, nblf = [0] * 3, [0] * 3, [0] * 3, [0] * 3
		ntlf[1], ntlf[0], ntlf[2] = tblf[0], tblf[1], tblf[2]
		ntrf[1], ntrf[0], ntrf[2] = ttlf[0], ttlf[1], ttlf[2]
		nbrf[1], nbrf[0], nbrf[2] = ttrf[0], ttrf[1], ttrf[2]
		nblf[1], nblf[0], nblf[2] = tbrf[0], tbrf[1], tbrf[2]
		elcopy = self.moves.copy()
		elcopy.append("F")
		return RubiksState(ntlf.copy(), ntrf.copy(), nblf.copy(), nbrf.copy(), ttlb.copy(), tblb.copy(), ttrb.copy(), tbrb.copy(), elcopy)
	def F2(self):
		""" Top Left Front set as Bottom Right Front. Bottom Right Front set as Top Left Front. Top Right Front set as Bottom Left Front. Bottom Left Front set as Top Right Front """
		ttlf = self.tlf.copy()
		tblf = self.blf.copy()
		ttrf = self.trf.copy()
		tbrf = self.brf.copy()
		ttlb = self.tlb.copy()
		tblb = self.blb.copy()
		ttrb = self.trb.copy()
		tbrb = self.brb.copy()
		ntlf, ntrf, nbrf, nblf = [0] * 3, [0] * 3, [0] * 3, [0] * 3
		ntlf[0], ntlf[1], ntlf[2] = tbrf[0], tbrf[1], tbrf[2]
		nbrf[0], nbrf[1], nbrf[2] = ttlf[0], ttlf[1], ttlf[2]
		ntrf[0], ntrf[1], ntrf[2] = tblf[0], tblf[1], tblf[2]
		nblf[0], nblf[1], nblf[2] = ttrf[0], ttrf[1], ttrf[2]
		
		elcopy = self.moves.copy()
		elcopy.append("F2")
		return RubiksState(ntlf.copy(), ntrf.copy(), nblf.copy(), nbrf.copy(), ttlb.copy(), tblb.copy(), ttrb.copy(), tbrb.copy(), elcopy)
	def Finverse(self):
		""" Bottom Left Front set as Top Left Front. Top Left Front set as Top Right Front. Top Right Front set as Bottom Right Front. Bottom Right Front set as Bottom Left Front """
		pass
	def B(self):
		# Indices 0, 1, 2 to 1, 0, 2 (mapping)
		""" Bottom Left Back to Top Left Back. Top Left Back to Top Right Back. Top Right Back to Bottom Right Back. Bottom Right Back to Bottom Left Back """
		ttlf = self.tlf.copy()
		tblf = self.blf.copy()
		ttrf = self.trf.copy()
		tbrf = self.brf.copy()
		ttlb = self.tlb.copy()
		tblb = self.blb.copy()
		ttrb = self.trb.copy()
		tbrb = self.brb.copy()
		ntlb, ntrb, nbrb, nblb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
		ntlb[1], ntlb[0], ntlb[2] = tblb[0], tblb[1], tblb[2]
		ntrb[1], ntrb[0], ntrb[2] = ttlb[0], ttlb[1], ttlb[2]
		nbrb[1], nbrb[0], nbrb[2] = ttrb[0], ttrb[1], ttrb[2]
		nblb[1], nblb[0], nblb[2] = tbrb[0], tbrb[1], tbrb[2]
		elcopy = self.moves.copy()
		elcopy.append("B")
		return RubiksState(ttlf.copy(), ttrf.copy(), tblf.copy(), tbrf.copy(), ntlb.copy(), nblb.copy(), ntrb.copy(), nbrb.copy(), elcopy)
	def B2(self):
		""" Bottom Right Back set as Top Left Back. Top Left Back set as Bottom Right Back. Bottom Left Back set as Top Right Back. Top Right Back set as Bottom Left Back """
		pass
	def Binverse(self):
		""" Bottom Left Back set as Top Left Back. Top Left Back set as Top Right Back. Top Right Back set as Bottom Right Back. Bottom Right Back set as Bottom Left Back """
		pass
		
	def is_solved(self):
		if self.left_face == ["O", "O", "O", "O"] and self.front_face == ["G", "G", "G", "G"] and self.right_face == ["R", "R", "R", "R"] and self.back_face == ["B", "B", "B", "B"] and self.top_face == ["W", "W", "W", "W"] and self.down_face == ["Y", "Y" , "Y" , "Y"]:
			print("Solved")
			print(self.moves)
			print("Solved: {} {} {} {} {} {}".format(self.left_face, self.front_face, self.right_face, self.back_face, self.top_face, self.down_face))
			return True
			exit(1)
		elif self.right_face == ["O", "O", "O", "O"] and self.front_face == ["G", "G", "G", "G"] and self.left_face == ["R", "R", "R", "R"] and self.back_face == ["B", "B", "B", "B"] and self.top_face == ["W", "W", "W", "W"] and self.down_face == ["Y", "Y" , "Y" , "Y"]:
			print("Solved")
			print(self.moves)
			print("Solved: {} {} {} {} {} {}".format(self.left_face, self.front_face, self.right_face, self.back_face, self.top_face, self.down_face))
			return True
			exit(1)
		elif self.left_face == ["O", "O", "O", "O"] and self.back_face == ["G", "G", "G", "G"] and self.right_face == ["R", "R", "R", "R"] and self.front_face == ["B", "B", "B", "B"] and self.top_face == ["W", "W", "W", "W"] and self.down_face == ["Y", "Y" , "Y" , "Y"]:
			print("Solved")
			print(self.moves)
			print("Solved: {} {} {} {} {} {}".format(self.left_face, self.front_face, self.right_face, self.back_face, self.top_face, self.down_face))
			return True
			exit(1)
		elif self.left_face == ["O", "O", "O", "O"] and self.front_face == ["G", "G", "G", "G"] and self.right_face == ["R", "R", "R", "R"] and self.back_face == ["B", "B", "B", "B"] and self.down_face == ["W", "W", "W", "W"] and self.top_face == ["Y", "Y" , "Y" , "Y"]:
			print("Solved")
			print(self.moves)
			print("Solved: {} {} {} {} {} {}".format(self.left_face, self.front_face, self.right_face, self.back_face, self.top_face, self.down_face))
			return True
			exit(1)
		else:
			print("Not solved: {} {} {} {} {} {}".format(self.left_face, self.front_face, self.right_face, self.back_face, self.top_face, self.down_face))
		return False

def CharlesTruscottRubiks():
#	item = RubiksState([])
# tlf, trf, blf, brf, tlb, blb, trb, brb, moves):
	item = RubiksState(["W", "O", "G"], ["W", "R", "G"], ["Y", "O", "G"], ["Y", "R", "G"], ["W", "O", "B"], ["Y", "O", "B"], ["W", "R", "B"], ["Y", "R", "B"], [])
	state = deque([])
	state.append(item)
	moves = [lambda s: s.L(), lambda s: s.L2(), lambda s: s.Linverse(),  lambda s: s.R(), lambda s: s.R2(), lambda s: s.Rinverse(), lambda s: s.U(), lambda s: s.U2(), lambda s: s.D(), lambda s: s.D2(), lambda s: s.F(),  lambda s: s.F2(), lambda s: s.B() ]
#	moves = [lambda s: s.L(), lambda s: s.L2(), lambda s: s.Linv(), lambda s: s.R(), lambda s: s.R2(), lambda s: s.Rinv(), lambda s: s.U(), lambda s: s.U2(), lambda s: s.Uinv(), lambda s: s.D(), lambda s: s.D2(), lambda s: s.Dinv(), lambda s: s.F(), lambda s: s.F2(), lambda s: s.Finv(), lambda s: s.B(), lambda s: s.B2(), lambda s: s.Binv()]

	for move in moves:
		e = move(item)
		state.append(e)
	state.popleft()
	c = 0
#	print(state)
	print("Charles Truscott Watters. My Rubik's cube solution Python algorithm.")
	from time import sleep
	while c < 18 ** 6:
		elem = state.popleft()
		for move in moves:
			t = move(elem)
			state.append(t)
			print(t, t.moves)
			print("Left Face: {} Front Face: {} Right Face: {} Back Face: {} Top Face: {} Down Face: {}".format(t.left_face, t.front_face, t.right_face, t.back_face, t.top_face, t.down_face))
			print("Authored by Charles Truscott Watters. Rubik's algorithm")
#			sleep(0.2)
			if t.is_solved() == True:
				print("Answer: ")
				print(t.moves)
				exit(1)
		c += 1


CharlesTruscottRubiks()