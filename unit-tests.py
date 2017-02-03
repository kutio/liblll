import unittest
from liblll import *

class ScalarProductTestCase(unittest.TestCase):
    def setUp(self):
        self.a = [-3, 5, 2]
        self.b = [1, -7, 3]
        self.result = -32

    def test_scalar_product(self):
        result = scalar_product(self.a, self.b)
        self.assertEqual(self.result, result) 

class Norml2TestCase(unittest.TestCase):
    def setUp(self):
        self.norml2_vector = [ 5, -1]
        self.norml2_result = 26 

    def test_norml2(self):
        res = norml2(self.norml2_vector)
        self.assertEqual(self.norml2_result, res) 

class MatrixTestCase(unittest.TestCase):
    def setUp(self):
        self.a = [[5, 3, 2],[1, 5, 6]]
        self.b = [[2, 4], [1, 7], [3, 2]]
        self.result = [[19, 45], [25, 51]]
        self.matrix_vector0 = [[1, 3, 2],[3, 5, 6]]
        self.matrix_vector1 = [[5, 1, 2],[1, 3, 6]]
        self.matrix_vector2 = [[5, 3, 1],[1, 5, 3]]

    def test_mat_mult(self):
        result = mat_mult(self.a, self.b)
        self.assertEqual(self.result, result) 

    def test_set_matrix_vector_0(self):
        a = [ e for e in self.a ]
        set_matrix_vector(a, 0, [1, 3])
        self.assertEqual(self.matrix_vector0, a) 

    def test_set_matrix_vector_1(self):
        a = [ e for e in self.a ]
        set_matrix_vector(a, 1, [1, 3])
        self.assertEqual(self.matrix_vector1, a) 

    def test_set_matrix_vector_1(self):
        a = [ e for e in self.a ]
        set_matrix_vector(a, 2, [1, 3])
        self.assertEqual(self.matrix_vector2, a) 

class VectorTestCase(unittest.TestCase):
    def setUp(self):
        self.n = [[5, 3, 2],[1, 5, 6]]
        self.vector0 = [5, 1]
        self.vector1 = [3, 5]
        self.vector2 = [2, 6]
        self.vector_add = [8, 6]
        self.vector_sub = [2, -4]
        self.vector_mult_const = [15, 3]
        self.norml2_vector = [ 5, -1]
        self.norml2_result = 26 

    def test_get_vector_0(self):
        vector0 = get_vector(self.n, 0)
        self.assertEqual(self.vector0, vector0) 

    def test_get_vector_1(self):
        vector1 = get_vector(self.n, 1)
        self.assertEqual(self.vector1, vector1) 

    def test_get_vector_2(self):
        vector2 = get_vector(self.n, 2)
        self.assertEqual(self.vector2, vector2) 

    def test_vector_add(self):
        res = vector_add(self.vector0, self.vector1)
        self.assertEqual(self.vector_add, res) 

    def test_vector_sub(self):
        res = vector_sub(self.vector0, self.vector1)
        self.assertEqual(self.vector_sub, res) 

    def test_vector_mult_const(self):
        res = vector_mult_const(self.vector0, 3)
        self.assertEqual(self.vector_mult_const, res) 

