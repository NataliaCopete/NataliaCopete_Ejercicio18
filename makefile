primera:primerord.pdf
	
primerord.pdf:valores.txt
	python ej18.py

valores.txt:
	c++ NataliaCopete_ej18.cpp
	./a.out>valores.txt

segunda:segundord.pdf Zvsy.pdf


segundord.pdf:valores2.txt
	python ej182.py

valores2.txt:
	c++ NataliaCopete_ej182.cpp
	./a.out>valores2.txt

