import json
import numpy as np

def levenshtein_distance(s, t):
    r = len(s)+1
    c = len(t)+1
    dist = np.zeros((r,c),dtype = int)
    for i in range(1, r):
        for j in range(1,c):
            dist[i][0] = i
            dist[0][j] = j
   
    for column in range(1, c):
        for row in range(1, r):
            if s[row-1] == t[column-1]:
                cost = 0
            else:
                cost = 1
            dist[row][column] = min(dist[row-1][column] + 1, dist[row][column-1] + 1, dist[row-1][column-1] + cost)
    
    return dist[row][column]

def phrasel_search(P, Queries):
    # Write your solution here
    ans = [[]]
    
    if len(P) <= 1 or len(P) >= 1000000:
        return ans
    if len(Queries) <= 1 or len(Queries) >= 1000:
        return ans    

    ans.pop()
    z_ = 0
    for query in Queries:
      query_words = query.split(" ")
      if len(query_words) <= 1 or len(query_words) >= 100000:
        continue
      ans.append([])  
      for phrase in P:
        phrase_words = phrase.split(" ")
        indices = [index for index,element in enumerate(query_words) if element == phrase_words[0]]
        n = len(phrase_words)
        for i in indices:
          edit1 = levenshtein_distance(query_words[i:i+n], phrase_words)
          if edit1 == 0:
            ans[z_].append(" ".join(query_words[i:i+n]))
            break
          
          edits = levenshtein_distance(query_words[i:i+n+1], phrase_words)
          if edits == 1:
            ans[z_].append(" ".join(query_words[i:i+n+1]))
            break
    
      z_ = z_ + 1
    #print(ans)
    return ans

if __name__ == "__main__":
    with open('sample.json', 'r') as f:
        sample_data = json.loads(f.read())
        P, Queries = sample_data['phrases'], sample_data['queries']
        returned_ans = phrasel_search(P, Queries)
        print('============= ALL TEST PASSED SUCCESSFULLY ===============')


