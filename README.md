# ShelfShare: A Book Sharing Social Network
<img src="https://user-images.githubusercontent.com/111751273/230335373-2b5f43b8-14be-4786-aeac-73b739196a62.jpg" width="100%">

<i>Fig. 1</i> Using the prompt 'Generate a picture of a cozy reading nook with a bookshelf filled with books and a comfortable armchair in warm and inviting colors.' This image was generated using AI on Deep Dream Generator.[1]

# Criteria A: Planning

## Problem Definition
As a member of School X's book club, I have noticed a lack of a dedicated social network for our book club community. While existing platforms such as Goodreads allow readers to connect worldwide, they do not provide a focused space for book club members within our school community to connect, share book reviews and recommendations, opinions/comments, discussions, and even post about special events such as book fairs and meeting reminders. Further, Goodreads doesn’t allow users to upload any image they wish, and users are also not able to edit/delete their posts or comments if they make a mistake. Through consultations with fellow book club members (see <a href="https://github.com/jonathanye29/unit4_project#evidence-of-consultation">Evidence of Consultation</a> in Appendix), it has become clear that a dedicated social network for book enthusiasts within our school community would be highly beneficial. Further, communication and sharing of book club events and discussions are scattered across multiple platforms such as Messenger, Facebook, and Email. This lack of a centralized platform makes it difficult to keep track of book club events, discussions, and announcements in one place. Further, finding different post categories is hard because there are so many types.


## Success Criteria
1. [Issue tackled: “lack of a dedicated social network for our book club community”] The platform allows only students from School X to register using their school emails.
2.  [Issue tackled: “they do not provide a focused space for book club members within our school community to connect, share book reviews and recommendations, opinions/comments, discussions, and even post about special events such as book fairs and meeting reminders. Users are also not able to edit/delete their posts or comments if they make a mistake.”] 
   - Users should be able to post posts of different categories such as: Announcements, Reminders,  Book Recommendations/Reviews, and Discussions
   - Users should be able to edit/delete their posts and comments
4. [Issue tackled: "communication and sharing of book club events and discussions are scattered across multiple platforms."] The platform should centralize all book club events, discussions, and announcements in one location. 
5.  [Issue tackled: ] 
6.  [Issue: tackled: “finding different post categories is hard because there are so many types”] The platform will allow the user to select what kind of posts they would like to view by category.
7. [Issue tackled: “doesn’t allow users to upload any image they wish”] The platform will allow users to upload any images they wish.


## Design Statement
I will design and develop a website for my school’s book club. This website will be developed using Python, HTML, CSS, SQLite, and the Flask framework. It will take approximately 3 weeks to develop and will be evaluated based on the given criteria.


## Rationale for Proposed Solution
There are two types of applications: web applications and mobile applications. Mobile applications can only be accessed through mobile devices, which limits the number of users who can access them. On the other hand, web applications can be accessed through any electronic device with a browser. Therefore, developing a web application would bring together all the necessary features in one place for the book club community to connect and engage with each other.

I decided to use HTML to develop the website as it is the standard markup language for creating web pages and web applications. HTML provides a simple and accessible foundation for building the user interface of the social network. This ensures that the platform will be compatible with various devices and browsers, allowing a wide range of users to access the application.


# Criteria B: Design
## System Diagram
## Wireframe
## Flow Diagram
## ER Diagram
![u4projectERdiagram](https://user-images.githubusercontent.com/111751273/230445149-14e32559-9299-4315-9ded-ff4e93d05c85.jpg)
<i>Fig. /i> Entity-Relationship (ER) diagram for ShelfShare's network database, illustrating the relationships between the Users, Posts, Reviews, and Comments tables. The diagram displays one-to-many relationships using lines starting with '1' and ending with 'N', indicating the cardinality of each relationship. For example, 1 user can have many (n) posts.

<img width="max" alt="Screen Shot 2023-04-07 at 9 29 08 PM" src="https://user-images.githubusercontent.com/111751273/230608928-1915bb1c-8f24-48cd-8241-b3e5be2a96ca.png">

<p align="center">
  <i>Fig. </i> Example Data in Users Table (Note: All information is fake and does not represent real individuals or their personal information)
</p>

<img width="max" alt="Screen Shot 2023-04-07 at 9 28 29 PM" src="https://user-images.githubusercontent.com/111751273/230608878-771dffd3-547a-4f55-9873-fd01c84caaae.png">

<p align="center">
  <i>Fig. </i> Example Data in Posts Table (Note: All information is fake and does not represent real posts or their authors)
</p>

<img width="max" alt="Screen Shot 2023-04-07 at 9 29 29 PM" src="https://user-images.githubusercontent.com/111751273/230608970-0458ea2a-c1e5-49e7-91f8-b46e0da26267.png">

<p align="center">
  <i>Fig. </i> Example Data in Reviews Table (Note: All information is fake and does not represent real reviews or their authors)
</p>
 
<img width="max" alt="Screen Shot 2023-04-07 at 9 29 45 PM" src="https://user-images.githubusercontent.com/111751273/230608999-5e2bdd27-2d98-4099-9478-aab25af60ec6.png">

<p align="center">
  <i>Fig. </i> Example Data in Comments Table (Note: All information is fake and does not represent real comments or their authors)
</p>

## UML Diagram
## Test plan
## Record of Tasks

# Criteria C: Development
## Existing tools
## List of techniques used
## Development

# Criteria D: Functionality


# Works cited
1. “Trending Dreams | Deep Dream Generator.” Deepdreamgenerator.com, 2023, deepdreamgenerator.com/. Accessed 2 Apr. 2023.
2. Grinberg, Miguel. “The Flask Mega-Tutorial Part I: Hello, World!” Miguelgrinberg.com, 2017, blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world. Accessed 3 Apr. 2023.
3. “HTML Tutorial.” W3schools.com, 2023, www.w3schools.com/html/default.asp. Accessed 3 Apr. 2023.
4. Sanyal, Sayantani. 10 Reasons Why Python Is One Of The Best Programming Languages. Accessed 7 Apr. 2023
5. “Flask.” Fullstackpython.com, 2016, www.fullstackpython.com/flask.html. Accessed 7 Apr. 2023.
6. Otto, Mark. “Get Started with Bootstrap.” Getbootstrap.com, 2023, getbootstrap.com/docs/5.3/getting-started/introduction/. Accessed 26 Apr. 2023.
7. lipis. “Lipis/Flag-Icons: A Curated Collection of All Country Flags in SVG — plus the CSS for Easier Integration.” GitHub, 28 Mar. 2023, github.com/lipis/flag-icons. Accessed 23 Apr. 2023.
8. 
9.  
10.
‌11.


# Appendix

## Evidence of Consultation
<img width="1007" alt="u4evidenceforconsultation" src="https://user-images.githubusercontent.com/111751273/230599929-1bf1a0f9-bf56-4adb-8be4-03b5b2566a31.png">


