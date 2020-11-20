# ConsumerAffairs

## Acceptance Criteria
 
- [ ] The completed assignment must be hosted in a git repository
  - The repository must include commit history (e.g., more than one commit)
- [ ] Users are able to submit reviews to the API
- [ ] Users are able to retrieve reviews that they submitted
- [ ] Users cannot see reviews submitted by other users
- [X] Use of the API requires a unique auth token for each user
- [X] Submitted reviews must include, at least, the following attributes:
  - [X] Rating - must be between 1 - 5
  - [X] Title - no more than 64 chars
  - [X] Summary - no more than 10k chars
  - [X] IP Address - IP of the review submitter
  - [X] Submission date - the date the review was submitted
  - [X] Company - information about the company for which the review was submitted, can be simple text (e.g., name, company id, etc.) or a separate model altogether
  - [X] Reviewer Metadata - information about the reviewer, can be simple text (e.g., name, email, reviewer id, etc.) or a separate model altogether
- [ ] Unit tests must be included providing 100% code coverage
- [ ] Include instructions on local setup details for both “app setup” and “data setup”
- [ ] Document the API
 
### Optional: 
 
- [ ] Provide an authenticated admin view that allows me to view review submissions
 
Organize the schema and data models in whatever manner you think makes the most sense and feel free to add any additional style and flair to the project that you'd like.
 
