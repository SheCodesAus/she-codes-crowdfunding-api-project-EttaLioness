# {{ ResearchMob }}
​


## What is ResearchMob?
ResearchMob is a crowdfunding platform enabling the community, industry and academia to contribute funding towards innovative scientific research.
Funds are directly distributed to the scientists conducting the research project, unlike receiving grands at a University where generally only 85-50% of total funds are received. 


## Target Audience
Open to the community and organisations that are interested in research and science that would otherwise have no access or ability to fund a scientific project. Contributors also have the choice to be acknowledged in the publication, thereby having a direct scientific impact that is shared with the world.

Scientists of all fields have the opportunity to receive funding where they may not be eligible or unable to be funded by a University or grant program. Thus, removing barriers and enabling scientific innovation and our world to excel.

## Technologies Used
-Django Restframework
-React
-Javascript

## { Basic Features }
​
### User Accounts
This could be a scientist that creates or is apart of a project team; or simply a supporter whether it is an invividual, a company or academic institute funding projects.
​
- [X] Username
- [X] First_name
- [X] Last_name
- [X] Email Address
- [X] Password
- [x] Date_joined
- [X] Image
- [X] Bio
- [X] Qualifications
- [X] Affilate
​
### Project
​
  - [X] Create a project
  - [X] Title
  - [X] Owner (a user)- creator of project
  - [X] Description
  - [X] question_one (Stored answers to question: What is the context of this research?)
  - [X] question_two (Stored answers to question: What is the significance/innovation of this project?)
  - [X] question_three (Stored answers to question: What are the goals of the project?)
  - [X] Image
  - [X] Video
  - [X] Target Amount to Fundraise
  - [X] Open/Close (Accepting new supporters)
  - [X] When was the project created
  - [X] When project ends
  - [X] category (field of study) the project belongs to
  - [X] project email, users could email project team(data saved, function not created yet)
  - [X] innovation star- similiar to a like button where a user acknowledges the innovation factor of the project

### Pledge
  - [X] Ability to pledge to a project
  - [X] An amount
  - [X] The project the pledge is for
  - [X] The supporter
  - [X] Whether the pledge is anonymous
  - [X] A comment to go with the pledge


### Implementation of CRUD on Basic Features

​- User
  - [X] Create
  - [X] Retrieve
  - [X] Update
  - [ ] Destroy- Do not want to loose any data of user roles in projects or pledges

- Project
  - [X] Create
  - [X] Retrieve
  - [X] Update
  - [X] Destroy

- Pledge
  - [X] Create
  - [X] Retrieve
  - [X] Update
  - [X] Destroy

​
### Implement suitable permissions
​
​- User
  - [ ] Limit who can create- Anyone can create, to entice and motivate participation
  - [ ] Limit who can retrieve- Anyone can retrieve, to entice and motivate participation
  - [X] Limit who can update- only owner can update
  - [X] Limit who can delete- only owner can delete

- Project
  - [X] Limit who can create- A user has to be logged in to  create
  - [ ] Limit who can retrieve- Anyone can retrieve, to entice and motivate participation
  - [X] Limit who can update- only owner can update
  - [X] Limit who can delete- only owner can delete

- Pledge
  - [X] Limit who can create- A user has to be logged in to  create
  - [ ] Limit who can retrieve- Anyone can retrieve, to entice and motivate participation
  - [X] Limit who can update- only owner can update
  - [X] Limit who can delete- only owner can delete

​
### Implement relevant status codes
​
- [X] Get returns 200
- [X] Create returns 201
- [X] Not found returns 404
​
### Handle failed requests gracefully 
​
- [X] 404 response returns JSON rather than text
​
### Use token authentication
​
- [X] impliment /api-token-auth/
​
## Additional features
​
- [X] ProjectRoles
  The ability for a project creator to apply project roles to other users
​
 CRUD execution:
  - [X] Limit who can create- A user has to be logged in and the project owner to create
  - [ ] Limit who can retrieve- Anyone can retrieve, to entice and motivate participation
  - [X] Limit who can update- only project owner can update
  - [X] Limit who can delete- only project owner can delete
​
- [X] Options to search(filter) by:

        -Project Category
        -Project Title
        -Project Name
        -Project roles by project
​        -Project roles by user that created project roles
        (across mutiple projects; applies if user created multiple projects)

- [ ] BudgetItems (Not yet executed)
​The ability for project creators to display how their funds will be distributed within their research project. This shows transparency and supporters are aware of how their money is being used.
Ideally will be represented as a bar chart.
​
CRUD execution:
  - [X] Limit who can create- Only project owner to create
  - [ ] Limit who can retrieve- Anyone can retrieve, to entice and motivate participation
  - [X] Limit who can update- only project owner can update
  - [X] Limit who can delete- only project owner can delete


- [ ] DeadlineDates (Not yet executed)
​The ability for project creators to create a schedule which displays progression on their research project with predetermined estimated dates and deliverables associate with that date(displayed as lab notes). 
Ideally will be represented as a timeline graph.
​
CRUD execution:
  - [X] Limit who can create- Only project owner to create
  - [ ] Limit who can retrieve- Anyone can retrieve, to entice and motivate participation
  - [X] Limit who can update- only project owner can update
  - [X] Limit who can delete- only project owner can delete

- [ ] Labnotes (Not yet executed)
​The ability for project creators to share project progression notes/results at their predetermined estimated date (displayed  lab notes). Ideally will be represented as a timeline graph.
​
CRUD execution:
  - [X] Limit who can create- Only project owner to create
  - [X] Limit who can retrieve- Only supporters(pledgers) and allocated projectrole users
  - [X] Limit who can update- only project owner can update
  - [X] Limit who can delete- only project owner can delete

### External libraries used
​
- [ ] django-filter- Not used
​
​

## API Specifications

![img](api_specification.png)

## Database Schema

![img](diagram_schema.png)

## Part A Submission Checklist
​
- [X] A link to the deployed project: https://delicate-moon-7806.fly.dev
- [X] A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.
- [X] A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.
- [X] A screenshot of Insomnia, demonstrating a token being returned.
- [X] Your refined API specification and Database Schema.
​
### Step by step instructions for how to register a new user and create a new project (i.e. endpoints and body data).
​
1. Create User
​
```shell
curl --request POST \
  --url http://127.0.0.1:8000/users/ \
  --header 'Content-Type: application/json' \
  --data '{
	"username": "testuser",
	"email": "not@myemail.com",
	"password": "not-my-password",
	"first_name": "Tom",
	"last_name": "Thomason",
	"image": "https://i.postimg.cc/rm82XhCm/default-profile-image.png",
	"bio": "Interested scientist",
	"qualifications": "None",
	"affiliate": "None"
}'
```
​
2. Sign in User
​
```shell
curl --request POST \
  --url http://127.0.0.1:8000/api-token-auth/ \
  --header 'Content-Type: application/json' \
  --data '{
	"username": "testuser",
	"password": "not-my-password"
}'
```
​
3. Create Project
​
```shell
curl --request POST \
  --url http://127.0.0.1:8000/projects/ \
  --header 'Authorization: Token 5b8c82ec35c8e8cb1fac24f8eb6d480a367f322a' \
  --header 'Content-Type: application/json' \
  --data "{
		'title': 'Part 3-Investigating Benfords Law in rainfall',
		'description' : 'observing whether benfords Law can be applied to natural environment data in rainfall and run-off',
		'goal': 500,
		'image': 'https://via.placeholder.com/.jpg',
		'is_open': true,
		'category': 'Eng',
		'total_stars': null
	
	}"
```