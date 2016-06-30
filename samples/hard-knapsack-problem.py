from liblll import *

pubkey = [6540888028860333268, 10724927494100152566, 7437764146142504235, 10923971926220653754, 1344346752246811475, 9081586885313697235, 3154766147261118272, 6599167894240630555, 6900004602215108806, 9533144650045521276, 12494886885327238797, 9322310964898911721, 11288897190203350086, 11652486987151529360, 5819221709466577658, 4322746197318339004, 10121811235098484482, 878037699937336259, 5614291386744850395, 4785671426070643848, 12360519029676519368, 8670694547086670532, 7863700661863175326, 6835922537529215029, 11860687372009192176, 2160255437154325511, 6945405259905216278, 9234506499337280811, 7894470988622533862, 2702267599744542684, 5725983718195848294, 444144665217672832]

the_sum = 101182239602424757338

mat = create_matrix_from_knapsack(pubkey, the_sum)
mat_reduced = lll_reduction(mat)

best_vect = best_vect_knapsack(mat_reduced)

# try complementary ?
apply_complementary = True
for i in range(len(best_vect)):
    if best_vect[i] != 0:
        apply_complementary = False

if apply_complementary:
    print("try complementary lattice")
    total_sum = 0
    for i in range(len(pubkey)):
        total_sum += pubkey[i]

    mat = create_matrix_from_knapsack(pubkey, total_sum-the_sum)
    mat_reduced = lll_reduction(mat)

    best_vect = best_vect_knapsack(mat_reduced)

    my_sum = 0
    for i in range(len(pubkey)):
        if best_vect[i] == 0:
            my_sum += pubkey[i]
    
    print("Verification :")
    print("my_sum = %ld, the_sum = %ld" % (my_sum, the_sum))

else:
    my_sum = 0
    for i in range(len(pubkey)):
        if best_vect[i] == 1:
            my_sum += pubkey[i]
    
    print("Verification :")
    print("my_sum = %ld, the_sum = %ld" % (my_sum, the_sum))

print("best_vect = ", best_vect)
