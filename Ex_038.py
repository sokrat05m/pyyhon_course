# https://www.codewars.com/kata/52449b062fb80683ec000024/train/python

def generate_hashtag(s):
    if (len(s) == 0) or (len(s) > 140):
        return False
    s = str.strip(s)
    s = str.title(s)
    s = ''.join(s.split())
    s = f"#{s}"
    return s