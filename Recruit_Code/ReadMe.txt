Goal	                                                            Status
Understand how relevant a candidate is to a job beyond keywords	    Semantic analysis
Generate a rich feature set using profile info                      You have full profiles
Train a strong ML model to rank candidates for each job             XGBoost is perfect
Test that model on new jobs & candidates                            You’ll do that after training

1
The data for candidate is live linkedin candidate data from Northeastern Univeristy.
Job Data was scaped from google using SERP API for saving manual efforts.
For each Job-Candidate pair, I generatde these features:

2
Feature                         Description
Feature	How to Generate
skills_semantic_score	          compare skill sets
experience_semantic_score	      compare exp text with JD
project_semantic_score	        compare project desc with JD
education_semantic_score	      compare degree/study field with JD
overall_semantic_match_score	  weighted average of above

3 
Summary: Semantic Analysis in Your Pipeline
Step	                    Semantic Used?	Tool/Library
JD Skill/Role Extraction	No	            Keyword / Regex
Skill Matching	          Yes	            SentenceTransformers
Experience Relevance	    Yes	            SemanticSimilarity
Project Matching	        Yes	            Cosine Similarity (First Approach to use BERT +cosine similarity(resulyted in low score))
ML Training	              Uses scores	    scikit-learn/XGBoost

4
Later used Ensamble modeling for tter scoring for all features. 
Models Used
all-mpnet-base-v2
intfloat/e5-base
BAAI/bge-base-en-v1.5

5
semantic feature dataset (Candidate-Job pairs) with semantic scores, for training your XGBoost ranking model:
Column Name	                    Description	                        Example Value
Candidate_ID	                  Unique candidate identifier	        6
Candidate_Name	                Name of the candidate	              Akshath Kamath
Job_ID	                        Unique Job identifier	              1
Job_Title	                      Job position/title	                Data Scientist
Company	                        Company Name	                      ASSA ABLOY
skills_semantic_score	          Skillset match (0-1)	               0.87
experience_semantic_score       Experience relevance score (0-1)	  0.74
project_semantic_score	        Project relevance score (0-1)	      0.80
publication
certification
education_semantic_score	    Education relevance score (0-1)	      0.60
Weighted average semantic score	                                    0.79
Label (Optional but Ideal)      Binary label indicating relevance   (1 or 0)	1 (Relevant), 0 (Not Relevant)

6
overall score smeantics calculated for Ranking based on final score with following weight preferences:
Experience: 40%
Projects: 40%
Publications: 6.67%
Skills: 6.67%
Education: 6.67%

Model Type	                When to Use	Pros	                                                          Cons
XGBoost + rank:pairwise	    For better rankings in your current setup	Simple upgrade, good ranking	    Slightly more complex than regression
LightGBM Ranker	            Need speed on large dataset	Very fast, accurate	                            Less documentation than XGBoost
BERT-based Ranker	          Deep NLP + semantic matching	                                              Most accurate for semantics	Needs large data + infra

model used: XGBoost + rank:pairwise. 

Pros: I was able to implement a authentic Datascience traing algorithm. But that created load on CPU.
Plan to explore LightGBM Ranker for faster and accurate results.
using LLM and Open AI was out of the scope of this project as I worked on purely Data Science Project.
