def primo(numero):
    l = int(numero ** 0.5) + 1 
    for n in range(2, l):     
        if numero % n == 0:
            return False 
            print "Il numero non si scompone" 
            else:     
            return True
def scomposizione(n):
	fattore = str(n) + " = 1"                   
	d = 2                                      
	while n >= d:                               
		if n % d == 0:                      
			fattore += ' * ' + str(d)
			n /= d                     
		else:
			d = d + 1                   
	return fattore

 
                  