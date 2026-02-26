import os
import filecmp
import shutil

def init():
    os.system("mkdir tests")
    os.system("mkdir hand_test")
    os.system("mkdir auto_test")
    os.system("mkdir hand_generators")
    os.system("mkdir auto_generators")
    shutil.copyfile("testlib.h", "./hand_generators/testlib.h")
    shutil.copyfile("testlib.h", "./auto_generators/testlib.h")
def make_heap():
    for x in os.listdir("./hand_test"):
        shutil.copyfile("./hand_test/" + x, "./heap/hand_test_" + x)
    for x in os.listdir("./auto_test"):
        shutil.copyfile("./auto_test/" + x, "./heap/auto_test_" + x)
    print("hand generators")
    arr = os.listdir("./hand_generators")
    for x in arr:
        if x[-3:len(x)] != "cpp":
            continue
        name = x[:len(x) - 4]
        if os.system(f"g++ -o {name}.exe ./hand_generators/{name}.cpp") != 0:
            continue
        print(name)
        t = int(input())
        for j in range(t):
            s = input()
            os.system(f".\\hand_generators\\{name}.exe {s} > .\\heap\\hand_generators_{name}_{str(j)}.in")
    print("auto generators")
    arr = os.listdir("./auto_generators")
    for x in arr:
        if x[-3:len(x)] != "cpp":
            continue
        name = x[:len(x) - 4]
        if os.system(f"g++ -o {name}.exe ./auto_generators/{name}.cpp") != 0:
            continue
        print(name)
        os.system("mkdir .\\auto_generators\\tests")
        shutil.copyfile("./auto_generators/" + name + ".exe", "./auto_generators/tests/" + name + ".exe" )
        os.chdir("./auto_generators/tests")
        os.system(name + ".exe")
        os.chdir("../")
        os.chdir("../")
        #os.system(".\\auto_generators\\tests\\" + name + ".exe" + " > ./auto_generators/tests")
        os.system("del .\\auto_generators\\tests\\" + name + ".exe")
        for y in os.listdir("./auto_generators/tests"):
            shutil.copyfile("./auto_generators/tests/" + y, "./heap/auto_generators_" + name + "_" + y + ".in")
                  
        
            

TEST = 1
def register_test(x):
    global TEST
    if os.system("validator.exe <" + x) != 0:
        return 0
    for y in os.listdir("./tests"):
        if filecmp.cmp(x, "./tests/" + y, shallow = False):
            return 0
    
    shutil.copyfile(x, "./tests/" + str(TEST) + ".in")
    TEST += 1
    return 1

def make_tests():
    os.system("g++ -o validator.exe validator.cpp")
    os.system("mkdir tests")
    for x in os.listdir("./heap"):
        register_test("./heap/" + x)
init()
make_heap()
make_tests()




