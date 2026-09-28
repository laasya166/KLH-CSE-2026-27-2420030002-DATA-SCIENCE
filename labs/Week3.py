#%%
import numpy as np
from scipy.spatial import distance
pointA=np.array([2,4,6])
pointB=np.array([5,1,9])
eucledian_dist=distance.euclidean(pointA,pointB)
print("Eucledian Distance:",eucledian_dist)
similarity_eulidean=1/(1+eucledian_dist)
print("Eucledian Similarity:",similarity_eulidean)
# %%
manhattan_dist=distance.cityblock(pointA,pointB)
print("Manhattan Distance:",manhattan_dist)
similarity_manhattan=1/(1+manhattan_dist)
print("Manhattan Similarity:",similarity_manhattan)
# %%
minkowski_dist=distance.minkowski(pointA,pointB,p=3)
print("Minkowski Distance:",minkowski_dist)
# %%
import pandas as pd
df=pd.DataFrame({
    'X':[10,20,30,40,50],
    'Y':[12,24,33,45,60]
})
corr_matrix=df.corr(method='pearson')
print("Pearson Correlation Matrix:\n",corr_matrix)
# %%
import pandas as pd
df=pd.DataFrame({
    'X':[10,20,30,40,50],
    'Y':[10,20,30,40,50]
})
corr_matrix=df.corr(method='pearson')
print("Pearson Correlation Matrix:\n",corr_matrix)
# %%
import pandas as pd
df=pd.read_csv("Iris.csv")
print(df.corr(method='pearson', numeric_only=float))
# %%
import pandas as pd
from scipy.stats import spearmanr
df=pd.DataFrame({
    'X':[10,20,30,40,50],
    'Y':[12,18,33,47,55]
})
corr_value,p_value=spearmanr(df['X'],df['Y'])
print(f"Spearman Correlatiion Coefficient:{corr_value}")
print(f"P-value:{p_value}")
# %%
import pandas as pd
df=pd.read_csv("Iris.csv")
print(df.corr(method='spearman', numeric_only=float))
# %%
import pandas as pd
from scipy.stats import spearmanr
df=pd.DataFrame({
    'sname':['a','b','c','d','e'],
    'TOC':[10,20,30,40,50],
    'QC':[12,18,33,47,55],
    'CD':[20,60,80,45,50],
    'DS':[12,15,39,41,55],
    'ASE':[10,28,29,47,33]
})
pearson_corr=df.corr(method='pearson',numeric_only=float)
print("Pearson Correlation Matrix:\n",pearson_corr)
spearman_corr=df.corr(method='spearman',numeric_only=float)
print("Spearman Correlation Matrix:\n",spearman_corr)
# %%
def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Strings must be of the same length")
    return sum(ch1 != ch2 for ch1, ch2 in zip(str1, str2))
s1="Karolin"
s2="Karelin"
hamming_dist=hamming_distance(s1,s2)
print(f"Hamming Distance between '{s1}' and '{s2}': {hamming_dist}")
# %%
def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Strings must be of the same length")
    return sum(ch1 != ch2 for ch1, ch2 in zip(str1, str2))
s1="My name is laasya"
s2="My name is not ya"
hamming_dist=hamming_distance(s1,s2)
print(f"Hamming Distance between '{s1}' and '{s2}': {hamming_dist}")
# %%
def jaccard_index(str1, str2):
    set1,set2=set(str1.split()),set(str2.split())
    intersection = set1.intersection(set2)
    union=set1.union(set2)
    return len(intersection)/len(union)
s1="data science is fun"
s2="science makes data useful"
print("Jaccard Index:",jaccard_index(s1,s2))
# %%
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
s1="data science is fun"
s2="science makes data useful"
vectorizer = CountVectorizer().fit([s1,s2])
vectors = vectorizer.transform([s1,s2])
cos_sim=cosine_similarity(vectors[0],vectors[1])[0][0]
print("Cosine Similarity: ",cos_sim)
# %%
def lcs_length(X,Y):
    m,n=len(X),len(Y)
    dp=[[0]*(n+1) for _ in range(m+1)]
    for i in range(m):
        for j in range(n):
            if X[i]==Y[j]:
                dp[i+1][j+1]=dp[i][j]+1
            else:
                dp[i+1][j+1]=max(dp[i+1][j],dp[i][j+1])
    return dp[m][n]

seq1="ABCDEF"
seq2="AEBDF"
length=lcs_length(seq1,seq2)
print(f"Length of Longest Common Subsequence between '{seq1}' and '{seq2}': {length}")

# %%
