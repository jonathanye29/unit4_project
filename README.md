# ShelfShare: A Book Sharing Social Network
<img src="https://user-images.githubusercontent.com/111751273/230335373-2b5f43b8-14be-4786-aeac-73b739196a62.jpg" width="100%">

Using the prompt 'Generate a picture of a cozy reading nook with a bookshelf filled with books and a comfortable armchair in warm and inviting colors.' This image was generated using AI on Deep Dream Generator.[1]

# Criteria A: Planning

## Problem Definition
As a School X book club member, I've observed the absence of a dedicated social network for our book club community. While platforms like Goodreads enable global connections, they don't offer a focused space for our school's book club to share reviews, discussions, or announcements. Users can't edit/delete posts or comments, upload desired images, or view past liked posts. Additionally, discovering popular content is challenging due to the presence of numerous less-liked or disliked posts. As there are many different post categories, it is hard to locate specific posts. Consultations with club members (see Fig A. 1 in <a href="https://github.com/jonathanye29/unit4_project#evidence-of-consultation">Evidence of Consultation</a> in Appendix) reveal a clear desire for a dedicated book club social network.

## Success Criteria
1. *[Issue tackled: “ absence of a dedicated social network for our book club community”]* The platform allows only students from School X to register using their school emails.

2. *[Issue tackled: 1. “they don't offer a focused space for our school's book club to share reviews, discussions, or event announcements" 2. "Users can't edit/delete posts or comments”]* Users should be able to post posts of different categories such as: Announcements,  Book Reviews, and Discussions, and be able to edit/delete their posts and comments

3. *[Issue tackled: “upload desired images”]* The platform will allow users to upload images in their posts.

4. *[Issue tackled: "or even see past posts they have liked"]* Users will be able to see all posts they have liked in the past.

5. *[Issue: tackled: “As there are many different post categories, it is hard to locate specific posts.”]* The platform will allow the user to select what kind of posts they would like to view by category.

6. *[Issue tackled: "discovering popular content is challenging due to the presence of numerous less-liked or disliked posts."]* Implement a sorting feature that allows users to view the top liked posts.

## Design Statement
I will design and develop a website for my school’s book club. This website will be developed using HTML, Bootstrap CSS, Python, SQLite, and the Flask framework. It will take approximately 3 weeks to develop and will be evaluated based on the given criteria.


## Rationale for Proposed Solution
There are web and mobile applications; however, mobile apps can only be accessed on mobile devices. Web applications, on the other hand, are accessible on any device with a browser. Therefore,  I will be creating a web application for my school's book club to bring all the necessary features in one place and provide a space for all book club members to connect and engage with each other.

I decided to use HTML to develop the website as it is the standard markup language for creating web pages and web applications. HTML provides a foundation for building the user interface of the social network [6]. In addition, I have chosen to use Bootstrap CSS, which offers responsiveness and a mobile-first approach, catering to a variety of devices and screen sizes. This combination ensures that the platform will be compatible with various devices and browsers, allowing a wide range of users to access the application with a consistent interface [7].

Many tools exist for creating web applications, including JavaScript, Python, C++, and more. I've chosen Python for my web application due to its vast library selection [8], enabling me to meet the book club's large-scale web app needs. I opted for Flask among Python frameworks like Flask because of its flexibility, which is crucial for specialized web apps. Unlike stricter frameworks such as Django, Flask works with numerous tools, allowing me to tailor the social network to the book club's requirements. [9]

For the website's database, I will be using SQLite. SQLite is a free database that does not require any additional server process, and is implemented on a single file. This database fits my client's needs as it is designed to handle large amounts of data efficiently [10]. It will be able to store all kinds of information safely and quickly, as it does not require to go through long procedural routines other databases such as IBM db2 use [11]. SQLite is the best option for the social network as it is reliable, efficient, and cost-friendly.

_Word Count_: **491**


# Criteria B: Design
## System Diagram
![jojojojojojo (3)](https://user-images.githubusercontent.com/111751273/237041440-084968a9-940f-4fd9-b906-93f07463106a.png)

<i>Fig. 2</i> This is the system diagram for the proposed solution

It serves as a visual representation of the system and its components, and their relationships to each other. As shown above, the web application will be programmed in python, and all information will be stored in the SQLite database. The application will have various inputs from the user, which will then output onto their screen.

## Flow Diagram

### Create Post
![u4flowchart2 (3)](https://user-images.githubusercontent.com/111751273/237036522-44151e72-d793-4eea-9b59-f0cc0ffde5c9.png)

<i>Fig. 3</i> This is the flow diagram that details the process of how the posts are created.

This function handles the creation of a new post. It first checks for an image in the request, safely saving it if present. Then, it extracts post details from the form, inserts the post into the database, and redirects the user to the homepage.

### Like Post
![u4flowchart3](https://user-images.githubusercontent.com/111751273/236672192-9402434f-47ba-456e-90f6-de9736a568d0.png)
<i>Fig. 4</i> This is the flow diagram that details the process of how users are able to like and unlike posts

This function handles the process of liking or unliking a post. It first decodes the user's token to get their user ID. Then, it checks if a like record exists in the database for the given user and post. If the record exists, it deletes the like (unlike). If not, it creates a new like record. Finally, it redirects the user back to the post.

### Comment Post Date Feature
![u4flowchart2](https://user-images.githubusercontent.com/111751273/237029431-8b35138c-460b-4e30-9d4f-3e6d1c18863a.png)
<i>Fig. 5</i> This is the flow diagram that details the process of how the web application displays how much time ago users posted their comments. This was a feature that my client wants as an addition to the users being able to post comments. 

The function basically finds the largest time unit (from a predefined list) that can be used to express a given time difference, and then formats this information as a string. The time units could be anything like seconds, minutes, hours, etc., and they are processed in the order they are found in the `time_units` list.

## UML Diagram
![u4UML (1)](https://user-images.githubusercontent.com/111751273/236996435-2f067243-d3c8-4321-bc14-9fcc704b8220.png)

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
|	Test for Image Uploading in Posts Database	|	Integration Test	|	1. Enter "Image!" as the Title, select "Announcement" for the category, and enter "This post includes this image." for the content 5.Select an image file to upload 6.Click the submit button  7.Check the 'posts' table in the "shelfshare.db" database	|	After creating the post with an image, the new post should be stored in the 'posts' table in the "shelfshare.db" database, including the image file name. This test verifies that the application properly stores posts with uploaded images in the database, ensuring that the uploaded images are associated with the correct posts and can be displayed when viewing the post.
|	Code Review	|	Reviewing Code	|	Review the entire codebase, identifying and removing any unused code or debugging and testing artifacts, and adding comments to detail parts of code.	|	Revised version of the code that follows good coding practices, with improved readability and organization

## Record of Tasks
|Task No	|	Planned Action	|	Planned Outcome	|	Time estimate	|	Target completion date	|	Criterion 
----------|------------|---------------|---------------|----------------|----------
1	|	Planning: Brainstorm and write the problem definition |	A clear description of the problem currently being faced.	|	15 mins.	|	05/04/2023	|	A
2	|Planning: Brainstorm and write the design statement	|	A clear design statement that details the plan and tools that will be used to resolve the problem being faced.	|	10 mins.	|	05/04/2023	|	A
3	|	Planning: Rationale for Proposed Solution	|	A clear justification that suits the client and developer.	|	20 mins.	|	10/04/2023	|	A
4	|	Planning: Brainstorm and write down success criteria		|	A clear success criteria that suits the client and resolves the problem	|	20 mins.	|	10/04/2023	|	A
5	|	Design: Create system diagram  	|	Have a clear idea of the hardware and software requirements for the proposed solution	|	45 minutes	|	13/04/2023	|	B
6	|	Design: Draw a wire frame and write an explanation of it	|	Have a clear wire frame that accurately represents and describes the application and have a brief explanation	|	30 mins.	|	13/04/2023	|	B
7	|	Design: Create flow diagrams and write brief explanations for each  	|	Have accurate flow diagrams for different parts of the program with brief explanations	|	1 hour	|	14/04/2023	|	B
8	|	Design: Draw an ER diagram and write a breif explanation of it|	A clear and organized visual representation of the data structure for the ShelfShare network with a brief explanation	|	45 minutes        	|	14/04/2023	|	B
9	|	Design: Create UML Diagram and write a brief description 	|	Have a clear UML Diagram that accurately shows the different classes and methods used with a brief explanation	|	30 minutes	|	15/04/2023	|	B
10	|	Design: Write the test plans	|	Procedures that should be taken to test the program and the expected outcome of each test is recorded	|	1 hour	|	17/04/2023	|	B
11	|	Planning: Follow up meeting with client	|	Present success criteria and development plan to client and get the approval (see Fig A. 2 in <a href="https://github.com/jonathanye29/unit4_project#evidence-of-consultation">Evidence of Consultation</a> in Appendix)|	20 minutes	|	17/04/2023	|	A
12	|	Development: Code a login and registration system	|	Create a program that allows the user to register and login to the application using a username and password they set up	|	1 hour	|	17/04/2023	|	C
13	|	Development: Code password encryption	|	Using 'sha256' to encrypt password and check password in login and registration	|	45 minutes	|	17/04/2023	|	C
14	|	Development: Code a password policy	|	Have a policy where when the user creates an account, their password must have a minimum of 8 characters	|	15 minutes	|	17/04/2023	|	C
15	|	Development: Create table for users in database	|	Have a table inside the database that includes all registered users' information (full name, email address, country, username, encrypted password)	|	5 minutes	|	17/04/2023	|	C
16	|	Development: Create table for posts in database	|	Have a table inside the database that includes all posted posts and the content that it contains (Title, Category, Content, Author, Datetime)	|	5 minutes	|	17/04/2023	|	C
17	|	Development: Create table for comments in database	|	Have a table inside the database that includes all posted comments and the content that it contains (Content, Author, Datetime)	|	5 minutes	|	17/04/2023	|	C
18	|	Development: Create table for likes in database	|	Have a table inside the database that includes all likes from users and the liked post	|	5 minutes	|	17/04/2023	|	C
19	|	Development: Code the login page	|	Have a working page for login on the website	|	20 minutes	|	17/04/2023	|	C
20	|	Development: Code the registration page	|	Have a working page for registration on the website	|	20 minutes	|	17/04/2023	|	C
21	|	Development: Code the base HTML template	|	Have a base.html template that will be used to extend to all other templates to complete the web application	|	10 minutes	|	17/04/2023	|	C
22	|	Development: Code the homepage of the web application	|	Have the layout of the homepage completed and on the website	|	20 minutes	|	18/04/2023	|	C
23	|	Development: Code the page for each post category (Announcements, Reminders, Book Recommendatrions, Book Reviews, Discussions, Reminders)	|	Have the layout for each category page completed and shown on the website 	|	30 minutes	|	18/04/2023	|	C
24	|	Development: Code the button and route functionality for the homepage	|	Each element shown on the homepage redirects to the assigned page (eg. Announcement button goes to Announcement Page)	|	20 minutes	|	18/04/2023	|	C
25	|	Development: Implement token-based authentication	|	Develop a secure token-based authentication system using JWT for protecting login required routes	|	2 hours	|	19/04/2023	|	C
26	|	Development: Code the create_post page	|	Have a page that shows the layout of creating a post	|	15 minutes	|	19/04/2023	|	C
27	|	Development: Code profile page	|	Have a page that shows the current users profile with their information (Name, Username, Email, Country, all their posts, comments and liked posts )	|	45 minutes	|	19/04/2023	|	C
28	|	Development: Code create post functionality	|	Have the create post page work with the code to allow the user to create a post and save it to the database	|	20 minutes	|	20/04/2023	|	C
29	|	Development: Code to display posts on all pages	|	Develop functionality to display all posts on the homepage and show specific category posts on their respective category pages	|	45 minutes	|	20/04/2023	|	C
30	|	Development: Code the edit post function	|	Have a functional program that allows the user to edit their own posts which updates to the database	|	30 minutes	|	20/04/2023	|	C
31	|	Development: Code comment feature	|	Have a program that allows the user to post comments on their own and others posts	|	45 minutes	|	21/04/2023	|	C
32	|	Development: Code the edit comment feature	|	Have a functional program that allows the user to edit their own comments which updates to the database	|	20 minutes	|	21/04/2023	|	C
33	|	Development: Code the delete function	|	Have a functional program that allows users to delete their own account, posts and comments	|	15 minutes	|	21/04/2023	|	C
34	|	Development: Code the logout system	|	Have a functional program that allows users to log out of their accounts	|	10 minutes	|	21/04/2023	|	C
35	|	Development: Code the upload image function	|	Have a functional program that allows the users to upload desired images in their posts	|	1 hour	|	25/04/2023	|	C
36	|	Planning: Third meeting with client	|	Show the application to the client and to ask for their opinion on the applications current progress	|	15 minutes	|	25/04/2023	|	A
37	|	Development: Code the country flag displayment	|	Have a functional program that shows the users country flag in their profile	|	1 hour 15 minutes	|	25/04/2023	|	C
38	|	Development: Code the like post function	|	Have a functional program that allows the users to like and unlike posts	|	25 minutes	|	26/04/2023	|	C
39	|	Development: Code the popular posts filter function	|	Have a functional program that filters posts by the amount of likes they have (most liked to least liked, vice versa)	|	1 hour	|	26/04/2023	|	C
40	|	Development: Code the tab icon for web application	|	Have a functional program that displays the social networks logo on the tab of the web application	|	30 minutes	|	26/04/2023	|	C
41	|	Development: Cleaning up the Code	|	Review the code to correctly format and remove unused code 	|	1 hour 30 minutes	|	27/04/2023	|	C
42 | Implementation: Get Client Evaluation on the Web Application | Have the website evaluated by the client and the subsequent evidence documented | 1 hour | 06/05/2023 | E 
43 | Beta Testing: Get Peer Evaluation on the Web Application | Have the website evaluated by a peer and the subsequent evidence documented | 1 hour | 07/05/2023 | E
44 | Implementation: Evaluate the recommendations given from both the client and peer | Take in and review the recommendations from both evaluations on how the website can be improved and document them properly | 20 minutes | 07/05/2023 | E 


# Criteria C: Development

## List of techniques used
- Flask Library/Routes
- Python/Javascript inside HTML
- CSS Styling
- Object-Oriented Programming(OOP)
- For loops
- If statements
- Variables
- Functions
- Lists
- Token-based authentication
- DRY Coding Technique
- Document Object Model (DOM)

## Development

### Email Policy (Success Criteria: 1)
```.py
if '@schoolx.edu' not in email:
    flash(("Invalid email address, not a 'School X email.", 'danger'))
```
My client wanted to create a social network platform exclusively for members of School X's book club. To achieve this, I needed to ensure that only students from School X could register using their school email addresses. To solve this problem, I used a basic yet effective 'if' statement in Python to verify if the user is attempting to register with a School X email address or not as shown in the code above. Further, when a user tries to register with an email that is not from School X, I made an error flash pop up message to remind the user that they need to register with a School X email.


### Country Selection
```.html
<label for="country" class="form-label">Country</label>
  <select id="country" name="country" class="form-control">
    <option value="Afghanistan">Afghanistan</option>
    <!-- rest of countries in alphabetical order -->
  </select>
```
As the client's bookclub is part of an international school, I thought it would be a nice addition for the students (users) to add what country they are from. I was able to achieve this by creating a dropdown menu in the registration screen, allowing the user to select their country. At first I had trouble finding a way to list all the countries for a dropdown, until I found a github repository that detailed the steps for a dropdown selection for all countries [13]. I was able to implement the country selection feature by creating an HTML `<label>` element to display the text "Country" and associating it with a `<select>` element. The `<select>` element contains a list of `<option>` elements, each representing a country, and allows users to choose one from the list.

<img width="1512" alt="Screen Shot 2023-05-08 at 10 47 51 PM" src="https://user-images.githubusercontent.com/111751273/236841101-bd249c50-93c6-40aa-8448-896ddb03d9e6.png">


### Country Flag
Following the third meeting with my client, they expressed a desire to enhance the country representation on the web application (See Fig A. 3 in <a href="https://github.com/jonathanye29/unit4_project#evidence-of-consultation">Evidence of Consultation</a> in Appendix). Previously, the user's country was only displayed as text in their profile. I suggested incorporating the country's flag alongside the text for a more visually appealing presentation, and the client was pleased with this idea. This was a challenge for me because it required converting country names to their respective two-letter codes, fetching the appropriate flag images, and seamlessly integrating them into the existing design of the user profiles. However, after doing research, I was able to learn how to utilize the `pycountry` library, which provides a convenient way to access country information [15].

```.py
def flag(country):
    try:
        return pycountry.countries.get(name=country).alpha_2.lower()
    except:
        return 'unknown'
```

As shown in the function above, I used a `try` block to attempt retrieving the two-letter country code using the combination of functions: `pycountry.countries.get(name=country).alpha_2.lower()`. If the provided country name is valid, this method returns the country code in lowercase. However, if the country name is not found within the `pycountry` library, the `try` block encounters an exception. In this case, the `except` block is executed, and the function returns the string `'unknown'` to indicate that the country code could not be determined for the given input. 

After creating the function to convert country names to their respective two-letter codes, I moved on to displaying the flags in the HTML. To achieve this, I utilized an open-source library called `"flag-icons"` by Lipis [16], which provides a collection of country flags in the form of CSS classes. To include this library in the project, I added the following line in the HTML head section:

```.html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/lipis/flag-icons@6.6.6/css/flag-icons.min.css"/>
```

With the flag function created and the "flag-icons" library integrated, I needed to make the function available in the Jinja2 templates used by the Flask application. To achieve this, I registered the flag function as a custom filter in the Jinja2 environment, like so:
```.py
app.jinja_env.filters['flag'] = flag
```
By registering the function as a filter, it became accessible in the Jinja2 templates, allowing me to use it to convert the country names to their respective two-letter codes.

In the HTML template, I then used the following line to display the user's country along with the corresponding flag icon:
```.html
<h6 class="card-subtitle mb-2">Country: <span class="fi fi-{{ user[3] | flag }}"></span> {{ user[3] }}</h6>
```
In this line, the `user[3] | flag` part utilizes the custom `flag` filter to convert the country name stored in `user[3]` from the database to the appropriate two-letter code. This effectively displayed the correct flag next to the country name in the user profile and successfully addressed the client's request for a more visually appealing representation of the user's country.

<img width="986" alt="Screen Shot 2023-05-08 at 10 49 19 PM" src="https://user-images.githubusercontent.com/111751273/236841443-e2df76b1-96f7-42ee-b2ef-ded8e557570a.png">
<p align="center">
  <i>(Disclaimer: The data presented is fictional and does not represent a real student user)</i>
</p>

### Token Encryption
While developing the website for my client, I realized that the website had lacked user authorization. Meaning anyone could access the web application wihtout having to actually register. To solve this I tried using cookies for identification purposes. However, it is essential to make sure that these cookies are protected. Simply assigning a user ID to a session, such as `session['token'] = user_id`, is not a secure practice. This is because a user could easily access their browser's inspector and modify the user ID to gain unauthorized access. Here is an example of an unprotected changeable token:

<img width="1068" alt="Screen Shot 2023-05-08 at 6 03 53 PM" src="https://user-images.githubusercontent.com/111751273/236783651-808e1f23-8904-44fc-861e-00e903b90316.png">

After doing research, I learned about JSON Web Tokens (JWT). JWT is a standard token format that is often used for authentication and authorization purposes [14]. To improve the security of the token, I used JWT to encode the user ID with a token encryption key, as shown in the following example: 
```.py
jwt.encode({'user_id': user_id}, token_encryption_key, algorithm='HS256')`. 
```

This encrypts the token as shown:

<img width="1070" alt="Screen Shot 2023-05-08 at 7 13 15 PM" src="https://user-images.githubusercontent.com/111751273/236798266-d22360f7-8781-48d6-8c00-d02db3a6951a.png">

However, this method still has an issue. If the user's computer is compromised, a hacker could potentially reuse the encrypted cookie to gain unauthorized access. To solve this issue, I implemented tokens set to expire after a specific amount of time after the user logs in, using JWT along with the `dotenv` library for managing the encryption key. This involves adding both the user ID and an expiration date to the token. Here is code I wrote within the login function that sets the token expiration:
```.py
if check_password(user_password=password, hashed_password=hash):
    print("Password correct.")
    token = jwt.encode({'user_id': id, 'exp': datetime.utcnow() + timedelta(minutes=180)}, token_key, algorithm='HS256')
    session['token'] = token
    print("Token created.")
    return redirect("/")
```

As a result, even if an attacker gains access to the token, it will eventually become invalid. 

To ensure that only authorized users can access certain parts of the website, I created a decorator function called `token_required(f)`. This function checks if the user's token is still valid (not expired or tampered with). Here is a snippet of this function:
```.py
if 'token' not in session:
    return redirect(url_for('login'))
try:
    data = jwt.decode(session['token'], token_key, algorithms=['HS256'])
except:
    return redirect(url_for('login'))
```
This function first checks if the 'token' key exists in the session. If not, the user is redirected to the login page. Next, a `try` block attempts to decode the token using `jwt.decode()`. If the token is valid, it will allow the user to proceed within the website that requires authorization, if the token is invalid, expired, or tampered with, the user is redirected to the login page. This solution effectively addresses the authorization issue and enhances the security of the web application. 


### Post Categorization (Success Criteria: 2)
In order to meet my clients need of users being able to post posts of different categories, I implemented the following code to enable users to create a post with a specified category:

```.py
if request.method == 'POST':
  title = request.form['title']
  category = request.form['category']
  content = request.form['content']
  user_id = current_user['user_id']
  create_post = (f"INSERT INTO posts (title, category, content, datetime, image_name, user_id) VALUES ('{title}', '{category}', '{content}', '{datetime.now()}', '{filename}','{user_id}')")
  db.run_save(query=create_post)

  return redirect(url_for('index'))
```
When a user submits a new post, the Flask application receives a POST request containing the post's title, category, content, and any attached image. The `request.form` is used to extract this information, and the user's ID is obtained from the `current_user` dictionary. Next, I constructed a SQL query to insert the new post into the "posts" table in the SQLite database. The query includes the title, category, content, current date and time, filename of the image, and user ID. The `db.run_save()` function is then used to execute the query and save the new post to the database. Finally, the user is redirected back to the index page, where they can see their newly created post. I also followed this method for allowing users to post comments and edit their posts/comments. 

To get the post category shown in the code above from earlier, I implemented a feature that enables users to post posts of categories, such as Announcements, Book Reviews, and Discussions, meeting my clients needs. I was able to do this by using the HTML `select` element and `option` elements for each of the desired categories. I set the `required` attribute on the `select` element to make sure all users select a post category before posting. If no category is selected, the post will not post and a built-in warning message will prompt the user to select their post category. The chosen category is then retrieved from the user's selection and inserted into the database as demonstrated in the earlier code. This can be see from the code shown below:

```.html
<select class="form-select" aria-label="Default select example" name="category" required>
    <option value="" selected disabled>Select Category</option>
    <option value="Announcement">Announcement</option>
    <!-- rest of post categories -->
</select>
```
<img width="1512" alt="Screen Shot 2023-05-08 at 10 49 48 PM" src="https://user-images.githubusercontent.com/111751273/236841551-305958d9-b70d-4682-b678-058f0a419353.png">

### Comment Post Time
As a part of my client's requirements were for users to be able to post comments, I thought it would be nice for the user to see how long ago they had posted their comment. I was able to solve this by implementing a loop that compares the current time with the time the comment was posted. This was accomplished by defining a function, `how_much_time_ago`, that calculates the time difference between the current time and the post's timestamp. Here is a snippet of the function:
```.py
for unit, unit_length in time_units:
  if time_diff.total_seconds() > unit_length:
      num_units = int(time_diff.total_seconds() // unit_length)
      unit = unit if num_units == 1 else unit + 's'  # Handle plural
      return f"{num_units} {unit} ago"
```
This piece of code is a loop that iterates over the defined list `time_units`. Each element of `time_units` consists of a string representation of a time unit ('year', 'month', 'week', 'day', 'hour', 'minute', 'second') and its corresponding length in seconds. The loop checks whether the total seconds of `time_diff` is greater than the current time unit length (I was able to get the current time value by using the Datetime library). If it is, it calculates the number of full units that fit into `time_diff` using integer division `//`. It then checks if the number of units is 1, and if so, it leaves the unit as singular. If not, it adds an 's' to the unit to make it plural. It then returns a string showing the number of units and the time unit itself (like "2 hours ago").

<img width="1281" alt="Screen Shot 2023-05-09 at 5 07 17 PM" src="https://user-images.githubusercontent.com/111751273/237034429-8ea024ba-c34a-4997-9fcb-6442cc6d67d3.png">

### Edit Post/Comment (Success Criteria: 2)
While developing this edit post and comment feature, I followed the steps I took to allow users create posts and comments. I was able to meet my client's needs by just creating a new function and query. Editting a post/comment is basically inserting a "new" post/comment into an already existing post/comment. I followed the exact same steps for editting comments and the only differences were the names of variables. For example, here is a code snippet for editting posts:
```.py
post = db.search(f"SELECT * FROM posts WHERE id = {post_id}")
```
In this code,  I am using the `db.search()` function to query the SQLite database and retrieve a specific post based on its `id` from the "posts" table. 

After the post is located, the owner of the post is redirected to the edit_post page, which is the same as the page shown when they were creating their post, however all the text fields, such as the title, category, content, are already filled out. This allows them to make the desired changes, and after they hit save changes, the database should update with the new edits to their post. Here is the edit query that I created:

```.py
query = f"UPDATE posts SET title='{title}', category='{category}', content='{content}', image_name='{image_name}' WHERE id={post_id}"
db.run_save(query)
```
This is similar to the query from creating posts, however this query uses `UPDATE` and `SET`. 'UPDATE', will update the table "posts", and `SET`, sets the new values into existing post values.

<img width="1000" alt="Screen Shot 2023-05-08 at 10 52 59 PM" src="https://user-images.githubusercontent.com/111751273/236842384-1e2406a2-a6cb-4148-a199-4c9be4f39edf.png">

<img width="1512" alt="Screen Shot 2023-05-08 at 10 55 13 PM" src="https://user-images.githubusercontent.com/111751273/236842947-dfbc1ec1-8083-4e8b-b557-2a99317d4ed9.png">

<img width="993" alt="Screen Shot 2023-05-08 at 10 55 50 PM" src="https://user-images.githubusercontent.com/111751273/236843076-cdd04d00-ac3c-4d12-b8c8-9cb9f6d65af0.png">

### Delete Posts/Comments (Success Criteria: 2)
To also fulfill my client's requirement of being able to delete posts and comment, I created a function that removes chosen posts/comments from the database. Below shows the function that deletes posts. This method is also used to delete comments as well.
```.py
def delete_post(post_id):
    db = database_worker("shelfshare.db")
    delete_post = f"DELETE FROM posts WHERE id = {post_id}"
    db.run_save(query=delete_post)
    return redirect('/profile')
```
Within this function, I first establish a connection to the SQLite database "shelfshare.db" using the database_worker class, which is an example of the Object-Oriented Programming (OOP) technique I use in developing my clients web application. This class handles various database-related tasks of the "shelfshare.db" database such as running queries, saving data, and fetching data. After the connection with the database is established, I created a query that deletes the post that has the 'post_id' as its 'id'. After the post is removed from the database, it redirects the user back to his profile with the post deleted.

<img width="1020" alt="Screen Shot 2023-05-08 at 11 50 14 PM" src="https://user-images.githubusercontent.com/111751273/236856386-d3d56518-8a1b-47d5-aee8-d7f267b9644f.png">

<img width="1010" alt="Screen Shot 2023-05-08 at 11 00 06 PM" src="https://user-images.githubusercontent.com/111751273/236844116-a872f0b8-f304-4726-aa62-be592851c695.png">

        
### Uploading Images (Success Criteria: 3)
One of the challenges I had faced was meeting my clien'ts requirement of allowing users to upload images. I did not know how to do that, so I had to reserach different methods. I was able to solve this by learning to how to use Python's Werkzeug library to implement image uploads [17]. The code snippet below demonstrates how I achieved this:
```.py
if 'image' in request.files:
    image = request.files['image']
    if image.filename != '':
        filename = secure_filename(image.filename)
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    else:
        filename = None
else:
    filename = None
```
The code checks whether an image file was submitted by the user or not. If present, it assigns the image to a variable and verifies that it has a filename. Then, it uses the Werkzeug library's `secure_filename` function to ensure the filename is safe to store, and saves the image in the specified upload folder. If no image is provided or if the image filename is empty, the code sets the filename variable to `None`.

<img width="693" alt="Screen Shot 2023-05-08 at 11 17 42 PM" src="https://user-images.githubusercontent.com/111751273/236848238-b4f156b1-3aca-4908-8b76-412283b6b363.png">
As shown in the image above, the upload folder holds all images that have been uploaded by users. The upload folder not only keeps the server's file structure organized but also allows all users of the website to access and view the uploaded images. By storing the images in a centralized location, the web application can easily serve these images to users when they visit the relevant pages or posts.

### Jinja2 for Past Likes (Success Criteria: 4)
My client wanted users to be able to see posts they had liked in the past. I was able to fulfill my client's need by using Jinja2. Jinja2 is a templating engine for Python that allows me to generate my client's web applications HTML pages. It enables the incorporation of variables, loops, and conditional statements (if statements) directly into HTML templates, allowing me to create pages that display customized content for each user, such as showing a list of posts they have liked in the past. Here is part of the HTML template code I wrote for allowing users to see their past liked posts:
```.html
<h3>Liked Posts:</h3>
  {% if liked_posts %}
      {% for post in liked_posts %}
          <!--all users liked posts-->
      {% endfor %}
      {% else %}
        <div class="card mb-3">
            <div class="card-body">
                <h5 class="card-title mb-1">You have no liked posts</h5>
            </div>
        </div>
  {% endif %}
```
In this HTML template, Jinja2 is used to display the list of thr user's liked posts. The `{% if liked_posts %}` statement checks if there are any liked posts available. If there are, the `{% for post in liked_posts %}` loop goes through each liked post and displays its content within the <!--all users liked posts-->. If there are no liked posts, the `{% else %}` block is executed, displaying a message "You have no liked posts" inside a card element. 

Furthermore, I utilized Jinja2 in a similar manner to display all the posts and comments a user has made on the platform. By iterating through the lists of user posts and comments. This approach satisfies my client's need of allowing users to see their past likes, and on top of that, all their posts and comments.

<img width="700" alt="Screen Shot 2023-05-08 at 11 46 59 PM" src="https://user-images.githubusercontent.com/111751273/236855559-ef19893e-a742-475a-a1c6-fcd4790ade81.png">

### Liking Posts
```.py
if like_record:
    # If the like record exists, delete it (unlike)
    unlike_query = f"DELETE FROM likes WHERE user_id = {user_id} AND post_id = {post_id}"
    db.run_save(query=unlike_query)
    
else:
    # If the like record doesn't exist, create it (like)
    like_query = f"INSERT INTO likes (user_id, post_id) VALUES ('{user_id}', '{post_id}')"
    db.run_save(query=like_query)
```

As a part of the web application, the client wants users to be able to like and unlike posts. To implement this feature, the code I created above checks if a "like" record already exists for a specific user and post combination in the "likes" table of the database.

If a "like" record exists, it means the user has already liked the post, so the code performs an "unlike" action. In this case, the `unlike_query` variable stores an SQL query that removes the existing "like" record from the "likes" table for the given user and post. The `db.run_save()` function is then called to execute the query and update the database.

If a "like" record does not exist, it means the user hasn't liked the post yet, so the code performs a "like" action. Here, the `like_query` variable stores an SQL query that inserts a new "like" record into the "likes" table for the given user and post. The `db.run_save()` function is then called to execute the query and update the database.

This implementation allows users to like and unlike posts, satisfying my client's need.


### View by Category (Success Criteria: 5)
As part of my client's needs, they want the user to be able to select what kind of posts they want to see by category. I was able to satisfy this requirement by implementing a navigation bar at the top of the web applications page at all time that show all categories of posts (Announcements, Reminders, Book Reviews, Book Recommendations, and Discussions). Here is a part of the HTML template code that I wrote for the navigation bar:
```.html
<div class="container-fluid">
  <nav class="navbar navbar-expand-lg navbar-light">
      <a class="navbar-brand" href="/">ShelfShare</a>
      <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
              <li class="nav-item">
                  <a class="nav-link" href="/announcements">Announcements</a>
              </li>
              <!--all other categories-->
          </ul>
      </div>
  </nav>
</div>
```
In this HTML code snippet, a responsive navigation bar is created using classes from Bootstrap's CSS library [12]. The navigation bar contains a brand name "ShelfShare" which serves as a link to the home page. Inside the navigation bar, there is a `<ul>` element containing a list of categories as `<li>` elements, each with an `<a>` element. The `<a>` element inside each list item serves as a link to the respective category page. When a user clicks on one of these links, they are redirected to the corresponding category page. For example, when a user clicks on the "Announcements" link, they are taken to the "/announcements" URL, where all posts in the Announcements category are displayed. This fulfills my client's requirement of allowing users to select what kind of posts they would like to view by category.


### Sort Feature (Success Criteria: 6)
Another challenge I came across while developing my client's web application was implementing the sorting feature that sorts posts by latest and top liked. To overcome this challenge, I discovered Document Object Model (DOM) manipulation techniques in JavaScript that enabled me to interact with the HTML elements on the page [18].

First, I used an SQL query to fetch the most liked posts:
```.sql
SELECT posts.*, users.name FROM posts INNER JOIN users ON posts.user_id = users.id WHERE posts.id IN (SELECT post_id FROM likes GROUP BY post_id ORDER BY COUNT(*) DESC)
```
In the SQL query shown above, I used `INNER JOIN` to combine data from the posts and users tables, ensuring that the author's name is retrieved along with the post information. Then I filtered the posts based on their like count using a subquery. This subquery gets the `post_id` from the "likes" table, groups them by post ID, and sorts by like count in descending order. The `IN` operator in the `WHERE` clause filters the posts with the IDs from the subquery, displaying only the top liked posts.

```.html
<label for="sort">Sort Posts By:</label>
    <select class="form-control mb-1" id="sort">
        <option value="latest" selected>Latest</option>
        <option value="popular">Top Liked</option>
    </select>
```
The code snippet shown above creates a dropdown menu using HTML elements. The `<label>` element assigns a descriptive label, "Sort Posts By:", for the dropdown menu. The `<select>` element with the `class="form-control mb-1"` and `id="sort"` attributes creates the actual dropdown menu, styled with Bootstrap classes. Inside the `<select>` element, there are two `<option>` elements, each representing a sorting choice for the user:
1. `<option value="latest" selected>`: This option sorts posts by the latest ones first. The `selected` attribute makes it the default selection when the page loads.
2. `<option value="popular">`: This option sorts posts by the top liked ones.

When the user selects an option, its `value` attribute will be used by JavaScript to determine the sorting method to apply. I utilized JavaScript and DOM manipulation to detect when the user changes the selection in the dropdown menu. When a change occurs, the script executes the appropriate action, such as redirecting the user to a different page that displays the posts sorted based on the selected option. This way, the sorting preferences selected by the user are applied seamlessly without having to reload the entire page. Here is the script:
```.html
<script>
    const sortSelect = document.querySelector('#sort');
    sortSelect.addEventListener('change', function() {
        const value = this.value;
        if (value === 'popular') {
            window.location.href = '/top_liked';
        }
    });
</script>
```
The script first uses `document.querySelector('#sort')` to select the dropdown menu with the `id` "sort". It then assigns this HTML element to the constant variable `sortSelect`. Next, an event listener is added to `sortSelect` to listen for the 'change' event, which occurs when the user selects a different option from the dropdown menu. When the 'change' event is detected, an anonymous function is executed. Inside this function, the `value` property of the selected option is assigned to the constant variable `value`. A conditional statement then checks if `value` is equal to 'popular', which corresponds to the "Top Liked" option. If this condition is met, the script uses `window.location.href` to navigate the user to the '/top_liked' URL, where the posts are sorted according to the number of likes they have received.

Through this method, I was able to successfully meet my client's requirement of having a sorting feature in the web application.

# Criteria D: Functionality
## Video of Web Application Functionality
https://github.com/jonathanye29/unit4_project/assets/111751273/bc04e8a2-4f23-480b-a19e-ff9e2e77ac97

<a href="https://youtu.be/2mcj87IsiNs">Link to the video on YouTube with captions</a>

# Criteria E: Evaluation
## Evaluation by Client
| Success Criteria   | Met? | Description          |
|---------------------------------------------------------------|------|------------------------------------------------------------|
| The platform allows only students from School X to register using their school emails. | Yes  | The registration process of the web application validates emails based on the school domain, ensuring only students can register.    |
| Users should be able to post posts of different categories such as: Announcements, Book Reviews, and Discussions, and be able to edit/delete their posts and comments. | Yes  | Users have the ability to post, edit, and delete any of their own posts and comments|
| The platform will allow users to upload images in their posts.   | Yes  | There is an image upload feature incorporated in the create post feature of the web application, allowing users to add visual features to their posts |
| Users will be able to see all posts they have liked in the past. | Yes  | The web application allows users to see all posts they have liked before in their profile page. |
| The platform will allow the user to select what kind of posts they would like to view by category.   | Yes  | The platform's navigation bar allows users to view posts by category, making it easier to locate specifc posts. |
| Implement a filtering feature that allows users to view the top liked posts.  | Yes  | The web application has a filter feature that allows posts to be sorted by 'Top Liked', allowing users to easily discover the most popular content. In addition, the web application by default sorts all posts by the 'Latest'. |

The client expresses high satisfaction with the developed web application, expressing that it effectively addresses all the outlined success criteria (see Fig A. 4 in <a href="https://github.com/jonathanye29/unit4_project#evidence-of-consultation"> Evidence of Consultation</a> in Appendix). During the evaluation, the client offered valuable feedback like suggesting the addition of visible like counts on each post to provide more immediate feedback to the user community. Having the amount of likes shown can allow users to see the difference in the amounts of likes each post has.

## Evaluation by Peer
My peer reviewer gave positive feedback on the web application (see Fig A. 5 in <a href="https://github.com/jonathanye29/unit4_project#evidence-of-consultation"> Evidence of Consultation</a> in Appendix), affirming that it successfully meets all the success criteria. They especially appreciated the categorization feature and the user's ability to filter posts by their likes. However, they suggested a potential enhancement in the form of more robust sorting options. Instead of limiting to the most liked and latest posts, the inclusion of additional sorting features such as least liked and oldest posts could provide users with a more comprehensive and nuanced browsing experience. This feedback will be invaluable in further refining the functionality and user experience of the web application.

## Recommendations
### Recommendation 1: Display Like Counts on Posts
The client suggested that displaying the number of likes each post has received would be a valuable addition to the platform (see Fig A. 4 in <a href="https://github.com/jonathanye29/unit4_project#evidence-of-consultation"> Evidence of Consultation</a> in Appendix). Displaying the like count on each post can greatly enhance the user experience and the overall sense of community on the platform. It introduces a more immediate and transparent form of user engagement, allowing users to see how their content is received by their peers in real time.

Furthermore, it also introduces a form of social proofing, where posts with higher like counts may encourage other users to engage with the content, fostering a more active discussion and interaction within the platform. It can also incentivize users to post higher quality content, knowing that their posts are being actively liked and acknowledged by their peers.

On a more practical note, the like count can serve as a quick reference for users to determine which posts are trending or most relevant within the community at any given time, thus aiding in navigation and discovery of content on the platform.

To implement this feature, an update to the HTML template and the database query used to retrieve post information can be made. The query should include the like count, and the HTML template should be adjusted to display this information alongside each post.

### Recommendation 2: Expand Sorting Options
The peer reviewer suggested incorporating more robust sorting options in addition to the existing "most liked" and "latest" filters (see Fig A. 5 in <a href="https://github.com/jonathanye29/unit4_project#evidence-of-consultation"> Evidence of Consultation</a> in Appendix). Expanding the sorting options available to users can significantly enhance their ability to navigate and discover content that is most relevant to their interests. By adding options such as "least liked" and "oldest", users gain more control and flexibility over their browsing experience, allowing them to engage with the platform in a way that best suits their preferences.

For instance, a "least liked" option may bring to light posts that have been overlooked or underappreciated, encouraging a more diverse range of discussions. On the other hand, an "oldest" option could be useful for users wanting to explore the history of discussions within the book club, or for finding older posts that they wish to revisit. Moreover, providing a variety of sorting options encourages repeated engagement, as users can choose to explore the platform's content in different ways each time they visit the web application. 

Implementing this recommendation would involve extending the existing dropdown menu in the HTML template to include these new sorting options. On the server side, the application would need to handle these additional sorting methods, adjusting the SQL query used to retrieve posts based on the user's selected sorting method.

# Works cited
1. “Trending Dreams | Deep Dream Generator.” Deepdreamgenerator.com, 2023, deepdreamgenerator.com/. Accessed 2 Apr. 2023.
2. Grinberg, Miguel. “The Flask Mega-Tutorial Part I: Hello, World!” Miguelgrinberg.com, 2017, blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world. Accessed 3 Apr. 2023.
3. “HTML Tutorial.” W3schools.com, 2023, www.w3schools.com/html/default.asp. Accessed 3 Apr. 2023.
4. Sanyal, Sayantani. 10 Reasons Why Python Is One Of The Best Programming Languages. Accessed 7 Apr. 2023
5. “Flask.” Fullstackpython.com, 2016, www.fullstackpython.com/flask.html. Accessed 7 Apr. 2023.
6. “Advantages and Disadvantages of HTML.” GeeksforGeeks, GeeksforGeeks, 25 Oct. 2020, www.geeksforgeeks.org/advantages-and-disadvanatges-of-html/. Accessed 10 April 2023.
7. Cyber Success. “What Is Bootstrap & Advantages of Bootstrap in Web Development.” Cyber Success, 24 Oct. 2021, www.cybersuccess.biz/advantages-of-bootstrap/. Accessed 10 April 2023.
8. Advantages and disadvantages of python - how it is dominating Programming World. DataFlair. Accessed April 10, 2023
9. Simplilearn. “Django vs. Flask: Understanding the Major Differences.” Simplilearn.com, Simplilearn, 4 Feb. 2021, www.simplilearn.com/flask-vs-django-article. Accessed 10 April 2023.
10. Gomathy, Kavya. "5 Reasons to Use SQLite, the Tiny Giant for Your Next Project." Medium, The Startup, 4 Jan. 2022, https://medium.com/swlh/5-reasons-to-use-sqlite-the-tiny-giant-for-your-next-project-a6bc384b2df4. Accessed April 10, 2023
11. Yegulalp, Serdar. "Why You Should Use SQLite." InfoWorld, IDG Communications, Inc., 13 Feb. 2019, https://www.infoworld.com/article/3331923/why-you-should-use-sqlite.html. Accessed April 10, 2023
12. Otto, Mark. “Get Started with Bootstrap.” Getbootstrap.com, 2023, getbootstrap.com/docs/5.3/getting-started/introduction/. Accessed 15 Apr. 2023.
13. 262588213843476. “HTML Country Select Dropdown List.” Gist, 3 May 2023, gist.github.com/danrovito/977bcb97c9c2dfd3398a. Accessed 20 Apr. 2023.
14. auth0.com. “JSON Web Tokens - Jwt.io.” Jwt.io, Auth0, 2013, jwt.io/introduction. Accessed April 22 2023.
15. “Pycountry.” PyPI, 5 Mar. 2022, pypi.org/project/pycountry/. Accessed 8 May 2023.
16. lipis. “Lipis/Flag-Icons: A Curated Collection of All Country Flags in SVG — plus the CSS for Easier Integration.” GitHub, 28 Mar. 2023, github.com/lipis/flag-icons. Accessed 25 Apr. 2023.
17. Soumitra. “Upload and Display Image Using Python Flask - Roy Tutorials.” Roy Tutorials, 13 Apr. 2020, roytuts.com/upload-and-display-image-using-python-flask/. Accessed 29 Apr. 2023.
18. “Examples of Web and XML Development Using the DOM - Web APIs | MDN.” Mozilla.org, 20 Feb. 2023, developer.mozilla.org/en US/docs/Web/API/Document_Object_Model/Examples. Accessed 1 May 2023.
19. knookie. “How to Add a Browser Tab Icon (Favicon) for a Website?” Stack Overflow, 3 Feb. 2011, stackoverflow.com/questions/4888377/how-to-add-a-browser-tab-icon-favicon-for-a-website. Accessed 9 May 2023.


# Appendix
## Evidence of Consultation
![Screen Shot 2023-05-06 at 8 46 37 PM](https://user-images.githubusercontent.com/111751273/236622106-71c778b6-838a-4e12-ac89-4bdc96d31c0d.png)
<i>Fig A. 1</i> Conversation between two club members (Disclaimer: Messenger names kept confidential for privacy purposes)

<img width="1037" alt="Screen Shot 2023-05-09 at 4 40 35 AM" src="https://user-images.githubusercontent.com/111751273/236918166-e0088101-a6cd-45cf-93af-acf55654d178.png">
<i>Fig A. 2</i> Client's approval of all success criteria and development plan after meeting.(Disclaimer: Mailer and recipient names kept confidential for privacy purposes)

<img width="1158" alt="Screen Shot 2023-05-09 at 5 01 43 AM" src="https://user-images.githubusercontent.com/111751273/236922415-1f344990-3e15-47ac-a345-2d27f86c7706.png">
<i>Fig A. 3</i> Client's approval of all the current state of the web applications development after meeting. (Disclaimer: Mailer and recipient names kept confidential for privacy purposes)

<img width="1176" alt="Screen Shot 2023-05-09 at 7 14 27 PM" src="https://github.com/jonathanye29/unit4_project/assets/111751273/92a8bf42-a1d6-4436-ab96-125eb579c9a1">
<i>Fig A. 4</i> Client evaluation of the web application (Disclaimer: Mailer and recipient names kept confidential for privacy purposes)</i>

<img width="1173" alt="Screen Shot 2023-05-09 at 8 26 44 PM" src="https://github.com/jonathanye29/unit4_project/assets/111751273/b34adf1b-e914-4334-8db4-9bb679d508a6">
<i>Fig A. 5</i> Peer evaluation of the web application (Disclaimer: Mailer and recipient names kept confidential for privacy purposes)

