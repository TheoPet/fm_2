# from bwt_fmindex_search.sa import *
from bwt_fmindex_search.fmindex import *

# Test suffix array functions

# Naive algorithm tests
text_normal_1 = "abracadabra"
text_normal_2 = "banana"
text_repetitive = "nanananananinininenene"
text_empty = ""
text_with_num = "aaba4bba2"
text_with_blancs= "This is a text"

assert set(suffix_array_naive(text_normal_1)) == set([10, 7, 0, 3, 5, 8, 1, 4, 6, 9, 2]), "Assertion error:" \
                                                                                          " suffix array" \
                                                                                          " naive failed with normal_1"

assert set(suffix_array_naive(text_normal_2)) == set([5, 3, 1, 0, 4, 2]), "Assertion error: suffix array with " \
                                                                          "normal_2 failed"
assert set(suffix_array_naive(text_repetitive)) == set([1, 3, 5, 7, 9, 21, 19, 17, 15, 13, 11, 0, 2, 4, 6, 8, 20,
                                                        18, 16, 14, 12, 10]), "Assertion error: suffix array naive " \
                                                                              "failed with repetitive string"

assert set(suffix_array_naive(text_empty)) == set([]), "Assertion error: suffix array naive failed with empty string"
assert set(suffix_array_naive(text_with_num)) == set([8, 4, 7, 3, 0, 1, 6, 2, 5]), "Assertion error: " \
                                                                                  "suffix array naive failed with " \
                                                                                  "num string"

assert set(suffix_array_naive(text_with_blancs)) == set([7, 4, 9, 0, 8, 11, 1, 5, 2, 6, 3, 13, 10, 12]), \
                                                    "Assertion error:suffix array naive failed on text_with_blancs"


# Suffix_array_manber_myers tests
assert set(suffix_array_manber_myers(text_normal_1)) == set([10, 7, 0, 3, 5, 8, 1, 4, 6, 9, 2]), "Assertion error:" \
                                                                                                 "manber_myers failed" \
                                                                                                 "with normal_1"
assert set(suffix_array_manber_myers(text_normal_2)) == set([5, 3, 1, 0, 4, 2]), "Assertion error: manber_myers " \
                                                                                 "failed with normal_2"
assert set(suffix_array_manber_myers(text_repetitive)) == set([1, 3, 5, 7, 9, 21, 19, 17, 15, 13, 11, 0, 2, 4, 6, 8,
                                                              20, 18, 16, 14, 12, 10]), "Assertion error:" \
                                                                                        "manber_myers failed with" \
                                                                                        "repetitive string"

assert set(suffix_array_manber_myers(text_empty)) == set([]), "Assertion error: manber_myers failed with empty string"
assert set(suffix_array_manber_myers(text_with_num)) == set([8, 4, 7, 3, 0, 1, 6, 2, 5]), "Assertion error:" \
                                                                                          "manber_myers failed" \
                                                                                          "on string with numbers"

assert set(suffix_array_manber_myers(text_with_blancs)) == set([7, 4, 9, 0, 8, 11, 1, 5, 2, 6, 3, 13, 10, 12]),\
                                                            "Assertion error: manber_myers failed on string with blancs"


#Test BWT

text_normal_bwt_1 = "abracadabra$"
suffix_array_normal_1 = suffix_array_manber_myers(text_normal_bwt_1)
assert (bw_transform(text_normal_bwt_1, suffix_array_normal_1)) == "ard$rcaaaabb"


text_normal_bwt_2 = "banana$"
suffix_array_normal_2 = suffix_array_manber_myers(text_normal_bwt_2)
assert (bw_transform(text_normal_bwt_2, suffix_array_normal_2)) == "annb$aa"

text_bwt_repetitive = "nanananananinininenene$"
suffix_array_repetitive = suffix_array_manber_myers(text_bwt_repetitive)
assert (bw_transform(text_bwt_repetitive, suffix_array_repetitive)) == "ennnnnnnnnnn$aaaaeeiiia"

