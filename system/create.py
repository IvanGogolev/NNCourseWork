import os
import filecmp
import shutil

def init():
    os.system("mkdir tests 2> nul")
    os.system("mkdir heap 2> nul")
    os.system("del tests /s /q 2> nul > nul")
    os.system("del heap /s /q 2> nul > nul")
    os.system("mkdir hand_test 2> nul")
    os.system("mkdir auto_test 2> nul")
    os.system("mkdir hand_generators 2> nul")
    os.system("mkdir auto_generators 2> nul")
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
        os.system("mkdir .\\hand_generators\\tests 2> nul")
        
        for j in range(t):
            open("./hand_generators/tests/" + name + ".exe", "w")
            shutil.copyfile("./" + name + ".exe", "./hand_generators/tests/" + name + ".exe" )
            s = input()
            os.system(".\\hand_generators\\tests\\" + name + ".exe" + " > ./hand_generators/tests/1 $ " + s)
            os.system("del .\\hand_generators\\tests\\" + name + ".exe")
            for y in os.listdir("./hand_generators/tests"):
                shutil.copyfile("./hand_generators/tests/" + y, "./heap/hand_generators_" + name + "_" + str(j) + "_" + y + ".in")
        os.system("rmdir .\\hand_generators\\tests /s /q 2> nul")
        os.system("del .\\" + name + ".exe")
    print("auto generators")
    arr = os.listdir("./auto_generators")
    for x in arr:
        if x[-3:len(x)] != "cpp":
            continue
        name = x[:len(x) - 4]
        if os.system(f"g++ -o {name}.exe ./auto_generators/{name}.cpp") != 0:
            continue
        print(name)
        os.system("mkdir .\\auto_generators\\tests 2> nul")
        open("./auto_generators/tests/" + name + ".exe", "w")
        shutil.copyfile("./" + name + ".exe", "./auto_generators/tests/" + name + ".exe" )
        os.system(".\\auto_generators\\tests\\" + name + ".exe" + " > ./auto_generators/tests/1.txt")
        os.system("del .\\auto_generators\\tests\\" + name + ".exe")
        for y in os.listdir("./auto_generators/tests"):
            shutil.copyfile("./auto_generators/tests/" + y, "./heap/auto_generators_" + name + "_" + y + ".in")
        os.system("del .\\" + name + ".exe")        
        os.system("rmdir .\\auto_generators\\tests 2> nul /s /q")
            

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
    for x in os.listdir("./heap"):
        register_test("./heap/" + x)
    os.system("rmdir heap /s /q")
    os.system("del .\\validator.exe")
    os.system("del .\\hand_generators\\testlib.h")
    os.system("del .\\auto_generators\\testlib.h")
init()
make_heap()
make_tests()
