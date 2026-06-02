# ML System Design — Real-Time CTR Prediction for Ad Bidding

- **Difficulty**: Hard (System Design)
- **Time budget**: ~25 min (think out loud, then write notes)
- **Format**: Open-ended. Write your answer as structured notes below.

## Context
You are designing the Click-Through Rate (CTR) prediction model for a real-time ad
bidding system. Every time a user visits a web page, an auction happens in ~100ms.
Your model must return a CTR score for each candidate ad in **under 10ms**.

## Questions to Answer

### 1. Label Definition
- How do you define the label (clicked = 1, not clicked = 0)?
- What is the **click delay problem**? If a user clicks 2 hours after seeing the ad,
  how do you handle training data collection?
- What is **label sparsity**? Roughly what % of ad impressions result in a click?

### 2. Features
List at least 8 features you would use. For each, note its category:
- User features (e.g. demographics, interest profile)
- Ad features (e.g. category, historical CTR)
- Context features (e.g. device, time of day, page topic)
- Cross features (combinations)

Then answer: `user_id` and `ad_id` have millions of unique values.
How do you encode them without creating an enormous sparse matrix?
(Hint: **embedding layers** or **feature hashing**)

### 3. Model Choice
- What is your baseline model? Why?
- What is your production model? Why?
- Famous real-world reference: Facebook used **GBDT + Logistic Regression** (2014 paper).
  What was the idea? Can you explain it in one sentence?

### 4. Meeting the 10ms Latency Requirement
List at least 3 concrete engineering decisions that make this possible.

### 5. Evaluation Metrics
- What offline metric do you use? Why NOT accuracy?
- What online metric do you use to measure real business impact?
- What is **calibration** and why does it matter for CTR models specifically?

## Write Your Answer Below
(Replace these prompts with your notes)

### My Label Definition
...

### My Feature List
...

### My Model Choice
...

### My Latency Strategy
...

### My Metrics
...
