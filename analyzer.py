def analyze_processes(processes):
	findings=[]
	suspicious = {
		"powershell.exe": 30,
		"cmd.exe": 20,
		"wscript.exe": 40,
		"cscript.exe": 40
	}
	suspicion_score = 0

	for process in processes:
		if process in suspicious:
			findings.append({
				"process": process,
				"score": suspicious[process]
			})

			suspicion_score += suspicious[process]
	return findings, suspicion_score
