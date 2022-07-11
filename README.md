# QnA-Made-Easy

## Inspiration
- Every online presentation, speech, or class is accompanied by a Q&A session in the end. In meetings with huge participation, the speaker is bombarded with questions. 
- A lot of people tend to ask the same question more than once. This makes it difficult for the moderator to filter out the unaddressed questions.
- It becomes a horrific ordeal when attendees send vulgar messages in the meeting's chat section. Popular video conferencing apps do not have the option to filter out such offensive messages.
- Additionally, the name of the person is displayed along with questions posted. Because of this people fear that their questions could be termed as ‘silly’ and what would others think of them. This fear of insecurity holds them back from asking questions. 

## Our solution
- A simple chrome extension that users can use to post questions anonymously during an online meeting. The extension automatically captures the meeting code and directs the questions to the backend database specific to that meeting code only.
- The extension also supports Speech Recognition, in case you do not want to type a long question.
- Before storing the questions in the database they undergo 2 checks:
  1. Profanity Check: To filter out offensive messages. 
  2. Similarity Check: To check if a similar question already exists in the database. 
- In the dashboard, the moderator can see the list of all the filtered questions. There is an option to reject a question or send the question to a temporary buffer zone. 
- If the moderator approves the question, it will appear automatically in the meeting's chat section.

## Novelty
- **Speech Recognition:** In case you do not want to type a long question, just read it aloud. 
- **Profanity Check:** Filters out the vulgar and offensive messages. 
- **Similarity Check:** Filters out the questions which are repetitive and similar. 
- **Anonymity:** In case you are hesitant or not confident to ask a question, we do not reveal your identity.
- **Dashboard:** To manage the filtered questions and post them to the meeting's chat section.

## How we built it
Our backend was made with **Django** and **Bootstrap** was used for frontend styling. For web automation and sending messages from the Django backend to Google Meet, we used **Selenium**. We used a trained **Linear SVM Model** to filter out messages that contain offensive content. For the similarity checker **Sentence Transformers** was used to generate vector embeddings and **Cosine Similarity** was used to generate the similarity score.


## How it works
<img src="https://i.ibb.co/KVTF58b/UB-hacking-2.png" width="500">

## Accomplishments that we're proud of
Going solo is never easy and I am proud of what I accomplished in 24 hours. This is the first time I built a Chrome Extension. Additionally, I figured out a way to use Selenium for sending messages from Django Backend to the Google Meet's chat section in real-time. 

## What's next for Q&A Made Easy
- Publish the extension on Chrome Store and deploy the Django backend service.
- Integrating a priority-based ranking system for questions.
- Figure out a way to capture the speaker's answer to every question and save it as a transcript.
