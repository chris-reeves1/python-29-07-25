General comments
Mark did well in this module. He demonstrated a good understanding of concepts we 
covered and showed he has a broad knowledgebase. 
He contributed to discussions and asked relevant questions. 

Learner Punctuality and engagement 
Mark was punctual throughout the module and engaged well through Webex. 

Recommendations on further learning
Continue to practice the basics of containerisation, Kubernetes and pipelines.


requirments:
- list of students. (contruct from prompt)
- input scores 1-4 for following attrubutes:
    - overal performance
    - General understanding
    - Contribution level
    - lab completion
    - punctuality
    - engagement
    - further study level

- Generate templates for feedback. Map scores to phrases/sentances 
    that can be added to a general feedback structure. 

    eg:
    x = {1:"ok", 2:"well", 3: "good", 4:"very good"}

    template = f"General Comments\n {student_name} did {x[{score}]} in this module.../n/n"
    template += f"Puctualiuty/n ...../n/n"
    template += f"Further learning...."

- save the feedack to a file for each student. 
    - File name should include the student name. 
    - All files to be saved to a directory called 'feedback'.
    - open the file in an editor to allow for changes/approval.

- fucntionality/comments/design/doc-strings/readibility/naming-convention. 
- stretch goal: formating for anything displayed on cli (colours/spacing)
- max 3 hours 