# -*- coding: utf-8 -*-

def formalize_police_number(policy_number):
    policy = []
    i = 0
    for cc, item in enumerate(policy_number):
        if item.isdigit():
            i += 1
        else:
            if i:
                policy.append(str(i))
                policy.append(item)
                i = 0
            else:
                policy.append(item)
        if cc == len(policy_number) - 1:
            policy.append(str(i))
    return ''.join(policy)