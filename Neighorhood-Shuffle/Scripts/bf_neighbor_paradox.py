def expected_distance(num_houses=100):
    total_dist = 0
    case_count = 0
    
    for you in range(num_houses):
        for friend in range(num_houses):

            # account for constraint violations
            if you != friend:
                total_dist += abs(you-friend)
                case_count += 1
    
    return(total_dist/case_count)