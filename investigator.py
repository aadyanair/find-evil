def make_decision(score):
	
	if score >= 40:
	    return "windows.cmdline"
	
	if score >= 20:
	    return "windows.netscan"
	    
	return None
