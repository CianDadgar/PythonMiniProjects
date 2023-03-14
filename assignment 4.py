def main():
    infile = open('numbers.txt','r')
    
    num1 = int(infile.readline())
    num2 = int(infile.readline())
    num3 = int(infile.readline())
    num4 = int(infile.readline())
    num5 = int(infile.readline())
    infile.close()
    total = num1 + num2 + num3 + num4 + num5

    outfile = open('output.txt', 'w')
    num6 = num1 * 2
    num7 = num2 * 2
    num8 = num3 * 2
    num9 = num4 * 2
    num10 = num5 * 2
    outfile.write('num6\n')
    outfile.write('num7\n')
    outfile.write('num8\n')
    outfile.write('num9\n')
    outfile.write('num10\n')
    print(num6)
    print(num7)
    print(num8)
    print(num9)
    print(num10)
    
    print('original sum:',total)
    
    outfile.close()

main()
    
    