text_bwt_empty = "$"
suffix_array_empty = suffix_array_manber_myers(text_bwt_empty)
assert (bw_transform(text_bwt_empty, suffix_array_empty)) == "$"

text_bwt_num = "aaba4bba2$"
suffix_array_num = suffix_array_manber_myers(text_bwt_num)
assert (bw_transform(text_bwt_num, suffix_array_num)) == "2aabb$aba4"

text_bwt_blancs = "This is a text$"
suffix_array_blancs = suffix_array_manber_myers(text_bwt_blancs)
assert (bw_transform(text_bwt_blancs, suffix_array_blancs)) == "ssat$ tT hiix e"

#Test helper functions

#count characters
assert(count_characters(text_normal_1)) == (Counter({'a': 5, 'b': 2, 'c': 1, 'd': 1, 'r': 2}))
assert(count_characters(text_empty)) == Counter()
assert(count_characters(text_with_blancs)) == (Counter({' ': 3, 'i': 2, 's': 2, 't': 2, 'a': 1, 'e': 1,
                                                        'h': 1, 'T': 1, 'x': 1}))

#terminate string
assert(terminate_string(text_normal_1)) == "abracadabra$"
assert(terminate_string(text_with_blancs)) == "This is a text$"
assert(terminate_string(text_empty)) == "$"
assert(terminate_string(text_bwt_num)) == "aaba4bba2$"

#calculate ranks
assert(calculate_ranks(text_normal_1)) == [0, 0, 0, 1, 0, 2, 0, 3, 1, 1, 4]
assert(calculate_ranks(text_normal_bwt_1)) == [0, 0, 0, 1, 0, 2, 0, 3, 1, 1, 4, 0]
assert(calculate_ranks(text_empty)) == []
assert(calculate_ranks(text_bwt_empty)) == [0]
assert(calculate_ranks(text_repetitive)) == [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 0, 6, 1, 7, 2, 8, 0, 9, 1, 10, 2]
assert(calculate_ranks(text_with_blancs)) == [0, 0, 0, 0, 0, 1, 1, 1, 0, 2, 0, 0, 0, 1]
assert(calculate_ranks(text_bwt_blancs)) == [0, 0, 0, 0, 0, 1, 1, 1, 0, 2, 0, 0, 0, 1, 0]
assert(calculate_ranks(text_bwt_num)) == [0, 1, 0, 2, 0, 1, 2, 3, 0, 0]

# FM testing
count_normal_text_1 = count_characters(text_normal_bwt_1)
count_normal_text_2 = count_characters(text_normal_bwt_2)
count_text_num = count_characters(text_bwt_num)
count_text_empty = count_characters(text_bwt_empty)
count_text_repetitive = count_characters(text_bwt_repetitive)
count_text_blancs = count_characters(text_bwt_blancs)

assert(calculate_first_occurrences(count_normal_text_1)) == {'$': 0, 'a': 1, 'b': 6, 'c': 8, 'd': 9, 'r': 10}
assert(calculate_first_occurrences(count_normal_text_2)) == {'$': 0, 'a': 1, 'b': 4, 'n': 5}
assert(calculate_first_occurrences(count_text_num)) == {'$': 0, '2': 1, '4': 2, 'a': 3, 'b': 7}
assert(calculate_first_occurrences(count_text_empty)) == {'$': 0}
assert(calculate_first_occurrences(count_text_repetitive)) == {'$': 0, 'a': 1, 'e': 6, 'i': 9, 'n': 12}
assert(calculate_first_occurrences(count_text_blancs)) == {'$': 0}

if __name__ == "__main__":
 sort_bucket_test = [1, 5, 7, 8, 9, 5]
 #sort_bucket(sort_bucket_test, [1, 2])
text_normal_bwt_num = "aaba4bb2$"
#suffix_array_num = suffix_array_manber_myers(text_normal_bwt_num)
print(count_characters(text_normal_bwt_num))
#print (calculate_ranks((text_normal_bwt_num)))
print (calculate_first_occurrences(count_characters(text_normal_bwt_num)))

#print (bw_transform(text_normal_bwt_num, suffix_array_num))