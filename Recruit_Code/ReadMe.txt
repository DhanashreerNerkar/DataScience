Goal	                                                            Status
Understand how relevant a candidate is to a job beyond keywords	    Semantic analysis
Generate a rich feature set using profile info                      You have full profiles
Train a strong ML model to rank candidates for each job             XGBoost is perfect
Test that model on new jobs & candidates                            You’ll do that after training

For each Job-Candidate pair, we’ll generate these features:

Feature                         Description
Feature	How to Generate
skills_semantic_score	        compare skill sets
experience_semantic_score	    compare exp text with JD
project_semantic_score	        compare project desc with JD
education_semantic_score	    compare degree/study field with JD
overall_semantic_match_score	weighted average of above

Summary: Semantic Analysis in Your Pipeline
Step	                    Semantic Used?	Tool/Library
JD Skill/Role Extraction	No	            Keyword / Regex
Skill Matching	            Yes	            SentenceTransformers
Experience Relevance	    Yes	            SemanticSimilarity
Project Matching	        Yes	            Cosine Similarity
ML Training	                Uses scores	    scikit-learn/XGBoost

semantic feature dataset (Candidate-Job pairs) with semantic scores, for training your XGBoost ranking model:
Column Name	                    Description	                        Example Value
Candidate_ID	                Unique candidate identifier	        6
Candidate_Name	                Name of the candidate	            Akshath Kamath
Job_ID	                        Unique Job identifier	            1
Job_Title	                    Job position/title	                Data Scientist
Company	                        Company Name	                    ASSA ABLOY
skills_semantic_score	        Skillset match (0-1)	            0.87
experience_semantic_score       Experience relevance score (0-1)	0.74
project_semantic_score	        Project relevance score (0-1)	    0.80
publication
certification
education_semantic_score	    Education relevance score (0-1)	    0.60
Weighted average semantic score	                                    0.79
Label (Optional but Ideal)      Binary label indicating relevance   (1 or 0)	1 (Relevant), 0 (Not Relevant)

Ranking based on final score with following weight preferences:
Experience: 40%
Projects: 40%
Publications: 6.67%
Skills: 6.67%
Education: 6.67%

Model Type	                When to Use	Pros	                                                        Cons
XGBoost + rank:pairwise	    For better rankings in your current setup	Simple upgrade, good ranking	Slightly more complex than regression
LightGBM Ranker	            Need speed on large dataset	Very fast, accurate	                            Less documentation than XGBoost
BERT-based Ranker	        Deep NLP + semantic matching	                                            Most accurate for semantics	Needs large data + infra


model used: XGBoost + rank:pairwise