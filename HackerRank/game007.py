def count_substring(string, sub_string):
    cnt=0
    for i in range(len(string)-len(sub_string)+1):
        if string[i:i+len(sub_string)]==sub_string:
            cnt+=1
    return cnt
