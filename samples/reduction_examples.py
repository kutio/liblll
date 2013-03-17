from liblll import * 
mat1 = [ [1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [5615, 3944, 8021, 2117, -7732]]
print "Example 1 : "
mat1 = create_matrix(mat1)
print "mat1 : "
print_mat(mat1)
print "mat1 is lll ? ", islll(mat1)
print "reduce mat : "
mat1pass = lll_reduction(mat1)
print_mat(mat1pass)
print "mat1 is lll ? ", islll(mat1pass)
print "\n"

mat2 = [[10, 11], [11, 12]]
print "Example 2 : "
mat2 = create_matrix(mat2)
print "mat2 : "
print_mat(mat2)
print "mat2 is lll ? ", islll(mat2)
print "reduce mat : "
mat2pass = lll_reduction(mat2)
print_mat(mat2pass)
print "mat2 is lll ? ", islll(mat2pass)
print "\n"

mat3 = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [15, 22, 13, -35]]
print "Example 3 : "
mat3 = create_matrix(mat3)
print "mat3 : "
print_mat(mat3)
print "mat3 is lll ? ", islll(mat3)
print "reduce mat : "
mat3pass = lll_reduction(mat3)
print_mat(mat3pass)
print "mat3 is lll ? ", islll(mat3pass)
print "\n"

mat4 = [[1, 0, 0], [0, 1, 0], [15, 22, -22]]
print "Example 4 : "
mat4 = create_matrix(mat4)
print "mat4 : "
print_mat(mat4)
print "mat4 is lll ? ", islll(mat4)
print "reduce mat : "
mat4pass = lll_reduction(mat4)
print_mat(mat4pass)
print "mat4 is lll ? ", islll(mat4pass)
print "\n"

mat5 = [[1, -1, 3], [1, 0, 5], [1, 2, 6]]
print "Example 5 : "
mat5 = create_matrix(mat5)
print "mat5 : "
print_mat(mat5)
print "mat5 is lll ? ", islll(mat5)
print "reduce mat : "
mat5pass = lll_reduction(mat5)
print_mat(mat5pass)
print "mat5 is lll ? ", islll(mat5pass)
print "\n"

mat6 = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [22, 87, 45, -67]]
print "Example 6 : "
mat6 = create_matrix(mat6)
print "mat6 : "
print_mat(mat6)
print "mat6 is lll ? ", islll(mat6)
print "reduce mat : "
mat6pass = lll_reduction(mat6)
print_mat(mat6pass)
print "mat6 is lll ? ", islll(mat6pass)
print "\n"

mat7 = [[1, -1], [-1, 2]]
print "Example 7 : "
mat7 = create_matrix(mat7)
print "mat7 : "
print_mat(mat7)
print "mat7 is lll ? ", islll(mat7)
print "reduce mat : "
mat7pass = lll_reduction(mat7)
print_mat(mat7pass)
print "mat7 is lll ? ", islll(mat7pass)
print "\n"


mat8 = [[2, 3], [0, 1]]
print "Example 8 : "
mat8 = create_matrix(mat8)
print "mat8 : "
print_mat(mat8)
print "mat8 is lll ? ", islll(mat8)
print "reduce mat : "
mat8pass = lll_reduction(mat8)
print_mat(mat8pass)
print "mat8 is lll ? ", islll(mat8pass)
print "\n"

mat9 = [[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [17, 8, 10, 14, 3, -30]]
print "Example 9 : "
mat9 = create_matrix(mat9)
print "mat9 : "
print_mat(mat9)
print "mat9 is lll ? ", islll(mat9)
print "reduce mat : "
mat9pass = lll_reduction(mat9)
print_mat(mat9pass)
print "mat9 is lll ? ", islll(mat9pass)
print "\n"


mat10 = [[263, -224, -3021], [289, -246, -3319], [850, -724, -9764]]
print "Example 10 : "
mat10 = create_matrix(mat10)
print "mat10 : "
print_mat(mat10)
print "mat10 is lll ? ", islll(mat10)
print "reduce mat : "
mat10pass = lll_reduction(mat10)
print_mat(mat10pass)
print "mat10 is lll ? ", islll(mat10pass)
print "\n"

