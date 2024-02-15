def event_probability(total, event):
    prob = (event / total) * 100
    return f"{prob:.2f}%"

def event_not_probability(total, event):
    # complement rule
    prob = (1 - (event / total)) * 100
    return f"{prob:.2f}%"

def disjoint_event_probability(total, event1, event2):
    # P(S u B) = P(S) + P(B) 
    prob = ((event1 + event2) / total) * 100
    return f"{prob:.2f}%"

def joint_event_probability(total, event1, event2, intersection):
    # inclusion-exclusion principle
    # P(S u B) = P(S) + P(B) − P(S n B)
    prob = ((event1 + event2 - intersection) / total) * 100
    return f"{prob:.2f}%"

if __name__ == "__main__":
    total_ppl = 100
    like_fb = 30
    like_bb = 40
    like_both = 20

    # in totatl people what is the change that person likes fb
    print(event_probability(total_ppl, like_fb))
    print(event_not_probability(total_ppl, like_fb))

    # if you can only like fb or bb, probability of liking either one
    print(disjoint_event_probability(total_ppl, like_fb, like_bb))

    # if you can like both fb and bb, % of total doing either
    print(joint_event_probability(total_ppl, like_fb, like_bb, like_both))
