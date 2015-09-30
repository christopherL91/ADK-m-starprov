```
	Input: matrix of size 2n * 2n

	pair: s -> (s0,s1), (s1,s2), (s2, s3), ...

	procedure solve(matrix)
	begin
		num <- 0
		for row <- matrix loop
			for (v,w) <- pair(matrix(row-1),matrix(row)) loop
				total <- mean([v,w])
				num <- num + filter(λ: x > total, [v,w])
			end loop
		end loop
		return num
	end
```

>	Korrekthetsbevis:
>	
>	Det är trivialt att ifall vi delar in matrisen i (n-1)^2 "delrutor" (räkna antal "hårkors" i en matris) 
