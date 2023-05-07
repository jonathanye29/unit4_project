# ShelfShare: A Book Sharing Social Network
<img src="https://user-images.githubusercontent.com/111751273/230335373-2b5f43b8-14be-4786-aeac-73b739196a62.jpg" width="100%">

Using the prompt 'Generate a picture of a cozy reading nook with a bookshelf filled with books and a comfortable armchair in warm and inviting colors.' This image was generated using AI on Deep Dream Generator.[1]

# Criteria A: Planning

## Problem Definition
As a School X book club member, I've observed the absence of a dedicated social network for our book club community. While platforms like Goodreads enable global connections, they don't offer a focused space for our school's book club to share reviews, discussions, or announcements. Users can't edit/delete posts or comments, upload desired images, or view past liked posts. Additionally, discovering popular content is challenging due to the presence of numerous less-liked or disliked posts. As there are many different post categories, it is hard to locate specific posts. Consultations with club members (see <a href="https://github.com/jonathanye29/unit4_project#evidence-of-consultation">Evidence of Consultation</a> in Appendix) reveal a clear desire for a dedicated book club social network.

## Success Criteria
1. *[Issue tackled: “ absence of a dedicated social network for our book club community”]* The platform allows only students from School X to register using their school emails.

2. *[Issue tackled: 1. “they don't offer a focused space for our school's book club to share reviews, discussions, or event announcements" 2. "Users can't edit/delete posts or comments”]* Users should be able to post posts of different categories such as: Announcements,  Book Reviews, and Discussions, and be able to edit/delete their posts and comments

3. *[Issue tackled: "discovering popular content is challenging due to the presence of numerous less-liked or disliked posts."]* Implement a filtering or sorting mechanism that allows users to easily discover and view highly-liked or popular posts.

4. *[Issue tackled: "or even see past posts they have liked"]* Users will be able to see all posts they have liked in the past.

5. *[Issue: tackled: “As there are many different post categories, it is hard to locate specific posts.”]* The platform will allow the user to select what kind of posts they would like to view by category.

6. *[Issue tackled: “upload desired images”]* The platform will allow users to upload images in their posts.

## Design Statement
I will design and develop a website for my school’s book club. This website will be developed using HTML, Bootstrap CSS, Python, SQLite, and the Flask framework. It will take approximately 3 weeks to develop and will be evaluated based on the given criteria.


## Rationale for Proposed Solution
There are web and mobile applications; however, mobile apps can only be accessed on mobile devices. Web applications, on the other hand, are accessible on any device with a browser. Therefore,  I will be creating a web application for my school's book club to bring all the necessary features in one place and provide a space for all book club members to connect and engage with each other.

I decided to use HTML to develop the website as it is the standard markup language for creating web pages and web applications. HTML provides a foundation for building the user interface of the social network [6]. In addition, I have chosen to use Bootstrap CSS, which offers responsiveness and a mobile-first approach, catering to a variety of devices and screen sizes. This combination ensures that the platform will be compatible with various devices and browsers, allowing a wide range of users to access the application with a consistent interface [7].

Many tools exist for creating web applications, including JavaScript, Python, C++, and more. I've chosen Python for my web application due to its vast library selection [^8], enabling me to meet the book club's large-scale web app needs. I opted for Flask among Python frameworks like Flask because of its flexibility, which is crucial for specialized web apps. Unlike stricter frameworks such as Django, Flask works with numerous tools, allowing me to tailor the social network to the book club's requirements. [9]

For the website's database, I will be using SQLite. SQLite is a free database that does not require any additional server process, and is implemented on a single file. This database fits my client's needs as it is designed to handle large amounts of data efficiently [10]. It will be able to store all kinds of information safely and quickly, as it does not require to go through long procedural routines other databases such as IBM db2 use [11]. SQLite is the best option for the social network as it is reliable, efficient, and cost-friendly.

_Word Count_: **491**


# Criteria B: Design
## System Diagram
![jojojojojojo (2)](https://user-images.githubusercontent.com/111751273/236675657-0ace4df1-aedc-4d44-9181-fc2a45cd81cd.png)

<i>Fig. 2</i> This is the system diagram for the proposed solution

## Flow Diagram
### Login System
![u4flowchart1 (1)](https://user-images.githubusercontent.com/111751273/236664876-93241420-14ad-49cd-94b9-b869e724d9db.png)
<i>Fig. 3</i> This is the flow diagram that details the process of how the login system works.

This method handles user login by checking the entered email and password, verifying the password against the stored password in the database, and creating a JWT token upon successful authentication to maintain the user's session. If the login fails, it displays error messages.

### Create Post
![u4flowchart2 (1)](https://user-images.githubusercontent.com/111751273/236667550-dc0668e5-b174-4688-9e57-77e6a044b79c.png)
<i>Fig. 4</i> This is the flow diagram that details the process of how the posts are created.

This method handles the creation of a new post. It first checks for an image in the request, safely saving it if present. Then, it extracts post details from the form, inserts the post into the database, and redirects the user to the homepage.

### Like Post
![u4flowchart3](https://user-images.githubusercontent.com/111751273/236672192-9402434f-47ba-456e-90f6-de9736a568d0.png)
<i>Fig. 5</i> This is the flow diagram that details the process of how users are able to like and unlike posts

This method handles the process of liking or unliking a post. It first decodes the user's token to get their user ID. Then, it checks if a like record exists in the database for the given user and post. If the record exists, it deletes the like (unlike). If not, it creates a new like record. Finally, it redirects the user back to the post.

## UML Diagram
![u4UML](https://user-images.githubusercontent.com/111751273/236673274-82e87354-2d09-423a-a62d-0baaf5b2ff90.png)

<i>Fig. 6</i> This is the UML diagram for the social network.

The class shown in the UML Diagram is responsible for handling database interactions, such as executing queries, saving changes, and closing the connection.

## ER Diagram
![u4projectERdiagram (1)](https://user-images.githubusercontent.com/111751273/236689127-eb15d37f-0739-4bec-8e81-60c3b56a149f.png)
<i>Fig. 7</i> Entity-Relationship (ER) diagram for ShelfShare's network database, illustrating the relationships between the Users, Posts, Likes, and Comments tables. The diagram displays one-to-many relationships using lines starting with '1' and ending with 'N', indicating the cardinality of each relationship. For example, 1 user can have many (n) posts.

![Screen Shot 2023-05-06 at 8 33 21 PM](https://user-images.githubusercontent.com/111751273/236621562-8dc78e4f-7ff3-4a0b-bd85-2984853d328b.png)
<p align="center">
  <i>Fig. 8</i> Example Data for Users Table (Disclaimer: The data presented is fictional and does not depict real comments or authors)
</p>

<img width="max" alt="Screen Shot 2023-04-07 at 9 28 29 PM" src="https://user-images.githubusercontent.com/111751273/230608878-771dffd3-547a-4f55-9873-fd01c84caaae.png">
<p align="center">
  <i>Fig. 9</i> Example Data for Posts Table (Disclaimer: The data presented is fictional and does not depict real comments or authors)
</p>

<img width="max" alt="Screen Shot 2023-04-07 at 9 29 29 PM" src="https://user-images.githubusercontent.com/111751273/230608970-0458ea2a-c1e5-49e7-91f8-b46e0da26267.png">
<p align="center">
  <i>Fig. 10</i> Example Data for Reviews Table (Disclaimer: The data presented is fictional and does not depict real comments or authors) 
</p>
 
<img width="max" alt="Screen Shot 2023-05-08 at 1 04 41 AM" src="https://user-images.githubusercontent.com/111751273/236688904-e654f3bd-06fb-4c63-b821-47c07c4b5fb7.png">
<p align="center">
  <i>Fig. 11</i> Example Data for Comments Table (Disclaimer: The data presented is fictional and does not depict real comments or authors)
</p>


## Wireframe
<img width="651" alt="Screen Shot 2023-05-05 at 9 05 47 PM" src="https://user-images.githubusercontent.com/111751273/236453336-e5980aca-6663-4f40-ba87-066a4ca50ca5.png">
<i>Fig. 12</i> The wireframe diagram displays the layout and structure of the Shelfshare social network application, including the login and registration pages, the homepage, pages for each category, the create post page, and the profile page. Users can navigate between these pages using buttons and links provided on each page. The purpose of the wireframe is to provide a visual representation of the user interface design and the flow of the application.

## Test plan
| Description | Test Type|  Input | Expected Output |
|-----------|--------|-------|------------------|
|	Test for Registration System	|	Unit Test	|	"1.Open Website 2.Click on the register button 3. Enter "John Doe" for the full name. Enter "johndoe@schoolx.edu" for the email address. Select "United States" for the country. Enter "johndoe123" for the username. Enter "johndoelovestoski" for the password and confirm password. 4. Click the register button on the page.	|	After clicking the register button, it should redirect to the login page with a message on the screen saying, "Registration completed. Please log in."  Fulfilling the clients need of registering with "@schoolx.edu" email addresses 
|	Test for Error Scenario for Registration System	|	Unit Test	|	1.Open Website 2.Click on the register button 3. Enter "John Doe/" for the full name. Enter "johndoe@gmail.com" for the email address. Select nothing for the country. Enter nothing for the username. Enter "john123" for the password and confirm password. 4. Click the register button on the page.	|	After clicking the register button, the page should refresh, with a red error messages appearing at the top of the screen detailing the errors saying: "Incorrect characters for the users Full Name", "Invalid email as it is not a '@schoolx.edu' email", "Missing country selection", and "Password too short, min. 8 characters". This outcome demonstrates that the application effectively validates user input during registration, ensuring data integrity.
|	Test for Users Database	|	Integration Test	|	1. Open Website 2. Click on the register button 3. Enter "Jane Smith" for the full name. Enter "janesmith@schoolx.edu" for the email address. Select "United States" for the country. Enter "janesmith123" for the username. Enter "janesmithlovesskating" for the password and confirm password. 4. Click the register button on the page.	|	After successfully registering, the new user's information should be stored into the "shelfshare.db" database, specifically in the "users" table. Each time a user registers, their information should be added to the "users" table, ensuring the system effectively manages user data and integrates the registration process with the database operations.
|	Test for Login System	|	Unit Test	|	1. Open Website 2. Click on the login button 3. Enter a valid email and password for an existing user (e.g., "johndoe@schoolx.edu" and "johndoelovestoski") 4. Click the login button on the page.	|	After clicking the submit button, the page should redirect to the homepage of the website
|	Test for error scenario for Login System	|	Unit Test	|	1. Open Website 2. Click on the login button 3. Enter an invalid email (e.g., "johndoe@gmail.com") and/or an incorrect password (e.g., "wrongpassword") 4. Click the login button on the page	|	After clicking the login button, the page should refresh, displaying a red error message at the top of the screen, indicating that the login attempt has failed due to incorrect email and/or password. This test ensures that the application effectively validates user input during login and prevents unauthorized access with incorrect credentials.
|	Test for Creating Posts	|	Unit Test	|	1.Open Website 2.Login 3.Click Create Post on the navigation bar 4.Enter in "My First Post!" as the title, select "Announcement" as the category, enter "This is my first ever post." as the content. 5.Click the submit button	|	After clicking the submit button, the page should redirect to the homepage of the website, displaying the new post with its Title, Category, Content, Author, and Post Date. Fulfilling the clients need of being able to create posts with categories
|	Test for Error Scenario for Creating Posts	|	Unit Test	|	1.Open Website 2.Login 3.Click Create Post on the navigation bar 4.Enter in only the title "My Second Post!" and leave the category and content fields empty 5.Click the submit button	|	After clicking the submit button, the user should see a specific error message indicating that the required fields (category and content) are not filled in. The post should not be created or displayed on the homepage. This test ensures that the application properly handles invalid input, enforces mandatory field requirements, and prevents incomplete posts from being created.
|	Test for Posts Database	|	Integration Test	|	1. Open Website 2. Login 3. Click Create Post on the navigation bar 4. Enter "My Post!" as the title, select "Announcement" as the category, enter "This is my post." as the content. 5. Click the submit button 	|	After clicking the submit button, the new post's information should be stored into the "shelfshare.db" database, specifically in the "posts" table. Each time a user creates a post, all post information should be added to the "posts" table, ensuring the system effectively manages post data and integrates the post creation process with the database operations.
|	Test for Editing Posts|Unit Test|1.Open Website 2.Login 3.Navigate to a post created by the logged-in user 4. Click the 'Edit' button below the post 5. Modify the post's title to 'My Edited Post!', change the category to 'Event', and update the content to 'This post has been edited.' 6. Click the 'Save Changes' button|After clicking the 'Save Changes' button, the page should refresh and display the updated post with its new Title, Category, and Content. This confirms that the application allows users to edit their own posts successfully, providing a way to correct or update information as needed.
|	Test for Edited Posts Database	|	Integration Test	|	1. Open Website 2. Login 3. Navigate to a post created by the logged-in user 4. Click the 'Edit' button below the post 5. Modify the post's title to 'My Edited Post Again!', change the category to 'Reminder', and update the content to 'This post has been edited again.' 6. Click the 'Save Changes' button	|	After clicking the 'Save Changes' button and refreshing the page, the updated post should be reflected in the "posts" table of the "shelfshare.db" database, confirming that the application correctly stores edited post data in the database. This ensures that the changes made by users are successfully saved and persist across sessions.
|	Test for Creating Comments	|Unit Test	|	1. Open Website 2. Login 3. Navigate to a post 4. Enter "This is my comment!" in the comment text box below the post 5. Click the 'Submit' button	|	After clicking the 'Submit' button, the page should refresh, and the new comment should be displayed below the post, including the commenter's name and the comment timestamp. This fulfills the client's need for users to be able to add comments to posts.
|	Test for Error Scenario for Creating Comments	|	Unit Test	|	1. Open Website 2. Login 3. Navigate to a post 4. Leave the comment text box empty 5. Click the 'Submit' button 	|	After clicking the 'Submit' button, an error message should appear, stating that the comment cannot be empty. The comment should not be created or displayed below the post. 
|	Test for Commenting Database	|	Integration Test	|	1. Open Website 2. Login 3. Navigate to a post 4. Enter "This is another comment!" in the comment text box below the post 5. Click the 'Submit' button	|	After clicking the 'Submit' button and refreshing the page, the new comment should be stored in the "comments" table of the "shelfshare.db" database, confirming that the application correctly stores comment data in the database. This ensures that user comments persist across sessions and are retrievable for future reference.
|	Test for Liking Posts	|	Unit Test	|	1. Open Website 2. Login 3. Navigate to a post 4. Click the 'Like' button below the post	|	After clicking the 'Like' button, the page should refresh, and the like button should now read "unlike", and the number of likes should increase by 1. This fulfills the client's need for users to be able to like posts, helps to identify popular content, and allows users to easily find and revisit posts they have liked in the past.
|	Test for Error Scenario for Liking Posts	|	Unit Test	|	1. Open Website 2. Login 3. Navigate to a post 4. Click the 'Like' button twice	|	After clicking the 'Like' button twice, the button should still show "like", as the post was liked then unliked, and the number of likes should still only increase by 1. This test ensures that the application properly handles multiple clicks on the 'Like' button and prevents users from liking a post multiple times.
|	Test for Liking Posts Database 	|	Integration Test	|	1. Open Website 2. Login 3. Navigate to a post 4. Click the 'Like' button for the post	|	After clicking the 'Like' button, a record should be stored in the "likes" table of the "shelfshare.db" database, reflecting the user's like of the post. This ensures that user likes are correctly stored in the database.
|	Test for Category Filtering	|	Unit Test	|	1.Open Website 2.Login 3.Click on the desired category (e.g., "Announcements") in the navigation bar	|After clicking on the desired category in the navigation bar, the page should display only the posts that belong to the selected category (e.g., "Announcements"), making it easier for users to locate specific posts by filtering them by category. This fulfills the clients needs for allowing users to select and view posts based on categories, addressing the issue of locating specific posts among many different post categories.
|	Test for Image Uploading	|	Unit Test	|	1.Open Website 2.Login 3.Click Create Post on the navigation bar 4.Enter "This Post has an Image!" as the Title, select "Announcement" for the category, and enter "This post includes this image." for the content 5.Select an image file to upload 6.Click the submit button 	|	After clicking the submit button, the page should redirect to the homepage, displaying the new post with its Title, Category, Content, Author, Post Date, and the uploaded image. This fulfills the success criteria of allowing users to upload images in their posts, addressing the issue of uploading desired images.
|	Test for Image Uploading in Posts Database	|	Integration Test	|	Enter "Image!" as the Title, select "Announcement" for the category, and enter "This post includes this image." for the content 5.Select an image file to upload 6.Click the submit button  7.Check the 'posts' table in the "shelfshare.db" database	|	After creating the post with an image, the new post should be stored in the 'posts' table in the "shelfshare.db" database, including the image file name. This test verifies that the application properly stores posts with uploaded images in the database, ensuring that the uploaded images are associated with the correct posts and can be displayed when viewing the post.
|	Code Review	|	Reviewing Code	|	Review the entire codebase, identifying and removing any unused code or debugging and testing artifacts, and adding comments to detail parts of code.	|	Revised version of the code that follows good coding practices, with improved readability and organization

## Record of Tasks
|Task No	|	Planned Action	|	Planned Outcome	|	Time estimate	|	Target completion date	|	Criterion 
----------|-----------------|-----------------|---------------|--------------------------|----------
1	|	"Brainstorm and write the problem definition	"	|	A clear description of the problem currently being faced.	|	15 mins.	|	05/04/2023	|	A
2	|	"Brainstorm and write the design statement	"	|	A clear design statement that details the plan and tools that will be used to resolve the problem being faced.	|	10 mins.	|	05/04/2023	|	A
3	|	Rationale for Proposed Solution	|	A clear justification that suits the client and developer.	|	20 mins.	|	10/04/2023	|	A
4	|	"Brainstorm and write down success criterias	"	|	A clear success criteria that suits the client and resolves the problem	|	20 mins.	|	10/04/2023	|	A
5	|	Create system diagram        	|	To have a clear idea of the hardware and software requirements for the proposed solution	|	45 minutes	|	13/04/2023	|	B
6	|	Draw a wire frame and write an explanation of it	|	Have a clear wire frame that accurately represents and describes the application and have a brief explanation	|	30 mins.	|	13/04/2023	|	B
7	|	Create flow diagrams and write brief explanations for each  	|	Have accurate flow diagrams for different parts of the program with brief explanations	|	1 hour	|	14/04/2023	|	B
8	|	Draw an ER diagram and write a breif explanation of it|	A clear and organized visual representation of the data structure for the ShelfShare network with a brief explanation	|	45 minutes        	|	14/04/2023	|	B
9	|	Create UML Diagram and write a brief description 	|	Have a clear UML Diagram that accurately shows the different classes and methods used with a brief explanation	|	30 minutes	|	15/04/2023	|	B
10	|	Write the test plans	|	Procedures that should be taken to test the program and the expected outcome of each test is recorded	|	1 hour	|	17/04/2023	|	B
11	|	Follow up meeting with client	|	Present success criterias and development plan to client and get the approval	|	20 minutes	|	17/04/2023	|	A
12	|	Code a login and registration system	|	Create a program that allows the user to register and login to the application using a username and password they set up	|	1 hour	|	17/04/2023	|	C
13	|	Code password encryption	|	Using 'sha256' to encrypt password and check password in login and registration	|	45 minutes	|	17/04/2023	|	C
14	|	Code a password policy	|	Have a policy where when the user creates an account, their password must have a minimum of 8 characters	|	15 minutes	|	17/04/2023	|	C
15	|	Create table for users in database	|	To have a table inside the database that includes all registered users' information (full name, email address, country, username, encrypted password)	|	5 minutes	|	17/04/2023	|	C
16	|	Create table for posts in database	|	To have a table inside the database that includes all posted posts and the content that it contains (Title, Category, Content, Author, Datetime)	|	5 minutes	|	17/04/2023	|	C
17	|	Create table for comments in database	|	To have a table inside the database that includes all posted comments and the content that it contains (Content, Author, Datetime)	|	5 minutes	|	17/04/2023	|	C
18	|	Create table for likes in database	|	To have a table inside the database that includes all likes from users and the liked post	|	5 minutes	|	17/04/2023	|	C
19	|	Code the login page	|	Have a working page for login on the website	|	20 minutes	|	17/04/2023	|	C
20	|	Code the registration page	|	Have a working page for registration on the website	|	20 minutes	|	17/04/2023	|	C
21	|	Code the base HTML template	|	Have a base.html template that will be used to extend to all other templates to complete the web application	|	10 minutes	|	17/04/2023	|	C
22	|	Code the homepage of the web application	|	Have the layout of the homepage completed and on the website	|	20 minutes	|	18/04/2023	|	C
23	|	Code the page for each post category (Announcements, Reminders, Book Recommendatrions, Book Reviews, Discussions, Reminders)	|	Have the layout for each category page completed and shown on the website 	|	30 minutes	|	18/04/2023	|	C
24	|	Code the button and route functionality for the homepage	|	Each element shown on the homepage redirects to the assigned page (eg. Announcement button goes to Announcement Page)	|	20 minutes	|	18/04/2023	|	C
25	|	Implement token-based authentication	|	Develop a secure token-based authentication system using JWT for protecting login required routes	|	2 hours	|	19/04/2023	|	C
26	|	Code the create_post page	|	Have a page that shows the layout of creating a post	|	15 minutes	|	19/04/2023	|	C
27	|	Code profile page	|	Have a page that shows the current users profile with their information (Name, Username, Email, Country, all their posts, comments and liked posts )	|	45 minutes	|	19/04/2023	|	C
28	|	Code create post functionality	|	Have the create post page work with the code to allow the user to create a post and save it to the database	|	20 minutes	|	20/04/2023	|	C
29	|	Code to display posts on all pages	|	Develop functionality to display all posts on the homepage and show specific category posts on their respective category pages	|	45 minutes	|	20/04/2023	|	C
30	|	Code the edit post function	|	Have a functional program that allows the user to edit their own posts which updates to the database	|	30 minutes	|	20/04/2023	|	C
31	|	Code comment feature	|	Have a program that allows the user to post comments on their own and others posts	|	45 minutes	|	21/04/2023	|	C
32	|	Code the edit comment feature	|	Have a functional program that allows the user to edit their own comments which updates to the database	|	20 minutes	|	21/04/2023	|	C
33	|	Code the delete function	|	Have a functional program that allows users to delete their own account, posts and comments	|	15 minutes	|	21/04/2023	|	C
34	|	Code the logout system	|	Have a functional program that allows users to log out of their accounts	|	10 minutes	|	21/04/2023	|	C
35	|	Code the upload image function	|	Have a functional program that allows the users to upload desired images in their posts	|	1 hour	|	25/04/2023	|	C
36	|	Third meeting with client	|	Showing the application to the client and to ask for their opinion on the applications current progress	|	15 minutes	|	25/04/2023	|	A
37	|	Code the country flag displayment	|	Have a functional program that shows the users country flag in their profile	|	1 hour 15 minutes	|	25/04/2023	|	C
38	|	Code the like post function	|	Have a functional program that allows the users to like and unlike posts	|	25 minutes	|	26/04/2023	|	C
39	|	Code the popular posts filter function	|	Have a functional program that filters posts by the amount of likes they have (most liked to least liked, vice versa)	|	1 hour	|	26/04/2023	|	C
40	|	Code the tab icon for web application	|	Have a functional program that displays the social networks logo on the tab of the web application	|	30 minutes	|	26/04/2023	|	C
41	|	Cleaning up the Code	|	Going back and reviewing the code to correctly format and remove unused code 	|	1 hour 30 minutes	|	27/04/2023	|	C

# Criteria C: Development

## Existing tools
|Libraries|
|---------|
| Flask 
| Werkzeug.utils 
| Functools
| JWT
| Dotenv 
| os
| Pycountry
| Datetime
| SQLite3
| Passlib

## List of techniques used
- Flask Library/Routes
- Python inside HTML
- CSS Styling
- Object-Oriented Programming(OOP)
- For loops
- If statements
- Variables
- Functions
- Lists
- Token-based authentication

## Development

### Success Criteria 1: The platform allows only students from School X to register using their school emails.
```.py
if '@schoolx.edu' not in email:
    flash(("Invalid email address, not a 'School X email.", 'danger'))
    print("Invalid email address, not a 'School X email.")
```
My client wanted to create a social network platform exclusively for members of School X's book club. To achieve this, I needed to ensure that only students from School X could register using their school email addresses. To solve this problem, I used a basic yet effective 'if' statement in Python to verify if the user is attempting to register with a School X email address or not as shown in the code snippet above. Further, when a user tries to register with an email thats not from School X, I made an error pop up message to remind the user that they need to register with a School X email.

### 



# Criteria D: Functionality


# Works cited
1. “Trending Dreams | Deep Dream Generator.” Deepdreamgenerator.com, 2023, deepdreamgenerator.com/. Accessed 2 Apr. 2023.
2. Grinberg, Miguel. “The Flask Mega-Tutorial Part I: Hello, World!” Miguelgrinberg.com, 2017, blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world. Accessed 3 Apr. 2023.
3. “HTML Tutorial.” W3schools.com, 2023, www.w3schools.com/html/default.asp. Accessed 3 Apr. 2023.
4. Sanyal, Sayantani. 10 Reasons Why Python Is One Of The Best Programming Languages. Accessed 7 Apr. 2023
5. “Flask.” Fullstackpython.com, 2016, www.fullstackpython.com/flask.html. Accessed 7 Apr. 2023.
6. “Advantages and Disadvantages of HTML.” GeeksforGeeks, GeeksforGeeks, 25 Oct. 2020, www.geeksforgeeks.org/advantages-and-disadvanatges-of-html/. Accessed 10 April 2023.
7. Cyber Success. “What Is Bootstrap & Advantages of Bootstrap in Web Development.” Cyber Success, 24 Oct. 2021, www.cybersuccess.biz/advantages-of-bootstrap/. Accessed 10 April 2023.
8. Advantages and disadvantages of python - how it is dominating Programming World. DataFlair. Accessed April 10, 2023
9. Simplilearn. “Django vs. Flask: Understanding the Major Differences.” Simplilearn.com, Simplilearn, 4 Feb. 2021, www.simplilearn.com/flask-vs-django-article#:~:text=Flask%20provides%20complete%20control%20and,best%20for%20developing%20sophisticated%20applications. Accessed 10 April 2023.
10. Gomathy, Kavya. "5 Reasons to Use SQLite, the Tiny Giant for Your Next Project." Medium, The Startup, 4 Jan. 2022, https://medium.com/swlh/5-reasons-to-use-sqlite-the-tiny-giant-for-your-next-project-a6bc384b2df4. Accessed April 10, 2023
11. Yegulalp, Serdar. "Why You Should Use SQLite." InfoWorld, IDG Communications, Inc., 13 Feb. 2019, https://www.infoworld.com/article/3331923/why-you-should-use-sqlite.html. Accessed April 10, 2023
12. Otto, Mark. “Get Started with Bootstrap.” Getbootstrap.com, 2023, getbootstrap.com/docs/5.3/getting-started/introduction/. Accessed 26 Apr. 2023.
13.lipis. “Lipis/Flag-Icons: A Curated Collection of All Country Flags in SVG — plus the CSS for Easier Integration.” GitHub, 28 Mar. 2023, github.com/lipis/flag-icons. Accessed 23 Apr. 2023.

‌


# Appendix

## Evidence of Consultation
![Screen Shot 2023-05-06 at 8 46 37 PM](https://user-images.githubusercontent.com/111751273/236622106-71c778b6-838a-4e12-ac89-4bdc96d31c0d.png)
<i>Fig. </i> (Messenger names kept confidential for privacy purposes)


