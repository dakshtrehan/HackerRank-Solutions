# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = 100
    mu = 500
    sigma = 80
    z = 1.96
    
    se = sigma / (n**0.5)
    
    print(mu-(z*se))
    print(mu+(z*se))
