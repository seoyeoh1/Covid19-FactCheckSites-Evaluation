# Covid19-FactCheckSites-Evaluation

### Are Covid-19 fact-check sites satisfying user needs?

We pursued a project evaluating the effectiveness of current Korean Covid-19 fact-check sites regarding information acquisition.

This project can be organized into three steps:

#### 1. Identifying users' informational needs
  - __Topic Scope Analysis__: Through performing topic modeling on user-generated questions from Q&A sites, we identified the scope of topics users questioned.
  - __Topic Depth Analysis__: From each topics identified, we performed co-occurence network analysis to discover sub-topics
  
*By comparing the topics dealt with in Q&A sites and fact-check sites, we assessed __whether fact-check sites addressed the topics users were interested in.__*

#### 2. Evaluating the quality of answers provides
  - We evaluated the quality of answers provided to users in fact-check sites
  
  Evaluation Criteria | Measures
  ------------ | -------------
  Quality | Answer length, Average number of nouns within a sentence
  Readability | Key sentence location, Average number of verb phrases by sentence
  Uncertainty | The level of answer ambiguity
  
#### Sites Referred
Q&A Sites:
  - Naver Kin: https://kin.naver.com/
  - Aha: https://www.a-ha.io/
  - HiDoc: https://www.hidoc.co.kr/

Fact Check Sites:
  - Seoul National University Fact Check Site: https://factcheck.snu.ac.kr/
  - Ministry of Health and Wealthfare: http://ncov.mohw.go.kr/factBoardList.do
