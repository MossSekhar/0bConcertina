class 0bConcertina {
    def __init__(self):
		''' Class Constructor '''
	
    def bitadd(bits, position):
    	''' Sets a bit at a position 0-indexed from the right. Based on
    	Make School's Bit Manipulation video '''
    	mask = 1 << position
    	return bin(x | mask)
    	
    def bitclear(bits, position):
    	''' Clears a bit from a position 0-indexed from the right. Based 			on Make School's Bit Manipulation video '''
    	mask = 1 << position
    	return bin(x & ~mask)
    	
    def bitflip(bits, position):
    	''' Flips a bit from a position 0-indexed from the right. Based on
    	Make School's Bit Manipulation video '''
    	mask = 1 << position
    	return bin(x ^ mask)
    	
    def bitcheck(bits, position):
    	''' Checks if a bit is set at a position 0-indexed from the 		right and outputs a boolean. Based on Make School's Bit
    	Manipulation video '''
    	shifted = bits >> position
		if (shifted & 1) == 1:
			return True
    	else:
    		return False
    		
    def bitmod(bits, position, setorclear):
    	''' Modifies a bit from a position 0-indexed from the right. Set 
    	setorclear to 1 if you want to set a bit, or 0 if you want to 
    	clear one.
    	Based on Make School's Bit Manipulation video '''
    	mask = 1 << position
    	return bin( (bits & ~mask) | (-setorclear & mask) )
    	
}
