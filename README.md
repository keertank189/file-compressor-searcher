Advance Algorithms Project

Team No: 101101

Team:
Aakansha Pant 		01FB16ECS018
Abhishek Saseendran	01FB16ECS005
Kaushik Ravi		01FB16ECS160
Keerthan Krishan 	01FB16ECS163

Project Outcome:
File Compression
Searching in a Compressed Space

Files Required:
	fm-build.py
	fmindex.py
	fm-search.py
	bwt.py
	test_data.txt

Execution:
python fm-build <input dataset> <indexfile> 
python fm-search.py <indexfile> "<querystring>"

Output:
	load:<time for loading the compressed file>
	count:<time taken to count the number of occurences>
	<no of occurences>
	matches:<time taken to find the exasct matched>
	[list of indicies]

