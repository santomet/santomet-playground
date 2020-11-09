from itertools import chain, combinations
from math import ceil


def all_subsets(ss, min_count=0):
    return chain(*map(lambda x: combinations(ss, x), range(min_count, len(ss)+1)))



def main():
    # general values
    no_of_states = 27
    quota1 = 55  #In percent! This is our minimum of 17 states
    quota2 = 65  # In percent! this is our minimum of 65% of population

    # indexes: do not change this!
    i_name = 0
    i_quota1_value = 1
    i_quota2_value = 2
    i_no_of_swings = 3

    states_all = []
    states_all.append(["Austria", 100 / no_of_states, 1.98, 0])
    states_all.append(["Belgium", 100 / no_of_states, 2.56, 0])
    states_all.append(["Bulgaria", 100 / no_of_states, 1.56, 0])
    states_all.append(["Croatia", 100 / no_of_states, 0.91, 0])
    states_all.append(["Cyprus", 100 / no_of_states, 0.2, 0])
    states_all.append(["Czechia", 100 / no_of_states, 2.35, 0])
    states_all.append(["Denmark", 100 / no_of_states, 1.3, 0])
    states_all.append(["Estonia", 100 / no_of_states, 0.3, 0])
    states_all.append(["Finland", 100 / no_of_states, 1.23, 0])
    states_all.append(["France", 100 / no_of_states, 14.98, 0])
    states_all.append(["Germany", 100 / no_of_states, 18.54, 0])
    states_all.append(["Greece", 100 / no_of_states, 2.4, 0])
    states_all.append(["Hungary", 100 / no_of_states, 2.18, 0])
    states_all.append(["Ireland", 100 / no_of_states, 1.10, 0])
    states_all.append(["Italy", 100 / no_of_states, 13.65, 0])
    states_all.append(["Latvia", 100 / no_of_states, 0.43, 0])
    states_all.append(["Lithuania", 100 / no_of_states, 0.62, 0])
    states_all.append(["Luxembourg", 100 / no_of_states, 0.14, 0])
    states_all.append(["Malta", 100 / no_of_states, 0.11, 0])
    states_all.append(["Netherlands", 100 / no_of_states, 3.89, 0])
    states_all.append(["Poland", 100 / no_of_states, 8.49, 0])
    states_all.append(["Portugal", 100 / no_of_states, 2.3, 0])
    states_all.append(["Romania", 100 / no_of_states, 4.34, 0])
    states_all.append(["Slovakia", 100 / no_of_states, 1.22, 0])
    states_all.append(["Slovenia", 100 / no_of_states, 0.47, 0])
    states_all.append(["Spain", 100 / no_of_states, 10.49, 0])
    states_all.append(["Sweden", 100 / no_of_states, 2.29, 0])


    # Check state count
    if len(states_all) == no_of_states:
        print("Preset number of states and actual number of states in list checks! ", no_of_states)
    else:
        print("Preset number of states and actual number of states in list does not correspond: ", no_of_states, " vs ", len(states_all))
        exit(1)

    # Check population
    population_check = 0
    for s in states_all:
        population_check += s[i_quota2_value]

    if population_check == 100:
        print("Correct! population counts to 100!")
    else:
        print("Error! Sum of population (quota 2) in the list is ", population_check)
        print("However some discrepancy is found even in official voting calculator so let's continue")

    # Now compute the min_states:
    min_states = ceil(no_of_states / 100 * quota1)

    print("Computed minimum of states for quota 1 is ", min_states)

    #now for the banzhaf: first get all the possible combinations

    no_of_swings_total = 0  # Save total number of flippers here: <3

    print("COMPUTING.....................")

    for subset in all_subsets(states_all, min_states):
        # Now i know that in this subset quota 1 already is satisfied, we only have to check if population quota is:
        population = 0
        for s in subset:
            population += s[i_quota2_value]

        if not population >= quota2: # If this does not meet, just skip and continue in the cycle
            continue


        # So we have both quotas satisfied. States in subset will win the qualified majority
        # Now the challenge is to find all the states which will change this if they swing
        # And save the fact in total and their counter.
        # Because we know that in the first quota they all have value of 1, we just remember that if
        # exactly min_states (for now 15) states are selected in this subset, we will count that as a breach

        quota1_not_satisfied = len(subset) == min_states

        for s in subset:
            # most important condition of them all!!
            quota2_not_satisfied = (population - s[i_quota2_value]) < quota2

            if quota1_not_satisfied or quota2_not_satisfied:
                no_of_swings_total += 1
                s[i_no_of_swings] += 1


    # Great! now just print results:
    print("Total swing votes: ", no_of_swings_total)

    print("Country name\tBanzhaf\tBanzhaf normalized".expandtabs(10))
    print("-------------------------------------------------------------------")
    for s in states_all:
        print("{0}\t{1}\t{2}%".format(s[i_name], s[i_no_of_swings],
                                                     s[i_no_of_swings]/no_of_swings_total*100).expandtabs(15))


    def sortfunc(s):
        return s[i_no_of_swings]

    states_all.sort(key=sortfunc, reverse=True)
    print()
    print()
    print("Sorted:")

    print("Country name\tBanzhaf\tBanzhaf normalized".expandtabs(10))
    print("-------------------------------------------------------------------")
    for s in states_all:
        print("{0}\t{1}\t{2}%".format(s[i_name], s[i_no_of_swings],
                                                     s[i_no_of_swings] / no_of_swings_total * 100).expandtabs(15))



if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()
