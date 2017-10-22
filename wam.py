class MatrixCicle:

    def __init__(self):
        self.index = 1
        self.dimension = 8
        self.matrix = [[0 for x in range(self.dimension)] for y in range(self.dimension)]
        self.matrixCicle(self.matrix, self.dimension)
        print("final: ")
        self.HoraDoShow()

    def matrixCicle(self, matrix, d):        
        print("new cicle ----------")
        print (d)
        #sup
        sup_i = 0
        sup_ji = 0
        sup_je = len(matrix) - 1
        #dir
        dir_ii = 0
        dir_ie = len(matrix) - 1
        dir_j = len(matrix) - 1
        #inf
        inf_i = len(matrix) - 1
        inf_ji = len(matrix) - 1
        inf_je = 0
        #esq
        esq_ii = len(matrix) - 1 
        esq_ie = 0
        esq_j = 0
        while True:
            if d <= 1:
                return
            self.sup(sup_i, sup_ji, sup_je)
            self.latDir(dir_ii, dir_ie, dir_j)
            self.inf(inf_i, inf_ji, inf_je)
            self.latEsq(esq_ii, esq_ie, esq_j)
            d -= 2
            #sup
            sup_i += 1
            sup_ji += 1
            sup_je -= 1
            #dir
            dir_ii += 1
            dir_ie -= 1
            dir_j -= 1
            #inf
            inf_i -= 1
            inf_ji -= 1
            inf_je += 1
            #esq
            esq_ii -= 1
            esq_ie += 1
            esq_j += 1

            self.matrix[sup_i][sup_je] = 0
            
    def sup(self,i, ji, je):
        print("----enter in sup----")
        self.HoraDoShow()
        iteratorJ = ji
        while iteratorJ <= je:
            if self.matrix[i][iteratorJ] == 0:
                self.matrix[i][iteratorJ] = self.index
                self.index += 1
            iteratorJ += 1 
        self.HoraDoShow()
        print("----out of sup----")

    def latDir(self, ii, ie, j):
        print("----enter in latDir----")
        self.HoraDoShow()
        iteratorI = ii
        while iteratorI <= ie:
            if self.matrix[iteratorI][j] == 0:
                self.matrix[iteratorI][j] = self.index
                self.index += 1
            iteratorI += 1
        self.HoraDoShow()
        print("----out of latDir----")

    def inf(self, i, ji, je):
        print("----enter in inf----")
        self.HoraDoShow()       
        iteratorJ = ji
        while iteratorJ >= je:
            if self.matrix[i][iteratorJ] == 0:
                self.matrix[i][iteratorJ] = self.index
                self.index += 1
            iteratorJ -= 1 
        self.HoraDoShow()
        print("----out of inf----")

    def latEsq(self, ii, ie, j):
        print("----enter in latEsq----")
        self.HoraDoShow()                
        iteratorI = ii
        while iteratorI >= ie:
            if self.matrix[iteratorI][j] == 0:
                self.matrix[iteratorI][j] = self.index
                self.index += 1
            iteratorI -= 1
        self.HoraDoShow()
        print("----out of latEsq----")
    
    def HoraDoShow(self):
        for line in self.matrix:
            print(line)
        print("\n")
    
    def printM(self, matrix):
        for line in matrix:
            print(line)
        print("\n")