# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# Authors : kutio <kutioo[.at.]gmail[.dot.]com>


from fractions import Fraction
import math

# matrix multiplication
def mat_mult(a, b):
    m = len(a)
    n = len(b[0])
    p = len(a[0])
    res = [ [0 for j in range(n) ] for i in range(m)]
    for i in range(m):
        for j in range(n):
            coeff = 0
            for k in range(p):
                coeff += a[i][k] * b[k][j]
            res[i][j] = coeff
    return res

# scalar product
def scalar_product(a, b):
    m = len(a)
    res = Fraction(0)
    for i in range(m):
        res += a[i] * b[i]
    return res

# display matrix
def print_mat(n):
    maxlen = 0
    for row in n:
        for f in row:
            if len(str(f)) > maxlen:
                maxlen = len(str(f))
    for row in n:
        row_str = ""
        for f in row:
            difflen = maxlen - len(str(f))
            sep = " "
            for i in range(difflen):
                sep = sep + " "
            row_str = row_str + sep + str(f)
        print(row_str)

# display vector
def print_vector(v):
    row_str = " ".join("%s" % i for i in v)
    print(row_str)

# get vector j in the matrix n
def get_vector(n, j):
    res = []
    for i in range(len(n)):
        res.append(n[i][j])
    return res

# vector substraction 
def vector_add(a, b):
    res = []
    for i in range(len(a)):
        res.append(a[i] + b[i])
    return res

# vector substraction 
def vector_sub(a, b):
    res = []
    for i in range(len(a)):
        res.append(a[i] - b[i])
    return res

# vector multiplication with a constant
def vector_mult_const(v, k):
    res = []
    for i in range(len(v)):
        res.append(v[i]*k)
    return res

# set vector j in the matrix n with vector v
def set_matrix_vector(n, k, v):
    row = len(n)
    col = len(n[0])
 
    # edit the good column
    for i in range(row):
        n[i][k] = v[i]
        
# norml2 : square of the L2-norm of the vector x
def norml2(a):
    return scalar_product(a, a)

def create_matrix_from_knapsack(knap, the_sum):
    n = len(knap)
    result = [ [Fraction(0) for j in range(n+1) ] for i in range(n+1)]

    # identity matrix
    for i in range(n):
        for j in range(n):
            if i == j:
                result[i][j] = Fraction(1)

    i = i + 1
    for k in range(n):
        result[i][k] = Fraction(knap[k])

    result[i][k+1] = -Fraction(the_sum)
    return result

def round(num):
    if (num > 0):
        return int(num+Fraction(1,2))
    else:
        return int(num-Fraction(1,2))

def create_matrix(n):
    row = len(n)
    col = len(n[0])
    res = [ [Fraction(n[i][j]) for j in range(col) ] for i in range(row)]
    return res

# [ 0, 2, -1, ... , 0, 1 ] + [1, -2, 2, ..., 0, -1] = [ 1, 0, 1, ..., 0, 0]    
def heuristic_u_plus_v(n):
    row = len(n)
    col = len(n[0])
    #negative vectors
    minus_1_tab = []
    #positive vectors
    plus_1_tab = []

    # this vector finishes with -1
    minus_1_vect = [ 0 for i in range(row) ]
    # this vector finishes with 1
    plus_1_vect = [ 0 for i in range(row) ]

    for i in range(row):
        if n[row-1][i] == 1:
            for j in range(row):
                plus_1_vect[j] = int(n[j][i])

            if plus_1_vect not in plus_1_tab:
                plus_1_tab.append(plus_1_vect)

        elif n[row-1][i] == -1:
            for j in range(row):
                minus_1_vect[j] = int(n[j][i])

            if minus_1_vect not in minus_1_tab:
                minus_1_tab.append(minus_1_vect)
    return vector_add(minus_1_vect, plus_1_vect)[:-1]

# retrieve the best vector for knapsack
def best_vect_knapsack(n):
    row = len(n)
    col = len(n[0])

    best_vect = [ 0 for i in range(row) ]
    solution = [ 0 for i in range(row-1) ]

    for i in range(row):
        if n[row-1][i] == 0:
            take_it = 1

            for j in range(col):
                if n[j][i] != Fraction(1):
                    if n[j][i] != Fraction(0):
                        take_it = 0

            if take_it:
                for j in range(row):
                    if n[j][i] == 1:
                        best_vect[j] = 1
                    elif n[j][i] == 0:
                        best_vect[j] = 0
                break;

    apply_heuristic = True
    for i in range(row):
        if best_vect[i] != 0:
            apply_heuristic = False

    if apply_heuristic:
        print("No direct solution found, apply heuristic")
        solution = heuristic_u_plus_v(n)
        for i in range(len(solution)):
            if solution[i] != 1:
                if solution[i] != 0:
                    # apply complement
                    print("no solution found with heuristics")
                    return [0]*row
    else:
        for i in range(row-1):
            solution[i] = best_vect[i]
    return solution

