import lab as lb 

def main():
    lab = lb.txtToArray(open("lab.txt").read())
    print(lb.camino(lab[:-2], lab[len(lab)-2], lab[len(lab)-1]))

if __name__ == "__main__":
    main()