class KnapsackTestCase(unittest.TestCase):
    def setUp(self):
        self.knapsack = [17, 8, 10, 14, 3]
        self.the_sum = 30
        self.knapsack_result = [[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [17, 8, 10, 14, 3, -30]]
        self.knap_best_vector_n = [[1, -1, -5, 3, -3], [0, -1, 0, -12, 4], [0, -1, 7, 1, -11], [1, 1, 5, -4, 2], [0, 1, -3, -2, -14]]
        self.knap_best_vector = [1, 0, 0, 1]

    def test_create_matrix_from_knapsack(self):
        res = create_matrix_from_knapsack(self.knapsack, self.the_sum)
        self.assertEqual(self.knapsack_result, res) 

    def test_best_vector(self):
        m = create_matrix(self.knap_best_vector_n)
        res = best_vect_knapsack(m)
        self.assertEqual(self.knap_best_vector, res) 
        

class UtilTestCase(unittest.TestCase):
    def setUp(self):
        self.round_pos = Fraction(7, 2)
        self.round_pos_res = 4

        self.round_neg = -Fraction(3, 2)
        self.round_neg_res = -2

    def test_round_pos(self):
        res = round(self.round_pos)
        self.assertEqual(self.round_pos_res, res)

    def test_round_neg(self):
        res = round(self.round_neg)
        self.assertEqual(self.round_neg_res, res)

class LLLTestCase(unittest.TestCase):
    def setUp(self):
        self.mat_gram_schmidt = [[1, 1], [0, 1]]
        self.mat_gram_schmidt_res = [[1, 0], [0, 1]]
        self.wikipedia_example = [[1, -1, 3], [1, 0, 5], [1, 2, 6]]
        self.wikipedia_example_reduced = [[0, 1, -1], [1, 0, 0], [0, 1, 2]]
        self.mat_reduction_1 = [[10, 11], [11, 12]]
        self.mat_reduction_1_reduced = [[-1, 0], [0, 1]]
        self.mat_reduction_2 = [[2, 3], [0, 1]]
        self.mat_reduction_2_reduced = [[-1, 1], [1, 1]]
        self.mat_reduction_3 = [[1, -1], [-1, 2]]
        self.mat_reduction_3_reduced = [[1, 0], [0, -1]]
        self.pubkey = [964266105338945, 6749864515101946, 964264861986975, 13499727318176232, 17356789956975810,3857053002628327, 12535438500695219, 10606879723866753, 10606828405887831, 16392324024362666, 13499318722439347, 7713307812454905, 6748217527825207, 6746569486347068, 8671806553725916, 2879615947706164, 18294696345811439, 6697131932913639, 15322796985338016, 753333165640954, 16934930158297044, 10727464396496856, 8919464717468072, 12053330796850461]
        self.first_sum = 85665597416613316
        self.second_sum = 68924182376697138
        self.best_vect_first_sum = [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0]
        self.best_vect_second_sum = [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1]
        self.not_full_rank = [ [ 0, 17, 1], [10, 100, 80], [-9, 11, 76], [110, 50, 60]]
        self.not_full_rank_reduced = [ [ -16, 0, 17], [-20, 10, 90], [65, -9, 20], [10, 110, -60]]

    def test_gram_schmidt(self):
        mu = [[Fraction(0), Fraction(0)], [Fraction(0), Fraction(0)]]
        m = [[Fraction(0), Fraction(0)], [Fraction(0), Fraction(0)]]
        B = [Fraction(0), Fraction(0)]

        gram_schmidt(self.mat_gram_schmidt, m, mu, B)
        self.assertEqual(self.mat_gram_schmidt_res, m)

    def test_lll_reduction_wikipedia(self):
        mat = create_matrix(self.wikipedia_example)
        mat_reduced = lll_reduction(mat)
        self.assertEqual(self.wikipedia_example_reduced, mat_reduced)

    def test_is_non_lll_wikipedia(self):
        mat = create_matrix(self.wikipedia_example)
        self.assertEqual(0, islll(mat))

    def test_is_lll_wikipedia(self):
        mat = create_matrix(self.wikipedia_example)
        mat_reduced = lll_reduction(mat)
        self.assertEqual(1, islll(mat_reduced))

    def test_lll_reduction_1(self):
        mat = create_matrix(self.mat_reduction_1)
        mat_reduced = lll_reduction(mat)
        self.assertEqual(self.mat_reduction_1_reduced, mat_reduced) 

    def test_lll_reduction_2(self):
        mat = create_matrix(self.mat_reduction_2)
        mat_reduced = lll_reduction(mat)
        self.assertEqual(self.mat_reduction_2_reduced, mat_reduced) 

    def test_lll_reduction_3(self):
        mat = create_matrix(self.mat_reduction_3)
        mat_reduced = lll_reduction(mat)
        self.assertEqual(self.mat_reduction_3_reduced, mat_reduced) 

    def test_lll_reduction_knapsack1(self):
        first_mat = create_matrix_from_knapsack(self.pubkey, self.first_sum)
        self.assertEqual(0, islll(first_mat)) 
        first_mat_reduced = lll_reduction(first_mat)
        self.assertEqual(1, islll(first_mat_reduced)) 
        res = best_vect_knapsack(first_mat_reduced)
        self.assertEqual(self.best_vect_first_sum, res) 

    def test_lll_reduction_knapsack2(self):
        second_mat = create_matrix_from_knapsack(self.pubkey, self.second_sum)
        self.assertEqual(0, islll(second_mat)) 
        second_mat_reduced = lll_reduction(second_mat)
        self.assertEqual(1, islll(second_mat_reduced)) 
        res = best_vect_knapsack(second_mat_reduced)
        self.assertEqual(self.best_vect_second_sum, res) 

    def test_lll_reduction_not_full_rank(self):
        basis = create_matrix(self.not_full_rank)
        expected_reduced_basis = create_matrix(self.not_full_rank_reduced)
        reduced_basis = lll_reduction(basis)
        self.assertEqual(expected_reduced_basis, reduced_basis) 



if __name__ == '__main__':
    unittest.main()