# gram schmidt algorithm
def gram_schmidt(g, m, mu, B):
    row = len(m)

    for i in range(row):
        # bi* = bi
        b_i = get_vector(g, i)
        b_i_star = b_i
        set_matrix_vector(m, i, b_i_star)

        for j in range(i):
            # u[i][j] = (bi, bj*)/Bj
            b_j_star = get_vector(m, j)
            b_i = get_vector(g, i)
            B[j] = norml2(b_j_star)
            mu[i][j] = Fraction(scalar_product(b_i, b_j_star), B[j])
            # bi* = bi* - u[i][j]* bj*
            b_i_star = vector_sub(b_i_star, vector_mult_const(b_j_star, mu[i][j]))
            set_matrix_vector(m, i, b_i_star)

        b_i_star = get_vector(m, i)
        # B[i] = (bi*, bi*)
        B[i] = scalar_product(b_i_star, b_i_star)
 

# reduce
def reduce(g, mu, k, l):
    row = len(g)
    col = len(g[0])

    if math.fabs(mu[k][l]) > Fraction(1, 2):
        r = round(mu[k][l])
        b_k = get_vector(g, k)
        b_l = get_vector(g, l)
        # bk = bk - r*bl
        set_matrix_vector(g, k, vector_sub(b_k, vector_mult_const(b_l, r)))

        for j in range(l):
            # u[k][j] = u[k][j] - r*u[l][j]
            mu[k][j] = mu[k][j] - r*mu[l][j]

        # u[k][l] = u[k][l] - r
        mu[k][l] = mu[k][l] - r


# lll_reduction from LLL book
def lll_reduction(n, lc=Fraction(3, 4)):
    row = len(n)
    col = len(n[0])

    m = [ [Fraction(0) for j in range(col) ] for i in range(row)]
    mu = [ [Fraction(0) for j in range(col) ] for i in range(row)]
    g = [ [n[i][j] for j in range(col) ] for i in range(row)]
    B = [ Fraction(0) for j in range(row) ]

    gram_schmidt(g, m, mu, B)

    # k = 2
    k = 1

    while 1:

        # 1 - perform (*) for l = k - 1
        reduce(g, mu, k, k-1)

        # lovasz condition
        if B[k] < (lc - mu[k][k-1]*mu[k][k-1])*B[k-1]:
            # 2
            # u = u[k][k-1]
            u = mu[k][k-1]

            # B = Bk + u^2*Bk-1
            big_B = B[k] + (u*u) * B[k-1]

            # mu[k][k-1] = u * B[k-1] / B
            mu[k][k-1] = u*Fraction(B[k-1], big_B)

            # Bk = Bk-1 * Bk / B
            B[k] = Fraction(B[k-1] * B[k], big_B)

            # Bk-1 = B
            B[k-1] = big_B

            # exchange bk and bk-1
            b_k = get_vector(g, k)
            b_k_minus_1 = get_vector(g, k-1)
            set_matrix_vector(g, k, b_k_minus_1)
            set_matrix_vector(g, k-1, b_k)
            
            # for j = 0 .. k-2
            for j in range(k-1):
                save = mu[k-1][j]
                mu[k-1][j] = mu[k][j]
                mu[k][j] = save

            for i in range(k+1, row):
                save = mu[i][k-1]
                mu[i][k-1] = mu[k][k-1]*mu[i][k-1] + mu[i][k] - u*mu[i][k]*mu[k][k-1]
                mu[i][k] = save - u*mu[i][k]

            # if k > 2
            if k > 1:
                k = k - 1

        else:
            for l in range(k-2, -1, -1):
                reduce(g, mu, k, l)

            if k == row-1:
                return g

            k = k + 1

# definition from the LLL book
def islll(n, lc=Fraction(3, 4)):
    row = len(n)
    col = len(n[0])

    m = [ [Fraction(0) for j in range(col) ] for i in range(row)]
    mu = [ [Fraction(0) for j in range(col) ] for i in range(row)]
    B = [ Fraction(0) for j in range(row) ]

    gram_schmidt(n, m, mu, B)

    for i in range(row):
        for j in range(i):
            if math.fabs(mu[i][j]) > Fraction(1, 2):
                return False

    for k in range(1, row):
        if B[k] < (lc - mu[k][k-1]*mu[k][k-1])*B[k-1]:
            return False
    return True

