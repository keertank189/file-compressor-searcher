# Advanced Algorithms Project

## Note : 
 - This is a repository containing a tool for the compression of text files, with a capability to subsequently search in the compressed space, without the need to de-compress the files. The project is built using the principles of the Burrows-Wheeler-Tranform, fm-indexing and the LZ-77 compression algorithm.
 - Python 3.5 has been used for the development of this project, and will run with python 3.x

Team No: 101101

Team:
Aakansha Pant 		01FB16ECS018
Abhishek Saseendran	01FB16ECS005
Kaushik Ravi		01FB16ECS160
Keertan Krishan 	01FB16ECS163

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
	load: time for loading the compressed file
	count: time taken to count the number of occurences 
	 no of occurences 
	matches: time taken to find the exact matched 
	[list of indicies]

