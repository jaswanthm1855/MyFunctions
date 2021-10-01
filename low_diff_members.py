def low_diff_members(input1, input2, input3):
    input2.sort(reverse=True)
    actual_members = []
    diff_between_actual_members = 100000000
    for i in range(0, input1):
        members = []
        diff_between_members = 0
        if i+input3 > input1:
            continue
        members.extend(input2[i: i+input3])
        for member_pos in range(0, len(members)):
            for other_member_pos in range(member_pos+1, len(members)):
                print(f"f_member={members[member_pos]}, other_member={members[other_member_pos]}")
                diff_between_members += members[member_pos] - members[other_member_pos]
            print(f"diff_between_members={diff_between_members}")
            if diff_between_members < diff_between_actual_members:
                diff_between_actual_members = diff_between_members
                actual_members = members

    print(actual_members)