import os
def code_coverage_criteria(sol_path, test_path):
	os.system(f"g++ --coverage -o a ./{sol_path}")
	for x in os.listdir(test_path):
		if x[-4:] == ".txt" or x[-3:] == ".in":
			file_path = test_path + "/" + x
			os.system("a.exe < " + file_path + " > nul")
	os.system(f"gcov ./{sol_path} > res.txt")
	
	report = open("res.txt").read()
	cov = open(sol_path + ".gcov").read()

	os.system("del " + sol_path + ".gcov")
	os.system("del " + sol_path[:-4] + ".gcda")
	os.system("del " + sol_path[:-4] + ".gcno")
	os.system("del a.exe")
	os.system("del res.txt")
	return report, cov
sol_path = "b.cpp"
test_path = "tests"
a, b = code_coverage_criteria(sol_path, test_path)
print(a)
print(b)